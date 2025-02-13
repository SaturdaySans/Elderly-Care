import streamlit as st
import os
import pandas as pd

# Initialize session state for navigation & login state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "settings"  # Default to settings page

ACCOUNTS_FILE = "accounts.csv"

def check_or_create_file():
    """Ensure the accounts file exists"""
    if not os.path.exists(ACCOUNTS_FILE):
        df = pd.DataFrame(columns=["username", "email", "password"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV"""
    check_or_create_file()
    return pd.read_csv(ACCOUNTS_FILE)

def save_account(username, email, password):
    """Save a new account to CSV"""
    df = load_accounts()
    new_user = pd.DataFrame([[username, email, password]], columns=["username", "email", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(ACCOUNTS_FILE, index=False)

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
    st.write("\n--- Login ---")

    with st.form("login_form"):
        identifier = st.text_input("Enter username or email:").strip()
        password = st.text_input("Enter password:", type="password").strip()
        submit = st.form_submit_button("Submit")

    if submit:
        df = load_accounts()
        user = df[(df["username"] == identifier) | (df["email"] == identifier)]

        if not user.empty and user.iloc[0]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user.iloc[0]["username"]
            st.session_state["page"] = "settings"  # Redirect back to settings
            st.experimental_rerun()
        else:
            st.write("❌ Invalid username/email or password.")

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.experimental_rerun()

def logout():
    """Log the user out"""
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["page"] = "settings"
    st.experimental_rerun()

def create_account():
    """Create a new account and save to file"""
    st.write("\n--- Create New Account ---")

    with st.form("register_form"):
        username = st.text_input("Enter username:").strip()
        email = st.text_input("Enter email:").strip()
        password = st.text_input("Enter password:", type="password").strip()
        submit = st.form_submit_button("Register")

    if submit:
        df = load_accounts()

        if not username or not email or not password:
            st.write("❌ All fields are required.")
            return
        if "@" not in email:
            st.write("❌ Invalid email format.")
            return
        if (df["username"] == username).any():
            st.write("❌ Username already taken.")
            return
        if (df["email"] == email).any():
            st.write("❌ Email already in use. Please login.")
            return

        save_account(username, email, password)
        st.write("✅ Account created successfully!")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["page"] = "settings"
        st.experimental_rerun()

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.experimental_rerun()

# **Navigation Handling**
check_or_create_file()  # Ensure file exists

if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "create_account":
    create_account()
