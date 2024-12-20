from backend.database import Database
from backend.user_service import UserService


class Hub:
  def __init__(self, config):
    database = Database(config['connection_string'])
    self.user_service = UserService(database)
