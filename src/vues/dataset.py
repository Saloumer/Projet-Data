import streamlit as st
from src.router import redirect

def load_view():

    st.markdown("base de données")
    if st.button("dataset"):
        redirect("/home", reload=True)