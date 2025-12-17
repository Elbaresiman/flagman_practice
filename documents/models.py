from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)

    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    receiver_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    status: Mapped[str] = mapped_column(String(50), default="SENT")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    sender = relationship(
        "User",
        back_populates="sent_documents",
        foreign_keys=[sender_id]
    )

    signatures = relationship(
        "Signature",
        back_populates="document",
        cascade="all, delete"
    )