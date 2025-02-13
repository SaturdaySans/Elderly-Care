import streamlit as st
import os
import pandas as pd

st.title("Medication")

file_path = "medication.csv"

if os.path.exists(file_path):
    try:
        medication = pd.read_csv(file_path)  # Automatically reads headers
        if medication.empty:
            st.warning("The CSV file is empty.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        medication = pd.DataFrame(columns=["Medication", "Time", "Taken"])
else:
    medication = pd.DataFrame(columns=["Medication", "Time", "Taken"])  # Empty DataFrame

st.write(medication)