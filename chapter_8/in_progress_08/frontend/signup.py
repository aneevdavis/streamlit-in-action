import streamlit as st
from frontend.pages import pages

hub = st.session_state.hub

with st.container(border=True):
  st.title("Sign up")
  username = st.text_input("Username")
  password = st.text_input("Password", type="password")
  confirm_password = st.text_input("Confirm password", type="password")

  if st.button("Create account", type="primary"):
    if password != confirm_password:
      st.error("Passwords do not match")
    else:
      user = hub.user_service.create_user(username, password)
      if user:
        st.success("Account created successfully")
      else:
        st.error("Username already exists")

st.page_link(pages["login"], label="Already have an account? Log in!")
