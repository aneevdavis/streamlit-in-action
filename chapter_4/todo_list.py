import streamlit as st

if "task_list" not in st.session_state:
    st.session_state.task_list = []
def add_task(task):
    st.session_state.task_list.append([task, False])

def mark_as_done(idx):
    st.session_state.task_list[idx][1] = True

task = st.text_input("Enter a task")
if st.button("Add task"):
    add_task(task)

st.write("## To-Do List")
for idx, [task, is_done] in enumerate(st.session_state.task_list):
    task_col, mark_as_done_col = st.columns(2)
    task_col.markdown(task if not is_done else f"~~{task}~~")
    if mark_as_done_col.button("Mark as done", key=idx):
        mark_as_done(idx)
        st.rerun()
