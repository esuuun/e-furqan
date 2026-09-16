#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Turkish (tr) Language Integration.
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("VERIFYING TURKISH (TR) LANGUAGE INTEGRATION")
print("=" * 60)

passed = True

# 1. Check tr_translations.json
tr_file = os.path.join(BASE_DIR, 'tr_translations.json')
if os.path.exists(tr_file):
    with open(tr_file, 'r', encoding='utf-8') as f:
        tr_data = json.load(f)
    print(f"✓ [OK] tr_translations.json exists with {len(tr_data)} verses.")
else:
    print("✗ [FAIL] tr_translations.json not found!")
    passed = False

# 2. Check dhamir_data.json
data_file = os.path.join(BASE_DIR, 'dhamir_data.json')
if os.path.exists(data_file):
    with open(data_file, 'r', encoding='utf-8') as f:
        dhamir_data = json.load(f)
    print(f"✓ [OK] dhamir_data.json loaded ({len(dhamir_data)} entries).")
    
    missing_teks_tr = [d for d in dhamir_data if not d.get('TeksArtiTR')]
    missing_bentuk_tr = [d for d in dhamir_data if not d.get('BentukKataTR')]
    missing_surat_tr = [d for d in dhamir_data if not d.get('SuratArtiTR')]
    missing_arti_tr = [d for d in dhamir_data if not d.get('ArtiKataTR')]

    if not missing_teks_tr:
        print(f"✓ [OK] TeksArtiTR: 100% complete ({len(dhamir_data)}/{len(dhamir_data)}).")
    else:
        print(f"✗ [FAIL] Missing TeksArtiTR in {len(missing_teks_tr)} entries!")
        passed = False

    if not missing_bentuk_tr:
        print(f"✓ [OK] BentukKataTR: 100% complete ({len(dhamir_data)}/{len(dhamir_data)}).")
    else:
        print(f"✗ [FAIL] Missing BentukKataTR in {len(missing_bentuk_tr)} entries!")
        passed = False

    if not missing_surat_tr:
        print(f"✓ [OK] SuratArtiTR: 100% complete ({len(dhamir_data)}/{len(dhamir_data)}).")
    else:
        print(f"✗ [FAIL] Missing SuratArtiTR in {len(missing_surat_tr)} entries!")
        passed = False

    if not missing_arti_tr:
        print(f"✓ [OK] ArtiKataTR: 100% complete ({len(dhamir_data)}/{len(dhamir_data)}).")
    else:
        print(f"✗ [FAIL] Missing ArtiKataTR in {len(missing_arti_tr)} entries!")
        passed = False
else:
    print("✗ [FAIL] dhamir_data.json not found!")
    passed = False

# 3. Check build_multilingual_dataset.py imports
try:
    from build_multilingual_dataset import SURAHS, BENTUK_LABELS, GRAMMATICAL_METADATA
    missing_surah_tr = [s for s, v in SURAHS.items() if 'arti_tr' not in v]
    missing_bentuk_labels = [b for b, v in BENTUK_LABELS.items() if 'tr' not in v]
    missing_grammar_tr = [k for k, v in GRAMMATICAL_METADATA.items() if 'arti_tr' not in v or 'desc_tr' not in v or 'jenis_tr' not in v]

    if not missing_surah_tr:
        print(f"✓ [OK] SURAHS arti_tr: 100% complete ({len(SURAHS)} surahs).")
    else:
        print(f"✗ [FAIL] Missing arti_tr in {len(missing_surah_tr)} surahs: {missing_surah_tr[:5]}")
        passed = False

    if not missing_bentuk_labels:
        print(f"✓ [OK] BENTUK_LABELS tr: 100% complete ({len(BENTUK_LABELS)} categories).")
    else:
        print(f"✗ [FAIL] Missing tr in BENTUK_LABELS: {missing_bentuk_labels}")
        passed = False

    if not missing_grammar_tr:
        print(f"✓ [OK] GRAMMATICAL_METADATA Turkish: 100% complete ({len(GRAMMATICAL_METADATA)} entries).")
    else:
        print(f"✗ [FAIL] Missing Turkish metadata in {len(missing_grammar_tr)} entries: {missing_grammar_tr[:5]}")
        passed = False
except Exception as e:
    print(f"✗ [FAIL] Error importing build_multilingual_dataset: {e}")
    passed = False

# 4. Check index.html and app.js
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html_content = f.read()
if 'value="tr"' in html_content:
    print("✓ [OK] index.html includes Turkish option in language selector.")
else:
    print("✗ [FAIL] index.html missing Turkish option!")
    passed = False

with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    js_content = f.read()
if 'tr:' in js_content and 'tr-TR' in js_content:
    print("✓ [OK] app.js includes I18N.tr dictionary and Turkish TTS configuration.")
else:
    print("✗ [FAIL] app.js missing I18N.tr or Turkish TTS configuration!")
    passed = False

print("=" * 60)
if passed:
    print("🎉 ALL TURKISH INTEGRATION CHECKS PASSED SUCCESSFULLY!")
else:
    print("❌ SOME CHECKS FAILED! PLEASE REVIEW.")
print("=" * 60)
