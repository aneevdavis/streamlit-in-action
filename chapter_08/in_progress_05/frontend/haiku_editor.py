import streamlit as st

@st.dialog("Haiku editor", width="large")
def haiku_editor(hub, user):
  haiku_text = st.text_area('Enter a haiku')
  if st.button('Save haiku', type='primary'):
    haiku = hub.haiku_service.create_haiku(user.username, haiku_text)
    if haiku:
      st.success('Haiku saved successfully!')
      st.rerun()
    else:
      st.error('Failed to save haiku')
