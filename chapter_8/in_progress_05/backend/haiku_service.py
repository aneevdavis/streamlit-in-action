from backend.haiku import Haiku

class HaikuService:
  def __init__(self, database):
    self.database = database

  def create_haiku(self, author, haiku_text):
    query = '''
      INSERT INTO haikus (author, text)
      VALUES (%s, %s)
      RETURNING haiku_id, created_at, author, text
    '''
    params = (author, haiku_text)
    results = self.database.execute_query(query, params)
    return Haiku(*results[0]) if results else None
