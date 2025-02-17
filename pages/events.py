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

calendar_options = {
    "editable": False,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}

calendar_events = [
    {"title": "Event 1", "start": "2023-07-31T08:30:00+08:00", "end": "2023-07-31T10:30:00+08:00", "resourceId": "a"},
    {"title": "Event 2", "start": "2023-07-31T07:30:00+08:00", "end": "2023-07-31T10:30:00+08:00", "resourceId": "b"},
    {"title": "Event 3", "start": "2023-07-31T10:40:00+08:00", "end": "2023-07-31T12:30:00+08:00", "resourceId": "a"},
]

# Rename the calendar variable to avoid conflict
calendar_display = calendar(
    events=calendar_events,
    options=calendar_options,
    key='calendar',
)

# Render the calendar in the Streamlit app
st.write(calendar_display)