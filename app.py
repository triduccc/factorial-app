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
            st.error("File user.txt không tồn tại!")
            return []
    except Exception as e:
        st.error(f"Lỗi khi đọc file user.txt: {e}")
        return []

def login_page():
    """Login Page"""
    st.title("Login")

    username = st.text_input("Nhập tên người dùng:")

    if st.button("Đăng nhập"):
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
        st.warning("Vui lòng nhập tên người dùng!")

def factorial_calculator():
    """Trang tính giai thừa"""
    st.title("Factorial Calculator")

    # Hiển thị thông tin user đã đăng nhập
    st.write(f"Xin chào, {st.session_state.username}!")

    # Nút đăng xuất
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # Chức năng tính giai thừa
    number = st.number_input("Nhập vào một số:",
                             min_value=0,
                             max_value=900)

    if st.button("Tính giai thừa"):
        result = fact(number)
        st.write(f"Giai thừa của {number} là {result}")

def greeting_page():
    """Trang chào hỏi cho user không hợp lệ"""
    st.title("Xin chào!")
    st.write(f"Xin chào {st.session_state.username}!")
    st.write("Bạn không có quyền truy cập vào chức năng tính giai thừa.")

    if st.button("Quay lại đăng nhập"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()        

def main():
    st.title (" Factorial Calculator ")
    number = st.number_input (" Enter a number :",
                                min_value = 0,
                                max_value = 900)
    
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()    
