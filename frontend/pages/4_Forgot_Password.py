import streamlit as st

st.set_page_config(page_title="Forgot Password", page_icon="❓")

st.title("❓ Reset Password")

email = st.text_input("Enter your registered email")

if st.button("Send Reset Link"):
    st.info("Backend reset system pending…")

# import streamlit as st
# from utils.api_helper import forgot_password_api

# st.set_page_config(page_title="Forgot Password", layout="centered")

# st.markdown("""
# <style>
# .forgot-card {
#     background: white;
#     padding: 35px;
#     border-radius: 16px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='forgot-card'>", unsafe_allow_html=True)
# st.subheader("Forgot Password")

# st.write("Enter your registered email to receive a password reset link.")

# email = st.text_input("Email")

if st.button("Send Reset Link", use_container_width=True):
    success, response = forgot_password_api({"email": email})

    if success:
        st.success("Password reset link sent to your email")
    else:
        st.error(response)

st.write("")
st.button("Back to Login", use_container_width=True,
          on_click=lambda: st.switch_page("pages/2_Login.py"))

st.markdown("</div>", unsafe_allow_html=True)
