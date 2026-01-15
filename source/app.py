import streamlit as st
import requests 
from config import configuration


st.title("app")

# Texte simple
st.write("Bienvenue dans ma première app Streamlit")

# Champ de saisie
nom = st.text_input("Quel est ton nom ?")

# Bouton
if st.button("Get name:"):
    if nom:
        resp = requests.get(configuration.backend_url)
        st.success(f"{resp.json()}")
    else:
        st.warn