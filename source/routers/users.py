from fastapi import APIRouter

from source.utils.main import main
from source.model.router import RequestModel


router = APIRouter()

@router.post("/users/", tags=["users"])
def read_users(req: RequestModel):
    
    file_bytes = req.file_bytes
    file_name = req.file_name
    query = req.query
    
    file_commented = main(file_bytes, file_name, query)
    
    return file_commented
