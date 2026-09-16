import urllib.request
import json

def test_trans(text, tl='en'):
    prefix = ""
    import re
    m = re.match(r"^([\d.]+\s*)(.*)$", text)
    if m:
        prefix = m.group(1)
        query = m.group(2).strip()
    else:
        query = text.strip()
    url = f"https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=id&tl={tl}&dt=t&q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return prefix + "".join([item[0] for item in data[0]])
    except Exception as e:
        return f"ERR: {e}"

tests = [
    "1. Nama dan Sifat Allah",
    "1.1.Sifat 1-6",
    "1.1.1.Persaksian Tauhid",
    "1.1.1.1. Tauhid itu fitrah manusia",
    "Al-Qur'an Tematis",
    "Sub Pokok Bahasan",
    "Tema",
    "Pokok",
    "Uraian",
    "Pelajari selengkapnya di tautan berikut:"
]

for t in tests:
    print(f"'{t}' -> '{test_trans(t)}'")
