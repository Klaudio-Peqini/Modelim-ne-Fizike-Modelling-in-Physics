import numpy as np
from scipy.integrate import solve_ivp
from .parameters import DoublePendulumParameters

def rhs(t, y, m1, m2, l1, l2, g):
    theta1, omega1, theta2, omega2 = y

    delta = theta1 - theta2

    den1 = l1 * (2*m1 + m2 - m2 * np.cos(2*theta1 - 2*theta2))
    den2 = l2 * (2*m1 + m2 - m2 * np.cos(2*theta1 - 2*theta2))

    dtheta1 = omega1
    dtheta2 = omega2

    domega1 = (
        -g * (2*m1 + m2) * np.sin(theta1)
        - m2 * g * np.sin(theta1 - 2*theta2)
        - 2 * np.sin(delta) * m2 * (omega2**2 * l2 + omega1**2 * l1 * np.cos(delta))
    ) / den1

    domega2 = (
        2 * np.sin(delta) * (
            omega1**2 * l1 * (m1 + m2)
            + g * (m1 + m2) * np.cos(theta1)
            + omega2**2 * l2 * m2 * np.cos(delta)
        )
    ) / den2

    return [dtheta1, domega1, dtheta2, domega2]

def simulate(params: DoublePendulumParameters) -> dict:
    params.validate()

    y0 = [params.theta1, params.omega1, params.theta2, params.omega2]
    t_eval = np.linspace(0.0, params.duration, params.n_points)

    sol = solve_ivp(
        rhs,
        (0.0, params.duration),
        y0,
        t_eval=t_eval,
        args=(params.m1, params.m2, params.l1, params.l2, params.g),
        rtol=1e-8,
        atol=1e-8,
    )

    theta1 = sol.y[0]
    omega1 = sol.y[1]
    theta2 = sol.y[2]
    omega2 = sol.y[3]

    x1 = params.l1 * np.sin(theta1)
    y1 = -params.l1 * np.cos(theta1)

    x2 = x1 + params.l2 * np.sin(theta2)
    y2 = y1 - params.l2 * np.cos(theta2)

    return {
        "t": sol.t,
        "theta1": theta1,
        "omega1": omega1,
        "theta2": theta2,
        "omega2": omega2,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "l1": params.l1,
        "l2": params.l2,
    }
