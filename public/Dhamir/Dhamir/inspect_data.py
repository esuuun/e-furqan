import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/Dhamir/dhamir_data.json', encoding='utf-8') as f:
    data = json.load(f)

print('Total entries:', len(data))
bentuks = sorted(list(set(d['Bentuk Kata'] for d in data if d.get('Bentuk Kata'))))
print('Bentuk Kata list:', bentuks)

no_katas = sorted(list(set(d['No kata'] for d in data if d.get('No kata'))))
print('No kata list:', no_katas)

for b in bentuks:
    items_b = [d for d in data if d['Bentuk Kata'] == b]
    print(f'=== {b} ({len(items_b)} records) ===')
    sub_nos = sorted(list(set(d['No kata'] for d in items_b if d.get('No kata'))))
    for n in sub_nos:
        items_bn = [d for d in items_b if d['No kata'] == n]
        first = items_bn[0]
        surat_ayat_list = [f"{d['SURAT']}:{d['AYAT']}" for d in items_bn]
        print(f"  [{n}] {first['Kata']} ({first['Arti kata']}) - Frek: {first['Frek kata']} - Total Ayat: {len(items_bn)}")
