import argparse
from .parameters import CrankRodParameters
from .simulation import simulate
from .plotting import plot_time_series
from .animation import animate_mechanism
from .symbolic_model import pretty_print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mjet i thjeshtë CLI për mekanizmin bielë-manivelë."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in ("plot", "animate"):
        sub = subparsers.add_parser(name)
        sub.add_argument("--r", type=float, default=0.05)
        sub.add_argument("--l", type=float, default=0.18)
        sub.add_argument("--omega", type=float, default=12.0)
        sub.add_argument("--duration", type=float, default=2.0)
        sub.add_argument("--n-points", type=int, default=800)

    subparsers.add_parser("symbolic")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "symbolic":
        pretty_print()
        return

    params = CrankRodParameters(
        r=args.r,
        l=args.l,
        omega=args.omega,
        duration=args.duration,
        n_points=args.n_points,
    )
    result = simulate(params)

    if args.command == "plot":
        plot_time_series(result)
    elif args.command == "animate":
        animate_mechanism(result)

if __name__ == "__main__":
    main()
