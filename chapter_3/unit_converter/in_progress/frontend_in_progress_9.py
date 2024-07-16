import streamlit as st
from backend import convert_value, list_quantities, list_units

quantity = st.sidebar.radio("Select a quantity", list_quantities())

st.title("Unit Converter")
input_num = float(st.text_input("Value to convert", value="0"))

units = list_units(quantity)
from_unit_col, to_unit_col = st.columns(2)
from_unit = from_unit_col.selectbox("From", units)
to_unit = to_unit_col.selectbox("To", units, index=1)

if st.button("Convert"):
    result = convert_value(quantity, from_unit, to_unit, input_num)
