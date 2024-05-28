import streamlit as st
from backend import convert_value, list_quantities, list_units

def format_value(
        value: float,
        unit_abbrev: str,
        decimal_places: int = None) -> str:
    is_rounded = decimal_places is not None
    rounded = round(value, decimal_places) if is_rounded else value
    formatted = format(rounded, ",")
    return f"{formatted} {unit_abbrev}"

quantity = st.sidebar.radio("Select a quantity", list_quantities())

st.title("Unit Converter")
input_num = float(st.text_input("Value", value="0"))

units = list_units(quantity)
from_unit_col, to_unit_col = st.columns(2)
from_unit = from_unit_col.selectbox("From", units)
to_unit = to_unit_col.selectbox("To", units, index=1)

places = None
if st.checkbox("Round result?", value=False):
    places = st.number_input(
        "Decimal places to round to", value=2, min_value=0)

if st.button("Convert"):
    result = convert_value(quantity, from_unit, to_unit, input_num)
    from_display = format_value(input_num, result.from_unit.abbrev)
    to_display = format_value(
        result.to_value, result.to_unit.abbrev, places)

    from_result_col, to_result_col = st.columns(2)
    from_value_col, to_value_col = st.columns(2)
    from_value_col.metric("From", from_display, delta=None)
    to_value_col.metric("To", to_display, delta=None)
