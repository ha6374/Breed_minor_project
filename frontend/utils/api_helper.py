# import requests

# # BACKEND_URL = "http://127.0.0.1:8000/api/v1"
# BACKEND_URL = "https://breed-minor-project.onrender.com/api/v1"

# # --- AUTH ---
# def signup(username: str, email: str, password: str):
#     try:
#         return requests.post(
#             f"{BACKEND_URL}/auth/signup",
#             json={"username": username, "email": email, "password": password},
#             timeout=10,
#         )
#     except Exception as e:
#         print("Signup error:", e)
#         return None

# def login(email: str, password: str):
#     try:
#         return requests.post(
#             f"{BACKEND_URL}/auth/login",
#             data={"username": email, "password": password},
#             timeout=10,
#         )
#     except Exception as e:
#         print("Login error:", e)
#         return None

# # --- FORGOT / RESET PASSWORD ---
# def forgot_password(email: str):
#     """
#     Tries to request a password reset for `email`.
#     Backend should expose something like POST /auth/forgot-password with JSON {"email": "..."}
#     """
#     try:
#         return requests.post(f"{BACKEND_URL}/auth/forgot-password", json={"email": email}, timeout=10)
#     except Exception as e:
#         print("Forgot password error:", e)
#         return None

# def reset_password(token: str, new_password: str):
#     """
#     If your backend supports a reset token flow, this function can be used by a reset page.
#     POST /auth/reset-password with {"token": "...", "password": "..."}
#     """
#     try:
#         return requests.post(f"{BACKEND_URL}/auth/reset-password", json={"token": token, "password": new_password}, timeout=10)
#     except Exception as e:
#         print("Reset password error:", e)
#         return None

# # --- PROFILE ---
# def get_user_profile(token: str):
#     try:
#         headers = {"Authorization": f"Bearer {token}"}
#         res = requests.get(f"{BACKEND_URL}/auth/profile", headers=headers, timeout=10)
#         if res.status_code == 200:
#             return res.json()
#         return None
#     except Exception as e:
#         print("Profile error:", e)
#         return None

# def update_user_profile(token: str, data: dict):
#     try:
#         headers = {"Authorization": f"Bearer {token}"}
#         res = requests.put(f"{BACKEND_URL}/auth/profile", headers=headers, json=data, timeout=10)
#         return res
#     except Exception as e:
#         print("Profile update error:", e)
#         return None

# # --- PREDICTION ---
# def predict(token: str, image_file):
#     try:
#         headers = {"Authorization": f"Bearer {token}"} if token else {}
#         files = {"file": (image_file.name, image_file.getvalue(), image_file.type)}
#         res = requests.post(f"{BACKEND_URL}/predict/", files=files, headers=headers, timeout=30)
#         return res
#     except Exception as e:
#         print("Prediction error:", e)
#         return None

# # --- UPLOAD PROFILE IMAGE ---
# def upload_profile_image(token: str, image_file):
#     try:
#         headers = {"Authorization": f"Bearer {token}"}
#         files = {"file": (image_file.name, image_file.getvalue(), image_file.type)}
#         res = requests.post(f"{BACKEND_URL}/auth/profile/image", headers=headers, files=files, timeout=15)
#         if res.status_code in (200, 201):
#             return res.json()
#         return None
#     except Exception as e:
#         print("Profile upload error:", e)
#         return None

import requests

BASE_URL = "https://breed-minor-project.onrender.com/api/v1"


def handle_response(response):
    try:
        data = response.json()
    except Exception:
        data = {}

    if response.status_code in [200, 201]:
        return True, data
    else:
        message = data.get("detail") or data.get("message") or "Something went wrong"
        return False, message


def signup_api(payload):
    response = requests.post(f"{BASE_URL}/auth/signup", json=payload)
    return handle_response(response)


def login_api(payload):
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    return handle_response(response)


def forgot_password_api(payload):
    response = requests.post(f"{BASE_URL}/auth/forgot-password", json=payload)
    return handle_response(response)


def reset_password_api(token, payload):
    response = requests.post(
        f"{BASE_URL}/auth/reset-password?token={token}", json=payload
    )
    return handle_response(response)


def get_profile_api(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
    return handle_response(response)


def upload_profile_image_api(token, file):
    headers = {"Authorization": f"Bearer {token}"}
    files = {"file": file}
    response = requests.post(
        f"{BASE_URL}/auth/profile/image", headers=headers, files=files
    )
    return handle_response(response)


def predict_breed_api(token, file):
    headers = {"Authorization": f"Bearer {token}"}
    files = {"file": file}
    response = requests.post(
        f"{BASE_URL}/predict/breed", headers=headers, files=files
    )
    return handle_response(response)
