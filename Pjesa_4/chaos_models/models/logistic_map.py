"""Modeli i hartës logjistike për studimin e kaosit determinist."""
from __future__ import annotations

import numpy as np


class LogisticMap:
    """Implementim i hartës logjistike.

    Ekuacioni:
        x_{n+1} = r x_n (1 - x_n)
    """

    def __init__(self, r: float = 3.7, x0: float = 0.2) -> None:
        if not (0.0 <= x0 <= 1.0):
            raise ValueError("x0 duhet të jetë në intervalin [0, 1].")
        self.r = float(r)
        self.x0 = float(x0)

    def iterate(self, n_steps: int) -> np.ndarray:
        """Kthen orbitën diskrete me gjatësi n_steps + 1."""
        if n_steps < 1:
            raise ValueError("n_steps duhet të jetë numër pozitiv.")
        x = np.empty(n_steps + 1, dtype=float)
        x[0] = self.x0
        for i in range(n_steps):
            x[i + 1] = self.r * x[i] * (1.0 - x[i])
        return x

    @staticmethod
    def iterate_many(r_values: np.ndarray, x0: float, n_steps: int, discard: int = 1000) -> np.ndarray:
        """Iteron shumë vlera të parametrit r në mënyrë vektoriale.

        Përdoret për diagramin e bifurkacionit.
        """
        if discard < 0:
            raise ValueError("discard duhet të jetë jo-negativ.")
        if n_steps < 1:
            raise ValueError("n_steps duhet të jetë numër pozitiv.")
        x = np.full_like(r_values, fill_value=x0, dtype=float)
        for _ in range(discard):
            x = r_values * x * (1.0 - x)
        out = np.empty((n_steps, len(r_values)), dtype=float)
        for i in range(n_steps):
            x = r_values * x * (1.0 - x)
            out[i, :] = x
        return out
