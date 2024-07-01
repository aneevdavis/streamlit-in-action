import streamlit as st

task_list = []

def add_task(task):
    task_list.append([task, False])

def toggle_done(idx):
    task_list[idx][1] = not task_list[idx][1]

def delete_task(idx):
    del task_list[idx]

total_tasks = len(task_list)
completed_tasks = sum(1 for _, is_done in task_list if is_done)
metric_display = f"{completed_tasks}/{total_tasks} done"
st.metric("Task completion", metric_display, delta=None)

with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task"):
        add_task(task)

st.write("## Today's to-dos:")
for idx, [task, is_done] in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    label = task if not is_done else f"~~{task}~~"
    checkbox = task_col.checkbox(label, is_done)
    if checkbox:
        toggle_done(idx)
    elif not checkbox:
        toggle_done(idx)

    if delete_col.button("Delete", key=f"delete_{idx}"):
        delete_task(idx)
