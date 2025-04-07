from backend.database import Database
from backend.user_service import UserService


class Hub:
  def __init__(self):
    database = Database()
    self.user_service = UserService(database)
