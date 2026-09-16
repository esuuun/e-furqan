#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch complete Bosnian Quran translations (Besim Korkut - bs.korkut)
for all 114 Surahs (6,236 verses) and cache into bs_translations.json.
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
out_file = os.path.join(BASE_DIR, 'bs_translations.json')

bs_translations = {}

print("Fetching complete 114 Surahs in Bosnian (bs.korkut - Besim Korkut)...")

try:
    url = "https://api.alquran.cloud/v1/quran/bs.korkut"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=35) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        surahs = data.get('data', {}).get('surahs', [])
        for s_obj in surahs:
            s_num = s_obj.get('number')
            for ay in s_obj.get('ayahs', []):
                a_num = ay.get('numberInSurah')
                txt = ay.get('text', '')
                if txt:
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    bs_translations[f"{s_num}:{a_num}"] = txt
        print(f"Bulk fetch successful! Total ayahs: {len(bs_translations)}")
except Exception as e:
    print(f"Bulk fetch failed: {e}. Falling back to per-surah fetch...")

if len(bs_translations) < 6236:
    for s in range(1, 115):
        try:
            url = f"https://api.alquran.cloud/v1/surah/{s}/bs.korkut"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                ayahs = data.get('data', {}).get('ayahs', [])
                for ay in ayahs:
                    a_num = ay.get('numberInSurah')
                    txt = ay.get('text', '')
                    if txt:
                        txt = re.sub(r'\s+', ' ', txt).strip()
                        bs_translations[f"{s}:{a_num}"] = txt
                print(f"[{s:03d}/114] Surah {s}: fetched {len(ayahs)} ayahs")
            time.sleep(0.05)
        except Exception as e:
            print(f"[{s:03d}/114] [WARN] Failed for Surah {s}: {e}. Retrying...")
            time.sleep(0.5)
            try:
                url = f"https://api.alquran.cloud/v1/surah/{s}/bs.korkut"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    ayahs = data.get('data', {}).get('ayahs', [])
                    for ay in ayahs:
                        a_num = ay.get('numberInSurah')
                        txt = ay.get('text', '')
                        if txt:
                            txt = re.sub(r'\s+', ' ', txt).strip()
                            bs_translations[f"{s}:{a_num}"] = txt
                    print(f"[{s:03d}/114] Surah {s} (Retry successful): fetched {len(ayahs)} ayahs")
            except Exception as e2:
                print(f"[{s:03d}/114] [ERROR] Retry failed for Surah {s}: {e2}")

print(f"\nTotal Bosnian translations collected: {len(bs_translations)}")

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(bs_translations, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(bs_translations)} ayahs to {out_file}")
