import streamlit as st

pages = {
  "login": st.Page("frontend/login.py", title="Log in",
                   icon=":material/login:"),
  "signup": st.Page("frontend/signup.py", title="Sign up",
                    icon=":material/person_add:"),
  "home": st.Page("frontend/home.py", title="Home",
                  icon=":material/home:"),
  "logout": st.Page("frontend/logout.py", title="Log out",
                    icon=":material/logout:")
}
