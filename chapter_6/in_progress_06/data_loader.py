import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SALES_DATA_PATH = BASE_DIR / "sales_data.csv"

def load_data():
  return pd.read_csv(SALES_DATA_PATH)