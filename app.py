import streamlit as st
import pandas as pd
from trends import TikTokTrendAnalyzer
from content_planner import ContentPlanner
from analyzer import VideoAnalyzer
import plotly.express as px
from datetime import datetime
import os
import glob

st.set_page_config(
    page_title="TikTok Trend Analyzer Pro",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS مخصص - TikTok Style
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

    * { font-family: 'Cairo', sans-serif !important; }

    .main-header {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ff0050, #00f2ea, #ff0050);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-shadow: 0 0 20px rgba(255,0,80,0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { filter: brightness(1); }
        to { filter: brightness(1.2); }
    }

    .metric-card {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 100%);
        border-radius: 20px;
        padding: 25px 15px;
        border: 2px solid transparent;
        border-image: linear-gradient(135deg, #ff0050, #00f2ea) 1;
        text-align: center;
        transition: transform 0.3s;
        margin: 5px 0;
    }
    .metric-card:hover { transform: scale(1.05); }

    .stButton>button {
        background: linear-gradient(90deg, #ff0050, #ff2d6e) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 12px 35px !important;
        font-weight: 900 !important;
        border: none !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(255,0,80,0.4) !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #00f2ea, #00c4cc) !important;
        color: #000 !important;
        box-shadow: 0 4px 20px rgba(0,242,234,0.5) !important;
        transform: translateY(-2px);
    }

    .stTextInput>div>div>input, .stSelectbox>div>div {
        border-radius: 15px !important;
        border: 2px solid #ff0050 !important;
        background: #0a0a1a !important;
        color: white !important;
    }

    .stRadio>div {
        background: linear-gradient(180deg, #0f0f23 0%, #1a1a2e 100%);
        border-radius: 15px;
        padding: 10px;
    }

    .stExpander {
        background: linear-gradient(135deg, #0a0a1a, #1a1a3e) !important;
        border-radius: 15px !important;
        border: 1px solid #ff0050 !important;
    }

    .footer-text {
        text-align: center;
        color: #888;
        font-size: 0.85rem;
        margin-top: 30px;
        padding: 15px;
        border-top: 1px solid #333;
    }

    /* تقليل الهوامش للجوال */
    .block-container { padding: 1rem 1rem 3rem !important; }
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.4rem !important; }
    h3 { font-size: 1.1rem !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<div style='text-align:center;'>🔥</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#ff0050; font-weight:900;'>TikTok Pro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00f2ea; font-size:0.8rem;'>Trend Analyzer</p>", unsafe_allow_html=True)
    st.markdown("---")

    menu = st.radio(
        "📋 القائمة",
        ["🏠 الرئيسية", "🔥 الاتجاهات", "📝 مخطط المحتوى", "🎬 تحليل الفيديو", "📊 التقارير"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### ⚙️ الإعدادات")
    region = st.selectbox("🌍 المنطقة", ["اليمن", "السعودية", "مصر", "الإمارات", "الكويت", "العالم"])
    category = st.selectbox("📂 التصنيف", ["الكل", "ترفيه", "تعليم", "تقنية", "أعمال", "صحة", "أزياء", "طعام"])

    st.markdown("---")
    st.markdown("<div class='footer-text'>© المهندس حافظ الصليحي<br>العلامة التجارية: الصليحي</div>", unsafe_allow_html=True)

# Main Content
if menu == "🏠 الرئيسية":
    st.markdown('<h1 class="main-header">🔥 TikTok Trend Analyzer Pro</h1>', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#aaa; margin-bottom:30px;'>أداة ذكية لتحليل الاتجاهات وتخطيط المحتوى الاحترافي</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:#ff0050; margin:0;'>🔥</h2>
            <h4 style='color:#fff; margin:5px 0;'>الاتجاهات</h4>
            <p style='color:#aaa; font-size:0.85rem; margin:0;'>رصد الهاشتاقات والصوتات الرائجة لحظياً</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:#00f2ea; margin:0;'>📝</h2>
            <h4 style='color:#fff; margin:5px 0;'>المحتوى</h4>
            <p style='color:#aaa; font-size:0.85rem; margin:0;'>توليد أفكار محتوى مخصصة حسب مجالك</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:#ffcc00; margin:0;'>📊</h2>
            <h4 style='color:#fff; margin:5px 0;'>التحليل</h4>
            <p style='color:#aaa; font-size:0.85rem; margin:0;'>تحليل أداء الفيديوهات وتحسين الاستراتيجية</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 ابدأ الآن")
    st.info("👈 اختر أداة من القائمة الجانبية للبدء في التحليل")

    # إحصائيات سريعة
    st.markdown("### 📈 إحصائيات سريعة")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("الهاشتاقات", "1,240+", "+12%")
    c2.metric("الصوتات", "856", "+8%")
    c3.metric("أفكار المحتوى", "3,500+", "+25%")
    c4.metric("الفيديوهات", "500+", "+15%")

    # معلومات Termux
    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#00f2ea; font-size:0.9rem;'>🤖 يعمل على Termux | Android</div>", unsafe_allow_html=True)

elif menu == "🔥 الاتجاهات":
    st.markdown('<h1 class="main-header">🔥 تحليل الاتجاهات</h1>', unsafe_allow_html=True)

    analyzer = TikTokTrendAnalyzer(region=region, category=category)

    tab1, tab2, tab3 = st.tabs(["📊 الهاشتاقات", "🎵 الصوتات", "📈 المقارنة"])

    with tab1:
        st.subheader("الهاشتاقات الرائجة")
        if st.button("🔄 جلب البيانات", key="hashtags"):
            with st.spinner("جاري تحليل الاتجاهات..."):
                hashtags = analyzer.get_trending_hashtags()
                st.session_state['hashtags'] = hashtags
                st.success(f"✅ تم جلب {len(hashtags)} هاشتاق!")

        if 'hashtags' in st.session_state:
            df = pd.DataFrame(st.session_state['hashtags'])
            st.dataframe(df, use_container_width=True, hide_index=True)

            fig = px.bar(df.head(15), x='hashtag', y='views', 
                        color='growth', color_continuous_scale=['#00f2ea', '#ff0050'],
                        title="أفضل 15 هاشتاق", template='plotly_dark')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                margin=dict(l=20, r=20, t=50, b=20)
            )
            st.plotly_chart(fig, use_container_width=True, use_container_height=True)

            if st.button("💾 تصدير Excel"):
                export_path = f"exports/hashtags_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
                df.to_excel(export_path, index=False)
                st.success(f"✅ تم الحفظ: {export_path}")

    with tab2:
        st.subheader("الصوتات الرائجة")
        if st.button("🔄 جلب البيانات", key="sounds"):
            with st.spinner("جاري التحليل..."):
                sounds = analyzer.get_trending_sounds()
                st.session_state['sounds'] = sounds
                st.success(f"✅ تم جلب {len(sounds)} صوت!")

        if 'sounds' in st.session_state:
            df = pd.DataFrame(st.session_state['sounds'])
            st.dataframe(df, use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("مقارنة الاتجاهات")
        keywords = st.text_input("أدخل كلمات مفتاحية (مفصولة بفاصلة)", "تعليم,ترفيه,تقنية")
        if st.button("📊 قارن"):
            with st.spinner("جاري المقارنة..."):
                comparison = analyzer.compare_trends(keywords.split(","))
                df_comp = pd.DataFrame(comparison)
                fig = px.line(df_comp, x='date', y='interest', color='keyword',
                             title="مقارنة الاهتمام عبر الزمن", template='plotly_dark')
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)', 
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    margin=dict(l=20, r=20, t=50, b=20)
                )
                st.plotly_chart(fig, use_container_width=True)

elif menu == "📝 مخطط المحتوى":
    st.markdown('<h1 class="main-header">📝 مخطط المحتوى الذكي</h1>', unsafe_allow_html=True)

    planner = ContentPlanner()

    niche = st.text_input("🎯 مجال حسابك", "تعليم البرمجة")
    target = st.selectbox("👥 الفئة المستهدفة", ["شباب 18-24", "شباب 25-34", "محترفون", "أطفال", "الكل"])

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✨ توليد أفكار"):
            with st.spinner("جاري توليد الأفكار..."):
                ideas = planner.generate_ideas(niche, target, region)
                st.session_state['ideas'] = ideas
                st.success(f"✅ تم توليد {len(ideas)} فكرة!")
    with col_btn2:
        if st.button("📅 خطة أسبوعية"):
            with st.spinner("جاري إنشاء الخطة..."):
                plan = planner.generate_weekly_plan(niche, target, region)
                st.session_state['weekly_plan'] = plan
                st.success("✅ تم إنشاء الخطة الأسبوعية!")

    if 'ideas' in st.session_state:
        for i, idea in enumerate(st.session_state['ideas']):
            with st.expander(f"💡 فكرة {i+1}: {idea['title']}"):
                st.write(f"**الوصف:** {idea['description']}")
                st.write(f"**الهاشتاقات:** `{idea['hashtags']}`")
                st.write(f"**أفضل وقت:** {idea['best_time']}")
                st.write(f"**التوقع:** {idea['engagement_prediction']}")

                if st.button(f"➕ أضف للخطة", key=f"add_{i}"):
                    if 'plan' not in st.session_state:
                        st.session_state['plan'] = []
                    st.session_state['plan'].append(idea)
                    st.success("✅ تمت الإضافة!")

    if 'weekly_plan' in st.session_state:
        st.markdown("---")
        st.subheader("📅 الخطة الأسبوعية")
        plan_df = pd.DataFrame(st.session_state['weekly_plan'])
        st.dataframe(plan_df, use_container_width=True, hide_index=True)
        if st.button("💾 تصدير الخطة"):
            export_path = f"exports/weekly_plan_{datetime.now().strftime('%Y%m%d')}.xlsx"
            plan_df.to_excel(export_path, index=False)
            st.success(f"✅ تم التصدير: {export_path}")

    if 'plan' in st.session_state and st.session_state['plan']:
        st.markdown("---")
        st.subheader("📋 خطتك المخصصة")
        plan_df = pd.DataFrame(st.session_state['plan'])
        st.dataframe(plan_df[['title', 'best_time', 'engagement_prediction']], use_container_width=True, hide_index=True)

elif menu == "🎬 تحليل الفيديو":
    st.markdown('<h1 class="main-header">🎬 تحليل أداء الفيديو</h1>', unsafe_allow_html=True)

    uploaded = st.file_uploader("📤 ارفع ملف فيديو (MP4)", type=['mp4', 'mov'])

    if uploaded:
        st.video(uploaded)
        if st.button("🔍 تحليل الفيديو"):
            with st.spinner("جاري التحليل..."):
                analyzer = VideoAnalyzer()
                results = analyzer.analyze_video(uploaded)

                # درجة الجودة
                score_color = "#00f2ea" if results['score'] >= 80 else "#ffcc00" if results['score'] >= 60 else "#ff0050"
                st.markdown(f"""
                <div style='text-align:center; padding:20px; background:linear-gradient(135deg, #0a0a1a, #1a1a3e); border-radius:20px; margin:15px 0;'>
                    <h2 style='color:{score_color}; font-size:3rem; margin:0;'>{results['score']}/100</h2>
                    <p style='color:#aaa;'>درجة جودة الفيديو</p>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("⏱️ المدة", results['duration'])
                col2.metric("📐 الدقة", results['resolution'])
                col3.metric("📦 الحجم", results['size'])

                st.subheader("💡 توصيات التحسين")
                for tip in results['tips']:
                    st.info(tip)

elif menu == "📊 التقارير":
    st.markdown('<h1 class="main-header">📊 التقارير المحفوظة</h1>', unsafe_allow_html=True)

    reports = glob.glob("exports/*.xlsx")

    if reports:
        for report in reports:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"📄 {os.path.basename(report)}")
                st.caption(f"الحجم: {os.path.getsize(report)/1024:.1f} KB")
            with col2:
                with open(report, 'rb') as f:
                    st.download_button("⬇️ تحميل", f, file_name=os.path.basename(report))
    else:
        st.info("📭 لا توجد تقارير محفوظة بعد")
        st.write("قم بتحليل الاتجاهات أو إنشاء خطة محتوى ثم تصديرها!")
