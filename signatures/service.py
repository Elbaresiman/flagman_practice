from sqlalchemy.orm import Session
from signatures.models import Signature
from signatures.utils import generate_signature
from documents.models import Document

def sign_document(db: Session, document: Document, user):
    signature_hash = generate_signature(phone=user.phone_number, document_id=document.id)
    signature = Signature(document_id=document.id, user_id=user.id, signature_hash=signature_hash)

    document.status = "SIGNED"

    db.add(signature)
    db.commit()
    db.refresh(signature)
    return signature