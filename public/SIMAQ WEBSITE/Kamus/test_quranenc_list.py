import urllib.request
import json

url = "https://quranenc.com/api/v1/translation/list"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for item in data.get('translations', []):
            if 'dutch' in item.get('language_iso_code', '').lower() or 'nl' in item.get('language_iso_code', '').lower() or 'dutch' in item.get('language_name', '').lower():
                print(item)
except Exception as e:
    print("QuranEnc list error:", e)
