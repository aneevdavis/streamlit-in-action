import requests

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
POSTER_URL_PREFIX = "https://image.tmdb.org/t/p/w500"

class Backend:
  def __init__(self, api_key):
    self.api_key = api_key

  def search_movies(self, query):
    params = {"api_key": self.api_key, "query": query}
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    results = response.json().get('results', [])
    return {movie["id"]: movie for movie in results}

  @staticmethod
  def get_poster_url(poster_path):
    return f"{POSTER_URL_PREFIX}{poster_path if poster_path else ''}"
