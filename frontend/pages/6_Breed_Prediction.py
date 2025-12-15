# import streamlit as st
# from utils.api_helper import predict


# st.set_page_config(page_title="Breed Prediction", page_icon="🐄", layout="wide")

# # ==========================
# # ACCESS CONTROL
# # ==========================
# if "token" not in st.session_state or st.session_state.token is None:
#     st.warning("⚠️ Please login to access this page.")
#     st.switch_page("pages/2_Login.py")

# # ==========================
# # SIDEBAR
# # ==========================
# with st.sidebar:
#     st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
#     st.header("🔍 Prediction Menu")

#     if st.button("🏠 Dashboard"):
#         st.switch_page("pages/5_Dashboard.py")

#     st.write("---")
#     if st.button("🚪 Logout"):
#         st.session_state.clear()
#         st.switch_page("pages/2_Login.py")


# # ==========================
# # MAIN PAGE
# # ==========================
# st.title("🐄 AI Breed Prediction")
# st.write("Upload a cattle image to identify the breed using our AI model.")

# uploaded_file = st.file_uploader(
#     "📤 Upload Cattle Image",
#     type=["jpg", "jpeg", "png"]
# )

# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#     with st.spinner("🔍 Analyzing image…"):
#         token = st.session_state.token
#         res = predict(token, uploaded_file)

#     if res is None:
#         st.error("❌ Unable to connect to server.")
#         st.stop()

#     if res.status_code != 200:
#         st.error(f"❌ Server Error: {res.text}")
#         st.stop()

#     data = res.json()

#     if "error" in data:
#         st.error(f"❌ Prediction Error: {data['error']}")
#         st.stop()

#     if "final_prediction" not in data or "top3_predictions" not in data:
#         st.error("❌ Invalid response from backend.")
#         st.write("Raw Response:", data)
#         st.stop()

#     # ==========================
#     # FINAL PREDICTION
#     # ==========================
#     st.markdown("---")
#     st.subheader("📌 Final Prediction")

#     final = data["final_prediction"]
#     st.success(
#         f"""### 🐮 {final['breed']}  
#         **Confidence:** {final['confidence']*100:.2f}%"""
#     )
   



#     # ==========================
#     # TOP 3 PREDICTIONS
#     # ==========================
#     st.markdown("---")
#     st.subheader("🏆 Top 3 Predictions")

#     for item in data["top3_predictions"]:
#         st.write(f"**{item['breed']}** — {item['confidence']*100:.2f}%")
#         st.progress(min(1.0, item["confidence"]))

import streamlit as st

st.set_page_config(page_title="Breed Prediction", page_icon="🔍")

if "token" not in st.session_state:
    st.switch_page("pages/2_Login.py")

st.title("🔍 Breed Prediction")

st.info("Model integration yaha aayega")

if st.button("⬅ Back to Dashboard"):
    st.switch_page("pages/5_Dashboard.py")

   
