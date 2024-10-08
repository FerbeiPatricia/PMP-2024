import numpy as np
import matplotlib.pyplot as plt
import arviz as az

# Parametrii pentru distribuțiile exponențiale
lambdas = [3, 6, 4]  # ratele λ1 = 3, λ2 = 6, λ3 = 4
probabilities = [3/13, 6/13, 4/13]  # probabilitățile corespunzătoare fiecărui frizer

# Generăm 10.000 de mostre pentru timpul de servire X
n_samples = 10000

# Alegem frizerul în funcție de probabilități
choices = np.random.choice([0, 1, 2], size=n_samples, p=probabilities)

# Inițializăm vectorul de timp de servire
X = np.zeros(n_samples)

# Generăm timpul de servire X pe baza frizerului ales
for i, lam in enumerate(lambdas):
    X[choices == i] = np.random.exponential(scale=1/lam, size=np.sum(choices == i))

# Calculăm media și deviația standard a timpilor de servire X
mean_X = np.mean(X)
std_X = np.std(X)

# Afișăm rezultatele
print(f"Media estimată a lui X: {mean_X:.3f} ore")
print(f"Deviația standard estimată a lui X: {std_X:.3f} ore")

# Graficul densității aproximative a distribuției lui X
az.plot_kde(X, label='Densitatea estimată', bw=0.1)
plt.title('Densitatea aproximativă a timpului de servire (X)')
plt.xlabel('Timp (ore)')
plt.ylabel('Densitate')
plt.legend()
plt.show()
