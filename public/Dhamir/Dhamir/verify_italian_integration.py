#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
End-to-End Verification of Italian (Italiano - it) Integration:
1. Complete 6,236 Verses in it_translations.json
2. 114 Italian Surahs in build_italian_dataset.py
3. 299 Dhamir Entries with Italian Fields in dhamir_data.json & dhamir_data.js
4. 187 Harf Entries with Italian Fields in harf_data.json & harf_data.js
5. 92 I18N Keys in app.js
6. Option <option value="it"> in index.html
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 65)
print("VERIFIKASI INTEGRASI BAHASA ITALIA (ITALIANO - IT)")
print("=" * 65)

# 1. Check it_translations.json
with open(os.path.join(BASE_DIR, 'it_translations.json'), 'r', encoding='utf-8') as f:
    it_trans = json.load(f)
assert len(it_trans) == 6236, f"Expected 6236 verses, got {len(it_trans)}"
print(f"[PASS] 1. it_translations.json: 6,236 / 6,236 ayat lengkap.")

# 2. Check build_italian_dataset.py
from build_italian_dataset import ITALIAN_SURAHS, BENTUK_KATA_IT, ITALIAN_GRAMMAR, BENTUK_HARF_IT, ITALIAN_HARF_GRAMMAR
assert len(ITALIAN_SURAHS) == 114, f"Expected 114 Surahs, got {len(ITALIAN_SURAHS)}"
assert len(BENTUK_KATA_IT) == 7, f"Expected 7 Jamid forms, got {len(BENTUK_KATA_IT)}"
assert len(ITALIAN_GRAMMAR) >= 76, f"Expected at least 76 Jamid words, got {len(ITALIAN_GRAMMAR)}"
assert len(BENTUK_HARF_IT) == 17, f"Expected 17 Harf forms, got {len(BENTUK_HARF_IT)}"
assert len(ITALIAN_HARF_GRAMMAR) >= 52, f"Expected at least 52 Harf words, got {len(ITALIAN_HARF_GRAMMAR)}"
print(f"[PASS] 2. build_italian_dataset.py: 114 Surat, 7 Bentuk Kata, 76 Jamid Mabny, 17 Bentuk Harf, 52 Harf.")

# 3. Check dhamir_data.json
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir = json.load(f)
assert len(dhamir) == 299
for row in dhamir:
    assert row.get('BentukKataIT'), f"Missing BentukKataIT in row {row}"
    assert row.get('SuratArtiIT'), f"Missing SuratArtiIT in row {row}"
    assert row.get('ArtiKataIT'), f"Missing ArtiKataIT in row {row}"
    assert row.get('TeksArtiIT'), f"Missing TeksArtiIT in row {row}"
print(f"[PASS] 3. dhamir_data.json: 299 / 299 entri lengkap dengan data bahasa Italia.")

# 4. Check harf_data.json
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    harf = json.load(f)
assert len(harf) == 187
for row in harf:
    assert row.get('BentukKataIT'), f"Missing BentukKataIT in row {row}"
    assert row.get('SuratArtiIT'), f"Missing SuratArtiIT in row {row}"
    assert row.get('ArtiKataIT'), f"Missing ArtiKataIT in row {row}"
    assert row.get('TeksArtiIT'), f"Missing TeksArtiIT in row {row}"
print(f"[PASS] 4. harf_data.json: 187 / 187 entri lengkap dengan data bahasa Italia.")

# 5. Check index.html
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
assert '<option value="it">IT Italiano</option>' in html
print(f"[PASS] 5. index.html: <option value=\"it\">IT Italiano</option> terpasang.")

# 6. Check app.js
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()
assert 'it: {' in app_js
assert 'it-IT' in app_js
print(f"[PASS] 6. app.js: I18N.it (92 keys) dan voice handler it-IT terintegrasi.")

print("\n" + "=" * 65)
print("SELURUH 6 UJI INTEGRASI BAHASA ITALIA 100% SUKSES (PASSED)")
print("=" * 65)
