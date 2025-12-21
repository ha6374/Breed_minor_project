# import streamlit as st
# import time

# st.set_page_config(
#     page_title="Welcome | Pashudhan AI",
#     page_icon="🐄",
#     layout="wide"
# )

# st.markdown("""
#     <div style="text-align:center; margin-top:80px;">
#         <img src="https://i.imgur.com/9B1xU6X.gif" width="280">
#         <h1 style="color:#4a4a4a; font-size:42px;">🐄 Pashudhan AI</h1>
#         <p style="font-size:22px;">Smart Cattle Breed Prediction System</p>
#     </div>
# """, unsafe_allow_html=True)

# time.sleep(2)

# st.switch_page("pages/2_Login.py")

# # # # import streamlit as st
# # # # import time

# # # # st.set_page_config(
# # # #     page_title="Welcome | Pashudhan AI",
# # # #     page_icon="🐄",
# # # #     layout="wide"
# # # # )

# # # # # ==========================
# # # # # SESSION / TOKEN CHECK
# # # # # ==========================
# # # # if "token" in st.session_state and st.session_state.token:
# # # #     st.success("Already logged in! Redirecting to Dashboard...")
# # # #     time.sleep(1)
# # # #     st.switch_page("5_Dashboard")  # Dashboard page

# # # # # ==========================
# # # # # INITIALIZE SPLASH FLAG
# # # # # ==========================
# # # # if "seen_splash" not in st.session_state:
# # # #     st.session_state.seen_splash = False

# # # # # ==========================
# # # # # MODERN SPLASH SCREEN
# # # # # ==========================
# # # # if not st.session_state.seen_splash:
# # # #     st.markdown("""
# # # #         <style>
# # # #             .title-text {
# # # #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# # # #                 -webkit-background-clip: text;
# # # #                 -webkit-text-fill-color: transparent;
# # # #                 font-weight: 900;
# # # #                 font-size: 3rem;
# # # #                 text-align: center;
# # # #                 animation: fadeInDown 1.5s ease-out;
# # # #             }

# # # #             @keyframes fadeInDown {
# # # #                 0% { opacity: 0; transform: translateY(-30px); }
# # # #                 100% { opacity: 1; transform: translateY(0); }
# # # #             }

# # # #             .splash-button {
# # # #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# # # #                 color: white;
# # # #                 border: none;
# # # #                 padding: 1rem 2rem;
# # # #                 border-radius: 12px;
# # # #                 font-size: 1.2rem;
# # # #                 font-weight: bold;
# # # #                 cursor: pointer;
# # # #                 transition: transform 0.3s ease, box-shadow 0.3s ease;
# # # #             }
# # # #             .splash-button:hover {
# # # #                 transform: scale(1.05);
# # # #                 box-shadow: 0 8px 20px rgba(0,0,0,0.2);
# # # #             }
# # # #         </style>
# # # #     """, unsafe_allow_html=True)

# # # #     st.markdown('<div style="text-align:center; margin-top:5rem;">', unsafe_allow_html=True)

# # # #     # Animated GIF
# # # #     st.image("https://i.imgur.com/9B1xU6X.gif", width=280)

# # # #     # Gradient title
# # # #     st.markdown('<h1 class="title-text">🐄 Pashudhan AI</h1>', unsafe_allow_html=True)
# # # #     st.markdown('<p style="font-size:22px; color:#4a4a4a;">Smart Cattle Breed Prediction System</p>', unsafe_allow_html=True)

# # # #     # Get Started Button
# # # #     col1, col2, col3 = st.columns([1,2,1])
# # # #     with col2:
# # # #         if st.button("Get Started", key="splash_btn"):
# # # #             st.session_state.seen_splash = True
# # # #             st.switch_page("2_Login")  # Redirect to Login

# # # #     st.markdown('</div>', unsafe_allow_html=True)
# # # #     st.stop()
# # # # else:
# # # #     # Splash already seen → go to login
# # # #     st.switch_page("2_Login")
# # # import streamlit as st
# # # import os
# # # import time

# # # st.set_page_config(
# # #     page_title="Welcome | Pashudhan AI",
# # #     page_icon="🐄",
# # #     layout="wide"
# # # )

