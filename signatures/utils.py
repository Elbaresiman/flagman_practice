import hashlib

SECRET = "2uWb6iT05NEG5J1SpCcx4O155pMLU4JAT5wjQPbphRs"

def generate_signature(phone: str, document_id: int) -> str:
    raw = f"{phone}:{document_id}:{SECRET}"
    return hashlib.sha256(raw.encode()).hexdigest()