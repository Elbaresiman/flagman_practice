from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    receiver_id: int
    organization_id: int

class DocumentOut(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True