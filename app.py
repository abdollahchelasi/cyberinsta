import streamlit as st
import sqlite3

# Create a database connection
conn = sqlite3.connect("todo.db")

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    completed BOOLEAN NOT NULL
)""")

# Create a form to collect todo item information
with st.form("Todo Form"):
    text = st.text_input("Todo item")
    passw = st.text_input("Pass", type="password")
    submit_button = st.form_submit_button("Add Todo")



    # If the form is submitted
    if submit_button:        
        
        # Save the todo item in the database
        c1 , c2 = st.columns(2)
        with c1:
            
            c.execute("INSERT INTO todos (text, completed) VALUES (?, ?)", (text, False))
        
        with c2:
            
            c.execute("INSERT INTO todos (text, completed) VALUES (?, ?)", (passw, False))
        
        conn.commit()

        # Display a success message
        st.success("Todo item added successfully")

# Get all todo items from the database
c.execute("SELECT * FROM todos")
todos = c.fetchall()







name = st.text_input("Name")
pas = st.text_input("Pass", type="password")
# subm = st.form_submit_button("Login")


if name == "a" and pas == "ch":
    

# Display the todo items
    for todo in todos:
    # id = todo[0]
    
        c1 , c2 = st.columns(2)
        with c1:
        
            text = todo[1]
    # passw = todo[2]
    # completed = todo[2]
        with c2:
        
            st.markdown(f" Name And Pass : {text}  {passw}")
    
    
    
        
        st.divider()
    
   
   
conn.close()



