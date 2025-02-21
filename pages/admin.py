import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv"

def load_accounts():
    """Load the accounts from the CSV file"""
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    """Save the updated accounts back to the CSV file"""
    df.to_csv(ACCOUNTS_FILE, index=False)

def create_account():
    """Create a new user account"""
    st.subheader("Create a New User")
    
    new_username = st.text_input("New Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    
    if st.button("Create User"):
        # Check if the required fields are filled
        if not new_username or not new_email or not new_password:
            st.error("All fields are required!")
            return

        accounts = load_accounts()

        # Check if the username already exists
        if new_username in accounts["username"].values:
            st.error("Username already exists!")
        else:
            # Add the new user with the role of "user"
            new_user = pd.DataFrame([[new_username, new_email, new_password, "user"]],
                                    columns=["username", "email", "password", "role"])
            accounts = pd.concat([accounts, new_user], ignore_index=True)
            save_accounts(accounts)
            st.success("User created successfully!")

def admin_ui():
    """UI for Admin to manage users and pages"""
    if st.button("Manage Accounts"):
        st.session_state["adminpage"] = "accounts"
    if st.button("Medication Tracker"):
        st.session_state["adminpage"] = "medication"
    if st.button("Event Edit"):
        st.session_state["adminpage"] = "events"

# Navigation UI
st.title("Admin Page")

# Check if the user is an Admin
if "role" in st.session_state and st.session_state["role"] == "Admin":
    # Initialize session state["adminpage"] if it does not exist
    if "adminpage" not in st.session_state:
        st.session_state["adminpage"] = "admin"
    
    # Handle page rendering based on the selected admin page
    if st.session_state["adminpage"] == "admin":
        admin_ui()
    elif st.session_state["adminpage"] == "accounts":
        create_account()  # Admin can create user accounts
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
    elif st.session_state["adminpage"] == "medication":
        st.write("Medication Tracker Page")  # Placeholder for medication page
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
    elif st.session_state["adminpage"] == "events":
        st.write("Event Edit Page")  # Placeholder for event edit page
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
else:
    st.error("Access denied. Admins only.")
