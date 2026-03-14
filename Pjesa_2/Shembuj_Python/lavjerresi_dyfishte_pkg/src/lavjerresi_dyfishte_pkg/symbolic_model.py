import sympy as sp

def build_symbolic_lagrangian():
    t = sp.symbols("t", real=True)
    m1, m2, l1, l2, g = sp.symbols("m1 m2 l1 l2 g", positive=True, real=True)

    theta1 = sp.Function("theta1")(t)
    theta2 = sp.Function("theta2")(t)

    x1 = l1 * sp.sin(theta1)
    y1 = -l1 * sp.cos(theta1)

    x2 = x1 + l2 * sp.sin(theta2)
    y2 = y1 - l2 * sp.cos(theta2)

    vx1 = sp.diff(x1, t)
    vy1 = sp.diff(y1, t)
    vx2 = sp.diff(x2, t)
    vy2 = sp.diff(y2, t)

    T = sp.Rational(1, 2) * m1 * (vx1**2 + vy1**2) + sp.Rational(1, 2) * m2 * (vx2**2 + vy2**2)
    V = m1 * g * y1 + m2 * g * y2
    L = sp.simplify(T - V)

    return {
        "t": t,
        "theta1": theta1,
        "theta2": theta2,
        "T": sp.simplify(T),
        "V": sp.simplify(V),
        "L": L,
    }

def pretty_print():
    exprs = build_symbolic_lagrangian()
    print("Energjia kinetike T =")
    sp.pprint(exprs["T"])
    print("\nEnergjia potenciale V =")
    sp.pprint(exprs["V"])
    print("\nLagranzhiani L = T - V =")
    sp.pprint(exprs["L"])

if __name__ == "__main__":
    pretty_print()
