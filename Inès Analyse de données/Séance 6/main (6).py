#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
import os

# Les fonctions locales

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        if element > 0:
            log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element1][1]])
    return classement

# La partie sur les îles

dossier_actuel = os.path.dirname(os.path.abspath(__file__))

# Recherche de mon fichier

noms_possibles = ["island-index (1).csv", "island-index.csv", "island-index (1)"]
dossiers_possibles = [dossier_actuel, os.path.join(dossier_actuel, "data")]

chemin_iles = None

for dossier in dossiers_possibles:
    for nom in noms_possibles:
        test_chemin = os.path.join(dossier, nom)
        if os.path.exists(test_chemin):
            chemin_iles = test_chemin
            break

if chemin_iles:
    iles = ouvrirUnFichier(chemin_iles)
    print(f"Fichier trouvé : {chemin_iles}")
    
    
    surfaces_iles = list(iles["Surface (km²)"])
    surfaces_iles.append(85545323)
    surfaces_iles.append(37856841)
    surfaces_iles.append(7768030)
    surfaces_iles.append(7605049)
    
    surfaces_globales = ordreDecroissant(surfaces_iles)
    log_surfaces = conversionLog(surfaces_globales)
    
    rangs = list(range(1, len(surfaces_globales) + 1))
    log_rangs = conversionLog(rangs)
    
    print("--- RÉSULTATS ÎLES ---")
    print(f"Nombre d'éléments : {len(surfaces_globales)}")
else:
    print("ERREUR : Fichier toujours introuvable.")
    print(f"Contenu du dossier actuel : {os.listdir(dossier_actuel)}")


if not os.path.exists(chemin_iles):
    chemin_iles = os.path.join(dossier_actuel, "island-index (1).csv")

try:
    iles = ouvrirUnFichier(chemin_iles)
    
    
    surfaces_iles = list(iles["Surface (km²)"])
# km2 est différent de exposant 2 
   
    surfaces_iles.append(85545323) # Asie / Afrique / Europe
    surfaces_iles.append(37856841) # Amérique
    surfaces_iles.append(7768030)  # Antarctique
    surfaces_iles.append(7605049)  # Australie

    
    surfaces_globales = ordreDecroissant(surfaces_iles)

    
    log_surfaces = conversionLog(surfaces_globales)

   
    rangs = list(range(1, len(surfaces_globales) + 1))
    log_rangs = conversionLog(rangs)

    print("--- RÉSULTATS ÎLES ---")
    print(f"Nombre d'éléments traités : {len(surfaces_globales)}")
    print(f"Plus grande surface (log) : {log_surfaces[0]:.2f}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier est introuvable. Vérifie qu'il est bien ici : {chemin_iles}")
except KeyError:
    print("ERREUR : La colonne 'Surface (km²)' est introuvable. Vérifie l'orthographe (avec le petit 2).")

# Partie sur le monde

chemin_monde = os.path.join(dossier_actuel, "data", "Le-Monde-HS-Etats-du-monde-2007-2025.csv")
if not os.path.exists(chemin_monde):
    chemin_monde = os.path.join(dossier_actuel, "Le-Monde-HS-Etats-du-monde-2007-2025.csv")

try:
    monde = ouvrirUnFichier(chemin_monde)
    print("\n--- RÉSULTATS MONDE ---")
    print("Fichier Monde chargé avec succès.")
except:
    pass

# Question 4
surfaces_globales = ordreDecroissant(surfaces_iles)

# Question 5 & 6
rangs = list(range(1, len(surfaces_globales) + 1))


log_surfaces = conversionLog(surfaces_globales)
log_rangs = conversionLog(rangs)

plt.figure(figsize=(10, 6))
plt.plot(log_rangs, log_surfaces, 'b.') # Points bleus
plt.xlabel("Logarithme du Rang")
plt.ylabel("Logarithme de la Surface")
plt.title("Loi rang-taille des surfaces terrestres (Log-Log)")
plt.grid(True)
plt.savefig("loi_rang_taille_iles.png")


# Question 7
# RÉPONSE : Oui, il est possible de faire un test sur les rangs. 
# On utilise des tests non-paramétriques comme le coefficient de corrélation de Spearman 
# ou le Tau de Kendall pour mesurer la force de la relation entre deux classements.

# Question 8
chemin_monde = os.path.join(dossier_actuel, "data", "Le-Monde-HS-Etats-du-monde-2007-2025.csv")

# Question 9
monde = ouvrirUnFichier(chemin_monde)

# Question 10
etats = list(monde["État"])
pop_2007 = list(monde["Pop 2007"])
pop_2025 = list(monde["Pop 2025"])
densite_2007 = list(monde["Densité 2007"])
densite_2025 = list(monde["Densité 2025"])

print(f"Nombre de pays qui ont été isolés : {len(etats)}")

# Étapes 11 à 14
rang_pop_2007 = ordrePopulation(pop_2007, etats)
rang_pop_2025 = ordrePopulation(pop_2025, etats)
rang_dens_2007 = ordrePopulation(densite_2007, etats)
rang_dens_2025 = ordrePopulation(densite_2025, etats)

comparaison_2007 = classementPays(rang_pop_2007, rang_dens_2007)
comparaison_2007.sort()

liste_rangs_pop = []
liste_rangs_dens = []

for ligne in comparaison_2007:
    liste_rangs_pop.append(ligne[0])
    liste_rangs_dens.append(ligne[1])

rho_spearman, p_val_s = scipy.stats.spearmanr(liste_rangs_pop, liste_rangs_dens)
tau_kendall, p_val_k = scipy.stats.kendalltau(liste_rangs_pop, liste_rangs_dens)

print(f"Spearman 2007 : {rho_spearman:.4f}")
print(f"Kendall 2007 : {tau_kendall:.4f}")

# Bonus
def calculerCoefficientsRangs(classement1, classement2):
    comparaison = classementPays(classement1, classement2)
    comparaison.sort()
    
    r1 = []
    r2 = []
    for ligne in comparaison:
        r1.append(ligne[0])
        r2.append(ligne[1])
    
    rho, _ = scipy.stats.spearmanr(r1, r2)
    tau, _ = scipy.stats.kendalltau(r1, r2)
    
    return rho, tau

# Concordance de 2007 à 2025
etats_liste = list(monde["État"])
resultats_temporels = []

# Algorithme : Pour chaque année : Pop vs Densité
for annee in range(2007, 2026):
    col_pop = f"Pop {annee}"
    col_dens = f"Densité {annee}"
    
    r_pop = ordrePopulation(list(monde[col_pop]), etats_liste)
    r_dens = ordrePopulation(list(monde[col_dens]), etats_liste)
    
    s, k = calculerCoefficientsRangs(r_pop, r_dens)
    resultats_temporels.append([annee, s, k])

