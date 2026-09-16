@echo off
chcp 65001 >nul
title SIMAQ.CLOUD - Local Server Launcher
color 0B

echo ================================================================
echo        SIMAQ.CLOUD - Ekosistem Pembelajaran Al-Qur'an
echo ================================================================
echo.
echo [1/3] Menyiapkan server lokal...
echo Direktori Root: %~dp0
cd /d "%~dp0"

echo [2/3] Membuka browser otomatis ke http://localhost:8000 ...
start "" "http://localhost:8000"

echo [3/3] Menjalankan server HTTP lokal di Port 8000...
echo ----------------------------------------------------------------
echo Server Aktif! Jangan tutup jendela ini selama menggunakan portal.
echo Buka di browser: http://localhost:8000
echo Tekan CTRL + C untuk menghentikan server.
echo ----------------------------------------------------------------
echo.

:: Coba jalankan server dengan Python
where python >nul 2>nul
if %errorlevel% equ 0 (
    python -m http.server 8000
    goto end
)

:: Coba jalankan server dengan Node / npx
where npx >nul 2>nul
if %errorlevel% equ 0 (
    npx -y serve -l 8000 .
    goto end
)

echo [PERINGATAN] Python maupun Node.js tidak terdeteksi di PATH sistem.
echo Membuka index.html secara langsung di browser...
start "" "%~dp0index.html"
pause

:end
