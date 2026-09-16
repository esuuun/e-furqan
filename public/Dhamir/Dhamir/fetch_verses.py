import json
import urllib.request
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/Dhamir/dhamir_data.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries to enrich: {len(data)}")

# Collect unique surahs
surahs_needed = sorted(list(set(int(item['SURAT']) for item in data if item.get('SURAT'))))
print(f"Surahs to fetch: {surahs_needed}")

surah_cache = {}
for s in surahs_needed:
    try:
        url = f"https://equran.id/api/v2/surat/{s}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            surah_cache[s] = {ay['nomorAyat']: ay for ay in res['data']['ayat']}
            print(f"Fetched Surah {s}: {len(surah_cache[s])} ayat")
    except Exception as e:
        print(f"equran.id failed for surah {s}: {e}, trying fallback...")
        surah_cache[s] = {}
    time.sleep(0.15)

for idx, item in enumerate(data):
    s = int(item['SURAT'])
    a = int(item['AYAT'])
    
    if s in surah_cache and a in surah_cache[s]:
        ay_data = surah_cache[s][a]
        item['TeksArab'] = ay_data.get('teksArab', '')
        item['TeksLatin'] = ay_data.get('teksLatin', '')
        item['TeksArti'] = ay_data.get('teksIndonesia', '')
        # Direct audio link from Mishary Rashid Alafasy ('05')
        if 'audio' in ay_data and '05' in ay_data['audio']:
            item['AudioUrl'] = ay_data['audio']['05']
        else:
            s_str = str(s).zfill(3)
            a_str = str(a).zfill(3)
            item['AudioUrl'] = f"https://everyayah.com/data/Alafasy_128kbps/{s_str}{a_str}.mp3"
        print(f"[{idx+1}/{len(data)}] Enriched QS. {s}:{a} | Latin: {item['TeksLatin'][:35]}...")
    else:
        # Fetch individual verse from gading.dev fallback
        try:
            url_g = f"https://api.quran.gading.dev/surah/{s}/{a}"
            req_g = urllib.request.Request(url_g, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_g, timeout=10) as resp_g:
                res_g = json.loads(resp_g.read().decode('utf-8'))['data']
                item['TeksArab'] = res_g['text']['arab']
                item['TeksLatin'] = res_g['text']['transliteration']['en']
                item['TeksArti'] = res_g['translation']['id']
                s_str = str(s).zfill(3)
                a_str = str(a).zfill(3)
                item['AudioUrl'] = f"https://everyayah.com/data/Alafasy_128kbps/{s_str}{a_str}.mp3"
                print(f"[{idx+1}/{len(data)}] Fallback enriched QS. {s}:{a}")
        except Exception as eg:
            print(f"Error on QS. {s}:{a}: {eg}")

with open('d:/Dhamir/dhamir_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved enriched data to dhamir_data.json")
