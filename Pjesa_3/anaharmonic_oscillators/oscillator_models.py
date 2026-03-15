"""
oscillator_models.py

Ky modul përmbledh funksionet anës së djathtë të ekuacioneve diferenciale
për disa modele tipike të oshilatorëve të studiuar në kurs.
"""

from __future__ import annotations

from typing import Callable


def harmonic_oscillator(t: float, y: list[float], omega: float) -> list[float]:
    x, v = y
    dxdt = v
    dvdt = -(omega ** 2) * x
    return [dxdt, dvdt]


def anharmonic_oscillator(t: float, y: list[float], omega: float, alpha: float) -> list[float]:
    x, v = y
    dxdt = v
    dvdt = -(omega ** 2) * x - alpha * (x ** 3)
    return [dxdt, dvdt]


def duffing_oscillator(
    t: float,
    y: list[float],
    delta: float,
    alpha: float,
    beta: float,
    gamma: float,
    forcing_omega: float,
) -> list[float]:
    x, v = y
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * (x ** 3) + gamma * __import__("math").cos(forcing_omega * t)
    return [dxdt, dvdt]


def van_der_pol_oscillator(t: float, y: list[float], mu: float) -> list[float]:
    x, v = y
    dxdt = v
    dvdt = mu * (1 - x ** 2) * v - x
    return [dxdt, dvdt]


def coupled_oscillators(t: float, y: list[float], wx: float, wy: float, eps: float) -> list[float]:
    x, vx, y_pos, vy = y

    dxdt = vx
    dvxdt = -(wx ** 2) * x - eps * y_pos

    dydt = vy
    dvydt = -(wy ** 2) * y_pos - eps * x

    return [dxdt, dvxdt, dydt, dvydt]


def get_model_rhs(args) -> tuple[Callable, tuple]:
    if args.model == "harmonic":
        return harmonic_oscillator, (args.omega,)

    if args.model == "anharmonic":
        return anharmonic_oscillator, (args.omega, args.alpha)

    if args.model == "duffing":
        return duffing_oscillator, (
            args.delta,
            args.alpha,
            args.beta,
            args.gamma,
            args.forcing_omega,
        )

    if args.model == "vdp":
        return van_der_pol_oscillator, (args.mu,)

    if args.model == "coupled":
        return coupled_oscillators, (args.wx, args.wy, args.eps)

    raise ValueError(f"Model i panjohur: {args.model}")


def get_default_initial_conditions(model: str) -> list[float]:
    defaults = {
        "harmonic": [1.0, 0.0],
        "anharmonic": [1.0, 0.0],
        "duffing": [0.5, 0.0],
        "vdp": [2.0, 0.0],
        "coupled": [1.0, 0.0, 0.5, 0.0],
    }
    return defaults[model]


def get_model_labels(model: str) -> dict[str, list[str] | str]:
    labels = {
        "harmonic": {
            "time_series": ["x(t)"],
            "title_time": "Oshilatori harmonik",
            "title_phase": "Hapësira fazore: oshilatori harmonik",
        },
        "anharmonic": {
            "time_series": ["x(t)"],
            "title_time": "Oshilatori anharmonik",
            "title_phase": "Hapësira fazore: oshilatori anharmonik",
        },
        "duffing": {
            "time_series": ["x(t)"],
            "title_time": "Oshilatori Duffing",
            "title_phase": "Hapësira fazore: oshilatori Duffing",
        },
        "vdp": {
            "time_series": ["x(t)"],
            "title_time": "Oshilatori van der Pol",
            "title_phase": "Hapësira fazore: oshilatori van der Pol",
        },
        "coupled": {
            "time_series": ["x(t)", "y(t)"],
            "title_time": "Oshilatorë të lidhur",
            "title_phase": "Portreti i konfiguruar në planin (x,y)",
        },
    }
    return labels[model]
