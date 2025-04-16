import os
import streamlit as st
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-..." # Replace with your own API key
openai = OpenAI()

human_message = lambda m: {"role": "user", "content": m}
ai_message = lambda m: {"role": "assistant", "content": m}

def talk_to_ai(question, history):
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=history + [human_message(question)],
    ).choices[0].message.content

st.session_state.history = st.session_state.get("history", [])
history = st.session_state.history

for message in history:
    st.chat_message(message["role"]).markdown(message["content"])

prompt= st.chat_input("Chat with me!")
if prompt:
    st.chat_message("human").markdown(prompt)
    response = talk_to_ai(prompt, history)
    history.extend([human_message(prompt), ai_message(response)])
    st.chat_message("ai").markdown(response)
