import streamlit as st

st.set_page_config(
    page_title="About the Founder - Data Science Academy", 
    page_icon="👨‍🏫",
    layout="wide"
)

# --- Custom CSS for Founder Page ---
st.markdown("""
<style>
    .founder-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .founder-name {
        font-size: 3rem;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .founder-title {
        font-size: 1.5rem;
        color: #ffffff;
        margin-top: 0.5rem;
    }
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 2rem;
    }
    .stat-box {
        background: rgba(255,255,255,0.2);
        padding: 1rem 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FFD700;
    }
    .stat-label {
        font-size: 1rem;
        color: white;
    }
    .journey-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .philosophy-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-bottom: 5px solid #764ba2;
    }
    .achievement-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 30px;
        display: inline-block;
        margin: 0.3rem;
        font-weight: 500;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .quote-box {
        background: #f0f2f6;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        font-style: italic;
        font-size: 1.2rem;
        color: #2c3e50;
        border: 2px dashed #667eea;
        margin: 2rem 0;
    }
    .social-link {
        background: #0077b5;
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 30px;
        text-decoration: none;
        display: inline-block;
        font-weight: bold;
        transition: transform 0.3s;
    }
    .social-link:hover {
        transform: scale(1.05);
    }
    .milestone-tag {
        background: #667eea;
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section with Enhanced Design ---
st.markdown("""
<div class="founder-header">
    <h1 class="founder-name">👨‍🏫 Mohd Abdul Hameed</h1>
    <p class="founder-title">Data Science & AI Trainer | Mentor | Education Innovator</p>
    <div class="stats-container">
        <div class="stat-box">
            <div class="stat-number">4+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">800+</div>
            <div class="stat-label">Students Trained</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">100%</div>
            <div class="stat-label">Practical Focus</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Quick Achievements Row ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🎯</h3>
        <p><strong>6</strong><br>Max Batch Size</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🚀</h3>
        <p><strong>8+</strong><br>Real Projects</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>💼</h3>
        <p><strong>90%</strong><br>Placement Rate</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🌙</h3>
        <p><strong>Evening</strong><br>Mentorship</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Main Content in Two Columns ---
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("""
    <div class="journey-card">
        <h2>🚀 My Journey</h2>
        <p style="font-size: 1.1rem; line-height: 1.6;">
        I started my journey in Data Science with a strong belief:<br>
        <b style="color: #667eea;">"Practical knowledge is more powerful than theoretical learning."</b>
        </p>
        <p style="margin-top: 1rem;">Over the past 4+ years, I have trained more than 800 students in:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills in badges
    skills = ["Data Science", "AI/ML", "Data Analytics", "SQL", "Power BI", "Python", "Excel", "Deep Learning", "Statistics"]
    for skill in skills:
        st.markdown(f'<span class="achievement-badge">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 2rem;" class="journey-card">
        <h4>📍 Current Role</h4>
        <p><b>Data Science & AI Trainer</b><br>
        Mentoring the next generation of data professionals</p>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown("""
    <div class="journey-card">
        <h2>🎯 Teaching Philosophy</h2>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin: 1rem 0;">✅ <b>Small Batch Size</b> (Max 6 Students) - Personalized attention</li>
            <li style="margin: 1rem 0;">✅ <b>Real-Time Projects</b> - Learn by doing, not just watching</li>
            <li style="margin: 1rem 0;">✅ <b>Hands-On Practice</b> - 70% practical, 30% theory</li>
            <li style="margin: 1rem 0;">✅ <b>Hybrid Learning</b> - Flexibility of online + offline</li>
            <li style="margin: 1rem 0;">✅ <b>Evening Mentorship</b> - Designed for working professionals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="journey-card" style="margin-top: 1rem;">
        <h2>🏆 Milestones</h2>
        <span class="milestone-tag">2019: Started Teaching</span>
        <span class="milestone-tag">2020: 200 Students</span>
        <span class="milestone-tag">2021: 400 Students</span>
        <span class="milestone-tag">2022: 600 Students</span>
        <span class="milestone-tag">2023: 800+ Students</span>
        <span class="milestone-tag">2024: 90% Placement Rate</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Why Started Section ---
st.markdown("""
<div class="philosophy-card">
    <h2 style="text-align: center;">🌍 Why I Started This Institute</h2>
    <div style="display: flex; justify-content: space-around; margin-top: 2rem;">
""", unsafe_allow_html=True)

prob_col1, prob_col2, prob_col3 = st.columns(3)

with prob_col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>📹</h3>
        <h4>Recorded Sessions Only</h4>
        <p>Students receive only recorded content with no live interaction</p>
    </div>
    """, unsafe_allow_html=True)

with prob_col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>🎓</h3>
        <h4>Lack of Practical Training</h4>
        <p>Colleges focus on theory, not real-world skills</p>
    </div>
    """, unsafe_allow_html=True)

with prob_col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>💼</h3>
        <h4>Working Professionals Struggle</h4>
        <p>No time for upskilling, forced to leave jobs to learn</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="quote-box">
    <h3>💡 My Vision</h3>
    <p style="font-size: 1.3rem;">"I wanted to build something different —<br>
    A mentorship-based, practical-driven learning space<br>
    where professionals don't have to choose between work and growth."</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Student Success Stats ---
st.header("📊 Impact & Success")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric(label="Students Trained", value="800+", delta="2024")
with metric_col2:
    st.metric(label="Placement Rate", value="90%", delta="15%")
with metric_col3:
    st.metric(label="Avg. Salary Hike", value="85%", delta="20 LPA Max")
with metric_col4:
    st.metric(label="Happy Students", value="750+", delta="4.8/5 Rating")

st.markdown("---")

# --- Testimonials Section ---
st.header("⭐ What Students Say")

testimonial1, testimonial2, testimonial3 = st.columns(3)

with testimonial1:
    st.markdown("""
    <div class="journey-card" style="text-align: center;">
        <p>⭐⭐⭐⭐⭐</p>
        <p><i>"Best mentor ever! His teaching style makes complex topics simple. Got placed at 12 LPA!"</i></p>
        <p><b>- Priya Sharma</b></p>
        <p>Data Scientist at Amazon</p>
    </div>
    """, unsafe_allow_html=True)

with testimonial2:
    st.markdown("""
    <div class="journey-card" style="text-align: center;">
        <p>⭐⭐⭐⭐⭐</p>
        <p><i>"The evening batches are perfect for working professionals. Learned Power BI and SQL in 2 months!"</i></p>
        <p><b>- Rahul Verma</b></p>
        <p>BI Analyst at Deloitte</p>
    </div>
    """, unsafe_allow_html=True)

with testimonial3:
    st.markdown("""
    <div class="journey-card" style="text-align: center;">
        <p>⭐⭐⭐⭐⭐</p>
        <p><i>"Small batch size makes all the difference. Got personal attention and cleared all doubts."</i></p>
        <p><b>- Neha Gupta</b></p>
        <p>Data Analyst at Flipkart</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Contact & Social Section ---
st.header("📬 Connect With Me")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: #0077b5; padding: 2rem; border-radius: 15px; color: white;">
        <h3 style="color: white;">💼 LinkedIn</h3>
        <p>Connect with me professionally</p>
        <a href="https://www.linkedin.com/in/mohd-abdul-hameed" target="_blank" style="background: white; color: #0077b5; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; font-weight: bold;">View Profile →</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white;">
        <h3 style="color: white;">📧 Email</h3>
        <p>For queries and collaborations</p>
        <p style="font-size: 1.2rem; font-weight: bold;">moabdhad555@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Call to Action ---
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem; border-radius: 20px; text-align: center; color: white;">
    <h2 style="color: white;">🎓 Ready to Start Your Data Science Journey?</h2>
    <p style="font-size: 1.2rem; margin: 1rem 0;">Join 800+ successful students who transformed their careers</p>
    <p style="font-size: 1.5rem; font-weight: bold;">First 3 Classes Free • Limited Seats (6 per batch)</p>
    <div style="margin-top: 2rem;">
        <a href="/Apply_Now" target="_blank" style="background: #FFD700; color: #2c3e50; padding: 1rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold; font-size: 1.2rem;">📩 Book Your Free Demo →</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- Footer Note ---
st.caption("© 2024 Mohd Abdul Hameed | M.A Data Science & AI Hub. All rights reserved.")