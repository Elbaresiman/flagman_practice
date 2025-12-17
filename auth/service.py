from sqlalchemy.orm import Session
from users.models import User
from core.security import hash_password

from core.security import verify_password
from core.jwt import create_access_token

def register_user(db: Session, email: str, phone: str, password: str) -> User:
    user = User(email=email, phone=phone, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None
    
    return create_access_token({"sub": str(user.id)})