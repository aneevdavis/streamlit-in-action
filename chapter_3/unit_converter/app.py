import streamlit as st

from backend import convert_value, list_quantities, list_units

with st.sidebar:
    quantity = st.radio("Select a quantity", list_quantities())

units = list_units(quantity)
st.write("# Unit Converter")

value = st.number_input("Value to convert")

from_unit_col, to_unit_col = st.columns(2)
with from_unit_col:
    from_unit = st.selectbox("From", units)

with to_unit_col:
    to_unit = st.selectbox("To", units)

convert_button_col, reset_button_col, reverse_button_col = st.columns(3)

if st.button("Convert"):
    result = convert_value(quantity, from_unit, to_unit, value)
    from_display_value = f"{value} {result.from_unit.abbreviation}"
    to_display_value = f"{result.to_value} {result.to_unit.abbreviation}"

    from_value_col, arrow_col, to_value_col = st.columns(3)
    from_value_col.metric("From", from_display_value, delta=None)
    arrow_col.metric("", "→")
    to_value_col.metric("To", to_display_value, delta=None)