from pydantic import BaseModel
from typing import List

class response_schema(BaseModel):
            paragraph_number: int
            section_number: int
            content: str

class response_schema_list(BaseModel):
    response: List[response_schema]