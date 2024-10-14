import pandas as pd
import streamlit as st
from datetime import date

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
ONE_MONTH_AGO = TODAY.replace(month=TODAY.month - 1)

def date_range_panel():
  start = st.date_input("Start date", value=ONE_MONTH_AGO)
  end = st.date_input("End date", value=TODAY)
  return pd.to_datetime(start), pd.to_datetime(end)
