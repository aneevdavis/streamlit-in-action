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

with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task"):
        add_task(task)

st.write("## To-Do List")
for idx, [task, is_done] in enumerate(st.session_state.task_list):
    task_col, change_status_col, delete_col = st.columns([0.6, 0.2, 0.2])
    task_col.markdown(task if not is_done else f"~~{task}~~")

    change_status_label = "Not done" if is_done else "Done"
    if change_status_col.button(change_status_label, key=f"toggle_{idx}"):
        toggle_done(idx)
        st.rerun()
        
    if delete_col.button("Delete", key=f"delete_{idx}"):
        delete_task(idx)
        st.rerun()
