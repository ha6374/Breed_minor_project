from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import init_db
from app.ml.model import load_ml_model
from app.utils.download_model import load_models_on_startup
from app.api import auth, predict

app = FastAPI(
    title="PashuBreed AI",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
)

# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def startup_event():
    # 1. Download models if not present
    load_models_on_startup()
    
    # 2. Load ML model into memory
    load_ml_model()

    # 3. Initialize database
    init_db()

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(predict.router, prefix="/api/v1", tags=["predict"])

# -----------------------------
# Health check
# -----------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}
