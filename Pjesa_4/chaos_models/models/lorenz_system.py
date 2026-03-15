"""Sistemi i Lorencit dhe integrimi numerik i tij."""
from __future__ import annotations

import numpy as np


def lorenz_rhs(state: np.ndarray, sigma: float, rho: float, beta: float) -> np.ndarray:
    """Anët e djathta të sistemit të Lorencit."""
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz], dtype=float)


class LorenzSystem:
    """Zgjidhja numerike e sistemit të Lorencit me metodën RK4."""

    def __init__(
        self,
        sigma: float = 10.0,
        rho: float = 28.0,
        beta: float = 8.0 / 3.0,
        initial_state: tuple[float, float, float] = (1.0, 1.0, 1.0),
    ) -> None:
        self.sigma = float(sigma)
        self.rho = float(rho)
        self.beta = float(beta)
        self.initial_state = np.array(initial_state, dtype=float)

    def rk4_step(self, state: np.ndarray, dt: float) -> np.ndarray:
        """Një hap RK4."""
        k1 = lorenz_rhs(state, self.sigma, self.rho, self.beta)
        k2 = lorenz_rhs(state + 0.5 * dt * k1, self.sigma, self.rho, self.beta)
        k3 = lorenz_rhs(state + 0.5 * dt * k2, self.sigma, self.rho, self.beta)
        k4 = lorenz_rhs(state + dt * k3, self.sigma, self.rho, self.beta)
        return state + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    def solve(self, t_max: float = 40.0, dt: float = 0.01) -> tuple[np.ndarray, np.ndarray]:
        """Integron sistemin në intervalin [0, t_max]."""
        if t_max <= 0:
            raise ValueError("t_max duhet të jetë pozitiv.")
        if dt <= 0:
            raise ValueError("dt duhet të jetë pozitiv.")
        n_steps = int(t_max / dt)
        t = np.linspace(0.0, n_steps * dt, n_steps + 1)
        traj = np.empty((n_steps + 1, 3), dtype=float)
        traj[0] = self.initial_state.copy()
        state = self.initial_state.copy()
        for i in range(n_steps):
            state = self.rk4_step(state, dt)
            traj[i + 1] = state
        return t, traj
