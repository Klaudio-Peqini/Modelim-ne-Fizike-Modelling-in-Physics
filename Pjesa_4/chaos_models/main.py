"""Skript kryesor për Pjesa 4: Kaosi dhe sistemet kaotike.

Shembuj përdorimi:
    python main.py --model logistic
    python main.py --model logistic_phase --r 3.9 --x0 0.21
    python main.py --model bifurcation
    python main.py --model lyapunov_scan
    python main.py --model lorenz
    python main.py --model lorenz_xy
    python main.py --model lorenz_sensitivity
"""
from __future__ import annotations

import argparse
from pathlib import Path

from models.lyapunov import lyapunov_logistic
from visualization.bifurcation import plot_bifurcation, plot_lyapunov_scan
from visualization.phase_space import (
    plot_logistic_orbit,
    plot_logistic_phase,
    plot_lorenz_attractor,
    plot_lorenz_projection,
    plot_lorenz_sensitivity,
)


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Production code për studimin pedagogjik të kaosit determinist.",
    )
    parser.add_argument(
        "--model",
        required=True,
        choices=[
            "logistic",
            "logistic_phase",
            "bifurcation",
            "lyapunov",
            "lyapunov_scan",
            "lorenz",
            "lorenz_xy",
            "lorenz_sensitivity",
        ],
        help="Modeli ose analiza që do të ekzekutohet.",
    )
    parser.add_argument("--r", type=float, default=3.7, help="Parametri r për hartën logjistike.")
    parser.add_argument("--x0", type=float, default=0.2, help="Kushti fillestar për hartën logjistike.")
    parser.add_argument("--n_steps", type=int, default=200, help="Numri i iterimeve për orbitat diskrete.")
    parser.add_argument("--discard", type=int, default=1000, help="Numri i iterimeve tranzitore që hidhen poshtë.")
    parser.add_argument("--keep_last", type=int, default=200, help="Numri i pikave finale për bifurkacionin.")
    parser.add_argument("--n_r", type=int, default=1500, help="Numri i vlerave të parametrit r në skanim.")
    parser.add_argument("--r_min", type=float, default=2.5, help="Vlera minimale e r për skanim.")
    parser.add_argument("--r_max", type=float, default=4.0, help="Vlera maksimale e r për skanim.")
    parser.add_argument("--t_max", type=float, default=40.0, help="Koha maksimale për sistemin e Lorencit.")
    parser.add_argument("--dt", type=float, default=0.01, help="Hapi kohor për sistemin e Lorencit.")
    parser.add_argument("--sigma", type=float, default=10.0, help="Parametri sigma i Lorencit.")
    parser.add_argument("--rho", type=float, default=28.0, help="Parametri rho i Lorencit.")
    parser.add_argument("--beta", type=float, default=8.0 / 3.0, help="Parametri beta i Lorencit.")
    parser.add_argument("--delta0", type=float, default=1.0e-8, help="Ndryshimi fillestar për testin e ndjeshmërisë në Lorenc.")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.model == "logistic":
        path = plot_logistic_orbit(r=args.r, x0=args.x0, n_steps=args.n_steps)
        print(f"Figura u ruajt te: {path}")

    elif args.model == "logistic_phase":
        path = plot_logistic_phase(r=args.r, x0=args.x0, n_steps=max(args.n_steps, 300), discard=min(args.discard, 300))
        print(f"Figura u ruajt te: {path}")

    elif args.model == "bifurcation":
        path = plot_bifurcation(
            r_min=args.r_min,
            r_max=args.r_max,
            n_r=args.n_r,
            keep_last=args.keep_last,
            discard=args.discard,
            x0=args.x0,
        )
        print(f"Figura u ruajt te: {path}")

    elif args.model == "lyapunov":
        lam = lyapunov_logistic(r=args.r, x0=args.x0, n_steps=max(args.n_steps, 2000), discard=args.discard)
        print(f"Eksponenti i Ljapunovit për r={args.r:.6f} është λ = {lam:.6f}")
        if lam > 0:
            print("Interpretim: dinamika është kaotike ose shumë afër regjimit kaotik.")
        elif abs(lam) < 1e-3:
            print("Interpretim: sistemi ndodhet afër kufirit të tranzicionit." )
        else:
            print("Interpretim: dinamika është jo-kaotike dhe perturbimet priren të tkurren.")

    elif args.model == "lyapunov_scan":
        path = plot_lyapunov_scan(r_min=args.r_min, r_max=args.r_max, n_r=min(args.n_r, 3000))
        print(f"Figura u ruajt te: {path}")

    elif args.model == "lorenz":
        path = plot_lorenz_attractor(
            t_max=args.t_max,
            dt=args.dt,
            sigma=args.sigma,
            rho=args.rho,
            beta=args.beta,
        )
        print(f"Figura u ruajt te: {path}")

    elif args.model == "lorenz_xy":
        path = plot_lorenz_projection(t_max=args.t_max, dt=args.dt)
        print(f"Figura u ruajt te: {path}")

    elif args.model == "lorenz_sensitivity":
        path = plot_lorenz_sensitivity(delta0=args.delta0, t_max=min(args.t_max, 25.0), dt=args.dt)
        print(f"Figura u ruajt te: {path}")

    else:
        raise ValueError("Model i panjohur.")


if __name__ == "__main__":
    main()
