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

words = {}
for r in rows[1:]:
    if not any(r): continue
    bk, nk, kata, arti, frek = r[0], r[1], r[2], r[3], r[4]
    bk = str(bk).strip() if bk is not None else ''
    nk = str(nk).strip() if nk is not None else ''
    kata = str(kata).strip() if kata is not None else ''
    arti = str(arti).strip() if arti is not None else ''
    key = (bk, nk)
    if key not in words:
        words[key] = {'kata': kata, 'arti': arti, 'frek': frek, 'count': 0}
    words[key]['count'] += 1

print(f'Total words: {len(words)}')
for (bk, nk), data in sorted(words.items(), key=lambda x: (x[0][0], str(x[0][1]))):
    print(f"{bk:<35} | No: {nk:<6} | {data['kata']:<10} | {data['arti']:<25} | Frek: {str(data['frek']):<5} | Ayat: {data['count']}")
