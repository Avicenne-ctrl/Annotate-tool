import streamlit as st
import requests 

st.title("app")

# Texte simple
st.write("Bienvenue dans ma première app Streamlit")

# Champ de saisie
nom = st.text_input("Quel est ton nom ?")

# Bouton
if st.button("Get name:"):
    if nom:
        resp = requests.get("http://127.0.0.1:8000/users/")
        st.success(f"{resp.json()}")
    else:
        st.warning("Merci d'entrer un nom")
