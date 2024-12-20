import streamlit as st
from backend.hub import Hub

pages = {
  "login": st.Page("frontend/login.py", title="Log in",
                   icon=":material/login:"),
  "signup": st.Page("frontend/signup.py", title="Sign up",
                    icon=":material/person_add:"),
}

if 'hub' not in st.session_state:
  config = st.secrets['config']
  st.session_state.hub = Hub(config)

page = st.navigation([pages['login'], pages['signup']])
page.run()
