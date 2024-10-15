import streamlit as st
from data_wrangling import get_filtered_data_within_date_range, prep_data
from filter_panel import filter_panel
from date_range_panel import date_range_panel
from metric_bar import metric_bar
from time_series_chart import time_series_chart
from pie_chart import pie_chart
from drilldown import drilldown
from query_params import set_widget_defaults, set_params
from info_display import info_display

st.set_page_config(layout='wide')
set_widget_defaults()

with st.sidebar:
  dd_button_container = st.container()
  start, end, compare_start, compare_end = date_range_panel()
  info_display(start, end, compare_start, compare_end)

data = prep_data()
filters = filter_panel(data)

main_df = get_filtered_data_within_date_range(data, start, end, filters)
if main_df.empty:
  st.warning("No data to display")
else:
  compare_df = get_filtered_data_within_date_range(
                  data, compare_start, compare_end, filters)
  metric_bar(main_df, compare_df)
  if dd_button_container.button("Drilldown", use_container_width=True):
    drilldown(main_df, compare_df)
  time_series_col, pie_chart_col = st.columns(2)
  with time_series_col:
    time_series_chart(main_df)
  with pie_chart_col:
    pie_chart(main_df)

set_params()
