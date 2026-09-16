import openpyxl
import json
import os
import sys
import urllib.request
import time
import re
from collections import defaultdict

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load existing caches
def load_all_caches():
    caches = {
        'verse': {},
        'en': {},
        'ms': {},
        'fr': {},
        'de': {},
        'ur': {},
        'hi': {},
        'bn': {},
        'ru': {},
        'zh': {},
        'es': {},
        'tr': {},
        'pt': {}
    }
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json',
        'ru': 'ru_translations.json',
        'zh': 'zh_translations.json',
        'es': 'es_translations.json',
        'tr': 'tr_translations.json',
        'pt': 'pt_translations.json'
    }
    for k, fn in files.items():
        fp = os.path.join(BASE_DIR, fn)
        if os.path.exists(fp):
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    caches[k] = json.load(f)
            except Exception as e:
                print(f"Error loading {fn}: {e}")
    return caches

caches = load_all_caches()

# 2. Select top 5 shortest verses per word from Harf Ghair Amil
wb = openpyxl.load_workbook(os.path.join(BASE_DIR, 'KAMUS Harf Ghair Amil.xlsx'), data_only=True)
ws = wb['KAMUS KATA']
rows = list(ws.iter_rows(values_only=True))

def standardize_cat(raw_b):
    raw_b = str(raw_b).strip() if raw_b else ''
    if raw_b.startswith('1.'): return '1. Harf Nafyi'
    if raw_b.startswith('2.'): return '2. Harf Tahqiq Taswif'
    if raw_b.startswith('3.'): return '3. Harf Syarat'
    if raw_b.startswith('4.'): return '4. Harf Mashdariyah'
    if raw_b.startswith('5.'): return '5. Harf Zaidah'
    if 'ISTIFHAM' in raw_b.upper(): return '6. Harf Istifham'
    if 'JAWAB' in raw_b.upper(): return '7. Harf Jawab'
    if 'IBTIDA' in raw_b.upper(): return '8. Harf Ibtida\''
    if 'TAFSHIL' in raw_b.upper(): return '9. Harf Tafshil'
    if 'MUFAJAAH' in raw_b.upper(): return '10. Harf Mufaja\'ah'
    if 'MUFASSIRAH' in raw_b.upper(): return '11. Harf Mufassirah'
    if 'ISTIFTAHIYAH' in raw_b.upper(): return '12. Harf Istiftahiyah'
    if 'RADA' in raw_b.upper(): return '13. Harf Rada\''
    if 'TA\'AJUB' in raw_b.upper() or 'TAAJUB' in raw_b.upper(): return '14. Harf Ta\'ajjub'
    if 'FARIQAH' in raw_b.upper(): return '15. Harf Fariqah'
    if 'MAUTHI' in raw_b.upper(): return '16. Harf Mauthi\'ah'
    if 'MABANY' in raw_b.upper(): return '17. Harf Mabany'
    return raw_b

groups = defaultdict(list)
seen = set()
for r in rows[1:]:
    if not any(r): continue
    b, nk, k, ak, fk, s, a, jlh = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    if not b or nk is None or s is None or a is None: continue
    std_b = standardize_cat(b)
    nk_str = str(nk).strip()
    try:
        s_int, a_int = int(s), int(a)
    except:
        continue
    ref_key = (std_b, nk_str, s_int, a_int)
    if ref_key in seen: continue
    seen.add(ref_key)
    
    v_key = f"{s_int}:{a_int}"
    t_arab = caches['verse'].get(v_key, {}).get('TeksArab', '')
    arab_len = len(t_arab) if t_arab else (jlh if jlh is not None else 999)
    groups[(std_b, nk_str)].append({
        'Bentuk': std_b,
        'No': nk_str,
        'Kata': str(k).strip() if k else '',
        'Arti': str(ak).strip() if ak else '',
        'Frek': fk,
        'SURAT': s_int,
        'AYAT': a_int,
        'arab_len': arab_len
    })

selected_items = []
for (b, nk), items in sorted(groups.items(), key=lambda x: (int(x[0][0].split('.')[0]), int(x[0][1]))):
    sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
    selected_items.extend(sorted_items[:5])

needed_verses = sorted(list(set((it['SURAT'], it['AYAT']) for it in selected_items)), key=lambda x: (x[0], x[1]))
print(f"Total selected items: {len(selected_items)} from {len(groups)} words")
print(f"Total unique verses needed: {len(needed_verses)}")

# 3. Check what is missing in verse_cache and each language
missing_verse_cache = [v for v in needed_verses if f"{v[0]}:{v[1]}" not in caches['verse']]
print(f"Missing in verse_cache.json: {len(missing_verse_cache)}")

