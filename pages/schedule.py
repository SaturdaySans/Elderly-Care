import streamlit as st
import os
import pandas as pd


st.title("Schedule")
st.divider()

# Show existing schedule (if any)
if os.path.exists("daily_routine.csv"):
    try:
        routine = pd.read_csv("daily_routine.csv")
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])
else:
    routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])  # Create an empty DataFrame
st.write(routine)

if "editing" not in st.session_state:
    st.session_state.editing = False

if st.button("Edit"):
    st.session_state.editing = True  # Set state to editing

if st.session_state.editing:
    schedule_name = st.text_input("Event Name:")
    start_time = st.number_input("Start Time (xxxx):", min_value=0, max_value=2359, step=1)
    end_time = st.number_input("End Time (xxxx):", min_value=0, max_value=2359, step=1)

    # Validate input
    if start_time and end_time and start_time < end_time:
        duration = end_time - start_time

        if st.button("Done!"):
            # Save to CSV
            dataframe = pd.DataFrame({
                "Events": [schedule_name], 
                "Start": [start_time], 
                "End": [end_time], 
                "Duration": [duration]
            })
            dataframe.to_csv("daily_routine.csv", mode='a', header=False, index=False)

            st.success("Event added successfully!")
            st.session_state.editing = False  # Exit edit mode
    else:
        st.warning("Please enter a valid start and end time.")
