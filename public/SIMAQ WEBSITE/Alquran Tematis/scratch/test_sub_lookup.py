import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sub_list = []
for tema, pbs in data.items():
    for pb, spbs in pbs.items():
        for spb, urs in spbs.items():
            total_verses = sum(len(urData.get('verses', [])) for urData in urs.values())
            sub_list.append({
                'tema': tema,
                'pokok': pb,
                'sub': spb,
                'uraianCount': len(urs),
                'verseCount': total_verses
            })

def find_sub(q):
    clean = q.lower().strip()
    # 1. exact
    for s in sub_list:
        if s['sub'].lower() == clean:
            return s
    # 2. starts with
    for s in sub_list:
        if s['sub'].lower().startswith(clean):
            return s
    # 3. substring
    for s in sub_list:
        if clean in s['sub'].lower():
            return s
    return None

test_queries = ['1.1.1', '1.1.1.Persaksian Tauhid', 'Persaksian Tauhid', '9.5.2', 'Waris', 'Hudaibiyah']
for q in test_queries:
    found = find_sub(q)
    print(f'Query: "{q}" -> Found: "{found["sub"] if found else None}"')
    if found:
        print(f'    Path: [{found["tema"]}] > [{found["pokok"]}] ({found["uraianCount"]} Uraian, {found["verseCount"]} Verses)')
