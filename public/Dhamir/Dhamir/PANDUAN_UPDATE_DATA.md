# 📖 Panduan Pembaruan Data (Update Data)

File pembaruan data otomatis telah berhasil dibuat untuk memudahkan Anda memperbarui data ayat, arti, transliterasi Latin, dan audio tilawah dari file Excel ke aplikasi web interaktif.

---

## 🚀 Cara Cepat Memperbarui Data (1-Klik)

### Cara 1: Double-Click File `.bat` (Paling Mudah di Windows)
Cukup **klik ganda (double-click)** pada file:
👉 **`update_data.bat`** di File Explorer.

Script akan:
1. Membuka jendela perintah secara otomatis.
2. Membaca data terbaru dari Excel (`DHAMIR copy.xlsx` atau `Kamus Jamid Mabny.xlsx`).
3. Mengambil teks Arab, transliterasi Latin resmi Kemenag, terjemahan 22 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ), serta audio MP3 per ayat.
4. Menghasilkan file **`dhamir_data.js`** dan **`dhamir_data.json`**.
5. Menampilkan ringkasan total ayat dan kata yang berhasil diperbarui.

---

### Cara 2: Menjalankan via Terminal / Command Prompt
Buka Terminal atau PowerShell di folder proyek ini, lalu jalankan:

```bash
python update_data.py
```

Secara default, script akan memperbarui **KEEMPAT KAMUS** (`Kamus Jamid Mabny`, `Kamus Harf Ghair Amil`, `Kamus Harf 'Amil`, dan `Kamus Musytaq`).

#### Opsi / Parameter Tambahan yang Tersedia:
- **Pilih Kamus Tertentu yang Ingin Diperbarui:**
  ```bash
  # Perbarui keempat kamus sekaligus (default)
  python update_data.py --dict all

  # Hanya perbarui Kamus Jamid Mabny
  python update_data.py --dict jamid

  # Hanya perbarui Kamus Harf Ghair Amil
  python update_data.py --dict harf

  # Hanya perbarui Kamus Harf 'Amil
  python update_data.py --dict harf_amil

  # Hanya perbarui Kamus Musytaq
  python update_data.py --dict musytaq
  ```
- **Tentukan File Excel Tertentu:**
  ```bash
  python update_data.py --excel "Kamus Jamid Mabny.xlsx"
  ```
- **Tentukan Nama Sheet Tertentu:**
  ```bash
  python update_data.py --sheet "KAMUS KATA"
  ```
- **Batasi Jumlah Contoh Ayat per Kata (misal max 5 ayat per kata):**
  ```bash
  python update_data.py --limit 5
  ```

---

## 📁 Struktur File Hasil Update & Cache 39 Bahasa

