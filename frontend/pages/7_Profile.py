# # # import streamlit as st
# # # from utils.api_helper import get_user_profile

# # # st.set_page_config(page_title="Profile")

# # # if "token" not in st.session_state or not st.session_state.token:
# # #     st.warning("Please login first.")
# # #     st.switch_page("main_app.py")

# # # st.title("👤 Your Profile")

# # # profile = get_user_profile(st.session_state.token)

# # # if profile:
# # #     st.json(profile)
# # # else:
# # #     st.error("Failed to fetch profile. Try re-logging in.")
# # import streamlit as st
# # from utils.api_helper import get_user_profile, update_user_profile

# # st.set_page_config(page_title="Profile", page_icon="👤", layout="centered")

# # # 🔒 Login check
# # if "token" not in st.session_state or not st.session_state.token:
# #     st.warning("Please login first.")
# #     st.switch_page("main_app.py")

# # # --- Fetch user data from backend ---
# # profile = get_user_profile(st.session_state.token)

# # if not profile:
# #     st.error("Failed to fetch profile. Try re-logging in.")
# #     st.stop()

# # # --- Custom CSS for Instagram-like design ---
# # st.markdown("""
# #     <style>
# #     .profile-card {
# #         background-color: #fff;
# #         padding: 2rem;
# #         border-radius: 20px;
# #         box-shadow: 0 4px 12px rgba(0,0,0,0.1);
# #         text-align: center;
# #         width: 400px;
# #         margin: auto;
# #     }
# #     .profile-pic {
# #         width: 120px;
# #         height: 120px;
# #         border-radius: 50%;
# #         object-fit: cover;
# #         margin-bottom: 1rem;
# #         border: 3px solid #ddd;
# #     }
# #     .edit-btn {
# #         background-color: #0095f6;
# #         color: white;
# #         border: none;
# #         padding: 8px 16px;
# #         border-radius: 8px;
# #         cursor: pointer;
# #         font-weight: bold;
# #     }
# #     .edit-btn:hover {
# #         background-color: #0077c8;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # --- Profile card ---
# # st.markdown('<div class="profile-card">', unsafe_allow_html=True)

# # # Default profile image (you can replace with API field later)
# # profile_image_url = "https://cdn-icons-png.flaticon.com/512/1077/1077012.png"

# # st.image(profile_image_url, use_column_width=False, width=120, caption="Profile Picture")

# # st.markdown(f"<h3>{profile.get('username', 'User')}</h3>", unsafe_allow_html=True)
# # st.markdown(f"<p style='color:gray'>{profile.get('email', '')}</p>", unsafe_allow_html=True)
# # st.markdown(f"<p>Joined: {profile.get('created_at', '')}</p>", unsafe_allow_html=True)

# # # --- Edit form ---
# # with st.expander("✏️ Edit Profile"):
# #     with st.form("edit_form"):
# #         new_username = st.text_input("Username", profile.get("username", ""))
# #         new_email = st.text_input("Email", profile.get("email", ""))
# #         submitted = st.form_submit_button("💾 Save Changes")

# #         if submitted:
# #             update_data = {"username": new_username, "email": new_email}
# #             if update_user_profile(st.session_state.token, update_data):
# #                 st.success("✅ Profile updated successfully!")
# #             else:
# #                 st.error("❌ Failed to update profile. Try again later.")

# # st.markdown('</div>', unsafe_allow_html=True)



# import streamlit as st
# from utils.api_helper import get_user_profile, update_user_profile, upload_profile_image

# st.set_page_config(page_title="Profile", layout="centered")

# # 🔒 Ensure user is logged in
# if "token" not in st.session_state or not st.session_state.token:
#     st.warning("Please login first.")
#     st.switch_page("main_app.py")

# # Fetch user data
# profile = get_user_profile(st.session_state.token)
# if not profile:
#     st.error("Failed to fetch profile. Try re-logging in.")
#     st.stop()

# # --- Custom CSS ---
# st.markdown("""
# <style>
# .profile-card {
#     background-color: #ffffff;
#     border-radius: 20px;
#     padding: 2rem;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#     text-align: center;
#     width: 450px;
#     margin: auto;
# }
# .profile-pic {
#     width: 130px;
#     height: 130px;
#     border-radius: 50%;
#     object-fit: cover;
#     margin-bottom: 1rem;
#     border: 3px solid #4caf50;
# }
# .edit-btn {
#     background-color: #2e7d32;
#     color: white;
#     font-weight: bold;
#     border: none;
#     padding: 8px 18px;
#     border-radius: 8px;
#     cursor: pointer;
#     transition: 0.3s;
# }
# .edit-btn:hover {
#     background-color: #1b5e20;
# }
# </style>
# """, unsafe_allow_html=True)

