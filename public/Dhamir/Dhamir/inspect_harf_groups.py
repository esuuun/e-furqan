import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('harf_data.json', 'r', encoding='utf-8') as f:
    harf = json.load(f)

groups = {}
for entry in harf:
    b = entry.get('Bentuk Kata')
    no = entry.get('No kata')
    k = entry.get('Kata')
    key = f"{b}__{no}"
    if key not in groups:
        groups[key] = {'bentuk': b, 'noKata': str(no), 'kata': k, 'entries': []}
    groups[key]['entries'].append(entry)

print(f"Total groups in harf_data: {len(groups)}")
for k, v in groups.items():
    print(f"Key: {k}, Kata: {v['kata']}, Ayat count: {len(v['entries'])}")
