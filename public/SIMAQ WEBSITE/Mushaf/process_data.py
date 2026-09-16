import pandas as pd
import json
import os
import math

try:
    print("Reading excel...")
    df = pd.read_excel('MASTER MUSHAF.xlsx')
    # Fill NaN with empty string
    df = df.fillna('')
    
    # We want to group by SURAT
    # If the column SURAT contains floats or weird strings, clean them up
    # Make sure we have integer representations for Surah
    def safe_int(val):
        try:
            return int(float(val))
        except:
            return str(val)
            
    df['SURAT_ID'] = df['SURAT'].apply(safe_int)
    
    out_dir = 'quran-app/public/data'
    os.makedirs(out_dir, exist_ok=True)
    
    # Also we should create a metadata file containing which Ayahs exist per Surah
    surah_metadata = {}
    
    grouped = df.groupby('SURAT_ID')
    for surah_id, group in grouped:
        if str(surah_id).strip() == '':
            continue
            
        surah_data = {}
        # Group by Ayah within Surah
        group['AYAT_ID'] = group['AYAT'].apply(safe_int)
        ayah_grouped = group.groupby('AYAT_ID')
        
        ayahs_list = []
        for ayah_id, ayah_group in ayah_grouped:
            if str(ayah_id).strip() == '':
                continue
            ayahs_list.append(ayah_id)
            # convert to dict
            records = ayah_group.to_dict(orient='records')
            surah_data[str(ayah_id)] = records
            
        # save surah data to file
        with open(os.path.join(out_dir, f'surah_{surah_id}.json'), 'w', encoding='utf-8') as f:
            json.dump(surah_data, f, ensure_ascii=False)
            
        surah_metadata[str(surah_id)] = sorted(list(set(ayahs_list)))
        print(f"Processed Surah {surah_id} with {len(ayahs_list)} Ayahs")
        
    with open(os.path.join(out_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
        json.dump(surah_metadata, f, ensure_ascii=False)
        
    print("Done processing data!")
except Exception as e:
    print("Error:", e)
