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
        st.switch_page("pages/2_Login.py")
    else:
        st.error("Signup failed! Try again.")

# import streamlit as st
# from utils.api_helper import signup_api

# st.set_page_config(page_title="Signup", layout="centered")

# st.markdown("""
# <style>
# .signup-card {
#     background: white;
#     padding: 35px;
#     border-radius: 16px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='signup-card'>", unsafe_allow_html=True)
# st.subheader("Create your account")

# email = st.text_input("Email")
# password = st.text_input("Password", type="password")
# confirm_password = st.text_input("Confirm Password", type="password")

# if st.button("Create Account", use_container_width=True):
#     if password != confirm_password:
#         st.error("Passwords do not match")
#     else:
#         success, response = signup_api({
#             "email": email,
#             "password": password
#         })

#         if success:
#             st.success("Account created successfully")
#             st.switch_page("pages/2_Login.py")
#         else:
#             st.error(response)

# st.write("")
# st.button("Back", use_container_width=True,
#           on_click=lambda: st.switch_page("pages/1_Welcome.py"))

# st.markdown("</div>", unsafe_allow_html=True)
