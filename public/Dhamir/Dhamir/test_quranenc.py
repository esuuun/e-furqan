import urllib.request
import json

print("Testing QuranEnc for Italian Piccardo and Dutch Siregar:")
for tr_key in ['italian_piccardo', 'dutch_siregar', 'dutch_mokhtasar', 'italian_machrafi', 'italian_rida']:
    try:
        url = f"https://quranenc.com/api/v1/translation/sura/{tr_key}/1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"[{tr_key}] SUCCESS! Surah 1 has {len(data.get('result', []))} verses.")
            for row in data.get('result', [])[:3]:
                print(f"  {row.get('aya')}: {row.get('translation')}")
    except Exception as e:
        print(f"[{tr_key}] Failed: {e}")
