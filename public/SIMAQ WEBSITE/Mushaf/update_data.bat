@echo off
echo Mengupdate data dari MASTER MUSHAF.xlsx...
cd /d "%~dp0"
python process_data.py
echo.
echo Proses Selesai! Silakan refresh browser Anda.
pause
