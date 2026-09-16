#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fetch Japanese Quran translation (Ryoichi Mita / 日本ムスリム協会)
from api.alquran.cloud and save to ja_translations.json.
"""

import os
import sys
import json
import urllib.request
import urllib.error

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

OUTPUT_FILE = 'ja_translations.json'
EDITION = 'ja.japanese'
API_URL = f'https://api.alquran.cloud/v1/quran/{EDITION}'

def fetch_japanese_translations():
    print(f"Fetching Japanese Quran translations from: {API_URL}")
    req = urllib.request.Request(API_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"[ERROR] Failed to fetch: {e}")
        sys.exit(1)
        
    if data.get('code') != 200 or 'data' not in data:
        print(f"[ERROR] Invalid API response: {data}")
        sys.exit(1)
        
    translations = {}
    total_ayahs = 0
    
    for surah in data['data']['surahs']:
        s_num = surah['number']
        for ayah in surah['ayahs']:
            a_num = ayah['numberInSurah']
            text = ayah['text'].strip()
            key = f"{s_num}:{a_num}"
            translations[key] = text
            total_ayahs += 1
            
    print(f"Successfully processed {total_ayahs} verses for Japanese (ja).")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
        
    print(f"Saved Japanese translations to {OUTPUT_FILE} (Size: {os.path.getsize(OUTPUT_FILE):,} bytes)")

if __name__ == '__main__':
    fetch_japanese_translations()
