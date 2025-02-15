import streamlit as st
import os
import pandas as pd

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide")

def side_bar_UI():
    st.sidebar.header("Alzheimer Help") #Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/schedule.py", label="Schedule", icon="📅")
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

#Functions
def main_menu_UI():
    st.image("resources/banner.png", use_container_width=True)
    st.title("--- Alzheimer help ---")
    st.divider()
    side_bar_UI()
    # Row 1
    col1, col2 = st.columns([1, 2])  # Adjust width ratios as needed
    with col1:
        st.image("resources/settings.png", width=200)
    with col2:
        st.page_link("pages/settings.py", label="Settings", icon="⚙️")
    
    st.write("")  

    # Row 2
    col3, col4 = st.columns([2, 1])
    with col3:
        st.page_link("pages/schedule.py", label="Schedule", icon="📅")
    with col4:
        st.image("resources/calendar.png", width=200)

    st.write("")  

    #Row 3
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image("resources/medicine.png", width=200)
    with col6:
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