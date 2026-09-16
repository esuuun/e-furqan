import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Import Spanish metadata
from build_spanish_metadata import SPANISH_SURAHS, BENTUK_KATA_ES, SPANISH_GRAMMAR

with open(os.path.join(BASE_DIR, 'es_translations.json'), 'r', encoding='utf-8') as f:
    es_translations = json.load(f)

with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir_data = json.load(f)

print(f"Loaded {len(dhamir_data)} records from dhamir_data.json")

for item in dhamir_data:
    b = item.get('Bentuk Kata')
    nk = item.get('No kata')
    key = f"{b}__{nk}"
    
    # 1. Bentuk Kata ES
    item['BentukKataES'] = BENTUK_KATA_ES.get(b, b)
    
    # 2. Surat Info ES
    s = str(item.get('SURAT', ''))
    item['SuratArtiES'] = SPANISH_SURAHS.get(s, item.get('SuratArtiEN', ''))
    
    # 3. Arti Kata ES
    if key in SPANISH_GRAMMAR:
        item['ArtiKataES'] = SPANISH_GRAMMAR[key].get('arti_es', item.get('ArtiKataEN', ''))
        if 'Grammar' not in item or item['Grammar'] is None:
            item['Grammar'] = {}
        item['Grammar']['desc_es'] = SPANISH_GRAMMAR[key].get('desc_es', '')
        item['Grammar']['jenis_es'] = SPANISH_GRAMMAR[key].get('jenis_es', '')
    else:
        item['ArtiKataES'] = item.get('ArtiKataEN', '')
        
    # 4. Verse Translation ES
    v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
    teks_es = es_translations.get(v_key)
    if not teks_es:
        teks_es = item.get('TeksArtiEN', item.get('TeksArtiID', ''))
    item['TeksArtiES'] = teks_es

# Save dhamir_data.json
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
    json.dump(dhamir_data, f, ensure_ascii=False, indent=2)

print(f"Saved {len(dhamir_data)} records to dhamir_data.json with Spanish support!")

# Save dhamir_data.js
js_content = f'''/**
 * Dataset Lengkap Multilingual Al-Qur'an 11 Bahasa (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES)
 * Total: {len(dhamir_data)} Rujukan Ayat
 */

const DHAMIR_DATA = {json.dumps(dhamir_data, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Saved dhamir_data.js ({round(os.path.getsize(os.path.join(BASE_DIR, 'dhamir_data.js'))/1024, 1)} KB)!")
