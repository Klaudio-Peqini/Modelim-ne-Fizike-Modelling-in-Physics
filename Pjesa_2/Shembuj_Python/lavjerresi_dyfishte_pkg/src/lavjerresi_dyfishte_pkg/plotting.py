import matplotlib.pyplot as plt

def plot_time_series(result: dict) -> None:
    t = result["t"]

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    axes[0].plot(t, result["theta1"], label="theta1")
    axes[0].plot(t, result["theta2"], label="theta2")
    axes[0].set_ylabel("Këndi [rad]")
    axes[0].set_title("Këndet")
    axes[0].legend()

    axes[1].plot(t, result["omega1"], label="omega1")
    axes[1].plot(t, result["omega2"], label="omega2")
    axes[1].set_ylabel("Shpejtësia këndore [rad/s]")
    axes[1].set_xlabel("t [s]")
    axes[1].set_title("Shpejtësitë këndore")
    axes[1].legend()

    fig.tight_layout()
    plt.show()
