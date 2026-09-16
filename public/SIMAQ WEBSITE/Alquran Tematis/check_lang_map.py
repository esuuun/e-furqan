import json, re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract LANG_UI_MAP
start = text.find('const LANG_UI_MAP = {')
end = text.find('const KEYWORD_SYNONYMS')

map_text = text[start:end]

test_keys = [
    'Cari', 'Filter Hasil:', 'Semua Hasil', 'Hanya Uraian Tematis', 
    'Hanya Teks Terjemahan Ayat', '💡 Kata Kunci Populer:', 'Sabar', 
    'Riba', 'Shalat', 'Taubat', 'Rezeki', 'Surga', 'Neraka', 
    'Orang Tua', 'Sedekah', 'Kiamat', 'Syukur'
]

for lang in ['en', 'ar', 'ms', 'ur', 'tr', 'fr']:
    # Check if lang is in map_text
    lang_block_start = map_text.find(f"'{lang}': {{")
    if lang_block_start == -1:
        print(f"Language {lang} NOT FOUND in LANG_UI_MAP!")
        continue
    # Find next language or end
    next_lang_start = map_text.find("': {", lang_block_start + 10)
    lang_block = map_text[lang_block_start:next_lang_start if next_lang_start != -1 else len(map_text)]
    
    missing = [k for k in test_keys if f"'{k}':" not in lang_block]
    print(f"Lang '{lang}': missing {len(missing)} keys -> {missing}")
