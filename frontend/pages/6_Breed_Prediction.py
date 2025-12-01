

# import streamlit as st
# from utils.api_helper import predict

# st.set_page_config(page_title="Breed Prediction", layout="wide")

# # require login
# if "token" not in st.session_state or st.session_state.token is None:
#     st.warning("Please login to access this page.")
#     st.session_state.page = "login"
#     st.rerun()

# st.title("🐄 Breed Prediction")

# uploaded_file = st.file_uploader("Upload cattle image (jpg/png/jpeg)", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Uploaded image", use_container_width=True)

#     # correct token
#     token = st.session_state.get("token")

#     if not token:
#         st.error("You must login first!")
#     else:
#         with st.spinner("Running prediction..."):
#             res = predict(token, uploaded_file)

#         if res is None:
#             st.error("No response from server")

#         elif res.status_code == 200:
#             st.write("DEBUG RESPONSE:", res.text)

#             data = res.json()

#             # --- FIX: normalize backend response ---
#             if isinstance(data, dict):
#                 if "breed" in data or "label" in data:
#                     preds = [data]   # single object → list
#                 else:
#                     preds = data.get("predictions", [])
#             elif isinstance(data, list):
#                 preds = data
#             else:
#                 preds = []

#             st.success("Prediction complete")

#             # --- Displaying predictions ---
#             for p in preds:
#                 label = p.get("label") or p.get("breed") or str(p)

#                 conf_raw = p.get("confidence", 0)

#                 # convert "9.77%" → 9.77
#                 try:
#                     if isinstance(conf_raw, str) and conf_raw.endswith("%"):
#                         conf = float(conf_raw.replace("%", ""))
#                     else:
#                         conf = float(conf_raw)
#                 except:
#                     conf = 0

#                 st.write(f"**{label}** — {conf:.2f}%")
#                 st.progress(min(conf / 100, 1.0))

#         else:
#             st.error(f"Prediction failed: {res.status_code}")
#             st.write(res.text)

# import streamlit as st
# from utils.api_helper import predict

# st.title("🐄 AI Breed Prediction")

# uploaded_file = st.file_uploader("Upload Cattle Image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     # st.image(uploaded_file, caption="Uploaded Image", width=None)
#     # st.image(uploaded_file, caption="Uploaded Image", width="stretch")
#     st.image(uploaded_file, caption="Uploaded image", use_container_width=True)


#     with st.spinner("Analyzing..."):
#         res = predict(st.session_state.token, uploaded_file)

#     # --------------------------
#     # Handle network errors
#     # --------------------------
#     if res is None:
#         st.error("❌ Unable to connect to server.")
#         st.stop()

#     # --------------------------
#     # Handle bad status codes
#     # --------------------------
#     if res.status_code != 200:
#         st.error(f"❌ Server Error: {res.text}")
#         st.stop()

#     data = res.json()

#     # --------------------------
#     # Handle backend error JSON
#     # --------------------------
#     if "error" in data:
#         st.error(f"❌ Prediction Error: {data['error']}")
#         st.stop()

#     # --------------------------
#     # Check required keys
#     # --------------------------
#     if "final_prediction" not in data or "custom_model" not in data:
#         st.error("❌ Invalid response from backend.")
#         st.write("Raw Response:", data)
#         st.stop()

#     # --------------------------
#     # Show Final Prediction
#     # --------------------------
#     st.subheader("📌 Final Prediction")
#     best = data["final_prediction"]
#     st.success(f"**{best['breed']}** — {best['confidence']*100:.2f}%")

#     st.markdown("---")

#     # --------------------------
#     # Show Custom Model Top-3
#     # --------------------------
#     st.subheader("🧠 Custom Model (Top 3)")
#     for item in data["custom_model"]:
#         st.write(f"**{item['breed']}** — {item['confidence']*100:.2f}%")
#         st.progress(min(1.0, item["confidence"]))

#     st.markdown("---")


# import streamlit as st
# from utils.api_helper import predict

# st.set_page_config(page_title="Breed Prediction", layout="wide")

# # --------------------------
# # Initialize token
# # --------------------------
# if "token" not in st.session_state:
#     st.session_state.token = None

# # --------------------------
# # Require login
# # --------------------------
# if st.session_state.token is None:
#     st.warning("⚠️ Please login to access this page.")
#     st.session_state.page = "login"
#     st.stop()  # Stop execution if not logged in

# st.title("🐄 AI Breed Prediction")

# # --------------------------
# # File uploader
# # --------------------------
# uploaded_file = st.file_uploader("Upload Cattle Image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#     # --------------------------
#     # Make prediction
#     # --------------------------
#     with st.spinner("Analyzing..."):
#         token = st.session_state.token  # get token from session state
#         res = predict(token, uploaded_file)

