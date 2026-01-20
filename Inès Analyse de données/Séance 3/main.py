import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    BASE_DIR,
    "data",
    "resultats-elections-presidentielles-2022-1er-tour.csv"
)

contenu = pd.read_csv(csv_path)



dossier_script = os.path.dirname(__file__)


chemin_fichier = os.path.join(
    dossier_script,
    "data",
    "resultats-elections-presidentielles-2022-1er-tour.csv"
)

# Question 4
with open(chemin_fichier, mode="r", encoding="utf-8") as fichier:
    df = pd.read_csv(fichier, sep=";")

print(df.head())

# Question 5
import numpy as np


colonnes_quantitatives = []

for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]:
        colonnes_quantitatives.append(col)

df_quant = contenu[colonnes_quantitatives]

print("\nColonnes quantitatives :")
print(colonnes_quantitatives)


# Moyennes #
moyennes = df_quant.mean().round(2).tolist()

# Médianes #
medianes = df_quant.median().round(2).tolist()

# Modes #
modes = df_quant.mode().iloc[0].round(2).tolist()

# Écarts-types #
ecarts_types = df_quant.std().round(2).tolist()

# Écart absolu à la moyenne #
ecarts_absolus_moyenne = (
    df_quant
    .sub(df_quant.mean())
    .abs()
    .mean()
    .round(2)
    .tolist()
)

# Étendue #
etendues = (df_quant.max() - df_quant.min()).round(2).tolist()

print("\n--- Paramètres statistiques ---")

print("Moyennes :", moyennes)
print("Médianes :", medianes)
print("Modes :", modes)
print("Écarts-types :", ecarts_types)
print("Écarts absolus à la moyenne :", ecarts_absolus_moyenne)
print("Étendues :", etendues)


import pandas as pd
import os


dossier_actuel = os.path.dirname(os.path.abspath(__file__))


chemin_fichier = os.path.join(dossier_actuel, 'data', 'resultats-elections-presidentielles-2022-1er-tour.csv')


df = pd.read_csv(chemin_fichier)

# Question 7
df_quantitatif = df.select_dtypes(include=['number'])

# Calcul de la distance interquartile (Q3 - Q1)
iqr = df_quantitatif.quantile(0.75) - df_quantitatif.quantile(0.25)

# Calcul de la distance interdécile (D9 - D1)
interdecile = df_quantitatif.quantile(0.9) - df_quantitatif.quantile(0.1)

print("Distance Interquartile :\n", iqr)
print("\nDistance Interdécile :\n", interdecile)



import matplotlib.pyplot as plt
import os


dossier_script = os.path.dirname(os.path.abspath(__file__))


chemin_img = os.path.join(dossier_script, 'img')

# Question 8
if not os.path.exists(chemin_img):
    os.makedirs(chemin_img)
    print(f"Dossier créé ici : {chemin_img}")


for col in df_quantitatif.columns:
    plt.figure(figsize=(8, 6))
    plt.boxplot(df_quantitatif[col].dropna())
    plt.title(f'Répartition : {col}')
    plt.ylabel('Valeurs')
    
   
    nom_propre = col.replace(' ', '_').replace('.', '_')
    
    plt.savefig(os.path.join(chemin_img, f'boxplot_{nom_propre}.png'))
    
    plt.close()


import pandas as pd
import os

# Question 10
dossier_script = os.path.dirname(os.path.abspath(__file__))
chemin_iles = os.path.join(dossier_script, 'data', 'island-index.csv')

try:
   
    df_iles = pd.read_csv(chemin_iles, sep=',', low_memory=False)
    
    
    if 'Surface (km2)' not in df_iles.columns and 'Surface (km²)' not in df_iles.columns:
        df_iles = pd.read_csv(chemin_iles, sep=';', low_memory=False)

    
    df_iles.columns = df_iles.columns.str.strip()
    
   
    col_surface = ""
    for c in df_iles.columns:
        if 'Surface' in c:
            col_surface = c
            break
            
    if col_surface == "":
        print(f"Colonnes trouvées : {list(df_iles.columns)}")
        raise KeyError("Impossible de trouver une colonne contenant 'Surface'")

    print(f"Fichier lu ! Colonne utilisée : '{col_surface}'")

  
    bornes = [0, 10, 25, 50, 100, 2500, 5000, 10000, float('inf')]
    noms_labels = ["]0, 10]", "]10, 25]", "]25, 50]", "]50, 100]", 
                   "]100, 2500]", "]2500, 5000]", "]5000, 10000]", "> 10000"]

    
    df_iles[col_surface] = pd.to_numeric(df_iles[col_surface], errors='coerce')

    df_iles['Classe_Surface'] = pd.cut(
        df_iles[col_surface], 
        bins=bornes, 
        labels=noms_labels,
        right=True
    )

    comptage = df_iles['Classe_Surface'].value_counts().sort_index()
    print("\nRésultat du dénombrement :")
    print(comptage)

except Exception as e:
    print(f"Erreur : {e}")


import os
import pandas as pd

# Bonus


df_export = comptage.reset_index()


df_export.columns = ['Tranche de Surface', 'Nombre d\'îles']


chemin_csv = os.path.join(dossier_script, 'resultat_categories_iles.csv')
chemin_excel = os.path.join(dossier_script, 'resultat_categories_iles.xlsx')

try:

    df_export.to_csv(chemin_csv, index=False, sep=';', encoding='utf-8-sig')
    
  
    df_export.to_excel(chemin_excel, index=False, sheet_name='Categories Iles')
    
    print("--- BONUS RÉUSSI ---")
    print(f"Fichier CSV créé : {chemin_csv}")
    print(f"Fichier Excel créé : {chemin_excel}")

except Exception as e:
    print(f"Erreur lors de l'export : {e}")