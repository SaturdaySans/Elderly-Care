#Yong Hong
import streamlit as st
import os
import pandas as pd

st.title("---Routine---")
st.divider()

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

