import streamlit as st
from bot import Bot

if "bot" not in st.session_state:
  api_keys = st.secrets["api_keys"]
  config = st.secrets["config"]
  st.session_state.bot = Bot(api_keys, config)
bot = st.session_state.bot

for message in bot.get_history():
  st.chat_message(message.type).markdown(message.content)

if human_message_text := st.chat_input("Chat with Nibby!"):
  st.chat_message("human").markdown(human_message_text)
  ai_message_text = bot.chat(human_message_text)
  st.chat_message("ai").markdown(ai_message_text)
