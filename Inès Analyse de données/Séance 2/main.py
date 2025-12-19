# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import os


csv_path = "data/resultats-elections-presidentielles-2022-1er-tour.csv"
contenu = pd.read_csv(csv_path)


# Question 1 

print(contenu.head())
print("Nombre de lignes :", len(contenu))
print("Nombre de colonnes :", len(contenu.columns))

print("\n--- Types des colonnes ---")
print(contenu.dtypes)


# Question 6 

nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)
print("Lignes :", nb_lignes)
print("Colonnes :", nb_colonnes)


# Question 7 

types_colonnes = []

for col in contenu.columns:
    dtype = contenu[col].dtype
    if pd.api.types.is_integer_dtype(dtype):
        types_colonnes.append("int")
    elif pd.api.types.is_float_dtype(dtype):
        types_colonnes.append("float")
    elif pd.api.types.is_bool_dtype(dtype):
        types_colonnes.append("bool")
    else:
        types_colonnes.append("str")

for nom, t in zip(contenu.columns, types_colonnes):
    print(nom, ":", t)


# Question 10 

print("\n--- Sommes des colonnes quantitatives ---")
for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]:
        print(col, ":", contenu[col].sum())


# Question 11

os.makedirs("images_barres", exist_ok=True)

for i in range(len(contenu)):
    dept = contenu.loc[i, "Libellé du département"]
    inscrits = contenu.loc[i, "Inscrits"]
    votants = contenu.loc[i, "Votants"]

    plt.figure(figsize=(6, 4))
    plt.bar(["Inscrits", "Votants"], [inscrits, votants])
    plt.title(dept)
    plt.ylabel("Nombre de personnes")

    nom_propre = dept.replace(" ", "_").replace("/", "_").replace("'", "")
    plt.savefig(f"images_barres/{nom_propre}.png")
    plt.close()


# Question 12 

os.makedirs("images_pie", exist_ok=True)

for i in range(len(contenu)):
    dept = contenu.loc[i, "Libellé du département"]

    valeurs = [
        contenu.loc[i, "Blancs"],
        contenu.loc[i, "Nuls"],
        contenu.loc[i, "Exprimés"],
        contenu.loc[i, "Abstentions"],
    ]

    labels = ["Blancs", "Nuls", "Exprimés", "Abstentions"]

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title(dept)

    nom_propre = dept.replace(" ", "_").replace("/", "_").replace("'", "")
    plt.savefig(f"images_pie/{nom_propre}.png")
    plt.close()


# Question 13 

plt.figure(figsize=(8, 6))
plt.hist(contenu["Inscrits"], bins=20, edgecolor="black")
plt.title("Distribution des inscrits par département")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Nombre de départements")
plt.savefig("histogramme_inscrits.png")
plt.close()


