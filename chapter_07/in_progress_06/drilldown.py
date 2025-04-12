import pandas as pd
import streamlit as st
from metric_config import metrics

def drilldown_dimensions():
  return st.multiselect(
    "Drilldown fields",
    ["Age group", "Gender", "Category", "Segment", "Product name", "State"]
  )

def get_metric_cols(df):
  metrics_dict = {met: metric.func(df) for met, metric in metrics.items()}
  return pd.Series(metrics_dict)

def get_aggregate_metrics(df, dimensions):
  if dimensions:
    grouped = df.groupby(dimensions)
    return grouped.apply(get_metric_cols).reset_index()
  metric_cols = get_metric_cols(df)
  return pd.DataFrame(metric_cols).T

def get_drilldown_table(df, dimensions):
  aggregated = get_aggregate_metrics(df, dimensions)
  return aggregated

def display_drilldown_table(df):
  if df is None:
    st.warning("No data available for selected filters and date range")
  else:
    st.dataframe(df, use_container_width=True, hide_index=True)

@st.dialog("Drilldown", width="large")
def drilldown(main_df, compare_df):
  dimensions = drilldown_dimensions()
  main_data = get_drilldown_table(main_df, dimensions)
  compare_data = get_drilldown_table(compare_df, dimensions)

  main_tab, compare_tab = st.tabs(["Main", "Compare"])
  with main_tab:
    display_drilldown_table(main_data)
  with compare_tab:
    display_drilldown_table(compare_data)
