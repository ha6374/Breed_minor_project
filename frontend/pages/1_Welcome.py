import streamlit as st
import time

st.set_page_config(
    page_title="Welcome | Pashudhan AI",
    page_icon="🐄",
    layout="wide"
)

st.markdown("""
    <div style="text-align:center; margin-top:80px;">
        <img src="https://i.imgur.com/9B1xU6X.gif" width="280">
        <h1 style="color:#4a4a4a; font-size:42px;">🐄 Pashudhan AI</h1>
        <p style="font-size:22px;">Smart Cattle Breed Prediction System</p>
    </div>
""", unsafe_allow_html=True)

time.sleep(2)

st.switch_page("2_Login")
