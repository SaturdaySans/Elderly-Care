import streamlit as st
import os
import pandas as pd
import time

st.title("---Medication Tracker---")

file_path = "medication.csv"

# Load CSV if it exists, otherwise create an empty DataFrame
if os.path.exists(file_path):
    try:
        medication = pd.read_csv(file_path)  
        if medication.empty:
            st.warning("The CSV file is empty.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        medication = pd.DataFrame(columns=["Medication", "Time", "Taken"])
else:
    medication = pd.DataFrame(columns=["Medication", "Time", "Taken"])  # Empty DataFrame

# Display medication list with checkboxes
updated_status = []

for index, row in medication.iterrows():
    checked = st.checkbox(f"{row['Medication']} ({row['Time']})", value=(row['Taken'] == "Yes"), key=index)
    updated_status.append("Yes" if checked else "No")

# Update the DataFrame with the new values
if st.button("Update Medication Status"):
    medication["Taken"] = updated_status
    medication.to_csv(file_path, index=False)
    st.success("Medication status updated!")

