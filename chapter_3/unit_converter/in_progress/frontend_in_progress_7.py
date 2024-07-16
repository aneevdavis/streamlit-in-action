import streamlit as st
from backend import convert_value, list_quantities, list_units

quantity = st.sidebar.radio("Select a quantity", list_quantities())

st.title("Unit Converter")
input_num = float(st.text_input("Value to convert", value="0"))

units = list_units(quantity)
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units, index=1)