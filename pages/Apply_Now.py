import streamlit as st

st.set_page_config(page_title="Apply Now", layout="wide")

st.title("🚀 Apply for Free 3 Evening Demo Classes")
st.subheader("Limited to 6 Students Per Batch")

st.markdown("---")

# Replace this link with your actual Google Form embed link
google_form_url = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?embedded=true"

st.markdown(
    f"""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeicND5RW7r9u1fcwlQVPHcmSKuut2JBx1KAUo1EFwafEx6LA/viewform?embedded=true" width="640" height="1434" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """,
    unsafe_allow_html=True
)