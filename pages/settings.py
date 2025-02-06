import streamlit as st
import os
import pandas as pd


from streamlit_app import *


st.write("Settings")

def account_UI():
    st.write("\n -- Dashboard --")
    st.write("1. Daily Routine")
    st.write("2. Logout of Account")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        #daily_routine()
        pass
    elif choice == '2':
        logout()

def login(accounts):
    check_or_create_file(accounts)  # Ensure file exists
    st.write("\n--- Login ---")
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
