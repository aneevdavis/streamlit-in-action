from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest
from mock_data import MOCK_MOVIES, MOCK_RESULTS

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

@patch("backend.Backend", MockBackend)
def test_search_functionality(setup_app):
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

@patch("backend.Backend", MockBackend)
def test_movie_details_display(setup_app):
  """Test that movie details are displayed correctly within expanders"""
  at = setup_app

  # Set up session state with search results
  at.session_state["results"] = MOCK_RESULTS
  at.run()

  # Verify expanders are created
  assert len(at.expander) == 2

  # Verify both movies' details are in the markdown elements
  markdown_texts = [m.value for m in at.markdown]
  for movie in MOCK_MOVIES:
    overview_text = f"**Overview:** {movie['overview']}"
    rating_text = f"**Rating:** {movie['vote_average']}"

    assert any(overview_text in text for text in
               markdown_texts), f"Overview for {movie['title']} not found"
    assert any(rating_text in text for text in
               markdown_texts), f"Rating for {movie['title']} not found"
