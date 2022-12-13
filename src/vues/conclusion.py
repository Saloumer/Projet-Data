import streamlit as st
from src.router import redirect

def load_view():

    st.markdown("La conclusion")
    if st.button("Conclusion"):
        redirect("/login", reload=True)