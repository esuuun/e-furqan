import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Test alquran cloud API
test_verse = "1:5"
url = f"https://api.alquran.cloud/v1/ayah/{test_verse}/fr.hamidullah"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("alquran.cloud result:", res['data']['text'])
except Exception as e:
    print("alquran.cloud error:", e)

# Test quran.com api
try:
    url2 = "https://api.quran.com/api/v4/verses/by_key/1:5?translations=136"
    req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req2, timeout=10) as resp2:
        res2 = json.loads(resp2.read().decode('utf-8'))
        print("quran.com result:", res2['verse']['translations'][0]['text'])
except Exception as e:
    print("quran.com error:", e)
