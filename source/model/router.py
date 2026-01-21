from pydantic import BaseModel

class request_model(BaseModel):
    user_query: str
    file_name: str
    files: str