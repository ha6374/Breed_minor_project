# import os
# import uuid
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import predict_custom, final_prediction, load_ml_model

# router = APIRouter(prefix="/predict", tags=["Predict"])

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Load model on startup
# load_ml_model()

# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded image
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)

#         with open(filepath, "wb") as f:
#             f.write(await file.read())

#         # Predict
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         return {
#             "top3_predictions": top3,
#             "final_prediction": best
#         }

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)


# import os
# import uuid
# import numpy as np
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import predict_custom, final_prediction, load_ml_model, model, preprocess_image, CLASS_NAMES
# from tensorflow.keras.models import Model

# router = APIRouter(prefix="/predict", tags=["Predict"])

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # -----------------------------
# # Load model and prepare feature extractor
# # -----------------------------
# load_ml_model()
# feature_model = Model(inputs=model.input, outputs=model.layers[-2].output)  # last dense before softmax

# # Precompute centroids for each class (load from training embeddings if available)
# # For simplicity, we will just use softmax confidence threshold here
# CONFIDENCE_THRESHOLD = 0.6  # top-1 confidence < 0.6 → unknown

# # -----------------------------
# # Predict endpoint with OOD detection
# # -----------------------------
# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded image
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)

#         with open(filepath, "wb") as f:
#             f.write(await file.read())

#         # Predict top3 using current model
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         # --- OOD Check ---
#         if best['confidence'] < CONFIDENCE_THRESHOLD:
#             return JSONResponse(
#                 {"error": "❌ Please upload a cow or buffalo image only."},
#                 status_code=400
#             )

#         return {
#             "top3_predictions": top3,
#             "final_prediction": best
#         }

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)


# # import os
# # import uuid
# # import numpy as np
# # import tensorflow as tf
# # from fastapi import APIRouter, UploadFile, File
# # from fastapi.responses import JSONResponse
# # from app.ml.model import load_ml_model, preprocess_image, CLASS_NAMES, model

# # router = APIRouter(prefix="/predict", tags=["Predict"])

# # UPLOAD_DIR = "uploads"
# # os.makedirs(UPLOAD_DIR, exist_ok=True)

# # # ===============================
# # # 1. Compute centroids for OOD
# # # ===============================
# # # We use the model's penultimate layer as embeddings
# # # Load precomputed centroids if already saved, else compute
# # CENTROIDS_PATH = "app/ml/centroids.npy"
# # if os.path.exists(CENTROIDS_PATH):
# #     centroids = np.load(CENTROIDS_PATH, allow_pickle=True).item()
# # else:
# #     # Compute centroids from your training dataset
# #     # TRAIN_DIR should have subfolders for each breed
# #     from tensorflow.keras.preprocessing.image import load_img, img_to_array
# #     from pathlib import Path

# #     TRAIN_DIR = Path(r"C:\Users\HARSH\AI_breed_app\backend\IndianCattleBuffaloeBreeds-Dataset\breeds\train")
# #     centroids = {}

# #     # Create a feature extractor model
# #     feature_model = tf.keras.Model(inputs=model.input, outputs=model.layers[-2].output)

# #     for breed_folder in TRAIN_DIR.iterdir():
# #         if breed_folder.is_dir():
# #             breed_name = breed_folder.name
# #             embeddings = []
# #             for img_file in breed_folder.glob("*.*"):
# #                 img = load_img(img_file, target_size=(224,224))
# #                 arr = img_to_array(img)/255.0
# #                 arr = np.expand_dims(arr, axis=0)
# #                 emb = feature_model.predict(arr)
# #                 embeddings.append(emb[0])
# #             centroids[breed_name] = np.mean(embeddings, axis=0)
# #     # Save centroids for future
# #     np.save(CENTROIDS_PATH, centroids)

# # # Threshold for unknown detection
# # OOD_THRESHOLD = 1.0  # adjust based on validation

# # # Feature extractor
# # feature_model = tf.keras.Model(inputs=model.input, outputs=model.layers[-2].output)

# # # ===============================
# # # 2. Prediction endpoint
# # # ===============================
# # @router.post("/")
# # async def predict_breed(file: UploadFile = File(...)):
# #     try:
# #         # Save uploaded image
# #         filename = f"{uuid.uuid4()}.jpg"
# #         filepath = os.path.join(UPLOAD_DIR, filename)

# #         with open(filepath, "wb") as f:
# #             f.write(await file.read())

# #         # ----------------------
# #         # Compute embedding
# #         # ----------------------
# #         img = preprocess_image(filepath)/255.0
# #         emb = feature_model.predict(img)[0]

# #         # ----------------------
# #         # Compute distances to centroids
# #         # ----------------------
# #         distances = {}
# #         for breed, centroid in centroids.items():
# #             dist = np.linalg.norm(emb - centroid)
# #             distances[breed] = dist

# #         # Find closest breed
# #         closest_breed = min(distances, key=distances.get)
# #         min_dist = distances[closest_breed]

# #         if min_dist > OOD_THRESHOLD:
# #             # Image not from known cattle breeds
# #             return JSONResponse({"error": "Please upload a cow or buffalo image."}, status_code=400)

