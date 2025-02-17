import streamlit as st
from streamlit_calendar import calendar
import pandas as pd

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/schedule.py", label="Schedule", icon="🗓️")  
    st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

side_bar_UI()

# Read the event data from the CSV file
file_path = "events.csv"

# Read the CSV into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert the DataFrame into the format expected by the calendar component
calendar_events = []
for index, row in df.iterrows():
    event = {
        "title": row["title"],
        "start": row["start"],
        "end": row["end"],
        "resourceId": row["resourceId"]
    }
    calendar_events.append(event)

# Display the calendar
calendar_display = calendar(
    events=calendar_events,
    key='calendar',
)

st.write(calendar_display)
