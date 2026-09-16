import json
import urllib.request
import time
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

unique_verses = sorted(list(set(f"{item['SURAT']}:{item['AYAT']}" for item in raw_data if item.get('SURAT') and item.get('AYAT'))), key=lambda x: (int(x.split(':')[0]), int(x.split(':')[1])))

print(f"Total unique verses: {len(unique_verses)}")

fr_translations = {}

# Try to fetch from alquran.cloud and fallback to quran.com
for idx, v_key in enumerate(unique_verses):
    s, a = v_key.split(':')
    text = None
    
    # 1. Try alquran.cloud
    try:
        url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/fr.hamidullah"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get('data') and res['data'].get('text'):
                text = res['data']['text']
    except Exception as e:
        print(f"[{idx+1}/{len(unique_verses)}] alquran.cloud failed for {v_key}: {e}")
    
    # 2. Fallback to quran.com
    if not text:
        try:
            url = f"https://api.quran.com/api/v4/verses/by_key/{s}:{a}?translations=136"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('verse') and res['verse'].get('translations'):
                    raw_html = res['verse']['translations'][0]['text']
                    # strip html tags if any
                    clean_txt = re.sub(r'<[^>]+>', '', raw_html).strip()
                    text = clean_txt
        except Exception as e:
            print(f"[{idx+1}/{len(unique_verses)}] quran.com failed for {v_key}: {e}")
            
    if text:
        # Clean up any excessive spaces / footnotes
        text = re.sub(r'\s+', ' ', text).strip()
        fr_translations[v_key] = text
        print(f"[{idx+1}/{len(unique_verses)}] {v_key} -> {text[:45]}...")
    else:
        print(f"FAILED to fetch {v_key}!")
        
    time.sleep(0.08)

out_file = os.path.join(BASE_DIR, 'fr_translations.json')
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(fr_translations, f, ensure_ascii=False, indent=2)

print(f"Saved {len(fr_translations)} translations to {out_file}")
