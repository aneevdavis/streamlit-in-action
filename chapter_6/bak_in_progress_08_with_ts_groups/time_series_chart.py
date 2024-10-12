import plotly.graph_objs as go
import streamlit as st

from metric_config import metrics, display_metrics

def get_metric_time_series(df, metric, splits):
  grouped = df.groupby(splits + ['Day'])
  data = grouped.apply(metric.func, include_groups=False).reset_index()
  data.columns = splits + ['Day', 'Value']
  return data

def get_time_series_chart(df, metric, splits):
  data = get_metric_time_series(df, metric, splits)
  dimension = splits[0] if splits else None
  fig = go.Figure()
  groups = data[dimension].unique() if splits else ['All']
  for group in groups:
    group_data = data[data[dimension] == group] if splits else data
    fig.add_trace(
      go.Scatter(
        x=group_data['Day'],
        y=group_data['Value'],
        mode='lines+markers',
        name=group
      )
    )

  fig.update_layout(
    title=f"{metric.title}" + (f" by {dimension}" if splits else ""),
    xaxis_title='Day',
    yaxis_title=metric.title,
    showlegend=True
  )
  return fig

def time_series_chart(df):
  with st.container(border=True):
    split_selection = st.selectbox("Group by", ["None", "Age group", "Gender", "State", "Category"])
    splits = [split_selection] if split_selection != "None" else []
    chart_tabs = st.tabs(display_metrics)
    for idx, met in enumerate(display_metrics):
      with chart_tabs[idx]:
        chart = get_time_series_chart(df, metrics[met], splits)
        st.plotly_chart(chart, use_container_width=True)
