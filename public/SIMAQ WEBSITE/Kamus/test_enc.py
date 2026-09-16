import urllib.request

for name, code in [('Dutch', 'nl.siregar'), ('Italian', 'it.piccardo')]:
    url = f"https://tanzil.net/trans/{code}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req).read()
    
    # Try different encodings
    for enc in ['utf-8', 'iso-8859-1', 'iso-8859-15', 'cp1252', 'latin1']:
        try:
            txt = raw.decode(enc)
            # check verse 2:2 or 2:1
            lines = [l for l in txt.splitlines() if '|' in l and not l.startswith('#')]
            print(f"{name} ({enc}): {lines[1] if len(lines) > 1 else 'N/A'}")
            print(f"  Sample line 2:7 -> {lines[6] if len(lines) > 6 else 'N/A'}")
            break
        except Exception as e:
            pass
