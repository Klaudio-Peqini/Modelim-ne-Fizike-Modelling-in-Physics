import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_mechanism(result: dict) -> FuncAnimation:
    crank_x = result["crank_x"]
    crank_y = result["crank_y"]
    x_piston = result["x_piston"]
    r = result["r"]
    l = result["l"]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_xlim(-(r + 0.02), l + r + 0.05)
    ax.set_ylim(-(r + 0.05), r + 0.05)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Animacion: mekanizmi bielë-manivelë")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")

    crank_line, = ax.plot([], [], "o-", lw=2)
    rod_line, = ax.plot([], [], "o-", lw=2)
    piston_point, = ax.plot([], [], "s", ms=10)

    def update(frame: int):
        xc = crank_x[frame]
        yc = crank_y[frame]
        xp = x_piston[frame]

        crank_line.set_data([0.0, xc], [0.0, yc])
        rod_line.set_data([xc, xp], [yc, 0.0])
        piston_point.set_data([xp], [0.0])
        return crank_line, rod_line, piston_point

    ani = FuncAnimation(fig, update, frames=len(crank_x), interval=20, blit=True)
    plt.show()
    return ani