# # --- Profile UI Card ---
# st.markdown('<div class="profile-card">', unsafe_allow_html=True)

# # ✅ Profile image display
# profile_img = profile.get("profile_image")
# if profile_img:
#     st.image(f"http://127.0.0.1:8000/{profile_img}", width=130, caption="Profile Picture")
# else:
#     st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=130, caption="Default Picture")

# # --- Upload new image ---
# uploaded_img = st.file_uploader("📸 Upload new profile picture", type=["png", "jpg", "jpeg"])
# if uploaded_img:
#     with st.spinner("Uploading..."):
#         ok = upload_profile_image(st.session_state.token, uploaded_img)
#         if ok:
#             st.success("✅ Profile picture updated successfully!")
#             st.rerun()
#         else:
#             st.error("❌ Upload failed. Try again later.")

# # --- Profile Info ---
# st.markdown(f"<h3>{profile.get('username', 'User')}</h3>", unsafe_allow_html=True)
# st.markdown(f"<p style='color:gray'>{profile.get('email', '')}</p>", unsafe_allow_html=True)
# st.markdown(f"<p>Joined: {profile.get('created_at', '')}</p>", unsafe_allow_html=True)

# # --- Edit form ---
# with st.expander("✏️ Edit Profile"):
#     with st.form("edit_profile_form"):
#         new_username = st.text_input("Username", value=profile.get("username", ""))
#         new_email = st.text_input("Email", value=profile.get("email", ""))
#         submitted = st.form_submit_button("💾 Save Changes")

#         if submitted:
#             ok = update_user_profile(st.session_state.token, {"username": new_username, "email": new_email})
#             if ok:
#                 st.success("✅ Profile updated successfully! Refresh to see changes.")
#             else:
#                 st.error("❌ Failed to update profile. Try again later.")

# st.markdown('</div>', unsafe_allow_html=True)


import streamlit as st
from utils.api_helper import get_user_profile, update_user_profile, upload_profile_image

st.set_page_config(page_title="Profile", page_icon="👤", layout="centered")

# ==========================
# ACCESS CONTROL
# ==========================
if "token" not in st.session_state or not st.session_state.token:
    st.warning("Please login first.")
    st.switch_page("pages/2_Login.py")

# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
    st.header("👤 Profile Menu")

    if st.button("🏠 Dashboard"):
        st.switch_page("pages/5_Dashboard.py")

    if st.button("🐄 Breed Prediction"):
        st.switch_page("pages/6_Prediction.py")

    st.write("---")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/2_Login.py")


# ==========================
# FETCH USER PROFILE
# ==========================
profile = get_user_profile(st.session_state.token)
if not profile:
    st.error("Failed to load profile. Please try again.")
    st.stop()

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>
.profile-card {
    background-color: #ffffff;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    text-align: center;
    width: 450px;
    margin: auto;
}
.profile-pic {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
    border: 3px solid #4caf50;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# UI CARD
# ==========================
st.markdown('<div class="profile-card">', unsafe_allow_html=True)

# PROFILE IMAGE
profile_img = profile.get("profile_image")
if profile_img:
    st.image(f"http://127.0.0.1:8000/{profile_img}", width=150)
else:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=150)

# UPLOAD NEW IMAGE
uploaded = st.file_uploader("📸 Upload new profile picture", type=["png", "jpg", "jpeg"])
if uploaded:
    with st.spinner("Uploading..."):
        ok = upload_profile_image(st.session_state.token, uploaded)
        if ok:
            st.success("Profile picture updated!")
            st.rerun()
        else:
            st.error("Upload failed!")

# BASIC DETAILS
st.markdown(f"### {profile.get('username', 'User')}")
st.markdown(f"**{profile.get('email', '')}**")
st.markdown(f"Joined: `{profile.get('created_at', '')}`")

# EDIT FORM
with st.expander("✏️ Edit Profile"):
    with st.form("edit_profile"):
        new_user = st.text_input("Username", value=profile.get("username", ""))
        new_email = st.text_input("Email", value=profile.get("email", ""))

        submit = st.form_submit_button("💾 Save")

        if submit:
            ok = update_user_profile(st.session_state.token, {
                "username": new_user,
                "email": new_email
            })
            if ok:
                st.success("Profile updated. Refresh to see changes.")
            else:
                st.error("Failed to update.")

st.markdown('</div>', unsafe_allow_html=True)
