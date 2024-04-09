import pandas as pd
import numpy as np
import math

def dist_euclidienne(x, y, a, b):
    distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    return distance

#fonction qui normalise les données
def normaliser(df : pd.DataFrame):
    dfcopie = df.copy()
    # parcourir chaque colonne
    for colonne in dfcopie.columns:
        minval = dfcopie[colonne].min()  #minimum de la colonne
        maxval = dfcopie[colonne].max()  #maximum de la colonne
        #normaliser les valeurs dans la colonne
        dfcopie[colonne] = (dfcopie[colonne] - minval) / (maxval - minval) #normaliser la valeur cellule
    return dfcopie

#fonction qui initialise la matrice selon la dataset donné
def initialiser_matrice(matrice : pd.DataFrame, df : pd.DataFrame):
    lignes = df.index.tolist()
    for i in lignes:
        for j in lignes:
            matrice.at[i, j] = dist_euclidienne(df.at[i, df.columns[0]], df.at[i, df.columns[1]], df.at[j, df.columns[0]], df.at[j, df.columns[1]])

#fonction qui retourne l'index du minimum dans la matrice
def indexMin(matrice : pd.DataFrame):
    minimum = matrice.iloc[1, 0] #initialiser le minimum
    indexlg = 1
    indexcol = 0
    for i in range(matrice.shape[0]):
        for j in range(i): 
            if matrice.iloc[i, j] < minimum:
                indexlg = i
                indexcol = j
                minimum = matrice.iloc[i, j]
    return indexlg, indexcol

def afficher_matrice(matrice: pd.DataFrame):
    labels = matrice.columns.tolist()
    df = pd.DataFrame(matrice, index=labels, columns=labels)

    table_styles = [
    {'selector': 'th', 'props': [('background-color', '#ced4da')]}, 
    {'selector': 'td:first-child', 'props': [('background-color', '#ced4da')]}, 
    ]
    styled_df = df.style.set_caption('Matrice des distances') \
                        .set_table_styles(table_styles) \
                        .set_table_attributes('border="1"') \
                        .set_properties(**{'text-align': 'center', 'font-size': '11px'})
    display(styled_df)