import streamlit as st

quantity = st.sidebar.radio("Select a quantity", ["Mass", "Length", "Time"])

st.title("Unit Converter")
input_num = float(st.text_input("Value to convert", value="0"))