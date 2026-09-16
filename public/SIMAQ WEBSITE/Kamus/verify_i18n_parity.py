#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify i18n parity across all 15 language dictionaries in app.js
"""

import sys
import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Extract I18N dictionary
idx_i18n = code.find('const I18N = {')
idx_i18n_end = code.find('};\n\n  // Helper for current i18n text', idx_i18n)
i18n_block = code[idx_i18n:idx_i18n_end]

def extract_keys(lang):
    m = re.search(r'\b' + lang + r':\s*\{([\s\S]*?)\n    \},?', i18n_block)
    if not m:
        return set()
    block = m.group(1)
    keys = re.findall(r'^\s*([a-zA-Z0-9_]+)\s*:', block, re.MULTILINE)
    return set(keys)

langs = ['id', 'en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it']
id_keys = extract_keys('id')

print(f"ID Base Keys Count: {len(id_keys)}\n")
all_good = True

for lang in langs:
    keys = extract_keys(lang)
    missing = id_keys - keys
    extra = keys - id_keys
    status = "OK" if len(missing) == 0 else "FAIL"
    print(f"[{status}] {lang.upper():<3}: {len(keys)} keys (Missing: {len(missing)}, Extra: {len(extra)})")
    if missing:
        print(f"       Missing keys in {lang.upper()}: {missing}")
        all_good = False

if all_good:
    print(f"\nALL {len(langs)} LANGUAGES HAVE 100% I18N PARITY!")
else:
    sys.exit(1)
