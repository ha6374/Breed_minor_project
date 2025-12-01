# from sqlmodel import SQLModel, create_engine, Session
# from app.core.config import settings

# engine = create_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)

# def init_db():
#     """Create all tables from SQLModel metadata"""
#     SQLModel.metadata.create_all(engine)

# def get_db():
#     """Dependency for FastAPI routes"""
#     with Session(engine) as session:
#         yield session
# from sqlmodel import SQLModel, create_engine, Session
# from app.core.config import settings

# # ✅ Database connection (PostgreSQL)
# engine = create_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)

# def init_db():
#     """Create all tables from SQLModel models"""
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     """Dependency for FastAPI routes"""
#     with Session(engine) as session:
#         yield session


from sqlmodel import SQLModel, create_engine, Session, select
from app.core.config import settings
from app.models.db_models import User  
from app.core.security import get_password_hash as hash_password


# ✅ Database connection (PostgreSQL)
engine = create_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)

def init_db():
    """Create all tables from SQLModel models"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency for FastAPI routes"""
    with Session(engine) as session:
        yield session

# -----------------------------
# Step 3: User helpers
# -----------------------------
def get_user_by_email(email: str):
    with Session(engine) as session:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user

def update_user_password(user: User, new_password: str, session: Session):
    user.hashed_password = hash_password(new_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
