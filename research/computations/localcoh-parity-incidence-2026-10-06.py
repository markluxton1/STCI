#!/usr/bin/env python3
"""Export actual one-target quartic incidence for the parity e2 direction.

Unlike the old paritycheck.m2, this contracts the verified full quartic
multiplication tensor, whose columns are actual degree-four forms.
The family is nu=(1+t^2,c*t), pure top coefficient 1, plus lambda*T3.
No full-family exclusion is asserted by this exporter.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "localcoh-symbol-top.json").read_text())
M = sp.Matrix(data["matrix"])
t, c, lam = sp.symbols("t c lam")
top = sp.Matrix([
    sp.expand((1 + t*t)**i * (c*t)**(3-i)).coeff(t, j)
    for i in range(4) for j in range(8)
])
lift, parameters = M.gauss_jordan_solve(top)
lift = lift.subs({parameter: 0 for parameter in parameters})
kernel = M.nullspace()
assert len(kernel) == 1
lift += lam * kernel[0]
assert M * lift == top

lines = (ROOT / "localcoh-incidence-tensor.txt").read_text().splitlines()
assert lines[0] == "30 18 74 542"
tensor = sp.zeros(74, 542)
for line in lines[1:]:
    row, column, value = line.split()
    tensor[int(row), int(column)] = sp.Rational(value)
mult = sp.Matrix.hstack(*[
    sum((tensor[:, 18*i+j] * lift[i] for i in range(30)), sp.zeros(74, 1))
    for j in range(18)
])
assert tensor[:, 540] == sp.eye(74)[:, 72]
assert tensor[:, 541] == sp.eye(74)[:, 73]
f = sp.symbols("f0:18")
for label, target in (("u", tensor[:, 540]), ("v", tensor[:, 541])):
    eqs = [sp.expand(value) for value in mult * sp.Matrix(f) - target]
    output = ROOT / f"localcoh-parity-incidence-{label}-2026-10-06.m2"
    output.write_text(
        "-- Generated actual parity incidence; see the Python exporter.\n"
        "R=QQ[c,lam," + ",".join(str(variable) for variable in f) + "];\n"
        "J=ideal(" + ",".join(str(value).replace("**", "^") for value in eqs if value) + ");\n"
        "print(numgens J);\n"
        "G=gb J;\n"
        "print(\"unit ideal: \"|toString(1_R % G == 0));\n"
        "print gens G;\n"
    )
print("PASS: actual degree-four tensor contracted on the parity lift plus T3")
print("Exported 74 equations per target, in c,lambda and eighteen quartic coefficients")
