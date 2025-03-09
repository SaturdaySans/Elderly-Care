import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv" #Declare file path 
MEDICATION_FILE = "medication.csv" #File path
EVENTS_FILE = "events.csv" #DFP
ROUTINE_FILE = "daily_routine.csv" #Declare file pathh

#Functions
#This page works by st.sessionstate determining which page/part your currently located
def load_accounts(): #loads accs from file csv
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df): # Saves the data back
    df.to_csv(ACCOUNTS_FILE, index=False)

def load_medications(): # Loads health/medicine datat
    return pd.read_csv(MEDICATION_FILE)

def save_medications(df): #Save medication
    df.to_csv(MEDICATION_FILE, index=False)

def load_events(): #Load events from events . cee ess vee
    return pd.read_csv(EVENTS_FILE)

def save_events(df): #Save events down
    df.to_csv(EVENTS_FILE, index=False)

def generate_uid(): #Fubnction for generating uid
    accounts = load_accounts()
    # Get the highest UID from the existing accounts
    if not accounts.empty:
        last_uid = accounts["UID"].max() #Get largest uid from our csv file yeah
        return str(int(last_uid) + 1) # Plus one to largest uid ^^^
    else:
        return "1000"  # Start from 1000 if no users currently exist

def manage_account(): #For managing accounts
    """Create a new user account or delete an existing account"""
    st.subheader("Manage User Accounts") #Title

    # Create a new user
    st.text("Create a New User")
    new_username = st.text_input("New Username") #Input username here
    new_email = st.text_input("Email") # Email inptu
    new_password = st.text_input("Password", type="password") # Pswd input

    if st.button("Create User"): #Button 
        # Check if the required fields are filled
        if not new_username or not new_email or not new_password: # k
            st.error("All fields are required!") # Error msg
            return 

        accounts = load_accounts() #Loads acount, self explanatory

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

    if st.button("Delete User"): #For deleting user
        accounts = load_accounts()

        # Ensure the UID is an integer and strip any extra spaces
        delete_uid = delete_uid.strip()

        # Check if UID exists in the accounts
        if delete_uid == "1000": #You cant remove my admin rights 
            st.error("The user with UID 1000 cannot be deleted.")  # Prevent deletion of UID 1000
            return
        elif delete_uid.isdigit() and int(delete_uid) in accounts["UID"].values:
            # Remove the user by UID
            accounts = accounts[accounts["UID"] != int(delete_uid)]  # Convert to integer for comparison
            save_accounts(accounts)
            st.success(f"User with UID: {delete_uid} has been deleted.") # Success msg
        else:
            st.error(f"No user found with UID: {delete_uid}") # If no user found

def manage_medications():
    """Add or edit medications in the CSV file""" 
    st.subheader("Manage Medications") #Header

    # Form to add new medication entry (without "Taken" field)
    medication_name = st.text_input("Medication Name") #Input the name of the medicine for the elderli to see the name of the medicine
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])  # When to consume medcine
    uid = st.text_input("UID of Patient") # Which elderly is it

    if st.button("Add Medication"): #Button
        # Check if all fields are filled
        if not medication_name or not time_of_day or not uid: #Check if all fields are filled
            st.error("All fields are required!") # errror message
            return


        medications = load_medications() #loads medicine

        #Add the new medication to the list (no "Taken" field)
        new_medication = pd.DataFrame([[medication_name, time_of_day, "No", uid]],  #default "Taken" as "No"
                                      columns=["Medication", "Time", "Taken", "UID"]) 
        medications = pd.concat([medications, new_medication], ignore_index=True) #Concat it in
        save_medications(medications)
        st.success("Medication added successfully!") # sucess message

    # Edit existing medication entry
    st.subheader("Edit Existing Medication Entry")

    # Display existing medications
    medications = load_medications() #Loads medication
    if not medications.empty: 
        st.write(medications)

        medication_to_edit = st.selectbox("Select Medication to Edit", medications["Medication"].unique()) # Dropdown box

        # Get the selected medication details
        selected_medication = medications[medications["Medication"] == medication_to_edit]

        #Edit form 
        new_time = st.selectbox("Edit Time of Day", ["Morning", "Afternoon", "Evening", "Night"], index=["Morning", "Afternoon", "Evening", "Night"].index(selected_medication["Time"].values[0]))
        new_uid = st.text_input("Edit UID of Patient", value=selected_medication["UID"].values[0])

        if st.button("Save Changes"):
            # Update the selected medication entry
            medications.loc[medications["Medication"] == medication_to_edit, ["Time", "UID"]] = [new_time, new_uid] # I didnt write this part of the code
            save_medications(medications)
            st.success("Medication details updated successfully!") # Success meessage

    else:
        st.write("No medications found.")

    # Delete medication entry
    st.subheader("Delete Medication Entry") #Subeader for the medication thing
    medication_to_delete = st.selectbox("Select Medication to Delete", medications["Medication"].unique()) # selectbox agian

    if st.button("Delete Medication"): # Button for deleting medi
        # Delete the selected medication from the list
        medications = medications[medications["Medication"] != medication_to_delete] #Delete medicine
        save_medications(medications) 
        st.success(f"Medication '{medication_to_delete}' has been deleted.") #Deleted message

