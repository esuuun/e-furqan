#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Hausa (ha) Integration in Dhamir & Harf Kamus App
"""

import os
import sys
import json
import re
import subprocess

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
passed = 0
failed = 0

def check(condition, desc):
    global passed, failed
    if condition:
        print(f"  [PASS] {desc}")
        passed += 1
    else:
        print(f"  [FAIL] {desc}")
        failed += 1

print("=" * 70)
print("VERIFYING HAUSA (HA) INTEGRATION")
print("=" * 70)

# 1. Check ha_translations.json
print("\n1. Verifying ha_translations.json...")
ha_path = os.path.join(BASE_DIR, 'ha_translations.json')
check(os.path.exists(ha_path), "ha_translations.json exists")
with open(ha_path, 'r', encoding='utf-8') as f:
    ha_trans = json.load(f)
check(len(ha_trans) == 6236, f"ha_translations.json has 6236 verses (got {len(ha_trans)})")
check(bool(ha_trans.get("1:1")), f"Verse 1:1 present: {ha_trans.get('1:1')}")
check(bool(ha_trans.get("112:1")), f"Verse 112:1 present: {ha_trans.get('112:1')}")

# 2. Check dhamir_data.json & dhamir_data.js
print("\n2. Verifying dhamir_data.json and dhamir_data.js...")
with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    d_json = json.load(f)
check(len(d_json) > 0, f"dhamir_data.json loaded {len(d_json)} items")

missing_d_bentuk = sum(1 for x in d_json if not x.get('BentukKataHA'))
missing_d_surat = sum(1 for x in d_json if not x.get('SuratArtiHA'))
missing_d_arti = sum(1 for x in d_json if not x.get('ArtiKataHA'))
missing_d_teks = sum(1 for x in d_json if not x.get('TeksArtiHA'))
missing_d_desc = sum(1 for x in d_json if not x.get('Grammar', {}).get('desc_ha'))
missing_d_jenis = sum(1 for x in d_json if not x.get('Grammar', {}).get('jenis_ha'))

check(missing_d_bentuk == 0, f"Dhamir BentukKataHA complete (0 missing)")
check(missing_d_surat == 0, f"Dhamir SuratArtiHA complete (0 missing)")
check(missing_d_arti == 0, f"Dhamir ArtiKataHA complete (0 missing)")
check(missing_d_teks == 0, f"Dhamir TeksArtiHA complete (0 missing)")
check(missing_d_desc == 0, f"Dhamir Grammar.desc_ha complete (0 missing)")
check(missing_d_jenis == 0, f"Dhamir Grammar.jenis_ha complete (0 missing)")

# 3. Check harf_data.json & harf_data.js
print("\n3. Verifying harf_data.json and harf_data.js...")
with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
    h_json = json.load(f)
check(len(h_json) > 0, f"harf_data.json loaded {len(h_json)} items")

missing_h_bentuk = sum(1 for x in h_json if not x.get('BentukKataHA'))
missing_h_surat = sum(1 for x in h_json if not x.get('SuratArtiHA'))
missing_h_arti = sum(1 for x in h_json if not x.get('ArtiKataHA'))
missing_h_teks = sum(1 for x in h_json if not x.get('TeksArtiHA'))
missing_h_desc = sum(1 for x in h_json if not x.get('Grammar', {}).get('desc_ha'))
missing_h_jenis = sum(1 for x in h_json if not x.get('Grammar', {}).get('jenis_ha'))

check(missing_h_bentuk == 0, f"Harf BentukKataHA complete (0 missing)")
check(missing_h_surat == 0, f"Harf SuratArtiHA complete (0 missing)")
check(missing_h_arti == 0, f"Harf ArtiKataHA complete (0 missing)")
check(missing_h_teks == 0, f"Harf TeksArtiHA complete (0 missing)")
check(missing_h_desc == 0, f"Harf Grammar.desc_ha complete (0 missing)")
check(missing_h_jenis == 0, f"Harf Grammar.jenis_ha complete (0 missing)")

# 4. Check index.html
print("\n4. Verifying index.html...")
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()
check('<option value="ha">NG Hausa</option>' in html, "index.html has <option value=\"ha\">NG Hausa</option>")

# 5. Check app.js
print("\n5. Verifying app.js...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

check("'ha'" in app_js, "app.js contains 'ha' lang key")
check("ha: {" in app_js, "app.js contains I18N.ha definition")
check("Sheikh Abubakar Mahmoud Gumi" in app_js, "app.js has Abubakar Gumi translation source")
check("bentuk_ha:" in app_js, "app.js has bentuk_ha mapping")
check("arti_ha:" in app_js, "app.js has arti_ha mapping")
check("suratArtiHA:" in app_js, "app.js has suratArtiHA mapping")
check("teksArtiHA:" in app_js, "app.js has teksArtiHA mapping")
check("langKey === 'ha'" in app_js, "app.js has getSpeechVoiceAndLang('ha')")
check("state.lang === 'ha'" in app_js, "app.js has state.lang === 'ha' conditional logic")

# Check Node.js syntax validation
print("\n6. Checking JavaScript Syntax via Node.js...")
try:
    res = subprocess.run(["node", "-c", "app.js"], capture_output=True, text=True, cwd=BASE_DIR)
    check(res.returncode == 0, f"app.js syntax valid (exit code 0)")
    if res.returncode != 0:
        print("  Error output:", res.stderr)
except Exception as e:
    print(f"  [WARN] Could not run node: {e}")

try:
    res = subprocess.run(["node", "-c", "dhamir_data.js"], capture_output=True, text=True, cwd=BASE_DIR)
    check(res.returncode == 0, f"dhamir_data.js syntax valid (exit code 0)")
except Exception as e:
    pass

try:
    res = subprocess.run(["node", "-c", "harf_data.js"], capture_output=True, text=True, cwd=BASE_DIR)
    check(res.returncode == 0, f"harf_data.js syntax valid (exit code 0)")
except Exception as e:
    pass

print("\n" + "=" * 70)
print(f"SUMMARY: {passed} PASSED, {failed} FAILED")
print("=" * 70)

if failed > 0:
    sys.exit(1)
