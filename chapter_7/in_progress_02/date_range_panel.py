import streamlit as st
from datetime import date, timedelta

TODAY = date.fromisoformat("2024-08-31") # Hardcode to last date in dataset
THIRTY_DAYS_AGO = TODAY - timedelta(days=30)

def date_range_panel():
  start = st.date_input("Start date", value=THIRTY_DAYS_AGO)
  end = st.date_input("End date", value=TODAY)
  return start, end
