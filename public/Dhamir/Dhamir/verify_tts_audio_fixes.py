#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Suite for Audio & TTS fixes (Hausa, Swahili, Persian)
"""

import os
import sys
import json
import urllib.request
import urllib.parse
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
print("VERIFYING TTS & AUDIO ENGINE FIXES (HAUSA, SWAHILI, PERSIAN)")
print("=" * 70)

# 1. Check EveryAyah Persian Recitation Endpoint (Makarem Shirazi)
print("\n1. Verifying Persian Recitation Audio (EveryAyah)...")
for sa in ['001001', '001002', '112001']:
    url = f'https://everyayah.com/data/translations/Makarem_Kabiri_16Kbps/{sa}.mp3'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=10)
        check(res.status == 200 and len(res.read()) > 10000, f"Makarem Shirazi Persian Audio {sa} accessible ({res.status})")
    except Exception as e:
        check(False, f"Makarem Shirazi Persian Audio {sa} failed: {e}")

# 2. Check Google Cloud Native TTS for Hausa
print("\n2. Verifying Hausa Native Cloud TTS...")
ha_text = "Da sunan Allah Mai rahama Mai jin kai"
ha_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=ha&client=tw-ob&q=" + urllib.parse.quote(ha_text)
try:
    req = urllib.request.Request(ha_url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, timeout=10)
    data = res.read()
    check(res.status == 200 and len(data) > 5000, f"Hausa Native Cloud TTS stream accessible ({len(data)} bytes)")
except Exception as e:
    check(False, f"Hausa Native Cloud TTS failed: {e}")

# 3. Check Google Cloud Native TTS for Swahili
print("\n3. Verifying Swahili Native Cloud TTS...")
sw_text = "Kwa jina la Mwenyezi Mungu Mwingi wa rehema Mwenye kurehemu"
sw_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=sw&client=tw-ob&q=" + urllib.parse.quote(sw_text)
try:
    req = urllib.request.Request(sw_url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, timeout=10)
    data = res.read()
    check(res.status == 200 and len(data) > 5000, f"Swahili Native Cloud TTS stream accessible ({len(data)} bytes)")
except Exception as e:
    check(False, f"Swahili Native Cloud TTS failed: {e}")

# 4. Check Google Cloud Native TTS for Turkish
print("\n4. Verifying Turkish Native Cloud TTS...")
tr_text = "O, eğlence için değildir."
tr_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=tr&client=tw-ob&q=" + urllib.parse.quote(tr_text)
try:
    req = urllib.request.Request(tr_url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, timeout=10)
    data = res.read()
    check(res.status == 200 and len(data) > 5000, f"Turkish Native Cloud TTS stream accessible ({len(data)} bytes)")
except Exception as e:
    check(False, f"Turkish Native Cloud TTS failed: {e}")

# 5. Check Google Cloud Native TTS for Dutch
print("\n5. Verifying Dutch Native Cloud TTS...")
nl_text = "In de naam van Allah, de Erbarmer, de Meest Barmhartige."
nl_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=nl&client=tw-ob&q=" + urllib.parse.quote(nl_text)
try:
    req = urllib.request.Request(nl_url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, timeout=10)
    data = res.read()
    check(res.status == 200 and len(data) > 5000, f"Dutch Native Cloud TTS stream accessible ({len(data)} bytes)")
except Exception as e:
    check(False, f"Dutch Native Cloud TTS failed: {e}")

# 6. Check Google Cloud Native TTS for Italian
print("\n6. Verifying Italian Native Cloud TTS...")
it_text = "In nome di Allah, il Compassionevole, il Misericordioso"
it_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=it&client=tw-ob&q=" + urllib.parse.quote(it_text)
try:
    req = urllib.request.Request(it_url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, timeout=10)
    data = res.read()
    check(res.status == 200 and len(data) > 5000, f"Italian Native Cloud TTS stream accessible ({len(data)} bytes)")
except Exception as e:
    check(False, f"Italian Native Cloud TTS failed: {e}")

# 4. Check app.js audio functions implementation
print("\n4. Verifying app.js audio functions implementation...")
with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

check('Makarem_Kabiri_16Kbps' in app_js, "app.js contains Makarem_Kabiri_16Kbps EveryAyah audio")
check('Fooladvand_Hedayatfar_40Kbps' in app_js, "app.js contains Fooladvand EveryAyah fallback")
check('getGoogleTtsUrls' in app_js, "app.js contains getGoogleTtsUrls chunking helper")
check('playCloudAudioQueue' in app_js, "app.js contains playCloudAudioQueue helper")
check('currentCloudAudio' in app_js, "app.js manages currentCloudAudio state")
check('hasNativeVoice' in app_js, "app.js checks hasNativeVoice for smart fallbacks")

# 5. Check JS syntax validation
print("\n5. Checking JS syntax via node...")
res_app = subprocess.run(['node', '-c', 'app.js'], capture_output=True, text=True, cwd=BASE_DIR)
check(res_app.returncode == 0, f"app.js syntax valid (exit code {res_app.returncode})")

print("\n" + "=" * 70)
print(f"SUMMARY: {passed} PASSED, {failed} FAILED")
print("=" * 70)

if failed > 0:
    sys.exit(1)
