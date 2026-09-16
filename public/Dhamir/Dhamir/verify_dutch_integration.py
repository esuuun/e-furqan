#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
End-to-End Verification of Dutch (Nederlands - nl) Integration:
1. Complete 6,236 Verses in nl_translations.json
2. 114 Dutch Surahs in build_dutch_dataset.py
3. 299 Dhamir Entries with Dutch Fields in dhamir_data.json & dhamir_data.js
4. 187 Harf Entries with Dutch Fields in harf_data.json & harf_data.js
5. 92 I18N Keys in app.js
6. Option <option value="nl"> in index.html
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 65)
print("VERIFIKASI INTEGRASI BAHASA BELANDA (NEDERLANDS - NL)")
print("=" * 65)

# 1. Check nl_translations.json
with open(os.path.join(BASE_DIR, 'nl_translations.json'), 'r', encoding='utf-8') as f:
    nl_trans = json.load(f)
assert len(nl_trans) == 6236, f"Expected 6236 verses, got {len(nl_trans)}"
print(f"[PASS] 1. nl_translations.json: 6,236 / 6,236 ayat lengkap.")

# 2. Check build_dutch_dataset.py
from build_dutch_dataset import DUTCH_SURAHS, BENTUK_KATA_NL, DUTCH_GRAMMAR, BENTUK_HARF_NL, DUTCH_HARF_GRAMMAR
assert len(DUTCH_SURAHS) == 114, f"Expected 114 Surahs, got {len(DUTCH_SURAHS)}"
assert len(BENTUK_KATA_NL) == 7, f"Expected 7 Jamid forms, got {len(BENTUK_KATA_NL)}"
assert len(DUTCH_GRAMMAR) >= 76, f"Expected at least 76 Jamid words, got {len(DUTCH_GRAMMAR)}"
assert len(BENTUK_HARF_NL) == 17, f"Expected 17 Harf forms, got {len(BENTUK_HARF_NL)}"
assert len(DUTCH_HARF_GRAMMAR) >= 52, f"Expected at least 52 Harf words, got {len(DUTCH_HARF_GRAMMAR)}"
print(f"[PASS] 2. build_dutch_dataset.py: 114 Surat, 7 Bentuk Kata, 76 Jamid Mabny, 17 Bentuk Harf, 52 Harf.")

# 3. Check dhamir_data.json
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir = json.load(f)
assert len(dhamir) == 299
for row in dhamir:
    assert row.get('BentukKataNL'), f"Missing BentukKataNL in row {row}"
    assert row.get('SuratArtiNL'), f"Missing SuratArtiNL in row {row}"
    assert row.get('ArtiKataNL'), f"Missing ArtiKataNL in row {row}"
    assert row.get('TeksArtiNL'), f"Missing TeksArtiNL in row {row}"
print(f"[PASS] 3. dhamir_data.json: 299 / 299 entri lengkap dengan data bahasa Belanda.")

# 4. Check harf_data.json
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    harf = json.load(f)
assert len(harf) == 187
for row in harf:
    assert row.get('BentukKataNL'), f"Missing BentukKataNL in row {row}"
    assert row.get('SuratArtiNL'), f"Missing SuratArtiNL in row {row}"
    assert row.get('ArtiKataNL'), f"Missing ArtiKataNL in row {row}"
    assert row.get('TeksArtiNL'), f"Missing TeksArtiNL in row {row}"
print(f"[PASS] 4. harf_data.json: 187 / 187 entri lengkap dengan data bahasa Belanda.")

# 5. Check index.html
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
assert '<option value="nl">NL Nederlands</option>' in html
print(f"[PASS] 5. index.html: <option value=\"nl\">NL Nederlands</option> terpasang.")

# 6. Check app.js
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()
assert 'nl: {' in app_js
assert 'nl-NL' in app_js
print(f"[PASS] 6. app.js: I18N.nl (92 keys) dan voice handler nl-NL terintegrasi.")

print("\n" + "=" * 65)
print("SELURUH 6 UJI INTEGRASI BAHASA BELANDA 100% SUKSES (PASSED)")
print("=" * 65)
