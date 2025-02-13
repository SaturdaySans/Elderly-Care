import streamlit as st
import os
import pandas as pd

st.title("Medication")

file_path = "medication.csv"


if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
    try:
        medication = pd.read_csv(file_path, names=["Medication","Time","Taken"], header=None, usecols=[0, 1, 2])
    except Exception as e:
        st.error(f"Error reading file: {e}")
        medication = pd.DataFrame(columns=["Medication","Time","Taken"])
else:
    medication = pd.DataFrame(columns=["Medication","Time","Taken"])  # Empty DataFrame

st.write(medication)