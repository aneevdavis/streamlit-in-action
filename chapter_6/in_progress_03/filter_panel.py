import streamlit as st
from data_wrangling import get_unique_values

filter_dims = ["age_group", "gender", "category", "segment",
               "product_name", "state"]

def filter_panel(df):
  with st.expander("Filters"):
    filter_cols = st.columns(len(filter_dims))
    for idx, dim in enumerate(filter_dims):
      with filter_cols[idx]:
        unique_vals = get_unique_values(df, dim)
        st.multiselect(dim, unique_vals)