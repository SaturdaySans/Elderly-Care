import streamlit as st
import os
import pandas as pd

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide")

# Function to load and execute a script file
def load_page(file_path):
    try:
        with open(file_path, "r") as file:
            exec(file.read(), globals())
    except FileNotFoundError:
        st.error(f"❌ Error: {file_path} not found.")
    except Exception as e:
        st.error(f"❌ Error loading {file_path}: {str(e)}")

def side_bar_UI():
    st.sidebar.header("Alzheimer Help") #Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    if st.sidebar.button("💊 Medication"):
        load_page("app_pages/medication.py")

    if st.sidebar.button("📅 Schedule"):
        load_page("app_pages/schedule.py")

    if st.sidebar.button("⚙️ Settings"):
        load_page("app_pages/settings.py")

#Functions
def main_menu_UI():
    st.title("--- Alzheimer help ---")
    st.divider()
    side_bar_UI()

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