#!/data/data/com.termux/files/usr/bin/bash
# ============================================
# TikTok Trend Analyzer Pro - Termux Runner
# By: Eng. Hafez Al-Sulaihi
# العلامة التجارية: الصليحي
# ============================================

echo ""
echo "=========================================="
echo "  🔥 TikTok Trend Analyzer Pro"
echo "  Starting on Termux..."
echo "=========================================="
echo ""

# الألوان
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

# التحقق من Python
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}[!] Python not found. Running installer first...${NC}"
    bash install.sh
fi

# التحقق من المكتبات
echo -e "${CYAN}[1/3] Checking libraries...${NC}"
python -c "import streamlit" 2>/dev/null || pip install streamlit pandas plotly openpyxl

# إنشاء مجلد التصدير
mkdir -p exports

echo -e "${CYAN}[2/3] Starting Streamlit server...${NC}"
echo -e "${YELLOW}    The app will be available at:${NC}"
echo -e "${GREEN}    http://localhost:8501${NC}"
echo ""

# محاولة فتح المتصفح (إذا كان متوفراً)
if command -v termux-open-url &> /dev/null; then
    sleep 3
    termux-open-url http://localhost:8501 &
fi

echo -e "${CYAN}[3/3] Launching app...${NC}"
echo "=========================================="
echo ""

# تشغيل التطبيق
streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port 8501
