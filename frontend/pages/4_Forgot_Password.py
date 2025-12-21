


# import streamlit as st
# from utils.api_helper import forgot_password

# st.set_page_config(page_title="Forgot Password", page_icon="❓", layout="centered")

# st.markdown("""
# <style>
# .forgot-card {
#     background: white;
#     padding: 35px;
#     border-radius: 16px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
#     max-width: 450px;
#     margin: auto;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='forgot-card'>", unsafe_allow_html=True)

# st.subheader("🔐 Forgot Password")
# st.write("Enter your registered email to receive a password reset link.")

# email = st.text_input("Email")

# if st.button("Send Reset Link", use_container_width=True):
#     if not email:
#         st.warning("⚠️ Please enter your email")
#     else:
#         success, message = forgot_password(email)
#         if success:
#             st.success(f"✅ {message}")
#         else:
#             st.error(f"❌ {message}")

# st.write("")
# st.button("Back to Login", use_container_width=True,
#           on_click=lambda: st.switch_page("pages/2_Login.py"))

# st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
from utils.api_helper import forgot_password
import requests

BACKEND_URL = "https://breed-minor-project.onrender.com/api/v1"

st.set_page_config(page_title="Reset Password", page_icon="🔐", layout="centered")

# -------------------------
# GET TOKEN FROM URL
# -------------------------
query_params = st.query_params
token = query_params.get("token")

st.markdown("""
<style>
.card {
    background: white;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.1);
    max-width: 450px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# =====================================================
# 🔁 RESET PASSWORD MODE (TOKEN EXISTS)
# =====================================================
if token:
    st.subheader("🔐 Reset Your Password")

    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Reset Password", use_container_width=True):
        if not new_password or not confirm_password:
            st.warning("⚠️ Please fill all fields")
        elif new_password != confirm_password:
            st.error("❌ Passwords do not match")
        else:
            res = requests.post(
                f"{BACKEND_URL}/auth/reset-password",
                json={
                    "token": token,
                    "password": new_password
                },
                timeout=15
            )

            if res.status_code == 200:
                st.success("✅ Password reset successful! Please login.")
                st.switch_page("pages/2_Login.py")
            else:
                st.error("❌ Invalid or expired token")

# =====================================================
# 📩 FORGOT PASSWORD MODE (NO TOKEN)
# =====================================================
else:
    st.subheader("📩 Forgot Password")
    st.write("Enter your registered email to receive a reset link.")

    email = st.text_input("Email")

    if st.button("Send Reset Link", use_container_width=True):
        if not email:
            st.warning("⚠️ Please enter email")
        else:
            success, message = forgot_password(email)
            if success:
                st.success("✅ If email exists, reset link sent.")
            else:
                st.error(f"❌ {message}")

    st.write("")
    st.button("⬅ Back to Login", use_container_width=True,
              on_click=lambda: st.switch_page("pages/2_Login.py"))

st.markdown("</div>", unsafe_allow_html=True)

