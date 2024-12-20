import streamlit as st
from frontend.haiku_editor import haiku_editor

hub = st.session_state.hub
user = st.session_state.user
st.title(f"Welcome, {user.username}!")

if st.button(':material/add_circle: Haiku', type='primary'):
    haiku_editor(hub, user)
