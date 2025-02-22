import streamlit as st #Streamlit!!!
import os
import pandas as pd #Dataframeowkr
from st_pages import add_page_title, get_nav_from_toml #For st pages
from utils import setup_navigation  # Import function from utils


st.set_page_config( #Configuration
    page_title="Elderly Care", 
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto" #Allows streamlit to default whether sidebar will be shown, False for phone etc
)

pg = setup_navigation()  # Call the function to setup navigation
pg.run()

#TO DO
#nil