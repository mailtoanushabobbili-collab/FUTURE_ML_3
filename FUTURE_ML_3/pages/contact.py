import streamlit as st

st.set_page_config(page_title="Contact Support", page_icon="📞")

st.title("📞 Contact Support")

st.write("Need help? Contact us.")

st.markdown("""
📧 Email: support@example.com

📞 Phone: +91-9876543210

🕒 Working Hours:
Monday - Saturday
9:00 AM - 6:00 PM
""")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")