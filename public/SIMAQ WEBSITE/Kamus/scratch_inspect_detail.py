import openpyxl, sys, json
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Kamus Harf \'Amil.xlsx', data_only=True)
ws = wb['KAMUS KATA']
rows = list(ws.iter_rows(values_only=True))

data = []
for r in rows[1:]:
    if not any(r): continue
    b, nk, k, ak, fk, s, a, jlh = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    data.append({
        'Bentuk': str(b).strip() if b else '',
        'No': str(nk).strip() if nk is not None else '',
        'Kata': str(k).strip() if k else '',
        'Arti': str(ak).strip() if ak else '',
        'Frek': fk,
        'SURAT': int(s) if s is not None else None,
        'AYAT': int(a) if a is not None else None,
        'JLH': jlh
    })

print(f'Total rows loaded: {len(data)}')
by_cat = {}
for d in data:
    cat = d['Bentuk']
    if cat not in by_cat:
        by_cat[cat] = {}
    no = d['No']
    if no not in by_cat[cat]:
        by_cat[cat][no] = {
            'word': d['Kata'],
            'arti': d['Arti'],
            'frek': d['Frek'],
            'count': 0,
            'verses': []
        }
    by_cat[cat][no]['count'] += 1
    by_cat[cat][no]['verses'].append(f"{d['SURAT']}:{d['AYAT']}")

for cat, words in sorted(by_cat.items()):
    print(f"\n=== {cat} ({len(words)} kata) ===")
    for no, w in sorted(words.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 99):
        print(f"  No {no:>2}: {w['word']} | {w['arti']} | Frek: {w['frek']} | {w['count']} contoh: {w['verses'][:4]}")
