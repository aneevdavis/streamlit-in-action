import streamlit as st
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [21, 28, 19, 26, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
edited_df = st.data_editor(df, num_rows="dynamic", key='data_editor')

st.write("Average age:", edited_df['Age'].mean())