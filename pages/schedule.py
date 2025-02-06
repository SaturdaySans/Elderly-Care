import streamlit as st
import os
import pandas as pd

st.title("Schedule")
st.divider()
routine = pd.read_csv("daily_routine.txt")
st.write(routine)
if st.button("Edit"):
    st.write("Test")