#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Verification Suite for Persian / Farsi (FA) Integration
"""

import json
import os
import sys
import subprocess

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
passed = 0
failed = 0

def check(condition, msg):
    global passed, failed
    if condition:
        print(f"  [PASS] {msg}")
        passed += 1
    else:
        print(f"  [FAIL] {msg}")
        failed += 1

print("=" * 70)
print("VERIFYING PERSIAN / FARSI (FA) INTEGRATION")
print("=" * 70)

# 1. Verifying fa_translations.json
print("\n1. Verifying fa_translations.json...")
fa_path = os.path.join(BASE_DIR, 'fa_translations.json')
check(os.path.exists(fa_path), "fa_translations.json exists")

if os.path.exists(fa_path):
    with open(fa_path, 'r', encoding='utf-8') as f:
        fa_trans = json.load(f)
    check(len(fa_trans) == 6236, f"fa_translations.json has 6236 verses (got {len(fa_trans)})")
    check('1:1' in fa_trans and len(fa_trans['1:1']) > 0, f"Verse 1:1 present: {fa_trans.get('1:1')}")
    check('112:1' in fa_trans and len(fa_trans['112:1']) > 0, f"Verse 112:1 present: {fa_trans.get('112:1')}")

# 2. Verifying dhamir_data.json and dhamir_data.js
print("\n2. Verifying dhamir_data.json and dhamir_data.js...")
dhamir_json_path = os.path.join(BASE_DIR, 'dhamir_data.json')
if os.path.exists(dhamir_json_path):
    with open(dhamir_json_path, 'r', encoding='utf-8') as f:
        dhamir_data = json.load(f)
    check(len(dhamir_data) > 0, f"dhamir_data.json loaded {len(dhamir_data)} items")
    
    missing_b = sum(1 for d in dhamir_data if not d.get('BentukKataFA'))
    missing_s = sum(1 for d in dhamir_data if not d.get('SuratArtiFA'))
    missing_a = sum(1 for d in dhamir_data if not d.get('ArtiKataFA'))
    missing_t = sum(1 for d in dhamir_data if not d.get('TeksArtiFA'))
    missing_desc = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('desc_fa'))
    missing_jenis = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('jenis_fa'))

    check(missing_b == 0, f"Dhamir BentukKataFA complete ({missing_b} missing)")
    check(missing_s == 0, f"Dhamir SuratArtiFA complete ({missing_s} missing)")
    check(missing_a == 0, f"Dhamir ArtiKataFA complete ({missing_a} missing)")
    check(missing_t == 0, f"Dhamir TeksArtiFA complete ({missing_t} missing)")
    check(missing_desc == 0, f"Dhamir Grammar.desc_fa complete ({missing_desc} missing)")
    check(missing_jenis == 0, f"Dhamir Grammar.jenis_fa complete ({missing_jenis} missing)")

# 3. Verifying harf_data.json and harf_data.js
print("\n3. Verifying harf_data.json and harf_data.js...")
harf_json_path = os.path.join(BASE_DIR, 'harf_data.json')
if os.path.exists(harf_json_path):
    with open(harf_json_path, 'r', encoding='utf-8') as f:
        harf_data = json.load(f)
    check(len(harf_data) > 0, f"harf_data.json loaded {len(harf_data)} items")
    
    missing_hb = sum(1 for d in harf_data if not d.get('BentukKataFA'))
    missing_hs = sum(1 for d in harf_data if not d.get('SuratArtiFA'))
    missing_ha = sum(1 for d in harf_data if not d.get('ArtiKataFA'))
    missing_ht = sum(1 for d in harf_data if not d.get('TeksArtiFA'))
    missing_hdesc = sum(1 for d in harf_data if not d.get('Grammar', {}).get('desc_fa'))
    missing_hjenis = sum(1 for d in harf_data if not d.get('Grammar', {}).get('jenis_fa'))

    check(missing_hb == 0, f"Harf BentukKataFA complete ({missing_hb} missing)")
    check(missing_hs == 0, f"Harf SuratArtiFA complete ({missing_hs} missing)")
    check(missing_ha == 0, f"Harf ArtiKataFA complete ({missing_ha} missing)")
    check(missing_ht == 0, f"Harf TeksArtiFA complete ({missing_ht} missing)")
    check(missing_hdesc == 0, f"Harf Grammar.desc_fa complete ({missing_hdesc} missing)")
    check(missing_hjenis == 0, f"Harf Grammar.jenis_fa complete ({missing_hjenis} missing)")

# 4. Verifying index.html
print("\n4. Verifying index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html_content = f.read()
check('value="fa"' in html_content, 'index.html has <option value="fa">فارسی</option>')

# 5. Verifying app.js
print("\n5. Verifying app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

check("'fa'" in app_js, "app.js contains 'fa' lang key")
check("fa: {" in app_js, "app.js contains I18N.fa definition")
check("ناصر مکارم شیرازی" in app_js, "app.js has Naser Makarem Shirazi translation source")
check("bentuk_fa:" in app_js, "app.js has bentuk_fa mapping")
check("arti_fa:" in app_js, "app.js has arti_fa mapping")
check("suratArtiFA:" in app_js, "app.js has suratArtiFA mapping")
check("teksArtiFA:" in app_js, "app.js has teksArtiFA mapping")
check("getSpeechVoiceAndLang" in app_js and "fa-IR" in app_js, "app.js has getSpeechVoiceAndLang('fa')")
check("state.lang === 'fa'" in app_js, "app.js has state.lang === 'fa' conditional logic")

# 6. Checking JavaScript Syntax via Node.js
print("\n6. Checking JavaScript Syntax via Node.js...")
for js_file in ['app.js', 'dhamir_data.js', 'harf_data.js']:
    res = subprocess.run(['node', '-c', os.path.join(BASE_DIR, js_file)], capture_output=True, text=True)
    check(res.returncode == 0, f"{js_file} syntax valid (exit code {res.returncode})")

print("\n" + "=" * 70)
print(f"SUMMARY: {passed} PASSED, {failed} FAILED")
print("=" * 70)

if failed > 0:
    sys.exit(1)
