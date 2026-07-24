#!/bin/bash
echo "=========================================="
echo "  🔥 TikTok Trend Analyzer Pro"
echo "  By: Eng. Hafez Al-Sulaihi"
echo "=========================================="
echo ""

if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 not found!"
    exit 1
fi

pip3 install -r requirements.txt
mkdir -p exports
streamlit run app.py
