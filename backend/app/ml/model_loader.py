# import os
# from pathlib import Path
# import gdown
# import json
# from tensorflow.keras.models import load_model

# # -----------------------------
# # Directories & paths
# # -----------------------------
# BASE_DIR = Path(__file__).parent.parent
# MODELS_DIR = BASE_DIR / "models"
# MODELS_DIR.mkdir(parents=True, exist_ok=True)

# MODEL_PATH = MODELS_DIR / "fine_tuned_model.h5"
# CUSTOM_MODEL_PATH = MODELS_DIR / "custom_cnn_best.h5"
# LABELS_PATH = MODELS_DIR / "labels.json"

# # -----------------------------
# # Google Drive download links
# # -----------------------------
# MODEL_LINKS = {
#     "custom_cnn_best.h5": "https://drive.google.com/uc?export=download&id=1gUD3IqwR_7UK0exoCkCdjquFoDsWkWB8",
#     "fine_tuned_model.h5": "https://drive.google.com/uc?export=download&id=1tG0nPBV4BdDUvQP2Hq7UJZQg5-DCyYdq",
#     # अगर labels.json भी Drive पर है तो add कर सकते हो
#     # "labels.json": "https://drive.google.com/uc?export=download&id=YOUR_LABELS_FILE_ID",
# }

# # -----------------------------
# # Download files if missing
# # -----------------------------
# def download_models():
#     for fname, url in MODEL_LINKS.items():
#         local_path = MODELS_DIR / fname
#         if not local_path.exists():
#             print(f"⬇ Downloading {fname} …")
#             try:
#                 gdown.download(url, str(local_path), quiet=False)
#                 print(f"✅ Downloaded {fname}")
#             except Exception as e:
#                 print(f"❌ Failed to download {fname}: {e}")
#                 raise
#         else:
#             print(f"✅ {fname} already exists, skipping download.")

# # -----------------------------
# # Load labels
# # -----------------------------
# def load_labels():
#     if not LABELS_PATH.exists():
#         raise FileNotFoundError(f"❌ Labels file not found at {LABELS_PATH}")
#     with open(LABELS_PATH, "r") as f:
#         labels = json.load(f)
#     print(f"✅ Loaded {len(labels)} classes from labels.json")
#     return labels

# # -----------------------------
# # Load ML model
# # -----------------------------
# def load_ml_model(model_path=MODEL_PATH):
#     if not model_path.exists():
#         raise FileNotFoundError(f"❌ Model not found at {model_path}")
#     print(f"📥 Loading ML model from: {model_path}")
#     model = load_model(model_path)
#     print("✅ ML model loaded successfully!")
#     return model

# # -----------------------------
# # Startup helper
# # -----------------------------
# def load_models_on_startup():
#     download_models()
#     labels = load_labels()
#     model = load_ml_model()
#     return model, labels

# # -----------------------------
# # Run standalone
# # -----------------------------
# if __name__ == "__main__":
#     model, labels = load_models_on_startup()
#     print("✅ All models and labels are ready!")
#     print(f"Available classes: {list(labels.values())}")


import os
from pathlib import Path
import gdown
from app.ml.model import MODEL_PATH, LABELS_PATH

MODELS_DIR = Path(MODEL_PATH).parent
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Google Drive direct download URLs
MODEL_LINKS = {
    "custom_cnn_best.h5": "https://drive.google.com/uc?export=download&id=1gUD3IqwR_7UK0exoCkCdjquFoDsWkWB8",
    "fine_tuned_model.h5": "https://drive.google.com/uc?export=download&id=1tG0nPBV4BdDUvQP2Hq7UJZQg5-DCyYdq"
    # "labels.json": "https://drive.google.com/uc?export=download&id=1tG0nPBV4BdDUvQP2Hq7UJZQg5-DCyYdq"  # अगर अलग है तो सही link लगाएँ
}

def download_models():
    for fname, url in MODEL_LINKS.items():
        local_path = MODELS_DIR / fname
        if not local_path.exists():
            print(f"⬇ Downloading {fname} …")
            gdown.download(url, str(local_path), quiet=False)
            print(f"✅ Downloaded {fname}")

def load_models_on_startup():
    download_models()
