import streamlit as st

def get_param(key):
  return st.query_params.get(key, None)

def set_widget_defaults():
  for key in st.query_params:
    if key.startswith('w:') and key not in st.session_state:
      st.session_state[key] = get_param(key)

def set_params():
  query_params_dict = {}
  for key in st.session_state:
    if key.startswith('w:'):
      value = st.session_state[key]
      query_params_dict[key] = value
      st.query_params[key] = value
  st.query_params.from_dict(query_params_dict)
