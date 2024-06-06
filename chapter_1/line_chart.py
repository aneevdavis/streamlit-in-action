import streamlit as st
import random

st.title("Die Roll Simulator")
num_rolls = st.slider('Number of die rolls', min_value=10, max_value=100)
if st.button('Plot Graph'):
    die_rolls = [random.randint(1, 6) for _ in range(num_rolls)]
    st.line_chart(data=die_rolls)
