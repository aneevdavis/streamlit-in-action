import streamlit as st
from data_wrangling import apply_filters, prep_data
from filter_panel import filter_panel

st.set_page_config(layout='wide')

data = prep_data()
filters = filter_panel(data)

main_df = apply_filters(data, filters)
st.write(main_df.head(5))
