import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('harf_data.json', 'r', encoding='utf-8') as f:
    harf_data = json.load(f)

# Group by (Bentuk Kata, No kata)
groups = {}
for entry in harf_data:
    b = entry.get('Bentuk Kata')
    no = entry.get('No kata')
    k = entry.get('Kata')
    key = f"{b}__{no}"
    if key not in groups:
        groups[key] = {
            'bentuk': b,
            'noKata': str(no),
            'kata': k,
            'arti': entry.get('Arti kata'),
            'entries': []
        }
    groups[key]['entries'].append(entry)

for key, g in groups.items():
    print(f"=== {key} | Kata: {g['kata']} ({g['arti']}) | Total: {len(g['entries'])} ayat ===")
    for e in g['entries']:
        surat = e.get('SURAT')
        ayat = e.get('AYAT')
        surat_nama = e.get('SuratNama')
        teks_arab = e.get('TeksArab')
        teks_arti = e.get('TeksArti')
        print(f"  [{surat}:{ayat} - {surat_nama}]")
        print(f"    AR: {teks_arab}")
        print(f"    ID: {teks_arti}")
