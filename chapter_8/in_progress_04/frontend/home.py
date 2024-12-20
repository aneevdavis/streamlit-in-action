import streamlit as st

user = st.session_state.user
st.title(f"Welcome, {user.username}!")