# # # # import streamlit as st
# # # # from utils import api_helper

# # # # st.set_page_config(
# # # #     page_title="PashuBreed AI",
# # # #     page_icon="🐄",
# # # #     layout="wide",
# # # #     initial_sidebar_state="expanded",
# # # # )

# # # # st.title("PashuBreed AI")

# # # # if "token" not in st.session_state:
# # # #     st.session_state["token"] = None

# # # # if st.session_state["token"] is None:
# # # #     st.subheader("Login or SignUp")
    
# # # #     login_tab, signup_tab = st.tabs(["Login", "SignUp"])

# # # #     with login_tab:
# # # #         email = st.text_input("Email")
# # # #         password = st.text_input("Password", type="password")
# # # #         if st.button("Login"):
# # # #             if email and password:
# # # #                 response = api_helper.login(email, password)
# # # #                 if response.status_code == 200:
# # # #                     st.success("Logged In as {}".format(email))
# # # #                     token = response.json()["access_token"]
# # # #                     st.session_state["token"] = token
# # # #                     st.rerun()

# # # #                 else:
# # # #                     st.warning("Incorrect Email/Password")
# # # #             else:
# # # #                 st.warning("Please enter email and password")

# # # #     with signup_tab:
# # # #         username = st.text_input("Username")
# # # #         email_signup = st.text_input("Email", key="email_signup")
# # # #         password_signup = st.text_input("Password", type="password", key="password_signup")
# # # #         if st.button("SignUp"):
# # # #             if username and email_signup and password_signup:
# # # #                 response = api_helper.signup(username, email_signup, password_signup)
# # # #                 if response.status_code == 200:
# # # #                     st.success("You have successfully created an account")
# # # #                     st.info("Go to Login tab to login")
# # # #                 else:
# # # #                     st.warning(response.json()["detail"])
# # # #             else:
# # # #                 st.warning("Please fill out all fields")
# # # # else:
# # # #     st.sidebar.success("You are logged in.")
# # # #     if st.sidebar.button("Logout"):
# # # #         st.session_state["token"] = None
# # # #         st.rerun()

    
# # # #     st.switch_page("pages/1_🐄_Breed_Prediction.py")



# # # import streamlit as st
# # # from utils.api_helper import login, signup, get_user_profile

# # # st.set_page_config(page_title="Pashudhan AI", layout="wide")

# # # # Initialize session variables
# # # if "token" not in st.session_state:
# # #     st.session_state.token = None
# # # if "page" not in st.session_state:
# # #     st.session_state.page = "login"

# # # # Sidebar (visible only after login)
# # # if st.session_state.token:
# # #     with st.sidebar:
# # #         st.image("assets/logo.png", use_container_width=True)
# # #         user_data = get_user_profile(st.session_state.token)
# # #         if user_data:
# # #             st.markdown(f"**👤 {user_data['username']}**")
# # #             st.caption(user_data["email"])
# # #         st.divider()
# # #         if st.button("Logout 🔒"):
# # #             st.session_state.token = None
# # #             st.session_state.page = "login"
# # #             st.rerun()

# # # # -------------------- LOGIN / SIGNUP PAGE --------------------
# # # if st.session_state.page == "login" and not st.session_state.token:
# # #     st.title("🐄 Welcome to Pashudhan AI")
# # #     st.markdown("### Login or Signup to continue")

# # #     tab1, tab2 = st.tabs(["🔐 Login", "📝 Signup"])

# # #     with tab1:
# # #         email = st.text_input("Email", key="login_email")
# # #         password = st.text_input("Password", type="password", key="login_pass")
# # #         if st.button("Login"):
# # #             if email and password:
# # #                 token = login(email, password)
# # #                 if token:
# # #                     st.session_state.token = token
# # #                     st.session_state.page = "dashboard"
# # #                     st.success("✅ Login successful!")
# # #                     st.rerun()
# # #                 else:
# # #                     st.error("❌ Invalid credentials or server issue.")
# # #             else:
# # #                 st.warning("Please fill all fields.")

