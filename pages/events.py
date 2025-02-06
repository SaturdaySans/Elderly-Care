import streamlit as st
import os
import pandas as pd

routine = pd.read_csv("daily_routine.txt")

st.write("--- Event Manager ---")
if st.button("Create Event"):
    st.write("Create Event")
    event_name = st.text_input("Event Name")
    event_date = st.text_input("Event Date")
    event_time = st.text_input("Event Time")
    event_location = st.text_input("Event Location")
    event_description = st.text_input("Event Description")
    event = pd.DataFrame({"Event Name": [event_name], "Event Date": [event_date], "Event Time": [event_time], "Event Location": [event_location], "Event Description": [event_description]})
    #routine = routine.append(event)
    routine.to_csv("daily_routine.txt", index=False)
    st.write("Event created successfully.")
    st.write(routine)
if st.button("Edit Event"):
    st.write("Edit Event")
    event_name = st.text_input("Event Name")
    event_date = st.text_input("Event Date")
    event_time = st.text_input("Event Time")
    event_location = st.text_input("Event Location")
    event_description = st.text_input("Event Description")
    event = pd.DataFrame({"Event Name": [event_name], "Event Date": [event_date], "Event Time": [event_time], "Event Location": [event_location], "Event Description": [event_description]})
    #routine = routine.append(event)
    routine.to_csv("daily_routine.txt", index=False)
    st.write("Event edited successfully.")
    st.write(routine)
if st.button("Delete Event"):
    st.write("Delete Event")
    event_name = st.text_input("Event Name")
    event_date = st.text_input("Event Date")
    event_time = st.text_input("Event Time")
    event_location = st.text_input("Event Location")
    event_description = st.text_input("Event Description")
    event = pd.DataFrame({"Event Name": [event_name], "Event Date": [event_date], "Event Time": [event_time], "Event Location": [event_location], "Event Description": [event_description]})
    #routine = routine.append(event)
    routine.to_csv("daily_routine.txt", index=False)
    st.write("Event deleted successfully.")
    st.write(routine)
if st.button("View Events"):
    st.write("View Events")
    st.write(routine)






st.write(routine)