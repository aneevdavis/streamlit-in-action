from backend.user import User

class UserService:
  def __init__(self, database):
    self.database = database

  def get_user(self, username):
    query = "SELECT * FROM users WHERE username = %s"
    params = (username,)
    results = self.database.execute_query(query, params)
    return User(*results[0]) if results else None

  def create_user(self, username, password):
    existing_user = self.get_user(username)
    if not existing_user:
      query = '''
        INSERT INTO users (username, password_hash)
          VALUES (%s, %s)
          RETURNING username, password_hash
      '''
      password_hash = User.hash_password(password)
      params = (username, password_hash)
      results = self.database.execute_query(query, params)
      return User(*results[0]) if results else None
    return None

  def get_authenticated_user(self, username, password):
    user = self.get_user(username)
    if user and user.authenticate(password):
        return user
    return None
