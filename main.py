import streamlit as st

st.write(
    "This is a landing page designed to showcase the simple authentication library."
)
st.write(
    "This is just a single import and a function to run, and the return value is either None, or the authenticated username."
)
st.write(
    "The user login is usually based in the sidebar (though ultimately configurable by passing True or False to the sidebar parameter of the auth function"
)
st.write(
    "All the user management and username and password entry should be taken care of by the library. To automatically have creation and edit access, just run the library directly as a streamlit script."
)

from authlib import auth

data = auth()  # auth(sidebar=False) or auth(False) if you don't want the sidebar
"""This both displays authentication input in the sidebar, and then returns the credentials for use locally"""

st.write(f"{'AUTHENTICATED!' if data else 'NOT authenticated'}")
st.write(
    f"Authentication data received = {data} (which is the username that has logged in)"
)
