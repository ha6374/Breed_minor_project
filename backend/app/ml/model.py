
# import os
# import json
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from tensorflow.keras.applications.mobilenet_v2 import (
#     MobileNetV2, preprocess_input, decode_predictions
# )
# from app.core.config import settings

# # ----------------------------- 1. LOAD LABELS -----------------------------
# with open(settings.LABELS_PATH, "r") as f:
#     labels_raw = json.load(f)

# # Convert "0": "breed" → 0: "breed"
# LABELS = {int(k): v for k, v in labels_raw.items()}
# NUM_CLASSES = len(LABELS)

# # Confidence threshold for "Not a Cattle"
# CONFIDENCE_THRESHOLD = 0.50  # 50%


# # ----------------------------- 2. BUILD CUSTOM CNN -----------------------------
# def build_custom_cnn() -> models.Model:
#     """Rebuilds the original custom CNN architecture."""
#     model = models.Sequential([
#         layers.Rescaling(1./255, input_shape=(224, 224, 3)),
#         layers.Conv2D(32, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),

#         layers.Conv2D(64, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),

#         layers.Conv2D(128, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),

#         layers.Flatten(),
#         layers.Dense(128, activation="relu"),
#         layers.Dropout(0.3),

#         layers.Dense(NUM_CLASSES, activation="softmax"),
#     ])

#     model.compile(
#         optimizer="adam",
#         loss="sparse_categorical_crossentropy",
#         metrics=["accuracy"],
#     )
#     return model


# # ----------------------------- 3. LOAD MODELS -----------------------------
# custom_model: models.Model | None = None
# pretrained_model: models.Model | None = None

# def load_ml_model():
#     """Loads custom CNN and MobileNetV2 models."""
#     global custom_model, pretrained_model

#     print(f"➡ Loading Custom CNN weights from: {settings.MODEL_PATH}")
#     custom_model = build_custom_cnn()
#     custom_model.load_weights(settings.MODEL_PATH)
#     print("✅ Custom CNN loaded!")

#     pretrained_model = MobileNetV2(weights="imagenet")
#     print("✅ MobileNetV2 loaded!")
#     print("🎉 All models loaded successfully.")


# # ----------------------------- 4. IMAGE PREPROCESSING -----------------------------
# def preprocess_image(path: str) -> np.ndarray:
#     """Prepare image for custom CNN."""
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img) / 255.0
#     return np.expand_dims(arr, axis=0)


# def preprocess_image_mobilenet(path: str) -> np.ndarray:
#     """Prepare image for MobileNetV2."""
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img)
#     arr = preprocess_input(arr)
#     return np.expand_dims(arr, axis=0)


# # ----------------------------- 5. PREDICTORS -----------------------------
# def predict_custom(path: str) -> list[dict]:
#     img = preprocess_image(path)
#     preds = custom_model.predict(img)[0]
#     top3_idx = preds.argsort()[-3:][::-1]

#     return [
#         {"breed": LABELS[i], "confidence": float(preds[i])}
#         for i in top3_idx
#     ]


# def predict_pretrained(path: str) -> list[dict]:
#     img = preprocess_image_mobilenet(path)
#     preds = pretrained_model.predict(img)

#     d = decode_predictions(preds, top=3)[0]

#     return [
#         {"breed": breed, "confidence": float(score)}
#         for (_, breed, score) in d
#     ]


# # ----------------------------- 6. MERGE PREDICTIONS -----------------------------
# # def final_prediction(custom_preds: list[dict], pretrained_preds: list[dict]) -> dict:
# #     """Returns best prediction. If confidence too low, return 'Not a Cattle'."""
# #     all_preds = custom_preds + pretrained_preds
# #     best = max(all_preds, key=lambda x: x["confidence"])

# #     if best["confidence"] < CONFIDENCE_THRESHOLD:
# #         return {"breed": "Not a Cattle", "confidence": float(best["confidence"])}
# #     return best 

# def final_prediction(custom_preds: list[dict], pretrained_preds: list[dict] = None) -> dict:
#     """
#     Returns best prediction based only on custom CNN.
#     If confidence too low, return 'Not a Cattle'.
#     """
#     if not custom_preds:
#         return {"breed": "Not a Cattle", "confidence": 0.0}

#     best = max(custom_preds, key=lambda x: x["confidence"])

#     if best["confidence"] < 0.50:
#         return {"breed": "Not a Cattle", "confidence": float(best["confidence"])}

#     return best


