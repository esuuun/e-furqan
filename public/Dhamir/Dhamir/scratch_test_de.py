import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Test alquran cloud API with de.bubenheim and de.aburida
test_verse = "1:5"
for ed in ["de.bubenheim", "de.aburida"]:
    url = f"https://api.alquran.cloud/v1/ayah/{test_verse}/{ed}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"alquran.cloud {ed} result:", res['data']['text'])
    except Exception as e:
        print(f"alquran.cloud {ed} error:", e)

# Test quran.com api with translation 208 and 27
for tid in [208, 27]:
    try:
        url2 = f"https://api.quran.com/api/v4/verses/by_key/1:5?translations={tid}"
        req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            res2 = json.loads(resp2.read().decode('utf-8'))
            if res2.get('verse') and res2['verse'].get('translations'):
                print(f"quran.com tid={tid} result:", res2['verse']['translations'][0]['text'])
    except Exception as e:
        print(f"quran.com tid={tid} error:", e)
