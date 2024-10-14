import plotly.graph_objs as go
import streamlit as st
from data_wrangling import get_metric_time_series
from metric_config import metrics, display_metrics
from dimension_config import time_chart_dims

def get_time_series_chart(df, metric, grain, splits):
  data = get_metric_time_series(df, metric, grain, splits)
  dimension = splits[0] if splits else None
  groups = data[dimension].unique() if splits else ['All']
  fig = go.Figure()
  for group in groups:
    group_data = data[data[dimension] == group] if splits else data
    fig.add_trace(
      go.Scatter(
        x=group_data[grain],
        y=group_data['Value'],
        mode='lines+markers',
        name=group
      )
    )

  fig.update_layout(
    title=f"{metric.title}" + (f" by {dimension}" if splits else ""),
    xaxis_title=grain,
    yaxis_title=metric.title,
    showlegend=True
  )
  return fig

def time_series_chart(df):
  with st.container(border=True):
    grain_options = ["Day", "Week", "Month", "Year"]
    grain_col, split_col = st.columns([2, 1])
    grain = grain_col.select_slider("Time grain", grain_options)
    split_dimension = split_col.selectbox(
      "Group by", ["None"] + time_chart_dims, key="ts_split")
    splits = [split_dimension] if split_dimension != "None" else []
    chart_tabs = st.tabs(display_metrics)
    for idx, met in enumerate(display_metrics):
      with chart_tabs[idx]:
        chart = get_time_series_chart(df, metrics[met], grain, splits)
        st.plotly_chart(chart, use_container_width=True)
