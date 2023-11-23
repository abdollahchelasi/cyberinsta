import streamlit as st

def main():
    st.title("Login Form")

    # Create a form to collect user information
    with st.form("Login Form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            # Save the username and password to a file
            save_credentials(username, password)
            st.success("Login successful")

def save_credentials(username, password):
    # Save the username and password to a file
    with open("credentials.txt", "w") as file:
        file.write(f"Username: {username}, Password: {password}")

if __name__ == "__main__":
    main()
