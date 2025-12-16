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
from utils.api_helper import login_api

st.set_page_config(page_title="Login", layout="centered")

st.markdown("""
<style>
.login-card {
    background: white;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='login-card'>", unsafe_allow_html=True)
st.subheader("Login to your account")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):
    success, response = login_api({
        "email": email,
        "password": password
    })

    if success:
        st.session_state["token"] = response.get("access_token")
        st.success("Login successful")
        st.switch_page("pages/5_Dashboard.py")
    else:
        st.error(response)

st.write("")
col1, col2 = st.columns(2)

with col1:
    st.button("Forgot Password?", use_container_width=True,
              on_click=lambda: st.switch_page("pages/4_Forgot_Password.py"))

with col2:
    st.button("Back", use_container_width=True,
              on_click=lambda: st.switch_page("pages/1_Welcome.py"))

st.markdown("</div>", unsafe_allow_html=True)