# # #     with tab2:
# # #         username = st.text_input("Username", key="signup_user")
# # #         email = st.text_input("Email", key="signup_email")
# # #         password = st.text_input("Password", type="password", key="signup_pass")
# # #         if st.button("Signup"):
# # #             if username and email and password:
# # #                 ok = signup(username, email, password)
# # #                 if ok:
# # #                     st.success("✅ Signup successful! Please login now.")
# # #                 else:
# # #                     st.error("❌ Signup failed. Try again.")
# # #             else:
# # #                 st.warning("Please fill all fields.")

# # # # -------------------- DASHBOARD --------------------
# # # elif st.session_state.token:
# # #     st.title("🐄 Pashudhan AI Dashboard")
# # #     st.markdown("### Select an option from the sidebar")

# # #     # Buttons for navigation
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         if st.button("🔍 Predict Breed"):
# # #             st.switch_page("pages/1_🐄_Breed_Prediction.py")
# # #     with col2:
# # #         if st.button("👤 View Profile"):
# # #             st.switch_page("pages/2_👤_Profile.py")




# # import streamlit as st
# # from utils.api_helper import login, signup, get_user_profile

# # # 🌿 --- PAGE CONFIG ---
# # st.set_page_config(page_title="🐄 Pashudhan AI", layout="wide")

# # # 🌿 --- SESSION INITIALIZATION ---
# # if "token" not in st.session_state:
# #     st.session_state.token = None
# # if "page" not in st.session_state:
# #     st.session_state.page = "login"

# # # 🌿 --- GLOBAL STYLES ---
# # st.markdown("""
# #     <style>
# #         /* Remove Streamlit default padding */
# #         .block-container {
# #             padding-top: 2rem;
# #             padding-bottom: 2rem;
# #             padding-left: 2rem;
# #             padding-right: 2rem;
# #         }
# #         /* Title Gradient */
# #         .title-text {
# #             background: linear-gradient(90deg, #00b09b, #96c93d);
# #             -webkit-background-clip: text;
# #             -webkit-text-fill-color: transparent;
# #             font-weight: 800;
# #             font-size: 3rem;
# #             text-align: center;
# #         }
# #         /* Buttons */
# #         div.stButton > button {
# #             background-color: #00b09b;
# #             color: white;
# #             font-weight: 600;
# #             border-radius: 10px;
# #             border: none;
# #             width: 100%;
# #             padding: 0.75rem;
# #             transition: 0.3s ease;
# #         }
# #         div.stButton > button:hover {
# #             background-color: #01947c;
# #             color: white;
# #             transform: scale(1.02);
# #         }
# #         /* Tabs Styling */
# #         .stTabs [data-baseweb="tab-list"] button {
# #             background-color: #e8f5e9;
# #             color: #2e7d32;
# #             border-radius: 8px;
# #             margin: 3px;
# #             font-weight: 600;
# #         }
# #         .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
# #             background-color: #2e7d32;
# #             color: white;
# #         }
# #         /* Sidebar Design */
# #         section[data-testid="stSidebar"] {
# #             background-color: #f0fdf4;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # 🌿 --- SIDEBAR (after login) ---
# # # 🌿 --- SIDEBAR (after login) ---
# # if st.session_state.token:
# #     with st.sidebar:
# #         # --- Sidebar Custom Styles ---
# #         st.markdown("""
# #             <style>
# #                 /* Sidebar background */
# #                 section[data-testid="stSidebar"] {
# #                     background: linear-gradient(180deg, #e8f5e9 0%, #c8e6c9 100%);
# #                     color: #1b5e20;
# #                     padding-top: 2rem;
# #                 }

