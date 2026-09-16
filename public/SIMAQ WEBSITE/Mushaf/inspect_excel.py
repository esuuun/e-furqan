import pandas as pd
import json

try:
    df = pd.read_excel('MASTER MUSHAF.xlsx')
    print("Columns:", df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head(5).to_json(orient='records', force_ascii=False))
except Exception as e:
    print("Error:", e)
