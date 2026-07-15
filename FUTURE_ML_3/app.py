import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Chatbot", page_icon="🤖")

# 🎨 Custom CSS (COLORS)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
    }
    .box {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .order {background-color: #2196F3;}
    .refund {background-color: #FF9800;}
    .contact {background-color: #9C27B0;}
    .shipping {background-color: #009688;}
    .payment {background-color: #E91E63;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 Customer Support Chatbot</div>', unsafe_allow_html=True)
st.write("Ask anything 👇")

# Session states
for key in ["order", "refund", "contact", "shipping", "payment"]:
    if key not in st.session_state:
        st.session_state[key] = False

# Input
user_input = st.text_input("💬 Type your question:")

# Detect intent
if user_input:
    text = user_input.lower()

    for key in st.session_state:
        st.session_state[key] = False

    if "order" in text:
        st.session_state.order = True

    elif "refund" in text:
        st.session_state.refund = True

    elif "contact" in text:
        st.session_state.contact = True

    elif "shipping" in text:
        st.session_state.shipping = True

    elif "payment" in text:
        st.session_state.payment = True

    else:
        st.success(get_response(user_input))

# 🎨 ORDER
if st.session_state.order:
    st.markdown('<div class="box order">📦 Track Your Order</div>', unsafe_allow_html=True)
    order_id = st.text_input("Order ID")

    if st.button("Track Order"):
        st.success(f"✅ Order {order_id} is on the way!")

# 🎨 REFUND
if st.session_state.refund:
    st.markdown('<div class="box refund">💰 Refund Status</div>', unsafe_allow_html=True)
    refund_id = st.text_input("Refund ID")

    if st.button("Check Refund"):
        st.success(f"💰 Refund {refund_id} processed!")

# 🎨 CONTACT
if st.session_state.contact:
    st.markdown('<div class="box contact">📞 Contact Us</div>', unsafe_allow_html=True)
    st.write("📧 support@example.com")
    st.write("📱 +1 234 567 890")

# 🎨 SHIPPING
if st.session_state.shipping:
    st.markdown('<div class="box shipping">🚚 Shipping Info</div>', unsafe_allow_html=True)
    st.write("Standard: 3-5 days")
    st.write("Express: 1-2 days")

# 🎨 PAYMENT
if st.session_state.payment:
    st.markdown('<div class="box payment">💳 Payment Methods</div>', unsafe_allow_html=True)
    st.write("- Cards")
    st.write("- UPI")
    st.write("- Net Banking")