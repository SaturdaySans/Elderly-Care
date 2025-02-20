import streamlit as st
from st_pages import get_nav_from_toml

def setup_navigation():
    """Global function to setup navigation and role-based access."""
    # Load navigation pages from the TOML file
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")

    # Display app logo
    st.logo("resources/calendar.png")

    # Ensure session state role exists
    if "role" not in st.session_state:
        st.session_state.role = None

    if "UID" not in st.session_state:
        st.session_state["UID"] = [1]  # Default non-admin UID

    # Check if user is admin (last digit of UID is 0)
    if st.session_state["UID"] and str(st.session_state["UID"][-1])[-1] == "0":
        st.session_state.role = "Admin"
        st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

    role = st.session_state.role

    # Define Admin page path (this page should only be visible for Admins)
    admin_pages = st.Page("pages/admin.py", title="Admin", icon=":material/security:")

    # If the user is an Admin, merge the Admin page into the navigation
    if role == "Admin":
        pg = st.navigation({**nav, "Admin": admin_pages})
    else:
        pg = st.navigation(nav)

    return pg  # Return the navigation object

def update_navigation():
    """Function to update the navigation and trigger a rerun."""
    # Call setup_navigation to refresh the navigation
    pg = setup_navigation()
    
    # Rerun the app after navigation is updated
    st.rerun()  # Use st.rerun() here as well