# # # # ==========================
# # # # SESSION / TOKEN CHECK
# # # # ==========================
# # # if "token" in st.session_state and st.session_state.token:
# # #     st.success("Already logged in! Redirecting to Dashboard...")
# # #     time.sleep(1)
# # #     st.switch_page("pages/5_Dashboard.py")  # Page title of dashboard

# # # # ==========================
# # # # INITIALIZE SPLASH FLAG
# # # # ==========================
# # # if "seen_splash" not in st.session_state:
# # #     st.session_state.seen_splash = False

# # # # ==========================
# # # # MODERN SPLASH SCREEN
# # # # ==========================
# # # if not st.session_state.seen_splash:
# # #     st.markdown("""
# # #         <style>
# # #             .title-text {
# # #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# # #                 -webkit-background-clip: text;
# # #                 -webkit-text-fill-color: transparent;
# # #                 font-weight: 900;
# # #                 font-size: 3rem;
# # #                 text-align: center;
# # #                 animation: fadeInDown 1.5s ease-out;
# # #             }

# # #             .splash-button {
# # #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# # #                 color: white;
# # #                 border: none;
# # #                 padding: 1rem 2rem;
# # #                 border-radius: 12px;
# # #                 font-size: 1.2rem;
# # #                 font-weight: bold;
# # #                 cursor: pointer;
# # #                 transition: transform 0.3s ease, box-shadow 0.3s ease;
# # #             }
# # #             .splash-button:hover {
# # #                 transform: scale(1.05);
# # #                 box-shadow: 0 8px 20px rgba(0,0,0,0.2);
# # #             }
# # #         </style>
# # #     """, unsafe_allow_html=True)

# # #     st.markdown('<div style="text-align:center; margin-top:5rem;">', unsafe_allow_html=True)

# # #     # Load logo.png
# # #     logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
# # #     if os.path.exists(logo_path):
# # #         st.image(logo_path, width=280)
# # #     else:
# # #         st.image("https://i.imgur.com/9B1xU6X.png", width=280)

# # #     # Gradient title
# # #     st.markdown('<h1 class="title-text">🐄 Pashudhan AI</h1>', unsafe_allow_html=True)
# # #     st.markdown('<p style="font-size:22px; color:#4a4a4a;">Smart Cattle Breed Prediction System</p>', unsafe_allow_html=True)

# # #     # Get Started Button
# # #     col1, col2, col3 = st.columns([1,2,1])
# # #     with col2:
# # #         if st.button("Get Started", key="splash_btn"):
# # #             st.session_state.seen_splash = True
# # #             st.switch_page("pages/2_Login.py")  # ✅ Use page title, not file name

# # #     st.markdown('</div>', unsafe_allow_html=True)
# # #     st.stop()
# # # else:
# # #     # Splash already seen → go to login
# # #     st.switch_page("pages/2_Login.py")  # ✅ Page title






# # import streamlit as st
# # import os
# # import time

# # st.set_page_config(
# #     page_title="Welcome | Pashudhan AI",
# #     page_icon="🐄",
# #     layout="wide"
# # )

# # # -------------------------
# # # CHECK IF USER ALREADY LOGGED IN
# # # -------------------------
# # if "token" in st.session_state and st.session_state.token:
# #     st.success("Already logged in! Redirecting to Dashboard...")
# #     time.sleep(1)
# #     st.switch_page("pages/5_Dashboard.py")  # Page title

# # # -------------------------
# # # SPLASH FLAG
# # # -------------------------
# # if "seen_splash" not in st.session_state:
# #     st.session_state.seen_splash = False

# # # -------------------------
# # # SPLASH SCREEN
# # # -------------------------
# # if not st.session_state.seen_splash:
# #     st.markdown("""
# #         <style>
# #             .title-text {
# #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# #                 -webkit-background-clip: text;
# #                 -webkit-text-fill-color: transparent;
# #                 font-weight: 900;
# #                 font-size: 3rem;
# #                 text-align: center;
# #                 animation: fadeInDown 1.5s ease-out;
# #             }
# #             .splash-button {
# #                 background: linear-gradient(90deg, #00b09b, #96c93d);
# #                 color: white;
# #                 border: none;
# #                 padding: 1rem 2rem;
# #                 border-radius: 12px;
# #                 font-size: 1.2rem;
# #                 font-weight: bold;
# #                 cursor: pointer;
# #                 transition: transform 0.3s ease, box-shadow 0.3s ease;
# #             }
# #             .splash-button:hover {
# #                 transform: scale(1.05);
# #                 box-shadow: 0 8px 20px rgba(0,0,0,0.2);
# #             }
# #         </style>
# #     """, unsafe_allow_html=True)

