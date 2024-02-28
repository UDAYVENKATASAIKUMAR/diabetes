import streamlit as st
import sqlite3
import subprocess
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if not username or not password:
            st.error("Username or password cannot be empty.")
            return None
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            return username
        else:
            st.error("Invalid username or password")
            return None
def register():
    st.title("Register")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        if not new_username or not new_password:
            st.error("Username or password cannot be empty.")
            return False
        add_user(new_username, new_password)
        st.success("Registration successful. You can now login.")
        return True
def main():
    create_table()
    pages = st.sidebar.selectbox("Navigation", ["Login", "Register"])
    if pages == "Login":
        username = login()
        if username:
            subprocess.Popen(["streamlit", "run", "diabeticpredict.py","--",username]) 
    elif pages == "Register":
        register()

if __name__ == "__main__":
    main()
