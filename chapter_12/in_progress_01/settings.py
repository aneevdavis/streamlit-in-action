import streamlit as st

QM_OPTIONS = ["Alex Trebek", "Eminem", "Gollum", "Gruk the Caveman"]
DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"]

default_settings = {
  "Quizmaster": [QM_OPTIONS[0]],
  "Difficulty": [DIFFICULTY_OPTIONS[1]]
}

def settings_editor():
  with st.popover("Settings", use_container_width=True):
    return st.data_editor(
      default_settings,
      key='settings_editor',
      column_config={
        'Quizmaster': st.column_config.SelectboxColumn(
          options=QM_OPTIONS, required=True),
        'Difficulty': st.column_config.SelectboxColumn(
          options=DIFFICULTY_OPTIONS, required=True)
      },
      num_rows='fixed',
      use_container_width=True,
    )
