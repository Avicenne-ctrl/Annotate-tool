import streamlit as st
import requests 
from config import configuration


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
        
        payload = {
            "user_query": user_query,
        }
        
        files = {file_name: bytes_data}

        resp = requests.post(configuration.backend_url, json=payload, files= files)
        
        if resp.status_code == 200:
            st.download_button('Download Commented Docx', resp, file_name='New_File.docx')
        
        else:
            st.warning("Isuue during file processing")
        
else:
    st.warning("Complete your request")
            
