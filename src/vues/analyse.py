import streamlit as st
from src.router import redirect
from src.controllers.auth import login
from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pb
import plotly.express as px



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


def afficherAgeSelonNombreAchat(df):
    st.markdown(""" 
    ## **En quoi consiste l'âge par rapport au nombre d'achats?**
    """)
    figure = plt.figure()
    sns.kdeplot(df,x='Age')
    p = sns.lineplot()
    p.set(title = "L'age")
    st.pyplot(figure)

    print("Client le plus âgé:",max(df['Age']))
    print("Client le plus jeune:",min(df['Age']))


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



def afficherNombreDachatsParClients(df):
    st.markdown(""" 
    ## **Le nombre d'achats effectués par les clients** :
    """)
    df['total_purchases']=df['MntFishProducts']+df["MntFruits"]+df['MntGoldProds']+df['MntMeatProducts']+df['MntSweetProducts']+df["MntWines"]
    figure = plt.figure()
    sns.kdeplot(df,x='total_purchases')
    p = sns.lineplot()
    p.set(title = " Le nombre d'achats effectués par les clients")
    plt.subplot()
    st.pyplot(figure)



def afficherRapportEntreNombreDachatsEtNombreEnfants(df):

    st.markdown(""" 
    ## **Le rapport entre le nombre d'achats et le nombre d'enfants et la taille de la famille** :
    """)
    figure1 = plt.figure()
    sns.stripplot(df,x='Teenhome',y='total_purchases') 
    p = sns.lineplot()
    p.set(title = "La relation entre le nombre d'achats et le nombre d’adolescents")
    st.pyplot(figure1)

    figure2 = plt.figure()
    sns.stripplot(df,x='Kidhome',y='total_purchases')
    p = sns.lineplot()
    p.set(title = "La relation entre le nombre d'achats et le nombre d’enfants")
    st.pyplot(figure2)

    st.markdown(""" 
    **On constate que les clients ayant des adolescents ont plus d'achats que ceux ayant des enfants.**
    """)


def afficherNombreTotalEnfantsDansFoyer(df):

    st.markdown(""" 
    ## **Le nombre total d'enfants vivant dans le foyer**:
    """)

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

    st.markdown(""" 
    **La majorité des clients de l'entreprise sont des individus qui vivent avec des partenaires.**
    """)


def afficherRelationEntreRevenuTailleFamilleNombreEnfants(df):


    st.markdown(""" 
    ## **Le nombre de membres de la famille**:
    """)

    c = df["Vivre_avec"].replace({"Alone": 1, "Partner":2}) 
    c = pb.to_numeric(c) 
    df["Vivre_avec"] = c
    # df["Vivre_avec"] = pd.to_numeric(df["Vivre_avec"].replace({"Alone": 1, "Partner":2}))
    df["taille_famille"] = df["Vivre_avec"] + df["nbre_enfant"]
    df["taille_famille"].value_counts()

    color_3=['#DF7861','#5F6F94','#CA4E79','#7A4069','#FFD700']

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.pie(
    df['taille_famille'].value_counts(), labels=[*df['taille_famille'].value_counts().index], autopct='%.1f%%',colors=color_3
    ,wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)
    centre_circle = plt.Circle((0,0),0.20,fc='white') 
    plt.gcf().gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.title(label='Le nombre de membres de la famille',fontsize=18,fontstyle='italic')
    fig.legend()
    st.pyplot(fig)

    st.markdown(""" 
    **La plupart des clients de l'entreprise font partie d'une famille de deux ou trois personnes.**
    """)

def afficherRapportEntreNombreDachatsEtTailleFamille(df):

    st.markdown(""" 
    ## **La relation entre nombre d'achats et taille de la famille**:
    """)

    figure3 = plt.figure()
    sns.stripplot(df,x='taille_famille',y='total_purchases')
    p = sns.lineplot()
    p.set(title = "La relation entre le nombre d'achats et la taille de la famille")
    st.pyplot(figure3)

    st.markdown(""" 
    **Ce graphique montre plus les membres de la famille sont nombreux, moins les achats sont importants.**
    """)

def afficherRapportEntreRevenuEtNombreEnfants(df):
    
    st.markdown(""" 
    ## **La relation entre le revenu et le nombre d’enfants**:
    """)

    # Supprimer les valeurs aberrantes
    df.dropna(subset=['Income'])
    df[df['Income']<150000]
    df[df['Income']<600000]



    figure = plt.figure()
    sns.stripplot(df,x='nbre_enfant',y='Income')
    p = sns.lineplot()
    p.set(title = "La relation entre le revenu et le nombre d’enfants")
    st.pyplot(figure)


    st.markdown(""" 
    **Tous les clients ont environ le même revenu, malgré la différence dans le nombre d'enfants, à l'exception de ceux qui en ont trois.**
    """)


