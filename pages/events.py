import streamlit as st
from streamlit_calendar import calendar
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml
# Load pages from .toml
nav = get_nav_from_toml(".streamlit/pages.toml")

# Display navigation
pg = st.navigation(nav)

# Add a title
add_page_title(pg)
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
