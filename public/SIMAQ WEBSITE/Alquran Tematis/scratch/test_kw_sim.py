import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = json.load(open('data.json', encoding='utf-8'))

terms = ['drunk', 'mabuk', 'khamr', 'khamar', 'memabukkan']

matched_uraian = []
matched_verses = {}

for tema, pbs in d.items():
    for pb, spbs in pbs.items():
        for spb, urs in spbs.items():
            for ur, urData in urs.items():
                u_text = f"{ur} {spb} {pb} {tema}".lower()
                if any(t in u_text for t in terms):
                    matched_uraian.append(ur)
                for v in urData.get('verses', []):
                    v_key = f"{v.get('surah_num')}:{v.get('ayat_num')}"
                    indo_text = v.get('indo', '').lower()
                    arab_text = v.get('arab', '')
                    name_text = v.get('surah_name', '').lower()
                    if any(t in indo_text or t in name_text or t in arab_text for t in terms):
                        matched_verses[v_key] = (v.get('surah_name'), v.get('surah_num'), v.get('ayat_num'), indo_text[:60])

print(f"Matched Uraian ({len(matched_uraian)}):")
for u in matched_uraian:
    print(' -', u)

print(f"\nMatched Verses ({len(matched_verses)}):")
for k, val in list(matched_verses.items())[:15]:
    print(f" - QS {val[0]} [{val[1]}]:{val[2]} -> {val[3]}...")
