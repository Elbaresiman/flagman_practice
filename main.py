from fastapi import FastAPI

from auth.router import router as auth_router
from documents.router import router as documents_router
from signatures.router import router as signatures_router

app = FastAPI(
    title="Document Signing Service",
    description="Backend service for document distribution and signing",
    version="1.0.0"
    )

@app.get("/")
def root():
    return {"status": "ok", "message": "Document Signing Service running"}

app.include_router(auth_router)
app.include_router(documents_router)
app.include_router(signatures_router)