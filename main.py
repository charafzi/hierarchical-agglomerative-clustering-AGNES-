import pandas as pd
import numpy as np
from package import *

data = pd.read_csv('dataAgnes.csv',index_col=0)
df = pd.DataFrame(data)
df

def agnes(df, nbclusters = 1):
    colonnes = df.columns.tolist() #labels des colonnes
    lignes = df.index.tolist()     #labels des lignes
    
    #normaliser la dataset
    df = normaliser(df)
    
    # création et initialisation de la matrice
    matrice = pd.DataFrame(index=lignes, columns=lignes)
    initialiser_matrice(matrice, df) 
    afficher_matrice(matrice)

    while len(matrice) > nbclusters :
        i,j=indexMin(matrice)
        #récupérer les éléments les plus proches
        g1=matrice.columns[j] #
        g2=matrice.columns[i]
        supp= ""+matrice.columns[i] #élément à enlever de la matrice
        nv_etiq = g1+"-"+g2
        #recalculer la matrice
        for k in range(0,len(matrice)):
            minimum = min(matrice.iloc[k, j],matrice.iloc[k, i])
            matrice.iloc[k, j] = minimum
            matrice.iloc[j, k] = minimum
        matrice.drop(g2, axis=1, inplace=True)
        matrice.drop(g2, inplace=True)
        matrice.rename(columns={g1: nv_etiq}, inplace=True)
        matrice.rename(index={g1: nv_etiq}, inplace=True)
        afficher_matrice(matrice)

agnes(df,2)