import streamlit as st
from src.router import redirect

def load_view():

    st.markdown("Analyse de données")
    if st.button("analyse"):
        redirect("/home", reload=True)