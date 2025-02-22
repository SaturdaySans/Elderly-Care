import streamlit as st #Imports Streamlit
import os
import pandas as pd #Dataframe
from st_pages import add_page_title, get_nav_from_toml #Pages sidebar thing
from utils import update_navigation  # Import the function to update the navigation


st.title("--- Elderly Care ---") #Main menu
st.divider() #Divider
st.page_link("pages/settings.py", label="Settings", icon="⚙️") #Links to settings
st.page_link("pages/routine.py", label="Routine", icon="🗓️") #Links to routine
st.page_link("pages/events.py", label="Events", icon="📆")  #Links to events
st.page_link("pages/medication.py", label="Medication", icon="💊") #LInks to medication
#if st.button("Baloons!"): #Buggy sadly
    #st.balloons()
