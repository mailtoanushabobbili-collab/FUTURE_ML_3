import streamlit as st

st.set_page_config(page_title="Shipping", page_icon="🚚")

st.title("🚚 Shipping Information")

st.success("""
Shipping Details

• Standard Delivery : 3-5 Days
• Express Delivery : 1-2 Days
• Free Shipping above ₹499
""")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")