import streamlit as st
from utils.api_helper import login


st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    response = login(email, password)

    if response.status_code == 200:
        st.session_state.token = response.json().get("token")
        st.success("Login Successful!")
        st.switch_page("5_Dashboard")
    else:
        st.error("Invalid credentials")

if st.button("Forgot Password?"):
    st.switch_page("4_Forgot_Password")

st.write("Don't have an account?")
if st.button("Create Account"):
    st.switch_page("3_Signup")
