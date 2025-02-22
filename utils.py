import streamlit as st
from st_pages import get_nav_from_toml, hide_pages #For managine sidebar pages

def setup_navigation():
    """Global function to setup navigation with role-based access."""
    # Load navigation pages from the TOML file
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")

    st.logo("resources/calendar.png") # Display app logo (Sidebar)

    # Ensure session state role exists
    if "role" not in st.session_state: 
        st.session_state.role = None #Should be moved to admin.py alrd

    if "UID" not in st.session_state:
        st.session_state["UID"] = [1]  # Default non-admin UID

    # Check the user's role, if they are not an admin, hide admin pages
    if st.session_state["role"] != "Admin":
        hide_pages(["Admin"])  # Hide admin pages for non-admin users

    # Display navigation
    pg = st.navigation(nav)

    return pg  # Return the navigation object

def update_navigation(): #Pretty sure this isnt used anywhere
    """Function to update the navigation and trigger a rerun."""
    # Call setup_navigation to refresh the navigation
    pg = setup_navigation()
    
    # Rerun the app after navigation is updated
    st.rerun()  # Use st.rerun() here as well
