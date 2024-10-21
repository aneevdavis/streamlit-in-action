import plotly.graph_objects as go
import streamlit as st
from data_wrangling import get_metric_grouped_by_dimension
from metric_config import metrics, pie_chart_display_metrics
from dimension_config import pie_chart_dims

def get_pie_chart(df, metric, dimension):
  data = get_metric_grouped_by_dimension(df, metric, dimension)
  fig = go.Figure()
  fig.add_trace(
    go.Pie(labels=data[dimension], values=data['Value'], hole=0.4)
  )
  return fig

def pie_chart(df):
  with st.container(border=True):
    split_dimension = st.selectbox("Group by", pie_chart_dims)
    metric_tabs = st.tabs(pie_chart_display_metrics)
    for idx, met in enumerate(pie_chart_display_metrics):
      with metric_tabs[idx]:
        chart = get_pie_chart(df, metrics[met], split_dimension)
        st.plotly_chart(chart, use_container_width=True)
