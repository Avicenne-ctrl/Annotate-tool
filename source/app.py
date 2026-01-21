import streamlit as st
import requests 
from config import configuration
import os
import base64

st.title("app")

# Texte simple
st.write("Bienvenue dans ma première app Streamlit")


uploaded_file = st.file_uploader("Choose a file", type= "docx")
user_query = st.text_input("What is your request ?")


if st.button("Start processing"):
    if uploaded_file is not None and user_query is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.read()
        file_name = uploaded_file.name
        
        payload = {
            "user_query": user_query,
            "file_name": file_name,
            "files": base64.b64encode(uploaded_file.getvalue()).decode(),
        }
        
        print(f"[App] send payload: {payload} and file size {len(base64.b64encode(uploaded_file.getvalue()).decode())}")
        
        try:
            resp = requests.post(configuration.backend_url, 
                                 json=payload, 
                                 # files= files
                                 )
            print(resp)
            if resp.status_code == 200:
                print(resp.json())
                
                commented_path = resp.json()
                with open(commented_path, "rb") as f:
                    commented_file = f.read()
                    
                st.download_button('Download Commented Docx', commented_file, file_name=f'commented_{file_name}.docx')
                os.remove(commented_path)
            
            else:
                print(resp)
                print(resp.json())

                st.warning("Isuue during file processing")
        
        except Exception as e:
            print(f"[App] error: {str(e)}")
        
else:
    st.warning("Complete your request")
            
