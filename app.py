import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor
c = conn.cursor()

# Create a form to collect the username and password
username = st.text_input("Username")
password = st.text_input("Password")

# If the user clicks on the submit button
if st.button("Submit"):

    # Insert the username and password into the database
    # c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    # conn.commit()
    
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )""")
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    # Commit the changes to the database
    conn.commit()

    st.write("Username and password saved successfully!")

# Close the connection to the database
conn.close()
