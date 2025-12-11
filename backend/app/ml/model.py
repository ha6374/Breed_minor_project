# import json
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from app.core.config import settings

# # -----------------------------
# # Paths from config
# # -----------------------------
# MODEL_PATH = settings.MODEL_PATH
# LABELS_PATH = settings.LABELS_PATH

# # -----------------------------
# # Load class names
# # -----------------------------
# with open(LABELS_PATH, "r") as f:
#     CLASS_NAMES = json.load(f)

# NUM_CLASSES = len(CLASS_NAMES)

# # -----------------------------
# # Load ML Model
# # -----------------------------
# model = None

# def load_ml_model():
#     global model

#     if not MODEL_PATH.exists():
#         raise FileNotFoundError(f"❌ Model not found at {MODEL_PATH}")

#     print(f"📥 Loading ML model from: {MODEL_PATH}")
#     model = tf.keras.models.load_model(MODEL_PATH)
#     print("✅ ML model loaded successfully!")

# # -----------------------------
# # Preprocess Image
# # -----------------------------
# def preprocess_image(path):
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img)
#     arr = np.expand_dims(arr, axis=0)
#     return arr  # normalization already inside model

# # -----------------------------
# # Predict top 3
# # -----------------------------
# def predict_custom(img_path):
#     if model is None:
#         raise RuntimeError("⚠ Model not loaded. Call load_ml_model() first.")

#     img = preprocess_image(img_path)
#     preds = model.predict(img)[0]

#     top3 = preds.argsort()[-3:][::-1]

#     return [
#         {
#             "breed": CLASS_NAMES[str(i)],
#             "confidence": float(preds[i])
#         }
#         for i in top3
#     ]




# # -----------------------------
# # Final prediction
# # -----------------------------
# def final_prediction(custom_preds):
#     return max(custom_preds, key=lambda x: x["confidence"])



import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from app.core.config import settings

# -----------------------------
# Paths from config
# -----------------------------
MODEL_PATH = settings.MODEL_PATH
LABELS_PATH = settings.LABELS_PATH

# -----------------------------
# Load class names
# -----------------------------
with open(LABELS_PATH, "r") as f:
    CLASS_NAMES = json.load(f)  # {"0": "Gir", "1": "Sahiwal", ..., "N": "unknown"}

NUM_CLASSES = len(CLASS_NAMES)

# -----------------------------
# Load ML Model
# -----------------------------
model = None

def load_ml_model():
    global model

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"❌ Model not found at {MODEL_PATH}")

    print(f"📥 Loading ML model from: {MODEL_PATH}")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ ML model loaded successfully!")

# -----------------------------
# Preprocess Image
# -----------------------------
def preprocess_image(path):
    img = load_img(path, target_size=(224, 224))
    arr = img_to_array(img)
    arr = np.expand_dims(arr, axis=0)
    return arr  # model already has Rescaling layer

# -----------------------------
# Predict top 3
# -----------------------------
def predict_custom(img_path):
    if model is None:
        raise RuntimeError("⚠ Model not loaded. Call load_ml_model() first.")

    img = preprocess_image(img_path)
    preds = model.predict(img)[0]

    # Get top 3 predictions
    top3 = preds.argsort()[-3:][::-1]

    results = [
        {
            "breed": CLASS_NAMES[str(i)],
            "confidence": float(preds[i])
        }
        for i in top3
    ]

    return results

# -----------------------------
# Final prediction with threshold
# -----------------------------
# def final_prediction(custom_preds, threshold=0.60):
#     """
#     If 'unknown' has highest confidence OR best confidence < threshold:
#         return unknown
#     Otherwise return the best real breed
#     """
#     best = max(custom_preds, key=lambda x: x["confidence"])

#     # If top class is unknown → return unknown
#     if best["breed"].lower() == "unknown":
#         return {"breed": "unknown", "confidence": best["confidence"]}

#     # If model is not confident enough → unknown
#     if best["confidence"] < threshold:
#         return {"breed": "unknown", "confidence": best["confidence"]}

#     # Otherwise → return best breed
#     return best

def final_prediction(custom_preds):
    """
    Return the top prediction.
    Only return 'unknown' if the top predicted class is actually 'unknown'.
    """
    best = max(custom_preds, key=lambda x: x["confidence"])

    if best["breed"].lower() == "unknown":
        return {"breed": "unknown", "confidence": best["confidence"]}

    return best


