import streamlit as st
from src.vues import login
from src.vues import home
from src.vues import objectif, dataset,analysededonnées,conclusion

from src.router import redirect , get_route

def navigation():
    route = get_route()
    if route == "/login":
        login.load_view()
    elif route == "/home":
        home.load_view()
    elif route == "/objectif":
        objectif.load_view()
    elif route == "/dataset":
        dataset.load_view()
    elif route == "/analysededonnées":
        analysededonnées.load_view()   
    elif route == "/conclusion":
        conclusion.load_view()   
    else:
        redirect("/login",reload=True) # redirection afficher
        login.load_view() #redirection cacher 
        #navigation() 
navigation()


    