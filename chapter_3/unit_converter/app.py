import streamlit as st
from backend import convert_value, list_quantities, list_units

quantity = st.sidebar.radio("Select a quantity", list_quantities())

st.title("Unit Converter")
input_num = float(st.text_input("Value", value="0"))

units = list_units(quantity)
from_unit_col, to_unit_col = st.columns(2)
from_unit = from_unit_col.selectbox("From", units)
to_unit = to_unit_col.selectbox("To", units, index=1)

if st.button("Convert"):
    result = convert_value(quantity, from_unit, to_unit, input_num)
    from_display = f"{result.from_value} {result.from_unit.abbrev}"
    to_display = f"{result.to_value} {result.to_unit.abbrev}"

    from_result_col, to_result_col = st.columns(2)
    from_value_col, to_value_col = st.columns(2)
    from_value_col.metric("From", from_display, delta=None)
    to_value_col.metric("To", to_display, delta=None)
