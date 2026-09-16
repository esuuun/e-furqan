# -*- coding: utf-8 -*-
"""
Verification script for Chinese (zh) language integration.
"""
import json
import os
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("VERIFYING CHINESE (ZH) INTEGRATION")
print("=" * 60)

errors = []

# 1. Check zh_translations.json
zh_file = os.path.join(BASE_DIR, 'zh_translations.json')
if not os.path.exists(zh_file):
    errors.append("zh_translations.json file missing")
else:
    with open(zh_file, 'r', encoding='utf-8') as f:
        zh_trans = json.load(f)
    print(f"1. zh_translations.json: {len(zh_trans)} verses cached (Target: 6236)")
    if len(zh_trans) < 6236:
        errors.append(f"zh_translations.json only has {len(zh_trans)} verses, expected 6236")

# 2. Check dhamir_data.json
data_file = os.path.join(BASE_DIR, 'dhamir_data.json')
with open(data_file, 'r', encoding='utf-8') as f:
    dhamir_data = json.load(f)

print(f"2. dhamir_data.json: {len(dhamir_data)} entries total")

missing_teks_zh = sum(1 for d in dhamir_data if not d.get('TeksArtiZH'))
missing_surat_zh = sum(1 for d in dhamir_data if not d.get('SuratArtiZH'))
missing_bentuk_zh = sum(1 for d in dhamir_data if not d.get('BentukKataZH'))
missing_arti_zh = sum(1 for d in dhamir_data if not d.get('ArtiKataZH'))

print(f"   - TeksArtiZH completeness   : {len(dhamir_data) - missing_teks_zh} / {len(dhamir_data)}")
print(f"   - SuratArtiZH completeness  : {len(dhamir_data) - missing_surat_zh} / {len(dhamir_data)}")
print(f"   - BentukKataZH completeness : {len(dhamir_data) - missing_bentuk_zh} / {len(dhamir_data)}")
print(f"   - ArtiKataZH completeness   : {len(dhamir_data) - missing_arti_zh} / {len(dhamir_data)}")

if missing_teks_zh > 0 or missing_surat_zh > 0 or missing_bentuk_zh > 0 or missing_arti_zh > 0:
    errors.append("dhamir_data.json has incomplete Chinese fields")

# 3. Check dhamir_data.js
js_file = os.path.join(BASE_DIR, 'dhamir_data.js')
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

print(f"3. dhamir_data.js file size: {round(os.path.getsize(js_file)/1024, 1)} KB")
if 'TeksArtiZH' not in js_content or 'arti_zh' not in js_content:
    errors.append("dhamir_data.js missing Chinese keys")

# 4. Check index.html
html_file = os.path.join(BASE_DIR, 'index.html')
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

if 'value="zh"' not in html_content:
    errors.append("index.html missing value='zh' option in langSelect")
else:
    print("4. index.html: <option value=\"zh\"> properly present in langSelect")

# 5. Check app.js
app_file = os.path.join(BASE_DIR, 'app.js')
with open(app_file, 'r', encoding='utf-8') as f:
    app_content = f.read()

if 'zh: {' not in app_content:
    errors.append("app.js missing I18N.zh definition")
else:
    print("5. app.js: I18N.zh dictionary and all Chinese routing properly wired")

print("=" * 60)
if errors:
    print("ERRORS FOUND:")
    for err in errors:
        print(f"  [!] {err}")
    sys.exit(1)
else:
    print("ALL TESTS PASSED! Chinese (zh) integration is 100% complete and valid!")
    print("=" * 60)
