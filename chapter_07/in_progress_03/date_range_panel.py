import pandas as pd
import streamlit as st
from datetime import date, timedelta

# Hardcode this to the last date in dataset to ensure reproducibility
LATEST_DATE = date.fromisoformat("2024-08-31")
THIRTY_DAYS_AGO = LATEST_DATE - timedelta(days=30)

def get_compare_range(start, end, comparison):
  offsets = {
    "MoM": pd.DateOffset(months=1),
    "QoQ": pd.DateOffset(months=3),
    "YoY": pd.DateOffset(years=1),
    "Previous period": pd.DateOffset((end - start).days + 1)
  }
  offset = offsets[comparison]
  return (start - offset).date(), (end - offset).date()

def date_range_panel():
  start = st.date_input("Start date", value=THIRTY_DAYS_AGO)
  end = st.date_input("End date", value=LATEST_DATE)
  comparison = st.selectbox(
    "Compare to", ["MoM", "QoQ", "YoY", "Previous period"])
  compare_start, compare_end = get_compare_range(start, end, comparison)
  st.info(f"Comparing with:  \n{compare_start} - {compare_end}")
  return start, end, compare_start, compare_end