| Nama File | Fungsi & Sumber Terjemahan |
| :--- | :--- |
| **`update_data.py`** | Script Python utama untuk membaca keempat Excel, memproses API, dan membuat file data. |
| **`update_data.bat`** | File jalan pintas (shortcut) Windows 1-klik untuk menjalankan update tanpa repot. |
| **`build_musytaq_dataset.py`** | Generator dataset khusus Kamus Musytaq (Morfologi, Tasrif, Wazan & Kaidah I'lal). |
| **`musytaq_data.js`** | File dataset JavaScript Kamus Musytaq (80 Akar Kata, 3.012 Entri Tasrif). |
| **`musytaq_data.json`** | Salinan data Kamus Musytaq dalam format JSON. |
| **`dhamir_data.js`** | File dataset JavaScript Kamus Jamid Mabny (7 Bentuk Kata, 76 Kata). |
| **`dhamir_data.json`** | Salinan data Kamus Jamid Mabny dalam format JSON. |
| **`harf_data.js`** | File dataset JavaScript Kamus Harf Ghair 'Amil (17 Bentuk Harf, 52 Kata). |
| **`harf_data.json`** | Salinan data Kamus Harf Ghair 'Amil dalam format JSON. |
| **`Harf_Ghair_Amil_Interaktif.xlsx`** | File Excel Interaktif Harf Ghair 'Amil dengan Dropdown Kategori, No Kata, Card VLOOKUP & Formula Dinamis. |
| **`harf_amil_data.js`** | File dataset JavaScript Kamus Harf 'Amil (6 Bentuk Harf, 54 Kata). |
| **`harf_amil_data.json`** | Salinan data Kamus Harf 'Amil dalam format JSON. |
| **`Harf_Amil_Interaktif.xlsx`** | File Excel Interaktif Harf 'Amil dengan Dropdown Kategori, No Kata, Card VLOOKUP & Formula Dinamis. |
| **`verse_cache.json`** | Cache lokal teks Arab, Latin Kemenag, dan audio Alafasy. |
| **`en_translations.json`** | Terjemahan Bahasa Inggris (Sahih International). |
| **`ms_translations.json`** | Terjemahan Bahasa Melayu (Syeikh Abdullah Basmeih / JAKIM). |
| **`fr_translations.json`** | Terjemahan Bahasa Prancis (Muhammad Hamidullah). |
| **`de_translations.json`** | Terjemahan Bahasa Jerman (Frank Bubenheim & Nadeem Elyas). |
| **`ur_translations.json`** | Terjemahan Bahasa Urdu (Maulana Fateh Muhammad Jalandhry). |
| **`hi_translations.json`** | Terjemahan Bahasa Hindi (Dr. Suhel Farooq Khan & Dr. Saifur Rahman Nadwi). |
| **`bn_translations.json`** | Terjemahan Bahasa Bengali / Bangla (Maulana Muhiuddin Khan). |
| **`ru_translations.json`** | Terjemahan Bahasa Rusia (Elmir Kuliev / Эльмир Кулиев). |
| **`zh_translations.json`** | Terjemahan Bahasa Mandarin / Cina (Muhammad Makin / 马坚 译本). |
| **`es_translations.json`** | Terjemahan Bahasa Spanyol (Muhammad Isa García). |
| **`tr_translations.json`** | Terjemahan Bahasa Turki (Türkiye Diyanet Vakfı). |
| **`pt_translations.json`** | Terjemahan Bahasa Portugis (Samir El-Hayek / Helmi Nasr). |
| **`ha_translations.json`** | Terjemahan Bahasa Hausa (Sheikh Abubakar Mahmoud Gumi). |
| **`sw_translations.json`** | Terjemahan Bahasa Swahili / Kiswahili (Sheikh Ali Muhsin Al-Barwani). |
| **`fa_translations.json`** | Terjemahan Bahasa Persia / Farsi (Ayatullah Naser Makarem Shirazi). |
| **`ja_translations.json`** | Terjemahan Bahasa Jepang (Ryoichi Mita / 日本ムスリム協会 / 三田了一 訳). |
| **`ko_translations.json`** | Terjemahan Bahasa Korea (Dr. Hamid Choi / 최영길 박사 번역). |
| **`nl_translations.json`** | Terjemahan Bahasa Belanda (Sofian S. Siregar). |
| **`it_translations.json`** | Terjemahan Bahasa Italia (Hamza Roberto Piccardo). |
| **`bs_translations.json`** | Terjemahan Bahasa Bosnia (Besim Korkut). |
| **`sq_translations.json`** | Terjemahan Bahasa Albania (Sherif Ahmeti). |

---

## 📝 Format Kolom di File Excel

Pastikan file Excel Anda memiliki kolom header berikut pada baris pertama (Sheet1 atau Data Master):

| Bentuk Kata | No kata | Kata | Arti kata | Frek kata | SURAT | AYAT |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `1. Dhamir` | `11a` | `أَنَا` | `SAYA / AKU` | `68` | `26` | `114` |
| `1. Dhamir` | `1a` | `هُوَ` | `DIA (LK)` | `481` | `112` | `1` |

> **Catatan:** Kolom `SURAT` diisi nomor surat (1–114) dan `AYAT` diisi nomor ayat. Sistem secara otomatis akan melengkapi nama surat, teks Arab ayat penuh, bacaan Latin, terjemahan, dan audio.
