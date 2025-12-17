from sqlalchemy.orm import Session
from documents.models import Document

def create_document(db: Session, title: str, file_path: str, sender_id: int,
                    receiver_id: int, organization_id: int) -> Document:
    document = Document(title=title, file_path=file_path, sender_id=sender_id,
        receiver_id=receiver_id, organization_id=organization_id, status="SENT")
    
    db.add(document)
    db.commit()
    db.refresh(document)

    return document