def afficherRelationEntreEducationEtRevenu(df):

    st.markdown(""" 
    ## **La relation entre l'éducation et le revenu**:
    """)

    df['Education'].value_counts()

    #fig1 = plt.figure()
    color_1=['#006064', '#3d5afe', '#880e4f','#dd2c00','#6a1b9a']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(
    df['Education'].value_counts(), labels=[*df['Education'].value_counts().index],shadow=True, autopct='%.1f%%',colors=color_1,wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'},
    startangle=90)
    centre_circle = plt.Circle((0,0),0.20,fc='white') 
    plt.gcf().gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.title(label='Education',fontsize=18,fontstyle='italic')
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(""" 
    **Le pourcentage de clients titulaires d'un diplôme universitaire atteint 97,6 %**
    """)

    st.markdown(""" 
    ## **Le revenu**:
    """)
    figure = plt.figure(figsize=(6,4))
    sns.boxplot(df,x='Income')
    st.pyplot(figure)

    df=df[df['Income']<200000]


    st.markdown(""" 
    ## **La relation entre le revenu et l'éducation**:
    """)

    st.plotly_chart(px.box(df, x="Education", y="Income"))

    st.markdown(""" 
    **Le revenu moyen de tous les clients est très similaire, sauf pour Basic.**
    """)

def afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df):

    st.markdown(""" ## **La relation entre le revenu et le nombre d'enfants**
    """)

    st.plotly_chart(px.scatter(df, x="nbre_enfant", y="Income"))

    st.markdown(""" 
    **Presque tous les clients ont un revenu semblable, même si le nombre d'enfants est différent, à l'exception de ceux qui en ont trois, étant donné que leur revenu commence à 20 000 et plus, contrairement aux autres.**""")


    st.markdown(""" ## **La relation entre le revenu et la taille de la famille**
    """)
#########################################################

    figure = plt.figure(figsize=(6,6))
    sns.boxenplot(df, x="taille_famille", y="Income")
    sns.stripplot(df, x="taille_famille", y="Income",color='#004d40')
    plt.title(label='Revenu / Taille de la famille',fontsize=14,fontstyle='italic')
    st.pyplot(figure)

##############################################################

    st.markdown(""" 
    **Tous les clients touchent approximativement le même revenu, malgré la différence de taille de la famille, à l'exception de ceux qui ont une part de taille de 5.**""")

def afficherRelationEntreRevenuEtNombreAchats(df):

    st.markdown(""" ## **La relation entre le revenu et le nombre d'achats**
    """)
    st.plotly_chart(px.scatter(df, x="total_purchases", y="Income"))

    st.markdown(""" **Il existe une relation quasi linéaire entre le revenu et le nombre d'achats.                                                                                                                        
    Les clients dont le nombres d’achats a atteint 500, la plupart d’entre eux ont un revenu annuel inférieur à 50 000, tandis que le reste de la clientèle a plus de 500 achats, la plupart d'entre eux ont plus de 50.000 revenus et peuvent atteindre 100 000.**""")


def afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df):

    st.markdown(""" ## **C'est quoi la relation entre le nombre d'achats d'une offre avec le nombre d'achats sur le site Web, le nombre d'achats sur le catalogue et le nombre d'achats sur le magasin ?**""")


    df['NumDealsPurchases'].value_counts()
    df['NumWebPurchases'].value_counts()

    figure = plt.figure(figsize=(6,6))
    sns.scatterplot(df,x='NumWebPurchases',y='NumDealsPurchases')
    st.pyplot(figure)

    df['NumCatalogPurchases'].value_counts()
    figure = plt.figure(figsize=(6,6))
    sns.scatterplot(df,x='NumCatalogPurchases',y='NumDealsPurchases')
    st.pyplot(figure)

    df['NumStorePurchases'].value_counts()
    figure = plt.figure(figsize=(6,6))
    sns.scatterplot(df,x='NumStorePurchases',y='NumDealsPurchases')
    st.pyplot(figure)

    st.markdown(""" ## **Quelle est la relation entre le nombre d'achats d'un Deal avec cmp accepté 1, cmp accepté 2, cmp accepté 3, cmp accepté 4, cmp accepté 5 et réponse ?**""")

    df['NumDealsPurchases'].value_counts()

    figure = plt.figure(figsize=(8,6))
    sns.countplot(df,x='NumDealsPurchases')
    st.pyplot(figure)

    st.markdown(""" **La quasi-totalité des clients ont fait un achat au moins une fois.**""")



def load_view():
    st.markdown("""**Dans cette section, je vais présenter un projet d'analyse de données sur l'analyse de la personnalité client en python**.""")

    st.markdown("# Analyse de données")

    df = lectureCsvFichier()

    afficherAgeClientSelonNaissance(df)

    afficherAgeSelonNombreAchat(df)

    afficherAgeMoyen(df)

    afficherNombreDachatsParClients(df)

    afficherRapportEntreNombreDachatsEtNombreEnfants(df)

    afficherNombreTotalEnfantsDansFoyer(df)

    afficherRelationEntreRevenuTailleFamilleNombreEnfants(df)

    afficherRapportEntreNombreDachatsEtTailleFamille(df)

    afficherRapportEntreRevenuEtNombreEnfants(df)

    afficherRelationEntreEducationEtRevenu(df)

    afficherRelationEntreRevenuTailleFamilleEtNombreEnfants(df)

    afficherRelationEntreRevenuEtNombreAchats(df)

    afficherRelationEntreNombreAchatsOffreNombreAchatsEtNombreAchatsCatalogue(df)

