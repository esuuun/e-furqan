import pandas as pd
import sys

try:
    df = pd.read_excel('Nabi Muhammad.xlsx')
    print("Columns:", df.columns.tolist())
    print("\nFirst 5 rows:")
    for i, row in df.head(5).iterrows():
        print(f"Row {i}:")
        for col in df.columns:
            val = str(row[col])[:100] # Truncate long text
            print(f"  {col}: {val}")
except Exception as e:
    print(f"Error reading Excel: {e}")
