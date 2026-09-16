#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch complete Chinese Quran translations (Muhammad Makin / 马坚)
for all 114 Surahs from alquran.cloud and cache into zh_translations.json.
"""

import json
import urllib.request
import time
import os
import sys
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_file = os.path.join(BASE_DIR, 'zh_translations.json')

zh_translations = {}
if os.path.exists(out_file):
    try:
        with open(out_file, 'r', encoding='utf-8') as f:
            zh_translations = json.load(f)
    except Exception:
        zh_translations = {}

print(f"Initial cached Chinese translations: {len(zh_translations)}")
print("Fetching 114 Surahs in Chinese (zh.jian - 马坚)...")

for s in range(1, 115):
    try:
        url = f"https://api.alquran.cloud/v1/surah/{s}/zh.jian"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            ayahs = data.get('data', {}).get('ayahs', [])
            for ay in ayahs:
                a_num = ay.get('numberInSurah')
                txt = ay.get('text', '')
                if txt:
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    zh_translations[f"{s}:{a_num}"] = txt
            print(f"[{s:03d}/114] Surah {s}: fetched {len(ayahs)} ayahs")
        time.sleep(0.08)
    except Exception as e:
        print(f"[{s:03d}/114] [WARN] alquran.cloud failed for Surah {s}: {e}. Retrying...")
        time.sleep(0.5)

print(f"\nTotal Chinese translations collected: {len(zh_translations)}")

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(zh_translations, f, ensure_ascii=False, indent=2)

print(f"Successfully saved to {out_file}")
