#!/bin/bash
# ============================================
# TikTok Trend Analyzer Pro - Hosting Setup
# For cPanel / Shared Hosting with Python
# By: Eng. Hafez Al-Sulaihi
# ============================================

echo "=========================================="
echo "  🔥 TikTok Trend Analyzer Pro"
echo "  Hosting Setup Script"
echo "=========================================="
echo ""

# التحقق من Python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "[ERROR] Python not found!"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
$PYTHON -m venv venv
source venv/bin/activate

echo "[2/4] Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[3/4] Creating exports directory..."
mkdir -p exports

echo "[4/4] Setup complete!"
echo ""
echo "To run:"
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
echo "=========================================="
