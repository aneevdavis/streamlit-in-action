import streamlit as st
from data_wrangling import prep_data
from filter_panel import filter_panel

st.set_page_config(layout='wide')

data = prep_data()
filter_panel(data)
st.write(data.head(5))
