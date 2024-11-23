import pandas as pd
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
SALES_DATA_PATH = BASE_DIR / "sales_data.csv"

@st.cache_data(show_spinner="Reading sales data...", ttl="1d")
def load_data():
  return pd.read_csv(SALES_DATA_PATH, dtype_backend='pyarrow')