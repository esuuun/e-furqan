import urllib.request
import json

def test_quran_api():
    surah = 5
    ayat = 103
    url = f"https://equran.id/api/v2/surat/{surah}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            ayat_data = next((a for a in data['data']['ayat'] if a['nomorAyat'] == ayat), None)
            if ayat_data:
                print(f"Arabic: {ayat_data['teksArab']}")
                print(f"Indo: {ayat_data['teksIndonesia']}")
            else:
                print("Ayat not found")
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == '__main__':
    test_quran_api()
