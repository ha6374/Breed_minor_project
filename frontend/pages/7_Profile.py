# import streamlit as st
# from utils.api_helper import get_user_profile, update_user_profile, upload_profile_image

# st.set_page_config(page_title="Profile", page_icon="👤", layout="centered")

# # ==========================
# # ACCESS CONTROL
# # ==========================
# if "token" not in st.session_state or not st.session_state.token:
#     st.warning("Please login first.")
#     st.switch_page("pages/2_Login.py")

# # ==========================
# # SIDEBAR
# # ==========================
# with st.sidebar:
#     st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
#     st.header("👤 Profile Menu")

#     if st.button("🏠 Dashboard"):
#         st.switch_page("pages/5_Dashboard.py")

#     if st.button("🐄 Breed Prediction"):
#         st.switch_page("pages/6_Breed_Prediction")

#     st.write("---")
#     if st.button("🚪 Logout"):
#         st.session_state.clear()
#         st.switch_page("pages/2_Login.py")


# # ==========================
# # FETCH USER PROFILE
# # ==========================
# profile = get_user_profile(st.session_state.token)
# if not profile:
#     st.error("Failed to load profile. Please try again.")
#     st.stop()

# # ==========================
# # CUSTOM CSS
# # ==========================
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
# </style>
# """, unsafe_allow_html=True)

# # ==========================
# # UI CARD
# # ==========================
# st.markdown('<div class="profile-card">', unsafe_allow_html=True)

# # PROFILE IMAGE
# profile_img = profile.get("profile_image")
# if profile_img:
#     st.image(f"https://breed-minor-project.onrender.com/{profile_img}", width=150)
# else:
#     st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=150)

# # UPLOAD NEW IMAGE
# uploaded = st.file_uploader("📸 Upload new profile picture", type=["png", "jpg", "jpeg"])
# if uploaded:
#     with st.spinner("Uploading..."):
#         ok = upload_profile_image(st.session_state.token, uploaded)
#         if ok:
#             st.success("Profile picture updated!")
#             st.rerun()
#         else:
#             st.error("Upload failed!")

# # BASIC DETAILS
# st.markdown(f"### {profile.get('username', 'User')}")
# st.markdown(f"**{profile.get('email', '')}**")
# st.markdown(f"Joined: `{profile.get('created_at', '')}`")

# # EDIT FORM
# with st.expander("✏️ Edit Profile"):
#     with st.form("edit_profile"):
#         new_user = st.text_input("Username", value=profile.get("username", ""))
#         new_email = st.text_input("Email", value=profile.get("email", ""))

#         submit = st.form_submit_button("💾 Save")

#         if submit:
#             ok = update_user_profile(st.session_state.token, {
#                 "username": new_user,
#                 "email": new_email
#             })
#             if ok:
#                 st.success("Profile updated. Refresh to see changes.")
#             else:
#                 st.error("Failed to update.")

# st.markdown('</div>', unsafe_allow_html=True)


# import streamlit as st
# from utils.api_helper import get_profile_api, upload_profile_image_api

# st.set_page_config(page_title="Profile", layout="centered")

# if "token" not in st.session_state:
#     st.switch_page("pages/2_Login.py")

# st.markdown("""
# <style>
# .profile-card {
#     background: white;
#     padding: 35px;
#     border-radius: 18px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='profile-card'>", unsafe_allow_html=True)
# st.subheader("My Profile")

# success, response = get_profile_api(st.session_state["token"])

# if success:
#     st.write(f"**Email:** {response.get('email')}")
# else:
#     st.error(response)

# st.write("### Update Profile Image")
# file = st.file_uploader("Upload new profile image", type=["jpg", "png", "jpeg"])

# if file:
#     success, response = upload_profile_image_api(
#         st.session_state["token"],
#         file
#     )

#     if success:
#         st.success("Profile image updated successfully")
#     else:
#         st.error(response)

# st.write("")
# st.button("Back to Dashboard", use_container_width=True,
#           on_click=lambda: st.switch_page("pages/5_Dashboard.py"))

# st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
from utils.api_helper import get_user_profile, update_user_profile, upload_profile_image

st.set_page_config(page_title="Profile | Pashudhan AI", page_icon="👤", layout="centered")

# ==========================
# ACCESS CONTROL
# ==========================
if "token" not in st.session_state or not st.session_state.token:
    st.warning("⚠️ Please login first.")
    st.stop()

# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
    st.header("👤 Profile Menu")

    if st.button("🏠 Dashboard"):
        st.switch_page("pages/5_Dashboard.py")

    if st.button("🐄 Breed Prediction"):
        st.switch_page("pages/6_Breed_Prediction.py")

    st.write("---")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/2_Login.py")

# ==========================
# FETCH USER PROFILE
# ==========================
profile = get_user_profile(st.session_state.token)
if not profile:
    st.error("⚠️ Failed to load profile. Please try again later.")
    st.stop()

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>
.profile-card {
    background-color: #f9f9f9;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    text-align: center;
    max-width: 450px;
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
# PROFILE CARD
# ==========================
st.markdown('<div class="profile-card">', unsafe_allow_html=True)

# PROFILE IMAGE
profile_img = profile.get("profile_image")
if profile_img:
    if profile_img.startswith("http"):
        st.image(profile_img, width=150)
    else:
        st.image(f"https://breed-minor-project.onrender.com/{profile_img}", width=150)
else:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=150)

# UPLOAD NEW IMAGE
uploaded = st.file_uploader("📸 Upload new profile picture", type=["png", "jpg", "jpeg"])
if uploaded:
    with st.spinner("Uploading..."):
        res = upload_profile_image(st.session_state.token, uploaded)
        if res:
            st.success("✅ Profile picture updated!")
            st.experimental_rerun()
        else:
            st.error("❌ Upload failed!")

# BASIC DETAILS
st.markdown(f"### {profile.get('username', 'User')}")
st.markdown(f"**{profile.get('email', '')}**")
st.markdown(f"Joined: `{profile.get('created_at', '')}`")

# EDIT FORM
with st.expander("✏️ Edit Profile"):
    with st.form("edit_profile"):
        new_user = st.text_input("Username", value=profile.get("username", ""))
        new_email = st.text_input("Email", value=profile.get("email", ""))

        submit = st.form_submit_button("💾 Save Changes")
        if submit:
            res = update_user_profile(st.session_state.token, {
                "username": new_user,
                "email": new_email
            })
            if res:
                st.success("✅ Profile updated successfully!")
                st.experimental_rerun()
            else:
                st.error("❌ Failed to update profile.")

st.markdown('</div>', unsafe_allow_html=True)

