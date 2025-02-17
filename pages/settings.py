import streamlit as st
import os
import pandas as pd

def side_bar_UI():
    st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    st.sidebar.page_link("pages/schedule.py", label="Schedule", icon="🗓️")  
    st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

side_bar_UI()

# File to store account data
ACCOUNTS_FILE = "accounts.csv"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "settings"  # Default to settings page

def check_or_create_file():
    """Ensure the accounts CSV file exists with headers"""
    if not os.path.exists(ACCOUNTS_FILE) or os.stat(ACCOUNTS_FILE).st_size == 0:
        df = pd.DataFrame(columns=["username", "email", "password"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV safely"""
    check_or_create_file()
    try:
        return pd.read_csv(ACCOUNTS_FILE)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["username", "email", "password"])

def account_UI():
    """Display Account Settings UI"""
    st.title("\n -- Account Settings --")

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
    """Login User"""
    st.write("\n--- Login ---")
    identifier = st.text_input("Enter username or email:").strip()
    password = st.text_input("Enter password:", type="password").strip()

    if st.button("Submit"):
        df = load_accounts()

        user = df[(df["username"] == identifier) | (df["email"] == identifier)]
        if not user.empty and user.iloc[0]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user.iloc[0]["username"]
            st.session_state["page"] = "settings"
            st.rerun()
        else:
            st.write("❌ Invalid username/email or password.")

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.rerun()

def logout():
    """Logout User"""
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["page"] = "settings"
    st.rerun()

def create_account():
    """Create a new account and save to CSV"""
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

        df = load_accounts()

        if username in df["username"].values:
            st.write("❌ Username already taken.")
            return
        if email in df["email"].values:
            st.write("❌ Email already in use. Please login.")
            return

        # Append new user
        new_user = pd.DataFrame([[username, email, password]], columns=["username", "email", "password"])
        new_user.to_csv(ACCOUNTS_FILE, mode='a', header=False, index=False)

        st.write("✅ Account created successfully!")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["page"] = "settings"
        st.rerun()

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.rerun()

# **Navigation Handling**
if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "create_account":
    create_account()
