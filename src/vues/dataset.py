import streamlit as st
from src.router import redirect
from pandas import DataFrame, read_csv


def load_view():

    st.markdown("## Base de données")


    df = read_csv("src/assets/marketing_campaign.tsv", sep="\t")
    st.dataframe(df)

    st.markdown("""
    #####  Ce dataset a été mis à disposition par le Dr. Omar Romero-Hernandez
    """)

    st.markdown("""
    **Liste des lignes de Dataset**: 

    Personnes:

    - ID : identifiant unique du client
    - Year_Birth : Année de naissance du client
    - Éducation : niveau d’éducation du client
    - Marital_Status : État matrimonial du client
    - Revenu : Revenu annuel du ménage du client
    - Kidhome : Nombre d’enfants dans le ménage du client
    - Teenhome: Nombre d’adolescents dans le ménage du client
    - Dt_Customer : Date d’inscription du client auprès de l’entreprise
    - Récence : nombre de jours depuis le dernier achat du client
    - Se plaindre: 1 si le client s’est plaint au cours des 2 dernières années, 0 sinon

    Des produits:

    - MntWines : Montant dépensé en vin au cours des 2 dernières années
    - MntFruits : Montant dépensé en fruits au cours des 2 dernières années
    - MntMeatProducts : Montant dépensé pour la viande au cours des 2 dernières années
    - MntFishProducts : Montant dépensé pour le poisson au cours des 2 dernières années
    - MntSweetProducts : Montant dépensé en sucreries au cours des 2 dernières années
    - MntGoldProds : Montant dépensé en or au cours des 2 dernières années

    Promotion:

    - NumDealsPurchases : Nombre d'achats effectués avec une remise
    - AcceptedCmp1 : 1 si le client a accepté l'offre dans la 1ère campagne, 0 sinon
    - AcceptedCmp2 : 1 si le client a accepté l'offre dans la 2ème campagne, 0 sinon
    - AcceptedCmp3 : 1 si le client a accepté l'offre dans la 3ème campagne, 0 sinon
    - AcceptedCmp4 : 1 si le client a accepté l'offre dans la 4ème campagne, 0 sinon
    - AcceptedCmp5 : 1 si le client a accepté l'offre dans la 5ème campagne, 0 sinon
    - Réponse : 1 si le client a accepté l'offre lors de la dernière campagne, 0 sinon

    Place:

    - NumWebPurchases : Nombre d'achats effectués via le site Web de l'entreprise
    - NumCatalogPurchases : Nombre d'achats effectués à l'aide d'un catalogue
    - NumStorePurchases : Nombre d'achats effectués directement en magasin
    - NumWebVisitsMonth : Nombre de visites sur le site Web de l'entreprise au cours du dernier mois

    """)
