import streamlit as st
from data_loader import load_data

def get_unique_values(df, column):
  return list(df[column].unique())

def clean_column_names(df):
  df.columns = df.columns.str.replace('_', ' ').str.capitalize()
  return df

@st.cache_data(show_spinner="Reading sales data...", ttl="1d")
def prep_data():
  return clean_column_names(load_data())