import streamlit as st
from data_wrangling import get_unique_values

filter_dims = ["Age group", "Gender", "Category", "Segment",
               "Product name", "State"]

def filter_panel(df):
  with st.expander("Filters"):
    filter_cols = st.columns(len(filter_dims))
    for idx, dim in enumerate(filter_dims):
      with filter_cols[idx]:
        unique_vals = get_unique_values(df, dim)
        st.multiselect(dim, unique_vals)