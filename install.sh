#!/data/data/com.termux/files/usr/bin/bash
# ============================================
# TikTok Trend Analyzer Pro - Termux Installer
# By: Eng. Hafez Al-Sulaihi
# العلامة التجارية: الصليحي
# ============================================

echo ""
echo "=========================================="
echo "  🔥 TikTok Trend Analyzer Pro"
echo "  Termux Auto-Installer"
echo "  By: Eng. Hafez Al-Sulaihi"
echo "=========================================="
echo ""

# الألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# التحقق من Termux
if [ -z "$TERMUX_VERSION" ] && [ ! -d "/data/data/com.termux" ]; then
    echo -e "${RED}[ERROR] This installer is designed for Termux only!${NC}"
    echo "Please run this on Termux (Android)."
    exit 1
fi

echo -e "${CYAN}[1/6] Updating packages...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[2/6] Installing Python & pip...${NC}"
pkg install -y python python-pip

echo -e "${CYAN}[3/6] Installing required packages...${NC}"
pkg install -y libxml2 libxslt

echo -e "${CYAN}[4/6] Installing Python libraries...${NC}"
pip install --upgrade pip
pip install streamlit pandas plotly openpyxl requests beautifulsoup4 lxml

echo -e "${CYAN}[5/6] Creating exports directory...${NC}"
mkdir -p exports

echo -e "${CYAN}[6/6] Setting permissions...${NC}"
chmod +x run-termux.sh
chmod +x run.sh

echo ""
echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}  ✅ Installation Complete!${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""
echo -e "${YELLOW}To start the app, run:${NC}"
echo -e "${CYAN}  ./run-termux.sh${NC}"
echo ""
echo -e "${YELLOW}Or manually:${NC}"
echo -e "${CYAN}  streamlit run app.py${NC}"
echo ""
echo -e "${YELLOW}The app will open at:${NC}"
echo -e "${CYAN}  http://localhost:8501${NC}"
echo ""
echo "=========================================="
