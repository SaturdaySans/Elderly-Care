import streamlit as st
from streamlit_calendar import calendar

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/schedule.py", label="Schedule", icon="🗓️")  
    st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

side_bar_UI()

st.write("test")
calendar_events = [
    {"title": "Singing", "start": "2025-02-18T08:30:00+08:00", "end": "2025-002-18T10:30:00+08:00", "resourceId": "a"},
    {"title": "Event 2", "start": "2023-07-31T07:30:00+08:00", "end": "2023-07-31T10:30:00+08:00", "resourceId": "b"},
    {"title": "Event 3", "start": "2023-07-31T10:40:00+08:00", "end": "2023-07-31T12:30:00+08:00", "resourceId": "a"},
]


# Rename the calendar variable to avoid conflict
calendar_display = calendar(
    events=calendar_events,
    key='calendar',
)

# Render the calendar in the Streamlit app
st.write(calendar_display)