import streamlit as st
from frontend.haiku_editor import haiku_editor
from frontend.haiku_display import display_haiku
from frontend.icons import ADD

hub = st.session_state.hub
user = st.session_state.user
st.title(f"Welcome, {user.username}!")

if st.button(f'{ADD} Haiku', type='primary'):
  haiku_editor(hub, user)

st.header(f"{user.username}'s haikus", divider="grey")
haikus = hub.haiku_service.get_haikus_by_author(user.username)
if len(haikus) == 0:
  st.info("You haven't written any haikus yet.")
else:
  for haiku in haikus:
    display_haiku(haiku)
