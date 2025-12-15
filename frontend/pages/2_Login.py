# import streamlit as st
# from utils.api_helper import login


# st.set_page_config(page_title="Login", page_icon="🔐")

# st.title("🔐 Login")

# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     response = login(email, password)

#     # if response is None:
#     #     st.error("❌ Server not responding. Please try again later.")

#     if response.status_code == 200:
#         st.session_state.token = response.json().get("token")
#         st.success("Login Successful!")
#         st.switch_page("pages/5_Dashboard.py")
#     else:
#         st.error("Invalid credentials")

# if st.button("Forgot Password?"):
#     st.switch_page("pages/4_Forgot_Password.py")

# st.write("Don't have an account?")
# if st.button("Create Account"):
#     st.switch_page("pages/3_Signup.py")
import streamlit as st
from utils.api_helper import login

st.set_page_config(page_title="Login", page_icon="🔐")

if "token" not in st.session_state:
    st.session_state.token = None

st.title("🔐 Login")

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    response = login(email, password)

    if response:
        st.write("STATUS:", response.status_code)
        st.write("BODY:", response.json())


    if response and response.status_code == 200:
        token = response.json().get("access_token")  # ✅ VERY IMPORTANT

        if token:
            st.session_state.token = token
            st.success("✅ Login Successful")
            st.switch_page("pages/5_Dashboard.py")
        else:
            st.error("❌ access_token not received")
    else:
        st.error("❌ Invalid credentials")

st.write("Don't have an account?")
if st.button("Create Account"):
    st.switch_page("pages/3_Signup.py")
