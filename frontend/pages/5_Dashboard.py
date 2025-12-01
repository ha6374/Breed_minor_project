# import streamlit as st
# from streamlit_extras.switch_page_button import switch_page


# if "token" not in st.session_state:
#     st.switch_page("pages/2_Login.py")

# st.set_page_config(page_title="Dashboard", page_icon="📊")

# # Sidebar
# with st.sidebar:
#     st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
#     st.subheader("👤 Profile")

#     st.write("Logged in user")

#     if st.button("🐄 Breed Prediction"):
#         st.switch_page("pages/6_Prediction.py")

#     st.write("---")
#     if st.button("🚪 Logout"):
#         st.session_state.clear()
#         st.switch_page("pages/2_Login.py")

# st.title("📊 Dashboard")
# st.write("Welcome to Pashudhan AI!")

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Dashboard", page_icon="📊")

# --- If user not logged in ---
if "token" not in st.session_state or st.session_state.token is None:
    switch_page("Login")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
    st.subheader("👤 Profile")

    st.write("Logged in user")

    # 🐄 Breed Prediction (ONLY this on Dashboard)
    if st.button("🐄 Breed Prediction"):
        switch_page("Prediction")

    st.write("---")

    # Logout
    if st.button("🚪 Logout"):
        st.session_state.clear()
        switch_page("Login")

# --- MAIN PAGE ---
st.title("📊 Dashboard")
st.write("Welcome to Pashudhan AI!")
