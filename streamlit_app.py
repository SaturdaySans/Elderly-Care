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


def account_UI():
    st.title("\n -- Dashboard --")
    if st.button("1. Daily Routine"):
        daily_routine()
    elif st.button("2. Logout of Account"):
        logout()

#Daily routine functions
def daily_routine():
    st.title("\n -- Daily Routine --")
    if st.button("1. Create Event"):
        create_event()
    elif st.button("2. Delete Event"):
        delete_event()
    elif st.button("3. Edit Event"):
        edit_event()
    elif st.button("4. View Events"):
        view_events()
    elif st.button("5. Back to Dashboard"):
        account_UI()


def create_event():
    st.write("check")


def delete_event():
    st.title("\n -- Delete Event --")
    event_to_remove = st.text_input("Enter event name: ").strip()

    with open(routine, 'r') as file:
        lines = file.readlines()

    # Variables to store updated content
    updated_content = []
    delete_lines = False

    # Filter out the event to delete
    for line in lines:
        if line.strip() == f"#{event_to_remove}":  # Check if the line matches the event name
            delete_lines = True  # Start skipping lines for this event
        elif line.strip() == "#":  # End of an event
            delete_lines = False
            continue  # Skip the separator line
        elif not delete_lines:
            updated_content.append(line)  #Put the other events into temporary list

    # Write the updated content back to the file
    with open(routine, 'w') as file:
        file.writelines(updated_content)


def edit_event():
    pass

def view_events():
    pass





#Login, logout and account creation functions
def login(accounts):
    st.empty()
    st.write(accounts)
##

def check_or_create_file(accounts):
    #Check if accounts.txt exists, and create it if it doesn't.
    if not os.path.exists(accounts):
        with open(accounts, 'w') as file:
            pass

def gps():
    pass



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