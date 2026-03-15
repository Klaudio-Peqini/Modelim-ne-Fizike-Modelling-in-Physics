
import numpy as np
from scipy.integrate import solve_ivp

def logistic_equation(t, N, r, K):
    return r * N * (1 - N / K)

def simulate_logistic(r=0.3, K=100, N0=5, t_max=100):
    t = np.linspace(0, t_max, 400)
    sol = solve_ivp(logistic_equation, [0, t_max], [N0], args=(r, K), t_eval=t)
    return sol.t, sol.y[0]
