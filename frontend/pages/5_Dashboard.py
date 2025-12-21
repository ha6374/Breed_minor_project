import streamlit as st


st.set_page_config(page_title="Dashboard", page_icon="📊")

# --- If user not logged in ---
if "token" not in st.session_state or st.session_state.token is None:
    st.switch_page("pages/2_Login.py")
    st.stop()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
    st.subheader("👤 Profile")

    st.write("Logged in user")

    # 🐄 Breed Prediction (ONLY this on Dashboard)
    # col1, col2, col3 = st.columns([1, 1, 1])

    # with col1:
    if st.button("🔍 Predict Breed"):
          try:
            st.switch_page("pages/6_Breed_Prediction.py")
          except Exception as e:
            st.error(f"Navigation error: {e}")

    st.write("---")

    # Logout
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/2_Login.py")

# --- MAIN PAGE ---
st.title("📊 Dashboard")
st.write("Welcome to Pashudhan AI!")

# # import streamlit as st

# # st.set_page_config(page_title="Breed Prediction", page_icon="🔍")

# # if "token" not in st.session_state:
# #     st.switch_page("pages/2_Login.py")

# # st.title("🔍 Breed Prediction")

# # st.info("Model integration yaha aayega")

# # if st.button("⬅ Back to Dashboard"):
# #     st.switch_page("pages/5_Dashboard.py")


# import streamlit as st

# st.set_page_config(page_title="Dashboard", layout="wide")

# if "token" not in st.session_state:
#     st.switch_page("pages/2_Login.py")

# st.markdown("""
# <style>
# .card {
#     background: white;
#     padding: 30px;
#     border-radius: 18px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.08);
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("📊 Dashboard")
# st.write("Welcome to the Breed Recognition System")

# st.success("✅ You are logged in")

# if st.button("🚪 Logout", use_container_width=True):
#     st.session_state.clear()
#     st.switch_page("pages/1_Welcome.py")

# st.markdown("---")

# c1, c2 = st.columns(2)

# with c1:
#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.subheader("Breed Prediction")
#     st.write("Upload cattle or buffalo image to predict its breed.")
#     st.button("Start Prediction", use_container_width=True,
#               on_click=lambda: st.switch_page("pages/6_Breed_Prediction.py"))
#     st.markdown("</div>", unsafe_allow_html=True)

# with c2:
#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.subheader("Profile")
#     st.write("View and manage your account information.")
#     st.button("Go to Profile", use_container_width=True,
#               on_click=lambda: st.switch_page("pages/7_Profile.py"))
#     st.markdown("</div>", unsafe_allow_html=True)

# st.write("")
# st.button("Logout", on_click=lambda: (
#     st.session_state.clear(),
#     st.switch_page("pages/1_Welcome.py")
# ))
