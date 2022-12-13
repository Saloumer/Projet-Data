import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np
from src.controllers.auth import login
from src.router import redirect
from pandas import DataFrame, read_csv

def lectureCsvFichier():
    df = read_csv("src/assets/marketing_campaign.tsv", sep="\t")
    st.dataframe(df)
    return df

def afficherAgeClientSelonNaissance(df):
    st.markdown(""" 
    ## **L'âge du client selon la date de naissance** :
    """)
    df["Age"] = 2014-df["Year_Birth"]
    st.dataframe(df)
    st.code(
    """ df["Age"] = 2014-df["Year_Birth"]
    """)

    figure = plt.figure()
    sns.kdeplot(df,x='Age')
    st.pyplot(figure)

def afficherAgeSelonNombreAchat(df):
jnsqakd kjqsn
    
def afficherNombreDachatsParClients(df):
    st.markdown(""" 
    ## **En quoi consiste l'âge par rapport au nombre d'achats?**
    """)
    sns.displot(df,x='Age',kind='kde')
    p = sns.lineplot()
    p.set(title = "L'age")
    plt.subplot()


def afficherRapportEntreNombreDachatsEtNombreEnfantsEtTailleFamille(df):

def afficherNombreTotalEnfantsDansFoyer(df):

def afficherRelationEntreRevenuTailleFamilleNombreEnfants(df):

def afficherRelationEntreEducationEtRevenu(df):

def afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df):

def afficherRelationEntreRevenuEtNombreAchats(df):

def afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df):


def load_view():

    st.markdown(" # Page Home")
    if st.button("connecter-vous"):
        redirect("/login", reload=True)
    
    st.markdown(""" 
    ## **Problématique** : 

    Si je souhaite mettre un produit sur le marcher, qui sera mes acheteurs? avec quelle support de vente?
    Produit / Type de personnes ( financier,age, Taille de la famille)
    Produit / place de vente  
    place de vente / Type de personne 
    """)

    
    df = lectureCsvFichier()

    afficherAgeClientSelonNaissance(df)
    
    afficherAgeSelonNombreAchat(df)

    afficherNombreDachatsParClients(df)

    afficherRapportEntreNombreDachatsEtNombreEnfantsEtTailleFamille(df)

    afficherNombreTotalEnfantsDansFoyer(df)

    afficherRelationEntreRevenuTailleFamilleNombreEnfants(df)

    afficherRelationEntreEducationEtRevenu(df)

    afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df)

    afficherRelationEntreRevenuEtNombreAchats(df)

    afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df)




    ############################"
    revenu = plt.figure()
    sns.boxplot(df,x='Income')
    st.pyplot(revenu)
    
    autre = plt.figure()
    sns.histplot(df, x='Age')

    #p = sns.lineplot()
    #p.set(title = "L'age")
    #plt.show(sns)
    st.pyplot(autre) 


    ############################"

    st.markdown(""" 
    ## **L'age moyen des clients?**
    """)
    st.code(""" df['Age'].mean()
    """)
    df['Age'].mean()
    st.markdown(""" 
    **L'age moyen des clients 45**
    """)

    fig, ax = plt.subplots(figsize=(13, 7))
    colors2=['#F034A3','#283593','#03a9f4','#004d40','#c2185b'] 
    ax.pie(
    df['Marital_Status'].value_counts(), labels=[*df['Marital_Status'].value_counts().index], autopct='%.2f',colors=colors2
    ,wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)
    centre_circle = plt.Circle((0,0),0.20,fc='white') 
    plt.gcf().gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.title(label='Etat civil',fontsize=22,fontstyle='oblique')
    fig.legend()
    st.pyplot(fig)


