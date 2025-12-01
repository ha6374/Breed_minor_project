from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
# from pydantic import BaseModel
# from app.db.session import get_db
from app.db.session import get_session
from fastapi import File, UploadFile


from pydantic import BaseModel, EmailStr
from typing import Optional
from app.core.security import get_current_user
import shutil, os

from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

from app.models.db_models import User
from app.db.session import get_session
# from app.core.security import hash_password, verify_password, create_access_token
from app.core.security import get_password_hash as hash_password, verify_password, create_access_token
from app.db.session import get_user_by_email, update_user_password


# from fastapi import APIRouter, HTTPException, Depends
# from pydantic import BaseModel, EmailStr
from app.core.security import generate_password_reset_token
from app.db import get_user_by_email, update_user_password
from app.utils.email import send_reset_email


router = APIRouter(tags=["auth"])

# ---------- SIGNUP ----------
class SignupRequest(BaseModel):
    username: str
    email: str
    password: str


@router.post("/signup")
def signup(payload: SignupRequest, session: Session = Depends(get_session)):
    # Check username
    user = session.exec(select(User).where(User.username == payload.username)).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Check email
    existing_email = session.exec(select(User).where(User.email == payload.email)).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        username=payload.username,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        is_active=True,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"id": user.id, "username": user.username, "email": user.email}


# ---------- LOGIN ----------
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    """
    OAuth2PasswordRequestForm sends:
      username: email (yes, it's named 'username' but we treat it as email)
      password: password
    """

    user = session.exec(select(User).where(User.email == form_data.username)).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(subject=user.email)
    return {"access_token": token, "token_type": "bearer"}




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    """Return user profile details"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.exec(select(User).where(User.email == email)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

from pydantic import BaseModel, EmailStr
from typing import Optional

class EditProfileRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

@router.put("/profile")
def update_profile(
    payload: EditProfileRequest,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    """Update user profile details"""
    try:
        # Decode the JWT to get user email
        payload_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email = payload_data.get("sub")

        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

        # Find the user
        user = db.exec(select(User).where(User.email == email)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update fields if provided
        if payload.username:
            user.username = payload.username
        if payload.email:
            # Optional: check if email already exists for another user
            existing = db.exec(select(User).where(User.email == payload.email, User.id != user.id)).first()
            if existing:
                raise HTTPException(status_code=400, detail="Email already in use")
            user.email = payload.email
        if payload.password:
            user.hashed_password = hash_password(payload.password)

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "message": "Profile updated successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at
            }
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")



# @router.post("/profile/image")
# def upload_profile_image(
#     file: UploadFile = File(...),
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_session)
# ):
#     payload_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#     email = payload_data.get("sub")

#     user = db.exec(select(User).where(User.email == email)).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Save the uploaded file
#     file_path = f"static/profile_pics/{user.id}_{file.filename}"
#     with open(file_path, "wb") as f:
#         f.write(file.file.read())

#     # Save the path in the database (make sure User model has profile_image column)
#     user.profile_image = file_path
#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     return {"message": "Profile image updated", "profile_image": file_path}


# from fastapi import UploadFile, File, Depends
# import shutil, os
# from sqlmodel import Session
# from app.db.session import get_session
# from app.models.db_models import User
# from app.core.security import get_current_user

UPLOAD_DIR = "app/uploads/profile_pics"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/profile/image")
def upload_profile_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    file_path = os.path.join(UPLOAD_DIR, f"{current_user.id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Store the path in DB
    current_user.profile_image = file_path
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    return {"message": "Profile image uploaded successfully", "path": file_path}


# Request model
class ForgotPasswordRequest(BaseModel):
    email: EmailStr

@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest):
    user = get_user_by_email(request.email)
    if not user:
        # For security: don't reveal whether email exists
        return {"message": "If the email exists, a reset link was sent."}

    # Generate reset token
    token = generate_password_reset_token(user.id)

    # Send email with reset link
    reset_link = f"http://localhost:8501/8_reset_password?token={token}"  # Frontend URL
    send_reset_email(to_email=user.email, reset_link=reset_link)

    return {"message": "If the email exists, a reset link was sent."}