def show_all_users(): #Print out the user data, (in ta table format)
    st.subheader("All Users") #Subheader
    accounts = load_accounts() #load accounts
    if not accounts.empty: # check if account empty
        st.write(accounts)
    else:
        st.write("No users found.") # no user found

def admin_ui(): #⌘c ⌘v, sets the current page to each of the following
    if st.button("Manage Accounts"):
        st.session_state["adminpage"] = "accounts" 
    if st.button("Manage Medications"):
        st.session_state["adminpage"] = "medications"
    if st.button("Show All Users"):
        st.session_state["adminpage"] = "show_users"
    if st.button("Event Edit"):
        st.session_state["adminpage"] = "events"
    if st.button("Profile Viewer"):
        st.session_state["adminpage"] = "profile"
    if st.button("Routine Edit"):
        st.session_state["adminpage"] = "routine"

def medication_ui(): #ui
    manage_medications() #unnecessary function

def events_ui(): #Events management ui
    st.subheader("Manage Events") # Subheader

    # Form to add a new event
    st.text("Add a New Event") # Text
    event_title = st.text_input("Event Title") #Text input
    event_start_date = st.date_input("Start Date") # Date input
    event_start_time = st.time_input("Start Time") # Start time
    event_end_date = st.date_input("End Date") # you get it
    event_end_time = st.time_input("End Time")
    event_resource = st.text_input("Resource ID")

    if st.button("Add Event"): # Button for adding events
        # Check if all fields are filled
        if not event_title or not event_start_date or not event_start_time or not event_end_date or not event_end_time or not event_resource:
            st.error("All fields are required!") # to make sure eevery field is filed
            return

        events = load_events() #Data

        event_start = pd.to_datetime(f"{event_start_date} {event_start_time}") # Combine date and time
        event_end = pd.to_datetime(f"{event_end_date} {event_end_time}")

        #add the new event to the list
        new_event = pd.DataFrame([[event_title, event_start, event_end, event_resource]],
                                 columns=["title", "start", "end", "resourceId"])
        events = pd.concat([events, new_event], ignore_index=True)
        save_events(events) #Save events
        st.success("Event added successfully!") #sucess msg

    #display existing events
    st.subheader("Existing Events")
    events = load_events() #load event
    if not events.empty: #not empty event
        st.write(events) #write event

        #delete event
        event_to_delete = st.selectbox("Select Event to Delete", events["title"].unique())


        if st.button("Delete Event"): #button to delete event
            # Delete the selected event from the list
            events = events[events["title"] != event_to_delete]
            save_events(events)
            st.success(f"Event '{event_to_delete}' has been deleted.")
    else:
        st.write("No events found.") #No found events

def profile_viewer_ui(): # Admins to view user uid, medication status & email pswd
    st.subheader("Profile Viewer") #Headers

    #Input field to enter UID to view user profile
    uid_to_view = st.text_input("Enter UID of the user to view their profile", key="uid_input_profile")

    if st.button("View Profile", key="view_profile_button"): #button
        if not uid_to_view: # if no uid
            st.error("Please enter a UID.") # please enter uid
            return

        #Clean up the UID 
        uid_to_view = uid_to_view.strip()

        if not uid_to_view.isdigit(): #Checkfs if it the uid is a digit!!!!
            st.error("Please enter a valid UID.") #Error msg #30
            return

        #load accounts and ensure UID is treated as a string
        accounts = load_accounts() #its 4 am
        accounts["UID"] = accounts["UID"].astype(str)  # Ensure the UID column is treated as a string
        medications = load_medications() #load medication

        # Ensure the medications UID is treated as a string as well
        medications["UID"] = medications["UID"].astype(str)  # Ensure medications UID is a string

        #Checks if UID exists in the accounts
        user_data = accounts[accounts["UID"] == uid_to_view]

        if user_data.empty: #If there is no data found (Match)
            st.error(f"No user found with UID: {uid_to_view}")
        else:
            #Display User details
            st.write("### User Details") #Write
            st.write(f"**Username**: {user_data['username'].values[0]}") #username
            st.write(f"**Email**: {user_data['email'].values[0]}") #Email
            st.write(f"**Password**: {user_data['password'].values[0]}") #For resetting passwords

            # Display the medications for the given UID
            user_medications = medications[medications["UID"] == uid_to_view]

            if not user_medications.empty: #not empy
                st.write("### Medications") #write
                # Display medication name, time, and taken status
                st.write(user_medications[["Medication", "Time", "Taken"]])  # I
            else:
                st.write("No medications found for this user.") #Error message


