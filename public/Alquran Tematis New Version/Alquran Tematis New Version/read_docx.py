import docx
import sys

try:
    doc = docx.Document('Nabi Muhammad ﷺ.docx')
    for i, p in enumerate(doc.paragraphs[:100]):
        text = p.text.strip()
        if text:
            print(f"[{i}] {text}")
except Exception as e:
    print(f"Error: {e}")
