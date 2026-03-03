import streamlit as st

st.set_page_config(
    page_title="M.A Data Science & AI Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- CUSTOM STYLING -----------------
st.markdown("""
<style>
body {
    background-color: #0F172A;
}
.main {
    background-color: #0F172A;
    color: white;
}
h1, h2, h3 {
    color: #14B8A6;
}
.stButton>button {
    background-color: #14B8A6;
    color: black;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
.section-divider {
    border-top: 1px solid #1E293B;
    margin-top: 40px;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)

# ----------------- HERO SECTION -----------------
st.title("Upskill After Work. Grow Without Quitting.")
st.subheader("Evening Mentorship for Future Data Professionals")

st.markdown("""
Hybrid Batches | Only 6 Students | 4 Months | Real Projects  
First 3 Classes FREE  
📍 Langar House, Hashim Nagar
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔥 Book Free 3 Classes"):
        st.switch_page("Apply_Now")

with col2:
    st.markdown("[💬 WhatsApp Now](https://wa.me/918977863123)")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ----------------- PROBLEM SECTION -----------------
st.header("Why Most Students & Professionals Struggle")

st.markdown("""
- Recorded sessions with no mentor support  
- No real-world project exposure  
- No flexible evening timing  
- No interview preparation  
- No personalized attention  
""")

st.markdown("### We Built Something Different.")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ----------------- WHY CHOOSE US -----------------
st.header("Why Choose M.A Data Science & AI Hub")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Experience", "4+ Years")
col2.metric("Students Trained", "800+")
col3.metric("Batch Size", "6 Only")
col4.metric("Mode", "Hybrid")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ----------------- FEATURED COURSES -----------------
st.header("Featured Programs")

st.markdown("""
### 📊 Data Science – ₹35,000  
SQL | Advanced Excel | Power BI | Python | ML | DL | NLP | 3+ Projects  

### 🤖 AI / Machine Learning – ₹40,000  
SQL | Python | ML | DL | NLP | Generative AI  

### 📈 Data Analytics – ₹30,000  
SQL | Advanced Excel | Power BI | Python  
""")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ----------------- FINAL CTA -----------------
st.header("Limited Seats. Next Batch Starting Soon.")

st.markdown("""
Only 6 Students Per Batch  
Evening 8 PM – 11 PM  
Hybrid Mode  
""")

if st.button("🚀 Apply Now"):
    st.switch_page("Apply_Now")