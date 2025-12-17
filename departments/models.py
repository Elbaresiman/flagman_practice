from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="departments")

    members = relationship(
        "UserDepartmentRole",
        back_populates="department",
        cascade="all, delete"
    )