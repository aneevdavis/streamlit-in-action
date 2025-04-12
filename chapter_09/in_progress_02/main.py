import streamlit as st
from game import Game

game = Game(st.secrets['llm_api_key'])

question = game.ask_llm_for_question()
st.container(border=True).write(question)

answer = st.text_input("Enter your answer")
if st.button("Submit"):
  evaluation = game.ask_llm_to_evaluate_answer(question, answer)
  if evaluation.is_correct:
    st.success("That's correct!")
  else:
    st.error("Sorry, that's incorrect.")
    st.info(f"The correct answer was: {evaluation.correct_answer}")
