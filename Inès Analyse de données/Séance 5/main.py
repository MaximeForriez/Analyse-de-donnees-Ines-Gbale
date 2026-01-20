#coding:utf8
import pandas as pd
import math
import scipy.stats
import os

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

dossier_actuel = os.path.dirname(os.path.abspath(__file__))
chemin_ech = os.path.join(dossier_actuel, 'data', 'Echantillonnage-100-Echantillons.csv')

donnees = ouvrirUnFichier(chemin_ech)

print("--- Résultat sur le calcul d'un intervalle de fluctuation ---")
moyennes = donnees.mean().round(0)
print(moyennes)

frequences_echantillons = (moyennes / moyennes.sum()).round(2)

pop_mere = {'Pour': 852, 'Contre': 911, 'Sans opinion': 422}
total_pop = 2185
f_mere = {k: round(v / total_pop, 2) for k, v in pop_mere.items()}

zc = 1.96
for opinion, p in f_mere.items():
    marge = zc * math.sqrt((p * (1 - p)) / total_pop)
    print(f"{opinion} : [{round(p - marge, 2)} ; {round(p + marge, 2)}]")

print("\n--- Résultat sur le calcul d'un intervalle de confiance ---")
premier_ech_list = list(donnees.iloc[0])
taille_ech1 = sum(premier_ech_list)
f_isole = [round(val / taille_ech1, 2) for val in premier_ech_list]

labels = ["Pour", "Contre", "Sans opinion"]
for i in range(len(f_isole)):
    f = f_isole[i]
    m_conf = zc * math.sqrt((f * (1 - f)) / taille_ech1)
    print(f"{labels[i]} : [{round(f - m_conf, 2)} ; {round(f + m_conf, 2)}]")

print("\n--- Théorie de la décision ---")
t1_path = os.path.join(dossier_actuel, 'data', 'Loi-normale-Test-1.csv')
t2_path = os.path.join(dossier_actuel, 'data', 'Loi-normale-Test-2.csv')

for path, nom in [(t1_path, "Test 1"), (t2_path, "Test 2")]:
    df_test = ouvrirUnFichier(path)
    stat, p_val = scipy.stats.shapiro(df_test.iloc[:, 0])
    resultat = "NORMALE" if p_val > 0.05 else "PAS NORMALE"
    print(f"{nom} : p-value = {p_val:.4f} -> {resultat}")

    # Théorie de l'estimation
print("\n--- Résultat sur le calcul d'un intervalle de confiance ---")

premier_echantillon_pandas = donnees.iloc[0]
premier_echantillon_list = list(premier_echantillon_pandas)

taille_ech1 = sum(premier_echantillon_list)
f_isole = [round(val / taille_ech1, 2) for val in premier_echantillon_list]

print(f"Effectif total de l'échantillon isolé : {taille_ech1}")
print(f"Fréquences observées (Pour, Contre, Sans opinion) : {f_isole}")

zc = 1.96
opinions = ["Pour", "Contre", "Sans opinion"]

print("\nIntervalles de confiance calculés :")
for i in range(len(f_isole)):
    f = f_isole[i]
    marge_erreur = zc * math.sqrt((f * (1 - f)) / taille_ech1)
    borne_inf = round(f - marge_erreur, 2)
    borne_sup = round(f + marge_erreur, 2)
    print(f"{opinions[i]} : [{borne_inf} ; {borne_sup}]")

    # Théorie de la décision
print("\n--- Théorie de la décision ---")

t1_path = os.path.join(dossier_actuel, 'data', 'Loi-normale-Test-1.csv')
t2_path = os.path.join(dossier_actuel, 'data', 'Loi-normale-Test-2.csv')

for path, nom in [(t1_path, "Test 1"), (t2_path, "Test 2")]:
    df_test = ouvrirUnFichier(path)
    stat, p_val = scipy.stats.shapiro(df_test.iloc[:, 0])
    resultat = "NORMALE" if p_val > 0.05 else "PAS NORMALE"
    print(f"{nom} : p-value = {p_val:.4f} -> {resultat}")