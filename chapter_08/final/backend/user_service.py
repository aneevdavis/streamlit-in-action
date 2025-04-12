from backend.user import User

class UserService:
  def __init__(self, database):
    self.database = database

  def get_user(self, username):
    query = "SELECT * FROM users WHERE username = :username"
    params = {'username': username}
    results = self.database.execute_query(query, params)
    return User(*results[0]) if results else None

  def create_user(self, username, password):
    existing_user = self.get_user(username)
    if not existing_user:
      query = '''
        INSERT INTO users (username, password_hash)
          VALUES (:username, :password_hash)
          RETURNING username, password_hash
      '''
      password_hash = User.hash_password(password)
      params = {'username': username, 'password_hash': password_hash}
      results = self.database.execute_query(query, params, write=True)
      return User(*results[0]) if results else None
    return None

  def get_authenticated_user(self, username, password):
    user = self.get_user(username)
    if user and user.authenticate(password):
        return user
    return None
