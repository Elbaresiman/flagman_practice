from core.database import engine, Base

from departments.models import Department
from documents.models import Document
from organization.models import Organization
from roles.models import Role
from signatures.models import Signature
from users.models import User

Base.metadata.create_all(bind=engine)
print("Tables created!")