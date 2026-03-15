
import numpy as np

def simulate_population_growth(r=0.2, N0=10, t_max=50, steps=500):
    t = np.linspace(0, t_max, steps)
    N = N0 * np.exp(r * t)
    return t, N
