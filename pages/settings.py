import streamlit as st
import os
import pandas as pd
from st_pages import get_nav_from_toml, hide_pages

# File to store account data
ACCOUNTS_FILE = "accounts.csv"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "UID" not in st.session_state:
    st.session_state["UID"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None
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
        return pd.read_csv(ACCOUNTS_FILE, dtype=str)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["username", "email", "password", "UID"])

def generate_UID(is_admin):
    """Generate UID based on account type."""
    df = load_accounts()
    existing_uids = set(df["UID"].tolist())
    suffix = "0" if is_admin else "1"
    uid_base = len(existing_uids) + 1  # Ensures unique ID
    while f"{uid_base}{suffix}" in existing_uids:
        uid_base += 1
    return f"{uid_base}{suffix}"

def create_account():
    """Create a new account."""
    st.write("\n--- Create New Account ---")
    username = st.text_input("Enter username:").strip()
    email = st.text_input("Enter email:").strip()
    password = st.text_input("Enter password:", type="password").strip()
    is_admin = st.checkbox("Create as Admin") if st.session_state["role"] == "Admin" else False

    if st.button("Register"):
        if not username or not email or not password:
            st.write("❌ All fields are required.")
            return
        if "@" not in email:
            st.write("❌ Invalid email format.")
            return

        df = load_accounts()
        if username in df["username"].values or email in df["email"].values:
            st.write("❌ Username or email already taken.")
            return

        UID = generate_UID(is_admin)
        new_user = pd.DataFrame([[username, email, password, UID]], columns=["username", "email", "password", "UID"])
        new_user.to_csv(ACCOUNTS_FILE, mode='a', header=False, index=False)
        st.write(f"✅ Account created successfully! UID: **{UID}**")
        
        # Update session state after successful registration
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["UID"] = UID
        st.session_state["role"] = "Admin" if UID[-1] == "0" else "User"
        
        hide_pages([] if st.session_state["role"] == "Admin" else ["Admin"])
        
        st.session_state["page"] = "settings"
        st.rerun()

def login():
    """Login User."""
    st.write("\n--- Login ---")
    identifier = st.text_input("Enter username or email:").strip()
    password = st.text_input("Enter password:", type="password").strip()

    if st.button("Submit"):
        df = load_accounts()
        user = df[(df["username"] == identifier) | (df["email"] == identifier)]
        if not user.empty and user.iloc[0]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user.iloc[0]["username"]
            st.session_state["UID"] = user.iloc[0]["UID"]
            st.session_state["role"] = "Admin" if str(user.iloc[0]["UID"])[-1] == "0" else "User"
            hide_pages([] if st.session_state["role"] == "Admin" else ["Admin"])
            st.session_state["page"] = "settings"
            st.rerun()
        else:
            st.write("❌ Invalid username/email or password.")
    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.rerun()

def logout():
    """Logout User."""
    st.session_state.clear()
    st.session_state["page"] = "settings"
    hide_pages(["Admin"])
    st.rerun()

def account_UI():
    """Display Account Settings UI."""
    st.title("\n -- Account Settings --")

    if st.session_state["logged_in"]:
        st.write(f"Logged in as: **{st.session_state['username']}**")
        st.write(f"UID: **{st.session_state['UID']}**")
        if st.button("Logout"):
            logout()
        if st.session_state["role"] == "Admin" and st.button("Create User Account"):
            st.session_state["page"] = "create_account"
        if st.button("Login"):
            st.session_state["page"] = "login"
        hide_pages([] if st.session_state["role"] == "Admin" else ["Admin"])
    else:
        if st.button("Create Account"):
            st.session_state["page"] = "create_account"
        if st.button("Login"):
            st.session_state["page"] = "login"

# **Navigation Handling**
if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "create_account":
    create_account()
st.write("Session State Debug:", {
    "logged_in": st.session_state.get("logged_in"),
    "username": st.session_state.get("username"),
    "UID": st.session_state.get("UID"),
    "role": st.session_state.get("role"),
    "page": st.session_state.get("page"),
})
