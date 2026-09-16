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

unique_verses = sorted(
    list(set(f"{item['SURAT']}:{item['AYAT']}" for item in raw_data if item.get('SURAT') and item.get('AYAT'))),
    key=lambda x: (int(x.split(':')[0]), int(x.split(':')[1]))
)

print(f"Total unique verses to fetch for Spanish (es.garcia): {len(unique_verses)}")

es_translations = {}

# Check if es_translations.json exists partially
out_file = os.path.join(BASE_DIR, 'es_translations.json')
if os.path.exists(out_file):
    try:
        with open(out_file, 'r', encoding='utf-8') as f:
            es_translations = json.load(f)
        print(f"Loaded {len(es_translations)} existing cached translations from es_translations.json")
    except Exception:
        pass

for idx, v_key in enumerate(unique_verses):
    if v_key in es_translations and es_translations[v_key]:
        continue

    s, a = v_key.split(':')
    text = None
    
    # 1. Try alquran.cloud with es.garcia (Muhammad Isa García)
    try:
        url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/es.garcia"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get('data') and res['data'].get('text'):
                text = res['data']['text']
    except Exception as e:
        pass
    
    # 2. Try alquran.cloud fallback to es.cortes
    if not text:
        try:
            url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/es.cortes"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('data') and res['data'].get('text'):
                    text = res['data']['text']
        except Exception as e:
            pass

    # 3. Fallback to quran.com (translation ID 140 or 83)
    if not text:
        try:
            url = f"https://api.quran.com/api/v4/verses/by_key/{s}:{a}?translations=140"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('verse') and res['verse'].get('translations'):
                    raw_html = res['verse']['translations'][0]['text']
                    clean_txt = re.sub(r'<[^>]+>', '', raw_html).strip()
                    text = clean_txt
        except Exception as e:
            pass

    if text:
        text = re.sub(r'\s+', ' ', text).strip()
        es_translations[v_key] = text
        print(f"[{idx+1}/{len(unique_verses)}] {v_key} -> {text[:55]}...")
    else:
        print(f"[{idx+1}/{len(unique_verses)}] FAILED to fetch {v_key}!")
        
    time.sleep(0.04)

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(es_translations, f, ensure_ascii=False, indent=2)

print(f"\n[DONE] Saved {len(es_translations)} Spanish translations to {out_file}")
