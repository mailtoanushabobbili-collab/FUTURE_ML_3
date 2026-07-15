import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "data", "customer_faq.csv")

faq_data = pd.read_csv(file_path)

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if user_input in greetings:
        return "👋 Hello! Welcome to Customer Support. How can I help you today?"

    # Order Status
    if "order" in user_input:
        return "📦 Please enter your Order ID to check your order status."

    # FAQ Matching
    for index, row in faq_data.iterrows():
        if user_input == row["Question"].lower():
            return row["Answer"]

    # Fallback
    return """❓ Sorry, I couldn't understand your question.

You can ask me about:
• Order Status
• Refund Policy
• Shipping
• Payment Methods
• Contact Support
"""