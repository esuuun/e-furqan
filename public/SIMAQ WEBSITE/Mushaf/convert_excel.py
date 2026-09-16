import pandas as pd
import json
import os

try:
    df = pd.read_excel('MASTER MUSHAF.xlsx')
    print("Number of rows:", len(df))
    # Fill NaN with empty string
    df = df.fillna('')
    # Export to JSON
    # We can group by SURAT and AYAT to make a structured JSON
    # Or just export the whole thing as records
    records = df.to_dict(orient='records')
    with open('quran_data.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False)
    print("Exported to quran_data.json")
    print("JSON size:", os.path.getsize('quran_data.json'))
except Exception as e:
    print("Error:", e)
