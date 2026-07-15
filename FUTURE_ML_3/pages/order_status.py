import streamlit as st

st.set_page_config(page_title="Order Status", page_icon="📦")

st.title("📦 Order Status")
st.write("Track your order here.")

order_id = st.text_input("Enter your Order ID")

if st.button("Check Status"):
    if order_id:
        st.success(f"✅ Order {order_id} is confirmed and will be delivered soon!")
    else:
        st.warning("⚠️ Please enter your Order ID.")