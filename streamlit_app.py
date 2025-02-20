import streamlit as st
import os
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(
    page_title="Elderly Care",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

# Load navigation pages
nav = get_nav_from_toml(".streamlit/pages_sections.toml")

# Display app logo
st.logo("resources/calendar.png", width=100)

# Ensure session state role exists
if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "User", "Admin"]

if "UID" not in st.session_state:
    st.session_state["UID"] = [1]


if st.session_state["UID"] and st.session_state["UID"][-1] == 0:
    st.session_state.role = "Admin"
    st.rerun()

role = st.session_state.role

# Define Admin page
admin_pages = st.Page("pages/admin.py", title="Admin", icon=":material/security:")

# Merge Admin page into navigation if user is Admin
if role == "Admin":
    pg = st.navigation({**nav, "Admin": admin_pages})
else:
    pg = st.navigation(nav)

# Run the navigation system
pg.run()
