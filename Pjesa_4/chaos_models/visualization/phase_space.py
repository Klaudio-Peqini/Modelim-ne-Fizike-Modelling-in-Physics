"""Vizualizime të orbitave, hapësirës së fazës dhe atraktorit të Lorencit."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from models.logistic_map import LogisticMap
from models.lorenz_system import LorenzSystem
from models.lyapunov import separation_growth_lorenz


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def plot_logistic_orbit(
    r: float = 3.7,
    x0: float = 0.2,
    n_steps: int = 100,
    savepath: str | Path = OUTPUT_DIR / "orbita_logjistike.png",
) -> Path:
    """Vizaton evolucionin kohor diskret të hartës logjistike."""
    orbit = LogisticMap(r=r, x0=x0).iterate(n_steps)
    n = np.arange(len(orbit))

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(n, orbit, marker="o", markersize=3, linewidth=1)
    ax.set_title(f"Orbita e hartës logjistike (r={r:.3f}, x0={x0:.3f})")
    ax.set_xlabel("Iterimi n")
    ax.set_ylabel(r"$x_n$")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath


def plot_logistic_phase(
    r: float = 3.7,
    x0: float = 0.2,
    n_steps: int = 400,
    discard: int = 50,
    savepath: str | Path = OUTPUT_DIR / "hapesira_fazes_logjistike.png",
) -> Path:
    """Vizaton hartën e vonuar x_n kundrejt x_{n+1}."""
    orbit = LogisticMap(r=r, x0=x0).iterate(n_steps + discard)
    orbit = orbit[discard:]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(orbit[:-1], orbit[1:], s=8, alpha=0.65)
    ax.set_title("Portreti diskret i fazës për hartën logjistike")
    ax.set_xlabel(r"$x_n$")
    ax.set_ylabel(r"$x_{n+1}$")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath


def plot_lorenz_attractor(
    t_max: float = 40.0,
    dt: float = 0.01,
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    savepath: str | Path = OUTPUT_DIR / "atraktori_lorencit.png",
) -> Path:
    """Vizaton atraktorin e Lorencit në hapësirën tridimensionale."""
    _, traj = LorenzSystem(sigma=sigma, rho=rho, beta=beta).solve(t_max=t_max, dt=dt)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(traj[:, 0], traj[:, 1], traj[:, 2], linewidth=0.6)
    ax.set_title("Atraktori i Lorencit")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath


def plot_lorenz_projection(
    t_max: float = 40.0,
    dt: float = 0.01,
    savepath: str | Path = OUTPUT_DIR / "projeksioni_xy_lorencit.png",
) -> Path:
    """Vizaton projeksionin (x, y) të atraktorit të Lorencit."""
    _, traj = LorenzSystem().solve(t_max=t_max, dt=dt)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(traj[:, 0], traj[:, 1], linewidth=0.7)
    ax.set_title("Projeksioni (x, y) i atraktorit të Lorencit")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath


def plot_lorenz_sensitivity(
    delta0: float = 1.0e-8,
    t_max: float = 20.0,
    dt: float = 0.01,
    savepath: str | Path = OUTPUT_DIR / "ndjeshmeria_lorencit.png",
) -> Path:
    """Vizaton rritjen e ndarjes mes dy trajektoreve të afërta."""
    t, dist = separation_growth_lorenz(delta0=delta0, t_max=t_max, dt=dt)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.semilogy(t, dist, linewidth=1.2)
    ax.set_title("Ndjeshmëria ndaj kushteve fillestare në sistemin e Lorencit")
    ax.set_xlabel("Koha")
    ax.set_ylabel("Distanca mes trajektoreve")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    savepath = Path(savepath)
    fig.savefig(savepath, dpi=200)
    plt.close(fig)
    return savepath
