from mistralai import Mistral
from pydantic import BaseModel
from typing import List
from source.utils.prompt import system_prompt
from source.model.agent import response_schema_list

import json
import logging

API_KEY = "yoaW3tekgTfjwiTNYoXyTjLxzmWcjkoM"

client = Mistral(api_key=API_KEY)

def call_mistral_agent(query: str) -> List[dict]:
    """
    Call mistral agent to get description comments
    
    Args:
        query (str): user query
        
    Return:
        LLM structured output
    """
    
    try:
        message = [{
        "role": "system",
        "content": system_prompt(),},
            {
        "role": "user",
        "content": query,},
        ]
            
        print("[LLM] Mistral thinking...")

        chat_response = client.chat.parse(
            model= "mistral-large-latest",
            messages = message,
            response_format = response_schema_list
        )
        
        json_resp = json.loads(chat_response.choices[0].message.content)
        json_resp = json_resp["response"]
        logging.info(f"[LLM] Mistral response: {json_resp}")
    
    except Exception as e:
        print(f"[LLM]: error occurs: {e}")
        json_resp = []
        
    return json_resp