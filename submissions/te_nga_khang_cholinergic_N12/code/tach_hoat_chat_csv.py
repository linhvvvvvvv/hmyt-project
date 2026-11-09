
import csv
import sqlite3
import sys
import re
from pathlib import Path

INPUT = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path('FAERS_2025_65plus_medications.csv').resolve()
if not INPUT.is_file():
    sys.exit(f'KHONG TIM THAY FILE: {INPUT}')
OUT = INPUT.parent / 'KET_QUA_TACH_THUOC'
OUT.mkdir(exist_ok=True)

def normalize(text):
    return re.sub(r'\s+', ' ', (text or '').strip()).upper()

conn = sqlite3.connect(str(OUT / 'tam_thong_ke.sqlite'))
conn.execute('PRAGMA journal_mode=WAL')
conn.execute('CREATE TABLE IF NOT EXISTS catalog (ingredient TEXT PRIMARY KEY, records INTEGER NOT NULL DEFAULT 0, example_drug TEXT, source TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS case_ingredients (primaryid TEXT, caseid TEXT, ingredient TEXT, PRIMARY KEY (primaryid, ingredient)) WITHOUT ROWID')

headers = ['primaryid','caseid','report_quarter','drug_seq','role_cod','drugname_reported','prod_ai_reported','ingredient_provisional','source','status']
processed = 0
expanded = 0
missing = 0
with INPUT.open('r', encoding='utf-8-sig', newline='', errors='replace') as inf, \
     (OUT / '01_MOI_DONG_THUOC_TACH_HOAT_CHAT.csv').open('w', encoding='utf-8-sig', newline='') as fo, \
     (OUT / '03_CHUA_RO_HOAT_CHAT.csv').open('w', encoding='utf-8-sig', newline='') as fm:
    reader = csv.DictReader(inf)
    needed = {'primaryid','caseid','drugname_reported','prod_ai_reported'}
    absent = needed - set(reader.fieldnames or [])
    if absent:
        sys.exit(f'FILE THIEU COT: {sorted(absent)}. Can dung medications.csv GOC.')
    writer = csv.DictWriter(fo, fieldnames=headers)
    writer.writeheader()
    bad_writer = csv.DictWriter(fm, fieldnames=headers)
    bad_writer.writeheader()
    for row in reader:
        processed += 1
        raw = normalize(row.get('prod_ai_reported'))
        name = normalize(row.get('drugname_reported'))
        if raw:
            parts = [normalize(x) for x in raw.split('\\') if normalize(x)]
            source = 'PROD_AI'
            status = 'NEED_VERIFICATION'
        else:
            # Fallback is NOT necessarily an ingredient; do not score it automatically.
            parts = [name] if name else ['']
            source = 'DRUGNAME_FALLBACK'
            status = 'REVIEW_NAME_ONLY'
        # Remove duplicate components in a single drug record, preserve order
        parts = list(dict.fromkeys(parts))
        for part in parts:
            data = {k: row.get(k,'') for k in headers if k in row}
            data.update(ingredient_provisional=part,source=source,status=status)
            writer.writerow(data)
            expanded += 1
            if status != 'NEED_VERIFICATION' or not part:
                bad_writer.writerow(data)
                missing += 1
            if part:
                conn.execute('INSERT INTO catalog(ingredient, records, example_drug, source) VALUES (?, 1, ?, ?) ON CONFLICT(ingredient) DO UPDATE SET records = records + 1', (part, name, source))
                conn.execute('INSERT OR IGNORE INTO case_ingredients(primaryid, caseid, ingredient) VALUES (?, ?, ?)', (row.get('primaryid',''), row.get('caseid',''), part))
        if processed % 50000 == 0:
            conn.commit()
            print(f'Da doc {processed:,} dong; tach {expanded:,} luot thanh phan...', flush=True)
    conn.commit()

with (OUT/'02_DANH_MUC_HOAT_CHAT_CAN_XAC_MINH.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f)
    w.writerow(['ingredient_provisional','so_luot_xuat_hien','vi_du_ten_thuoc','nguon_ban_dau','ingredient_verified','rxnorm_rxcui','mapping_status','ACB_2012','ACB_source'])
    for ing, count, example, src in conn.execute('SELECT ingredient,records,example_drug,source FROM catalog ORDER BY records DESC'):
        w.writerow([ing,count,example,src,'','','NEED_RXNORM_VERIFICATION' if src == 'PROD_AI' else 'REVIEW_NAME_ONLY','',''])

with (OUT/'04_MOI_HO_SO_MOI_HOAT_CHAT_KHONG_TRUNG.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f)
    w.writerow(['primaryid','caseid','ingredient_provisional'])
    for r in conn.execute('SELECT primaryid,caseid,ingredient FROM case_ingredients ORDER BY primaryid,ingredient'):
        w.writerow(r)

n_ingredients=conn.execute('SELECT COUNT(*) FROM catalog').fetchone()[0]
print(f'HOAN THANH: {processed:,} dong thuoc, {expanded:,} luot hoat chat, {n_ingredients:,} ten so bo, {missing:,} dong can xem ten thuoc.')
print('THU MUC KET QUA:', OUT)
conn.close()
