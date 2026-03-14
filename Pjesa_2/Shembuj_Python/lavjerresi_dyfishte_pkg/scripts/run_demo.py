from lavjerresi_dyfishte_pkg.parameters import DoublePendulumParameters
from lavjerresi_dyfishte_pkg.simulation import simulate
from lavjerresi_dyfishte_pkg.plotting import plot_time_series
from lavjerresi_dyfishte_pkg.animation import animate_pendulum

def main():
    params = DoublePendulumParameters(
        m1=1.0, m2=1.0, l1=1.0, l2=1.0,
        theta1=0.6, theta2=0.2, omega1=0.0, omega2=0.0,
        duration=10.0, n_points=1500
    )
    result = simulate(params)
    plot_time_series(result)
    animate_pendulum(result)

if __name__ == "__main__":
    main()
