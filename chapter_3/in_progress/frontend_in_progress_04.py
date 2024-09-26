import streamlit as st

quantity = st.sidebar.radio("Select a quantity", ["Mass", "Length", "Time"])
st.title("Unit Converter")