# #                 /* User card */
# #                 .user-card {
# #                     background-color: white;
# #                     border-radius: 12px;
# #                     padding: 1rem;
# #                     box-shadow: 0 2px 6px rgba(0,0,0,0.1);
# #                     text-align: center;
# #                     margin-bottom: 1rem;
# #                 }

# #                 /* Logo */
# #                 .sidebar-logo {
# #                     display: flex;
# #                     justify-content: center;
# #                     align-items: center;
# #                     margin-bottom: 1rem;
# #                 }

# #                 /* Buttons */
# #                 div[data-testid="stButton"] > button {
# #                     background-color: #2e7d32;
# #                     color: white;
# #                     font-weight: 600;
# #                     border-radius: 10px;
# #                     width: 100%;
# #                     border: none;
# #                     margin-top: 8px;
# #                     transition: 0.3s ease;
# #                 }
# #                 div[data-testid="stButton"] > button:hover {
# #                     background-color: #1b5e20;
# #                     transform: scale(1.02);
# #                 }
# #             </style>
# #         """, unsafe_allow_html=True)

# #         # --- Logo ---
# #         st.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
# #         st.image("assets/logo.png", width=160)
# #         st.markdown('</div>', unsafe_allow_html=True)

# #         # --- User info card ---
# #         user_data = get_user_profile(st.session_state.token)
# #         if user_data:
# #             st.markdown(f"""
# #                 <div class="user-card">
# #                     <h4>👤 {user_data['username']}</h4>
# #                     <p style="color:gray; font-size: 0.9rem;">{user_data['email']}</p>
# #                 </div>
# #             """, unsafe_allow_html=True)

# #         # --- Navigation Buttons ---
# #         st.markdown("### 🚀 Quick Access")
# #         if st.button("🏠 Dashboard"):
# #             st.session_state.page = "dashboard"
# #             st.rerun()
# #         if st.button("🔍 Predict Breed"):
# #             st.switch_page("pages/1_🐄_Breed_Prediction.py")
# #         if st.button("👤 Profile"):
# #             st.switch_page("pages/2_👤_Profile.py")

# #         st.divider()

# #         # --- Logout Button ---
# #         if st.button("🚪 Logout"):
# #             st.session_state.token = None
# #             st.session_state.page = "login"
# #             st.rerun()


# # # 🌿 --- LOGIN / SIGNUP PAGE ---
# # if st.session_state.page == "login" and not st.session_state.token:
# #     st.markdown('<div class="title-text">🐄 Pashudhan AI</div>', unsafe_allow_html=True)
# #     st.markdown("### Your Smart Livestock Breed Identifier")

# #     tab1, tab2 = st.tabs(["🔐 Login", "📝 Signup"])

# #     # --- LOGIN TAB ---
# #     with tab1:
# #         st.subheader("Welcome Back 👋")
# #         email = st.text_input("📧 Email", key="login_email")
# #         password = st.text_input("🔑 Password", type="password", key="login_pass")

# #         if st.button("Login"):
# #             if email and password:
# #                 token = login(email, password)
# #                 if token:
# #                     st.session_state.token = token
# #                     st.session_state.page = "dashboard"
# #                     st.success("✅ Login successful!")
# #                     st.rerun()
# #                 else:
# #                     st.error("❌ Invalid credentials or server issue.")
# #             else:
# #                 st.warning("⚠️ Please fill all fields.")

# #     # --- SIGNUP TAB ---
# #     with tab2:
# #         st.subheader("Create Account ✨")
# #         username = st.text_input("👤 Username", key="signup_user")
# #         email = st.text_input("📧 Email", key="signup_email")
# #         password = st.text_input("🔑 Password", type="password", key="signup_pass")

# #         if st.button("Signup"):
# #             if username and email and password:
# #                 ok = signup(username, email, password)
# #                 if ok:
# #                     st.success("✅ Signup successful! Please login now.")
# #                 else:
# #                     st.error("❌ Signup failed. Try again.")
# #             else:
# #                 st.warning("⚠️ Please fill all fields.")

