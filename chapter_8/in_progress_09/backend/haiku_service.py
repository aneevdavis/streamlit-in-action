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

  def get_haikus_by_author(self, author):
    query = 'SELECT * FROM haikus WHERE author = %s'
    params = (author,)
    results = self.database.execute_query(query, params)
    return [Haiku(*row) for row in results]

  def update_haiku(self, haiku_id, haiku_text):
    query = 'UPDATE haikus SET text = %s WHERE haiku_id = %s RETURNING *'
    params = (haiku_text, haiku_id)
    results = self.database.execute_query(query, params)
    return Haiku(*results[0]) if results else None

  def delete_haiku(self, haiku_id):
    query = 'DELETE FROM haikus WHERE haiku_id = %s RETURNING *'
    params = (haiku_id,)
    results = self.database.execute_query(query, params)
    return Haiku(*results[0]) if results else None

