import streamlit as st

@st.dialog("Drilldown", width="large")
def drilldown(main_df, compare_df, metric):
  main_tab, compare_tab = st.tabs(["Main", "Compare"])
  with main_tab:
    st.dataframe(main_df, use_container_width=True, hide_index=True)
  with compare_tab:
    st.dataframe(compare_df, use_container_width=True, hide_index=True)