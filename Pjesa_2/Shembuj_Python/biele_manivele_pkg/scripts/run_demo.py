from biele_manivele_pkg.parameters import CrankRodParameters
from biele_manivele_pkg.simulation import simulate
from biele_manivele_pkg.plotting import plot_time_series
from biele_manivele_pkg.animation import animate_mechanism

def main():
    params = CrankRodParameters(r=0.05, l=0.18, omega=12.0, duration=2.0, n_points=600)
    result = simulate(params)
    plot_time_series(result)
    animate_mechanism(result)

if __name__ == "__main__":
    main()
