import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('harf_data.json', 'r', encoding='utf-8') as f:
    harf_data = json.load(f)

for e in harf_data:
    if e.get('Bentuk Kata') == '1. Harf Nafyi':
        print(f"No: {e.get('No kata')} | Kata: {e.get('Kata')} | {e.get('SURAT')}:{e.get('AYAT')}")
        print(f"   AR: {e.get('TeksArab')}")
