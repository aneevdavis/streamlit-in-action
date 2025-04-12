import streamlit as st

hub = st.session_state.hub

with st.container(border=True):
  st.title("Log in")
  username = st.text_input("Username", key="login_username")
  password = st.text_input("Password", type="password")

  if st.button("Log in", type="primary"):
    user = hub.user_service.get_authenticated_user(username, password)
    if user:
      st.session_state.logged_in = True
      st.session_state.user = user
      st.success("Logged in successfully")
    else:
      st.error("Invalid username or password")
