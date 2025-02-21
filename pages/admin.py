import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv"

def load_accounts():
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    df.to_csv(ACCOUNTS_FILE, index=False)

def create_account():
    st.subheader("Create a New User")
    new_username = st.text_input("New Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    if st.button("Create User"):
        accounts = load_accounts()
        if new_username in accounts["username"].values:
            st.error("Username already exists!")
        else:
            new_user = pd.DataFrame([[new_username, new_email, new_password, "user"]],
                                    columns=["username", "email", "password", "role"])
            accounts = pd.concat([accounts, new_user], ignore_index=True)
            save_accounts(accounts)
            st.success("User created successfully!")

def admin_ui():
    if st.button("Manage Accounts"):
        st.session_state["adminpage"] = "accounts"
    if st.button("Medication Tracker"):
        st.session_state["adminpage"] = "medication"
    if st.button("Event Edit"):
        st.session_state["adminpage"] = "events"

# Navigation UI
st.title("Admin Page")
if "role" in st.session_state and st.session_state["role"] == "Admin":
    # Check if session_state["adminpage"] exists; if not, initialize it
    if "adminpage" not in st.session_state:
        st.session_state["adminpage"] = "admin"
    
    # Handle page rendering based on the selected admin page
    if st.session_state["adminpage"] == "admin":
        admin_ui()
    elif st.session_state["adminpage"] == "accounts":
        create_account()
    elif st.session_state["adminpage"] == "medication":
        st.write("Medication Tracker Page")  # Placeholder for medication page
    elif st.session_state["adminpage"] == "events":
        st.write("Event Edit Page")  # Placeholder for event edit page
else:
    st.error("Access denied. Admins only.")