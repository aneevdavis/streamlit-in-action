import streamlit as st
from bot import Bot

if "bot" not in st.session_state:
    api_keys = st.secrets["api_keys"]
    st.session_state.bot = Bot(api_keys)
bot = st.session_state.bot

if human_message_text := st.chat_input("Chat with Nibby!"):
    st.chat_message("human").markdown(human_message_text)
    ai_message_text = bot.chat(human_message_text)
    st.chat_message("ai").markdown(ai_message_text)
