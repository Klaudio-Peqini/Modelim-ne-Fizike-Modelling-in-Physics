import sympy as sp

def build_symbolic_expressions():
    t = sp.symbols("t", real=True)
    r, l, omega = sp.symbols("r l omega", positive=True, real=True)

    theta = omega * t
    x = r * sp.cos(theta) + sp.sqrt(l**2 - r**2 * sp.sin(theta)**2)
    v = sp.diff(x, t)
    a = sp.diff(v, t)

    return {
        "t": t,
        "r": r,
        "l": l,
        "omega": omega,
        "theta": sp.simplify(theta),
        "x": sp.simplify(x),
        "v": sp.simplify(v),
        "a": sp.simplify(a),
    }

def pretty_print():
    exprs = build_symbolic_expressions()
    print("theta(t) =")
    sp.pprint(exprs["theta"])
    print("\nx(t) =")
    sp.pprint(exprs["x"])
    print("\nv(t) =")
    sp.pprint(exprs["v"])
    print("\na(t) =")
    sp.pprint(exprs["a"])

if __name__ == "__main__":
    pretty_print()
