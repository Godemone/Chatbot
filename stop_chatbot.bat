@echo off
echo 🤖 Chatbot Kapatma Aracı
echo ================================

echo.
echo 🛑 Python işlemleri kapatılıyor...
taskkill /f /im python3.13.exe 2>nul
taskkill /f /im python.exe 2>nul
taskkill /f /im python3.exe 2>nul

echo.
echo 🔍 Port 5000 kontrol ediliyor...
netstat -an | findstr :5000
if %errorlevel% equ 0 (
    echo ⚠️  Port 5000 hala aktif olabilir.
) else (
    echo ✅ Port 5000 serbest.
)

echo.
echo ✅ Chatbot kapatma işlemi tamamlandı!
pause 