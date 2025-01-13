import streamlit as st
from game import Game

game = Game(st.secrets['llm_api_key'])

question = game.ask_llm_for_question()
st.container(border=True).write(question)
