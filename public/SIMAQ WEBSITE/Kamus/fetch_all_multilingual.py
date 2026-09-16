import json
import urllib.request
import time
import os
import sys
import openpyxl
import re

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("FETCHING MULTILINGUAL QURAN TRANSLATIONS (7 LANGUAGES)")
print("=" * 60)

# 1. Read Kamus Jamid Mabny.xlsx and get candidate / shortest verses
wb = openpyxl.load_workbook(os.path.join(BASE_DIR, 'Kamus Jamid Mabny.xlsx'), data_only=True)
sheet = wb['KAMUS KATA']
rows = list(sheet.iter_rows(values_only=True))
header = [str(h).strip() if h else '' for h in rows[0]]

# Group and get top 5 shortest verses per word
from collections import defaultdict
word_groups = defaultdict(list)
seen_refs = set()

# Load verse cache for lengths
verse_cache_path = os.path.join(BASE_DIR, 'verse_cache.json')
verse_cache = {}
if os.path.exists(verse_cache_path):
    with open(verse_cache_path, 'r', encoding='utf-8') as f:
        verse_cache = json.load(f)

for r in rows[1:]:
    if not any(r): continue
    item = dict(zip(header, r))
    b = str(item.get('Bentuk Kata', '')).strip()
    nk = str(item.get('No kata', '')).strip()
    s = item.get('SURAT')
    a = item.get('AYAT')
    
    if not b or not nk or s is None or a is None:
        continue
    try:
        s_int = int(s)
        a_int = int(a)
    except Exception:
        continue

    ref_key = (b, nk, s_int, a_int)
    if ref_key in seen_refs:
        continue
    seen_refs.add(ref_key)

    v_key = f"{s_int}:{a_int}"
    t_arab = verse_cache.get(v_key, {}).get('TeksArab', '')
    word_groups[(b, nk)].append({
        'SURAT': s_int,
        'AYAT': a_int,
        'v_key': v_key,
        'arab_len': len(t_arab) if t_arab else 9999
    })

selected_vkeys = set()
for k, items in word_groups.items():
    sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
    for it in sorted_items[:5]:
        selected_vkeys.add(it['v_key'])

print(f"Total Unique Verses in 5-verse dataset: {len(selected_vkeys)}")

# Also extract unique surahs needed
surahs_needed = sorted(list(set(int(k.split(':')[0]) for k in selected_vkeys)))
print(f"Total Unique Surahs needed: {len(surahs_needed)}")

# 2. Languages to fetch:
# ms: ms.basmeih
# fr: fr.hamidullah
# de: de.bubenheim
# ur: ur.jalandhry
# hi: hi.farooq

editions = {
    'ms': ('ms_translations.json', 'ms.basmeih'),
    'fr': ('fr_translations.json', 'fr.hamidullah'),
    'de': ('de_translations.json', 'de.bubenheim'),
    'ur': ('ur_translations.json', 'ur.jalandhry'),
    'hi': ('hi_translations.json', 'hi.farooq'),
    'bn': ('bn_translations.json', 'bn.bengali'),
    'tr': ('tr_translations.json', 'tr.diyanet'),
    'ha': ('ha_translations.json', 'ha.gumi'),
    'sw': ('sw_translations.json', 'sw.barwani'),
    'fa': ('fa_translations.json', 'fa.makarem')
}

for lang, (fn, edition_id) in editions.items():
    fpath = os.path.join(BASE_DIR, fn)
    t_dict = {}
    if os.path.exists(fpath):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                t_dict = json.load(f)
        except Exception:
            t_dict = {}

    missing_surahs = []
    for s in surahs_needed:
        # Check if all needed ayahs in this surah are present
        needed_in_s = [vk for vk in selected_vkeys if vk.startswith(f"{s}:")]
        if any(vk not in t_dict or not t_dict[vk] for vk in needed_in_s):
            missing_surahs.append(s)

    print(f"\n[{lang.upper()} - {edition_id}] Surahs to fetch: {len(missing_surahs)} / {len(surahs_needed)}")

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
                        # Clean text
                        txt = re.sub(r'\s+', ' ', txt).strip()
                        t_dict[f"{s}:{a_num}"] = txt
                print(f"  ({idx}/{len(missing_surahs)}) Surah {s}: fetched {len(ayahs)} ayahs")
            time.sleep(0.1)
        except Exception as e:
            print(f"  [ERROR] Failed Surah {s} for {lang}: {e}")
            time.sleep(0.5)

    # Save cache file
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(t_dict, f, ensure_ascii=False, indent=2)
    print(f"  -> Saved {len(t_dict)} translations to {fn}")

print("\nMultilingual translation fetching complete!")
