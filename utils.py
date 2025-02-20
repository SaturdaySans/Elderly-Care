import streamlit as st
from st_pages import get_nav_from_toml

def setup_navigation():
    """Global function to setup navigation and role-based access."""
    # Load navigation pages
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")

    # Display app logo
    st.logo("resources/calendar.png")

    # Ensure session state role exists
    if "role" not in st.session_state:
        st.session_state.role = None

    if "UID" not in st.session_state:
        st.session_state["UID"] = [1]  # Default non-admin UID

    # Check if user is admin (last digit of UID is 0)
    if st.session_state["UID"] and str(st.session_state["UID"][-1])[-1] == '0':
        st.session_state.role = "Admin"

    role = st.session_state.role

    # Define Admin page correctly as a dictionary
    admin_pages = {"Admin": st.Page("pages/admin.py", title="Admin", icon=":material/security:")}

    # Merge Admin page into navigation if user is Admin
    if role == "Admin":
        pg = st.navigation({**nav, **admin_pages})  # Merged dictionary with admin page
    else:
        pg = st.navigation(nav)

    return pg  # Return the navigation object
