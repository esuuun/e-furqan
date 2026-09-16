import pandas as pd
import urllib.request
import json
import time
import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sirah Rasulullah - Halaman {PAGE_NUM}</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --text-color: #e2e8f0;
            --card-bg: #111827;
            --card-border: #1e293b;
            --accent: #14b8a6;
            --accent-glow: rgba(20, 184, 166, 0.15);
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 2rem 1rem;
            line-height: 1.7;
            background-image: radial-gradient(circle at 50% 0%, #1e293b 0%, transparent 50%);
        }
        .section-title {
            font-size: 1.35rem;
            font-weight: 600;
            margin-top: 4rem;
            margin-bottom: 2rem;
            display: inline-block;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--accent);
            text-align: left;
            color: #f8fafc;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding-bottom: 4rem;
        }
        .verse-title {
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 1rem;
            color: var(--accent);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .verse-title::before {
            content: '';
            display: block;
            width: 8px;
            height: 8px;
            background-color: var(--accent);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--accent);
        }
        .flip-card {
            background-color: transparent;
            width: 100%;
            perspective: 1000px;
            margin-bottom: 3rem;
            cursor: pointer;
        }
        .flip-card-inner {
            position: relative;
            width: 100%;
            transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
            transform-style: preserve-3d;
            display: grid;
        }
        .flip-card:hover .flip-card-front {
            border-color: #334155;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }
        .flip-card-front, .flip-card-back {
            grid-area: 1 / 1 / 2 / 2;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 3rem;
            box-sizing: border-box;
            border-radius: 20px;
            border: 1px solid var(--card-border);
            transition: border-color 0.3s, box-shadow 0.3s;
        }
        .flip-card-front {
            background: linear-gradient(145deg, #0b1120, #0f172a);
            font-size: 1.15rem;
            text-align: center;
            color: #cbd5e1;
        }
        .flip-card-back {
            background: linear-gradient(145deg, #111827, #0f172a);
            transform: rotateY(180deg);
            font-family: 'Amiri', serif;
            font-size: 2.4rem;
            line-height: 2.2;
            direction: rtl;
            text-align: center;
            border-color: var(--accent);
            box-shadow: 0 0 40px var(--accent-glow);
            color: #f1f5f9;
        }
        .flip-card.flipped .flip-card-inner {
            transform: rotateY(180deg);
        }
        .hint {
            text-align: center;
            font-size: 0.95rem;
            color: #94a3b8;
            margin-bottom: 3rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background: #1e293b;
            padding: 0.75rem 1.5rem;
            border-radius: 999px;
            width: fit-content;
            margin-left: auto;
            margin-right: auto;
            border: 1px solid #334155;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(148, 163, 184, 0.2); }
            70% { box-shadow: 0 0 0 10px rgba(148, 163, 184, 0); }
            100% { box-shadow: 0 0 0 0 rgba(148, 163, 184, 0); }
        }
        .header-navigation {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin-bottom: 3rem;
        }
        .nav-row {
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        .btn-pilih {
            background-color: var(--accent);
            color: var(--bg-color);
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
            min-width: 220px;
            text-align: center;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .btn-pilih:hover {
            background-color: #0d9488;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        .selection-text {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            flex-grow: 1;
            font-weight: 600;
            color: #f8fafc;
            font-size: 1.1rem;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
        }
        @media (max-width: 640px) {
            .nav-row {
                flex-direction: column;
                align-items: stretch;
                gap: 0.5rem;
            }
            .btn-pilih {
                min-width: 100%;
            }
            .selection-text {
                text-align: center;
            }
            .flip-card-front { font-size: 1rem; padding: 2rem; }
            .flip-card-back { font-size: 1.8rem; padding: 2rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-navigation">
            <div class="nav-row">
                <button class="btn-pilih">Pilih Tema</button>
                <div class="selection-text">{TEMA}</div>
            </div>
            <div class="nav-row">
                <button class="btn-pilih">Pilih Sub tema</button>
                <div class="selection-text">{SUB_TEMA}</div>
            </div>
            <div class="nav-row">
                <button class="btn-pilih">Pilih Pokok Bahasan</button>
                <div class="selection-text">{POKOK_BAHASAN}</div>
            </div>
        </div>
        
        <div class="hint">
            <span>✨</span> Klik pada kartu untuk membalik dan melihat teks Arabnya
        </div>

        {CONTENT}

    </div>
</body>
</html>
"""

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

import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]

def main():
    import glob
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
    
    sub_pokoks = df['sub pokok bahasan'].unique()
    
    page_num = 1
    for sp in sub_pokoks:
        group = df[df['sub pokok bahasan'] == sp]
        
        tema = str(group.iloc[0]['tema']).strip()
        sub_tema = str(group.iloc[0]['pokok bahasan']).strip()
        pokok_bahasan = str(sp).strip()
        
        content_html = ""
        
        uraians = group['uraian'].unique()
        for ur in uraians:
            content_html += f'<div class="section-title">{ur}</div>\n'
            
            if 'lihat juga' in str(ur).lower():
                continue
            
            verses_group = group[group['uraian'] == ur]
            
            for _, row in verses_group.iterrows():
                try:
                    surat_num = int(row['surat'])
                    ayat_num = int(row['ayat'])
                except ValueError:
                    print(f"Invalid surat/ayat: {row['surat']}:{row['ayat']}")
                    continue
                    
                surah_data = get_surah(surat_num)
                if not surah_data:
                    continue
                    
                nama_latin = surah_data['namaLatin']
                
                # Find ayat
                ayat_data = next((a for a in surah_data['ayat'] if a['nomorAyat'] == ayat_num), None)
                if not ayat_data:
                    print(f"Ayat {ayat_num} not found in Surah {surat_num}")
                    continue
                    
                teks_arab = ayat_data['teksArab']
                teks_indo = ayat_data['teksIndonesia']
                
                content_html += f'''
        <div class="verse-title">{nama_latin} [{surat_num}]: {ayat_num}</div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    {teks_indo}
                </div>
                <div class="flip-card-back">
                    {teks_arab}
                </div>
            </div>
        </div>
'''
        
        final_html = HTML_TEMPLATE.replace("{PAGE_NUM}", str(page_num))
        final_html = final_html.replace("{TEMA}", tema)
        final_html = final_html.replace("{SUB_TEMA}", sub_tema)
        final_html = final_html.replace("{POKOK_BAHASAN}", pokok_bahasan)
        final_html = final_html.replace("{CONTENT}", content_html)
        
        # Since halaman_1.html is the original one we created, let's just overwrite it or create new ones
        filename = f"halaman_{page_num}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"Generated {filename} for: {pokok_bahasan[:50]}")
        page_num += 1

if __name__ == '__main__':
    main()
