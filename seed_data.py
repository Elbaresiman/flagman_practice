# seed_data.py
from core.database import SessionLocal
from users.models import User
from organization.models import Organization
from organization.user_organization import UserOrganization
from core.security import hash_password

db = SessionLocal()

alice = User(
    email="alice@test.com",
    phone="+111111111",
    password_hash=hash_password("password123")
)

bob = User(
    email="bob@test.com",
    phone="+222222222",
    password_hash=hash_password("password123")
)

db.add_all([alice, bob])
db.commit()

org = Organization(name="Cool Company Inc.")
db.add(org)
db.commit()

db.add_all([
    UserOrganization(user_id=alice.id, organization_id=org.id),
    UserOrganization(user_id=bob.id, organization_id=org.id),
])

db.commit()
db.close()

print("Seed data inserted!")
