from fastapi import APIRouter

import logging
import json

from source.utils.agent import call_mistral_agent
from source.utils.prompt import user_prompt
from source.model.router import request_model

router = APIRouter()
    
@router.post("/users/")
def read_users(item: request_model):
    
    try:
        resp_json = json.loads(item.json())
        
        print(resp_json)
        print(type(resp_json))
        
        user_query = resp_json["user_query"]
        file_content = resp_json["file_content"]
    
        user_prompt = user_prompt(user_query, file_content)
        mistral_analysis = call_mistral_agent(user_prompt)
                
        return mistral_analysis
    
    except Exception as e:
        logging.error(f"[User Router] error: {str(e)}")
        return {}