# #         # ----------------------
# #         # Normal prediction
# #         # ----------------------
# #         preds = model.predict(img)[0]
# #         top3_idx = preds.argsort()[-3:][::-1]
# #         top3 = [
# #             {"breed": CLASS_NAMES[str(i)], "confidence": float(preds[i])}
# #             for i in top3_idx
# #         ]
# #         final = max(top3, key=lambda x: x["confidence"])

# #         return {"top3_predictions": top3, "final_prediction": final}

# #     except Exception as e:
# #         return JSONResponse({"error": str(e)}, status_code=500)



# import os
# import uuid
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import predict_custom, final_prediction, load_ml_model, CLASS_NAMES

# router = APIRouter(prefix="/predict", tags=["Predict"])

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Load model at startup
# load_ml_model()

# # Threshold for unknown images
# CONFIDENCE_THRESHOLD = 0.5  # tune this

# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded image
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)
#         with open(filepath, "wb") as f:
#             f.write(await file.read())

#         # Predict
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         # Check if prediction is valid cow/buffalo breed
#         valid_breeds = [
#             "Alambadi","Amritmahal","Ayrshire","Banni","Bargur","Bhadawari","Brown_Swiss",
#             "Dangi","Deoni","Gir","Guernsey","Hallikar","Hariana","Holstein_Friesian",
#             "Jaffrabadi","Jersey","Kangayam","Kankrej","Kasargod","Kenkatha","Kherigarh",
#             "Khillari","Krishna_Valley","Malnad_gidda","Mehsana","Murrah","Nagori","Nagpuri",
#             "Nili_Ravi","Nimari","Ongole","Pulikulam","Rathi","Red_Dane","Red_Sindhi",
#             "Sahiwal","Surti","Tharparkar","Toda","Umblachery","Vechur"
#         ]

#         # If top prediction not valid OR confidence too low → return error
#         if best["breed"] not in valid_breeds or best["confidence"] < CONFIDENCE_THRESHOLD:
#             return JSONResponse(
#                 {"error": "❌ Please upload a cow or buffalo image."},
#                 status_code=400
#             )

#         return {
#             "top3_predictions": top3,
#             "final_prediction": best
#         }

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)



# import os
# import uuid
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import predict_custom, final_prediction, load_ml_model

# router = APIRouter(prefix="/predict", tags=["Predict"])

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Load model on startup
# load_ml_model()

# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded image
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)

#         with open(filepath, "wb") as f:
#             f.write(await file.read())

#         # Predict
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         # If best is unknown → return stable output
#         if best["breed"].lower() == "unknown":
#             return {
#                 "breed": "unknown",
#                 "confidence": best["confidence"],
#                 "top3_predictions": top3,
#                 "message": "Image does not match any known breed."
#             }

#         return {
    
#             "breed": best["breed"],
#             "confidence": best["confidence"],
#             "top3_predictions": top3
#         }

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)


# import os
# import uuid
# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.ml.model import predict_custom, final_prediction, load_ml_model

# router = APIRouter(prefix="/predict", tags=["Predict"])

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Load model on startup
# load_ml_model()

# @router.post("/")
# async def predict_breed(file: UploadFile = File(...)):
#     try:
#         # Save uploaded image
#         filename = f"{uuid.uuid4()}.jpg"
#         filepath = os.path.join(UPLOAD_DIR, filename)

#         with open(filepath, "wb") as f:
#             f.write(await file.read())

#         # Predict
#         top3 = predict_custom(filepath)
#         best = final_prediction(top3)

#         # Build response dictionary
#         response = {
#             "final_prediction": best,
#             "top3_predictions": top3
#         }

#         # Optional: Add message if unknown
#         if best["breed"].lower() == "unknown":
#             response["message"] = "Image does not match any known breed."

#         return response

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)
import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.ml.model import predict_custom, final_prediction, load_ml_model

router = APIRouter(prefix="/predict", tags=["Predict"])

# ---------------- CONFIG ---------------- #
UPLOAD_DIR = "uploads"
CONFIDENCE_THRESHOLD = 0.45   # ⭐ IMPORTANT
ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load model once on startup
load_ml_model()

# --------------------------------------- #

@router.post("/")
async def predict_breed(file: UploadFile = File(...)):
    try:
        # --------- FILE VALIDATION --------- #
        ext = file.filename.split(".")[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Invalid file format. Upload jpg, jpeg or png image."
            )

        # --------- SAVE IMAGE --------- #
        filename = f"{uuid.uuid4()}.{ext}"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(await file.read())

        # --------- MODEL PREDICTION --------- #
        top3 = predict_custom(filepath)
        best = final_prediction(top3)

        breed = best.get("breed", "unknown")
        confidence = float(best.get("confidence", 0.0))

        # --------- UNKNOWN HANDLING --------- #
        if confidence < CONFIDENCE_THRESHOLD:
            response = {
                "breed": "Unknown",
                "confidence": confidence,
                "top3_predictions": top3,
                "message": "Breed could not be confidently identified."
            }
        else:
            response = {
                "breed": breed,
                "confidence": confidence,
                "top3_predictions": top3
            }

        # --------- CLEANUP IMAGE --------- #
        if os.path.exists(filepath):
            os.remove(filepath)

        return response

    except HTTPException as e:
        raise e

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Prediction failed", "details": str(e)}
        )
