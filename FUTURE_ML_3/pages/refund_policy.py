import streamlit as st

st.set_page_config(page_title="Refund Policy", page_icon="💰")

st.title("💰 Refund Policy")

st.info("""
Our refund policy:

• Return within 30 days.
• Product should be unused.
• Original invoice is required.
• Refund will be processed within 5-7 working days.
""")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")