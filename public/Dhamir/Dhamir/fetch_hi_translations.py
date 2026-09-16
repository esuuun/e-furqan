import json
import urllib.request
import time
import os
import sys
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

unique_verses = sorted(
    list(set(f"{item['SURAT']}:{item['AYAT']}" for item in raw_data if item.get('SURAT') and item.get('AYAT'))),
    key=lambda x: (int(x.split(':')[0]), int(x.split(':')[1]))
)

print(f"Total unique verses to fetch: {len(unique_verses)}")

hi_translations = {}

def fetch_single_verse(v_key):
    s, a = v_key.split(':')
    text = None
    
    # 1. Try alquran.cloud with hi.hindi (Suhel Farooq Khan & Saifur Rahman Nadwi)
    try:
        url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/hi.hindi"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get('data') and res['data'].get('text'):
                text = res['data']['text']
    except Exception:
        pass
    
    # 2. Try alquran.cloud with hi.farooq (Muhammad Farooq Khan & Muhammad Ahmed)
    if not text:
        try:
            url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/hi.farooq"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('data') and res['data'].get('text'):
                    text = res['data']['text']
        except Exception:
            pass

    # 3. Fallback to quranenc API
    if not text:
        try:
            url = f"https://quranenc.com/api/v1/translation/aya/hindi_omari/{s}/{a}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('result') and res['result'].get('translation'):
                    text = res['result']['translation']
        except Exception:
            pass

    if text:
        text = re.sub(r'\s+', ' ', text).strip()
        return v_key, text
    return v_key, None

# Run concurrent fetch
with ThreadPoolExecutor(max_workers=8) as executor:
    future_to_verse = {executor.submit(fetch_single_verse, v): v for v in unique_verses}
    completed_count = 0
    for future in as_completed(future_to_verse):
        v_key, text = future.result()
        completed_count += 1
        if text:
            hi_translations[v_key] = text
            if completed_count % 10 == 0 or completed_count == len(unique_verses):
                print(f"[{completed_count}/{len(unique_verses)}] Fetched {v_key} -> {text[:35]}...")
        else:
            print(f"[{completed_count}/{len(unique_verses)}] FAILED for {v_key}")

print(f"\nSuccessfully fetched {len(hi_translations)} / {len(unique_verses)} Hindi translations.")

with open(os.path.join(BASE_DIR, 'hi_translations.json'), 'w', encoding='utf-8') as f:
    json.dump(hi_translations, f, ensure_ascii=False, indent=2)

print("Saved hi_translations.json")
