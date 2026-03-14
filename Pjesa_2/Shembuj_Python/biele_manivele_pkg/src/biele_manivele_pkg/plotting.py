import matplotlib.pyplot as plt

def plot_time_series(result: dict) -> None:
    t = result["t"]
    x = result["x_piston"]
    v = result["v_piston"]
    a = result["a_piston"]

    fig, axes = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

    axes[0].plot(t, x)
    axes[0].set_ylabel("x [m]")
    axes[0].set_title("Pozicioni i pistonit")

    axes[1].plot(t, v)
    axes[1].set_ylabel("v [m/s]")
    axes[1].set_title("Shpejtësia e pistonit")

    axes[2].plot(t, a)
    axes[2].set_ylabel("a [m/s²]")
    axes[2].set_xlabel("t [s]")
    axes[2].set_title("Përshpejtimi i pistonit")

    fig.tight_layout()
    plt.show()
