import streamlit as st

st.set_page_config(page_title="Payment", page_icon="💳")

st.title("💳 Payment Methods")

st.write("We accept:")

st.markdown("""
- 💳 Credit Card
- 💳 Debit Card
- 📱 UPI
- 🏦 Net Banking
- 💵 Cash on Delivery
""")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")