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
    st.markdown(
        """
        <div style="position: relative; text-align: center;">
            <!-- The Banner Image -->
            <img src="resources/banner.png" alt="Banner" style="width: 100%; height: auto;">

            <!-- The Text Overlay -->
            <div style="
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: white;
                font-size: 2em;
                font-weight: bold;
                text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
            ">
                Alzheimer help
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("--- Alzheimer help ---")
    st.divider()
    side_bar_UI()
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/schedule.py", label="Schedule")
    st.page_link("pages/medication.py", label="Medication")

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