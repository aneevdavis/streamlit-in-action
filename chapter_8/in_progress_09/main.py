import streamlit as st

from backend.hub import Hub
from backend.database import Database
from frontend.pages import pages

@st.cache_resource
def get_database():
  connection_string = st.secrets['config']['connection_string']
  database = Database(connection_string)
  return database

if 'hub' not in st.session_state:
  st.session_state.hub = Hub(get_database())

if 'logged_in' in st.session_state and st.session_state.logged_in:
  page = st.navigation([pages['home'], pages['logout']])
else:
  page = st.navigation([pages['login'], pages['signup']])

page.run()
