import urllib.request
import json
import re

url = "https://quranenc.com/api/v1/translation/sura/italian_piccardo/2"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for item in data.get('result', [])[:5]:
        print(f"2:{item['aya']}: {item['translation']}")
