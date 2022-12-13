import streamlit as st
from src.controllers.auth import login

def load_view():

    st.title("Les planètes du système Solaire (Dataset)")

    st.header("Page de connexion")

    Email = st.text_input("Email")

    password = st.text_input("Mot de passe",type="password")

    if st.button("se connecter") == False:
        st.warning("veuiller entrer votre email et votre mot de passe")
    else:
        res = login(Email,password)
        if res:
            st.success("Bienvenue!")
        else:
            st.error("Email ou mot de passe incorrect(s)")

