import json
import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/Dhamir/dhamir_data.json', encoding='utf-8') as f:
    data = json.load(f)

unique_verses = sorted(list(set(f"{item['SURAT']}:{item['AYAT']}" for item in data if item.get('SURAT') and item.get('AYAT'))), key=lambda x: (int(x.split(':')[0]), int(x.split(':')[1])))

print(f"Total dataset entries: {len(data)}, Unique verses needed: {len(unique_verses)}")
print("Sample verses:", unique_verses[:10])
