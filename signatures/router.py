from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user, get_db
from documents.models import Document
from .service import sign_document
from users.models import User

router = APIRouter(prefix="/signatures", tags=["signatures"])

@router.post("/{document_id}")

def sign(document_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    document = db.get(Document, document_id)

    if not document:
        raise HTTPException(404, "Document not found")
    
    if document.receiver_id != user.id:
        raise HTTPException(403, "Not allowed to sign this document")
    
    if document.status == "SIGNED":
        raise HTTPException(400, "Already signed")
    
    sign_document(db, document, user)
    return {"message": "Document signed successfully"}