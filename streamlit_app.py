import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml
from utils import setup_navigation  # Import the global function


st.set_page_config(
    page_title="Elderly Care",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

pg = setup_navigation()  # Call the function to setup navigation
pg.run()  # Run the navigation system
