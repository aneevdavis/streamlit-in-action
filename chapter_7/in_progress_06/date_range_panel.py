import pandas as pd
import streamlit as st
from datetime import date, timedelta

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
THIRTY_DAYS_AGO = TODAY - timedelta(days=30)

named_ranges = ["This month", "This quarter", "This year"]

def get_named_date_range(range_name):
  start_dates = {
    "This month": TODAY.replace(day=1),
    "This quarter": TODAY.replace(
      day=1, month=TODAY.month - TODAY.month % 3),
    "This year": TODAY.replace(day=1, month=1),
  }
  return start_dates[range_name], TODAY

def main_date_range(range_name):
  if range_name == "Custom":
    start = st.date_input("Start date", value=THIRTY_DAYS_AGO)
    end = st.date_input("End date", value=TODAY)
  else:
    start, end = get_named_date_range(range_name)
  return start, end

def compare_date_range():
  compare_start = st.date_input("Compare start date")
  compare_end = st.date_input("Compare end date")
  return pd.to_datetime(compare_start), pd.to_datetime(compare_end)

def date_range_panel():
  range_name = st.selectbox("Date range", named_ranges + ["Custom"])
  start, end = main_date_range(range_name)
  compare_start, compare_end = compare_date_range()
  return start, end, compare_start, compare_end
