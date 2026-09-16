import json
import urllib.request
import time
import os
import sys
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("FETCHING BANGLA (BN) QURAN TRANSLATIONS (Muhiuddin Khan)")
print("=" * 60)

# Load existing verses needed from dhamir_data.json
verse_keys = set()
data_path = os.path.join(BASE_DIR, 'dhamir_data.json')
if os.path.exists(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    for item in raw_data:
        s = item.get('SURAT')
        a = item.get('AYAT')
        if s and a:
            verse_keys.add(f"{s}:{a}")

unique_surahs = sorted(list(set(int(k.split(':')[0]) for k in verse_keys)))
print(f"Total Unique Verses needed: {len(verse_keys)}")
print(f"Total Unique Surahs to fetch: {len(unique_surahs)}")

# Load existing translations
bn_cache_path = os.path.join(BASE_DIR, 'bn_translations.json')
bn_translations = {}
if os.path.exists(bn_cache_path):
    try:
        with open(bn_cache_path, 'r', encoding='utf-8') as f:
            bn_translations = json.load(f)
        print(f"Existing translations: {len(bn_translations)}")
    except Exception:
        bn_translations = {}

# Check which surahs have missing verses
missing_surahs = []
for s in unique_surahs:
    needed_in_s = [vk for vk in verse_keys if vk.startswith(f"{s}:")]
    if any(vk not in bn_translations or not bn_translations[vk] for vk in needed_in_s):
        missing_surahs.append(s)

print(f"Surahs to fetch: {len(missing_surahs)} / {len(unique_surahs)}")

edition_id = 'bn.bengali'

for idx, s in enumerate(missing_surahs, 1):
    try:
        url = f"https://api.alquran.cloud/v1/surah/{s}/{edition_id}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            ayahs = data.get('data', {}).get('ayahs', [])
            for ay in ayahs:
                a_num = ay.get('numberInSurah')
                txt = ay.get('text', '')
                if txt:
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    bn_translations[f"{s}:{a_num}"] = txt
            print(f"  ({idx}/{len(missing_surahs)}) Surah {s}: fetched {len(ayahs)} ayahs")
        time.sleep(0.05)
    except Exception as e:
        print(f"  [ERROR] Failed Surah {s}: {e}")
        time.sleep(0.3)

# Save cache
with open(bn_cache_path, 'w', encoding='utf-8') as f:
    json.dump(bn_translations, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(bn_translations)} Bangla translations to bn_translations.json")

# Verify all needed verses are present
missing = [vk for vk in verse_keys if vk not in bn_translations or not bn_translations[vk]]
if missing:
    print(f"[WARN] Still missing {len(missing)} verses: {missing[:10]}")
else:
    print("SUCCESS: 100% of required Bangla translations fetched!")
