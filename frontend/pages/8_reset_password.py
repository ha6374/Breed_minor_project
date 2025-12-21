# import streamlit as st
# import requests

# # BACKEND_URL = "http://127.0.0.1:8000/api/v1/auth"
# BACKEND_URL = "https://breed-minor-project.onrender.com/api/v1/auth"

# st.set_page_config(page_title="Reset Password", layout="wide")

# st.title("🔑 Reset Your Password")

# token = st.query_params.get("token")

# if not token:
#     st.error("Invalid or missing token.")
#     st.stop()

# new_password = st.text_input("Enter New Password", type="password")

# if st.button("Reset Password"):
#     response = requests.post(
#         f"{BACKEND_URL}/reset-password",
#         json={"token": token, "new_password": new_password}
#     )

#     if response.status_code == 200:
#         st.success("Password reset successful! Please login again.")
#     else:
#         st.error("Failed to reset password. Token may be expired.")

# # import streamlit as st
# # from utils.api_helper import reset_password_api

# # st.set_page_config(page_title="Reset Password", layout="centered")

# # st.markdown("""
# # <style>
# # .reset-card {
# #     background: white;
# #     padding: 35px;
# #     border-radius: 16px;
# #     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # st.markdown("<div class='reset-card'>", unsafe_allow_html=True)
# # st.subheader("Reset Password")

# # token = st.query_params.get("token", "")
# # new_password = st.text_input("New Password", type="password")
# # confirm_password = st.text_input("Confirm New Password", type="password")

# # if st.button("Reset Password", use_container_width=True):
# #     if new_password != confirm_password:
# #         st.error("Passwords do not match")
# #     elif not token:
# #         st.error("Invalid or missing reset token")
# #     else:
# #         success, response = reset_password_api(
# #             token,
# #             {"password": new_password}
# #         )

# #         if success:
# #             st.success("Password reset successfully")
# #             st.switch_page("pages/2_Login.py")
# #         else:
# #             st.error(response)


# # st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st
# from utils.api_helper import reset_password

# st.set_page_config(
#     page_title="Reset Password",
#     page_icon="🔑",
#     layout="centered"
# )

# st.markdown("""
# <style>
# .reset-card {
#     background: white;
#     padding: 35px;
#     border-radius: 16px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
#     max-width: 450px;
#     margin: auto;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='reset-card'>", unsafe_allow_html=True)

# st.subheader("🔑 Reset Password")

# # 🔹 Read token from URL
# params = st.experimental_get_query_params()
# token = params.get("token", [None])[0]

# if not token:
#     st.error("❌ Invalid or missing reset token.")
#     st.stop()

# new_password = st.text_input("New Password", type="password")
# confirm_password = st.text_input("Confirm Password", type="password")

# if st.button("Reset Password", use_container_width=True):
#     if not new_password or not confirm_password:
#         st.warning("⚠️ Please fill all fields")
#     elif new_password != confirm_password:
#         st.error("❌ Passwords do not match")
#     else:
#         success, message = reset_password(token, new_password)
#         if success:
#             st.success("✅ Password reset successfully!")
#             st.button(
#                 "Go to Login",
#                 use_container_width=True,
#                 on_click=lambda: st.switch_page("pages/2_Login.py")
#             )
#         else:
#             st.error(f"❌ {message}")

# st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
import requests

BACKEND_URL = "https://breed-minor-project.onrender.com/api/v1"

st.set_page_config(
    page_title="Reset Password",
    page_icon="🔑",
    layout="centered"
)

# -----------------------------
# Get token from URL
# -----------------------------
query_params = st.query_params
token = query_params.get("token")

st.markdown("""
<style>
.reset-card {
    background: white;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.1);
    max-width: 450px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='reset-card'>", unsafe_allow_html=True)

st.subheader("🔑 Reset Your Password")

if not token:
    st.error("❌ Invalid or missing reset token.")
    st.stop()

new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Reset Password", use_container_width=True):
    if not new_password or not confirm_password:
        st.warning("⚠️ Please fill all fields")
    elif new_password != confirm_password:
        st.error("❌ Passwords do not match")
    else:
        try:
            res = requests.post(
                f"{BACKEND_URL}/auth/reset-password",
                json={
                    "token": token,
                    "new_password": new_password
                },
                timeout=15
            )

            if res.status_code == 200:
                st.success("✅ Password reset successful!")
                st.button(
                    "Go to Login",
                    on_click=lambda: st.switch_page("pages/2_Login.py"),
                    use_container_width=True
                )
            else:
                st.error(res.json().get("detail", "❌ Reset failed"))

        except Exception as e:
            st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)

