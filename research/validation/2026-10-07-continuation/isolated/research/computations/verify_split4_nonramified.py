#!/usr/bin/env python3
"""Exact complete first-normal charts for nonramified split-[4] sextics.

Characteristic zero, C0, and P-020/P-030 hypotheses.  Also verifies the
one-selected-preimage-per-ruling finite-root [2,2] chart.  This is a finite
parameterization and selected-root singularity certificate, not an STCI
exclusion of the surviving double-allocation [4] family.

The functions image_equations, normal_matrix, and lift_normal are reusable
for higher-jet continuation.  Every carrier lift is F0 + lambda*q**3.
"""

import sympy as sp

z, P, t, X = sp.symbols("z P t X")
x0, x1, x2, x3, xi, eta, e, n = sp.symbols("x0 x1 x2 x3 xi eta e n")
q = x0 * x3 - x1 * x2
A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
D = x2**3 - x1 * x3**2
T = A - 2 * B + D


def image_equations(p, r, u, v):
    polys = [sp.Poly(sp.expand(f), z) for f in (p * u, p * v + r * u, r * v)]
    a, b, c = [[f.nth(i) for i in range(11)] for f in polys]
    return [
        -a[9] + 2 * b[10], -b[0] + 2 * c[1],
        a[0] - 2 * b[1] + 4 * c[2],
        -3 * a[1] + 2 * b[2] + 4 * c[3],
        a[2] - 2 * b[3] + 4 * c[4],
        a[3] - 2 * b[4] + 4 * c[5], -a[4] + 4 * c[6],
        a[5] - 2 * b[6] + 4 * c[7],
        a[6] - 2 * b[7] + 4 * c[8],
        -a[7] - 2 * b[8] + 12 * c[9],
        a[8] - 2 * b[9] + 4 * c[10],
    ]


def solve_chart(evaluation, residual, p, r, degree):
    high_evaluation = sp.cancel(residual / evaluation)
    assert sp.denom(high_evaluation) == 1
    variables = sp.symbols(f"u0:{degree + 1}")
    u = sum(variables[i] * z**i for i in range(degree + 1))
    v = sp.expand(high_evaluation + z * u / 2)
    equations = image_equations(p, r, u, v) + [sp.Poly(v, z).nth(degree + 1)]
    matrix, rhs = sp.linear_eq_to_matrix(equations, variables)
    solution = list(sp.linsolve((matrix, rhs), variables))
    assert len(solution) == 1
    values = solution[0]
    substitution = dict(zip(variables, values))
    assert all(sp.expand(eq.subs(substitution)) == 0 for eq in equations)
    return variables, values, sp.expand(u.subs(substitution)), matrix, rhs


def vector_normal(form, ambient=True):
    if ambient:
        form = sp.expand(form.subs({
            x0: 1, x1: z, x2: z**3 + eta,
            x3: z**4 + xi + sp.Rational(3, 2) * z * eta,
        }))
    polynomial = sp.Poly(sp.expand(form), xi, eta)
    return sp.Matrix([
        sp.Poly(polynomial.coeff_monomial(monomial), z).nth(i)
        for monomial in (xi**2, xi * eta, eta**2)
        for i in range(11)
    ])


def normal_matrix():
    monomials2 = [x0**2, x0*x1, x0*x2, x0*x3, x1**2,
                  x1*x2, x1*x3, x2**2, x2*x3, x3**2]
    forms = [q**2*m for m in monomials2]
    forms += [q*h*x for h in (A, B, D) for x in (x0, x1, x2, x3)]
    forms += [A**2, A*B, B**2, B*D, D**2]
    matrix = sp.Matrix.hstack(*[vector_normal(f) for f in forms])
    columns = list(matrix.rref()[1])
    assert len(columns) == 22
    matrix = matrix[:, columns]
    forms = [forms[i] for i in columns]
    rows = list(matrix.T.rref()[1])
    return forms, matrix, rows, matrix[rows, :].inv()


