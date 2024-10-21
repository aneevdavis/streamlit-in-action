import streamlit as st
from datetime import date, timedelta

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
THIRTY_DAYS_AGO = TODAY - timedelta(days=30)

named_ranges = ["This month", "This quarter", "This year"]

def get_named_date_range(range_name):
  start_dates = {
    "This month": TODAY.replace(day=1),
    "This quarter": TODAY.replace(
      day=1, month=TODAY.month - TODAY.month % 3 + 1),
    "This year": TODAY.replace(day=1, month=1),
  }
  return start_dates[range_name], TODAY

def date_range_panel():
  main_range = st.selectbox("Date range", named_ranges + ["Custom"])
  if main_range == "Custom":
    start = st.date_input("Start date", value=THIRTY_DAYS_AGO)
    end = st.date_input("End date", value=TODAY)
  else:
    start, end = get_named_date_range(main_range)
  return start, end