# # # 🌿 --- DASHBOARD PAGE ---
# # elif st.session_state.token:
# #     st.markdown('<div class="title-text">🐄 Pashudhan AI Dashboard</div>', unsafe_allow_html=True)
# #     st.markdown("### Explore AI-powered livestock tools")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         if st.button("🔍 Predict Breed"):
# #             st.switch_page("pages/1_🐄_Breed_Prediction.py")
# #     with col2:
# #         if st.button("👤 View Profile"):
# #             st.switch_page("pages/2_👤_Profile.py")

# #     st.markdown("---")
# #     st.markdown(
# #         "<p style='text-align:center; color:gray;'>Powered by AI | Developed with ❤️ by Harsh Patel</p>",
# #         unsafe_allow_html=True,
# #     )



# import streamlit as st
# from utils.api_helper import login, signup, get_user_profile

# st.set_page_config(page_title="Pashudhan AI", layout="wide", initial_sidebar_state="expanded")

# # --- Session init
# if "token" not in st.session_state:
#     st.session_state.token = None
# if "page" not in st.session_state:
#     st.session_state.page = "login"

# # --- Shared CSS (professional look)
# st.markdown(
#     """
#     <style>
#     :root{--green:#2e7d32;--muted:#6b7280}
#     .block-container{padding:1.5rem 2rem;}
#     .hero {
#       background: linear-gradient(135deg,#0f766e 0%, #34d399 100%);
#       color: white;
#       padding: 2rem;
#       border-radius: 12px;
#       box-shadow: 0 8px 30px rgba(2,6,23,0.08);
#       margin-bottom:1.5rem;
#     }
#     .hero h1{font-size:2.2rem;margin:0 0 .25rem 0}
#     .card {background:white;border-radius:12px;padding:1.25rem;box-shadow:0 6px 18px rgba(2,6,23,0.06)}
#     section[data-testid="stSidebar"] { background: linear-gradient(180deg,#ecfdf5,#d1fae5); }
#     .logo-row{display:flex;align-items:center;gap:12px}
#     .logo-row img{border-radius:8px}
#     .user-card{background:white;border-radius:10px;padding:12px;margin-bottom:12px;box-shadow:0 4px 10px rgba(2,6,23,0.04)}
#     .sidebar-btn{width:100%;padding:8px;border-radius:8px;background:var(--green);color:white;border:none;font-weight:600}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # --- Sidebar (after login)
# if st.session_state.token:
#     with st.sidebar:
#         # logo + title
#         st.markdown('<div class="logo-row">', unsafe_allow_html=True)
#         try:
#             st.image("assets/logo.png", width=58)
#         except Exception:
#             st.markdown("<div style='width:58px;height:58px;background:#e6f4ea;border-radius:8px;'></div>", unsafe_allow_html=True)
#         st.markdown("<div><strong>Pashudhan AI</strong><div style='font-size:12px;color:gray'>Cattle Breed AI</div></div>", unsafe_allow_html=True)
#         st.markdown('</div>')
#         st.markdown("---")

#         # user card (profile fetch)
#         user = get_user_profile(st.session_state.token)
#         if user:
#             st.markdown(f'<div class="user-card"><strong>👋 {user.get("username") or user.get("name")}</strong><div style="color:var(--muted);font-size:12px">{user.get("email")}</div></div>', unsafe_allow_html=True)
#         else:
#             st.info("Unable to load profile")

#         # navigation
#         if st.button("🔍 Predict Breed"):
#             st.session_state.page = "predict"; st.experimental_rerun()
#         if st.button("👤 Profile"):
#             st.session_state.page = "profile"; st.experimental_rerun()
#         st.markdown("---")
#         if st.button("🚪 Logout"):
#             st.session_state.token = None
#             st.session_state.page = "login"
#             st.rerun()


