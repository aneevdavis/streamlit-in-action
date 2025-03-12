import streamlit as st
from backend import Backend

backend = Backend(st.secrets["api_key"])

with st.sidebar:
  movie_query = st.text_input("Search for a movie")
  if st.button("Search", type="primary"):
    st.session_state.results = backend.search_movies(movie_query)

if "results" in st.session_state:
  for _, movie in st.session_state.results.items():
    title, date = movie["title"], movie["release_date"]
    year = date.split("-")[0] if date else "N/A"
    with st.expander(f"{title} ({year})"):
      poster_url = Backend.get_poster_url(movie.get('poster_path', None))
      st.image(poster_url, width=250)
      st.markdown(f"**Overview:** {movie.get('overview', 'N/A')}")
      st.markdown(f"**Rating:** {movie.get('rating', 'N/A')}")
