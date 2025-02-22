#Yong Hong
import streamlit as st #Streamlit
import os
import pandas as pd

st.title("---Routine---") #Title
st.divider() #Divider

file_path = "daily_routine.csv" #Declare file

# Check if file exists
if os.path.exists(file_path) and os.stat(file_path).st_size > 0: 
    try:
        routine = pd.read_csv(file_path, names=["Events", "Start", "End", "Duration"], header=None, usecols=[0, 1, 2, 3]) #Stroe the csv data into variable routine
    except Exception as e:
        st.error(f"Error reading file: {e}") #Reads out error, for debugging purposes too
        routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])
else:
    routine = pd.DataFrame(columns=["Events", "Start", "End", "Duration"])  # Empty DataFrame (If file doesnt exist for some reason)

st.write(routine) #Writes out the data (Streamlit defaults to table iirc)

