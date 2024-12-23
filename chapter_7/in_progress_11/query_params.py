import streamlit as st
from datetime import date

def get_param(key):
  if key not in st.query_params:
    return None
  value = st.query_params[key]
  if value.startswith('L#'):
    return value[2:].split(',')
  if value.startswith('D#'):
    return date.fromisoformat(value[2:])
  return value

def set_widget_defaults():
  for key in st.query_params:
    if key.startswith('w:') and key not in st.session_state:
      st.session_state[key] = get_param(key)

def set_params():
  query_params_dict = {}
  for key in st.session_state:
    if key.startswith('w:'):
      value = st.session_state[key]
      if value:
        if isinstance(value, list):
          value = f'L#{','.join(value)}'
        elif isinstance(value, date):
          value = f'D#{value.isoformat()}'
        query_params_dict[key] = value
  st.query_params.from_dict(query_params_dict)
