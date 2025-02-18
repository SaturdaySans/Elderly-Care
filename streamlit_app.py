import streamlit as st
import os
import pandas as pd
from st_pages import Page, show_pages, add_page_title

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide",
    initial_sidebar_state="auto")



# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("pages/events.py", "Page 2", ":book:"),
    ]
)

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/routine.py", label="Routine", icon="🗓️")  
    st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")



#Functions
def main_menu_UI():
    st.image("resources/banner.png", use_container_width=True)
    st.title("--- Alzheimer help ---")
    st.divider()
    side_bar_UI()
    st.page_link("pages/settings.py", label="Settings", icon="⚙️")
    st.page_link("pages/routine.py", label="Routine", icon="🗓️")
    st.page_link("pages/events.py", label="Events", icon="📆")  
    st.page_link("pages/medication.py", label="Medication", icon="💊")

def main():
    main_menu_UI()


#Call main
main()





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