# # --- Main content
# if st.session_state.page == "login" and not st.session_state.token:
#     st.markdown('<div class="hero"><h1>🐄 Pashudhan AI</h1><div>Smart cattle breed recognition powered by AI</div></div>', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.subheader("🔐 Login")
#         email = st.text_input("Email", key="login_email")
#         password = st.text_input("Password", type="password", key="login_pass")
#         if st.button("Login"):
#             res = login(email, password)
#             if res and res.status_code == 200:
#                 token = res.json().get("access_token")
#                 if token:
#                     st.session_state.token = token
#                     st.session_state.page = "dashboard"
#                     st.success("Logged in")
#                     st.rerun()
#                 else:
#                     st.error("Login response missing token")
#             else:
#                 st.error(f"Login failed: {res.text if res is not None else 'no response'}")

#     with col2:
#         st.subheader("📝 Create account")
#         su_name = st.text_input("Full name", key="su_name")
#         su_email = st.text_input("Email", key="su_email")
#         su_password = st.text_input("Password", type="password", key="su_pass")
#         if st.button("Signup"):
#             res = signup(su_name, su_email, su_password)
#             if res and res.status_code in (200, 201):
#                 st.success("Signup success — please login")
#             else:
#                 st.error(f"Signup failed: {res.text if res is not None else 'no response'}")

# elif st.session_state.token:
#     # Dashboard
#     st.markdown('<div class="hero"><h1>Dashboard</h1><div>Welcome to your prediction dashboard</div></div>', unsafe_allow_html=True)

#     # quick action cards
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         st.markdown('<div class="card"><h4>Predict</h4><p>Upload an image and get breed predictions</p></div>', unsafe_allow_html=True)
#         if st.button("Go to Predict"):
#             st.session_state.page = "predict"; st.experimental_rerun()
#     with c2:
#         st.markdown('<div class="card"><h4>Profile</h4><p>View or edit your account</p></div>', unsafe_allow_html=True)
#         if st.button("Open Profile"):
#             st.session_state.page = "profile"; st.experimental_rerun()
#     with c3:
#         st.markdown('<div class="card"><h4>Help</h4><p>Docs & contact</p></div>', unsafe_allow_html=True)
#         if st.button("Open Help"):
#             st.info("Open docs or contact info here")

#     st.markdown("---")
#     st.markdown("### Recent predictions (sample)")
#     # sample table (replace with real API data if you add endpoint)
#     st.table([{"Image":"sample.jpg","Predicted":"Sahiwal","Confidence":"92%"}])



# import streamlit as st
# import os
# from utils.api_helper import login, signup, get_user_profile, update_user_profile



# # 🌿 --- PAGE CONFIG ---
# st.set_page_config(page_title="🐄 Pashudhan AI", layout="wide")

# # 🌿 --- SESSION INIT ---
# if "token" not in st.session_state:
#     st.session_state.token = None
# if "page" not in st.session_state:
#     st.session_state.page = "login"

