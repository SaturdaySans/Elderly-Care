import streamlit as st
import os
import pandas as pd

st.title("Schedule")
st.divider()
routine = pd.read_csv("daily_routine.txt")
st.write(routine)
if st.button("Edit"):
    schedule_name = st.text_input("Event Name:")
    start_time = st.number_input("Start Time (xxxx):")
    end_time = st.number_input("End Time (xxxx):")
    duration = end_time - start_time
    if st.button("Done!"):
        dataframe = pd.DataFrame({"Events": [schedule_name], "Start": [start_time], "End": [end_time], "Duration": [duration]})
        dataframe.to_csv("daily_routine.txt", mode='a', header=False, index=False)