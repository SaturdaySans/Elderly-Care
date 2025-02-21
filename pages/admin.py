import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv"
MEDICATION_FILE = "medication.csv"
EVENTS_FILE = "events.csv"

def load_accounts():
    """Load the accounts from the CSV file"""
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    """Save the updated accounts back to the CSV file"""
    df.to_csv(ACCOUNTS_FILE, index=False)

def load_medications():
    """Load the medication data from the CSV file"""
    return pd.read_csv(MEDICATION_FILE)

def save_medications(df):
    """Save the updated medications back to the CSV file"""
    df.to_csv(MEDICATION_FILE, index=False)

def load_events():
    """Load the events from the CSV file"""
    return pd.read_csv(EVENTS_FILE)

def save_events(df):
    """Save the updated events back to the CSV file"""
    df.to_csv(EVENTS_FILE, index=False)

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
    delete_uid = st.text_input("Enter UID of user to delete", key=f"delete_uid_input_{st.session_state.get('adminpage', 'admin')}")  # Dynamic key

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

def manage_medications():
    """Add or edit medications in the CSV file"""
    st.subheader("Manage Medications")

    # Form to add new medication entry (without "Taken" field)
    medication_name = st.text_input("Medication Name")
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    uid = st.text_input("UID of Patient")

    if st.button("Add Medication"):
        # Check if all fields are filled
        if not medication_name or not time_of_day or not uid:
            st.error("All fields are required!")
            return

        medications = load_medications()

        # Add the new medication to the list (no "Taken" field)
        new_medication = pd.DataFrame([[medication_name, time_of_day, "No", uid]],  # Default "Taken" as "No"
                                      columns=["Medication", "Time", "Taken", "UID"])
        medications = pd.concat([medications, new_medication], ignore_index=True)
        save_medications(medications)
        st.success("Medication added successfully!")

    # Edit existing medication entry
    st.subheader("Edit Existing Medication Entry")

    # Display existing medications
    medications = load_medications()
    if not medications.empty:
        st.write(medications)

        medication_to_edit = st.selectbox("Select Medication to Edit", medications["Medication"].unique())

        # Get the selected medication details
        selected_medication = medications[medications["Medication"] == medication_to_edit]

        # Edit form (but do not allow editing the "Taken" field)
        new_time = st.selectbox("Edit Time of Day", ["Morning", "Afternoon", "Evening", "Night"], index=["Morning", "Afternoon", "Evening", "Night"].index(selected_medication["Time"].values[0]))
        new_uid = st.text_input("Edit UID of Patient", value=selected_medication["UID"].values[0])

        if st.button("Save Changes"):
            # Update the selected medication entry (skip "Taken" field)
            medications.loc[medications["Medication"] == medication_to_edit, ["Time", "UID"]] = [new_time, new_uid]
            save_medications(medications)
            st.success("Medication details updated successfully!")

    else:
        st.write("No medications found.")

    # Delete medication entry
    st.subheader("Delete Medication Entry")
    medication_to_delete = st.selectbox("Select Medication to Delete", medications["Medication"].unique())

    if st.button("Delete Medication"):
        # Delete the selected medication from the list
        medications = medications[medications["Medication"] != medication_to_delete]
        save_medications(medications)
        st.success(f"Medication '{medication_to_delete}' has been deleted.")

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
    if st.button("Manage Medications"):
        st.session_state["adminpage"] = "medications"
    if st.button("Show All Users"):
        st.session_state["adminpage"] = "show_users"
    if st.button("Event Edit"):
        st.session_state["adminpage"] = "events"

def medication_ui():
    """Medication Tracker UI"""
    manage_medications()

def events_ui():
    """Event Management UI for Admin"""
    st.subheader("Manage Events")

    # Form to add a new event
    st.text("Add a New Event")
    event_title = st.text_input("Event Title")
    event_start = st.date_input("Start Date")
    event_end = st.date_input("End Date")
    event_resource = st.text_input("Resource ID")

    if st.button("Add Event"):
        # Check if all fields are filled
        if not event_title or not event_start or not event_end or not event_resource:
            st.error("All fields are required!")
            return

        events = load_events()

        # Add the new event to the list
        new_event = pd.DataFrame([[event_title, event_start, event_end, event_resource]],
                                 columns=["title", "start", "end", "resourceId"])
        events = pd.concat([events, new_event], ignore_index=True)
        save_events(events)
        st.success("Event added successfully!")

    # Display existing events
    st.subheader("Existing Events")
    events = load_events()
    if not events.empty:
        st.write(events)

        # Delete an event
        event_to_delete = st.selectbox("Select Event to Delete", events["title"].unique())

        if st.button("Delete Event"):
            # Delete the selected event from the list
            events = events[events["title"] != event_to_delete]
            save_events(events)
            st.success(f"Event '{event_to_delete}' has been deleted.")
    else:
        st.write("No events found.")

# Navigation UI remains the same as before
# Handle the admin UI rendering and manage other sections like "accounts", "medications", etc.

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
    elif st.session_state["adminpage"] == "medications":
        medication_ui()  # Medication management UI
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
    elif st.session_state["adminpage"] == "events":
        events_ui()
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"  # Go back to the admin page
else:
    st.error("Access denied. Admins only.")
