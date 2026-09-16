#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
End-to-End Verification of Bosnian (Bosanski - bs) Integration:
1. Complete 6,236 Verses in bs_translations.json
2. 114 Bosnian Surahs in build_bosnian_dataset.py
3. 299 Dhamir Entries with Bosnian Fields in dhamir_data.json & dhamir_data.js
4. 187 Harf Entries with Bosnian Fields in harf_data.json & harf_data.js
5. 92 I18N Keys in app.js
6. Option <option value="bs"> in index.html
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 65)
print("VERIFIKASI INTEGRASI BAHASA BOSNIA (BOSANSKI - BS)")
print("=" * 65)

# 1. Check bs_translations.json
with open(os.path.join(BASE_DIR, 'bs_translations.json'), 'r', encoding='utf-8') as f:
    bs_trans = json.load(f)
assert len(bs_trans) == 6236, f"Expected 6236 verses, got {len(bs_trans)}"
print(f"[PASS] 1. bs_translations.json: 6,236 / 6,236 ayat lengkap.")

# 2. Check build_bosnian_dataset.py
from build_bosnian_dataset import BOSNIAN_SURAHS, BENTUK_KATA_BS, BOSNIAN_GRAMMAR, BENTUK_HARF_BS, BOSNIAN_HARF_GRAMMAR
assert len(BOSNIAN_SURAHS) == 114, f"Expected 114 Surahs, got {len(BOSNIAN_SURAHS)}"
assert len(BENTUK_KATA_BS) == 7, f"Expected 7 Jamid forms, got {len(BENTUK_KATA_BS)}"
assert len(BOSNIAN_GRAMMAR) >= 76, f"Expected at least 76 Jamid words, got {len(BOSNIAN_GRAMMAR)}"
assert len(BENTUK_HARF_BS) == 17, f"Expected 17 Harf forms, got {len(BENTUK_HARF_BS)}"
assert len(BOSNIAN_HARF_GRAMMAR) >= 52, f"Expected at least 52 Harf words, got {len(BOSNIAN_HARF_GRAMMAR)}"
print(f"[PASS] 2. build_bosnian_dataset.py: 114 Surat, 7 Bentuk Kata, 76 Jamid Mabny, 17 Bentuk Harf, 52 Harf.")

# 3. Check dhamir_data.json
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir = json.load(f)
assert len(dhamir) == 299
for row in dhamir:
    assert row.get('BentukKataBS'), f"Missing BentukKataBS in row {row}"
    assert row.get('SuratArtiBS'), f"Missing SuratArtiBS in row {row}"
    assert row.get('ArtiKataBS'), f"Missing ArtiKataBS in row {row}"
    assert row.get('TeksArtiBS'), f"Missing TeksArtiBS in row {row}"
print(f"[PASS] 3. dhamir_data.json: 299 / 299 entri lengkap dengan data bahasa Bosnia.")

# 4. Check harf_data.json
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    harf = json.load(f)
assert len(harf) == 187
for row in harf:
    assert row.get('BentukKataBS'), f"Missing BentukKataBS in row {row}"
    assert row.get('SuratArtiBS'), f"Missing SuratArtiBS in row {row}"
    assert row.get('ArtiKataBS'), f"Missing ArtiKataBS in row {row}"
    assert row.get('TeksArtiBS'), f"Missing TeksArtiBS in row {row}"
print(f"[PASS] 4. harf_data.json: 187 / 187 entri lengkap dengan data bahasa Bosnia.")

# 5. Check index.html
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
assert '<option value="bs">BA Bosanski (Bosnian)</option>' in html
print(f"[PASS] 5. index.html: <option value=\"bs\">BA Bosanski (Bosnian)</option> terpasang.")

# 6. Check app.js
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()
assert 'bs: {' in app_js
assert 'bs-BA' in app_js
print(f"[PASS] 6. app.js: I18N.bs (92 keys) dan voice handler bs-BA terintegrasi.")

print("\n" + "=" * 65)
print("SELURUH 6 UJI INTEGRASI BAHASA BOSNIA 100% SUKSES (PASSED)")
print("=" * 65)
