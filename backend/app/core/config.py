import os
from typing import ClassVar
from pydantic_settings import BaseSettings
from pathlib import Path

# backend/app/core/config.py → go 2 directories up → backend/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:123456@localhost:5432/ai_breed_db"
    SECRET_KEY: str = "supersecretkey"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # FIXED: must be annotated for Pydantic v2
    # MODEL_PATH: ClassVar[str] = os.path.join(BASE_DIR, "models", "fine_tuned_model.h5")
    # LABELS_PATH: ClassVar[str] = os.path.join(BASE_DIR, "models", "labels.json")
    
    

    MODEL_PATH: ClassVar[Path] = Path(BASE_DIR) / "models" / "fine_tuned_model.h5"
    LABELS_PATH: ClassVar[Path] = Path(BASE_DIR) / "models" / "labels.json"


    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: str

    class Config:
        env_file = ".env"

settings = Settings()
