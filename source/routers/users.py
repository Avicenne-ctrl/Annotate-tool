from fastapi import APIRouter
from typing import Annotated
from fastapi import UploadFile, File, Depends
from pydantic import Field, BaseModel

import logging
import json

from source.utils.main import main
from source.model.router import request_model

router = APIRouter()
    
@router.post("/users/")
def read_users(item: request_model):
    
    try:
        resp_json = json.loads(item.json())
        
        print(resp_json)
        print(type(resp_json))
        
        user_query = resp_json["user_query"]
        file_name = resp_json["file_name"]
        files = resp_json["files"]
    
        file_commented = main(files, file_name, user_query)
                
        return file_commented
    
    except Exception as e:
        logging.error(f"[User Router] error: {str(e)}")
