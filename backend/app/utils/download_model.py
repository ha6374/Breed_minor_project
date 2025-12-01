import os
from pathlib import Path
import gdown
from app.ml.model import MODEL_PATH, LABELS_PATH

MODELS_DIR = Path(MODEL_PATH).parent
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Google Drive direct download URLs
MODEL_LINKS = {
    "custom_cnn_best.h5": "https://drive.google.com/uc?export=download&id=1gUD3IqwR_7UK0exoCkCdjquFoDsWkWB8",
    "fine_tuned_model.h5": "https://drive.google.com/uc?export=download&id=1tG0nPBV4BdDUvQP2Hq7UJZQg5-DCyYdq",
    "labels.json": "https://drive.google.com/uc?export=download&id=1feEqBS6UtFBBdOEBCzaQXHsFjbbAScVi"
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