# Fetch missing verses for verse_cache from equran.id / alquran.cloud
surahs_to_fetch = sorted(list(set(v[0] for v in missing_verse_cache)))
print(f"Surahs to fetch from equran.id: {surahs_to_fetch}")

for s in surahs_to_fetch:
    try:
        url = f"https://equran.id/api/v2/surat/{s}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            for ay in res['data']['ayat']:
                a_num = ay['nomorAyat']
                v_key = f"{s}:{a_num}"
                audio_url = ay.get('audio', {}).get('05', f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a_num:03d}.mp3")
                caches['verse'][v_key] = {
                    'TeksArab': ay.get('teksArab', ''),
                    'TeksLatin': ay.get('teksLatin', ''),
                    'TeksArtiID': ay.get('teksIndonesia', ''),
                    'TeksArti': ay.get('teksIndonesia', ''),
                    'AudioUrl': audio_url
                }
        print(f"Fetched equran.id for surah {s}")
    except Exception as e:
        print(f"Failed equran.id for surah {s}: {e}")
    time.sleep(0.1)

# Check single missing fallback
for s, a in missing_verse_cache:
    v_key = f"{s}:{a}"
    if v_key not in caches['verse'] or not caches['verse'][v_key].get('TeksArab'):
        try:
            url_g = f"https://api.quran.gading.dev/surah/{s}/{a}"
            req_g = urllib.request.Request(url_g, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_g, timeout=10) as resp_g:
                res_g = json.loads(resp_g.read().decode('utf-8'))['data']
                caches['verse'][v_key] = {
                    'TeksArab': res_g['text']['arab'],
                    'TeksLatin': res_g['text']['transliteration']['en'],
                    'TeksArtiID': res_g['translation']['id'],
                    'TeksArti': res_g['translation']['id'],
                    'AudioUrl': f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a:03d}.mp3"
                }
                print(f"Fallback fetched verse {v_key}")
        except Exception as eg:
            print(f"Failed fallback for {v_key}: {eg}")

# 4. Check & Fetch Translations for all languages
edition_map = {
    'en': 'en.sahih',
    'ms': 'ms.basmeih',
    'fr': 'fr.hamidullah',
    'de': 'de.bubenheim',
    'ur': 'ur.jalandhry',
    'hi': 'hi.farooq',
    'bn': 'bn.bengali',
    'ru': 'ru.kuliev',
    'zh': 'zh.jian',
    'es': 'es.garcia',
    'tr': 'tr.diyanet',
    'pt': 'pt.elhayek'
}

for lang, edition in edition_map.items():
    missing_for_lang = [v for v in needed_verses if f"{v[0]}:{v[1]}" not in caches[lang] or not caches[lang][f"{v[0]}:{v[1]}"]]
    print(f"Lang {lang} ({edition}): missing {len(missing_for_lang)} verses")
    
    if missing_for_lang:
        # Group by surah to fetch in bulk if possible, or fetch ayah
        for s, a in missing_for_lang:
            v_key = f"{s}:{a}"
            try:
                url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/{edition}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    res = json.loads(resp.read().decode('utf-8'))
                    if res.get('data') and res['data'].get('text'):
                        caches[lang][v_key] = res['data']['text'].strip()
            except Exception as e:
                # Fallback for Spanish or others
                if lang == 'es':
                    try:
                        url2 = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/es.cortes"
                        req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req2, timeout=10) as resp2:
                            res2 = json.loads(resp2.read().decode('utf-8'))
                            if res2.get('data') and res2['data'].get('text'):
                                caches[lang][v_key] = res2['data']['text'].strip()
                    except:
                        pass
            time.sleep(0.04)
        print(f"Completed fetching for {lang}: total in cache = {len(caches[lang])}")

# Save updated caches
files = {
    'verse': 'verse_cache.json',
    'en': 'en_translations.json',
    'ms': 'ms_translations.json',
    'fr': 'fr_translations.json',
    'de': 'de_translations.json',
    'ur': 'ur_translations.json',
    'hi': 'hi_translations.json',
    'bn': 'bn_translations.json',
    'ru': 'ru_translations.json',
    'zh': 'zh_translations.json',
    'es': 'es_translations.json',
    'tr': 'tr_translations.json',
    'pt': 'pt_translations.json'
}
for k, fn in files.items():
    with open(os.path.join(BASE_DIR, fn), 'w', encoding='utf-8') as f:
        json.dump(caches[k], f, ensure_ascii=False, indent=2)

print("\n[SUCCESS] All caches successfully updated and saved!")
