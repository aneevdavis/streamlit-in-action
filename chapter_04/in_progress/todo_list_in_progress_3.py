import streamlit as st
from task import Task

task_list = [Task("Buy milk"), Task("Walk the dog")]

st.header("Today's to-dos:", divider="gray")
for task in task_list:
    task_col, delete_col = st.columns([0.8, 0.2])
    task_col.checkbox(task.name, task.is_done)
    if delete_col.button("Delete"):
        pass
