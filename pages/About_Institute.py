import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="M.A Data Science & AI Hub", 
    page_icon="🏫",
    layout="wide"
)

# --- Custom CSS for Institute Page ---
st.markdown("""
<style>
    .institute-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    .institute-name {
        font-size: 3rem;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .institute-tagline {
        font-size: 1.5rem;
        color: #ffffff;
        margin-top: 1rem;
        font-style: italic;
    }
    .mission-vision-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        height: 100%;
        transition: transform 0.3s;
        border-bottom: 5px solid #1e3c72;
    }
    .mission-vision-card:hover {
        transform: translateY(-5px);
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s;
        border: 1px solid #e0e0e0;
    }
    .feature-card:hover {
        transform: scale(1.05);
        border-color: #1e3c72;
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .stat-box {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
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
    .location-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #1e3c72;
    }
    .benefit-tag {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 30px;
        display: inline-block;
        margin: 0.3rem;
        font-weight: 500;
    }
    .quote-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.3rem;
        font-style: italic;
    }
    .batch-highlight {
        background: #FFD700;
        color: #1e3c72;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="institute-header">
    <h1 class="institute-name">🏫 M.A Data Science & AI Hub</h1>
    <p class="institute-tagline">Evening Mentorship for Future Data Professionals</p>
    <div style="margin-top: 2rem;">
        <span class="batch-highlight">Limited Seats: 6 per batch</span>
        <span class="batch-highlight" style="margin-left: 1rem;">First 3 Classes Free</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Mission & Vision in Columns ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="mission-vision-card">
        <h2 style="color: #1e3c72;">🎯 Our Mission</h2>
        <p style="font-size: 1.2rem; line-height: 1.6;">
        To create industry-ready Data Professionals <br>
        <strong>without forcing them to leave their job or college.</strong>
        </p>
        <div style="margin-top: 1rem;">
            <span class="benefit-tag">Working Professionals</span>
            <span class="benefit-tag">College Students</span>
            <span class="benefit-tag">Career Switchers</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="mission-vision-card">
        <h2 style="color: #1e3c72;">👁 Our Vision</h2>
        <p style="font-size: 1.2rem; line-height: 1.6;">
        To become the most <strong>practical and skill-focused</strong><br>
        Data Science training hub in the region.
        </p>
        <div style="margin-top: 1rem;">
            <span class="benefit-tag">100% Practical</span>
            <span class="benefit-tag">Industry Focused</span>
            <span class="benefit-tag">Skill First</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Key Statistics ---
st.markdown("## 📊 Institute at a Glance")

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">800+</div>
        <div class="stat-label">Students Trained</div>
    </div>
    """, unsafe_allow_html=True)

with stat2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">4+</div>
        <div class="stat-label">Years Experience</div>
    </div>
    """, unsafe_allow_html=True)

with stat3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">90%</div>
        <div class="stat-label">Placement Rate</div>
    </div>
    """, unsafe_allow_html=True)

with stat4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">6</div>
        <div class="stat-label">Max Batch Size</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- What Makes Us Different ---
st.markdown("## 💡 What Makes Us Different")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">👥</div>
        <h3>Small Batches</h3>
        <p><strong>6 Students Only</strong></p>
        <p>Personalized attention for every student. No crowded classrooms.</p>
    </div>
    """, unsafe_allow_html=True)

with feature2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔄</div>
        <h3>Hybrid Mode</h3>
        <p><strong>Offline + Online</strong></p>
        <p>Flexibility to learn from anywhere. Best of both worlds.</p>
    </div>
    """, unsafe_allow_html=True)

with feature3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3>Real Projects</h3>
        <p><strong>3+ Live Projects</strong></p>
        <p>Build portfolio while you learn. Industry-ready skills.</p>
    </div>
    """, unsafe_allow_html=True)

feature4, feature5, feature6 = st.columns(3)

with feature4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎁</div>
        <h3>Free Demo</h3>
        <p><strong>First 3 Classes Free</strong></p>
        <p>Experience our teaching before you commit.</p>
    </div>
    """, unsafe_allow_html=True)

with feature5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📜</div>
        <h3>Certification</h3>
        <p><strong>Industry Recognized</strong></p>
        <p>Get certified and boost your career.</p>
    </div>
    """, unsafe_allow_html=True)

with feature6:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💳</div>
        <h3>EMI Options</h3>
        <p><strong>Flexible Payment</strong></p>
        <p>Learn now, pay later. Zero cost EMI available.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Programs Offered ---
st.markdown("## 📚 Programs We Offer")

programs = st.columns(3)

with programs[0]:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
        <h3 style="color: #1e3c72;">📊 Data Science</h3>
        <p>Complete Data Science with ML & AI</p>
        <p><strong>6 Months • ₹45,000</strong></p>
    </div>
    """, unsafe_allow_html=True)

