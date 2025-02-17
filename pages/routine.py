import streamlit as st
import os
import pandas as pd

st.title("---Routine---")
st.divider()

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/routine.py", label="Routine", icon="🗓️")  
    st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

side_bar_UI()

file_path = "daily_routine.csv"

# Check if file exists
if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
    try:
        routine = pd.read_csv(file_path, names=["Events", "Start", "End", "Duration"], header=None, usecols=[0, 1, 2, 3])
    except Exception as e:
        st.error(f"Error reading file: {e}")
        routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])
else:
    routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])  # Empty DataFrame


st.write(routine)

# Initialize session state for editing mode
if "editing" not in st.session_state:
    st.session_state.editing = False

if st.button("Edit"):
    st.session_state.editing = True  # Enable editing mode

if st.session_state.editing:
    routine_name = st.text_input("Event Name:", st.session_state.get("routine_name", ""))
    start_time = st.number_input("Start Time:", min_value=0, max_value=2359, step=1, value=st.session_state.get("start_time", 0))
    end_time = st.number_input("End Time:", min_value=0, max_value=2359, step=1, value=st.session_state.get("end_time", 0))

    # Validate input
    if start_time and end_time and start_time < end_time:
        duration = end_time - start_time

        if st.button("Done!"):
            new_entry = pd.DataFrame({"Events": [routine_name], "Start": [start_time], "End": [end_time], "Duration": [duration]})
            
            # Check if the file exists before writing
            write_header = not os.path.exists(file_path) or os.stat(file_path).st_size == 0

            # Open file in append mode, ensuring a newline is properly added
            with open(file_path, mode='a', newline='') as file:
                new_entry.to_csv(file, header=write_header, index=False)

            st.success("Event added successfully!")

            # Reset editing mode
            st.session_state.editing = False
            st.session_state.routine_name = ""
            st.session_state.start_time = 0
            st.session_state.end_time = 0

            # Refresh the page to show the new data
            st.rerun()
    else:
        st.warning("Please enter a valid start and end time.")

st.page_link("streamlit_app.py", label="Menu")