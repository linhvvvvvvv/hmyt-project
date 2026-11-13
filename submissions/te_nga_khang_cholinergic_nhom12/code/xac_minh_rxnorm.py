import argparse, csv, json, time, urllib.parse, urllib.request
from pathlib import Path

BASE = 'https://rxnav.nlm.nih.gov/REST'
INPUT_DEFAULT = '02_DANH_MUC_HOAT_CHAT_CAN_XAC_MINH.csv'
OUT = Path('RXNORM_KET_QUA')
FIELDS = ['ingredient_provisional','so_luot_xuat_hien','vi_du_ten_thuoc','nguon_ban_dau',
          'ingredient_verified','rxnorm_rxcui','mapping_status','ACB_2012','ACB_source',
          'rxnorm_query','rxnorm_notes']

def api(path, params=None):
    url = BASE + path + ('?' + urllib.parse.urlencode(params) if params else '')
    request = urllib.request.Request(url, headers={'User-Agent': 'FAERS-ACB-research/1.0 (academic mapping)'})
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.load(response)

def find_ids(name):
    d = api('/rxcui.json', {'name':name,'search':'2'})
    return list(dict.fromkeys(d.get('idGroup',{}).get('rxnormId',[]) or []))

def ingredients(rxcui):
    prop = api('/rxcui/'+rxcui+'/properties.json').get('properties',{})
    tty = prop.get('tty','')
    if tty == 'IN':
        return [(rxcui, prop.get('name',''))], tty
    # PIN = precise ingredient (salt/form), must relate to base IN if possible.
    d = api('/rxcui/'+rxcui+'/related.json', {'tty':'IN'})
    vals=[]
    for group in d.get('relatedGroup',{}).get('conceptGroup',[]) or []:
        if group.get('tty')=='IN':
            for c in group.get('conceptProperties',[]) or []:
                vals.append((c.get('rxcui',''),c.get('name','')))
    vals=list(dict.fromkeys((i,n) for i,n in vals if i and n))
    return vals, tty

def resolve(name):
    try:
        ids=find_ids(name)
        if not ids:
            return '', '', 'NO_RXNORM_MATCH', 'Không tìm thấy khớp exact/normalized'
        hits=[]; types=[]
        for rid in ids[:6]:
            ing,ty=ingredients(rid)
            types.append(ty)
            hits.append((rid, tuple(sorted(set(ing)))))
        if len(ids)>6:
            return '', '|'.join(ids), 'REVIEW_MULTIPLE_RXCUI', 'Có hơn 6 mã khớp'
        unique={h[1] for h in hits if h[1]}
        if len(unique)!=1:
            return '', '|'.join(ids), 'REVIEW_AMBIGUOUS', 'Có nhiều khớp/không có hoạt chất rõ: '+','.join(types)
        ing=next(iter(unique))
        if len(ing)!=1:
            return ' | '.join(n for _,n in ing), '|'.join(ids), 'REVIEW_COMBINATION', 'Nhiều hoạt chất: kiểm tra thuốc phối hợp'
        if any(t in ('BN','SBD','SCD','BPCK','GPCK') for t in types):
            # Ingredient obtained from drug/brand relation, keep for review instead of automatically accepting.
            return ing[0][1], '|'.join(ids), 'REVIEW_BRAND_OR_PRODUCT', 'Kiểm tra tên thương mại/sản phẩm'
        return ing[0][1], '|'.join(ids), 'RXNORM_MAPPED', 'Khớp exact/normalized; cần rà soát QC'
    except Exception as e:
        return '', '', 'API_ERROR', str(e)[:170]

def main():
    parser=argparse.ArgumentParser(description='Xác minh tên thuốc FAERS với RxNorm, không tự chấm ACB')
    parser.add_argument('csv_file', nargs='?', default=INPUT_DEFAULT)
    parser.add_argument('--limit',type=int,default=300,help='Số tên mới xử lý mỗi lần (mặc định 300)')
    parser.add_argument('--delay',type=float,default=.25,help='Khoảng nghỉ giữa các lượt (giây)')
    args=parser.parse_args()
    OUT.mkdir(exist_ok=True)
    source=Path(args.csv_file)
    if not source.exists():
        print('KHÔNG THẤY FILE:',source); return
    with source.open(encoding='utf-8-sig',newline='') as f:
        original=list(csv.DictReader(f))
    cachefile=OUT/'rxnorm_cache.csv'
    cache={}
    if cachefile.exists():
        with cachefile.open(encoding='utf-8-sig',newline='') as f:
            cache={x['ingredient_provisional'].strip().upper(): x for x in csv.DictReader(f)}
    new=0
    with cachefile.open('a',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS)
        if f.tell()==0:w.writeheader()
        for row in original:
            name=row['ingredient_provisional'].strip()
            if not name or name.upper() in cache: continue
            if new>=args.limit:break
            mapped,rxcui,status,note=resolve(name)
            record={c:row.get(c,'') for c in FIELDS}
            record.update(ingredient_verified=mapped,rxnorm_rxcui=rxcui,
                          mapping_status=status, rxnorm_query=name, rxnorm_notes=note,
                          ACB_2012='', ACB_source='')
            w.writerow(record); f.flush(); cache[name.upper()]=record
            new+=1
            if new%25==0:print(f'Đã tra thêm {new} tên | gần nhất: {name} -> {status}', flush=True)
            time.sleep(args.delay)
    merged=[]
    for row in original:
        key=row['ingredient_provisional'].strip().upper()
        obj={c:row.get(c,'') for c in FIELDS}
        if key in cache:obj.update(cache[key])
        merged.append(obj)
    for filename,rows in [
       ('01_KET_QUA_DANH_MUC.csv',merged),
       ('02_CAN_KIEM_TRA.csv',[x for x in merged if x['mapping_status'] != 'RXNORM_MAPPED']),
       ('03_DA_KHOP_RXNORM.csv',[x for x in merged if x['mapping_status']=='RXNORM_MAPPED'])]:
        with (OUT/filename).open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
    print('\nXONG LƯỢT NÀY! Mới tra:',new,'| Tổng đã tra:',len(cache),'/',len(original))
    print('Đọc các CSV trong:',OUT.resolve())
    print('Lưu ý: Chưa có điểm ACB; chưa chuẩn hóa hoàn tất các tên cần review.')

if __name__=='__main__':main()
