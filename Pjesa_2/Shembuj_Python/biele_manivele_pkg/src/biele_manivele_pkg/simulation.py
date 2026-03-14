import numpy as np
from .parameters import CrankRodParameters

def piston_position(theta: np.ndarray, r: float, l: float) -> np.ndarray:
    return r * np.cos(theta) + np.sqrt(l**2 - (r * np.sin(theta))**2)

def simulate(params: CrankRodParameters) -> dict:
    params.validate()

    t = np.linspace(0.0, params.duration, params.n_points)
    theta = params.omega * t
    x = piston_position(theta, params.r, params.l)

    dt = t[1] - t[0]
    v = np.gradient(x, dt)
    a = np.gradient(v, dt)

    crank_x = params.r * np.cos(theta)
    crank_y = params.r * np.sin(theta)

    return {
        "t": t,
        "theta": theta,
        "x_piston": x,
        "v_piston": v,
        "a_piston": a,
        "crank_x": crank_x,
        "crank_y": crank_y,
        "r": params.r,
        "l": params.l,
        "omega": params.omega,
    }
