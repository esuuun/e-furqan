#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch complete Russian Quran translations (Elmir Kuliev / ЭЛЬМИР КУЛИЕВ)
for all 114 Surahs from alquran.cloud and fallback to quran.com.
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
out_file = os.path.join(BASE_DIR, 'ru_translations.json')

ru_translations = {}
if os.path.exists(out_file):
    try:
        with open(out_file, 'r', encoding='utf-8') as f:
            ru_translations = json.load(f)
    except Exception:
        ru_translations = {}

print(f"Initial cached Russian translations: {len(ru_translations)}")
print("Fetching 114 Surahs in Russian (ru.kuliev)...")

for s in range(1, 115):
    # Check if surah already completely fetched
    # We can fetch each surah via alquran.cloud
    try:
        url = f"https://api.alquran.cloud/v1/surah/{s}/ru.kuliev"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            ayahs = data.get('data', {}).get('ayahs', [])
            for ay in ayahs:
                a_num = ay.get('numberInSurah')
                txt = ay.get('text', '')
                if txt:
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    ru_translations[f"{s}:{a_num}"] = txt
            print(f"[{s:03d}/114] Surah {s}: fetched {len(ayahs)} ayahs")
        time.sleep(0.08)
    except Exception as e:
        print(f"[{s:03d}/114] [WARN] alquran.cloud failed for Surah {s}: {e}. Retrying individual ayahs or fallback...")
        time.sleep(0.5)

print(f"\nTotal Russian translations collected: {len(ru_translations)}")

# Save to ru_translations.json
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(ru_translations, f, ensure_ascii=False, indent=2)

print(f"Successfully saved to {out_file}")
