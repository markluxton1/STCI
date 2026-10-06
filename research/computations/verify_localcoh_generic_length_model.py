#!/usr/bin/env python3
"""Exact inverse-system model showing why special Gorenstein fibers cannot be assumed.

Run with the research SymPy interpreter:
  /private/tmp/stci-cas-venv/bin/python research/computations/verify_localcoh_generic_length_model.py
"""
import sympy as sp

c = sp.symbols("c")

# Monomials denote xi^-i eta^-j, i,j >= 1. Multiplication truncates as soon
# as either inverse exponent becomes zero.
def mul(element, xi_power=0, eta_power=0):
    return {
        (i - xi_power, j - eta_power): value
        for (i, j), value in element.items()
        if i > xi_power and j > eta_power and value != 0
    }

def sub(left, right):
    keys = set(left) | set(right)
    return {
        key: value
        for key in keys
        if (value := sp.expand(left.get(key, 0) - right.get(key, 0))) != 0
    }

alpha = {(1, 4): c, (2, 1): sp.Integer(1)}
e = {(1, 1): sp.Integer(1)}
assert mul(alpha, xi_power=1) == e
assert mul(alpha, eta_power=3) == {(1, 1): c}
assert not mul(alpha, xi_power=2)
assert not mul(alpha, xi_power=1, eta_power=1)
assert not sub(mul(alpha, eta_power=3), {(1, 1): c})

# In the free D-basis alpha, eta alpha, eta^2 alpha, e, these matrices
# describe the quotient D[xi,eta]/(xi^2,xi eta,eta^3-c xi).
Xi = sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
Eta = sp.Matrix([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, c, 0]])
assert Xi * Eta == sp.zeros(4)
assert Eta * Xi == sp.zeros(4)
assert Xi**2 == sp.zeros(4)
assert Eta**3 == c * Xi
assert Eta**4 == sp.zeros(4)

generic_socle = sp.Matrix.vstack(Xi, Eta).nullspace()
special_socle = sp.Matrix.vstack(Xi, Eta.subs(c, 0)).nullspace()
assert len(generic_socle) == 1
assert len(special_socle) == 2
assert generic_socle[0] == sp.Matrix([0, 0, 0, 1])
assert set(tuple(v) for v in special_socle) == {(0, 0, 1, 0), (0, 0, 0, 1)}

# Generic maximal-ideal successive ranks are 3,2,1,0. The curve component
# J=(xi,eta^3) has quotient with basis 1,eta,eta^2.
assert sp.Matrix.hstack(Xi, Eta).rank() == 3
assert (Eta**2).rank() == 2
assert (Eta**3).rank() == 1
print("PASS: generic cyclic algebra has length four and Hilbert function (1,1,1,1)")
print("PASS: xi alpha=e and eta^3 alpha=c e, with length-three multiplier ideal")
print("PASS: top coefficient may vanish while the generated socle stays nonzero")
print("PASS: special fiber has socle dimension two; relative Gorenstein inference is false")
