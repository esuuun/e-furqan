#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Verification Suite for Korean (KO) Integration
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
print("VERIFYING KOREAN (KO) INTEGRATION")
print("=" * 70)

# 1. Verifying ko_translations.json
print("\n1. Verifying ko_translations.json...")
ko_path = os.path.join(BASE_DIR, 'ko_translations.json')
check(os.path.exists(ko_path), "ko_translations.json exists")

if os.path.exists(ko_path):
    with open(ko_path, 'r', encoding='utf-8') as f:
        ko_trans = json.load(f)
    check(len(ko_trans) == 6236, f"ko_translations.json has 6236 verses (got {len(ko_trans)})")
    check('1:1' in ko_trans and len(ko_trans['1:1']) > 0, f"Verse 1:1 present: {ko_trans.get('1:1')}")
    check('112:1' in ko_trans and len(ko_trans['112:1']) > 0, f"Verse 112:1 present: {ko_trans.get('112:1')}")

# 2. Verifying dhamir_data.json and dhamir_data.js
print("\n2. Verifying dhamir_data.json and dhamir_data.js...")
dhamir_json_path = os.path.join(BASE_DIR, 'dhamir_data.json')
if os.path.exists(dhamir_json_path):
    with open(dhamir_json_path, 'r', encoding='utf-8') as f:
        dhamir_data = json.load(f)
    check(len(dhamir_data) > 0, f"dhamir_data.json loaded {len(dhamir_data)} items")
    
    missing_b = sum(1 for d in dhamir_data if not d.get('BentukKataKO'))
    missing_s = sum(1 for d in dhamir_data if not d.get('SuratArtiKO'))
    missing_a = sum(1 for d in dhamir_data if not d.get('ArtiKataKO'))
    missing_t = sum(1 for d in dhamir_data if not d.get('TeksArtiKO'))
    missing_desc = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('desc_ko'))
    missing_jenis = sum(1 for d in dhamir_data if not d.get('Grammar', {}).get('jenis_ko'))

    check(missing_b == 0, f"Dhamir BentukKataKO complete ({missing_b} missing)")
    check(missing_s == 0, f"Dhamir SuratArtiKO complete ({missing_s} missing)")
    check(missing_a == 0, f"Dhamir ArtiKataKO complete ({missing_a} missing)")
    check(missing_t == 0, f"Dhamir TeksArtiKO complete ({missing_t} missing)")
    check(missing_desc == 0, f"Dhamir Grammar.desc_ko complete ({missing_desc} missing)")
    check(missing_jenis == 0, f"Dhamir Grammar.jenis_ko complete ({missing_jenis} missing)")

# 3. Verifying harf_data.json and harf_data.js
print("\n3. Verifying harf_data.json and harf_data.js...")
harf_json_path = os.path.join(BASE_DIR, 'harf_data.json')
if os.path.exists(harf_json_path):
    with open(harf_json_path, 'r', encoding='utf-8') as f:
        harf_data = json.load(f)
    check(len(harf_data) > 0, f"harf_data.json loaded {len(harf_data)} items")
    
    missing_hb = sum(1 for d in harf_data if not d.get('BentukKataKO'))
    missing_hs = sum(1 for d in harf_data if not d.get('SuratArtiKO'))
    missing_ha = sum(1 for d in harf_data if not d.get('ArtiKataKO'))
    missing_ht = sum(1 for d in harf_data if not d.get('TeksArtiKO'))
    missing_hdesc = sum(1 for d in harf_data if not d.get('Grammar', {}).get('desc_ko'))
    missing_hjenis = sum(1 for d in harf_data if not d.get('Grammar', {}).get('jenis_ko'))

    check(missing_hb == 0, f"Harf BentukKataKO complete ({missing_hb} missing)")
    check(missing_hs == 0, f"Harf SuratArtiKO complete ({missing_hs} missing)")
    check(missing_ha == 0, f"Harf ArtiKataKO complete ({missing_ha} missing)")
    check(missing_ht == 0, f"Harf TeksArtiKO complete ({missing_ht} missing)")
    check(missing_hdesc == 0, f"Harf Grammar.desc_ko complete ({missing_hdesc} missing)")
    check(missing_hjenis == 0, f"Harf Grammar.jenis_ko complete ({missing_hjenis} missing)")

# 4. Verifying index.html
print("\n4. Verifying index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html_content = f.read()
check('value="ko"' in html_content, 'index.html has <option value="ko">한국어</option>')

# 5. Verifying app.js
print("\n5. Verifying app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

check("'ko'" in app_js, "app.js contains 'ko' lang key")
check("ko: {" in app_js, "app.js contains I18N.ko definition")
check("최영길" in app_js or "Hamid Choi" in app_js, "app.js has Hamid Choi translation source")
check("bentuk_ko" in app_js, "app.js has bentuk_ko mapping")
check("arti_ko" in app_js, "app.js has arti_ko mapping")
check("suratArtiKO" in app_js, "app.js has suratArtiKO mapping")
check("teksArtiKO" in app_js, "app.js has teksArtiKO mapping")
check("getSpeechVoiceAndLang" in app_js and "ko-KR" in app_js, "app.js has getSpeechVoiceAndLang('ko')")
check("state.lang === 'ko'" in app_js, "app.js has state.lang === 'ko' conditional logic")

# 6. Checking JavaScript Syntax via Node.js
print("\n6. Checking JavaScript Syntax via Node.js...")
try:
    res_app = subprocess.run(['node', '-c', 'app.js'], capture_output=True, text=True, cwd=BASE_DIR)
    check(res_app.returncode == 0, f"app.js syntax valid (exit code {res_app.returncode})")
    
    res_dhamir = subprocess.run(['node', '-c', 'dhamir_data.js'], capture_output=True, text=True, cwd=BASE_DIR)
    check(res_dhamir.returncode == 0, f"dhamir_data.js syntax valid (exit code {res_dhamir.returncode})")
    
    res_harf = subprocess.run(['node', '-c', 'harf_data.js'], capture_output=True, text=True, cwd=BASE_DIR)
    check(res_harf.returncode == 0, f"harf_data.js syntax valid (exit code {res_harf.returncode})")
except Exception as e:
    check(False, f"Node.js check failed: {e}")

print("\n" + "=" * 70)
print(f"SUMMARY: {passed} PASSED, {failed} FAILED")
print("=" * 70)

if failed > 0:
    sys.exit(1)
