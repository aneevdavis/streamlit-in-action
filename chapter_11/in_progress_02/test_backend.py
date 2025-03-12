import pytest
from unittest.mock import patch, Mock
from backend import Backend, SEARCH_URL
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

