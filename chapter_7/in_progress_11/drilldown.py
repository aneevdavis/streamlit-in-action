import pandas as pd
import streamlit as st
from dimension_config import drilldown_dims
from metric_config import metrics
from data_wrangling import get_unique_values, apply_filters

def drilldown_dimensions():
  return st.multiselect("Drilldown fields", drilldown_dims)

def drilldown_filters(df, dimensions):
  filters = {}
  if dimensions:
    filter_cols = st.columns(len(dimensions))
    for idx, dim in enumerate(dimensions):
      with filter_cols[idx]:
        values = get_unique_values(df, dim)
        selected = st.selectbox(dim, ["All"] + values)
        filters[dim] = [selected] if selected != "All" else []
  return filters

def get_metric_cols(df):
  metrics_dict = {met: metric.func(df) for met, metric in metrics.items()}
  return pd.Series(metrics_dict)

def get_aggregate_metrics(df, dimensions):
  if dimensions:
    grouped = df.groupby(dimensions)
    return grouped.apply(get_metric_cols).reset_index()
  metric_cols = get_metric_cols(df)
  return pd.DataFrame(metric_cols).T

def add_total_row(df, all_df, dimensions):
  total_metrics = get_metric_cols(all_df)
  if dimensions:
    dim_vals = {dim: '' for dim in dimensions}
    dim_vals[dimensions[0]] = 'Total'
    total_row = pd.DataFrame({**dim_vals, **total_metrics}, index=[0])
    return pd.concat([total_row, df], ignore_index=True)
  total_row = pd.DataFrame({'': 'Total', **total_metrics}, index=[0])
  return total_row

def get_drilldown_table(df, dimensions, filters):
  filtered = apply_filters(df, filters)
  if filtered.empty:
    return None
  aggregated = get_aggregate_metrics(filtered, dimensions)
  with_total = add_total_row(aggregated, filtered, dimensions)
  return with_total

def display_drilldown_table(df):
  if df is None:
    st.warning("No data available for selected filters and date range")
  else:
    st.dataframe(df, use_container_width=True, hide_index=True)

@st.dialog("Drilldown", width="large")
def drilldown(main_df, compare_df):
  dimensions = drilldown_dimensions()
  filters = drilldown_filters(main_df, dimensions)

  main_data = get_drilldown_table(main_df, dimensions, filters)
  compare_data = get_drilldown_table(compare_df, dimensions, filters)

  main_tab, compare_tab = st.tabs(["Main", "Compare"])
  with main_tab:
    display_drilldown_table(main_data)
  with compare_tab:
    display_drilldown_table(compare_data)