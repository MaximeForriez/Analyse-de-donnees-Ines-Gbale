# Élements de corrections

## Séance 2.

### Questions

- **Question 8.** Il n'existe aucune hiérarchie entre les caractères qualitatifs et les caractères quantitatifs.

### Code

- Excellent !

## Séance 3.

### Questions

- **Question 5.** L'écart à la moyenne peut être non nul.

- **Question 6.** Il manque la partie sur la symétrie.

### Code

- Excellent !

## Séance 4

### Questions

- Il manque beaucoup d'éléments.

### Code

- Excellent !

## Séance 5

### Questions

- Excellent !

### Code

- Excellent !

- Vous êtes une des rares personnes qui a trouvé la bonne $p-value$ pour la distribution test1.

## Séance 6

### Questions

- Il manque beaucoup d'éléments.

### Code

- Problème d'encodage !

- Le résultat est faux pour les tests. Vous avez écrit :

```
    rho_spearman, p_val_s = scipy.stats.spearmanr(liste_rangs_pop, liste_rangs_dens)
    tau_kendall, p_val_k = scipy.stats.kendalltau(liste_rangs_pop, liste_rangs_dens)
```

Il aurait fallu écrit quelque chose comme :

```
    rho_spearman_pop, p_val_s_pop = scipy.stats.spearmanr(liste_rangs_pop_2007, liste_rangs_pop_2025)
    tau_kendall_pop, p_val_k_pop = scipy.stats.kendalltau(liste_rangs_pop_2007, liste_rangs_pop_2025)

    rho_spearman, p_val_s = scipy.stats.spearmanr(liste_rangs_dens_2007, liste_rangs_dens_2025_)
    tau_kendall, p_val_k = scipy.stats.kendalltau(liste_rangs_dens_2007, liste_rangs_dens_2025)
```

## Humanités numériques

- Aucun rendu.

## Remarques générales

- Aucun dépôt régulier sur `GitHub`.

- Attention ! Vous mettez du code `LaTeX` dans un fichier de traitement texte.

- Attention ! Vous devez appeler votre fichier de code `main.py`. Vous comprendrez si vous faites un jour du `Python` avancé.

- Module parfaitement compris, comme l'établit vos liens entre les questions de cours et les exercices de code.
