
import argparse

from models.population_growth import simulate_population_growth
from models.logistic_growth import simulate_logistic
from models.sir_model import simulate_sir
from models.seir_model import simulate_seir
from models.traffic_flow import simulate_traffic

from visualization.epidemic_curves import plot_sir
from visualization.phase_plots import phase_plot
from visualization.traffic_simulation import plot_traffic

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)

    args = parser.parse_args()

    if args.model == "population":
        t, N = simulate_population_growth()
        phase_plot(t, N, "t", "N", "Exponential Population Growth")

    elif args.model == "logistic":
        t, N = simulate_logistic()
        phase_plot(t, N, "t", "N", "Logistic Population Growth")

    elif args.model == "sir":
        t, y = simulate_sir()
        plot_sir(t, y[0], y[1], y[2])

    elif args.model == "seir":
        t, y = simulate_seir()
        phase_plot(t, y[2], "t", "I", "SEIR Infected Curve")

    elif args.model == "traffic":
        history = simulate_traffic()
        plot_traffic(history)

    else:
        print("Unknown model")

if __name__ == "__main__":
    main()