with programs[1]:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
        <h3 style="color: #1e3c72;">📈 Data Analytics</h3>
        <p>Excel, SQL, Python, Power BI, Tableau</p>
        <p><strong>4 Months • ₹35,000</strong></p>
    </div>
    """, unsafe_allow_html=True)

with programs[2]:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
        <h3 style="color: #1e3c72;">🤖 AI/ML</h3>
        <p>Machine Learning, Deep Learning, GenAI</p>
        <p><strong>6 Months • ₹55,000</strong></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Location Section with Map ---
st.markdown("## 📍 Our Location")

loc_col1, loc_col2 = st.columns([1, 1])

with loc_col1:
    st.markdown("""
    <div class="location-card">
        <h3 style="color: #1e3c72;">🏢 Visit Us</h3>
        <p style="font-size: 1.2rem;">
        <strong>13-6-823/39/1</strong><br>
        Langar House, Hashim Nagar<br>
        Hyderabad - 500008<br>
        </p>
        <div style="margin-top: 1rem;">
            <p>📍 <strong>Landmark:</strong> Near Langar House Bus Stop</p>
            <p>🕒 <strong>Timings:</strong> 6:00 PM - 9:00 PM (Evening Batches)</p>
            <p>📞 <strong>Phone:</strong> +91 98765 43210</p>
            <p>📧 <strong>Email:</strong> info@madatascience.com</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with loc_col2:
    # Embed Google Map (using iframe)
    st.markdown("""
    <div style="border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15225.876209786842!2d78.376182!3d17.406047!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb93dc8c5d69df%3A0x1963b3ae2b3b3c9!2sLangar%20House%2C%20Hyderabad%2C%20Telangana!5e0!3m2!1sen!2sin!4v1620000000000!5m2!1sen!2sin" 
            width="100%" 
            height="300" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy">
        </iframe>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Upcoming Batches ---
st.markdown("## 🗓️ Upcoming Batches")

batch1, batch2, batch3 = st.columns(3)

with batch1:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; border: 2px solid #1e3c72; text-align: center;">
        <h4 style="color: #1e3c72;">Data Science</h4>
        <p><strong>Start Date:</strong> April 15, 2024</p>
        <p><strong>Timing:</strong> 7:00 PM - 9:00 PM</p>
        <p><strong>Seats Left:</strong> 3/6</p>
        <span class="batch-highlight">Hurry!</span>
    </div>
    """, unsafe_allow_html=True)

with batch2:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; border: 2px solid #1e3c72; text-align: center;">
        <h4 style="color: #1e3c72;">Data Analytics</h4>
        <p><strong>Start Date:</strong> April 20, 2024</p>
        <p><strong>Timing:</strong> 8:00 PM - 10:00 PM</p>
        <p><strong>Seats Left:</strong> 4/6</p>
        <span class="batch-highlight">Weekend Batch</span>
    </div>
    """, unsafe_allow_html=True)

with batch3:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; border: 2px solid #1e3c72; text-align: center;">
        <h4 style="color: #1e3c72;">AI/ML</h4>
        <p><strong>Start Date:</strong> May 1, 2024</p>
        <p><strong>Timing:</strong> 7:00 PM - 9:00 PM</p>
        <p><strong>Seats Left:</strong> 5/6</p>
        <span class="batch-highlight">Early Bird</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Testimonials ---
st.markdown("## ⭐ What Our Students Say")

test1, test2 = st.columns(2)

with test1:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <p>⭐⭐⭐⭐⭐</p>
        <p><i>"The evening batches are perfect for working professionals. Got placed at 12 LPA!"</i></p>
        <p><strong>- Priya Sharma</strong> (Data Scientist at Amazon)</p>
    </div>
    """, unsafe_allow_html=True)

with test2:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <p>⭐⭐⭐⭐⭐</p>
        <p><i>"Small batch size makes all the difference. Personalized attention and practical learning."</i></p>
        <p><strong>- Rahul Verma</strong> (BI Analyst at Deloitte)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Quote Box ---
st.markdown("""
<div class="quote-box">
    <p style="font-size: 2rem;">"</p>
    <p>Building Skills. Not Just Certificates.</p>
    <p style="font-size: 2rem;">"</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Call to Action ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3c72;">🎯 Ready to Start Your Journey?</h3>
        <p style="font-size: 1.2rem;">First 3 Classes Free • Limited Seats (6 per batch)</p>
        <div style="margin-top: 2rem;">
            <a href="/Apply_Now" target="_blank" style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 1rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold; font-size: 1.2rem;">📩 Book Your Free Demo →</a>
        </div>
        <p style="margin-top: 1rem;">📍 Visit us at Langar House, Hyderabad</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 10px;">
    <p>© 2024 M.A Data Science & AI Hub. All rights reserved.</p>
    <p>📍 Langar House, Hyderabad | 📞 +91 98765 43210 | 📧 moabdhad555@gmail.com</p>
</div>
""", unsafe_allow_html=True)