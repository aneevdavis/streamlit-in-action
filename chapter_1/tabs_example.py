import streamlit as st

tab1, tab2, tab3 = st.tabs(["Mission", "About us", "Careers"])
with tab1:
    st.header("Our Mission")
    st.write("Our mission is to teach people to make web apps in Python.")

with tab2:
    st.header("About Us")
    st.write("We are a group of Python enthusiasts.")

with tab3:
    st.header("Careers")
    st.write("We are hiring! Apply today!")