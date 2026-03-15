"""Llogaritje të thjeshta të eksponentëve të Ljapunovit."""
from __future__ import annotations

import numpy as np

from models.logistic_map import LogisticMap
from models.lorenz_system import LorenzSystem


def lyapunov_logistic(r: float, x0: float = 0.2, n_steps: int = 5000, discard: int = 1000) -> float:
    """Eksponenti i Ljapunovit për hartën logjistike.

    Formula e përdorur:
        lambda = lim (1/N) sum ln |f'(x_n)|,
    ku f'(x) = r (1 - 2x).
    """
    model = LogisticMap(r=r, x0=x0)
    orbit = model.iterate(n_steps + discard)
    orbit = orbit[discard:]
    derivative = np.abs(r * (1.0 - 2.0 * orbit[:-1]))
    derivative = np.clip(derivative, 1.0e-14, None)
    return float(np.mean(np.log(derivative)))


def lyapunov_scan_logistic(
    r_min: float = 2.5,
    r_max: float = 4.0,
    n_r: int = 800,
    x0: float = 0.2,
    n_steps: int = 4000,
    discard: int = 1000,
) -> tuple[np.ndarray, np.ndarray]:
    """Skanim i eksponentit të Ljapunovit në funksion të parametrit r."""
    r_values = np.linspace(r_min, r_max, n_r)
    lambdas = np.array(
        [lyapunov_logistic(r, x0=x0, n_steps=n_steps, discard=discard) for r in r_values],
        dtype=float,
    )
    return r_values, lambdas


def separation_growth_lorenz(
    delta0: float = 1.0e-8,
    t_max: float = 20.0,
    dt: float = 0.01,
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Ndjek rritjen e distancës mes dy trajektoreve shumë pranë njëra-tjetrës.

    Kjo jep një vlerësim pedagogjik të ndjeshmërisë ndaj kushteve fillestare.
    """
    base = LorenzSystem(sigma=sigma, rho=rho, beta=beta, initial_state=(1.0, 1.0, 1.0))
    pert = LorenzSystem(sigma=sigma, rho=rho, beta=beta, initial_state=(1.0 + delta0, 1.0, 1.0))
    t, traj1 = base.solve(t_max=t_max, dt=dt)
    _, traj2 = pert.solve(t_max=t_max, dt=dt)
    dist = np.linalg.norm(traj1 - traj2, axis=1)
    dist = np.clip(dist, 1.0e-16, None)
    return t, dist
