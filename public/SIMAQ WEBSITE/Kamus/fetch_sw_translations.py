#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch complete Swahili Quran translations (Ali Muhsin Al-Barwani)
for all 114 Surahs from alquran.cloud and cache into sw_translations.json.
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
out_file = os.path.join(BASE_DIR, 'sw_translations.json')

sw_translations = {}
if os.path.exists(out_file):
    try:
        with open(out_file, 'r', encoding='utf-8') as f:
            sw_translations = json.load(f)
    except Exception:
        sw_translations = {}

print(f"Initial cached Swahili translations: {len(sw_translations)}")

# Try fetching entire Quran in single bulk request first
try:
    print("Attempting bulk download of entire Quran in Swahili (sw.barwani)...")
    url = "https://api.alquran.cloud/v1/quran/sw.barwani"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        surahs = data.get('data', {}).get('surahs', [])
        for s_obj in surahs:
            s_num = s_obj.get('number')
            for ay in s_obj.get('ayahs', []):
                a_num = ay.get('numberInSurah')
                txt = ay.get('text', '')
                if txt:
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    sw_translations[f"{s_num}:{a_num}"] = txt
        print(f"Bulk download successful! Total verses collected: {len(sw_translations)}")
except Exception as e:
    print(f"Bulk download failed ({e}). Falling back to per-surah fetching...")

# Fallback: per-surah fetching if any missing
if len(sw_translations) < 6236:
    for s in range(1, 115):
        # Check if surah already completely loaded
        surah_keys = [k for k in sw_translations if k.startswith(f"{s}:")]
        if len(surah_keys) > 0 and len(sw_translations) >= 6236:
            continue

        try:
            url = f"https://api.alquran.cloud/v1/surah/{s}/sw.barwani"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                ayahs = data.get('data', {}).get('ayahs', [])
                for ay in ayahs:
                    a_num = ay.get('numberInSurah')
                    txt = ay.get('text', '')
                    if txt:
                        txt = re.sub(r'\s+', ' ', txt).strip()
                        sw_translations[f"{s}:{a_num}"] = txt
                print(f"[{s:03d}/114] Surah {s}: fetched {len(ayahs)} ayahs")
            time.sleep(0.05)
        except Exception as e:
            print(f"[{s:03d}/114] [WARN] Failed for Surah {s}: {e}. Retrying...")
            time.sleep(0.5)
            try:
                url = f"https://api.alquran.cloud/v1/surah/{s}/sw.barwani"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    ayahs = data.get('data', {}).get('ayahs', [])
                    for ay in ayahs:
                        a_num = ay.get('numberInSurah')
                        txt = ay.get('text', '')
                        if txt:
                            txt = re.sub(r'\s+', ' ', txt).strip()
                            sw_translations[f"{s}:{a_num}"] = txt
                    print(f"[{s:03d}/114] Surah {s} (Retry successful): fetched {len(ayahs)} ayahs")
            except Exception as e2:
                print(f"[{s:03d}/114] [ERROR] Retry failed for Surah {s}: {e2}")

print(f"\nTotal Swahili translations collected: {len(sw_translations)}")

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(sw_translations, f, ensure_ascii=False, indent=2)

print(f"Successfully saved to {out_file}")
