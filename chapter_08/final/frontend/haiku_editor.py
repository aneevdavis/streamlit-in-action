import streamlit as st

@st.dialog("Haiku editor", width="large")
def haiku_editor(hub, user, haiku=None):
  default_text = haiku.text if haiku else ''
  haiku_text = st.text_area('Enter a haiku', value=default_text)
  if st.button('Save haiku', type='primary'):
    if haiku:
      new_haiku = hub.haiku_service.update_haiku(haiku.haiku_id, haiku_text)
    else:
      new_haiku = hub.haiku_service.create_haiku(user.username, haiku_text)
    if new_haiku:
      st.success('Haiku saved successfully!')
      st.rerun()
    else:
      st.error('Failed to save haiku')
