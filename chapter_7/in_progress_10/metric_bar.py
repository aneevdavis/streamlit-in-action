import streamlit as st
from metric_config import metrics, display_metrics
from formatting import format_metric
from drilldown import drilldown

def get_metric(df, metric):
  return metric.func(df)

def get_formatted_value(value, metric):
  return format_metric(value, metric.type)

def get_delta(value, compare_df, metric):
  delta = None
  if compare_df is not None:
    compare_value = get_metric(compare_df, metric)
    if compare_value != 0:
      delta = (value - compare_value) / compare_value
  return delta

def get_formatted_delta(value, compare_df, metric):
  delta = get_delta(value, compare_df, metric)
  formatted_delta = None
  if delta is not None:
    formatted_delta = format_metric(delta, "percent")
  return formatted_delta

def metric_bar(main_df, compare_df):
  with st.container(border=True):
    metric_cols = st.columns(len(display_metrics))
    for idx, metric_name in enumerate(display_metrics):
      metric = metrics[metric_name]
      with metric_cols[idx]:
        value = get_metric(main_df, metric)
        formatted_value = get_formatted_value(value, metric)
        formatted_delta = get_formatted_delta(value, compare_df, metric)
        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
          st.metric(
            metric.title, formatted_value, formatted_delta, "normal")
