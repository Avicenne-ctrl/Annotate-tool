import streamlit as st
import requests 
import os
import base64

from spire.doc import *
from spire.doc.common import *

from config import configuration
from source.utils.tools import save_file, extract_structured_spire_content, main_annotator

st.title("app")

# Texte simple
st.write("Bienvenue dans ma première app Streamlit")


uploaded_file = st.file_uploader("Choose a file", type= "docx")
user_query = st.text_input("What is your request ?")


if st.button("Start processing"):
    if uploaded_file is not None and user_query is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        file_name = uploaded_file.name
        temp_file_name = f"commented_{file_name}"
        path_temp_file = f"temp_{file_name}"
        
        save_file(bytes_data, path_temp_file)
        
        doc = Document()
        doc.LoadFromFile(path_temp_file)
        
        file_content = extract_structured_spire_content(doc)
        
        payload = {
            "user_query": user_query,
            "file_content": file_content,
        }
    
        print(f"[App] send payload: {payload} and file {file_content[:10]}")
    
        resp = requests.post(configuration.backend_url, 
                                json=payload, 
                                timeout=600,
                                )
        print(f"[APP] API response: {resp.json()}")
   