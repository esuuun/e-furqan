# d:/SIMAQ WEBSITE/Mushaf/generate_mushaf_js.py
import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEBSITE_ROOT = os.path.dirname(BASE_DIR)
PUBLIC_DATA_DIR = os.path.join(BASE_DIR, 'quran-app', 'public', 'data')
OUT_JS_DIR = os.path.join(BASE_DIR, 'data_js')
KAMUS_DIR = os.path.join(WEBSITE_ROOT, 'Kamus')

os.makedirs(OUT_JS_DIR, exist_ok=True)

print(f"Generating JS dataset from {PUBLIC_DATA_DIR} to {OUT_JS_DIR}...")

# Helper to clean arabic diacritics and normalize
def clean_arabic(text):
    if not text:
        return ''
    text = str(text)
    text = re.sub(r'\d+', '', text)
    text = text.replace('\u0671', '\u0627') # Wasla to Alef
    text = re.sub(r'[\u064B-\u065F\u06E1\u06D6-\u06ED]', '', text) # Tashkeel / Harakat
    return re.sub(r'\s+', ' ', text).strip()

# 1. Generate surah_1.js ... surah_114.js
surah_count = 0
for surah_num in range(1, 115):
    json_path = os.path.join(PUBLIC_DATA_DIR, f'surah_{surah_num}.json')
    if not os.path.exists(json_path):
        continue
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    js_content = f"""window.__MUSHAF_SURAH_DATA = window.__MUSHAF_SURAH_DATA || {{}};
window.__MUSHAF_SURAH_DATA[{surah_num}] = {json.dumps(data, ensure_ascii=False)};
"""
    out_path = os.path.join(OUT_JS_DIR, f'surah_{surah_num}.js')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    surah_count += 1

print(f"Generated {surah_count} Surah JS files.")

# 2. Build Kamus Lookup dictionary
lookup = {
    'musytaq_roots': {},
    'jamid_words': {},
    'harf_amil_words': {},
    'harf_words': {}
}

# 2a. Musytaq Roots
musytaq_file = os.path.join(KAMUS_DIR, 'musytaq_data.json')
if os.path.exists(musytaq_file):
    with open(musytaq_file, 'r', encoding='utf-8') as f:
        m_data = json.load(f)
    for lvl in m_data.get('levels', []):
        for r in lvl.get('roots', []):
            akar = clean_arabic(r.get('akar', ''))
            dasar = clean_arabic(r.get('dasar', ''))
            no_akar = r.get('no_akar', '')
            if akar:
                lookup['musytaq_roots'][akar] = {'id': no_akar, 'level': lvl.get('level', 1)}
                lookup['musytaq_roots'][akar.replace(' ', '')] = {'id': no_akar, 'level': lvl.get('level', 1)}
            if dasar and dasar not in lookup['musytaq_roots']:
                lookup['musytaq_roots'][dasar] = {'id': no_akar, 'level': lvl.get('level', 1)}

print(f"Musytaq roots mapped: {len(lookup['musytaq_roots'])}")

# 2b. Jamid Mabny
dhamir_file = os.path.join(KAMUS_DIR, 'dhamir_data.json')
if os.path.exists(dhamir_file):
    with open(dhamir_file, 'r', encoding='utf-8') as f:
        j_data = json.load(f)
    for item in j_data:
        kata = clean_arabic(item.get('Kata', ''))
        no_kata = item.get('No kata', '')
        if kata:
            lookup['jamid_words'][kata] = {'no': no_kata}
            lookup['jamid_words'][kata.replace(' ', '')] = {'no': no_kata}

print(f"Jamid words mapped: {len(lookup['jamid_words'])}")

# 2c. Harf Amil
harf_amil_file = os.path.join(KAMUS_DIR, 'harf_amil_data.json')
if os.path.exists(harf_amil_file):
    with open(harf_amil_file, 'r', encoding='utf-8') as f:
        ha_data = json.load(f)
    for item in ha_data:
        kata = clean_arabic(item.get('Kata', ''))
        no_kata = item.get('No kata', '')
        if kata:
            lookup['harf_amil_words'][kata] = {'no': no_kata}
            lookup['harf_amil_words'][kata.replace(' ', '')] = {'no': no_kata}

print(f"Harf Amil words mapped: {len(lookup['harf_amil_words'])}")

# 2d. Harf Ghair Amil
harf_file = os.path.join(KAMUS_DIR, 'harf_data.json')
if os.path.exists(harf_file):
    with open(harf_file, 'r', encoding='utf-8') as f:
        h_data = json.load(f)
    for item in h_data:
        kata = clean_arabic(item.get('Kata', ''))
        no_kata = item.get('No kata', '')
        if kata:
            lookup['harf_words'][kata] = {'no': no_kata}
            lookup['harf_words'][kata.replace(' ', '')] = {'no': no_kata}

print(f"Harf Ghair Amil words mapped: {len(lookup['harf_words'])}")

# Write kamus_lookup.js
kamus_lookup_path = os.path.join(OUT_JS_DIR, 'kamus_lookup.js')
with open(kamus_lookup_path, 'w', encoding='utf-8') as f:
    f.write(f"window.__KAMUS_LOOKUP = {json.dumps(lookup, ensure_ascii=False, indent=2)};\n")

print(f"Successfully generated: {kamus_lookup_path}")
