#Tyler
import streamlit as st
import os
import pandas as pd
from st_pages import hide_pages #Allows for admin.py to be hid

# File to store account data
ACCOUNTS_FILE = "accounts.csv"

#Creation of accounts can ONLY be done by ADMINS in pages/admin.py

# Initialize session state (Session State Is Shared Between Pages)
if "logged_in" not in st.session_state: #For if user is logged in
    st.session_state["logged_in"] = False
if "username" not in st.session_state: #To store username (Use csv file instead)
    st.session_state["username"] = None
if "UID" not in st.session_state: #UID
    st.session_state["UID"] = None
if "role" not in st.session_state: #User/Admin
    st.session_state["role"] = None

if "page" not in st.session_state: #To determine which page gets shown
    st.session_state["page"] = "login"  # Default to login page

def check_or_create_file(): #Check if file exists, and create the file if it does not
    #Ensure the accounts CSV file exists with headers
    if not os.path.exists(ACCOUNTS_FILE) or os.stat(ACCOUNTS_FILE).st_size == 0: 
        df = pd.DataFrame(columns=["username", "email", "password", "role", "UID"])
        df.to_csv(ACCOUNTS_FILE, index=False)

def load_accounts():
    #Load accounts from CSV safely
    check_or_create_file()
    try:
        return pd.read_csv(ACCOUNTS_FILE, dtype=str) 
    except pd.errors.EmptyDataError: #Incase its empty
        return pd.DataFrame(columns=["username", "email", "password", "role", "UID"])

def login():
    #Login User
    st.title("\n--- Login ---") #Titel
    identifier = st.text_input("Enter username or email:").strip() #Email / Username 
    password = st.text_input("Enter password:", type="password").strip() #Pswd

    if st.button("Submit"): #Click to submit
        df = load_accounts() #Loads the pretermined data

        user = df[(df["username"] == identifier) | (df["email"] == identifier)] 
        if not user.empty and user.iloc[0]["password"] == password: #ensures that the pswd & identifier matches the ones in csv file
            st.session_state["logged_in"] = True
            st.session_state["username"] = user.iloc[0]["username"]
            st.session_state["UID"] = user.iloc[0]["UID"]  # Set UID after login
            st.session_state["role"] = user.iloc[0]["role"] 

            # Check role and hide pages if not admin
            if st.session_state["role"] == "Admin":
                hide_pages([]) #Admin page unhid (Can see in sidebar)
            else:
                hide_pages(["Admin"])  #Hides admin page (For non-admins)

            st.session_state["page"] = "settings" #Sends them to settings page
            st.rerun()
        else:
            st.write("❌ Invalid username/email or password.") #Error mssage

    if st.button("Back"): #Back to settings
        st.session_state["page"] = "settings" #Changes sessions state to settings
        st.rerun()

def account_UI():
    #Display Account Settings UI
    st.title("\n -- Account Settings --") #Titleee

    if st.session_state["logged_in"]: #Checks if user is logged in
        st.write(f"Logged in as: **{st.session_state['username']}**") #Displays username
        st.write(f"UID: **{st.session_state['UID']}**") #Displays UID
        if st.button("Logout"): #Logout button
            logout() 
    else: #If user isnt logged in
        if st.button("Login"): #Login utton
            st.session_state["page"] = "login" #Sends them to login page 

def logout():
    #Logout User
    st.session_state.clear()
    st.session_state["page"] = "settings"
    st.rerun()

# **Navigation Handling**
if st.session_state["page"] == "settings": #Settings
    account_UI()
elif st.session_state["page"] == "login":
    login()

#FOR DEBUGGING ONLY (Remove when done)
#st.write("Session State Debug:", {
    #"logged_in": st.session_state.get("logged_in"),
    #"username": st.session_state.get("username"),
    #"UID": st.session_state.get("UID"),
    #"role": st.session_state.get("role"),
    #"page": st.session_state.get("page"),
#})
