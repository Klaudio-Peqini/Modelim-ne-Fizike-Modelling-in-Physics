import argparse
from .parameters import DoublePendulumParameters
from .simulation import simulate
from .plotting import plot_time_series
from .animation import animate_pendulum
from .symbolic_model import pretty_print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mjet i thjeshtë CLI për lavjerrësin e dyfishtë."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in ("plot", "animate"):
        sub = subparsers.add_parser(name)
        sub.add_argument("--m1", type=float, default=1.0)
        sub.add_argument("--m2", type=float, default=1.0)
        sub.add_argument("--l1", type=float, default=1.0)
        sub.add_argument("--l2", type=float, default=1.0)
        sub.add_argument("--g", type=float, default=9.81)
        sub.add_argument("--theta1", type=float, default=0.6)
        sub.add_argument("--theta2", type=float, default=0.2)
        sub.add_argument("--omega1", type=float, default=0.0)
        sub.add_argument("--omega2", type=float, default=0.0)
        sub.add_argument("--duration", type=float, default=10.0)
        sub.add_argument("--n-points", type=int, default=1500)

    subparsers.add_parser("symbolic")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "symbolic":
        pretty_print()
        return

    params = DoublePendulumParameters(
        m1=args.m1,
        m2=args.m2,
        l1=args.l1,
        l2=args.l2,
        g=args.g,
        theta1=args.theta1,
        theta2=args.theta2,
        omega1=args.omega1,
        omega2=args.omega2,
        duration=args.duration,
        n_points=args.n_points,
    )
    result = simulate(params)

    if args.command == "plot":
        plot_time_series(result)
    elif args.command == "animate":
        animate_pendulum(result)

if __name__ == "__main__":
    main()
