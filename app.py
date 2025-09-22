import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("❌ GEMINI_API_KEY environment variable not set!")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Choose model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit page setup
st.set_page_config(page_title="Phoenix Helpline", page_icon="🦅")
st.title("🦅 Phoenix Helpline")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Gemini API
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"❌ Error: {e}"

    # Store bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
