import streamlit as st
from backend.database import Database

st.title('Haiku Haven')

connection_string = st.secrets['config']['connection_string']
database = Database(connection_string)
query_results = database.execute_query('SELECT * FROM haikus')
st.write(query_results)