# # 🌿 --- GLOBAL STYLES ---
# st.markdown("""
#     <style>
#         .block-container {padding: 2rem 3rem;}
#         .title-text {
#             background: linear-gradient(90deg, #00b09b, #96c93d);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             font-weight: 800;
#             font-size: 3rem;
#             text-align: center;
#         }
#         div.stButton > button {
#             background-color: #00b09b;
#             color: white;
#             font-weight: 600;
#             border-radius: 10px;
#             border: none;
#             width: 100%;
#             padding: 0.75rem;
#             transition: 0.3s ease;
#         }
#         div.stButton > button:hover {
#             background-color: #01947c;
#             transform: scale(1.03);
#         }
#         /* Sidebar visible only after login */
#         section[data-testid="stSidebar"] {
#             background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 100%);
#             color: white;
#             padding-top: 2rem;
#         }
#         .profile-header {
#             display: flex;
#             align-items: center;
#             gap: 12px;
#             padding: 0.8rem 1rem;
#             background: rgba(255,255,255,0.1);
#             border-radius: 12px;
#             margin: 0 1rem 1rem 1rem;
#             box-shadow: 0 2px 8px rgba(0,0,0,0.15);
#             cursor: pointer;
#             transition: all 0.3s ease;
#         }
#         .profile-header:hover {background: rgba(255,255,255,0.15);}
#         .profile-pic {
#             width: 48px;
#             height: 48px;
#             border-radius: 50%;
#             object-fit: cover;
#             border: 2px solid white;
#         }
#         .username {
#             font-weight: 600;
#             color: white;
#             font-size: 1rem;
#         }
#         .profile-card {
#             background-color: #fff;
#             padding: 1.5rem;
#             border-radius: 16px;
#             box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#             text-align: center;
#             margin: 0 1rem;
#         }
#         .profile-pic-lg {
#             width: 100px;
#             height: 100px;
#             border-radius: 50%;
#             object-fit: cover;
#             margin-bottom: 0.5rem;
#             border: 3px solid #4caf50;
#         }
#         .edit-btn {
#             background-color: #0095f6;
#             color: white;
#             border: none;
#             padding: 8px 16px;
#             border-radius: 8px;
#             cursor: pointer;
#             font-weight: bold;
#         }
#         .edit-btn:hover {background-color: #0077c8;}
#     </style>
# """, unsafe_allow_html=True)

# # 🌿 --- SIDEBAR (after login only) ---
# if st.session_state.token:
#     with st.sidebar:
#         user_data = get_user_profile(st.session_state.token)
#         profile_image_url = user_data.get("profile_image") if user_data and user_data.get("profile_image") else "https://cdn-icons-png.flaticon.com/512/1077/1077012.png"

#         if "profile_expanded" not in st.session_state:
#             st.session_state.profile_expanded = False

#         # --- Profile Header ---
#         clicked = st.button("👤 View Profile", key="profile_btn")
#         st.markdown(
#             f'<div class="profile-header"><img src="{profile_image_url}" class="profile-pic"><span class="username">{user_data.get("username", "User")}</span></div>',
#             unsafe_allow_html=True
#        )


#         # --- Expanded profile section ---
#         if st.session_state.profile_expanded:
#             st.markdown('<div class="profile-card">', unsafe_allow_html=True)

#             # Profile Details
#             st.image(profile_image_url, use_column_width=False, width=100)
#             st.markdown(f"### {user_data.get('username', 'User')}")
#             st.markdown(f"📧 {user_data.get('email', 'N/A')}")
#             st.markdown(f"🕒 Joined: {user_data.get('created_at', 'N/A')}")

#             # Edit form
#             with st.expander("✏️ Edit Profile"):
#                 with st.form("edit_form_sidebar"):
#                     new_username = st.text_input("Username", user_data.get("username", ""))
#                     new_email = st.text_input("Email", user_data.get("email", ""))
#                     save = st.form_submit_button("💾 Save Changes")

#                     if save:
#                         update_data = {"username": new_username, "email": new_email}
#                         if update_user_profile(st.session_state.token, update_data):
#                             st.success("✅ Profile updated successfully!")
#                         else:
#                             st.error("❌ Update failed. Try again later.")

#             st.divider()
#             if st.button("🚪 Logout"):
#                 st.session_state.token = None
#                 st.session_state.page = "login"
#                 st.rerun()

#             st.markdown('</div>', unsafe_allow_html=True)

#         # --- Toggle dropdown ---
#         if clicked:
#             st.session_state.profile_expanded = not st.session_state.profile_expanded


# # 🌿 --- LOGIN / SIGNUP PAGE ---
# if st.session_state.page == "login" and not st.session_state.token:
#     # 🔒 Hide sidebar (before login)
#     st.markdown("""
#         <style>
#             [data-testid="stSidebar"] {display: none;}
#             .block-container {padding-top: 3rem;}
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="title-text">🐄 Pashudhan AI</div>', unsafe_allow_html=True)
#     st.markdown("### Your Smart Livestock Breed Identifier")

