import pandas as pd
import streamlit as st
from datetime import date

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
ONE_MONTH_AGO = TODAY.replace(month=TODAY.month - 1)

named_ranges = ["This month", "This quarter", "This year"]

def get_named_date_range(range_name):
  start_dates = {
    "This month": TODAY.replace(day=1),
    "This quarter": TODAY.replace(
      day=1, month=TODAY.month - TODAY.month % 3),
    "This year": TODAY.replace(day=1, month=1),
  }
  return start_dates[range_name], TODAY

def date_range_panel():
  main_range = st.selectbox("Date range", named_ranges + ["Custom"])
  if main_range == "Custom":
    start = st.date_input("Start date", value=ONE_MONTH_AGO)
    end = st.date_input("End date", value=TODAY)
  else:
    start, end = get_named_date_range(main_range)
  return pd.to_datetime(start), pd.to_datetime(end)
