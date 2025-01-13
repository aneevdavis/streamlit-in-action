import streamlit as st
from game import Game

if 'game' not in st.session_state:
  st.session_state.game = Game(st.secrets['llm_api_key'])
game = st.session_state.game

if game.status == 'GET_QUESTION':
  with st.spinner('Obtaining question...') as status:
    question = game.obtain_question()
    st.rerun()

elif game.status == 'ASK_QUESTION':
  st.container(border=True).write(game.curr_question)
  answer = st.text_input("Enter your answer")
  if st.button("Submit", type='primary'):
    game.accept_answer(answer)
    st.rerun()

elif game.status == 'EVALUATE_ANSWER':
  with st.spinner('Evaluating answer...') as status:
    game.evaluate_answer()
    st.rerun()

elif game.status == 'STATE_RESULT':
  if game.curr_eval.is_correct:
    st.success("That's correct!")
  else:
    st.error("Sorry, that's incorrect.")
    st.info(f"The correct answer was: {game.curr_eval.correct_answer}")
