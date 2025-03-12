import pytest
import toml
from backend import Backend
from unittest.mock import patch, Mock
from mock_data import MOCK_MOVIES, MOCK_RESULTS
from streamlit.testing.v1 import AppTest

@pytest.fixture
def setup_app():
  at = AppTest.from_file("frontend.py")
  at.secrets["api_key"] = "test_api_key"
  return at

@patch('requests.get')
def test_frontend_backend_integration(mock_get, setup_app):
  mock_response = Mock()
  mock_response.json.return_value = {'results': MOCK_MOVIES}
  mock_get.return_value = mock_response

  at = setup_app
  at.run()

  # Enter search query and click button
  at.sidebar.text_input[0].set_value("test movie").run()
  at.sidebar.button[0].click().run()

  # Verify results are in session_state
  assert "results" in at.session_state
  assert at.session_state["results"] == MOCK_RESULTS

  # Verify expanders are displayed
  expected_expanders = len(MOCK_MOVIES)
  actual_expanders = len(at.expander)
  assert actual_expanders == expected_expanders, \
    f"Expected {expected_expanders} expanders, found {actual_expanders}"

@pytest.mark.uses_api
def test_backend_api_integration():
  secrets = toml.load(".streamlit/secrets.toml")
  backend = Backend(secrets["api_key"])
  results = backend.search_movies("ferris bueller")

  # Assert that there's at least one result
  assert len(results.keys()) > 0, "No results returned from backend API"

  # Assert that 1986 classic "Ferris Bueller's Day Off" is in the results
  has_fbdo_movie = any(
    movie["title"] == "Ferris Bueller's Day Off"
      and movie["release_date"].startswith("1986")
    for _id, movie in results.items()
  )
  assert has_fbdo_movie, "Ferris Bueller's Day Off not found in results"
