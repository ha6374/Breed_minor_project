
# # import numpy as np
# # from fastapi import APIRouter, UploadFile, File
# # from PIL import Image
# # import tensorflow as tf
# # import json
# # import io

# # router = APIRouter(prefix="/predict", tags=["Predict"])

# # MODEL_PATH = "custom_cnn_best.h5"   # ← Correct model
# # LABELS_PATH = "labels.json"

# # # Load model
# # model = tf.keras.models.load_model(MODEL_PATH)

# # # Load labels
# # with open(LABELS_PATH, "r") as f:
# #     labels = json.load(f)

# # labels = {int(k): v for k, v in labels.items()}

# # @router.post("/")
# # async def predict_animal(file: UploadFile = File(...)):
# #     img_bytes = await file.read()
# #     img = Image.open(io.BytesIO(img_bytes)).resize((224, 224))

# #     img = np.array(img) / 255.0
# #     img = np.expand_dims(img, axis=0)

# #     preds = model.predict(img)
    
# #     pred_index = int(np.argmax(preds))
# #     pred_label = labels[pred_index]
# #     confidence = float(np.max(preds))

# #     return {
# #         "breed": pred_label,
# #         "confidence": f"{confidence*100:.2f}%"
# #     }
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import load_ml_model, predict_custom, final_prediction
# import os, uuid

# router = APIRouter(prefix="/predict", tags=["Predict"])
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Load the model at server startup
# load_ml_model()

# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded file
#         file_bytes = await file.read()
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)
#         with open(filepath, "wb") as f:
#             f.write(file_bytes)

#         # Get predictions
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         return JSONResponse({
#             "custom_model": top3,
#             "final_prediction": best
#         })

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)

import os
import uuid
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.ml.model import predict_custom, final_prediction, load_ml_model

router = APIRouter(prefix="/predict", tags=["Predict"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load model on startup
load_ml_model()

@router.post("/")
async def predict_breed(file: UploadFile = File(...)):
    try:
        # Save uploaded image
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(await file.read())

        # Predict
        top3 = predict_custom(filepath)
        best = final_prediction(top3)

        return {
            "top3_predictions": top3,
            "final_prediction": best
        }

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
