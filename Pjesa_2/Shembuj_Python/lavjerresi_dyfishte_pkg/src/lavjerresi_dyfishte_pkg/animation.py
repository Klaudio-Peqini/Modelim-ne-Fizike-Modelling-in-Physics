import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_pendulum(result: dict) -> FuncAnimation:
    x1, y1 = result["x1"], result["y1"]
    x2, y2 = result["x2"], result["y2"]
    l1, l2 = result["l1"], result["l2"]

    L = l1 + l2

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-L - 0.2, L + 0.2)
    ax.set_ylim(-L - 0.2, L + 0.2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Animacion: lavjerrësi i dyfishtë")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")

    line, = ax.plot([], [], "o-", lw=2)
    trace, = ax.plot([], [], lw=1)

    def update(frame: int):
        line.set_data([0.0, x1[frame], x2[frame]], [0.0, y1[frame], y2[frame]])
        trace.set_data(x2[:frame+1], y2[:frame+1])
        return line, trace

    ani = FuncAnimation(fig, update, frames=len(x1), interval=20, blit=True)
    plt.show()
    return ani
