"""Vizualizime për bifurkacionin e hartës logjistike."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from models.logistic_map import LogisticMap
from models.lyapunov import lyapunov_scan_logistic


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def plot_bifurcation(
    r_min: float = 2.5,
    r_max: float = 4.0,
    n_r: int = 2000,
    keep_last: int = 200,
    discard: int = 1000,
    x0: float = 0.2,
    savepath: str | Path = OUTPUT_DIR / "bifurkacioni_logjistik.png",
) -> Path:
    """Gjeneron diagramin e bifurkacionit."""
    r_values = np.linspace(r_min, r_max, n_r)
    points = LogisticMap.iterate_many(r_values, x0=x0, n_steps=keep_last, discard=discard)

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(keep_last):
        ax.plot(r_values, points[i], ",", alpha=0.25)
    ax.set_title("Diagrami i bifurkacionit për hartën logjistike")
    ax.set_xlabel("Parametri r")
    ax.set_ylabel("Vlerat asimptotike të x_n")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath


def plot_lyapunov_scan(
    r_min: float = 2.5,
    r_max: float = 4.0,
    n_r: int = 800,
    savepath: str | Path = OUTPUT_DIR / "lyapunov_logjistik.png",
) -> Path:
    """Vizaton eksponentin e Ljapunovit kundrejt parametrit r."""
    r_values, lambdas = lyapunov_scan_logistic(r_min=r_min, r_max=r_max, n_r=n_r)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(r_values, lambdas, linewidth=1.2)
    ax.axhline(0.0, linestyle="--", linewidth=1.0)
    ax.set_title("Eksponenti i Ljapunovit për hartën logjistike")
    ax.set_xlabel("Parametri r")
    ax.set_ylabel(r"$\lambda$")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath
