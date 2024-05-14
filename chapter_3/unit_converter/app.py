import streamlit as st

from backend import convert_value, list_quantities, list_units

with st.sidebar:
    quantity = st.radio("Select a quantity", list_quantities())

units = list_units(quantity)
st.title("Unit Converter")

value = st.number_input("Value to convert")

from_unit_col, to_unit_col = st.columns(2)
with from_unit_col:
    from_unit = st.selectbox("From", units)

with to_unit_col:
    to_unit = st.selectbox("To", units)

convert_button_col, reset_button_col, reverse_button_col = st.columns(3)

if st.button("Convert"):
    result = convert_value(quantity, from_unit, to_unit, value)
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}")