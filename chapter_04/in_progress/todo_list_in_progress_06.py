import streamlit as st
from task import Task

task_list = []

def add_task(task_name: str):
    task_list.append(Task(task_name))

def delete_task(idx: int):
    del task_list[idx]

def mark_done(task: Task):
    task.is_done = True

def mark_not_done(task: Task):
    task.is_done = False

with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task", type="primary"):
        add_task(task)

st.header("Today's to-dos:", divider="gray")
for idx, task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    task_col.checkbox(task.name, task.is_done, key=f"task_{idx}")
    if delete_col.button("Delete", key=f"delete_{idx}"):
        pass
