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

def afficherAgeMoyen(df):
    st.markdown(""" 
    ## **L'age moyen des clients?**
    """)
    st.code(""" df['Age'].mean()
    """)
    df['Age'].mean()
    st.markdown(""" 
    **L'age moyen des clients 45**
    """)


def afficherAgeSelonNombreAchat(df):
    st.markdown(""" 
    ## **En quoi consiste l'âge par rapport au nombre d'achats?**
    """)
    figure = plt.figure()
    sns.kdeplot(df,x='Age')
    st.pyplot(figure)

def afficherNombreDachatsParClients(df):
    df['total_purchases']=df['MntFishProducts']+df["MntFruits"]+df['MntGoldProds']+df['MntMeatProducts']+df['MntSweetProducts']+df["MntWines"]
    figure = plt.figure()
    sns.kdeplot(df,x='total_purchases')
    p = sns.lineplot()
    p.set(title = " Le nombre d'achats effectués par les clients")
    plt.subplot()
    st.pyplot(figure)

def afficherRapportEntreNombreDachatsEtNombreEnfantsEtTailleFamille(df):
    figure = plt.figure()
    sns.stripplot(df,x='Teenhome',y='total_purchases') 
    p = sns.lineplot()
    p.set(title = "La relation entre le nombre d'achats et le nombre d’adolescents")
    #plt.subplot()
    st.pyplot(figure)

    figure = plt.figure()
    sns.catplot(df,x='Kidhome',y='total_purchases',kind='strip')
    p = sns.lineplot()
    p.set(title = "La relation entre le nombre d'achats et le nombre d’enfants")
    plt.subplot()
    st.pyplot(figure)


def afficherNombreTotalEnfantsDansFoyer(df):
    df["nbre_enfant"]=df["Kidhome"]+df["Teenhome"]
    df["nbre_enfant"].head()

    df['Marital_Status'].value_counts()

    df['Marital_Status'].replace('Alone','Single',inplace=True)
    df['Marital_Status'].replace('Absurd','Single',inplace=True)
    df['Marital_Status'].replace('YOLO','Single',inplace=True)

    df["Vivre_avec"]=df["Marital_Status"].replace({"Married":"Partner", "Together":"Partner", "Widow":"Alone", "Divorced":"Alone" ,'Single':"Alone"})

    df["Vivre_avec"]= df["Vivre_avec"].replace({"Alone": "1", "partner": "2"})
    df["Vivre_avec"].head(135)

    fig, ax = plt.subplots(figsize=(13, 7))
    colors2=['#F034A3','#283593','#03a9f4','#004d40','#c2185b'] 

    patches, texts, pcts = ax.pie(
    df['Marital_Status'].value_counts(), labels=[*df['Marital_Status'].value_counts().index], autopct='%.2f',colors=colors2
    ,wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)
    centre_circle = plt.Circle((0,0),0.20,fc='white') 
    plt.gcf().gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.title(label='Etat civil',fontsize=22,fontstyle='oblique')
    fig.legend()

#def afficherRelationEntreRevenuTailleFamilleNombreEnfants(df):

#def afficherRelationEntreEducationEtRevenu(df):

#def afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df):

#def afficherRelationEntreRevenuEtNombreAchats(df):

#def afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df):


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

    afficherAgeMoyen(df)
    
    afficherAgeSelonNombreAchat(df)

    afficherNombreDachatsParClients(df)

    afficherRapportEntreNombreDachatsEtNombreEnfantsEtTailleFamille(df)

    #afficherNombreTotalEnfantsDansFoyer(df)

    #afficherRelationEntreRevenuTailleFamilleNombreEnfants(df)

    #afficherRelationEntreEducationEtRevenu(df)

    #afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df)

    #afficherRelationEntreRevenuEtNombreAchats(df)

    #afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df)




    
 

    