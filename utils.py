import streamlit as st
from st_pages import get_nav_from_toml, hide_pages

def setup_navigation():
    """Global function to setup navigation."""
    # Load navigation pages from the TOML file
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")

    # Display app logo
    st.logo("resources/calendar.png")

    # Ensure session state role exists
    if "role" not in st.session_state:
        st.session_state.role = None

    if "UID" not in st.session_state:
        st.session_state["UID"] = [1]  # Default non-admin UID
    hide_pages(["Admin"])

    # Display standard navigation (no admin-specific logic)
    pg = st.navigation(nav)

    return pg  # Return the navigation object

def update_navigation():
    """Function to update the navigation and trigger a rerun."""
    # Call setup_navigation to refresh the navigation
    pg = setup_navigation()
    
    # Rerun the app after navigation is updated
    st.rerun()  # Use st.rerun() here as well
