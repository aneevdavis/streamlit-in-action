from psycopg2.pool import ThreadedConnectionPool

MIN_CONNECTIONS = 1
MAX_CONNECTIONS = 10


class Database:
  def __init__(self, connection_string):
    self.connection_pool = ThreadedConnectionPool(
      MIN_CONNECTIONS, MAX_CONNECTIONS, connection_string
    )

  def connect(self):
    return self.connection_pool.getconn()

  def close(self, connection):
    self.connection_pool.putconn(connection)

  def close_all(self):
    print("Closing all connections...")
    self.connection_pool.closeall()

  def execute_query(self, query, params=()):
    connection = self.connect()
    try:
      cursor = connection.cursor()
      cursor.execute(query, params)
      results = cursor.fetchall()
      connection.commit()
      return results
    except Exception:
      connection.rollback()
      raise
    finally:
      self.close(connection)
