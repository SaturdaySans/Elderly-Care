import streamlit as st
import os
import pandas as pd

st.write("hi")
routine = pd.read_csv("daily_routine.txt")
st.write(routine)