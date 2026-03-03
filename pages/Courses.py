import streamlit as st

st.set_page_config(page_title="Courses", layout="wide")

st.title("📚 Our Programs")
st.markdown("### Choose Your Learning Path")

st.markdown("---")

st.subheader("🎓 Data Science Master Program")
st.write("4 Months | Hybrid | ₹35,000")
st.page_link("pages/Data_Science.py", label="View Details", icon="🚀")

st.subheader("🤖 Artificial Intelligence & Machine Learning")
st.write("4 Months | Hybrid | ₹40,000")
st.page_link("pages/AIML.py", label="View Details", icon="🧠")

st.subheader("📊 Data Analytics")
st.write("3 Months | Hybrid | ₹30,000")
st.page_link("pages/Data_analytics.py", label="View Details", icon="📈")

st.subheader("🧠 SQL Professional")
st.write("Short Term | ₹8,000")
st.page_link("pages/SQL.py", label="View Details", icon="💾")

st.subheader("📊 Power BI Mastery")
st.write("₹8,000")
st.page_link("pages/Power_BI.py", label="View Details", icon="📊")

st.subheader("🐍 Python for Data Analysis")
st.write("₹10,000")
st.page_link("pages/Python.py", label="View Details", icon="🐍")

st.subheader("📊 Excel & Advanced Excel")
st.write("₹7,000")
st.page_link("pages/Excel.py", label="View Details", icon="📑")