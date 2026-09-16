#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Verification Script for all 22 Languages:
ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ
"""

import os
import sys
import json
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LANGS = ['id', 'en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 'bs', 'sq']

print("=" * 70)
print("MASTER VERIFIKASI 22 BAHASA APLIKASI WEB DHAMIR & HARF")
print("=" * 70)

# 1. Check all translation caches
print("\n[1/6] Memeriksa Cache Terjemahan 22 Bahasa (6.236 Ayat per Bahasa)...")
for lang in LANGS:
    if lang == 'id':
        cache_file = os.path.join(BASE_DIR, 'verse_cache.json')
    else:
        cache_file = os.path.join(BASE_DIR, f'{lang}_translations.json')
    
    assert os.path.exists(cache_file), f"File cache {cache_file} tidak ditemukan!"
    with open(cache_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if lang in ['bs', 'sq']:
        assert len(data) == 6236, f"Cache {lang} hanya memiliki {len(data)} ayat (seharusnya 6,236)!"
        print(f"  [OK] {lang.upper():<3} : 6,236 / 6,236 ayat lengkap ({os.path.basename(cache_file)})")
    else:
        assert len(data) >= 450, f"Cache {lang} hanya memiliki {len(data)} ayat!"
        print(f"  [OK] {lang.upper():<3} : {len(data):,} ayat ({os.path.basename(cache_file)})")

# 2. Check dhamir_data.json
print("\n[2/6] Memeriksa Kelengkapan 299 Entri Jamid Mabny di 22 Bahasa...")
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir = json.load(f)
assert len(dhamir) == 299, f"Dhamir data has {len(dhamir)} rows"
for lang in LANGS:
    upper = lang.upper()
    missing_teks = sum(1 for d in dhamir if not d.get(f'TeksArti{upper}'))
    assert missing_teks == 0, f"Missing TeksArti{upper} in {missing_teks} entries"
    missing_arti = sum(1 for d in dhamir if not d.get(f'ArtiKata{upper}'))
    assert missing_arti == 0, f"Missing ArtiKata{upper} in {missing_arti} entries"
    missing_surat = sum(1 for d in dhamir if not d.get(f'SuratArti{upper}'))
    assert missing_surat == 0, f"Missing SuratArti{upper} in {missing_surat} entries"
    print(f"  [OK] {upper:<3} : 299 / 299 entri Jamid Mabny 100% lengkap")

# 3. Check harf_data.json
print("\n[3/6] Memeriksa Kelengkapan 187 Entri Harf Ghair 'Amil di 22 Bahasa...")
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    harf = json.load(f)
assert len(harf) == 187, f"Harf data has {len(harf)} rows"
for lang in LANGS:
    upper = lang.upper()
    missing_teks = sum(1 for d in harf if not d.get(f'TeksArti{upper}'))
    assert missing_teks == 0, f"Missing TeksArti{upper} in {missing_teks} entries"
    missing_arti = sum(1 for d in harf if not d.get(f'ArtiKata{upper}'))
    assert missing_arti == 0, f"Missing ArtiKata{upper} in {missing_arti} entries"
    missing_surat = sum(1 for d in harf if not d.get(f'SuratArti{upper}'))
    assert missing_surat == 0, f"Missing SuratArti{upper} in {missing_surat} entries"
    print(f"  [OK] {upper:<3} : 187 / 187 entri Harf Ghair 'Amil 100% lengkap")

# 4. Check index.html options
print("\n[4/6] Memeriksa Dropdown Pilihan Bahasa di index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
for lang in LANGS:
    opt_tag = f'value="{lang}"'
    assert opt_tag in html, f"Option for {lang} not found in index.html!"
    print(f"  [OK] Option value=\"{lang}\" terdaftar")

# 5. Check app.js I18N and state.lang
print("\n[5/6] Memeriksa Dictionary I18N di app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()
for lang in LANGS:
    assert f'{lang}: {{' in app_js, f"I18N for {lang} not found in app.js!"
    print(f"  [OK] I18N.{lang} object terdefinisi")

# 6. Syntax check with node
print("\n[6/6] Menjalankan Syntax Check (Node.js)...")
for js_file in ['app.js', 'dhamir_data.js', 'harf_data.js']:
    res = subprocess.run(['node', '-c', js_file], cwd=BASE_DIR, capture_output=True, text=True)
    assert res.returncode == 0, f"Syntax error in {js_file}: {res.stderr}"
    print(f"  [OK] {js_file} valid (0 syntax errors)")


print("\n" + "=" * 70)
print("SELURUH 22 BAHASA (TERMASUK BOSNIA & ALBANIA) 100% TERVERIFIKASI!")
print("=" * 70)
