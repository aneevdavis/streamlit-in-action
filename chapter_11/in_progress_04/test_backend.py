import pytest
from unittest.mock import patch, Mock
from backend import Backend, SEARCH_URL, POSTER_URL_PREFIX
from mock_data import MOCK_MOVIES, MOCK_RESULTS

@pytest.fixture
def backend():
  api_key = "test_api_key"
  return Backend(api_key)

@patch('requests.get')
def test_search_movies_success(mock_get, backend):
  mock_response = Mock()
  mock_response.json.return_value = {'results': MOCK_MOVIES}
  mock_get.return_value = mock_response

  results = backend.search_movies("test query")

  mock_get.assert_called_once_with(
    SEARCH_URL,
    params={"api_key": backend.api_key, "query": "test query"}
  )
  assert len(results) == len(MOCK_MOVIES)
  for _id, movie in MOCK_RESULTS.items():
    assert _id in results
    assert results[_id]["title"] == movie["title"]

@patch('requests.get')
def test_search_movies_no_results(mock_get, backend):
  mock_response = Mock()
  mock_response.json.return_value = {'results': []}
  mock_get.return_value = mock_response

  result = backend.search_movies("query with no matching results")
  assert result == []

def test_get_poster_url():
  poster_path = "/test_path.jpg"
  expected_url = f"{POSTER_URL_PREFIX}{poster_path}"
  result_url = Backend.get_poster_url(poster_path)
  assert result_url == expected_url

def test_get_nonexistent_poster_url():
  poster_path = None
  expected_url = POSTER_URL_PREFIX
  result_url = Backend.get_poster_url(poster_path)
  assert result_url == expected_url
