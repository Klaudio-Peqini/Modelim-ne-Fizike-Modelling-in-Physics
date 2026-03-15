
import numpy as np
from scipy.integrate import solve_ivp

def sir_equations(t, y, beta, gamma):
    S, I, R = y
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

def simulate_sir(beta=0.4, gamma=0.1, S0=0.99, I0=0.01, R0=0.0, t_max=100):
    t = np.linspace(0, t_max, 400)
    sol = solve_ivp(sir_equations, [0, t_max], [S0, I0, R0], args=(beta, gamma), t_eval=t)
    return sol.t, sol.y
