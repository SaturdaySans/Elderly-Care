import streamlit as st
import os

# Initialize session state for navigation & login state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "settings"  # Default to settings page

ACCOUNTS_FILE = "accounts.txt"

def account_UI():
    """Display Account settings menu based on login state"""
    st.write("\n -- Account Settings --")

    if st.session_state["logged_in"]:
        st.write(f"Logged in as: **{st.session_state['username']}**")
        if st.button("Logout"):
            logout()
    else:
        if st.button("Create Account"):
            st.session_state["page"] = "create_account"
        if st.button("Login"):
            st.session_state["page"] = "login"

def login():
    """Login user by checking credentials"""
    check_or_create_file(ACCOUNTS_FILE)
    st.write("\n--- Login ---")
    identifier = st.text_input("Enter username or email:").strip()
    password = st.text_input("Enter password:", type="password").strip()

    if st.button("Submit"):
        with open(ACCOUNTS_FILE, 'r') as file:
            accounts = file.read().strip().split("#\n")

        for account in accounts:
            lines = account.strip().split("\n")
            if len(lines) == 3:
                username, email, stored_password = lines
                if identifier in [username, email] and password == stored_password:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["page"] = "settings"  # Redirect back to settings
                    return

        st.write("❌ Invalid username/email or password.")

    if st.button("Back"):
        st.session_state["page"] = "settings"

def logout():
    """Log the user out"""
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["page"] = "settings"

def create_account():
    """Create a new account and save to file"""
    st.write("\n--- Create New Account ---")
    username = st.text_input("Enter username:").strip()
    email = st.text_input("Enter email:").strip()
    password = st.text_input("Enter password:", type="password").strip()

    if st.button("Register"):
        if not username or not email or not password:
            st.write("❌ All fields are required.")
            return
        if "@" not in email:
            st.write("❌ Invalid email format.")
            return

        users = []
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, 'r') as file:
                accounts = file.read().strip().split("#\n")
                for acc in accounts:
                    details = acc.strip().split("\n")
                    if len(details) == 3:
                        users.append({'username': details[0], 'email': details[1], 'password': details[2]})

        # Check for duplicates
        for user in users:
            if user['username'] == username:
                st.write("❌ Username already taken.")
                return
            if user['email'] == email:
                st.write("❌ Email already in use. Please login.")
                return

        # Save new account
        with open(ACCOUNTS_FILE, 'a') as file:
            if os.path.getsize(ACCOUNTS_FILE) > 0:
                file.write("#\n")
            file.write(f"{username}\n{email}\n{password}\n")

        st.write("✅ Account created successfully!")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["page"] = "settings"

    if st.button("Back"):
        st.session_state["page"] = "settings"

def check_or_create_file(filename):
    """Ensure the accounts file exists"""
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

# **Navigation Handling**
if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "create_account":
    create_account()
