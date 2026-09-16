#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master verification script for all 29 languages in Dhamir & Harf Web Application.
"""

import json
import os
import sys
import subprocess

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LANGS = [
    ('ID', 'id', 'verse_cache.json'),
    ('EN', 'en', 'en_translations.json'),
    ('MS', 'ms', 'ms_translations.json'),
    ('FR', 'fr', 'fr_translations.json'),
    ('DE', 'de', 'de_translations.json'),
    ('UR', 'ur', 'ur_translations.json'),
    ('HI', 'hi', 'hi_translations.json'),
    ('BN', 'bn', 'bn_translations.json'),
    ('RU', 'ru', 'ru_translations.json'),
    ('ZH', 'zh', 'zh_translations.json'),
    ('ES', 'es', 'es_translations.json'),
    ('TR', 'tr', 'tr_translations.json'),
    ('PT', 'pt', 'pt_translations.json'),
    ('HA', 'ha', 'ha_translations.json'),
    ('SW', 'sw', 'sw_translations.json'),
    ('FA', 'fa', 'fa_translations.json'),
    ('JA', 'ja', 'ja_translations.json'),
    ('KO', 'ko', 'ko_translations.json'),
    ('NL', 'nl', 'nl_translations.json'),
    ('IT', 'it', 'it_translations.json'),
    ('BS', 'bs', 'bs_translations.json'),
    ('SQ', 'sq', 'sq_translations.json'),
    ('TH', 'th', 'th_translations.json'),
    ('BER', 'ber', 'ber_translations.json'),
    ('AM', 'am', 'am_translations.json'),
    ('AZ', 'az', 'az_translations.json'),
    ('BG', 'bg', 'bg_translations.json'),
    ('CS', 'cs', 'cs_translations.json'),
    ('DV', 'dv', 'dv_translations.json'),
]

print("=" * 75)
print("MASTER VERIFIKASI 29 BAHASA APLIKASI WEB DHAMIR & HARF")
print("=" * 75)

# 1. Check translation caches
print("\n[1/6] Memeriksa Cache Terjemahan 29 Bahasa...")
for code_upper, code_lower, cache_file in LANGS:
    fp = os.path.join(BASE_DIR, cache_file)
    if not os.path.exists(fp):
        print(f"  [FAIL] Cache {cache_file} tidak ditemukan!")
        sys.exit(1)
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"  [OK] {code_upper:<4}: {len(data):,} ayat ({cache_file})")

# 2. Check 299 Jamid Mabny entries
print("\n[2/6] Memeriksa Kelengkapan 299 Entri Jamid Mabny di 29 Bahasa...")
dhamir_file = os.path.join(BASE_DIR, 'dhamir_data.json')
with open(dhamir_file, 'r', encoding='utf-8') as f:
    dhamir_data = json.load(f)

for code_upper, code_lower, _ in LANGS:
    missing_teks = sum(1 for x in dhamir_data if not x.get(f'TeksArti{code_upper}'))
    missing_arti = sum(1 for x in dhamir_data if not x.get(f'ArtiKata{code_upper}'))
    missing_surat = sum(1 for x in dhamir_data if not x.get(f'SuratArti{code_upper}'))
    
    if missing_teks > 0 or missing_arti > 0 or missing_surat > 0:
        print(f"  [FAIL] {code_upper}: missing_teks={missing_teks}, missing_arti={missing_arti}, missing_surat={missing_surat}")
        sys.exit(1)
    else:
        print(f"  [OK] {code_upper:<4}: {len(dhamir_data)} / {len(dhamir_data)} entri Jamid Mabny 100% lengkap")

# 3. Check 187 Harf Ghair 'Amil entries
print("\n[3/6] Memeriksa Kelengkapan 187 Entri Harf Ghair 'Amil di 29 Bahasa...")
harf_file = os.path.join(BASE_DIR, 'harf_data.json')
with open(harf_file, 'r', encoding='utf-8') as f:
    harf_data = json.load(f)

for code_upper, code_lower, _ in LANGS:
    missing_teks = sum(1 for x in harf_data if not x.get(f'TeksArti{code_upper}'))
    missing_arti = sum(1 for x in harf_data if not x.get(f'ArtiKata{code_upper}'))
    missing_surat = sum(1 for x in harf_data if not x.get(f'SuratArti{code_upper}'))
    
    if missing_teks > 0 or missing_arti > 0 or missing_surat > 0:
        print(f"  [FAIL] {code_upper}: missing_teks={missing_teks}, missing_arti={missing_arti}, missing_surat={missing_surat}")
        sys.exit(1)
    else:
        print(f"  [OK] {code_upper:<4}: {len(harf_data)} / {len(harf_data)} entri Harf Ghair 'Amil 100% lengkap")

# 4. Check index.html dropdown options
print("\n[4/6] Memeriksa Dropdown Pilihan Bahasa di index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

for _, code_lower, _ in LANGS:
    expected_opt = f'value="{code_lower}"'
    if expected_opt in index_html:
        print(f"  [OK] Option {expected_opt} terdaftar")
    else:
        print(f"  [FAIL] Option {expected_opt} TIDAK DITEMUKAN di index.html!")
        sys.exit(1)

# 5. Check I18N dictionary in app.js
print("\n[5/6] Memeriksa Dictionary I18N di app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

for _, code_lower, _ in LANGS:
    expected_key = f"{code_lower}: {{"
    if expected_key in app_js:
        print(f"  [OK] I18N.{code_lower} object terdefinisi")
    else:
        print(f"  [FAIL] I18N.{code_lower} TIDAK DITEMUKAN di app.js!")
        sys.exit(1)

# 6. Run JS Syntax Checks
print("\n[6/6] Menjalankan Syntax Check (Node.js)...")
for js_f in ['app.js', 'dhamir_data.js', 'harf_data.js']:
    res = subprocess.run(['node', '-c', os.path.join(BASE_DIR, js_f)], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  [OK] {js_f} valid (0 syntax errors)")
    else:
        print(f"  [FAIL] {js_f} syntax error:\n{res.stderr}")
        sys.exit(1)

print("\n" + "=" * 75)
print("SELURUH 29 BAHASA (TERMASUK CZECH & DHIVEHI) 100% TERVERIFIKASI & SIAP!")
print("=" * 75)