#     # --------------------------
#     # Handle network errors
#     # --------------------------
#     if res is None:
#         st.error("❌ Unable to connect to server.")
#         st.stop()

#     # --------------------------
#     # Handle bad status codes
#     # --------------------------
#     if res.status_code != 200:
#         st.error(f"❌ Server Error: {res.text}")
#         st.stop()

#     data = res.json()

#     # --------------------------
#     # Handle backend error JSON
#     # --------------------------
#     if "error" in data:
#         st.error(f"❌ Prediction Error: {data['error']}")
#         st.stop()

#     # --------------------------
#     # Check required keys
#     # --------------------------
#     if "final_prediction" not in data or "top3_predictions" not in data:
#         st.error("❌ Invalid response from backend.")
#         st.write("Raw Response:", data)
#         st.stop()
#     # --------------------------
#     # Show Final Prediction
#     # --------------------------
#     st.subheader("📌 Final Prediction")
#     best = data["top3_predictions"]
#     st.success(f"**{best['breed']}** — {best['confidence']*100:.2f}%")

#     st.markdown("---")

#     # --------------------------
#     # Show Custom Model Top-3
#     # --------------------------
#     st.subheader("🧠 Custom Model (Top 3)")
#     for item in data["custom_model"]:
#         st.write(f"**{item['breed']}** — {item['confidence']*100:.2f}%")
#         st.progress(min(1.0, item["confidence"]))

#     st.markdown("---")


# import streamlit as st
# from utils.api_helper import predict

# st.set_page_config(page_title="Breed Prediction", layout="wide")

# if "token" not in st.session_state or st.session_state.token is None:
#     st.warning("⚠️ Please login to access this page.")
#     st.stop()

# st.title("🐄 AI Breed Prediction")

# uploaded_file = st.file_uploader("Upload Cattle Image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#     with st.spinner("Analyzing..."):
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

#     # Show Final Prediction
#     st.subheader("📌 Final Prediction")
#     final = data["final_prediction"]
#     st.success(f"**{final['breed']}** — {final['confidence']*100:.2f}%")

#     st.markdown("---")

#     # Top-3 Predictions
#     st.subheader("🧠 Top 3 Predictions")
#     for item in data["top3_predictions"]:
#         st.write(f"**{item['breed']}** — {item['confidence']*100:.2f}%")
#         st.progress(min(1.0, item["confidence"]))


import streamlit as st
from utils.api_helper import predict

st.set_page_config(page_title="Breed Prediction", page_icon="🐄", layout="wide")

# ==========================
# ACCESS CONTROL
# ==========================
if "token" not in st.session_state or st.session_state.token is None:
    st.warning("⚠️ Please login to access this page.")
    st.switch_page("pages/2_Login.py")

# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.image("https://i.imgur.com/9B1xU6X.gif", width=120)
    st.header("🔍 Prediction Menu")

    if st.button("🏠 Dashboard"):
        st.switch_page("pages/5_Dashboard.py")

    st.write("---")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/2_Login.py")


# ==========================
# MAIN PAGE
# ==========================
st.title("🐄 AI Breed Prediction")
st.write("Upload a cattle image to identify the breed using our AI model.")

uploaded_file = st.file_uploader(
    "📤 Upload Cattle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Analyzing image…"):
        token = st.session_state.token
        res = predict(token, uploaded_file)

    if res is None:
        st.error("❌ Unable to connect to server.")
        st.stop()

    if res.status_code != 200:
        st.error(f"❌ Server Error: {res.text}")
        st.stop()

    data = res.json()

    if "error" in data:
        st.error(f"❌ Prediction Error: {data['error']}")
        st.stop()

    if "final_prediction" not in data or "top3_predictions" not in data:
        st.error("❌ Invalid response from backend.")
        st.write("Raw Response:", data)
        st.stop()

    # ==========================
    # FINAL PREDICTION
    # ==========================
    st.markdown("---")
    st.subheader("📌 Final Prediction")

    final = data["final_prediction"]
    st.success(
        f"""### 🐮 {final['breed']}  
        **Confidence:** {final['confidence']*100:.2f}%"""
    )

    # ==========================
    # TOP 3 PREDICTIONS
    # ==========================
    st.markdown("---")
    st.subheader("🏆 Top 3 Predictions")

    for item in data["top3_predictions"]:
        st.write(f"**{item['breed']}** — {item['confidence']*100:.2f}%")
        st.progress(min(1.0, item["confidence"]))
