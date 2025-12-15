# # import streamlit as st
# # import time

# # st.set_page_config(
# #     page_title="Welcome | Pashudhan AI",
# #     page_icon="🐄",
# #     layout="wide"
# # )

# # st.markdown("""
# #     <div style="text-align:center; margin-top:80px;">
# #         <img src="https://i.imgur.com/9B1xU6X.gif" width="280">
# #         <h1 style="color:#4a4a4a; font-size:42px;">🐄 Pashudhan AI</h1>
# #         <p style="font-size:22px;">Smart Cattle Breed Prediction System</p>
# #     </div>
# # """, unsafe_allow_html=True)

# # time.sleep(2)

# # st.switch_page("pages/2_Login.py")

# import streamlit as st
# import time

# st.set_page_config(
#     page_title="Welcome | Pashudhan AI",
#     page_icon="🐄",
#     layout="wide"
# )

# # ==========================
# # SESSION / TOKEN CHECK
# # ==========================
# if "token" in st.session_state and st.session_state.token:
#     st.success("Already logged in! Redirecting to Dashboard...")
#     time.sleep(1)
#     st.switch_page("5_Dashboard")  # Dashboard page

# # ==========================
# # INITIALIZE SPLASH FLAG
# # ==========================
# if "seen_splash" not in st.session_state:
#     st.session_state.seen_splash = False

# # ==========================
# # MODERN SPLASH SCREEN
# # ==========================
# if not st.session_state.seen_splash:
#     st.markdown("""
#         <style>
#             .title-text {
#                 background: linear-gradient(90deg, #00b09b, #96c93d);
#                 -webkit-background-clip: text;
#                 -webkit-text-fill-color: transparent;
#                 font-weight: 900;
#                 font-size: 3rem;
#                 text-align: center;
#                 animation: fadeInDown 1.5s ease-out;
#             }

#             @keyframes fadeInDown {
#                 0% { opacity: 0; transform: translateY(-30px); }
#                 100% { opacity: 1; transform: translateY(0); }
#             }

#             .splash-button {
#                 background: linear-gradient(90deg, #00b09b, #96c93d);
#                 color: white;
#                 border: none;
#                 padding: 1rem 2rem;
#                 border-radius: 12px;
#                 font-size: 1.2rem;
#                 font-weight: bold;
#                 cursor: pointer;
#                 transition: transform 0.3s ease, box-shadow 0.3s ease;
#             }
#             .splash-button:hover {
#                 transform: scale(1.05);
#                 box-shadow: 0 8px 20px rgba(0,0,0,0.2);
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div style="text-align:center; margin-top:5rem;">', unsafe_allow_html=True)

#     # Animated GIF
#     st.image("https://i.imgur.com/9B1xU6X.gif", width=280)

#     # Gradient title
#     st.markdown('<h1 class="title-text">🐄 Pashudhan AI</h1>', unsafe_allow_html=True)
#     st.markdown('<p style="font-size:22px; color:#4a4a4a;">Smart Cattle Breed Prediction System</p>', unsafe_allow_html=True)

#     # Get Started Button
#     col1, col2, col3 = st.columns([1,2,1])
#     with col2:
#         if st.button("Get Started", key="splash_btn"):
#             st.session_state.seen_splash = True
#             st.switch_page("2_Login")  # Redirect to Login

#     st.markdown('</div>', unsafe_allow_html=True)
#     st.stop()
# else:
#     # Splash already seen → go to login
#     st.switch_page("2_Login")

import streamlit as st
import os
import time

st.set_page_config(
    page_title="Welcome | Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)

# ==========================
# SESSION / TOKEN CHECK
# ==========================
if "token" in st.session_state and st.session_state.token:
    st.success("Already logged in! Redirecting to Dashboard...")
    time.sleep(1)
    st.switch_page("pages/5_Dashboard.py")  # Dashboard page

# ==========================
# INITIALIZE SPLASH FLAG
# ==========================
if "seen_splash" not in st.session_state:
    st.session_state.seen_splash = False

# ==========================
# MODERN SPLASH SCREEN
# ==========================
if not st.session_state.seen_splash:
    st.markdown("""
        <style>
            .title-text {
                background: linear-gradient(90deg, #00b09b, #96c93d);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 900;
                font-size: 3rem;
                text-align: center;
                animation: fadeInDown 1.5s ease-out;
            }

            .splash-button {
                background: linear-gradient(90deg, #00b09b, #96c93d);
                color: white;
                border: none;
                padding: 1rem 2rem;
                border-radius: 12px;
                font-size: 1.2rem;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .splash-button:hover {
                transform: scale(1.05);
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; margin-top:5rem;">', unsafe_allow_html=True)

    # ✅ Load local logo.png
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=280)
    else:
        # fallback online image
        st.image("https://i.imgur.com/9B1xU6X.png", width=280)

    # Gradient title
    st.markdown('<h1 class="title-text">🐄 Pashudhan AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:22px; color:#4a4a4a;">Smart Cattle Breed Prediction System</p>', unsafe_allow_html=True)

    # Get Started Button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Get Started", key="splash_btn"):
            st.session_state.seen_splash = True
            st.switch_page("pages/2_Login.py")  # Login page

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()
else:
    # Splash already seen → go to login
    st.switch_page("pages/2_Login.py")