# #     st.markdown('<div style="text-align:center; margin-top:5rem;">', unsafe_allow_html=True)

# #     # ✅ Load local logo
# #     logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
# #     if os.path.exists(logo_path):
# #         st.image(logo_path, width=280)
# #     else:
# #         st.image("https://i.imgur.com/9B1xU6X.png", width=280)

# #     # Title
# #     st.markdown('<h1 class="title-text">🐄 Pashudhan AI</h1>', unsafe_allow_html=True)
# #     st.markdown('<p style="font-size:22px; color:#4a4a4a;">Smart Cattle Breed Prediction System</p>', unsafe_allow_html=True)

# #     # Get Started Button
# #     col1, col2, col3 = st.columns([1,2,1])
# #     with col2:
# #         if st.button("Get Started", key="splash_btn"):
# #             st.session_state.seen_splash = True
# #             st.switch_page("pages/2_Login.py")  # ✅ Page title

# #     st.markdown('</div>', unsafe_allow_html=True)
# #     st.stop()
# # else:
# #     # Already seen → go to Login
# #     st.switch_page("pages/2_Login.py")






# # import streamlit as st

# # st.set_page_config(page_title="Welcome", layout="wide")

# # st.markdown("""
# # <style>
# # .hero {
# #     padding: 60px 40px;
# # }
# # .hero h1 {
# #     font-size: 42px;
# #     font-weight: 700;
# # }
# # .hero p {
# #     color: #6b7280;
# #     font-size: 18px;
# # }
# # .card {
# #     background: white;
# #     padding: 25px;
# #     border-radius: 18px;
# #     box-shadow: 0 10px 24px rgba(0,0,0,0.08);
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # st.markdown("<div class='hero'>", unsafe_allow_html=True)
# # st.markdown("<h1>Breed Recognition System</h1>", unsafe_allow_html=True)
# # st.markdown(
# #     "<p>AI based cattle and buffalo breed identification system using deep learning</p>",
# #     unsafe_allow_html=True
# # )
# # st.markdown("</div>", unsafe_allow_html=True)

# # c1, c2, c3 = st.columns(3)

# # with c1:
# #     st.markdown("<div class='card'>", unsafe_allow_html=True)
# #     st.subheader("Accurate Prediction")
# #     st.write("Deep learning model trained on Indian cattle and buffalo breeds.")
# #     st.markdown("</div>", unsafe_allow_html=True)

# # with c2:
# #     st.markdown("<div class='card'>", unsafe_allow_html=True)
# #     st.subheader("User Friendly")
# #     st.write("Clean interface with proper flow for real world usage.")
# #     st.markdown("</div>", unsafe_allow_html=True)

# # with c3:
# #     st.markdown("<div class='card'>", unsafe_allow_html=True)
# #     st.subheader("Practical Application")
# #     st.write("Helpful for farmers, researchers and veterinary support.")
# #     st.markdown("</div>", unsafe_allow_html=True)

# # st.write("")
# # col1, col2 = st.columns(2)

# # with col1:
# #     st.button("Login", use_container_width=True, on_click=lambda: st.switch_page("pages/2_Login.py"))

# # with col2:
# #     st.button("Create Account", use_container_width=True, on_click=lambda: st.switch_page("pages/3_Signup.py"))




# # new code begain
# import streamlit as st
# import os
# import time

# # -------------------------
# # PAGE CONFIG
# # -------------------------
# st.set_page_config(
#     page_title="Welcome | Pashudhan AI",
#     page_icon="🐄",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # -------------------------
# # AUTO REDIRECT IF LOGGED IN
# # -------------------------
# if "token" in st.session_state and st.session_state.token:
#     st.switch_page("pages/5_Dashboard.py")

# # -------------------------
# # SPLASH FLAG
# # -------------------------
# if "seen_splash" not in st.session_state:
#     st.session_state.seen_splash = False

