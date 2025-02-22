#Yong Hong
import streamlit as st
from streamlit_calendar import calendar #For calendar ui woo
import pandas as pd


file_path = "events.csv" # Read the event data from the CSV file

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
#Referenced frm source: https://github.com/im-perativa/streamlit-calendar

st.write(calendar_display)
