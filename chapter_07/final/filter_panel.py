import streamlit as st
from data_wrangling import get_unique_values, apply_filters

filter_dims = ["Age group", "Gender", "Category", "Segment",
               "Product name", "State"]

def filter_panel(df):
  filters = {}
  with st.expander("Filters"):
    filter_cols = st.columns(len(filter_dims))
    effective_df = df
    for idx, dim in enumerate(filter_dims):
      with filter_cols[idx]:
        effective_df = apply_filters(effective_df, filters)
        unique_vals = get_unique_values(effective_df, dim)
        filters[dim] = st.multiselect(
          dim, unique_vals, key=f'w:filter|{dim}')
  return filters
