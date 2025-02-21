import streamlit as st
import pandas as pd

ACCOUNTS_FILE = "accounts.csv"

def load_accounts():
    return pd.read_csv(ACCOUNTS_FILE)

def save_accounts(df):
    df.to_csv(ACCOUNTS_FILE, index=False)
    
st.title("Admin Page")
if "role" in st.session_state["role"] == "admin":
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
else:
    st.error("Access denied. Admins only.")
