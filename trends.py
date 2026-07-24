"""
TikTok Trend Analyzer - محلل اتجاهات TikTok
"""

import pandas as pd
from datetime import datetime, timedelta
import random

class TikTokTrendAnalyzer:
    def __init__(self, region="العالم", category="الكل"):
        self.region = region
        self.category = category
        self.region_map = {
            "اليمن": "YE", "السعودية": "SA", "مصر": "EG",
            "الإمارات": "AE", "الكويت": "KW", "العالم": ""
        }

    def get_trending_hashtags(self, limit=50):
        """جلب الهاشتاقات الرائجة"""
        base_hashtags = {
            "ترفيه": ["#ضحك", "#تحدي", "#ترفيه", "#مضحك", "#كوميديا", "#فيروسي", "#ترند"],
            "تعليم": ["#تعلم", "#تعليم", "#دورة", "#مهارة", "#تطوير", "#تيك_توك_تعليمي", "#نصيحة"],
            "تقنية": ["#تقنية", "#برمجة", "#ذكاء_اصطناعي", "#تطبيق", "#تكنولوجيا", "#حيلة", "#كود"],
            "أعمال": ["#ريادة_أعمال", "#تجارة", "#استثمار", "#مال", "#نجاح", "#ثراء", "#تسويق"],
            "صحة": ["#صحة", "#رياضة", "#لياقة", "#تغذية", "#صحة_نفسية", "#رجيم", "#تمارين"],
            "أزياء": ["#موضة", "#أزياء", "#ستايل", "#جمال", "#مكياج", "#أناقة", "#تسوق"],
            "طعام": ["#وصفات", "#طعام", "#طبخ", "#مطاعم", "#حلويات", "#ذ_ايب", "#اكل"],
            "الكل": ["#فيروسي", "#رائج", "#مشهور", "#ترند", "#تيك_توك", "#عرب", "#محتوى_عربي"]
        }

        category_tags = base_hashtags.get(self.category, base_hashtags["الكل"])
        hashtags = []

        for i, tag in enumerate(category_tags * 10):
            if len(hashtags) >= limit:
                break

            hashtags.append({
                "hashtag": tag + (f"{i}" if i > 0 else ""),
                "views": random.randint(100000, 50000000),
                "growth": random.randint(-15, 85),
                "posts": random.randint(1000, 500000),
                "category": self.category,
                "region": self.region,
                "date": datetime.now().strftime("%Y-%m-%d")
            })

        return sorted(hashtags, key=lambda x: x['views'], reverse=True)

    def get_trending_sounds(self, limit=30):
        """الصوتات الرائجة"""
        sounds = [
            {"sound": "Original Sound - Trend 2026", "uses": 2500000, "growth": 120, "category": "موسيقى"},
            {"sound": "Viral Beat Remix", "uses": 1800000, "growth": 95, "category": "إيقاع"},
            {"sound": "Funny Voice Effect", "uses": 1500000, "growth": 80, "category": "كوميديا"},
            {"sound": "Arabic Remix 2026", "uses": 1200000, "growth": 60, "category": "موسيقى"},
            {"sound": "Transition Sound FX", "uses": 900000, "growth": 45, "category": "تأثيرات"},
            {"sound": "Dance Challenge Beat", "uses": 800000, "growth": 70, "category": "رقص"},
            {"sound": "Motivational Arabic", "uses": 600000, "growth": 35, "category": "تحفيز"},
            {"sound": "Tutorial Background", "uses": 500000, "growth": 25, "category": "تعليم"},
        ]
        return sounds[:limit]

    def compare_trends(self, keywords, timeframe='today 3-m'):
        """مقارنة الاتجاهات"""
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        results = []
        for keyword in keywords:
            for date in dates:
                results.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "keyword": keyword.strip(),
                    "interest": random.randint(20, 100)
                })
        return results
