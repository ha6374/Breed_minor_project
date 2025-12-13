import streamlit as st

st.set_page_config(
    page_title="Welcome | Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)

# -----------------------------
# SESSION INITIALIZATION (KEY!)
# -----------------------------
if "token" not in st.session_state:
    st.session_state.token = None

if "seen_welcome" not in st.session_state:
    st.session_state.seen_welcome = False

# -----------------------------
# WELCOME / SPLASH SCREEN
# -----------------------------
if not st.session_state.seen_welcome:
    st.markdown("""
        <div style="text-align:center; margin-top:80px;">
            <img src="https://i.imgur.com/9B1xU6X.gif" width="280">
            <h1 style="color:#4a4a4a; font-size:42px;">🐄 Pashudhan AI</h1>
            <p style="font-size:22px;">Smart Cattle Breed Prediction System</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 Get Started"):
            st.session_state.seen_welcome = True
            st.switch_page("pages/2_Login.py")
            st.stop()

    st.stop()

# -----------------------------
# FALLBACK REDIRECT
# -----------------------------
st.switch_page("pages/2_Login.py")
st.stop()
