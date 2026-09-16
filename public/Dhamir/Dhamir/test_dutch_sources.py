import urllib.request
import json
import re

print("1. Testing Quran.com Dutch translation (id=235):")
try:
    url = "https://api.quran.com/api/v4/verses/by_chapter/1?translations=235&per_page=10"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for v in data.get('verses', []):
            text = v['translations'][0]['text']
            clean = re.sub(r'<[^>]*>', '', text).strip()
            print(f"  {v['verse_key']}: {clean}")
except Exception as e:
    print("  Failed:", e)

print("\n2. Testing GitHub Dutch Siregar raw sources:")
gh_urls = [
    "https://raw.githubusercontent.com/semarketir/quranjson/master/source/surah/surah_1.json",
    "https://raw.githubusercontent.com/Ghamdi/Quran-Translations/master/nl.siregar.txt"
]
for u in gh_urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            print(f"  Found {u} ({len(content)} bytes)")
    except Exception as e:
        print(f"  {u} error: {e}")
