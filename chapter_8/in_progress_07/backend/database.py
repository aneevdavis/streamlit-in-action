import streamlit as st
from sqlalchemy import text

class Database:
  def __init__(self):
    self.conn = st.connection("haikudb", type="sql")

  def execute_query(self, query, params=(), write=False):
    with self.conn.session as session:
      result = session.execute(text(query), params)
      if write:
        session.commit()
      return result.fetchall()
