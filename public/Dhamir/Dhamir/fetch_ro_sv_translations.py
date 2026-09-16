#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch complete Romanian (ro.grigore) and Swedish (sv.bernstrom) Quran translations
for all 114 Surahs (6,236 verses) and cache into ro_translations.json and sv_translations.json.
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

targets = [
    ('ro', 'ro.grigore', 'ro_translations.json', 'George Grigore (Română)'),
    ('sv', 'sv.bernstrom', 'sv_translations.json', 'Knut Bernström (Svenska)')
]

for lang, edition_id, out_filename, title in targets:
    out_file = os.path.join(BASE_DIR, out_filename)
    translations = {}
    
    if os.path.exists(out_file):
        try:
            with open(out_file, 'r', encoding='utf-8') as f:
                translations = json.load(f)
            if len(translations) == 6236:
                print(f"[{lang.upper()}] Cache {out_filename} already has all 6,236 verses!")
                continue
        except Exception:
            translations = {}
            
    print(f"\n=======================================================")
    print(f"Fetching complete 114 Surahs in {lang.upper()} ({edition_id} - {title})...")
    print(f"=======================================================")
    
    # Try bulk fetch first
    try:
        url = f"https://api.alquran.cloud/v1/quran/{edition_id}"
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
                        translations[f"{s_num}:{a_num}"] = txt
            print(f"Bulk fetch successful! Total ayahs: {len(translations)}")
    except Exception as e:
        print(f"Bulk fetch failed: {e}. Falling back to per-surah fetch...")
        
    if len(translations) < 6236:
        for s in range(1, 115):
            url = f"https://api.alquran.cloud/v1/surah/{s}/{edition_id}"
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    ayahs = data.get('data', {}).get('ayahs', [])
                    for ay in ayahs:
                        a_num = ay.get('numberInSurah')
                        txt = ay.get('text', '')
                        if txt:
                            txt = re.sub(r'\s+', ' ', txt).strip()
                            translations[f"{s}:{a_num}"] = txt
                    print(f"[{s:03d}/114] Surah {s}: fetched {len(ayahs)} ayahs")
                time.sleep(0.05)
            except Exception as e:
                print(f"[{s:03d}/114] [WARN] Failed for Surah {s}: {e}. Retrying...")
                time.sleep(0.5)
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        data = json.loads(resp.read().decode('utf-8'))
                        ayahs = data.get('data', {}).get('ayahs', [])
                        for ay in ayahs:
                            a_num = ay.get('numberInSurah')
                            txt = ay.get('text', '')
                            if txt:
                                txt = re.sub(r'\s+', ' ', txt).strip()
                                translations[f"{s}:{a_num}"] = txt
                        print(f"[{s:03d}/114] Surah {s} (Retry successful): fetched {len(ayahs)} ayahs")
                except Exception as e2:
                    print(f"[{s:03d}/114] [ERROR] Retry failed for Surah {s}: {e2}")

    print(f"Total {lang.upper()} translations collected: {len(translations)}")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_file}")

print("\nAll Romanian and Swedish translations successfully fetched and cached!")
