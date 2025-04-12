import streamlit as st
from sqlalchemy import text

class Database:
  def __init__(self):
    self.conn = st.connection("haikuconn", type="sql")

  def execute_query(self, query, params={}, write=False):
    with self.conn.session as session:
      try:
        result = session.execute(text(query), params)
        if write:
          session.commit()
        return result.fetchall()
      except Exception:
        if write:
          session.rollback()
        raise
