import streamlit as st
from data_loader import load_data

data = load_data()
st.write(data.head(5))
