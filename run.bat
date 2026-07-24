@echo off
echo ==========================================
echo   🔥 TikTok Trend Analyzer Pro
echo   By: Eng. Hafez Al-Sulaihi
echo ==========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not installed!
    pause
    exit /b 1
)

echo [1/2] Installing requirements...
pip install -r requirements.txt

echo [2/2] Starting app...
streamlit run app.py

echo.
pause
