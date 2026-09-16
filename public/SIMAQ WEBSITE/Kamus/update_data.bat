@echo off
chcp 65001 >nul
title Update Data Dhamir Al-Qur'an
cls

echo ==================================================================
echo           PEMBARUAN OTOMATIS DATA DHAMIR AL-QUR'AN               
echo ==================================================================
echo.

:: Cek apakah Python terpasang
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
    goto RUN_SCRIPT
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=py
    goto RUN_SCRIPT
)

echo [ERROR] Python tidak ditemukan di sistem Anda!
echo Silakan install Python dari https://www.python.org/downloads/
echo dan pastikan centang "Add Python to PATH" saat instalasi.
echo.
pause
exit /b 1

:RUN_SCRIPT
echo Menggunakan: %PY_CMD%
echo Memeriksa dependensi...
%PY_CMD% -c "import openpyxl" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Menginstall modul 'openpyxl'...
    %PY_CMD% -m pip install openpyxl
    echo.
)

echo Menjalankan update_data.py...
echo.
%PY_CMD% update_data.py %*

echo.
echo ==================================================================
echo Tekan sembarang tombol untuk menutup jendela ini...
pause >nul
