# TikTok Trend Analyzer Pro - Docker
# By: Eng. Hafez Al-Sulaihi
# العلامة التجارية: الصليحي

FROM python:3.11-slim

WORKDIR /app

# تثبيت المتطلبات النظامية
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# نسخ الملفات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# إنشاء مجلد التصدير
RUN mkdir -p exports

# منفذ Streamlit
EXPOSE 8501

# تشغيل التطبيق
CMD ["streamlit", "run", "app.py", "--server.headless=true", "--server.address=0.0.0.0", "--server.port=8501"]