# import os
# import json
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from tensorflow.keras.applications.mobilenet_v2 import (
#     MobileNetV2, preprocess_input, decode_predictions
# )
# from app.core.config import settings

# # ------------------------ Load Labels ------------------------
# with open(settings.LABELS_PATH, "r") as f:
#     labels_raw = json.load(f)
# LABELS = {int(k): v for k, v in labels_raw.items()}
# NUM_CLASSES = len(LABELS)

# # ------------------------ Custom CNN ------------------------
# def build_custom_cnn():
#     model = models.Sequential([
#         layers.Rescaling(1./255, input_shape=(224, 224, 3)),
#         layers.Conv2D(32, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),
#         layers.Conv2D(64, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),
#         layers.Conv2D(128, (3, 3), activation="relu"),
#         layers.MaxPooling2D(2, 2),
#         layers.Flatten(),
#         layers.Dense(128, activation="relu"),
#         layers.Dropout(0.3),
#         layers.Dense(NUM_CLASSES, activation="softmax"),
#     ])
#     model.compile(
#         optimizer="adam",
#         loss="sparse_categorical_crossentropy",
#         metrics=["accuracy"],
#     )
#     return model

# # ------------------------ Load Models ------------------------
# custom_model = None
# pretrained_model = None

# def load_ml_model():
#     global custom_model, pretrained_model

#     print(f"➡ Loading Custom CNN weights from: {settings.MODEL_PATH}")
#     custom_model = build_custom_cnn()
#     custom_model.load_weights(settings.MODEL_PATH)
#     print("✅ Custom CNN loaded!")

#     pretrained_model = MobileNetV2(weights="imagenet")
#     print("✅ MobileNetV2 loaded!")
#     print("🎉 All models loaded successfully.")

# # ------------------------ Preprocessing ------------------------
# def preprocess_image(path):
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img) / 255.0
#     return np.expand_dims(arr, axis=0)

# def preprocess_image_mobilenet(path):
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img)
#     arr = preprocess_input(arr)
#     return np.expand_dims(arr, axis=0)

# # ------------------------ Prediction ------------------------
# def predict_custom(path):
#     img = preprocess_image(path)
#     preds = custom_model.predict(img)[0]
#     top3_idx = preds.argsort()[-3:][::-1]
#     return [{"breed": LABELS[i], "confidence": float(preds[i])} for i in top3_idx]

# def predict_pretrained(path):
#     img = preprocess_image_mobilenet(path)
#     preds = pretrained_model.predict(img)
#     decoded = decode_predictions(preds, top=3)[0]
#     return [{"breed": breed, "confidence": float(score)} for (_, breed, score) in decoded]

# # ------------------------ Cattle Filter ------------------------
# CATTLE_CLASSES = ["ox", "oxcart", "water_buffalo", "cow", "zebu"]
# CATTLE_THRESHOLD = 0.3

# def predict_final(image_path):
#     # Custom CNN prediction
#     custom_preds = predict_custom(image_path)
#     top_custom = custom_preds[0]

#     # MobileNetV2 check
#     pretrained_preds = predict_pretrained(image_path)
#     cattle_conf = max([p["confidence"] for p in pretrained_preds if p["breed"] in CATTLE_CLASSES], default=0)

#     # Final decision
#     if cattle_conf >= CATTLE_THRESHOLD:
#         return {
#             "final_prediction": top_custom,
#             "custom_model": custom_preds,
#             "pretrained_model": pretrained_preds
#         }
#     else:
#         return {
#             "final_prediction": {"breed": "Not a Cattle", "confidence": 1.0},
#             "custom_model": custom_preds,
#             "pretrained_model": pretrained_preds
#         }

# app/ml/model.py
# import os
# import json
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from app.core.config import settings

# # Load class names
# with open(settings.LABELS_PATH, "r") as f:
#     CLASS_NAMES = json.load(f)

# NUM_CLASSES = len(CLASS_NAMES)

# # -----------------------------
# # Load FULL MODEL (not just weights)
# # -----------------------------
# model = None

# def load_ml_model():
#     global model
#     model = tf.keras.models.load_model(settings.MODEL_PATH)
#     print("✅ Loaded FULL fine-tuned MobileNetV2 model!")

# # -----------------------------
# # Preprocess image
# # -----------------------------
# def preprocess_image(path):
#     img = load_img(path, target_size=(224, 224))
#     arr = img_to_array(img)
#     arr = np.expand_dims(arr, axis=0)
#     return arr   # rescaling is inside model

# # -----------------------------
# # Predict top 3
# # -----------------------------
# def predict_custom(img_path):
#     if model is None:
#         raise RuntimeError("Model not loaded.")

#     img = preprocess_image(img_path)
#     preds = model.predict(img)[0]

#     top3 = preds.argsort()[-3:][::-1]

#     return [
#         {"breed": CLASS_NAMES[str(i)], "confidence": float(preds[i])}
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
    CLASS_NAMES = json.load(f)

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
    return arr  # normalization already inside model

# -----------------------------
# Predict top 3
# -----------------------------
def predict_custom(img_path):
    if model is None:
        raise RuntimeError("⚠ Model not loaded. Call load_ml_model() first.")

    img = preprocess_image(img_path)
    preds = model.predict(img)[0]

    top3 = preds.argsort()[-3:][::-1]

    return [
        {
            "breed": CLASS_NAMES[str(i)],
            "confidence": float(preds[i])
        }
        for i in top3
    ]

# -----------------------------
# Final prediction
# -----------------------------
def final_prediction(custom_preds):
    return max(custom_preds, key=lambda x: x["confidence"])
