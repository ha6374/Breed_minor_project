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
            st.switch_page("pages/6_Breed_Prediction")
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
