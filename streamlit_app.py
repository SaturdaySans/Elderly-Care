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
#I have 0 clue how to implement this in, should we just skip the accounts part
def login(accounts):
    print("\n--- Login ---")
    identifier = input("Enter username or email: ").strip()
    #Insert "#" between accounts
    with open(accounts, 'r') as file:
        accounts = file.read().split("#\n")

    for account in accounts:
        lines = account.strip().split("\n")
        if len(lines) == 3:  # Ensure the account has all necessary details
            username, email, stored_password = lines
            if identifier == username or identifier == email:
                # Match found; request password
                password = input("Enter password: ").strip()
                if password == stored_password:
                    print(f"Welcome, {username}!")
                    login_account = username
                    account_UI()
                    return True
                else:
                    print("Incorrect password, please try again.")
                    main()
                    return False

    # No match found
    print("Invalid username/email. Please try again.")
    main()
    return False

def logout():
    login_account = None
    main_menu_UI()

def create_account(accounts):
    #Create a new account and save it to the text file.
    print("\n--- Create New Account ---")
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    # Validate inputs
    if not username or not email or not password:
        print("All fields are required. Please try again.")
        main()
    if "@" not in email:
        print("Invalid email.")
        main()

    users = []  # List to hold parsed users
    if os.path.exists(accounts):  # Check if the file exists
        with open(accounts, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                if i + 2 < len(lines):
                    users.append({
                        'username': lines[i].strip(),
                        'email': lines[i+1].strip(),
                        'password': lines[i+2].strip()
                    })

    # Check for username/email conflicts
    for user in users:
        if user['username'] == username:
            print("Username already in use, please pick another one.")
            main()
        if user['email'] == email:
            print("Email already in use, if this is you, please login.")
            main()

    # Append new user data to the file
    with open(accounts, 'a') as file:
        if os.path.getsize(accounts) > 0:  # Add separator if file is not empty
            file.write("#\n")
        file.write(f"{username}\n{email}\n{password}\n")
    print("Account created successfully!")

    main()

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