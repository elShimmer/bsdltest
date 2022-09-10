from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit
import streamlit as st

"""
# Welcome to the BSDL_Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# page1.py

if "shared" not in st.session_state:
   st.session_state["shared"] = True

# page2.py
import streamlit as st
st.write(st.session_state["shared"])
# If page1 already executed, this should write True
