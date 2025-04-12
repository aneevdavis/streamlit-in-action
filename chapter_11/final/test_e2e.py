import pytest
from streamlit.testing.v1 import AppTest

@pytest.mark.uses_api
def test_movie_search_end_to_end():
  at = AppTest.from_file("frontend.py")
  at.run()

  # Verify initial state has search components
  assert len(at.sidebar.text_input) == 1
  assert len(at.sidebar.button) == 1

  # Enter search query and click button
  at.sidebar.text_input[0].set_value("Inception").run()
  at.sidebar.button[0].click().run()

  # Verify results are in session_state
  assert "results" in at.session_state
  results = at.session_state["results"]

  # Verify there's at least one result
  assert len(results) > 0

  # Verify there's an expander for each result
  assert len(at.expander) == len(results)

  for idx, movie in enumerate(results.values()):
    title = movie["title"]
    assert title in at.expander[idx].label

    # Verify overview is in markdown elements
    overview_text = f"**Overview:** {movie.get('overview', 'N/A')}"
    assert any(overview_text in m.value for m in at.markdown), \
      f"Overview for {title} not found"
