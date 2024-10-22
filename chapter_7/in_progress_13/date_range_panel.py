import pandas as pd
import streamlit as st
from datetime import date, timedelta

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
THIRTY_DAYS_AGO = TODAY - timedelta(days=30)

named_ranges = ["This month", "This quarter", "This year"]
named_comparisons = ["MoM", "QoQ", "YoY", "Previous period"]

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
    "Previous period": pd.DateOffset((end - start).days + 1)
  }
  offset = offsets[comparison]
  return (start - offset).date(), (end - offset).date()

def main_date_range():
  main_range = st.selectbox(
              "Date range", named_ranges + ["Custom"], key="w:main_range")
  if main_range == "Custom":
    start = st.date_input(
            "Start date", value=THIRTY_DAYS_AGO, key="w:main_start")
    end = st.date_input("End date", value=TODAY, key="w:main_end")
  else:
    start, end = get_named_date_range(main_range)
  return start, end

def compare_date_range(start, end):
  comparison = st.selectbox(
    "Compare to", named_comparisons + ["Custom"], key="w:compare_range")
  if comparison == "Custom":
    compare_start = st.date_input(
                    "Compare start date", key="w:compare_start")
    compare_end = st.date_input("Compare end date", key="w:compare_end")
  else:
    compare_start, compare_end = get_prev_period(start, end, comparison)
  return compare_start, compare_end

def date_range_panel():
  start, end = main_date_range()
  compare_start, compare_end = compare_date_range(start, end)
  return start, end, compare_start, compare_end
