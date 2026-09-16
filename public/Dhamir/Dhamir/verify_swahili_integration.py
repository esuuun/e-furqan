#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Verification Suite for Swahili (SW / Kiswahili) Integration
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
print("VERIFYING SWAHILI (SW) INTEGRATION")
print("=" * 70)

# 1. Verifying sw_translations.json
print("\n1. Verifying sw_translations.json...")
sw_path = os.path.join(BASE_DIR, 'sw_translations.json')
check(os.path.exists(sw_path), "sw_translations.json exists")

if os.path.exists(sw_path):
    with open(sw_path, 'r', encoding='utf-8') as f:
        sw_trans = json.load(f)
    check(len(sw_trans) == 6236, f"sw_translations.json has 6236 verses (got {len(sw_trans)})")
    check('1:1' in sw_trans and len(sw_trans['1:1']) > 0, f"Verse 1:1 present: {sw_trans.get('1:1')}")
    check('112:1' in sw_trans and len(sw_trans['112:1']) > 0, f"Verse 112:1 present: {sw_trans.get('112:1')}")

# 2. Verifying dhamir_data.json and dhamir_data.js
print("\n2. Verifying dhamir_data.json and dhamir_data.js...")
dhamir_json_path = os.path.join(BASE_DIR, 'dhamir_data.json')
if os.path.exists(dhamir_json_path):
    with open(dhamir_json_path, 'r', encoding='utf-8') as f:
        dhamir_data = json.load(f)
    check(len(dhamir_data) > 0, f"dhamir_data.json loaded {len(dhamir_data)} items")
    
    missing_b = sum(1 for d in dhamir_data if not d.get('BentukKataSW'))
    missing_s = sum(1 for d in dhamir_data if not d.get('SuratArtiSW'))
    missing_a = sum(1 for d in dhamir_data if not d.get('ArtiKataSW'))
    missing_t = sum(1 for d in dhamir_data if not d.get('TeksArtiSW'))
    missing_desc = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('desc_sw'))
    missing_jenis = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('jenis_sw'))

    check(missing_b == 0, f"Dhamir BentukKataSW complete ({missing_b} missing)")
    check(missing_s == 0, f"Dhamir SuratArtiSW complete ({missing_s} missing)")
    check(missing_a == 0, f"Dhamir ArtiKataSW complete ({missing_a} missing)")
    check(missing_t == 0, f"Dhamir TeksArtiSW complete ({missing_t} missing)")
    check(missing_desc == 0, f"Dhamir Grammar.desc_sw complete ({missing_desc} missing)")
    check(missing_jenis == 0, f"Dhamir Grammar.jenis_sw complete ({missing_jenis} missing)")

# 3. Verifying harf_data.json and harf_data.js
print("\n3. Verifying harf_data.json and harf_data.js...")
harf_json_path = os.path.join(BASE_DIR, 'harf_data.json')
if os.path.exists(harf_json_path):
    with open(harf_json_path, 'r', encoding='utf-8') as f:
        harf_data = json.load(f)
    check(len(harf_data) > 0, f"harf_data.json loaded {len(harf_data)} items")
    
    missing_hb = sum(1 for d in harf_data if not d.get('BentukKataSW'))
    missing_hs = sum(1 for d in harf_data if not d.get('SuratArtiSW'))
    missing_ha = sum(1 for d in harf_data if not d.get('ArtiKataSW'))
    missing_ht = sum(1 for d in harf_data if not d.get('TeksArtiSW'))
    missing_hdesc = sum(1 for d in harf_data if not d.get('Grammar', {}).get('desc_sw'))
    missing_hjenis = sum(1 for d in harf_data if not d.get('Grammar', {}).get('jenis_sw'))

    check(missing_hb == 0, f"Harf BentukKataSW complete ({missing_hb} missing)")
    check(missing_hs == 0, f"Harf SuratArtiSW complete ({missing_hs} missing)")
    check(missing_ha == 0, f"Harf ArtiKataSW complete ({missing_ha} missing)")
    check(missing_ht == 0, f"Harf TeksArtiSW complete ({missing_ht} missing)")
    check(missing_hdesc == 0, f"Harf Grammar.desc_sw complete ({missing_hdesc} missing)")
    check(missing_hjenis == 0, f"Harf Grammar.jenis_sw complete ({missing_hjenis} missing)")

# 4. Verifying index.html
print("\n4. Verifying index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html_content = f.read()
check('value="sw"' in html_content, 'index.html has <option value="sw">Kiswahili</option>')

# 5. Verifying app.js
print("\n5. Verifying app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

check("'sw'" in app_js, "app.js contains 'sw' lang key")
check("sw: {" in app_js, "app.js contains I18N.sw definition")
check("Ali Muhsin Al-Barwani" in app_js, "app.js has Ali Muhsin Al-Barwani translation source")
check("bentuk_sw:" in app_js, "app.js has bentuk_sw mapping")
check("arti_sw:" in app_js, "app.js has arti_sw mapping")
check("suratArtiSW:" in app_js, "app.js has suratArtiSW mapping")
check("teksArtiSW:" in app_js, "app.js has teksArtiSW mapping")
check("getSpeechVoiceAndLang" in app_js and "sw-TZ" in app_js, "app.js has getSpeechVoiceAndLang('sw')")
check("state.lang === 'sw'" in app_js, "app.js has state.lang === 'sw' conditional logic")

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
