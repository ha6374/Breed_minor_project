# from datetime import datetime, timedelta
# from typing import Any, Union

# # from app.core.security import get_current_user
# # from app.core.security import get_current_user

# # from datetime import datetime, timedelta
# from jose import jwt

# from jose import JWTError, jwt
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from app.core.config import settings

# from sqlmodel import Session, select


# from jose import jwt
# from passlib.context import CryptContext

# from app.core.config import settings

# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# ALGORITHM = "HS256"


# def create_access_token(
#     subject: Union[str, Any], expires_delta: timedelta = None
# ) -> str:
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(
#             minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#         )
#     to_encode = {"exp": expire, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
#     """
#     Decode JWT token and fetch current user from DB.
#     """
#     from app.db.session import get_session
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials.",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     user = session.exec(select(User).where(User.email == username)).first()
#     if user is None:
#         raise credentials_exception
#     return user



# SECRET_KEY = "supersecretkey"
# ALGORITHM = "HS256"
# RESET_TOKEN_EXPIRE_MINUTES = 30

# def generate_password_reset_token(user_id: int) -> str:
#     expire = datetime.utcnow() + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
#     to_encode = {"user_id": user_id, "exp": expire}
#     token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return token

from datetime import datetime, timedelta
from typing import Any, Union

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from sqlmodel import Session, select
from passlib.context import CryptContext

from app.models.db_models import User  # safe top-level import

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
ALGORITHM = "HS256"
SECRET_KEY = "supersecretkey"
RESET_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Decode JWT token and fetch current user from DB.
    """
    # ✅ Local import to avoid circular import
    from app.db.session import get_session

    session: Session = next(get_session())
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        if not email:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise credentials_exception
    return user


def generate_password_reset_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    to_encode = {"user_id": user_id, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
