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
      day=1, month=TODAY.month - TODAY.month % 3 + 1),
    "This year": TODAY.replace(day=1, month=1),
  }
  return start_dates[range_name], TODAY

def get_prev_period(start, end, comparison):
  offsets = {
    "MoM": pd.DateOffset(months=1),
    "QoQ": pd.DateOffset(months=3),
    "YoY": pd.DateOffset(years=1),
  }
  offset = offsets.get(comparison, pd.DateOffset((end - start).days + 1))
  return start - offset, end - offset

def main_date_range(range_name):
  if range_name == "Custom":
    start = st.date_input(
          "Start date", value=THIRTY_DAYS_AGO, key="w:main_start")
    end = st.date_input("End date", value=TODAY, key="w:main_end")
  else:
    start, end = get_named_date_range(range_name)
  return pd.to_datetime(start), pd.to_datetime(end)

def compare_date_range(range_name, start, end):
  allowed_comparisons = {
    "This month": ["MoM", "QoQ", "YoY"],
    "This quarter": ["QoQ", "YoY"],
    "This year": ["YoY"],
    "Custom": ["MoM", "QoQ", "YoY"]
  }
  options = (
    ["Previous period"]
    + allowed_comparisons.get(range_name, [])
    + ["Custom"]
  )
  comparison = st.selectbox("Compare to", options, key="w:compare_range")
  if comparison == "Custom":
    compare_start = st.date_input(
          "Compare start date", key="w:compare_start")
    compare_end = st.date_input("Compare end date", key="w:compare_end")
  else:
    compare_start, compare_end = get_prev_period(start, end, comparison)
  return pd.to_datetime(compare_start), pd.to_datetime(compare_end)

def date_range_panel():
  range_name = st.selectbox(
        "Date range", named_ranges + ["Custom"], key="w:main_range")
  start, end = main_date_range(range_name)
  compare_start, compare_end = compare_date_range(range_name, start, end)
  return start, end, compare_start, compare_end
