import streamlit as st
from utils.api_helper import signup

st.set_page_config(page_title="Signup", page_icon="📝")

st.title("📝 Create Account")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Signup"):
    response = signup(username, email, password)

    if response.status_code == 200 or response.status_code == 201:
        st.success("Account created successfully!")
        st.switch_page("pages/2_Login")
    else:
        st.error("Signup failed! Try again.")
