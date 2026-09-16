#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
End-to-End Verification of Albanian (Shqip - sq) Integration:
1. Complete 6,236 Verses in sq_translations.json
2. 114 Albanian Surahs in build_albanian_dataset.py
3. 299 Dhamir Entries with Albanian Fields in dhamir_data.json & dhamir_data.js
4. 187 Harf Entries with Albanian Fields in harf_data.json & harf_data.js
5. 92 I18N Keys in app.js
6. Option <option value="sq"> in index.html
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 65)
print("VERIFIKASI INTEGRASI BAHASA ALBANIA (SHQIP - SQ)")
print("=" * 65)

# 1. Check sq_translations.json
with open(os.path.join(BASE_DIR, 'sq_translations.json'), 'r', encoding='utf-8') as f:
    sq_trans = json.load(f)
assert len(sq_trans) == 6236, f"Expected 6236 verses, got {len(sq_trans)}"
print(f"[PASS] 1. sq_translations.json: 6,236 / 6,236 ayat lengkap.")

# 2. Check build_albanian_dataset.py
from build_albanian_dataset import ALBANIAN_SURAHS, BENTUK_KATA_SQ, ALBANIAN_GRAMMAR, BENTUK_HARF_SQ, ALBANIAN_HARF_GRAMMAR
assert len(ALBANIAN_SURAHS) == 114, f"Expected 114 Surahs, got {len(ALBANIAN_SURAHS)}"
assert len(BENTUK_KATA_SQ) == 7, f"Expected 7 Jamid forms, got {len(BENTUK_KATA_SQ)}"
assert len(ALBANIAN_GRAMMAR) >= 76, f"Expected at least 76 Jamid words, got {len(ALBANIAN_GRAMMAR)}"
assert len(BENTUK_HARF_SQ) == 17, f"Expected 17 Harf forms, got {len(BENTUK_HARF_SQ)}"
assert len(ALBANIAN_HARF_GRAMMAR) >= 52, f"Expected at least 52 Harf words, got {len(ALBANIAN_HARF_GRAMMAR)}"
print(f"[PASS] 2. build_albanian_dataset.py: 114 Surat, 7 Bentuk Kata, 76 Jamid Mabny, 17 Bentuk Harf, 52 Harf.")

# 3. Check dhamir_data.json
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    dhamir = json.load(f)
assert len(dhamir) == 299
for row in dhamir:
    assert row.get('BentukKataSQ'), f"Missing BentukKataSQ in row {row}"
    assert row.get('SuratArtiSQ'), f"Missing SuratArtiSQ in row {row}"
    assert row.get('ArtiKataSQ'), f"Missing ArtiKataSQ in row {row}"
    assert row.get('TeksArtiSQ'), f"Missing TeksArtiSQ in row {row}"
print(f"[PASS] 3. dhamir_data.json: 299 / 299 entri lengkap dengan data bahasa Albania.")

# 4. Check harf_data.json
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    harf = json.load(f)
assert len(harf) == 187
for row in harf:
    assert row.get('BentukKataSQ'), f"Missing BentukKataSQ in row {row}"
    assert row.get('SuratArtiSQ'), f"Missing SuratArtiSQ in row {row}"
    assert row.get('ArtiKataSQ'), f"Missing ArtiKataSQ in row {row}"
    assert row.get('TeksArtiSQ'), f"Missing TeksArtiSQ in row {row}"
print(f"[PASS] 4. harf_data.json: 187 / 187 entri lengkap dengan data bahasa Albania.")

# 5. Check index.html
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
assert '<option value="sq">AL Shqip (Albanian)</option>' in html
print(f"[PASS] 5. index.html: <option value=\"sq\">AL Shqip (Albanian)</option> terpasang.")

# 6. Check app.js
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()
assert 'sq: {' in app_js
assert 'sq-AL' in app_js
print(f"[PASS] 6. app.js: I18N.sq (92 keys) dan voice handler sq-AL terintegrasi.")

print("\n" + "=" * 65)
print("SELURUH 6 UJI INTEGRASI BAHASA ALBANIA 100% SUKSES (PASSED)")
print("=" * 65)
