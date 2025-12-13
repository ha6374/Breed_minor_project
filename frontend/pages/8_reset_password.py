import streamlit as st
import requests

# BACKEND_URL = "http://127.0.0.1:8000/api/v1/auth"
BACKEND_URL = "https://breed-minor-project.onrender.com/api/v1/auth"

st.set_page_config(page_title="Reset Password", layout="wide")

st.title("🔑 Reset Your Password")

token = st.query_params.get("token")

if not token:
    st.error("Invalid or missing token.")
    st.stop()

new_password = st.text_input("Enter New Password", type="password")

if st.button("Reset Password"):
    response = requests.post(
        f"{BACKEND_URL}/reset-password",
        json={"token": token, "new_password": new_password}
    )

    if response.status_code == 200:
        st.success("Password reset successful! Please login again.")
    else:
        st.error("Failed to reset password. Token may be expired.")
