import streamlit as st

st.set_page_config(page_title="Forgot Password", page_icon="❓")

st.title("❓ Reset Password")

email = st.text_input("Enter your registered email")

if st.button("Send Reset Link"):
    st.info("Backend reset system pending…")
