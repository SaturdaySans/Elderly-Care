import streamlit as st
from st_pages import get_nav_from_toml

# Setup the main app with navigation
def setup_navigation():
    # Load navigation pages from TOML configuration
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")
    
    # Display app logo
    st.logo("resources/calendar.png")
    
    # Ensure session state role exists
    if "role" not in st.session_state:
        st.session_state.role = None

    # Ensure session state UID exists
    if "UID" not in st.session_state:
        st.session_state["UID"] = [1]  # Default non-admin UID

    # Check if the user is an Admin
    if st.session_state["UID"] and st.session_state["UID"][-1] == 0:
        st.session_state.role = "Admin"
        st.rerun()  # Rerun only if you want the state to change immediately

    role = st.session_state.role

    # Define the admin page if needed
    admin_pages = st.Page("pages/admin.py", title="Admin", icon=":material/security:")

    # Merge Admin page into navigation if user is Admin
    if role == "Admin":
        pg = st.navigation({**nav, "Admin": admin_pages})
    else:
        pg = st.navigation(nav)
    
    # Page rendering logic based on user navigation
    page = st.selectbox("Select a page", list(nav.keys()))
    st.write(f"Showing {page} content here...")
