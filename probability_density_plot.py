import numpy as np
import matplotlib.pyplot as plt

# Définir la fonction de densité de probabilité
def pdf(x):
    return 1 - np.abs(x) if np.abs(x) < 1 else 0

# Créer un espace de valeurs pour x
x = np.linspace(-1.5, 1.5, 1000)
y = np.array([pdf(xi) for xi in x])

# Tracer le graphe
plt.plot(x, y, label='f(x) = 1 - |x|', color='blue')
plt.fill_between(x, y, alpha=0.3, color='blue')
plt.title("Graph of the Probability Density Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