def load_routines(): #load routines from csv file, not sure why this is down here instead
    return pd.read_csv(ROUTINE_FILE)

def save_routines(df): #saves routine
    df.to_csv(ROUTINE_FILE, index=False)

def routine_editor_ui(): #Routine editor
    st.subheader("Manage Routines")

    # Load existing routines
    routines = load_routines() #Load routines

    if not routines.empty: #if routine isnt empty
        st.write(routines) #write out the routine
    else:
        st.write("No routines found.") #when no rroutine found

    # Add a new routine
    st.text("Add a New Routine") #text to add routine
    event_name = st.text_input("Event Name") # event name input
    start_time = st.time_input("Start Time") #time input
    end_time = st.time_input("End Time") #end time input

    if st.button("Add Routine"): #button to add routine
        if event_name:
            start = start_time.hour * 100 + start_time.minute  #Convert time to right format
            end = end_time.hour * 100 + end_time.minute 
            # Calculate duration based on start and end time
            duration = (end - start) if end >= start else (end + 2400 - start) 

            # Ensure the duration is always positive
            new_routine = pd.DataFrame([[event_name, start, end, duration]],
                                        columns=["Events", "Start", "End", "Duration"]) # dataframe
            routines = pd.concat([routines, new_routine], ignore_index=True) #add it in
            save_routines(routines)
            st.success("Routine added successfully!") #successs message

    # Edit an existing routine
    if not routines.empty: # add comments for this
        st.subheader("Edit Existing Routine") # subheader
        routine_to_edit = st.selectbox("Select Routine", routines["Events"].unique()) # Selectbox
        selected_routine = routines[routines["Events"] == routine_to_edit] #Selected routine
        
        #Convert time
        start_hour = selected_routine["Start"].values[0] // 100 
        start_minute = selected_routine["Start"].values[0] % 100
        end_hour = selected_routine["End"].values[0] // 100
        end_minute = selected_routine["End"].values[0] % 100

        new_start_time = st.time_input("Edit Start Time", value=pd.to_datetime(f"2022-01-01 {start_hour}:{start_minute}").time())
        new_end_time = st.time_input("Edit End Time", value=pd.to_datetime(f"2022-01-01 {end_hour}:{end_minute}").time())

        #Calculate new duration
        new_start = new_start_time.hour * 100 + new_start_time.minute
        new_end = new_end_time.hour * 100 + new_end_time.minute
        new_duration = (new_end - new_start) if new_end >= new_start else (new_end + 2400 - new_start)  # Handle crossing midnight

        if st.button("Save Changes"): #Button to save
            routines.loc[routines["Events"] == routine_to_edit, ["Start", "End", "Duration"]] = [new_start, new_end, new_duration]
            save_routines(routines) #saves routine
            st.success("Routine updated successfully!") #success message

    # Delete a routine
    if not routines.empty: #if routine filled
        st.subheader("Delete Routine") #delete outine
        routine_to_delete = st.selectbox("Select Routine to Delete", routines["Events"].unique()) #dropbar to choose which one to dt
        if st.button("Delete Routine"): #button
            routines = routines[routines["Events"] != routine_to_delete] #remove it
            save_routines(routines)
            st.success(f"Routine '{routine_to_delete}' deleted.")








# NAVIGATION UI
st.title("---Admin Page---")

#Check if the user is an Admin
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
            st.session_state["adminpage"] = "admin" # Go back to the admin page
    elif st.session_state["adminpage"] == "events":
        events_ui() #Load Events UI
        if st.button("Back"):
            st.session_state["adminpage"] = "admin" # Go back to the admin page
    elif st.session_state["adminpage"] == "profile":
        profile_viewer_ui()
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"# Go back to the admin page
    elif st.session_state["adminpage"] == "routine":
        routine_editor_ui()
        if st.button("Back"):
            st.session_state["adminpage"] = "admin"# Go back to the admin page
else:
    st.error("Access denied. Admins only.")

# Sorry for the Gramatical errors
# We couldnt fix the need to double click to switch pages (st.rerun)