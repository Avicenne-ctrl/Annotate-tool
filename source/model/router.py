from pydantic import BaseModel

class RequestModel(BaseModel):
    file_bytes: bytes
    file_name: str
    query: str