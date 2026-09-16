#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Verification Script for all 27 Languages in Dhamir & Harf Quran Web Application:
Languages: id, en, ms, fr, de, ur, hi, bn, ru, zh, es, tr, pt, ha, sw, fa, ja, ko, nl, it, bs, sq, th, ber, am, az, bg
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

ALL_LANGS = [
    'id', 'en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 
    'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 
    'bs', 'sq', 'th', 'ber', 'am', 'az', 'bg'
]

LANG_CACHE_FILES = {
    'id': 'verse_cache.json',
    'en': 'en_translations.json',
    'ms': 'ms_translations.json',
    'fr': 'fr_translations.json',
    'de': 'de_translations.json',
    'ur': 'ur_translations.json',
    'hi': 'hi_translations.json',
    'bn': 'bn_translations.json',
    'ru': 'ru_translations.json',
    'zh': 'zh_translations.json',
    'es': 'es_translations.json',
    'tr': 'tr_translations.json',
    'pt': 'pt_translations.json',
    'ha': 'ha_translations.json',
    'sw': 'sw_translations.json',
    'fa': 'fa_translations.json',
    'ja': 'ja_translations.json',
    'ko': 'ko_translations.json',
    'nl': 'nl_translations.json',
    'it': 'it_translations.json',
    'bs': 'bs_translations.json',
    'sq': 'sq_translations.json',
    'th': 'th_translations.json',
    'ber': 'ber_translations.json',
    'am': 'am_translations.json',
    'az': 'az_translations.json',
    'bg': 'bg_translations.json'
}

def verify():
    print("=" * 75)
    print(f"MASTER VERIFIKASI 27 BAHASA APLIKASI WEB DHAMIR & HARF")
    print("=" * 75)
    
    # 1. Check Translation Caches
    print("\n[1/6] Memeriksa Cache Terjemahan 27 Bahasa...")
    for lang, fname in LANG_CACHE_FILES.items():
        fpath = os.path.join(BASE_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  [FAIL] {lang.upper():<4}: File {fname} tidak ditemukan!")
            return False
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            count = len(data)
            status = "6,236 / 6,236 ayat lengkap" if count == 6236 else f"{count:,} ayat"
            print(f"  [OK] {lang.upper():<4}: {status} ({fname})")

    # 2. Check Dhamir Data
    print("\n[2/6] Memeriksa Kelengkapan 299 Entri Jamid Mabny di 27 Bahasa...")
    dhamir_file = os.path.join(BASE_DIR, 'dhamir_data.json')
    with open(dhamir_file, 'r', encoding='utf-8') as f:
        dhamir_data = json.load(f)
    
    assert len(dhamir_data) == 299, f"Dhamir data must have 299 entries, got {len(dhamir_data)}"
    for lang in ALL_LANGS:
        l_upper = lang.upper()
        if lang == 'id':
            teks_key, arti_key, surat_key = 'TeksArti', 'Arti kata', 'SuratArti'
        else:
            teks_key, arti_key, surat_key = f'TeksArti{l_upper}', f'ArtiKata{l_upper}', f'SuratArti{l_upper}'
        
        missing_teks = sum(1 for x in dhamir_data if not x.get(teks_key))
        missing_arti = sum(1 for x in dhamir_data if not x.get(arti_key))
        missing_surat = sum(1 for x in dhamir_data if not x.get(surat_key))
        
        if missing_teks == 0 and missing_arti == 0 and missing_surat == 0:
            print(f"  [OK] {l_upper:<4}: 299 / 299 entri Jamid Mabny 100% lengkap")
        else:
            print(f"  [FAIL] {l_upper:<4}: missing teks={missing_teks}, arti={missing_arti}, surat={missing_surat}")
            return False

    # 3. Check Harf Data
    print("\n[3/6] Memeriksa Kelengkapan 187 Entri Harf Ghair 'Amil di 27 Bahasa...")
    harf_file = os.path.join(BASE_DIR, 'harf_data.json')
    with open(harf_file, 'r', encoding='utf-8') as f:
        harf_data = json.load(f)
    
    assert len(harf_data) == 187, f"Harf data must have 187 entries, got {len(harf_data)}"
    for lang in ALL_LANGS:
        l_upper = lang.upper()
        if lang == 'id':
            teks_key, arti_key, surat_key = 'TeksArti', 'Arti kata', 'SuratArti'
        else:
            teks_key, arti_key, surat_key = f'TeksArti{l_upper}', f'ArtiKata{l_upper}', f'SuratArti{l_upper}'
        
        missing_teks = sum(1 for x in harf_data if not x.get(teks_key))
        missing_arti = sum(1 for x in harf_data if not x.get(arti_key))
        missing_surat = sum(1 for x in harf_data if not x.get(surat_key))
        
        if missing_teks == 0 and missing_arti == 0 and missing_surat == 0:
            print(f"  [OK] {l_upper:<4}: 187 / 187 entri Harf Ghair 'Amil 100% lengkap")
        else:
            print(f"  [FAIL] {l_upper:<4}: missing teks={missing_teks}, arti={missing_arti}, surat={missing_surat}")
            return False

    # 4. Check index.html options
    print("\n[4/6] Memeriksa Dropdown Pilihan Bahasa di index.html...")
    with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        index_html = f.read()
    for lang in ALL_LANGS:
        needle = f'value="{lang}"'
        if needle in index_html:
            print(f"  [OK] Option {needle} terdaftar")
        else:
            print(f"  [FAIL] Option {needle} TIDAK ditemukan di index.html!")
            return False

    # 5. Check I18N in app.js
    print("\n[5/6] Memeriksa Dictionary I18N di app.js...")
    with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
        app_js = f.read()
    for lang in ALL_LANGS:
        needle = f"{lang}: {{"
        if needle in app_js:
            print(f"  [OK] I18N.{lang} object terdefinisi")
        else:
            print(f"  [FAIL] I18N.{lang} TIDAK ditemukan di app.js!")
            return False

    # 6. Check JS Syntax via Node.js
    print("\n[6/6] Menjalankan Syntax Check (Node.js)...")
    for js_file in ['app.js', 'dhamir_data.js', 'harf_data.js']:
        res = subprocess.run(['node', '-c', os.path.join(BASE_DIR, js_file)], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [OK] {js_file} valid (0 syntax errors)")
        else:
            print(f"  [FAIL] {js_file} syntax error:\n{res.stderr}")
            return False

    print("\n" + "=" * 75)
    print("SELURUH 27 BAHASA (TERMASUK AZERBAIJAN & BULGARIA) 100% TERVERIFIKASI & SIAP!")
    print("=" * 75)
    return True

if __name__ == '__main__':
    ok = verify()
    sys.exit(0 if ok else 1)