# # -------------------------
# # SPLASH SCREEN
# # -------------------------
# if not st.session_state.seen_splash:

#     # -------------------------
#     # FULLSCREEN + NO SCROLL + NO CONTAINER
#     # -------------------------
#     st.markdown("""
#     <style>
#     /* Hide Streamlit UI */
#     #MainMenu, header, footer {
#         visibility: hidden;
#         height: 0;
#     }

#     html, body {
#         margin: 0;
#         padding: 0;
#         height: 100%;
#         overflow: hidden;
#     }

#     [data-testid="stApp"] {
#         height: 100vh;
#         overflow: hidden;
#         background: linear-gradient(135deg, #e9fff5, #f7fffb);
#     }

#     .block-container {
#         padding: 0 !important;
#         margin: 0 !important;
#         height: 100vh;
#         overflow: hidden;
#     }

#     /* Perfect center */
#     .center-wrapper {
#         position: fixed;
#         inset: 0;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         text-align: center;
#     }

#     /* Title */
#     .title {
#         font-size: 3.8rem;
#         font-weight: 900;
#         background: linear-gradient(90deg, #00b09b, #96c93d);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-top: 1.2rem;
#     }

#     .subtitle {
#         font-size: 1.4rem;
#         color: #555;
#         margin-bottom: 3rem;
#         font-weight: 500;
#     }

#     .stButton > button {
#         background: linear-gradient(90deg, #00b09b, #96c93d);
#         color: white;
#         border-radius: 18px;
#         padding: 0.9rem 3.5rem;
#         font-size: 1.25rem;
#         font-weight: 700;
#         border: none;
#         transition: all 0.35s ease;
#     }

#     .stButton > button:hover {
#         transform: scale(1.1);
#         box-shadow: 0 20px 45px rgba(0,0,0,0.28);
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # -------------------------
#     # CENTER CONTENT (NO BOX)
#     # -------------------------
#     st.markdown('<div class="center-wrapper"><div>', unsafe_allow_html=True)

#     # LOGO
#     logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
#     if os.path.exists(logo_path):
#         st.image(logo_path, width=260)
#     else:
#         st.image("https://i.imgur.com/9B1xU6X.png", width=260)

#     # TEXT
#     st.markdown('<div class="title">🐄 Pashudhan AI</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<div class="subtitle">Smart Cattle Breed Prediction System</div>',
#         unsafe_allow_html=True
#     )

#     # BUTTON
#     if st.button("Get Started"):
#         st.session_state.seen_splash = True
#         st.switch_page("pages/2_Login.py")

#     st.markdown('</div></div>', unsafe_allow_html=True)

#     # -------------------------
#     # AUTO REDIRECT (10 SECONDS)
#     # -------------------------
#     time.sleep(10)
#     st.session_state.seen_splash = True
#     st.switch_page("pages/2_Login.py")

#     st.stop()

# # -------------------------
# # FALLBACK
# # -------------------------
# else:
#     st.switch_page("pages/2_Login.py")

import streamlit as st
import os

st.set_page_config(
    page_title="Welcome | Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)

# ---------- Styles ----------
st.markdown("""
<style>
    .welcome-title {
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(90deg, #00b09b, #96c93d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .get-started-btn button {
        background-color: #00b09b;
        color: white;
        font-size: 18px;
        padding: 0.75rem 2.5rem;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        transition: 0.3s ease;
    }
    .get-started-btn button:hover {
        background-color: #01947c;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown('<div style="text-align:center; margin-top:3rem;">', unsafe_allow_html=True)

# Cow / Splash Image (local preferred)
splash_path = os.path.join(os.path.dirname(__file__), "..", "assets", "splash.gif")
logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")

if os.path.exists(splash_path):
    st.image(splash_path, width=350)
elif os.path.exists(logo_path):
    st.image(logo_path, width=300)
else:
    st.markdown("<h1>🐄</h1>", unsafe_allow_html=True)

st.markdown('<h1 class="welcome-title">Pashudhan AI</h1>', unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:22px;'>Smart Livestock Breed Identification — powered by AI</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Get Started Button ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Get Started", key="get_started"):
        st.switch_page("pages/2_Login.py")

st.markdown("</div>", unsafe_allow_html=True)

