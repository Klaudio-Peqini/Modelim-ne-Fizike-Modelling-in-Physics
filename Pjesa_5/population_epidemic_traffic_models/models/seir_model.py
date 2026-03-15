
import numpy as np
from scipy.integrate import solve_ivp

def seir_equations(t, y, beta, sigma, gamma):
    S, E, I, R = y
    dS = -beta * S * I
    dE = beta * S * I - sigma * E
    dI = sigma * E - gamma * I
    dR = gamma * I
    return [dS, dE, dI, dR]

def simulate_seir(beta=0.4, sigma=0.2, gamma=0.1, S0=0.99, E0=0.0, I0=0.01, R0=0.0, t_max=100):
    t = np.linspace(0, t_max, 400)
    sol = solve_ivp(seir_equations, [0, t_max], [S0, E0, I0, R0], args=(beta, sigma, gamma), t_eval=t)
    return sol.t, sol.y
