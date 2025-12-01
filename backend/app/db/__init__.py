from sqlmodel import select
from app.db.session import get_session
from app.models.db_models import User


def get_user_by_email(email: str):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.email == email)).first()
        return user

def update_user_password(user_id: int, new_password: str):
    with next(get_session()) as session:
        user = session.get(User, user_id)
        if user:
            user.hashed_password = new_password  # agar hash karna ho to hash function use karo
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        return None
