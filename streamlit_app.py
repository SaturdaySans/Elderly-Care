import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml

#Admin Page (For us)

st.set_page_config(
    page_title="Elderly Care",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide",
    initial_sidebar_state="auto")

nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

st.logo("resources/calendar.png") # Sets logo of the app

if "role" not in st.session_state:
    st.session_state.role = None
ROLES = [None, "User", "Admin"]
if st.session_state["UID"][-1] == 0:
    st.session_state.role = "Admin"
    st.rerun()
role = st.session_state.role
admin_pages = st.Page("pages/admin.py", title="Admin", icon=":material/security:", default=(role == "Admin"))
page_dict = {}
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages
if len(page_dict) > 0:
    pg = st.navigation({"Admin": admin_pages} | page_dict)


#Functions (Not Used)
def main_menu_UI():
    #st.image("resources/banner.png", use_container_width=True)
    st.title("--- Alzheimer help ---")
    st.divider()
    st.page_link("pages/settings.py", label="Settings", icon="⚙️")
    st.page_link("pages/routine.py", label="Routine", icon="🗓️")
    st.page_link("pages/events.py", label="Events", icon="📆")  
    st.page_link("pages/medication.py", label="Medication", icon="💊")

def main():
    pg.run()


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
