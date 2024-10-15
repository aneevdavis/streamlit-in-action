import pandas as pd
import streamlit as st
from dimension_config import drilldown_dims
from metric_config import metrics

def drilldown_dimensions():
  return st.multiselect("Drilldown fields", drilldown_dims)

def get_metric_cols(df, metric_name):
  metrics_dict = {metric_name: metrics[metric_name].func(df)}
  return pd.Series(metrics_dict)

def get_aggregate_drilldown_data(df, metric_name, dimensions):
  if dimensions:
    grouped = df.groupby(dimensions)
    return grouped.apply(get_metric_cols, metric_name).reset_index()
  return get_metric_cols(df, metric_name).reset_index()

def get_drilldown_table(df, metric_name, dimensions):
  aggregated = get_aggregate_drilldown_data(df, metric_name, dimensions)
  return aggregated

def display_drilldown_table(df):
  if df is None:
    st.warning("No data available for selected filters and date range")
  else:
    st.dataframe(df, use_container_width=True, hide_index=True)

@st.dialog("Drilldown", width="large")
def drilldown(main_df, compare_df, metric_name):
  dimensions = drilldown_dimensions()
  main_data = get_drilldown_table(main_df, metric_name, dimensions)
  compare_data = get_drilldown_table(compare_df, metric_name, dimensions)

  main_tab, compare_tab = st.tabs(["Main", "Compare"])
  with main_tab:
    display_drilldown_table(main_data)
  with compare_tab:
    display_drilldown_table(compare_data)