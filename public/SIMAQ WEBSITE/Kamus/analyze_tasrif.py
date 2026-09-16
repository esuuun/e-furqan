import sys, openpyxl, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
wb = openpyxl.load_workbook('Kamus Musytaq.xlsx', data_only=True)
sheet = wb['KAMUS KATA']

tasrifs = [sheet.cell(r, 4).value for r in range(2, sheet.max_row + 1) if sheet.cell(r, 4).value]
tasrifs = [str(t).strip() for t in tasrifs]

c = Counter(tasrifs)
print(f"Total entries: {len(tasrifs)}, Unique tasrif codes: {len(c)}")
print("\nMost common tasrif codes:")
for t, cnt in c.most_common(30):
    print(f"{t}: {cnt}")

# Let's categorize by prefix:
prefixes = Counter([t.split()[0] if t.split() else '' for t in tasrifs])
print("\nTasrif Type Prefixes:")
for p, cnt in prefixes.most_common():
    print(f"{p}: {cnt}")
