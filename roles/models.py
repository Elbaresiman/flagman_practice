from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON, nullable=False)