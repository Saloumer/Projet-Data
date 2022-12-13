import streamlit as st
from src.router import redirect

def load_view():

    st.markdown("Objectif du projet")
    if st.button("objet"):
        redirect("/login", reload=True)
    