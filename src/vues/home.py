import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np
from src.controllers.auth import login
from src.router import redirect
from pandas import DataFrame, read_csv
import pandas as pd
import plotly.express as px
from src.controllers.auth import logout


def load_view():
    st.title("Acceuil")

    if st.button("Deconnexion"):
        logout()
        redirect("/login", reload=True)

def load_view():

    st.markdown(" # Page Home")
    
    st.markdown(""" 
    ##### Problématique : 

    Si je souhaite mettre un produit sur le marcher:
    - Quel segment de clientèle est le plus susceptible d’acheter le produit? 
    - La relation entre l'age, taille de la famille, revenu et le nombre d'achat?
    - Avec quelle support de vente?
 
    """)
    st.markdown(""" **J'ai choisi d'effectuer mon analyse à l'aide du langage python**.
    """)


    st.markdown(""" ## Pourquoi utiliser le langage Python?
    - Il constitue le langage de programmation le plus disponible.
    - Il est la langue open source la plus utilisée dans le monde.
    - Il est un langage à plateformes multiples.
    - Il identifie et met automatiquement en correspondance les types de données. 
    - Il est généralement facile à utiliser, ce qui demande moins de temps pour le codage.
    - Il n'existe aucune limite pour le traitement des données.
    """)

    st.markdown(""" ### En python, nous travaillons avec les bibliothèques suivantes.:

    - ##### Librairie Pandas : 
    Pour la transformation des données, il est également facile de lire les données dans divers formats.
    - ##### Librairie Matplotlib: 
    Est un outil pour tracer des graphiques et visualiser des donnéeset. Matplotlib contient une sous-bibliothèque **pyplot** qui crée une interface proche du logiciel commercial Matlab.
    - ##### Librairie Seborne:
    Pour la visualisation de données, spécialisée dans l’analyse statistique. Seaborne permet la réalisation de graphes statistiques de qualité.
    """)


    

   

