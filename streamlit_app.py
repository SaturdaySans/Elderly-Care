import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml

# 🛠️ Fix: Move `st.set_page_config()` to the top before any other `st` calls
st.set_page_config( 
    layout="wide"
)

nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml" 
)

st.logo("resources/calendar.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()





#Todo: 
#Rewrite validation for daily routine, HHMM format, etc.
#Refine input validation for account creation, email validation, etc.
#Set up streamlit UI
#GPS tracking 
#Daily routine
#Reminders
#Move main menu UI in main() to user_interface()
#Admin account that can delete accounts?
#Allow user to go back to main menu in the sub-menus.
#Add file close() everywhere it is missing.
#Optimise the code, make it neater.
#Add a way to go back to the main menu in all sub-menus.
#Fix delete event
#Add edit event function
#Add view events function
