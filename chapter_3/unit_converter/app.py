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

def render_app() -> None:
    st.title("Unit Converter")

    quantity = st.sidebar.radio("Select a quantity", list_quantities())
    units = list_units(quantity)

    value = float(st.text_input("Value to convert", value="0"))

    from_unit_col, to_unit_col = st.columns(2)
    with from_unit_col:
        from_unit = st.selectbox("From", units)
    with to_unit_col:
        to_unit = st.selectbox("To", units, index=1)

    places = None
    if st.checkbox("Round result", value=False):
        places = st.number_input("Decimal places to round to", value=2)

    result = convert_value(quantity, from_unit, to_unit, value)
    from_display = format_value(value, result.from_unit.abbrev)
    to_display = format_value(
        result.to_value, result.to_unit.abbrev, places)

    from_value_col, to_value_col = st.columns(2)
    from_value_col.metric("From", from_display, delta=None)
    to_value_col.metric("To", to_display, delta=None)

render_app()