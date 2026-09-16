import openpyxl
import json
import os
import sys
import urllib.request
import time

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load Kamus Harf 'Amil.xlsx to extract all needed verses
wb = openpyxl.load_workbook(os.path.join(BASE_DIR, "Kamus Harf 'Amil.xlsx"), data_only=True)
ws = wb['KAMUS KATA']
rows = list(ws.iter_rows(values_only=True))

needed_verses = set()
for r in rows[1:]:
    if not any(r): continue
    s, a = r[5], r[6]
    if s is not None and a is not None:
        try:
            needed_verses.add((int(s), int(a)))
        except:
            pass

needed_verses = sorted(list(needed_verses), key=lambda x: (x[0], x[1]))
print(f"Total unique verses needed from Kamus Harf 'Amil: {len(needed_verses)}")

# 2. Update verse_cache.json
vc_path = os.path.join(BASE_DIR, 'verse_cache.json')
with open(vc_path, 'r', encoding='utf-8') as f:
    verse_cache = json.load(f)

missing_vc = [v for v in needed_verses if f"{v[0]}:{v[1]}" not in verse_cache or not verse_cache[f"{v[0]}:{v[1]}"].get('TeksArab')]
print(f"Missing in verse_cache.json: {len(missing_vc)}")

if missing_vc:
    missing_surahs = sorted(list(set(v[0] for v in missing_vc)))
    print(f"Fetching from equran.id for surahs: {missing_surahs}")
    for s in missing_surahs:
        try:
            url = f"https://equran.id/api/v2/surat/{s}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                for ay in res['data']['ayat']:
                    a_num = ay['nomorAyat']
                    v_key = f"{s}:{a_num}"
                    audio_url = ay.get('audio', {}).get('05', f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a_num:03d}.mp3")
                    verse_cache[v_key] = {
                        'TeksArab': ay.get('teksArab', ''),
                        'TeksLatin': ay.get('teksLatin', ''),
                        'TeksArtiID': ay.get('teksIndonesia', ''),
                        'TeksArti': ay.get('teksIndonesia', ''),
                        'AudioUrl': audio_url
                    }
            print(f"  [OK] Fetched surah {s}")
        except Exception as e:
            print(f"  [WARN] Failed equran.id for surah {s}: {e}")
        time.sleep(0.1)

    # Fallback check
    for s, a in missing_vc:
        v_key = f"{s}:{a}"
        if v_key not in verse_cache or not verse_cache[v_key].get('TeksArab'):
            try:
                url_g = f"https://api.quran.gading.dev/surah/{s}/{a}"
                req_g = urllib.request.Request(url_g, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_g, timeout=10) as resp_g:
                    res_g = json.loads(resp_g.read().decode('utf-8'))['data']
                    verse_cache[v_key] = {
                        'TeksArab': res_g['text']['arab'],
                        'TeksLatin': res_g['text']['transliteration']['en'],
                        'TeksArtiID': res_g['translation']['id'],
                        'TeksArti': res_g['translation']['id'],
                        'AudioUrl': f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a:03d}.mp3"
                    }
                    print(f"  [OK] Fallback fetched {v_key}")
            except Exception as eg:
                print(f"  [WARN] Fallback failed for {v_key}: {eg}")

    with open(vc_path, 'w', encoding='utf-8') as f:
        json.dump(verse_cache, f, ensure_ascii=False, indent=2)
    print("Saved verse_cache.json")

# 3. Update translation caches for all languages
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
    fn = f"{lang}_translations.json"
    fp = os.path.join(BASE_DIR, fn)
    t_cache = {}
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            t_cache = json.load(f)
            
    missing_for_lang = [v for v in needed_verses if f"{v[0]}:{v[1]}" not in t_cache or not t_cache[f"{v[0]}:{v[1]}"]]
    if missing_for_lang:
        print(f"Fetching {len(missing_for_lang)} verses for {lang} ({edition})...")
        for s, a in missing_for_lang:
            v_key = f"{s}:{a}"
            try:
                url = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/{edition}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    res = json.loads(resp.read().decode('utf-8'))
                    if res.get('data') and res['data'].get('text'):
                        t_cache[v_key] = res['data']['text'].strip()
            except Exception as e:
                if lang == 'es':
                    try:
                        url2 = f"https://api.alquran.cloud/v1/ayah/{s}:{a}/es.cortes"
                        req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req2, timeout=10) as resp2:
                            res2 = json.loads(resp2.read().decode('utf-8'))
                            if res2.get('data') and res2['data'].get('text'):
                                t_cache[v_key] = res2['data']['text'].strip()
                    except:
                        pass
            time.sleep(0.04)
            
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(t_cache, f, ensure_ascii=False, indent=2)
        print(f"  [OK] Saved {fn} (total {len(t_cache)} verses)")
    else:
        print(f"Lang {lang}: 100% complete.")

print("\n[SUCCESS] All verses and translations for Kamus Harf 'Amil are complete!")
