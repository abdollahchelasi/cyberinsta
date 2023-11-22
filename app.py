import streamlit as st

# Create a form to collect the username and password
username = st.text_input("Username")
password = st.text_input("Password")

# If the user clicks on the submit button
if st.button("Submit"):

    # Save the username and password to a file
    with open("data.txt", "w") as f:
        f.write(f"username={username}\npassword={password}")

    st.write("Username and password saved successfully!")
