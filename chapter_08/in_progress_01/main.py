import streamlit as st
from backend.database import Database

st.title('Haiku Haven')

database = Database()
query_results = database.execute_query('SELECT * FROM haikus')
st.write(query_results)
