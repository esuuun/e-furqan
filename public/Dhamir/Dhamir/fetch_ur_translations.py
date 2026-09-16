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

ur_translations = {}

def fetch_single_verse(v_key):
    s, a = v_key.split(':')
    text = None
    
    # 1. Try alquran.cloud with ur.jalandhry (Fateh Muhammad Jalandhry)
    try:
        url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/ur.jalandhry"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get('data') and res['data'].get('text'):
                text = res['data']['text']
    except Exception:
        pass
    
    # 2. Try alquran.cloud with ur.maududi
    if not text:
        try:
            url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/ur.maududi"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('data') and res['data'].get('text'):
                    text = res['data']['text']
        except Exception:
            pass

    # 3. Try alquran.cloud with ur.ahmedali
    if not text:
        try:
            url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/ur.ahmedali"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('data') and res['data'].get('text'):
                    text = res['data']['text']
        except Exception:
            pass

    # 4. Fallback to quran.com API (ur translation id = 97 or 234)
    if not text:
        try:
            url = f"https://api.quran.com/api/v4/verses/by_key/{s}:{a}?translations=97"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if res.get('verse') and res['verse'].get('translations'):
                    raw_html = res['verse']['translations'][0]['text']
                    clean_txt = re.sub(r'<[^>]+>', '', raw_html).strip()
                    text = clean_txt
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
            ur_translations[v_key] = text
            if completed_count % 10 == 0 or completed_count == len(unique_verses):
                print(f"[{completed_count}/{len(unique_verses)}] Fetched {v_key} -> {text[:30]}...")
        else:
            print(f"[{completed_count}/{len(unique_verses)}] FAILED for {v_key}")

out_file = os.path.join(BASE_DIR, 'ur_translations.json')
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(ur_translations, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(ur_translations)} Urdu translations to {out_file}")
