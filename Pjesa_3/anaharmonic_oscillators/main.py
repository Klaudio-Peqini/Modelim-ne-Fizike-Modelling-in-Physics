#!/usr/bin/env python3
"""
main.py

Skript kryesor për simulimin e oshilatorëve linearë dhe jo-linearë
në kuadër të kursit "Modellimi në Fizikë".

Përdorimi tipik:
    python main.py --model duffing --tmax 80 --dt 0.01 --phase
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from oscillator_models import get_model_rhs, get_default_initial_conditions, get_model_labels


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simulim numerik i modeleve të ndryshme të oshilatorëve."
    )

    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=["harmonic", "anharmonic", "duffing", "vdp", "coupled"],
        help="Zgjedh modelin fizik që do të simulohet."
    )

    parser.add_argument("--tmin", type=float, default=0.0, help="Koha fillestare e simulimit.")
    parser.add_argument("--tmax", type=float, default=50.0, help="Koha përfundimtare e simulimit.")
    parser.add_argument("--dt", type=float, default=0.01, help="Hapi kohor për rrjetën e vizualizimit.")
    parser.add_argument("--method", type=str, default="RK45", help="Metoda e solve_ivp.")

    # Parametra të përgjithshëm
    parser.add_argument("--x0", type=float, default=None, help="Pozicioni fillestar x(0).")
    parser.add_argument("--v0", type=float, default=None, help="Shpejtësia fillestare v(0).")

    # Parametra për harmonic / anharmonic
    parser.add_argument("--omega", type=float, default=1.0, help="Frekuenca natyrore për modelet 1D.")
    parser.add_argument("--alpha", type=float, default=0.5, help="Parametër jo-linear (anharmonic / Duffing).")

    # Parametra për Duffing
    parser.add_argument("--delta", type=float, default=0.2, help="Koeficienti i disipimit për Duffing.")
    parser.add_argument("--beta", type=float, default=1.0, help="Koeficienti kubik për Duffing.")
    parser.add_argument("--gamma", type=float, default=0.3, help="Amplituda e forcës së jashtme për Duffing.")
    parser.add_argument("--forcing-omega", dest="forcing_omega", type=float, default=1.2,
                        help="Frekuenca e forcës së jashtme për Duffing.")

    # Parametër për van der Pol
    parser.add_argument("--mu", type=float, default=3.0, help="Parametri mu për oshilatorin van der Pol.")

    # Parametra për coupled
    parser.add_argument("--wx", type=float, default=1.0, help="Frekuenca natyrore në drejtimin x.")
    parser.add_argument("--wy", type=float, default=1.2, help="Frekuenca natyrore në drejtimin y.")
    parser.add_argument("--eps", type=float, default=0.3, help="Koeficienti i lidhjes mes dy oshilatorëve.")
    parser.add_argument("--y0", type=float, default=0.5, help="Pozicioni fillestar y(0) për modelin coupled.")
    parser.add_argument("--vy0", type=float, default=0.0, help="Shpejtësia fillestare vy(0) për modelin coupled.")

    # Vizualizimi dhe ruajtja
    parser.add_argument("--phase", action="store_true", help="Vizaton edhe hapësirën fazore.")
    parser.add_argument("--savefig", action="store_true", help="Ruaj figurat në disk.")
    parser.add_argument("--outdir", type=str, default="figures", help="Dosja ku ruhen figurat.")
    parser.add_argument("--dpi", type=int, default=150, help="Rezolucioni i figurave të ruajtura.")

    return parser.parse_args()


def build_initial_conditions(args: argparse.Namespace) -> list[float]:
    defaults = get_default_initial_conditions(args.model)

    if args.model == "coupled":
        return [
            args.x0 if args.x0 is not None else defaults[0],
            args.v0 if args.v0 is not None else defaults[1],
            args.y0,
            args.vy0,
        ]

    return [
        args.x0 if args.x0 is not None else defaults[0],
        args.v0 if args.v0 is not None else defaults[1],
    ]


def run_simulation(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray]:
    rhs, rhs_args = get_model_rhs(args)

    y0 = build_initial_conditions(args)
    t_eval = np.arange(args.tmin, args.tmax + args.dt, args.dt)

    sol = solve_ivp(
        rhs,
        (args.tmin, args.tmax),
        y0,
        t_eval=t_eval,
        args=rhs_args,
        method=args.method,
    )

    if not sol.success:
        raise RuntimeError(f"Integrimi numerik dështoi: {sol.message}")

    return sol.t, sol.y


def ensure_outdir(path_str: str) -> Path:
    path = Path(path_str)
    path.mkdir(parents=True, exist_ok=True)
    return path


def plot_time_series(t: np.ndarray, y: np.ndarray, model: str, savefig: bool, outdir: Path, dpi: int) -> None:
    labels = get_model_labels(model)

    plt.figure(figsize=(9, 5))
    for idx, label in enumerate(labels["time_series"]):
        plt.plot(t, y[idx], label=label)

    plt.xlabel("t")
    plt.ylabel("Amplituda")
    plt.title(labels["title_time"])
    if len(labels["time_series"]) > 1:
        plt.legend()
    plt.tight_layout()

    if savefig:
        plt.savefig(outdir / f"{model}_time_series.png", dpi=dpi)

    plt.show()


def plot_phase_space(y: np.ndarray, model: str, savefig: bool, outdir: Path, dpi: int) -> None:
    labels = get_model_labels(model)

    if model == "coupled":
        plt.figure(figsize=(6.5, 6))
        plt.plot(y[0], y[2])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(labels["title_phase"])
        plt.tight_layout()
        if savefig:
            plt.savefig(outdir / f"{model}_phase.png", dpi=dpi)
        plt.show()
        return

    plt.figure(figsize=(6.5, 6))
    plt.plot(y[0], y[1])
    plt.xlabel("x")
    plt.ylabel("v")
    plt.title(labels["title_phase"])
    plt.tight_layout()

    if savefig:
        plt.savefig(outdir / f"{model}_phase.png", dpi=dpi)

    plt.show()


def main() -> None:
    args = parse_args()
    t, y = run_simulation(args)
    outdir = ensure_outdir(args.outdir) if args.savefig else Path(args.outdir)

    plot_time_series(t, y, args.model, args.savefig, outdir, args.dpi)

    if args.phase:
        plot_phase_space(y, args.model, args.savefig, outdir, args.dpi)


if __name__ == "__main__":
    main()