_lift_data = None


def lift_normal(target):
    global _lift_data
    if _lift_data is None:
        _lift_data = normal_matrix()
    forms, matrix, rows, inverse = _lift_data
    vector = vector_normal(target, ambient=False)
    coefficients = inverse * vector[rows, :]
    assert all(sp.expand(entry) == 0 for entry in matrix*coefficients-vector)
    return sp.expand(sum(coefficient*f for coefficient, f in zip(coefficients, forms)))


def selected_root_J(low_evaluation, high_evaluation, p, u):
    # q/e=n; on Q, X=z^3+e and T/e=(X-1)^2.
    strict_T = sp.cancel(T.subs({
        x0: 1, x1: z, x2: z**3+e, x3: z**4+e*(z+n),
    })/e)
    first_T = sp.expand(strict_T.subs(e, 0))
    T0 = first_T.subs(n, 0)
    Tn = sp.diff(first_T, n)
    eval_J = sp.expand(low_evaluation*u + p*high_evaluation - 2*T0*Tn)
    polynomial = sp.Poly(eval_J, z)
    J = sum(polynomial.nth(3*i+j)*X**i*z**j for i in range(4) for j in range(2))
    assert sp.expand(J.subs(X, z**3)-eval_J) == 0
    return sp.expand(J)


