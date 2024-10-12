import pandas as pd
import streamlit as st
from data_loader import load_data

def get_unique_values(df, column):
  return list(df[column].unique())

def clean_column_names(df):
  df.columns = df.columns.str.replace('_', ' ').str.capitalize()
  return df

def apply_filters(df, filters):
  for col, values in filters.items():
    if values:
      df = df[df[col].isin(values)]
  return df

@st.cache_data(show_spinner="Reading sales data...", ttl="1d")
def prep_data() -> pd.DataFrame:
  df = clean_column_names(load_data())
  df['Day'] = pd.to_datetime(df['Date'])
  return df

def get_data_within_date_range(df, start, end):
  if start is not None and end is not None:
    return df[(df['Day'] >= start) & (df['Day'] <= end)]
  return df

def get_filtered_data_within_date_range(df, start, end, filters):
  df_within_range = get_data_within_date_range(df.copy(), start, end)
  return apply_filters(df_within_range, filters)
