# 🔥 TikTok Trend Analyzer Pro

**أداة Python احترافية لتحليل اتجاهات TikTok وتخطيط المحتوى**

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3046/3046126.png" width="100">
  <br><br>
  <strong>المهندس حافظ عبده محمد أحمد الصليحي</strong><br>
  <span style="color:#ff0050;">🏷️ العلامة التجارية: الصليحي</span><br>
  📧 hafez.asl14@yahoo.com | 📱 737930041
</div>

---

## 🚀 طرق التشغيل

| المنصة | الطريقة | الملف |
|--------|---------|-------|
| 📱 **Termux (Android)** | `bash install.sh` ثم `bash run-termux.sh` | `install.sh` |
| 🖥️ **Windows** | انقر مرتين على `run.bat` | `run.bat` |
| 🐧 **Linux/Mac** | `bash run.sh` | `run.sh` |
| 🌐 **Render.com** | انقر "Deploy to Render" | `render.yaml` |
| 🐳 **Docker** | `docker build -t tiktok . && docker run -p 8501:8501 tiktok` | `Dockerfile` |
| 🖥️ **cPanel/استضافة مشتركة** | `bash setup-hosting.sh` | `setup-hosting.sh` |

---

## 📤 رفع على GitHub

### 1. إنشاء مستودع جديد
```bash
# على جهازك (Termux/PC)
git init
git add .
git commit -m "Initial commit - TikTok Trend Analyzer Pro"
git branch -M main

# أنشئ مستودع على GitHub ثم:
git remote add origin https://github.com/USERNAME/tiktok-trend-analyzer.git
git push -u origin main
```

### 2. أو رفع مباشر (بدون Git)
- ادخل إلى [github.com/new](https://github.com/new)
- سمِّه `tiktok-trend-analyzer`
- ارفع الملفات يدوياً عبر واجهة GitHub

---

## 🌐 النشر على Render.com (مجاني)

### الطريقة السريعة:
1. ارفع المشروع على GitHub
2. ادخل إلى [render.com](https://render.com)
3. انقر **"New +"** → **"Web Service"**
4. اربط مستودع GitHub
5. اختر **"Docker"** كـ Environment
6. انقر **"Create Web Service"**

### أو عبر ملف render.yaml (Blueprints):
1. ارفع المشروع على GitHub
2. في Render، اختر **"Blueprints"** → **"New Blueprint Instance"**
3. اربط المستودع وسينشر تلقائياً!

**الرابط سيكون:** `https://tiktok-trend-analyzer.onrender.com`

---

## 🖥️ النشر على Vultr VPS

### 1. إنشاء VPS
- اختر Ubuntu 22.04
- اختر plan مناسب (1GB RAM كافية)

### 2. الاتصال بالخادم
```bash
ssh root@YOUR_SERVER_IP
```

### 3. تثبيت Docker
```bash
apt update && apt install -y docker.io docker-compose
systemctl enable docker
```

### 4. نسخ المشروع
```bash
git clone https://github.com/USERNAME/tiktok-trend-analyzer.git
cd tiktok-trend-analyzer
```

### 5. تشغيل التطبيق
```bash
docker build -t tiktok-analyzer .
docker run -d -p 8501:8501 --name tiktok tiktok-analyzer
```

### 6. فتح الجدار الناري
```bash
ufw allow 8501/tcp
```

**الرابط:** `http://YOUR_SERVER_IP:8501`

---

## 🏠 النشر على استضافة مشتركة (cPanel)

### 1. تفعيل Python في cPanel
- اذهب إلى **Setup Python App**
- اختر Python 3.11
- اضبط المسار على مجلد المشروع

### 2. تثبيت المتطلبات
```bash
cd ~/public_html/tiktok
curl -sS https://getcomposer.org/installer | php
pip install -r requirements.txt
```

### 3. إعداد Passenger
- تأكد من وجود `passenger_wsgi.py`
- اضبط Domain على المجلد

### 4. أو استخدم setup-hosting.sh
```bash
bash setup-hosting.sh
```

---

## 📁 هيكل المشروع

```
tiktok_trend_analyzer/
│
├── 📄 app.py                    ← التطبيق الرئيسي (Streamlit)
├── 📄 trends.py                 ← محلل الاتجاهات
├── 📄 content_planner.py        ← مخطط المحتوى الذكي
├── 📄 analyzer.py               ← محلل الفيديو
│
├── 📄 requirements.txt          ← المتطلبات
├── 📄 runtime.txt               ← إصدار Python
├── 📄 Procfile                  ← تكوين Heroku/Render
├── 📄 app.json                  ← تكوين Heroku
│
├── 🐳 Dockerfile                ← Docker image
├── 📄 render.yaml               ← تكوين Render Blueprints
├── 📄 .dockerignore             ← استبعاد ملفات Docker
│
├── 📄 install.sh                ← تثبيت Termux
├── 📄 run-termux.sh             ← تشغيل Termux
├── 📄 run.sh                    ← تشغيل Linux/Mac
├── 📄 run.bat                   ← تشغيل Windows
├── 📄 setup-hosting.sh          ← تثبيت استضافة مشتركة
├── 📄 passenger_wsgi.py         ← cPanel Passenger
│
├── 📁 .streamlit/
│   └── config.toml              ← إعدادات Streamlit
│
├── 📁 exports/                  ← مجلد التقارير المصدرة
└── 📄 README.md                 ← دليل الاستخدام (هذا الملف)
```

---

## ✨ المميزات

| الميزة | الوصف |
|--------|-------|
| 🔥 **تحليل الاتجاهات** | هاشتاقات وصوتات رائجة مع إحصائيات ورسوم بيانية |
| 📝 **مخطط المحتوى** | توليد أفكار فيديوهات مخصصة حسب مجالك |
| 📅 **خطة أسبوعية** | جدول محتوى كامل لـ 7 أيام |
| 🎬 **تحليل الفيديو** | درجة جودة وتوصيات تحسين قبل النشر |
| 📊 **تصدير Excel** | تقارير جاهزة للعملاء |
| 🌍 **دعم المناطق العربية** | اليمن، السعودية، مصر، الإمارات، الكويت |
| 📱 **متوافق مع الجوال** | Termux + Streamlit = متجر في جيبك |
| 🌐 **قابل للنشر** | Docker + Render + VPS + cPanel |

---

## 💡 أفكار الربح من الأداة

| الخدمة | السعر المقترح |
|--------|--------------|
| بيع التطبيق كاملاً | $30 - $100 |
| تحليل حساب TikTok | $10 - $30/شهر |
| خطة محتوى شهرية | $20 - $50/شهر |
| تقرير اتجاهات أسبوعي | $5 - $15/أسبوع |
| ترخيص للشركات | $100 - $500/سنة |

---

## ⚠️ ملاحظات قانونية

هذه الأداة تستخدم **مصادر بيانات عامة وقانونية** فقط:
- تحليل البيانات المتاحة علنياً
- لا تنتهك شروط TikTok
- لا تستخدم بوتات أو متابعين وهميين

---

## 👤 المطور

<div align="center">
  <strong>المهندس حافظ عبده محمد أحمد الصليحي</strong><br>
  📧 hafez.asl14@yahoo.com<br>
  📧 hafez.asl@gmail.com<br>
  📱 737930041<br>
  🏷️ العلامة التجارية: <strong>الصليحي</strong>
</div>

---

<div align="center">
  <strong>🚀 ابدأ رحلتك نحو المحتوى الاحترافي!</strong><br>
  <sub>صُممت بـ ❤️ في اليمن</sub>
</div>
# tiktok_trend_analyzer1
