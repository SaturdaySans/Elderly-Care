import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml
from utils import update_navigation  # Import the function to update the navigation


st.title("--- Elderly Care ---") #Main menu
st.divider()
st.page_link("pages/settings.py", label="Settings", icon="⚙️")
st.page_link("pages/routine.py", label="Routine", icon="🗓️")
st.page_link("pages/events.py", label="Events", icon="📆")  
st.page_link("pages/medication.py", label="Medication", icon="💊")

