import streamlit as st
import os
import pandas as pd
from st_pages import hide_pages

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
    st.session_state["page"] = "login"  # Default to login page

def check_or_create_file():
    """Ensure the accounts CSV file exists with headers"""
    if not os.path.exists(ACCOUNTS_FILE) or os.stat(ACCOUNTS_FILE).st_size == 0:
        df = pd.DataFrame(columns=["username", "email", "password", "role", "UID"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV safely"""
    check_or_create_file()
    try:
        return pd.read_csv(ACCOUNTS_FILE, dtype=str)  # Ensure UID is treated as a string
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["username", "email", "password", "role", "UID"])

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
            st.session_state["role"] = user.iloc[0]["role"]

            # Check role and hide pages if not admin
            if st.session_state["role"] == "Admin":
                hide_pages([])
            else:
                hide_pages(["Admin"])  

            st.session_state["page"] = "settings"
            st.rerun()
        else:
            st.write("❌ Invalid username/email or password.")

    if st.button("Back"):
        st.session_state["page"] = "settings"
        st.rerun()

def account_UI():
    """Display Account Settings UI"""
    st.title("\n -- Account Settings --")

    if st.session_state["logged_in"]:
        st.write(f"Logged in as: **{st.session_state['username']}**")
        st.write(f"UID: **{st.session_state['UID']}**")
        if st.button("Logout"):
            logout()
    else:
        if st.button("Login"):
            st.session_state["page"] = "login"

def logout():
    """Logout User"""
    st.session_state.clear()
    st.session_state["page"] = "settings"
    st.rerun()

# **Navigation Handling**
if st.session_state["page"] == "settings":
    account_UI()
elif st.session_state["page"] == "login":
    login()

st.write("Session State Debug:", {
    "logged_in": st.session_state.get("logged_in"),
    "username": st.session_state.get("username"),
    "UID": st.session_state.get("UID"),
    "role": st.session_state.get("role"),
    "page": st.session_state.get("page"),
})
