import streamlit as st

quantity = st.sidebar.radio("Select a quantity", ["Mass", "Length", "Time"])

st.title("Unit Converter")
input_num = float(st.text_input("Value to convert", value="0"))

units = ["Kilograms", "Grams", "Pounds", "Ounces"]
from_unit_col, to_unit_col = st.columns(2)
from_unit = from_unit_col.selectbox("From", units)
to_unit = to_unit_col.selectbox("To", units, index=1)

if st.button("Convert"):
    pass