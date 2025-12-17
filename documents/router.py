from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user, get_db
from .service import create_document
from .schemas import DocumentCreate, DocumentOut
from users.models import User
from .models import Document

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentOut)
def send_document(data: DocumentCreate = Depends(), file: UploadFile = File(...),
                  db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    document = create_document(db=db, title=data.title, file_path=file_path, sender_id=user.id,
                               receiver=data.receiver_id, organization_id=data.organization_id)
    
    return document

@router.get("/inbox", response_model=list[DocumentOut])
def inbox(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return (db.query(Document).filter(Document.receiver_id == user.id).all())

@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return user.email