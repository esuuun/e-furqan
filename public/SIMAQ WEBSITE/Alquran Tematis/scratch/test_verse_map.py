import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

verse_map = {}
for tema, pbs in data.items():
    for pb, spbs in pbs.items():
        for spb, urs in spbs.items():
            for ur, vdata in urs.items():
                for v in vdata.get('verses', []):
                    key = f"{v['surah_num']}:{v['ayat_num']}"
                    if key not in verse_map:
                        verse_map[key] = {
                            'surah_num': v['surah_num'],
                            'surah_name': v['surah_name'],
                            'ayat_num': v['ayat_num'],
                            'arab': v.get('arab', ''),
                            'indo': v.get('indo', ''),
                            'audio': v.get('audio', ''),
                            'topics': []
                        }
                    verse_map[key]['topics'].append({
                        'tema': tema,
                        'pokok': pb,
                        'sub': spb,
                        'uraian': ur
                    })

print(f'Total indexed unique verses: {len(verse_map)}')
multi_topic = [k for k, v in verse_map.items() if len(v['topics']) > 1]
print(f'Verses appearing in multiple topics: {len(multi_topic)}')
sample_key = '2:255'
if sample_key in verse_map:
    print(f'Sample 2:255 topics ({len(verse_map[sample_key]["topics"])}):')
    for t in verse_map[sample_key]['topics']:
        print(f" - Tema: {t['tema']} | Pokok: {t['pokok']} | Sub: {t['sub']} | Uraian: {t['uraian']}")
