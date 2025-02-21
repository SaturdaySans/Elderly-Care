import streamlit as st
import os
import pandas as pd
import random
from st_pages import get_nav_from_toml, hide_pages
# settings.py
import streamlit as st
import os
import pandas as pd

# File to store account data
ACCOUNTS_FILE = "accounts.csv"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None

def check_or_create_file():
    """Ensure the accounts CSV file exists with headers"""
    if not os.path.exists(ACCOUNTS_FILE):
        df = pd.DataFrame(columns=["username", "email", "password", "role"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV safely"""
    check_or_create_file()
    return pd.read_csv(ACCOUNTS_FILE)

def authenticate(username, password):
    """Authenticate user credentials"""
    accounts = load_accounts()
    user = accounts[(accounts["username"] == username) & (accounts["password"] == password)]
    if not user.empty:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = user.iloc[0]["role"]
        return True
    return False

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if authenticate(username, password):
        st.success(f"Welcome {username}!")
        if st.session_state["role"] == "admin":
            st.page_link("admin.py", label="Go to Admin Page")
    else:
        st.error("Invalid username or password")

if not st.session_state["logged_in"]:
    st.stop()

def create_account():
    """Create a new admin account"""
    new_username = st.text_input("New Admin Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    if st.button("Create Admin Account"):
        accounts = load_accounts()
        if new_username in accounts["username"].values:
            st.error("Username already exists!")
        else:
            new_user = pd.DataFrame([[new_username, new_email, new_password, "admin"]],
                                    columns=["username", "email", "password", "role"])
            accounts = pd.concat([accounts, new_user], ignore_index=True)
            accounts.to_csv(ACCOUNTS_FILE, index=False)
            st.success("Admin account created successfully!")
