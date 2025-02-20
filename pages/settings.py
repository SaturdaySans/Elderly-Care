import streamlit as st
import os
import pandas as pd
import random


# File to store account data
ACCOUNTS_FILE = "accounts.csv"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "UID" not in st.session_state:
    st.session_state["UID"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "settings"  # Default to settings page

def check_or_create_file():
    """Ensure the accounts CSV file exists with headers"""
    if not os.path.exists(ACCOUNTS_FILE) or os.stat(ACCOUNTS_FILE).st_size == 0:
        df = pd.DataFrame(columns=["username", "email", "password", "UID"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV safely"""
    check_or_create_file()
    try:
        return pd.read_csv(ACCOUNTS_FILE, dtype=str)  # Ensure UID is treated as a string
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["username", "email", "password", "UID"])

def account_UI():
    """Display Account Settings UI"""
    st.title("\n -- Account Settings --")

    if st.session_state["logged_in"]:
        st.write(f"Logged in as: **{st.session_state['username']}**")
        st.write(f"UID: **{st.session_state['UID']}**")
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
            st.session_state["UID"] = user.iloc[0]["UID"]  # Set UID after login
            st.session_state["page"] = "settings"
            st.rerun()
        else:
            st.write("❌ Invalid username/email or password.")

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.rerun()

def logout():
    """Logout User"""
    st.session_state.clear()
    st.session_state["page"] = "settings"
    st.rerun()

def generate_UID(_username, admin_UID=None):
    """Generate UID for admin and sub-accounts."""
    first_part = _username[:4]
    
    if admin_UID:  # If admin is creating a sub-account
        base_UID = admin_UID[:-1]  # Remove last digit (0)
        existing_uids = load_accounts()["UID"].tolist()
        existing_uids = [str(uid) for uid in existing_uids]  # Ensure they are strings
        suffix = 1  # Start with "1"
        while str(base_UID) + str(suffix) in existing_uids:
            suffix += 1
        return str(base_UID) + str(suffix)
    
    # Generate UID for new admin account
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return first_part + random_numbers + "0"

def create_account():
    """Create a new account and save to CSV"""
    st.write("\n--- Create New Account ---")
    username = st.text_input("Enter username:").strip()
    email = st.text_input("Enter email:").strip()
    password = st.text_input("Enter password:", type="password").strip()

    admin_UID = st.session_state.get("UID", None)
    is_admin = admin_UID and str(admin_UID).endswith("0")

    if is_admin:
        st.write("🔹 You are an admin. You can create sub-accounts.")
        if st.button("Generate Sub-Account"):
            sub_UID = generate_UID(username, admin_UID)
            st.write(f"✅ Sub-Account UID: **{sub_UID}**")

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

        # Generate UID based on admin or regular user
        UID = generate_UID(username, admin_UID) if is_admin else generate_UID(username)

        # Append new user
        new_user = pd.DataFrame([[username, email, password, UID]], columns=["username", "email", "password", "UID"])
        new_user.to_csv(ACCOUNTS_FILE, mode='a', header=False, index=False)

        st.write(f"✅ Account created successfully! Your UID: **{UID}**")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["UID"] = UID
        st.session_state["page"] = "settings"
        st.rerun()


# **Navigation Handling**
if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "create_account":
    create_account()