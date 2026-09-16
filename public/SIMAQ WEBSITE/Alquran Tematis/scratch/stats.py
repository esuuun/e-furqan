import json
import sys

def get_stats():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_temas = len(data)
    total_pb = 0
    total_spb = 0
    total_ur = 0
    total_verses = 0
    surahs_referenced = set()
    surah_distribution = {}

    tema_stats = []

    for tema, pbs in data.items():
        pb_count = len(pbs)
        spb_count = 0
        ur_count = 0
        verse_count = 0
        tema_surahs = set()

        for pb, spbs in pbs.items():
            spb_count += len(spbs)
            for spb, urs in spbs.items():
                ur_count += len(urs)
                for ur, ur_data in urs.items():
                    verses = ur_data.get('verses', [])
                    verse_count += len(verses)
                    for v in verses:
                        s_num = v.get('surah_num')
                        s_name = v.get('surah_name')
                        surahs_referenced.add(s_num)
                        tema_surahs.add(s_num)
                        surah_distribution[s_name] = surah_distribution.get(s_name, 0) + 1

        total_pb += pb_count
        total_spb += spb_count
        total_ur += ur_count
        total_verses += verse_count

        tema_stats.append({
            'tema': tema,
            'pb_count': pb_count,
            'spb_count': spb_count,
            'ur_count': ur_count,
            'verse_count': verse_count,
            'surah_count': len(tema_surahs)
        })

    print("=== SUMMARY STATS ===")
    print(f"Total Temas: {total_temas}")
    print(f"Total Pokok Bahasan: {total_pb}")
    print(f"Total Sub Pokok Bahasan: {total_spb}")
    print(f"Total Uraian: {total_ur}")
    print(f"Total Verses: {total_verses}")
    print(f"Surahs Referenced: {len(surahs_referenced)} / 114")
    print("\n=== PER TEMA STATS ===")
    for ts in tema_stats:
        print(f"- {ts['tema']}: {ts['pb_count']} PB | {ts['spb_count']} SPB | {ts['ur_count']} Uraian | {ts['verse_count']} Verses | {ts['surah_count']} Surahs")

if __name__ == '__main__':
    get_stats()