#     tab1, tab2 = st.tabs(["🔐 Login", "📝 Signup"])

#     # --- Login ---
#     with tab1:
#         st.subheader("Welcome Back 👋")
#         email = st.text_input("📧 Email", key="login_email")
#         password = st.text_input("🔑 Password", type="password", key="login_pass")
#         if st.button("Login"):
#             if email and password:
#                 res = login(email, password)
#                 if res and res.status_code == 200:
#                     token = res.json().get("access_token")
#                     if token:
#                         st.session_state.token = token
#                         st.session_state.page = "dashboard"
#                         st.success("✅ Login successful!")
#                         st.rerun()
#                     else:
#                         st.error("❌ Login failed.")
#                 else:
#                     st.error("Invalid credentials or server issue.")

#     # --- Signup ---
#     with tab2:
#         st.subheader("Create Account ✨")
#         username = st.text_input("👤 Username", key="signup_user")
#         email = st.text_input("📧 Email", key="signup_email")
#         password = st.text_input("🔑 Password", type="password", key="signup_pass")

#         if st.button("Signup"):
#             if username and email and password:
#                 res = signup(username, email, password)
#                 if res and res.status_code == 201:
#                     st.success("✅ Signup successful! Please login now.")
#                 else:
#                     st.error("Signup failed. Try again.")


# # 🌿 --- DASHBOARD PAGE ---
# elif st.session_state.token:
#     # 🐄 Center logo at top
#     # --- Logo section in dashboard ---
#     logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
#     st.markdown("""
#     <style>
#         .dashboard-banner {
#             background: linear-gradient(135deg, #00b09b, #96c93d);
#             border-radius: 20px;
#             padding: 2rem;
#             margin: 2rem 0;
#             color: white;
#             text-align: center;
#             box-shadow: 0 4px 15px rgba(0,0,0,0.15);
#             animation: fadeIn 1.5s ease-in-out;
#         }
#         @keyframes fadeIn {
#             from { opacity: 0; transform: translateY(20px); }
#             to { opacity: 1; transform: translateY(0); }
#         }
#     </style>

#     <div class="dashboard-banner">
#         <h2>Welcome back to <b>Pashudhan AI</b> 🐄</h2>
#         <p>Analyze and predict cattle breeds using advanced deep learning models.</p>
#     </div>
# """, unsafe_allow_html=True)




#     st.markdown('<div class="title-text">🐄 Pashudhan AI Dashboard</div>', unsafe_allow_html=True)
#     st.markdown("### Explore AI-powered livestock tools")

#     # Only one button on dashboard
#     if st.button("🔍 Predict Breed"):
#         st.switch_page("pages/1_🐄_Breed_Prediction.py")

#     st.markdown("---")
#     st.markdown(
#         "<p style='text-align:center; color:gray;'>Powered by AI | Developed with ❤️ by Beed Brigade</p>",
#         unsafe_allow_html=True,
#     )


# main_app.py
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
        if st.button("🔍 Predict Breed"):
            # if your prediction page is a separate streamlit page, use switch_page
            try:
                st.switch_page("pages/1_🐄_Breed_Prediction.py")
            except Exception:
                # fallback: set page variable so your router can handle
                st.session_state.page = "breed_prediction"
                st.rerun()
        if st.button("👤 Profile"):
            try:
                st.switch_page("Profile")
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

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("🔍 Predict Breed"):
            try:
              # Use page filename without .py
              st.switch_page("6_Breed_Prediction")
            except Exception:
            # fallback in case switch_page fails
              st.session_state.page = "Breed_Prediction"
              st.rerun()

    
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Powered by AI | Developed with ❤️ by Beed Brigade</p>",
        unsafe_allow_html=True,
    )
