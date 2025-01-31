import streamlit as st
import os
import pandas as pd


login_account = None

accounts = pd.read_csv("accounts.txt") #Assign the data
routine = pd.read_csv("daily_routine.txt")

def main_menu_UI():
    st.title("\n--- Alzheimer help ---")
    st.divider()
    
    if st.button("1. Create Account"):
        create_account(accounts)
    elif st.button("2. Login"):
        if login(accounts):
            return  #Exit the main menu and into users account.
    elif st.button("3. Exit"):
        st.write("Exiting the program. Goodbye!")


def create_account(accounts):
    st.write("hi")

def login(accounts):
    st.write("hi")

def main():
    main_menu_UI()


#Call main
main()





#Todo: 
#Rewrite validation for daily routine, HHMM format, etc.
#Refine input validation for account creation, email validation, etc.
#Set up streamlit UI
#GPS tracking 
#Daily routine
#Reminders
#Move main menu UI in main() to user_interface()
#Admin account that can delete accounts?
#Allow user to go back to main menu in the sub-menus.
#Add file close() everywhere it is missing.
#Optimise the code, make it neater.
#Add a way to go back to the main menu in all sub-menus.
#Fix delete event
#Add edit event function
#Add view events function