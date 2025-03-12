import pytest
from unittest.mock import patch
from streamlit.testing.v1 import AppTest
from mock_data import MOCK_RESULTS

class MockBackend:
  @staticmethod
  def get_poster_url(path):
    return "https://mock-image-server.com/poster.jpg"

  def __init__(self, api_key):
    self.api_key = api_key

  def search_movies(self, query):
    return MOCK_RESULTS

@pytest.fixture
def setup_app():
  at = AppTest.from_file("frontend.py")
  at.secrets["api_key"] = "test_api_key"
  return at

@patch("backend.Backend", MockBackend)
def test_initial_state(setup_app):
  at = setup_app
  at.run()

  # Check if sidebar has search input and button
  assert len(at.sidebar.text_input) == 1
  assert len(at.sidebar.button) == 1
  assert "Search" in at.sidebar.button[0].label

  # Check that results are not visible initially
  assert "results" not in at.session_state
  assert len(at.expander) == 0