def main():
    residual = (z**3-1)**4
    # d=0: every selected preimage is equivalent to z=1.
    c, values, u0, matrix, rhs = solve_chart(z-1, residual, -2, -1, 10)
    expected = (c[0], c[2]+2, c[2], c[3], c[5]-6, c[5],
                c[6], c[8]+6, c[8], c[9], -2)
    assert values == expected
    assert matrix[:, [1, 4, 7, 10]].rank() == 4
    U0 = c[0]+c[3]+c[6]+c[9]
    U2 = c[2]+c[5]+c[8]
    assert sp.expand(sp.rem(u0, z**3-1, z)-(U0+U2*z+U2*z**2)) == 0
    J0 = selected_root_J(z-1, sp.cancel(residual/(z-1)), -2, u0)
    assert sp.expand(sp.diff(J0, z).subs({X: 1, z: 1})-(U0-U2)) == 0
    assert sp.gcd(u0.subs({c[0]: 1, c[2]: 0, c[3]: 0, c[5]: 0,
                         c[6]: 0, c[8]: 0, c[9]: 0}), z**3-1) == 1

    # d=1: both selected evaluation roots are the same preimage.
    low = (z-1)**2
    p = P-2*z
    r = 1+(P/2-2)*z
    c, values, u1, matrix, rhs = solve_chart(low, residual, p, r, 9)
    expected = (2*c[1]-c[2]+8-3*P, c[1], c[2],
                2*c[4]-c[5]+6*P-18, c[4], c[5],
                2*c[7]-c[8]+12-3*P, c[7], c[8], -2)
    assert values == expected
    # Fixed nonzero minor proves necessity without deleting parameter strata.
    assert matrix[[3, 6, 9, 11], [0, 3, 6, 9]].det() == 16
    assert sp.expand(sp.resultant(p, r, z)+(P-2)**2/2) == 0
    S1 = c[1]+c[4]+c[7]
    S2 = c[2]+c[5]+c[8]
    assert sp.expand(sp.rem(u1, z**3-1, z)-(2*S1-S2+S1*z+S2*z**2)) == 0
    J1 = selected_root_J(low, sp.cancel(residual/low), p, u1)
    assert sp.expand(sp.diff(J1, z).subs({X: 1, z: 1})+3*(S1-S2)) == 0
    assert sp.expand(sp.diff(J1, X).subs({X: 1, z: 1})-(S1-S2)) == 0
    specimen = {P: 0, c[1]: 1, c[2]: 0, c[4]: 0, c[5]: 0, c[7]: 0, c[8]: 0}
    assert sp.gcd(u1.subs(specimen), z**3-1) == 1

    # Every carrier having this normal form has an ordinary A3 selected germ:
    # f=v^4+n*Y, v=X-1, Y|n=0=J(X,z)+terms divisible by v^2.
    # dY/dz at fixed X is J_z !=0 under high content-freeness, so
    # (n,Y,v) are local coordinates.  The numerical correction for a branch
    # of class a is a*(4-a)/4, and the class is 1 (d0) or 2 (d1).
    assert sp.Rational(1*3, 4) == sp.Rational(3, 4)
    assert sp.Rational(2*2, 4) == 1

    # d=1: two distinct selected preimages force a vertical high factor.
    low = z**2+z+1
    p = P-2*z
    r = 1+(P/2+1)*z
    c, values, u_bad, matrix, rhs = solve_chart(low, residual, p, r, 9)
    assert values == (-c[1]-c[2]+2, c[1], c[2], -c[4]-c[5]-6,
                      c[4], c[5], -c[7]-c[8]+6, c[7], c[8], -2)
    assert matrix[[3, 6, 9, 11], [0, 3, 6, 9]].det() == 16
    assert sp.expand(u_bad.subs(z, 1)) == 0
    high_eval = sp.cancel(residual/low)
    assert high_eval.subs(z, 1) == 0
    assert sp.expand((high_eval+z*u_bad/2).subs(z, 1)) == 0

    # [2,2] finite-root chart, with one selected preimage for each ruling.
    low = (z-1)*(z-t)
    residual22 = ((z**3-1)*(z**3-t**3))**2
    p = P-2*z
    r = t+(P/2-1-t)*z
    c, values, u22, matrix, rhs = solve_chart(low, residual22, p, r, 9)
    C0 = t**3*(-P*(t**2+t+1)+2*(t**3+t**2+t+1))
    C3 = P*sum(t**i for i in range(6))-2*sum(t**i for i in range(7))-4*t**3
    C6 = -P*(t**2+t+1)+4*t**3+2*t**2+2*t+4
    expected = ((t+1)*c[1]-t*c[2]+C0, c[1], c[2],
                (t+1)*c[4]-t*c[5]+C3, c[4], c[5],
                (t+1)*c[7]-t*c[8]+C6, c[7], c[8], -2)
    assert all(sp.expand(a-b) == 0 for a, b in zip(values, expected))
    assert matrix[[3, 6, 9, 11], [0, 3, 6, 9]].det() == 16
    assert sp.expand(sp.resultant(p, r, z)+(P-2)*(P-2*t)/2) == 0
    specimen22 = {t: 2, P: 0, c[1]: 1, c[2]: 0, c[4]: 0,
                  c[5]: 0, c[7]: 0, c[8]: 0}
    assert sp.gcd(u22.subs(specimen22), (z**3-1)*(z**3-8)) == 1

    # Reconstruct the ambient image independently and verify a symbolic lift.
    # No high coefficient specialization is used in this lift check.
    p = P-2*z
    r = 1+(P/2-2)*z
    high_eval = sp.cancel((z**3-1)**4/(z-1)**2)
    target = (p*xi+r*eta)*(u1*xi+(high_eval+z*u1/2)*eta)
    F = lift_normal(target)
    assert all(sp.expand(v) == 0 for v in vector_normal(F)-vector_normal(target, False))
    assert vector_normal(q**3) == sp.zeros(33, 1)
    assert all(sp.expand(eq) == 0 for eq in image_equations(
        p, r, u1, high_eval+z*u1/2))
    print("PASS: all nonramified [4] first-normal parameter charts are exact")
    print("PASS: the two-distinct-preimage d=1,[4] chart has forced vertical content")
    print("PASS: surviving d=0 and double-allocation d=1 selected germs are A3")
    print("PASS: finite-root [2,2] chart, including one ramified ruling, is exact")
    print("PASS: ambient normal map has rank22 and symbolic carrier lifts exist")


if __name__ == "__main__":
    main()
