import streamlit as st
import os
import pandas as pd
import random
from st_pages import get_nav_from_toml, hide_pages # type: ignore



# File to store account data
ACCOUNTS_FILE = "accounts.csv"

def check_or_create_file():
    """Ensure the accounts CSV file exists with headers"""
    if not os.path.exists(ACCOUNTS_FILE) or os.stat(ACCOUNTS_FILE).st_size == 0:
        df = pd.DataFrame(columns=["username", "email", "password", "UID", "role"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    """Load accounts from CSV safely"""
    check_or_create_file()
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    """Save accounts back to CSV"""
    df.to_csv(ACCOUNTS_FILE, index=False)

def generate_uid(role, count):
    """Generate UID ending in yxx where y=0 for admin, 1 for user, and xx is count"""
    return f"{role}{count:02d}"

def create_account(username, email, password, role):
    df = load_accounts()
    user_count = len(df[df["role"] == role])
    uid = generate_uid(role, user_count + 1)
    new_account = pd.DataFrame([[username, email, password, uid, role]], columns=df.columns)
    df = pd.concat([df, new_account], ignore_index=True)
    save_accounts(df)
    return uid

# --- ADMIN PAGE ---
def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Welcome, Admin!")
    if st.button("Create User Account"):
        st.session_state.page = "create_user"

# --- USER CREATION PAGE ---
def create_user_page():
    st.title("Create User Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create User"):
        uid = create_account(username, email, password, "1")
        st.success(f"User account created! UID: {uid}")

# --- LOGIN PAGE ---
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        df = load_accounts()
        user = df[(df["username"] == username) & (df["password"] == password)]
        if not user.empty:
            role = user.iloc[0]["role"]
            if role == "0":
                st.session_state.page = "admin"
            else:
                st.session_state.page = "user"
        else:
            st.error("Invalid credentials")

# --- MAIN ---
if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "admin":
    admin_dashboard()
elif st.session_state.page == "create_user":
    create_user_page()
