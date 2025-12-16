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

# import streamlit as st
# from utils.api_helper import reset_password_api

# st.set_page_config(page_title="Reset Password", layout="centered")

# st.markdown("""
# <style>
# .reset-card {
#     background: white;
#     padding: 35px;
#     border-radius: 16px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='reset-card'>", unsafe_allow_html=True)
# st.subheader("Reset Password")

# token = st.query_params.get("token", "")
# new_password = st.text_input("New Password", type="password")
# confirm_password = st.text_input("Confirm New Password", type="password")

# if st.button("Reset Password", use_container_width=True):
#     if new_password != confirm_password:
#         st.error("Passwords do not match")
#     elif not token:
#         st.error("Invalid or missing reset token")
#     else:
#         success, response = reset_password_api(
#             token,
#             {"password": new_password}
#         )

#         if success:
#             st.success("Password reset successfully")
#             st.switch_page("pages/2_Login.py")
#         else:
#             st.error(response)

# st.markdown("</div>", unsafe_allow_html=True)
