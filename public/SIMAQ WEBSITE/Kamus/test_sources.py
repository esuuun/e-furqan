import urllib.request
import json
import re

print("Fetching from Quran.com ID 153 (Italian - Piccardo):")
url = 'https://api.quran.com/api/v4/verses/by_chapter/1?translations=153&per_page=10'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for v in data.get('verses', []):
        text = v['translations'][0]['text']
        clean = re.sub(r'<[^>]*>', '', text).strip()
        print(f"{v['verse_key']}: {clean}")

print("\nFetching from Tanzil for Dutch (Sofian Siregar) and Italian (Piccardo):")
for code, name in [('nl.siregar', 'Dutch'), ('it.piccardo', 'Italian')]:
    try:
        t_url = f"https://tanzil.net/trans/{code}"
        t_req = urllib.request.Request(t_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(t_req, timeout=10) as t_resp:
            lines = t_resp.read().decode('utf-8').splitlines()
            print(f"{name} Tanzil header: {lines[0] if lines else 'empty'}")
            # print verse 1:7 or 2:2
            for l in lines[:15]:
                if '|' in l and not l.startswith('#'):
                    print(f"  {l}")
    except Exception as e:
        print(f"Tanzil error for {code}: {e}")
