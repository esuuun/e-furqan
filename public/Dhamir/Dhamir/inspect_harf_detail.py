import openpyxl
import json
import os
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

wb = openpyxl.load_workbook('KAMUS Harf Ghair Amil.xlsx', data_only=True)
ws = wb['KAMUS KATA']
rows = list(ws.iter_rows(values_only=True))

print(f"Total rows in 'KAMUS Harf Ghair Amil.xlsx': {len(rows)}")
cats = {}
for r in rows[1:]:
    if not any(r): continue
    b, nk, k, ak, fk, s, a, jlh = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    b = str(b).strip() if b is not None else ''
    nk = str(nk).strip() if nk is not None else ''
    k = str(k).strip() if k is not None else ''
    ak = str(ak).strip() if ak is not None else ''
    if b not in cats:
        cats[b] = {}
    if nk not in cats[b]:
        cats[b][nk] = {'kata': k, 'arti': ak, 'frek': fk, 'rows': []}
    cats[b][nk]['rows'].append((s, a, jlh))

for b, nks in cats.items():
    print(f"\nCategory: [{b}] (Total {len(nks)} words)")
    for nk, data in nks.items():
        first_ref = f"QS {data['rows'][0][0]}:{data['rows'][0][1]}" if data['rows'] else "-"
        print(f"   - No {nk:<4}: {data['kata']:<10} | {data['arti']:<35} | Frek: {str(data['frek']):<5} | Ayat: {len(data['rows']):<4} (e.g. {first_ref})")
