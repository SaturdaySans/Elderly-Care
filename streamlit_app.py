import streamlit as st
import os


st.title("Alzheimer Help") # Tests Ignore
st.write("Hello world")
st.write({"key": ["value"]})

login_account = None
filename = "accounts.txt"

def main_menu_UI():
    print("\n--- Alzheimer help ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == '1':
        create_account(filename)
    elif choice == '2':
        if login(filename):
            return  #Exit the main menu and into users account.
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main()

def account_UI():
    
    print("\n -- Dashboard --")
    print("1. Logout of Account")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        logout()

def daily_routine():
    pass

def login(filename):
    check_or_create_file(filename)  # Ensure file exists
    print("\n--- Login ---")
    identifier = input("Enter username or email: ").strip()

    with open(filename, 'r') as file:
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

def create_account(filename):
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
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as file:
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
    with open(filename, 'a') as file:
        if os.path.getsize(filename) > 0:  # Add separator if file is not empty
            file.write("#\n")
        file.write(f"{username}\n{email}\n{password}\n")
    print("Account created successfully!")

    main()

##

def check_or_create_file(filename):
    #Check if accounts.txt exists, and create it if it doesn't.
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

def gps():
    pass


def main():
    main_menu_UI()


main()





#Todo: 
#Fix login bug where cannot login even with correct information
#Add a check in account creation. If a username/email is alr in use, request for renaming.
#Refine input validation for account creation 
#Set up streamlit UI
#GPS tracking
#Daily routine
#Reminders
#Move main menu UI in main() to user_interface()
#Admin account that can delete accounts?
#Allow user to go back to main menu in the sub-menus.