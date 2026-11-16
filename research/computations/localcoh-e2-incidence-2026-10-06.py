#!/usr/bin/env python3
"""Export all four normalized primitive-degree-two ancestor incidence charts.

The pure top is h*(p,r)^3 in divided-power coordinates; p,r are binary
quadratics and h is linear. p(0) or r(0) is normalized to 1, as required
by primitivity; h has either nonzero constant term normalized to 1 or is t.
The one lower principal-part parameter is retained. The three exact
top-lifting equations are imposed, without assuming a primitive fourth
neighborhood or excluding a zero of h.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "localcoh-symbol-top.json").read_text())
M = sp.Matrix(data["matrix"])
L = sp.Matrix(data["annihilator"])
columns = list(M.rref()[1])
N = M[:, columns]
rows = list(N.T.rref()[1])
assert len(columns) == len(rows) == 29
inverse = N[rows, :].inv()
kernel = M.nullspace()[0]

lines = (ROOT / "localcoh-incidence-tensor.txt").read_text().splitlines()
tensor = sp.zeros(74, 542)
for line in lines[1:]:
    row, column, value = line.split()
    tensor[int(row), int(column)] = sp.Rational(value)

t = sp.symbols("t")
p0, p1, p2, r0, r1, r2, h1, lam = sp.symbols("p0 p1 p2 r0 r1 r2 h1 lam")
f = sp.symbols("f0:18")
g = sp.symbols("g0:18")
for initial in ("p", "r"):
    for hchart in ("constant", "t"):
        p = (1 if initial == "p" else p0) + p1*t + p2*t*t
        r = (1 if initial == "r" else r0) + r1*t + r2*t*t
        h = 1 + h1*t if hchart == "constant" else t
        parameters = ([p1, p2, r0, r1, r2] if initial == "p"
                      else [p0, p1, p2, r1, r2])
        if hchart == "constant":
            parameters.append(h1)
        parameters.append(lam)
        top = sp.Matrix([
            sp.expand(h*p**i*r**(3-i)).coeff(t, j)
            for i in range(4) for j in range(8)
        ])
        obstruction = L*top
        reduced = inverse * top[rows, :]
        alpha = sp.zeros(30, 1)
        for column, coordinate in zip(columns, reduced):
            alpha[column] = coordinate
        alpha += lam * kernel
        mult = sp.Matrix.hstack(*[
            sum((tensor[:, 18*i+j]*alpha[i] for i in range(30)), sp.zeros(74, 1))
            for j in range(18)
        ])
        for mode in ("u", "both"):
            variables = parameters + list(f) + (list(g) if mode == "both" else [])
            eqs = list(obstruction) + list(mult*sp.Matrix(f) - tensor[:, 540])
            if mode == "both":
                eqs += list(mult*sp.Matrix(g) - tensor[:, 541])
            eqs = [sp.expand(value) for value in eqs if value != 0]
            name = f"localcoh-e2-{initial}-{hchart}-{mode}-2026-10-06.m2"
            (ROOT / name).write_text(
                "-- Exact top-direction chart exported by localcoh-e2-incidence-2026-10-06.py\n"
                "-- If non-unit, primitive e2 requires Res(p,r) nonzero.\n"
                "R=QQ[" + ",".join(str(variable) for variable in variables) + "];\n"
                "J=ideal(\n" + ",\n".join(str(value).replace("**", "^") for value in eqs) + ");\n"
                "print(\"equations \"|toString numgens J);\n"
                "G=gb J;\n"
                "print(\"unit ideal: \"|toString(1_R % G == 0));\n"
                "print(\"basis elements: \"|toString numColumns gens G);\n"
                "if 1_R % G == 0 then print gens G;\n"
            )
        print(f"EXPORTED: e2 chart initial={initial}, h={hchart}; alpha retains T3", flush=True)
