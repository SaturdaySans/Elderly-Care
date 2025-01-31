import streamlit as st
import os



login_account = None

accounts = "accounts.txt"
routine = "daily_routine.txt"

def main_menu_UI():
    st.title("\n--- Alzheimer help ---")
    st.divider()
    test1=st.button("1. Create Account")
    st.button("2. Login")
    st.button("3. Exit")
    st.write(test1)

    choice = input("Enter your choice: ").strip()
    if choice == '1':
        create_account(accounts)
    elif choice == '2':
        if login(accounts):
            return  #Exit the main menu and into users account.
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main()

def account_UI():
    print("\n -- Dashboard --")
    print("1. Daily Routine")
    print("2. Logout of Account")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        daily_routine()
    elif choice == '2':
        logout()

#Daily routine functions
def daily_routine():
    #Create file if it does not exist
    if not os.path.exists(routine):
        with open(routine, 'w') as file:
            pass
    print("\n -- Daily Routine --")
    print("1. Create Event")
    print("2. Delete Event")
    print("3. Edit Event")
    print("4. View Events")
    print("5. Back to Dashboard")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        create_event()
    elif choice == '2':
        delete_event()
    elif choice == '3':
        edit_event()
    elif choice == '4':
        view_events()
    elif choice == '5':
        account_UI()
    else:
        print("Invalid choice. Please try again.")
        daily_routine()

def create_event():
    routine_file = "daily_routine.txt"
    with open(routine_file, 'r') as file:
        routine_content = file.read().split("#\n")

    print("\n -- Create Event --")
    event_name = input("Enter event name: ").strip()
    event_start_time = int(input("Enter event start time(Please enter in HHMM format without ':'): ").strip())
    event_end_time = int(input("Enter event end time(Please enter in HHMM format without ':'): ").strip())
    event_duration = event_end_time - event_start_time

    with open(routine_file, 'a') as file:
        # Insert "#" between events
        if os.path.getsize(routine_file) > 0:  # Add separator if file is not empty
            file.write("#\n")
        file.write(f"{event_name}\n{event_start_time}\n{event_end_time}\n{event_duration}\n")
    print("Event created successfully!")
    daily_routine()

def delete_event():
    print("\n -- Delete Event --")
    event_to_remove = input("Enter event name: ").strip()

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
    check_or_create_file(accounts)  # Ensure file exists
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