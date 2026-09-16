import os
import pandas as pd
import urllib.request
import json
import time

CACHE_FILE = 'quran_cache.json'
quran_cache = {}

if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            raw_cache = json.load(f)
            quran_cache = {int(k): v for k, v in raw_cache.items()}
    except Exception as e:
        print(f"Error loading cache: {e}")
        quran_cache = {}

def get_surah(surah_num):
    if surah_num in quran_cache:
        return quran_cache[surah_num]
    
    url = f"https://equran.id/api/v2/surat/{surah_num}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            quran_cache[surah_num] = data['data']
            print(f"Fetched Surah {surah_num} from API.")
            return quran_cache[surah_num]
    except Exception as e:
        print(f"API Error fetching Surah {surah_num}: {e}")
        return None

import glob
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]

def sort_hierarchy(h):
    if not isinstance(h, dict):
        return h
    if "verses" in h and "is_lihat_juga" in h:
        return h
    sorted_dict = {}
    for k in sorted(h.keys(), key=natural_sort_key):
        sorted_dict[k] = sort_hierarchy(h[k])
    return sorted_dict

def main():
    excel_files = [f for f in glob.glob('*.xlsx') if not f.startswith('~$')]
    excel_files.sort(key=natural_sort_key)
    
    all_dfs = []
    for f in excel_files:
        temp_df = pd.read_excel(f)
        temp_df.columns = temp_df.columns.str.strip().str.lower()
        temp_df.rename(columns={
            'sub pokok bahsan': 'sub pokok bahasan',
            'urian': 'uraian'
        }, inplace=True)
        temp_df = temp_df.ffill()
        all_dfs.append(temp_df)
        
    df = pd.concat(all_dfs, ignore_index=True)

    hierarchy = {}

    for _, row in df.iterrows():
        tema = ' '.join(str(row['tema']).strip().split())
        pb = ' '.join(str(row['pokok bahasan']).strip().split())
        spb = ' '.join(str(row['sub pokok bahasan']).strip().split())
        ur = ' '.join(str(row['uraian']).strip().split())
        
        if 'lihat juga' in ur.lower():
            continue
            
        if tema not in hierarchy:
            hierarchy[tema] = {}
        if pb not in hierarchy[tema]:
            hierarchy[tema][pb] = {}
        if spb not in hierarchy[tema][pb]:
            hierarchy[tema][pb][spb] = {}
        if ur not in hierarchy[tema][pb][spb]:
            hierarchy[tema][pb][spb][ur] = {
                "is_lihat_juga": False,
                "verses": []
            }

        try:
            surat_num = int(row['surat'])
            ayat_num = int(row['ayat'])
        except ValueError:
            continue
            
        surah_data = get_surah(surat_num)
        if not surah_data:
            continue
            
        nama_latin = surah_data['namaLatin']
        
        ayat_data = next((a for a in surah_data['ayat'] if a['nomorAyat'] == ayat_num), None)
        if not ayat_data:
            continue
            
        teks_arab = ayat_data['teksArab']
        teks_indo = ayat_data['teksIndonesia']
        audio_url = ayat_data.get('audio', {}).get('05', '')
        
        hierarchy[tema][pb][spb][ur]["verses"].append({
            "surah_name": nama_latin,
            "surah_num": surat_num,
            "ayat_num": ayat_num,
            "arab": teks_arab,
            "indo": teks_indo,
            "audio": audio_url
        })

    hierarchy = sort_hierarchy(hierarchy)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(hierarchy, f, ensure_ascii=False, indent=2)

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write('window.quranData = ' + json.dumps(hierarchy, ensure_ascii=False) + ';')

    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(quran_cache, f, ensure_ascii=False)
        
    print("Successfully built data.json and data.js!")

if __name__ == '__main__':
    main()
