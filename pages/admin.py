import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv"

def load_accounts():
    """Load the accounts from the CSV file"""
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    """Save the updated accounts back to the CSV file"""
    df.to_csv(ACCOUNTS_FILE, index=False)

def generate_uid():
    """Generate a UID starting from 1000 and incrementing"""
    accounts = load_accounts()
    # Get the highest UID from the existing accounts 
    if not accounts.empty:
        last_uid = accounts["UID"].max()
        return str(int(last_uid) + 1)
    else:
        return "1000"  # Start from UID 1000 if no users currently exist

def manage_account():
    """Create a new user account or delete an existing account"""
    st.subheader("Manage User Accounts")

    # Create a new user
    st.text("Create a New User")
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
            # Generate UID for the new user
            new_uid = generate_uid()

            # Add the new user with the role of "user" and the generated UID
            new_user = pd.DataFrame([[new_username, new_email, new_password, "user", new_uid]],
                                    columns=["username", "email", "password", "role", "UID"])
            accounts = pd.concat([accounts, new_user], ignore_index=True)
            save_accounts(accounts)
            st.success(f"User created successfully with UID: {new_uid}")

    # Delete an existing user by UID
    st.text("Delete a User by UID")
    delete_uid = st.text_input("Enter UID of user to delete")

    if st.button("Delete User"):
        accounts = load_accounts()
        
        # Ensure the UID is an integer and strip any extra spaces
        delete_uid = delete_uid.strip()
        
        # Check if UID exists in the accounts
        if delete_uid.isdigit() and int(delete_uid) in accounts["UID"].values:
            # Remove the user by UID
            accounts = accounts[accounts["UID"] != int(delete_uid)]  # Convert to integer for comparison
            save_accounts(accounts)
            st.success(f"User with UID: {delete_uid} has been deleted.")
        else:
            st.error(f"No user found with UID: {delete_uid}")


    # Delete an existing user by UID
    st.text("Delete a User by UID")
    delete_uid = st.text_input("Enter UID of user to delete")

    if st.button("Delete User"):
        accounts = load_accounts()
        
        # Check if UID exists in the accounts
        if delete_uid not in accounts["UID"].values:
            st.error(f"No user found with UID: {delete_uid}")
        else:
            # Remove the user by UID
            accounts = accounts[accounts["UID"] != delete_uid]
            save_accounts(accounts)
            st.success(f"User with UID: {delete_uid} has been deleted.")

def show_all_users():
    """Show a table of all users"""
    st.subheader("All Users")
    accounts = load_accounts()
    if not accounts.empty:
        st.write(accounts)
    else:
        st.write("No users found.")

def admin_ui():
    """UI for Admin to manage users and pages"""
    if st.button("Manage Accounts"):
        st.session_state["adminpage"] = "accounts"
    if st.button("Show All Users"):
        st.session_state["adminpage"] = "show_users"
    if st.button("Medication Tracker"):
        st.session_state["adminpage"] = "medication"
    if st.button("Event Edit"):
        st.session_state["adminpage"] = "events"

def medication_ui():
    if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page


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
        manage_account()  # Admin can create and delete user accounts
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
    elif st.session_state["adminpage"] == "show_users":
        show_all_users()  # Show all users
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
    elif st.session_state["adminpage"] == "medication":
        st.write("Medication Tracker Page")  # Placeholder for medication page
        medication_ui()
    elif st.session_state["adminpage"] == "events":
        st.write("Event Edit Page")  # Placeholder for event edit page
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
else:
    st.error("Access denied. Admins only.")
