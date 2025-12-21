# import streamlit as st


# st.set_page_config(page_title="Dashboard", page_icon="📊")

# # --- If user not logged in ---
# if "token" not in st.session_state or st.session_state.token is None:
#     st.switch_page("pages/2_Login.py")
#     st.stop()

# # --- SIDEBAR ---
# with st.sidebar:
#     st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
#     st.subheader("👤 Profile")

#     st.write("Logged in user")

#     # 🐄 Breed Prediction (ONLY this on Dashboard)
#     # col1, col2, col3 = st.columns([1, 1, 1])

#     # with col1:
#     if st.button("🔍 Predict Breed"):
#           try:
#             st.switch_page("pages/6_Breed_Prediction.py")
#           except Exception as e:
#             st.error(f"Navigation error: {e}")

#     st.write("---")

#     # Logout
#     if st.button("🚪 Logout"):
#         st.session_state.clear()
#         st.switch_page("pages/2_Login.py")

# # --- MAIN PAGE ---
# st.title("📊 Dashboard")
# st.write("Welcome to Pashudhan AI!")

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

# import streamlit as st

# st.set_page_config(
#     page_title="Dashboard | Pashudhan AI",
#     page_icon="🐄",
#     layout="wide"
# )

# # 🔒 Protect page
# if "token" not in st.session_state or not st.session_state.token:
#     st.warning("Please login first")
#     st.switch_page("pages/2_Login.py")

# # ------------------ STYLES ------------------
# st.markdown("""
# <style>
# .dashboard-container {
#     background: linear-gradient(135deg, #00b09b, #96c93d);
#     padding: 3rem;
#     border-radius: 25px;
#     color: white;
#     text-align: center;
#     box-shadow: 0 8px 25px rgba(0,0,0,0.2);
#     animation: fadeIn 1.2s ease-in-out;
# }

# @keyframes fadeIn {
#     from {opacity: 0; transform: translateY(30px);}
#     to {opacity: 1; transform: translateY(0);}
# }

# .card {
#     background: white;
#     border-radius: 20px;
#     padding: 2rem;
#     text-align: center;
#     box-shadow: 0 6px 18px rgba(0,0,0,0.12);
#     transition: transform 0.3s ease;
# }

# .card:hover {
#     transform: scale(1.05);
# }

# .predict-btn button {
#     background: linear-gradient(90deg, #ff9800, #ff5722);
#     color: white;
#     font-size: 20px;
#     padding: 0.8rem 2.5rem;
#     border-radius: 15px;
#     border: none;
#     font-weight: 700;
# }

# .predict-btn button:hover {
#     background: linear-gradient(90deg, #fb8c00, #f4511e);
# }
# </style>
# """, unsafe_allow_html=True)

# # ------------------ HEADER ------------------
# st.markdown("""
# <div class="dashboard-container">
#     <h1>🐄 Welcome to Pashudhan AI</h1>
#     <p style="font-size:20px;">
#         AI-powered cattle breed identification system
#     </p>
# </div>
# """, unsafe_allow_html=True)

# st.write("")
# st.write("")

# # ------------------ MAIN ACTION ------------------
# col1, col2, col3 = st.columns([1,2,1])

# with col2:
#     st.markdown("""
#     <div class="card">
#         <h2>🔍 Predict Cattle Breed</h2>
#         <p>
#             Upload an image of cattle and let our AI model identify the breed
#             instantly with high accuracy.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.write("")

#     if st.button("🚀 Start Prediction", key="predict_btn"):
#         st.switch_page("pages/6_Breed_Prediction.py")

# # ------------------ INFO CARDS ------------------
# st.write("")
# st.write("")

# c1, c2, c3 = st.columns(3)

# with c1:
#     st.markdown("""
#     <div class="card">
#         <h3>⚡ Fast</h3>
#         <p>Instant predictions using optimized deep learning models.</p>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown("""
#     <div class="card">
#         <h3>🎯 Accurate</h3>
#         <p>Trained on real cattle images for reliable results.</p>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown("""
#     <div class="card">
#         <h3>🌱 Farmer Friendly</h3>
#         <p>Designed for easy use by farmers and researchers.</p>
#     </div>
#     """, unsafe_allow_html=True)


import streamlit as st

st.set_page_config(
    page_title="Dashboard | Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)

# 🔒 Protect page
if "token" not in st.session_state or not st.session_state.token:
    st.warning("Please login first")
    st.switch_page("pages/2_Login.py")

# ------------------ GLOBAL THEME FIX ------------------
st.markdown("""
<style>

/* Whole page background */
.stApp {
    background-color: #f4f6f8;
}

/* Remove default Streamlit padding */
.block-container {
    padding-top: 2rem;
}

/* HEADER */
.dashboard-header {
    background: linear-gradient(135deg, #00b09b, #96c93d);
    padding: 3rem;
    border-radius: 22px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* CARD */
.card {
    background: #ffffff;
    color: #222222;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #ff9800, #ff5722);
    color: white;
    font-size: 20px;
    padding: 0.8rem 2.5rem;
    border-radius: 14px;
    border: none;
    font-weight: 700;
    width: 100%;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #fb8c00, #f4511e);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
<div class="dashboard-header">
    <h1>🐄 Welcome to Pashudhan AI</h1>
    <p style="font-size:20px; margin-top:10px;">
        AI-powered cattle breed identification system
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ------------------ MAIN ACTION ------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("""
    <div class="card">
        <h2>🔍 Predict Cattle Breed</h2>
        <p style="font-size:16px;">
            Upload a cattle image and let our AI model identify the breed
            instantly with high accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 Start Prediction"):
        st.switch_page("pages/6_Breed_Prediction.py")

# ------------------ INFO CARDS ------------------
st.write("")
st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h3>⚡ Fast</h3>
        <p>Instant predictions using optimized deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Accurate</h3>
        <p>Trained on real cattle images for reliable results.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h3>🌱 Farmer Friendly</h3>
        <p>Designed for easy use by farmers and researchers.</p>
    </div>
    """, unsafe_allow_html=True)

