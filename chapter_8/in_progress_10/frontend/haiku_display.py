import streamlit as st
from frontend.haiku_editor import haiku_editor
from frontend.icons import CALENDAR, CLOCK, EDIT, DELETE

hub = st.session_state.hub
user = st.session_state.user

def get_haiku_created_display(haiku):
  day = haiku.created_at.strftime('%Y-%m-%d')
  time = haiku.created_at.strftime('%H:%M')
  return f':gray[{CALENDAR} {day}  \n {CLOCK} {time}]'

def get_haiku_text_display(haiku):
  display_text = haiku.text.replace('\n', '  \n')
  return f':green[{display_text}]'

def edit_button(haiku):
  if st.button(f'{EDIT}', key=f"edit_{haiku.haiku_id}"):
    haiku_editor(hub, user, haiku)

def delete_button(haiku):
  if st.button(f'{DELETE}', key=f"delete_{haiku.haiku_id}"):
    deleted_haiku = hub.haiku_service.delete_haiku(haiku.haiku_id)
    if deleted_haiku:
      st.rerun()
    else:
      st.error("Failed to delete haiku.")

def display_haiku(haiku):
  with st.container(border=True):
    cols = st.columns([2, 5, 1, 1])
    created_col, text_col, edit_col, delete_col = cols

    created_col.markdown(get_haiku_created_display(haiku))
    text_col.markdown(get_haiku_text_display(haiku))
    with edit_col:
      edit_button(haiku)
    with delete_col:
      delete_button(haiku)
