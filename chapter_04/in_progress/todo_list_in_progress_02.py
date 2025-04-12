import streamlit as st
from task import Task

task_list = [Task("Buy milk"), Task("Walk the dog")]

st.header("Today's to-dos:", divider="gray")
for task in task_list:
    st.checkbox(task.name, task.is_done)

