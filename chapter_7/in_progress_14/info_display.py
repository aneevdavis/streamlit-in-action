import streamlit as st

def info_display(start, end, compare_start, compare_end):
  display_info = [
    f"**Main date range**:  \n{start.date()} to {end.date()}",
    f"**Compare to**:  \n{compare_start.date()} to {compare_end.date()}",
    f"**Filters**:  \n{get_filter_info()}"
  ]
  st.info("\n\n".join(display_info))

def get_filter_info():
  filter_info = ""
  for key, value in st.session_state.items():
    if key.startswith('w:filter'):
      if value:
        truncated = value[:2] + ['...'] if len(value) > 2 else value
        filter_name = key.split('|')[1]
        filter_info += f"*{filter_name}*: {', '.join(truncated)}  \n"
  return filter_info