import streamlit as st
from game import Game

def start_new_game():
  st.session_state.game = Game(st.secrets['llm_api_key'])
  st.rerun()

def new_game_button(game):
  if game and not game.is_over():
    button_text, button_type = "Restart game", "secondary"
  else:
    button_text, button_type = "Start new game", "primary"
  if st.button(button_text, use_container_width=True, type=button_type):
    start_new_game()

game = st.session_state.game if 'game' in st.session_state else None
side_col, main_col = st.columns([2, 3])
with side_col:
  st.header("⚡ Fact Frenzy", divider='gray')
  new_game_button(game)

with main_col:
  if game:
    st.header(
      f"Question {len(game.questions)} / {game.max_questions}",
      divider='gray'
    )
    st.subheader(f"Score: {game.score}")

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

      if game.is_over():
        with st.container(border=True):
          st.markdown(f"Game over! Your final score is: **{game.score}**")
      else:
        st.button(
          "Next question",
          type='primary',
          on_click=lambda: game.proceed_to_next_question()
        )
