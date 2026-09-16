import openpyxl
import json
import sys

wb = openpyxl.load_workbook('d:/Dhamir/DHAMIR copy.xlsx', data_only=True)
sheet = wb['Sheet1']
rows = list(sheet.iter_rows(values_only=True))
header = [str(c).strip() if c is not None else '' for c in rows[0]]

data = []
for r in rows[1:]:
    if not any(r):
        continue
    item = {}
    for h, val in zip(header, r):
        item[h] = val
    data.append(item)

with open('d:/Dhamir/dhamir_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Exported {len(data)} rows successfully.")
