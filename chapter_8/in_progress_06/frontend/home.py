import streamlit as st
from frontend.haiku_editor import haiku_editor
from frontend.haiku_display import display_haiku

hub = st.session_state.hub
user = st.session_state.user
st.title(f"Welcome, {user.username}!")

if st.button(':material/add_circle: Haiku', type='primary'):
    haiku_editor(hub, user)

st.header(f"{user.username}'s haikus", divider="grey")
haikus = hub.haiku_service.get_haikus_by_author(user.username)
for haiku in haikus:
  display_haiku(haiku)
