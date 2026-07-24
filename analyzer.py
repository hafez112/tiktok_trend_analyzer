"""
Video Analyzer - تحليل الفيديو
"""

from datetime import datetime

class VideoAnalyzer:
    def __init__(self):
        self.optimal_duration = {"hook": 3, "short": 15, "medium": 60, "long": 180}

    def analyze_video(self, file_obj):
        file_size = len(file_obj.getvalue()) if hasattr(file_obj, 'getvalue') else 0
        size_mb = file_size / (1024 * 1024)
        duration_seconds = int(size_mb * 5)
        resolution = "1080x1920" if size_mb > 50 else "720x1280" if size_mb > 20 else "540x960" if size_mb > 5 else "other"
        tips = self._generate_tips(duration_seconds, resolution, size_mb)
        return {
            "duration": self._format_duration(duration_seconds),
            "duration_seconds": duration_seconds, "resolution": resolution,
            "size": f"{size_mb:.2f} MB", "size_mb": size_mb,
            "tips": tips, "score": self._calculate_score(duration_seconds, resolution, size_mb),
            "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def _format_duration(self, seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes} دقيقة {secs} ثانية" if minutes > 0 else f"{secs} ثانية"

    def _generate_tips(self, duration, resolution, size_mb):
        tips = []
        if duration < 10:
            tips.append("⚠️ الفيديو قصير جداً. حاول أن يكون 15 ثانية على الأقل.")
        elif duration > 180:
            tips.append("⚠️ الفيديو طويل. فيديوهات 15-60 ثانية الأكثر انتشاراً.")
        elif 15 <= duration <= 60:
            tips.append("✅ المدة مثالية! أعلى نسبة مشاهدة كاملة.")

        if resolution == "1080x1920":
            tips.append("✅ الدقة ممتازة! Full HD عمودي يظهر بشكل احترافي.")
        elif resolution == "720x1280":
            tips.append("✅ الدقة جيدة، لكن 1080x1920 يعطي جودة أفضل.")
        else:
            tips.append("❌ الدقة تحتاج تحسين. استخدم 1080x1920.")

        if size_mb > 100:
            tips.append("⚠️ حجم الملف كبير. جرب ضغط الفيديو.")

        tips.extend([
            "💡 ابدأ الفيديو بـ Hook قوي في أول 3 ثواني.",
            "💡 أضف نصوصاً على الشاشة - 85% يشاهدون بدون صوت.",
            "💡 استخدم موسيقى رائجة من مكتبة TikTok.",
            "💡 اطلب التفاعل (تعليق، مشاركة، متابعة) في النهاية."
        ])
        return tips

    def _calculate_score(self, duration, resolution, size_mb):
        score = 50
        if 15 <= duration <= 60: score += 25
        elif duration < 15: score += 10
        else: score += 5
        if resolution == "1080x1920": score += 15
        elif resolution == "720x1280": score += 10
        else: score += 5
        if 5 <= size_mb <= 50: score += 10
        elif size_mb < 5: score += 5
        return min(score, 100)
