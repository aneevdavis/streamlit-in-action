from backend.haiku import Haiku

class HaikuService:
  def __init__(self, database):
    self.database = database

  def create_haiku(self, author, haiku_text):
    query = '''
      INSERT INTO haikus (author, text)
      VALUES (:author, :text)
      RETURNING haiku_id, created_at, author, text
    '''
    params = {'author': author, 'text': haiku_text}
    results = self.database.execute_query(query, params, write=True)
    return Haiku(*results[0]) if results else None

  def get_haikus_by_author(self, author):
    query = 'SELECT * FROM haikus WHERE author = :author'
    params = {'author': author}
    results = self.database.execute_query(query, params)
    return [Haiku(*row) for row in results]

  def update_haiku(self, haiku_id, haiku_text):
    query = '''
      UPDATE haikus SET text = :text WHERE haiku_id = :id RETURNING *
    '''
    params = {'text': haiku_text, 'id': haiku_id}
    results = self.database.execute_query(query, params, write=True)
    return Haiku(*results[0]) if results else None

  def delete_haiku(self, haiku_id):
    query = 'DELETE FROM haikus WHERE haiku_id = :id RETURNING *'
    params = {'id': haiku_id}
    results = self.database.execute_query(query, params, write=True)
    return Haiku(*results[0]) if results else None
