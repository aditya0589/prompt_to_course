import streamlit as st
from db_utils import create_user, verify_user, get_user

def login_ui():
    if st.session_state.get("logged_in"):
        st.sidebar.success(f"Welcome, {st.session_state.username}!")
        return True

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if verify_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("✅ Logged in successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

    with tab2:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            if get_user(new_user):
                st.warning("User already exists.")
            else:
                create_user(new_user, new_pass)
                st.success(" Registered successfully! Now login.")
                st.balloons()

    return False
