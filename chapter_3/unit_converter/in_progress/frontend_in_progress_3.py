import streamlit as st
from backend import convert_value, list_quantities, list_units

quantity = st.radio("Select a quantity", list_quantities())