import streamlit as st
from src.controllers.auth import login
from src.router import redirect


def load_view():

    st.title("Page de connexion")
    Email = st.text_input("Email")
    password = st.text_input("Mot de passe",type="password")

    if st.button("se connecter"):
        if login(Email,password):
            redirect("/home", reload=True)


        else:
            st.text("Erreur de connexion")



