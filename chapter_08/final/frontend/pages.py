import streamlit as st
from frontend.icons import LOGIN, LOGOUT, SIGNUP, HOME

pages = {
  "login": st.Page("frontend/login.py", title="Log in", icon=LOGIN),
  "signup": st.Page("frontend/signup.py", title="Sign up", icon=SIGNUP),
  "home": st.Page("frontend/home.py", title="Home", icon=HOME),
  "logout": st.Page("frontend/logout.py", title="Log out", icon=LOGOUT)
}
