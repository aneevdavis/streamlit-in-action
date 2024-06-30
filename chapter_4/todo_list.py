import streamlit as st

if "task_list" not in st.session_state:
    st.session_state.task_list = []

def add_task(task):
    st.session_state.task_list.append([task, False])

def toggle_done(idx):
    current_status = st.session_state.task_list[idx][1]
    st.session_state.task_list[idx][1] = not current_status

def delete_task(idx):
    del st.session_state.task_list[idx]

task_list = st.session_state.task_list
total_tasks = len(task_list)
completed_tasks = sum(1 for _, is_done in task_list if is_done)
metric_display = f"{completed_tasks}/{total_tasks} done"
st.metric("Task completion", metric_display, delta=None)

with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task"):
        add_task(task)
        st.rerun()

st.write("## To-Do List")
for idx, [task, is_done] in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    label = task if not is_done else f"~~{task}~~"
    checkbox = task_col.checkbox(label, is_done, key=f"checkbox_{idx}")
    if checkbox and not is_done:
        toggle_done(idx)
        st.rerun()
    elif not checkbox and is_done:
        toggle_done(idx)
        st.rerun()

    if delete_col.button("Delete", key=f"delete_{idx}"):
        delete_task(idx)
        st.rerun()
