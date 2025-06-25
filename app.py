import streamlit as st
from factorial import fact
import os

def load_users():
    """Read the user list from user.txt"""
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("File user.txt does not exist!")
            return []
    except Exception as e:
        st.error(f"Error reading user.txt file: {e}")
        return []

def login_page():
    """Login Page"""
    st.title("Login")

    username = st.text_input("Enter username:")

    if st.button("Login"):
        if username:
            users = load_users()
        if username in users:
            st.session_state.logged_in = True   
            st.session_state.username = username
            st.rerun() 
        else:
            st.session_state.show_greeting = True
            st.session_state.username = username
            st.rerun()
    else:
        st.warning("Please enter a username!")

def factorial_calculator():
    """Factorial Calculator"""
    st.title("Factorial Calculator")

    # Display logged-in user information
    st.write(f"Hello, {st.session_state.username}!")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # Factorial calculation function
    number = st.number_input("Enter a number:",
                             min_value=0,
                             max_value=900)

    if st.button("Calculate factorial"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")

def greeting_page():
    """Greeting page for invalid user"""
    st.title("Hello!")
    st.write(f"Hello {st.session_state.username}!")
    st.write("You do not have access to the factorial calculation function.")

    if st.button("Go back to login"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()        

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = False
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    # Navigate pages based on login status
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
