#coding:utf8

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import os


"""
dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']
"""

# Question 1
if not os.path.exists('img'):
    os.makedirs('img')


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import os


if not os.path.exists('img'):
    os.makedirs('img')

# Lois discrètes

plt.figure()
x_dirac = np.arange(-2, 5)
y_dirac = [0, 0, 1, 0, 0, 0, 0] 
plt.stem(x_dirac, y_dirac)
plt.title("Loi de Dirac (concentration sur 0)")
plt.savefig('img/dirac.png')


low, high = 1, 7
x_unif = np.arange(low, high)
y_unif = stats.planck.pmf(x_unif, 0.5)
plt.figure()
plt.bar(x_unif, [1/6]*6)
plt.title("Loi Uniforme Discrète")
plt.savefig('img/uniforme_discrete.png')


n, p = 10, 0.5
x_binom = np.arange(0, n+1)
plt.figure()
plt.bar(x_binom, stats.binom.pmf(x_binom, n, p))
plt.title(f"Loi Binomiale (n={n}, p={p})")
plt.savefig('img/binomiale.png')


mu = 3
x_poisson = np.arange(0, 15)
plt.figure()
plt.bar(x_poisson, stats.poisson.pmf(x_poisson, mu))
plt.title(f"Loi de Poisson (mu={mu})")
plt.savefig('img/poisson_discret.png')


a = 2.0
x_zipf = np.arange(1, 11)
plt.figure()
plt.bar(x_zipf, stats.zipf.pmf(x_zipf, a))
plt.title("Loi de Zipf (a=2)")
plt.savefig('img/zipf.png')


# Lois continues

x_cont = np.linspace(-5, 15, 500)

plt.figure()
plt.plot(x_cont, stats.norm.pdf(x_cont, 0, 1))
plt.title("Loi Normale (moyenne=0, ecart-type=1)")
plt.savefig('img/normale.png')

plt.figure()
plt.plot(x_cont, stats.lognorm.pdf(x_cont, 1))
plt.title("Loi Log-Normale")
plt.savefig('img/lognormale.png')

plt.figure()
plt.plot(x_cont, stats.chi2.pdf(x_cont, df=3))
plt.title("Loi du Chi2 (3 degrés de liberté)")
plt.savefig('img/chi2.png')

plt.figure()
x_pareto = np.linspace(1, 10, 500)
plt.plot(x_pareto, stats.pareto.pdf(x_pareto, b=2.6))
plt.title("Loi de Pareto (b=2.6)")
plt.savefig('img/pareto.png')

plt.show()

# Question 2

def calculer_stats(nom_loi, distribution):
    """
    Fonction qui calcule et affiche la moyenne et l'écart-type 
    d'une distribution scipy.stats
    """
  
    moyenne, variance = distribution.stats(moments='mv')
    ecart_type = np.sqrt(variance) 
    
    print(f"--- {nom_loi} ---")
    print(f"Moyenne théorique : {moyenne:.2f}")
    print(f"Écart-type théorique : {ecart_type:.2f}\n")
    return moyenne, ecart_type



print("CALCUL DES PARAMÈTRES DES LOIS :\n")

# Lois Discrètes (on reprend les paramètres utilisés pour les graphiques)
calculer_stats("Loi Binomiale (n=10, p=0.5)", stats.binom(n=10, p=0.5))
calculer_stats("Loi de Poisson (mu=3)", stats.poisson(mu=3))
calculer_stats("Loi de Zipf (a=2)", stats.zipf(a=2))

# Lois Continues
calculer_stats("Loi Normale (0, 1)", stats.norm(loc=0, scale=1))
calculer_stats("Loi Log-Normale (s=1)", stats.lognorm(s=1))
calculer_stats("Loi du Chi2 (df=3)", stats.chi2(df=3))
calculer_stats("Loi de Pareto (b=2.6)", stats.pareto(b=2.6))