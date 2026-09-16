import json
import os
import sys
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries in dhamir_data.json: {len(data)}")

# Verification checks
missing_bentuk_bn = [d for d in data if not d.get('BentukKataBN')]
missing_surat_bn = [d for d in data if not d.get('SuratArtiBN')]
missing_arti_bn = [d for d in data if not d.get('ArtiKataBN')]
missing_teks_bn = [d for d in data if not d.get('TeksArtiBN')]

print(f"Missing BentukKataBN: {len(missing_bentuk_bn)}")
print(f"Missing SuratArtiBN:  {len(missing_surat_bn)}")
print(f"Missing ArtiKataBN:   {len(missing_arti_bn)}")
print(f"Missing TeksArtiBN:   {len(missing_teks_bn)}")

if not missing_bentuk_bn and not missing_surat_bn and not missing_arti_bn and not missing_teks_bn:
    print("\n[SUCCESS] All 301 entries have complete Bangla (BN) data!")
else:
    print("\n[WARN] Some fields are missing!")
    sys.exit(1)

# Sample check
sample = data[0]
print("\nSample entry (1st):")
print(f"  Word:        {sample.get('Kata')} ({sample.get('Latin')})")
print(f"  Bentuk (BN): {sample.get('BentukKataBN')}")
print(f"  Surah (BN):  {sample.get('SuratNama')} ({sample.get('SuratArtiBN')})")
print(f"  Arti (BN):   {sample.get('ArtiKataBN')}")
print(f"  Teks (BN):   {sample.get('TeksArtiBN')[:70]}...")
