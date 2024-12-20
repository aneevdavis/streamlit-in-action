from backend.database import Database
from backend.user_service import UserService
from backend.haiku_service import HaikuService


class Hub:
  def __init__(self, config):
    database = Database(config['connection_string'])
    self.user_service = UserService(database)
    self.haiku_service = HaikuService(database)
