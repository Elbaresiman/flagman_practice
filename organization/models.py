from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from core.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    users = relationship(
        "UserOrganization",
        back_populates="organization",
        cascade="all, delete"
    )

    departments = relationship(
        "Department",
        back_populates="organization",
        cascade="all, delete"
    )