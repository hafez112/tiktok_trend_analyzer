"""
Content Planner - مخطط المحتوى الذكي
"""

import random
from datetime import datetime

class ContentPlanner:
    def __init__(self):
        self.templates = {
            "تعليم": [
                {"title": "شرح مفهوم في 60 ثانية", "description": "اختر موضوعاً معقداً وابسطه في دقيقة واحدة", "hashtags": "#تعلم_سريع #تعليم #تطوير #مهارات", "best_time": "7:00 مساءً - 9:00 مساءً", "engagement_prediction": "عالي جداً 🔥"},
                {"title": "5 أخطاء شائعة في [المجال]", "description": "اعرض الأخطاء مع حلول سريعة", "hashtags": "#أخطاء_شائعة #نصائح #تعليم", "best_time": "8:00 مساءً - 10:00 مساءً", "engagement_prediction": "عالي 🔥"},
                {"title": "تحدي تعلم مهارة في 24 ساعة", "description": "سجل رحلة تعلمك لمهارة جديدة", "hashtags": "#تحدي #تعلم #مهارة #24ساعة", "best_time": "6:00 مساءً - 8:00 مساءً", "engagement_prediction": "عالي جداً 🔥🔥"},
                {"title": "قارن بين طريقتين", "description": "الطريقة القديمة vs الحديثة", "hashtags": "#مقارنة #تطوير #تقنية", "best_time": "7:30 مساءً - 9:30 مساءً", "engagement_prediction": "متوسط إلى عالي 🔥"},
                {"title": "أسئلة شائعة في 30 ثانية", "description": "اجمع أسئلة متكررة وأجب عنها", "hashtags": "#أسئلة_شائعة #نصائح #سريع", "best_time": "12:00 ظهراً - 2:00 ظهراً", "engagement_prediction": "عالي 🔥"},
            ],
            "ترفيه": [
                {"title": "تحدي الـ 24 ساعة", "description": "عيش يوماً بتحدي معين", "hashtags": "#تحدي #24ساعة #ترفيه #فيروسي", "best_time": "8:00 مساءً - 11:00 مساءً", "engagement_prediction": "عالي جداً 🔥🔥"},
                {"title": "ردة فعل على فيديو فيروسي", "description": "اعرض ردة فعلك الحقيقية", "hashtags": "#ردة_فعل #فيروسي #ترفيه", "best_time": "9:00 مساءً - 12:00 منتصف الليل", "engagement_prediction": "عالي 🔥"},
            ],
            "تقنية": [
                {"title": "مراجعة أداة جديدة", "description": "جرب أداة تقنية حديثة", "hashtags": "#مراجعة #تقنية #تطبيق", "best_time": "8:00 مساءً - 10:00 مساءً", "engagement_prediction": "عالي 🔥"},
                {"title": "حيلة برمجية في 15 ثانية", "description": "اعرض كود أو حيلة سريعة", "hashtags": "#برمجة #حيلة #تقنية #كود", "best_time": "7:00 مساءً - 9:00 مساءً", "engagement_prediction": "عالي جداً 🔥🔥"},
            ],
            "أعمال": [
                {"title": "قصة نجاح ملهمة", "description": "اعرض أبرز محطات نجاح ريادي", "hashtags": "#ريادة_أعمال #نجاح #قصة", "best_time": "7:00 صباحاً - 9:00 صباحاً", "engagement_prediction": "عالي 🔥"},
                {"title": "نصيحة مالية غيّرت حياتي", "description": "شارك نصيحة واحدة مؤثرة", "hashtags": "#مال #استثمار #نصيحة #ثراء", "best_time": "8:00 صباحاً - 10:00 صباحاً", "engagement_prediction": "عالي جداً 🔥🔥"},
            ],
            "صحة": [
                {"title": "تمارين سريعة للمكتب", "description": "3 تمارين أثناء العمل", "hashtags": "#صحة #رياضة #تمارين #لياقة", "best_time": "6:00 صباحاً - 8:00 صباحاً", "engagement_prediction": "عالي 🔥"},
            ],
            "أزياء": [
                {"title": "تحويلة ملابس بميزانية محدودة", "description": "إطلالة رائعة بأقل التكاليف", "hashtags": "#موضة #أزياء #ستايل #ميزانية", "best_time": "4:00 عصراً - 6:00 عصراً", "engagement_prediction": "عالي 🔥"},
            ],
            "طعام": [
                {"title": "وصفة سريعة في 30 ثانية", "description": "وصفة سهلة مع النتيجة", "hashtags": "#وصفات #طعام #طبخ #سريع", "best_time": "12:00 ظهراً - 2:00 ظهراً", "engagement_prediction": "عالي جداً 🔥🔥"},
            ],
            "الكل": [
                {"title": "يوم في حياتي", "description": "سجل يومك بأسلوب سينمائي", "hashtags": "#يوم_في_حياتي #يوميات #حياة", "best_time": "7:00 مساءً - 9:00 مساءً", "engagement_prediction": "عالي 🔥"},
                {"title": "سر نجاحي في 30 ثانية", "description": "نصيحة واحدة مؤثرة", "hashtags": "#نجاح #نصيحة #تحفيز", "best_time": "8:00 مساءً - 10:00 مساءً", "engagement_prediction": "عالي 🔥"},
                {"title": "قبل وبعد - فرق كبير!", "description": "تحول ملحوظ في أي مجال", "hashtags": "#قبل_وبعد #تحول #إنجاز", "best_time": "7:00 مساءً - 9:00 مساءً", "engagement_prediction": "عالي جداً 🔥🔥"},
            ]
        }

        self.best_times = {
            "شباب 18-24": ["8:00 مساءً", "9:00 مساءً", "10:00 مساءً"],
            "شباب 25-34": ["7:00 مساءً", "8:00 مساءً", "12:00 ظهراً"],
            "محترفون": ["7:00 صباحاً", "8:00 صباحاً", "12:30 ظهراً"],
            "أطفال": ["4:00 عصراً", "5:00 عصراً", "6:00 مساءً"],
            "الكل": ["7:00 مساءً - 9:00 مساءً"]
        }

    def generate_ideas(self, niche, target_audience, region, count=10):
        """توليد أفكار محتوى مخصصة"""
        category = self._detect_category(niche)
        templates = self.templates.get(category, self.templates["الكل"])

        ideas = []
        for template in templates:
            idea = template.copy()
            idea['title'] = idea['title'].replace("[المجال]", niche)
            idea['description'] = idea['description'].replace("[المجال]", niche)
            idea['hashtags'] += f" #{niche.replace(' ', '_')} #{region.replace(' ', '_')}"
            if target_audience in self.best_times:
                idea['best_time'] = random.choice(self.best_times[target_audience])
            ideas.append(idea)

        ideas.extend(self._generate_custom_ideas(niche, target_audience, region, count - len(ideas)))
        return ideas[:count]

    def _detect_category(self, niche):
        niche_lower = niche.lower()
        keywords = {
            "تعليم": ["تعليم", "تعلم", "دورة", "مدرسة", "جامعة", "دراسة", "لغة"],
            "ترفيه": ["ترفيه", "ضحك", "كوميديا", "مضحك", "تحدي"],
            "تقنية": ["تقنية", "برمجة", "تطبيق", "كمبيوتر", "هاتف", "ذكاء اصطناعي"],
            "أعمال": ["أعمال", "ريادة", "تجارة", "استثمار", "مال", "تسويق"],
            "صحة": ["صحة", "رياضة", "لياقة", "تغذية", "رجيم"],
            "أزياء": ["أزياء", "موضة", "جمال", "مكياج", "ستايل"],
            "طعام": ["طعام", "طبخ", "وصفات", "مطعم", "حلويات"]
        }
        for category, words in keywords.items():
            for word in words:
                if word in niche_lower:
                    return category
        return "الكل"

    def _generate_custom_ideas(self, niche, target, region, count):
        prompts = [
            f"أهم 3 نصائح في {niche} لا يعرفها إلا المحترفون",
            f"كيف بدأت رحلتي في {niche} من الصفر",
            f"الفرق بين المبتدئ والمحترف في {niche}",
            f"أدوات مجانية تساعدك في {niche}",
            f"أكبر خطأ يرتكبه الجميع في {niche}",
            f"تحدي: تطبيق ما تعلمته في {niche} لمدة أسبوع",
            f"أسئلة متكررة عن {niche} - الجزء 1",
            f"كيف تربح من {niche} في {region}",
        ]
        ideas = []
        for i, prompt in enumerate(prompts[:count]):
            ideas.append({
                "title": prompt,
                "description": f"فيديو تفاعلي يشرح {prompt} بأسلوب مبسط",
                "hashtags": f"#{niche.replace(' ', '_')} #تيك_توك #محتوى_عربي #{region.replace(' ', '_')}",
                "best_time": random.choice(self.best_times.get(target, ["7:00 مساءً"])),
                "engagement_prediction": random.choice(["عالي 🔥", "عالي جداً 🔥🔥", "متوسط 🔥"])
            })
        return ideas

    def generate_weekly_plan(self, niche, target_audience, region):
        days = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"]
        ideas = self.generate_ideas(niche, target_audience, region, count=7)
        plan = []
        for day, idea in zip(days, ideas):
            plan.append({
                "day": day, "title": idea['title'], "best_time": idea['best_time'],
                "hashtags": idea['hashtags'], "status": "مخطط"
            })
        return plan
