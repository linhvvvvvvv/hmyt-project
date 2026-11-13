import argparse
import csv
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix, ConfusionMatrixDisplay,
                             roc_auc_score, average_precision_score, precision_recall_fscore_support)
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='FAERS_2025_65plus_ML.csv', help='Duong dan den CSV ML')
parser.add_argument('--output', default='BASELINE_KET_QUA', help='Thu muc ket qua')
args = parser.parse_args()
source = Path(args.input)
if not source.exists():
    raise SystemExit(f'Khong thay CSV: {source.resolve()}\nHay dat CSV cung thu muc voi file .py, hoac dung --input "DUONG_DAN"')
out = Path(args.output); out.mkdir(parents=True, exist_ok=True)

cols = ['primaryid','caseid','caseversion','age_years','sex','n_unique_meds','fall_reported']
df = pd.read_csv(source, usecols=cols, dtype={'primaryid':'string','caseid':'string','sex':'string'}, low_memory=False)
for name in ('age_years','n_unique_meds','fall_reported','caseversion'):
    df[name] = pd.to_numeric(df[name], errors='coerce')
df = df[df['fall_reported'].isin([0,1]) & df['caseid'].notna()].copy()
# Neu 1 case co nhieu phien ban: chon phien ban cao nhat, de 1 dong / case.
df = df.sort_values(['caseid','caseversion'], na_position='first').drop_duplicates('caseid', keep='last')
df = df[df['age_years'].isna() | df['age_years'].between(65,115)].copy()
df['sex'] = df['sex'].fillna('UNKNOWN').astype(str).str.upper().str.strip()
df.loc[~df['sex'].isin(['F','M']), 'sex'] = 'UNKNOWN'
X = df[['age_years','sex','n_unique_meds']]
y = df['fall_reported'].astype(int)
if len(df) < 100 or y.nunique()<2:
    raise SystemExit('Dataset khong du ho so hoac chi co mot nhan.')
# Group-aware split: caseid khong the bi chia sang hai tap.
train_idx, test_idx = next(GroupShuffleSplit(n_splits=1,test_size=.2,random_state=42).split(X,y,groups=df['caseid']))
X_train,X_test = X.iloc[train_idx],X.iloc[test_idx]
y_train,y_test = y.iloc[train_idx],y.iloc[test_idx]
if y_train.nunique()<2 or y_test.nunique()<2:raise SystemExit('Thieu lop duong tinh o train/test; can dieu chinh split.')
pre = ColumnTransformer([
 ('numeric', Pipeline([('missing',SimpleImputer(strategy='median')),('scale',StandardScaler())]), ['age_years','n_unique_meds']),
 ('categorical', OneHotEncoder(handle_unknown='ignore'), ['sex'])
])
model = Pipeline([('prep',pre),('clf',LogisticRegression(max_iter=1000,class_weight='balanced',random_state=42))])
model.fit(X_train,y_train)
probs=model.predict_proba(X_test)[:,1]
preds=(probs>=0.5).astype(int)
report=classification_report(y_test,preds,zero_division=0)
auc=roc_auc_score(y_test,probs)
ap=average_precision_score(y_test,probs)
cm=confusion_matrix(y_test,preds,labels=[0,1])
with (out/'bao_cao_baseline.txt').open('w',encoding='utf-8') as f:
 f.write('FAERS 2025 - Baseline Logistic Regression\n')
 f.write('Dinh nghia nhan: bao cao co FALL / khong bao cao FALL, KHONG phai nguy co te nga lam sang.\n')
 f.write('Features: age_years, sex, n_unique_meds; bo ACB va DDI (chua tinh).\n')
 f.write('Tach 80/20 theo caseid; neu case trung phien ban, giu caseversion cao nhat.\n')
 f.write('Can kiem tra nhan va phuong phap xu ly duplicate truoc khi cong bo khoa hoc.\n\n')
 f.write(f'Tong case: {len(df):,}\nTrain: {len(train_idx):,}\nTest: {len(test_idx):,}\n')
 f.write(f'FALL=1 overall: {int(y.sum()):,} ({y.mean():.2%})\n')
 f.write(f'FALL=1 test: {int(y_test.sum()):,} ({y_test.mean():.2%})\n')
 f.write(f'ROC-AUC: {auc:.4f}\nAverage precision (PR-AUC summary/AP): {ap:.4f}\n')
 f.write(f'Test prevalence (AP random baseline): {y_test.mean():.4f}\n\n')
 f.write(report+'\nConfusion matrix [0,1]:\n'+str(cm)+'\n')
pd.DataFrame({'caseid':df.iloc[test_idx]['caseid'].to_numpy(), 'y_true':y_test.to_numpy(), 'prob_fall_reported':probs, 'y_pred_0_5':preds}).to_csv(out/'du_doan_test.csv',index=False,encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(5,4));ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=['No FALL report','FALL report']).plot(ax=ax,colorbar=False,cmap='Blues');fig.tight_layout();fig.savefig(out/'confusion_matrix.png',dpi=170);plt.close(fig)
print('\nHOAN THANH BASELINE!')
print(f'Case: {len(df):,} | FALL: {int(y.sum()):,} | Test: {len(test_idx):,}')
print(f'ROC-AUC: {auc:.4f} | Average Precision: {ap:.4f}')
print(report)
print('Ket qua o:',out.resolve())
