import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",
    page_icon="🧠",  
    layout="wide"
)

# Inject CSS using st.components.v1.html (without using st.markdown)
css_code = """
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #34495e;
        text-align: center;
        margin-bottom: 10px;
    }
    .nav-card {
        background: #f7f7f7;
        border-radius: 8px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .nav-card a {
        text-decoration: none;
        color: #2980b9;
        font-size: 1.2rem;
    }
</style>
"""
# Render the CSS
components.html(css_code, height=0, width=0)

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")
    st.sidebar.write("Navigate to different sections:")
    st.sidebar.write("🏠 Home: [streamlit_app.py](streamlit_app.py)")
    st.sidebar.write("💊 Medication: [pages/medication.py](pages/medication.py)")
    st.sidebar.write("📅 Schedule: [pages/schedule.py](pages/schedule.py)")
    st.sidebar.write("⚙️ Settings: [pages/settings.py](pages/settings.py)")
    st.sidebar.info("Check your schedule daily for reminders and updates.")

def main_menu_UI():
    # Banner image (replace URL with your own image path if available)
    st.image("https://via.placeholder.com/1200x300.png?text=Alzheimer%27s+Disease+Awareness", 
             use_column_width=True, output_format="PNG")

    # Title and subtitle using st.write with HTML
    st.write('<div class="main-title">Alzheimer Help</div>', unsafe_allow_html=True)
    st.write('<div class="sub-title">Your Companion in Managing Alzheimer\'s Disease</div>', unsafe_allow_html=True)
    st.divider()

    # Navigation Cards using columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('<div class="nav-card"><a href="pages/medication.py">Medication 💊</a><br>Manage and track medication.</div>', 
                 unsafe_allow_html=True)
    with col2:
        st.write('<div class="nav-card"><a href="pages/schedule.py">Schedule 📅</a><br>Organize daily routines and appointments.</div>', 
                 unsafe_allow_html=True)
    with col3:
        st.write('<div class="nav-card"><a href="pages/settings.py">Settings ⚙️</a><br>Adjust your preferences and settings.</div>', 
                 unsafe_allow_html=True)

    st.write("---")
    st.write("Welcome to Alzheimer Help. This platform is designed to provide support and organization tools for individuals managing Alzheimer's disease. Use the sidebar or the navigation above to get started.")
    
    # Include sidebar
    side_bar_UI()

def main():
    main_menu_UI()

if __name__ == "__main__":
    main()
