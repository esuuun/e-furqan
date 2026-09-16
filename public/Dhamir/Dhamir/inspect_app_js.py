import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('dhamir_data.json', 'r', encoding='utf-8') as f:
    dhamir = json.load(f)

with open('harf_data.json', 'r', encoding='utf-8') as f:
    harf = json.load(f)

print('=== HARF CHECKS ===')
for i in [0, 10, 20, 30, 40, 50, 60, 80, 100, 150, 180]:
    if i < len(harf):
        r = harf[i]
        print(f"[{r['Bentuk Kata']} | {r['Kata']}]")
        print(f"  NL: {r.get('ArtiKataNL')} | {r.get('SuratArtiNL')} | {r.get('TeksArtiNL')[:45]}...")
        print(f"  IT: {r.get('ArtiKataIT')} | {r.get('SuratArtiIT')} | {r.get('TeksArtiIT')[:45]}...")

print('\n=== DHAMIR CHECKS ===')
for i in [0, 20, 50, 90, 130, 160, 190, 220, 250, 280]:
    if i < len(dhamir):
        r = dhamir[i]
        print(f"[{r['Bentuk Kata']} | {r['Kata']}]")
        print(f"  NL: {r.get('ArtiKataNL')} | {r.get('SuratArtiNL')} | {r.get('TeksArtiNL')[:45]}...")
        print(f"  IT: {r.get('ArtiKataIT')} | {r.get('SuratArtiIT')} | {r.get('TeksArtiIT')[:45]}...")






