import os
import time
import subprocess
import glob

def get_excel_mtimes():
    mtimes = {}
    for f in glob.glob('*.xlsx'):
        if not f.startswith('~$'):
            mtimes[f] = os.path.getmtime(f)
    return mtimes

print("=======================================================")
print("  Auto-Watch File Excel Aktif!")
print("  Setiap kali file .xlsx disimpan/diubah, data web akan")
print("  diperbarui secara otomatis.")
print("=======================================================")
print("Tekan Ctrl + C untuk menghentikan.\n")

last_mtimes = get_excel_mtimes()

while True:
    try:
        time.sleep(2)
        current_mtimes = get_excel_mtimes()
        if current_mtimes != last_mtimes:
            print(f"[{time.strftime('%H:%M:%S')}] Perubahan file Excel terdeteksi! Memperbarui data...")
            subprocess.run(["python", "build_data.py"])
            print(f"[{time.strftime('%H:%M:%S')}] Selesai! Refresh browser (F5) untuk melihat perubahan.\n")
            last_mtimes = current_mtimes
    except KeyboardInterrupt:
        print("\nAuto-Watch dihentikan.")
        break
    except Exception as e:
        print(f"Error: {e}")
