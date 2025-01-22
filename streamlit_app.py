import streamlit as st
import os


st.title("Alzheimer Help") # Tests Ignore
st.write("Hello world")
st.write({"key": ["value"]})


def user_interface():
    pass

def daily_routine():
    pass

def login(filename):
    print("\n--- Login ---")
    identifier = input("Enter username or email: ").strip()
    password = input("Enter password: ").strip()

    with open(filename, 'r') as file:
        accounts = file.read().split("#\n")

    for account in accounts:
        lines = account.strip().split("\n")
        if len(lines) == 3:
            username, email, stored_password = lines
            if (identifier == username or identifier == email) and password == stored_password:
                print(f"Welcome, {username}!")
                return True

    print("Invalid username/email or password. Please try again.")
    return False

def logout():
    pass

def create_account(filename):
    #Create a new account and save it to the text file.
    print("\n--- Create New Account ---")
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    # Validate inputs
    if not username or not email or not password:
        print("All fields are required. Please try again.")
        return
    if "@" not in email:
        print("Invalid email.")
        main()

    # Save the account details to the text file
    with open(filename, 'a') as file:
        if os.path.getsize(filename) > 0:  # Check if there are other users of the app
            file.write("#\n")
        file.write(f"{username}\n{email}\n{password}\n")
        print("Account created successfully!")
        main()

def check_or_create_file(filename):
    #Check if accounts.txt exists, and create it if it doesn't.
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

def gps():
    pass


def main():
    filename = "accounts.txt"
    check_or_create_file(filename)

    print("\n--- Account Manager ---")
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





#Todo: 
#Add a check in account creation. If a username/email is alr in use, request for renaming.
#Refine input validation for account creation 
#Set up streamlit UI
#GPS tracking
#Daily routine
#Reminders
#Move main menu UI in main() to user_interface()
#Admin account that can delete accounts??
