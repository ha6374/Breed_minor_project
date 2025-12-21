import streamlit as st
import os
from utils.api_helper import login, signup, get_user_profile, update_user_profile, forgot_password




st.set_page_config(
    page_title="Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)




# 🌿 --- SESSION INIT ---
if "token" not in st.session_state:
    st.session_state.token = None
if "page" not in st.session_state:
    st.session_state.page = "login"
if "seen_splash" not in st.session_state:
    st.session_state.seen_splash = False
if "profile_expanded" not in st.session_state:
    st.session_state.profile_expanded = False

# 🌿 --- GLOBAL STYLES ---
st.markdown("""
    <style>
        .block-container {padding: 2rem 3rem;}
        .title-text {
            background: linear-gradient(90deg, #00b09b, #96c93d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 3rem;
            text-align: center;
        }
        div.stButton > button {
            background-color: #00b09b;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            border: none;
            width: 100%;
            padding: 0.75rem;
            transition: 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #01947c;
            transform: scale(1.03);
        }
        /* Sidebar visible only after login */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 100%);
            color: white;
            padding-top: 2rem;
        }
        .profile-header {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0.8rem 1rem;
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            margin: 0 1rem 1rem 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .profile-header:hover {background: rgba(255,255,255,0.12);}
        .profile-pic {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid white;
        }
        .username {
            font-weight: 600;
            color: white;
            font-size: 1rem;
        }
        .profile-card {
            background-color: #fff;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
            margin: 0 1rem;
        }
        .profile-pic-lg {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 0.5rem;
            border: 3px solid #4caf50;
        }
        .edit-btn {
            background-color: #0095f6;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        .edit-btn:hover {background-color: #0077c8;}
        .small-link { color: #0077c8; cursor: pointer; text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Welcome / Splash Screen
# -------------------------
if not st.session_state.seen_splash:
    # show splash UI
    st.markdown('<div style="text-align:center; margin-top:3rem;">', unsafe_allow_html=True)
    splash_path = os.path.join(os.path.dirname(__file__), "assets", "splash.gif")
    if os.path.exists(splash_path):
        st.image(splash_path, width=350)
    else:
        # fallback: static logo if gif not present
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path, width=300)
        else:
            st.markdown("🐄", unsafe_allow_html=True)

    st.markdown('<h1 style="margin-top:1rem;">Welcome to <b>Pashudhan AI</b></h1>', unsafe_allow_html=True)
    st.markdown("<p>Smart livestock breed identification — powered by AI.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Get Started"):
            st.session_state.seen_splash = True
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# -------------------------
# SIDEBAR (after login only)
# -------------------------
if st.session_state.token:
    with st.sidebar:
        user_data = get_user_profile(st.session_state.token) or {}
        profile_image_url = user_data.get("profile_image") if user_data and user_data.get("profile_image") else "https://cdn-icons-png.flaticon.com/512/1077/1077012.png"

        clicked = st.button("👤 View Profile", key="profile_btn")
        st.markdown(
            f'<div class="profile-header"><img src="{profile_image_url}" class="profile-pic"><span class="username">{user_data.get("username", "User")}</span></div>',
            unsafe_allow_html=True
       )

        # navigation
        st.markdown("---")
        if st.button("🏠 Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
        # if st.button("🔍 Predict Breed"):
        #     # if your prediction page is a separate streamlit page, use switch_page
        #     try:
        #         switch_page("6_Breed_Prediction")
        #     except Exception:
        #         # fallback: set page variable so your router can handle
        #         st.session_state.page = "6_Breed_Prediction"
        #         st.rerun()
        if st.button("👤 Profile"):
            try:
                st.switch_page("7_Profile")
            except Exception:
                st.session_state.page = "profile"
                st.rerun()

        st.markdown("---")
        if st.button("🚪 Logout"):
            st.session_state.token = None
            st.session_state.page = "login"
            st.rerun()

        # --- Expanded profile section ---
        if st.session_state.profile_expanded:
            st.markdown('<div class="profile-card">', unsafe_allow_html=True)

            # Profile Details
            st.image(profile_image_url, use_column_width=False, width=100)
            st.markdown(f"### {user_data.get('username', 'User')}")
            st.markdown(f"📧 {user_data.get('email', 'N/A')}")
            st.markdown(f"🕒 Joined: {user_data.get('created_at', 'N/A')}")

            # Edit form
            with st.expander("✏️ Edit Profile"):
                with st.form("edit_form_sidebar"):
                    new_username = st.text_input("Username", user_data.get("username", ""))
                    new_email = st.text_input("Email", user_data.get("email", ""))
                    save = st.form_submit_button("💾 Save Changes")

                    if save:
                        res = update_user_profile(st.session_state.token, {"username": new_username, "email": new_email})
                        if res and getattr(res, "status_code", None) in (200, 201):
                            st.success("✅ Profile updated successfully!")
                        else:
                            st.error("❌ Update failed. Try again later.")

            st.divider()
            st.markdown('</div>', unsafe_allow_html=True)

        if clicked:
            st.session_state.profile_expanded = not st.session_state.profile_expanded

# -------------------------
# LOGIN / SIGNUP PAGE
# -------------------------
if st.session_state.page == "login" and not st.session_state.token:
    # 🔒 Hide sidebar (before login)
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none;}
            .block-container {padding-top: 2rem;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title-text">🐄 Pashudhan AI</div>', unsafe_allow_html=True)
    st.markdown("### Your Smart Livestock Breed Identifier")

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Signup"])

    # --- Login ---
    with tab1:
        st.subheader("Welcome Back 👋")
        email = st.text_input("📧 Email", key="login_email")
        password = st.text_input("🔑 Password", type="password", key="login_pass")
        colL, colR = st.columns([3,1])
        with colL:
            if st.button("Login"):
                if email and password:
                    res = login(email, password)
                    if res and getattr(res, "status_code", None) == 200:
                        token = res.json().get("access_token")
                        if token:
                            st.session_state.token = token
                            st.session_state.page = "dashboard"
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Login failed.")
                    else:
                        st.error("Invalid credentials or server issue.")
        with colR:
            if st.button("Forgot?"):
                st.session_state.show_forgot = not st.session_state.get("show_forgot", False)

        if st.session_state.get("show_forgot", False):
            with st.expander("Forgot Password"):
                forgot_email = st.text_input("Enter your registered email", key="forgot_email")
                if st.button("Send reset link"):
                    if forgot_email:
                        res = forgot_password(forgot_email)
                        if res and getattr(res, "status_code", None) in (200, 201):
                            st.success("✅ If the email exists, a reset link was sent.")
                        else:
                            st.error("❌ Could not send reset link. Try again later.")

    # --- Signup ---
    with tab2:
        st.subheader("Create Account ✨")
        username = st.text_input("👤 Username", key="signup_user")
        email = st.text_input("📧 Email", key="signup_email")
        password = st.text_input("🔑 Password", type="password", key="signup_pass")

        if st.button("Signup"):
            if username and email and password:
                res = signup(username, email, password)
                if res and getattr(res, "status_code", None) in (200, 201, 204):
                    st.success("✅ Signup successful! Please login now.")
                else:
                    st.error("Signup failed. Try again.")

# -------------------------
# DASHBOARD PAGE
# -------------------------
elif st.session_state.token:
    # 🐄 Center logo at top
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
    st.markdown("""
    <style>
        .dashboard-banner {
            background: linear-gradient(135deg, #00b09b, #96c93d);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            color: white;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            animation: fadeIn 1.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    <div class="dashboard-banner">
        <h2>Welcome back to <b>Pashudhan AI</b> 🐄</h2>
        <p>Analyze and predict cattle breeds using advanced deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title-text">🐄 Pashudhan AI Dashboard</div>', unsafe_allow_html=True)
    st.markdown("### Explore AI-powered livestock tools")

    # col1, col2, col3 = st.columns([1,1,1])
    # with col1:
    # if st.button("🔍 Predict Breed"):
    #         try:
    #           # Use page filename without .py
    #           switch_page("6_Breed_Prediction")
    #         except Exception:
    #         # fallback in case switch_page fails
    #           st.session_state.page = "6_Breed_Prediction"
    #           st.rerun()
    if st.button("🔍 Predict Breed", key="predict_dashboard"):
        st.switch_page("pages/6_Breed_Prediction.py")
        
        

    
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Powered by AI | Developed with ❤️ by Beed Brigade</p>",
        unsafe_allow_html=True,
    )
# # # import streamlit as st
# # # import time

# # # st.set_page_config(
# # #     page_title="Welcome | Pashudhan AI",
# # #     page_icon="🐄",
# # #     layout="wide"
# # # )

# # # st.markdown("""
# # #     <div style="text-align:center; margin-top:80px;">
# # #         <h1 style="font-size:50px;">🐄 Pashudhan AI</h1>
# # #         <p style="font-size:22px;">Smart Cattle Breed Prediction System</p>
# # #     </div>
# # # """, unsafe_allow_html=True)

# # # time.sleep(2)

# # # st.switch_page("pages/1_Welcome.py")

# import streamlit as st


# st.set_page_config(
# page_title="Pashudhan AI",
# page_icon="🐄",
# layout="centered"
# )


# CUSTOM_CSS = """
# <style>
# body {
# background: linear-gradient(135deg, #f5f7fa, #e4efe9);
# }


# .main-title {
# font-size: 42px;
# font-weight: 800;
# text-align: center;
# color: #1f2937;
# }


# .subtitle {
# text-align: center;
# font-size: 18px;
# color: #4b5563;
# margin-bottom: 30px;
# }


# .card {
# background: white;
# padding: 30px;
# border-radius: 18px;
# box-shadow: 0 10px 25px rgba(0,0,0,0.08);
# margin-bottom: 25px;
# }


# .primary-btn button {
# background: linear-gradient(90deg, #16a34a, #22c55e) !important;
# color: white !important;
# font-size: 18px !important;
# padding: 0.6em 1.2em !important;
# border-radius: 12px !important;
# }
# </style>
# """


# st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# # import streamlit as st

# # # -------------------------------------------------
# # # App configuration
# # # -------------------------------------------------
# # st.set_page_config(
# #     page_title="Pashudhan AI",
# #     page_icon="🐄",
# #     layout="centered"
# # )

# # # -------------------------------------------------
# # # Entry point / Router
# # # -------------------------------------------------
# # # Streamlit app hamesha main.py se start hoti hai
# # # Isliye yahan se Welcome page par redirect kar rahe hain
# # # Taaki clean and professional flow mile
# # # -------------------------------------------------

# # st.switch_page("pages/1_Welcome.py")
