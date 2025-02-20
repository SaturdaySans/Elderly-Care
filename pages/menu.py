import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml
from utils import update_navigation  # Import function


st.title("--- Elderly Care ---")
st.divider()
st.page_link("pages/settings.py", label="Settings", icon="⚙️")
st.page_link("pages/routine.py", label="Routine", icon="🗓️")
st.page_link("pages/events.py", label="Events", icon="📆")  
st.page_link("pages/medication.py", label="Medication", icon="💊")

# Display current role and UID for debugging purposes
st.write("Role:", st.session_state.get("role", "Not Set"))
st.write("UID:", st.session_state.get("UID", "Not Set"))

# Ensure the role is initialized correctly
if "role" not in st.session_state:
    st.session_state.role = None
    st.session_state.UID = [1]  # Default UID for non-admins, adjust as needed

# If the role is admin, refresh the navigation
if st.session_state.role == "Admin":  # Example of checking role
    update_navigation()  # Call to refresh navigation and rerun the app