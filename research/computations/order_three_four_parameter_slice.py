#!/usr/bin/env python3
"""Exact certificate for q=(1,z,Az+B,Cz+D), characteristic zero.

Run with SymPy 1.14.0. Reuses the accepted first ambient operator, the
complete actual sextic symbol source, and the parity-slice checker.
No source footer is executed and no artifacts are generated. The exact
calculation and its scope are stated in the owning synthesis note.
"""
import json

import sympy as s
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.matrices import DomainMatrix

from order_three_sextic_slice import HERE, coefficients, load_prefix, zero, z, B, C

A, D = s.symbols("A D")
P9 = (15849*B**9 + 144531*B**8 + 341525*B**7 - 1138436*B**6
      - 8388388*B**5 - 16074040*B**4 + 8264096*B**3
      + 80572544*B**2 + 119321280*B + 58870912)
Q = 93*B**2 + 431*B + 584
H = 60*B**3 + 333*B**2 + 718*B + 556
X = -(B-2)*(3*B-2)**2*H / (4*(17*B+38)*Q)
CB = (9*B**3 + 32*B**2 + 96*B + 100)/(17*B+38)
DB = -4*A*(5*B+9)/(3*B-2)
MINOR_ROWS = [0, 1, 2, 3, 4, 5, 6, 8, 10]


def rational_zero(expr):
    assert s.cancel(expr) == 0


def branch_value(expr):
    """Even-A expression after C,D elimination, then A^2=X."""
    poly = s.Poly(s.expand(expr.subs(D, DB).subs(C, CB)), A)
    assert all(k[0] % 2 == 0 for k, value in poly.terms())
    return s.cancel(sum(value*X**(k[0]//2) for k, value in poly.terms()))


def main():
    p, t = A*z+B, C*z+D
    forms = [s.expand(z*t-p*p), s.expand(z*p-t), s.expand(p-z*z)]
    a, b, c = forms
    q = s.Matrix([1, z, p, t])
    r = (s.Matrix([0, c*c, -b*c, b*b-a*c])-z**3*q).applyfunc(s.expand)
    assert all(s.degree(value, z) <= 3 for value in r)
    T = s.Matrix([[a, b, c, 0], [0, a, b, c]])
    assert (T*q).applyfunc(s.expand) == s.zeros(2, 1)
    assert (T*r).applyfunc(s.expand) == s.zeros(2, 1)
    plucker = [c*c, -b*c, b*b-a*c, a*c, -a*b, a*a]
    for value, (i, j) in zip(plucker, [(0, 1), (0, 2), (0, 3),
                                     (1, 2), (1, 3), (2, 3)]):
        zero(q[i]*r[j]-q[j]*r[i]-value)
    first = load_prefix("generalization_quadratic_root_curve_universal_incidence.py", "EXAMPLE")
    point = dict(zip(first["VARIABLES"], coefficients(forms, 2)))
    evaluate = lambda entry: s.sympify(first["evaluate"](entry, point))
    residue = s.Matrix([evaluate(entry) for entry in first["D_VECTOR"]])
    operator = s.Matrix([[evaluate(entry) for entry in row] for row in first["A"]])
    duals = [q, z*q, z**2*q, r]
    pairing = s.Matrix([[s.expand(v[iv]).coeff(z, -k-1)
                         for k, iu, iv in first["ROWS"]] for v in duals])
    assert (pairing*operator).applyfunc(s.expand) == s.zeros(4, 12)
    expected = s.Matrix([
        (18*A*B**2+16*A*B+6*A*C-12*A-9*B*D+6*C*D-16*D)/8,
        (16*A**2+10*A*D+6*B**3+10*B**2+2*B*C-20*B-4*C+3*D**2-48)/8,
        (20*A*B+36*A+3*B*D-2*D)/4,
        (60*A**2*B**2-12*A**2*B+12*A**2*C-144*A**2
         +27*A*B**2*D-40*A*B*D+16*A*C*D-48*A*D
         -9*B**4+9*B**3*C-30*B**3-8*B**2*C+2*B*C**2-24*B*C
         -18*B*D**2+72*B+9*C*D**2+24*C-14*D**2)/8,
    ])
    assert (pairing*residue-expected).applyfunc(s.expand) == s.zeros(4, 1)
    f0, f1, f2, f3 = expected

    # Complete denominator coverage on A != 0. The third pairing first
    # excludes 3B-2=0 and solves D; the first then solves C.
    zero(f2.subs(B, s.Rational(2, 3))-s.Rational(37, 3)*A)
    rational_zero(f2.subs(D, DB))
    numerator_c = 9*B**3+32*B**2+96*B+100-(17*B+38)*C
    rational_zero(f0.subs(D, DB)-3*A*numerator_c/(4*(3*B-2)))
    assert numerator_c.subs(B, -s.Rational(38, 17)) == -s.Rational(271284, 4913)
    rational_zero(f1.subs(D, DB).subs(C, CB)-Q*(A*A-X)/(3*B-2)**2)
    # At Q=0 the non-A part cannot vanish, so dividing by Q loses no point.
    assert s.gcd(Q, (B-2)*(3*B-2)**2*H) == 1
    rational_zero(branch_value(f0))
    rational_zero(branch_value(f1))
    rational_zero(branch_value(f3)-3*P9/(8*(17*B+38)**2*Q))
    assert s.gcd(P9, s.diff(P9, B)) == 1
    assert s.gcd(P9, (B-2)*(3*B-2)*(17*B+38)*Q*H) == 1

    # A=0,D!=0 forces B=2/3,C=11/3; the other two equations disagree.
    zero(f2.subs(A, 0)-D*(3*B-2)/4)
    zero(f0.subs({A: 0, B: s.Rational(2, 3)})-D*(6*C-22)/8)
    edge = {A: 0, B: s.Rational(2, 3), C: s.Rational(11, 3)}
    zero(f1.subs(edge)-(27*D*D-584)/72)
    zero(f3.subs(edge)-(21*D*D+244)/24)
    assert s.gcd(27*D*D-584, 21*D*D+244) == 1
    print("PASS: full dual pairings, A!=0 elimination, all denominator boundaries, and A=0,D!=0 exclusion")

    # A binary quartic discriminant nonzero gives four distinct projective
    # branch points and excludes every common fiber of a,b,c.
    U = (A**3*D-A*A*B*C+3*A*B*D-A*C*D
         +B**3-2*B*B*C+B*C*C-D*D)
    V = (27*A**3*D-27*A*A*B*C+81*A*B*D-27*A*C*D
         -81*B*B*C+18*B*C*C-C**3-27*D*D)
    delta = s.expand(b*b-4*a*c)
    zero(s.discriminant(delta, z)+256*U**3*V)
    # No branch root is lost at infinity: delta has degree four at all
    # eighteen points. Independently c has nonzero leading coefficient -1,
    # so there is no common fiber at infinity even before this test.
    zero(delta.coeff(z, 4)-(4*C-3*A*A))
    leading_num, leading_den = s.cancel(4*CB-3*X).as_numer_denom()
    assert s.gcd(P9, leading_num*leading_den) == 1
    for factor in (U, V):
        numerator, denominator = branch_value(factor).as_numer_denom()
        assert s.gcd(P9, numerator*denominator) == 1
    print("PASS: exactly eighteen distinct smooth A!=0 points (nine B values, two nonzero A values each)")

    # Compute the same 9-row actual-source minor over the quadratic algebra
    # QQ(B)[A]/(A^2-X). Division-free Berkowitz avoids assuming this algebra
    # is a field. This is an exact determinant computation, not sampling.
    base = s.QQ.frac_field(B)
    extension = MonogenicFiniteExtension(s.Poly(A*A-X, A, domain=base))
    aa, bb, cc, dd = (extension.convert(e) for e in (A, B, CB, DB))
    fcoeff = [[-bb*bb, dd-2*aa*bb, cc-aa*aa],
              [-dd, bb-cc, aa], [bb, aa, -extension.one]]
    data = json.loads((HERE/"conditional_2_12_symbol_map_2026_10_20.json").read_text())
    M = s.Matrix(data["symbol_matrix_33_by_23"])
    J = s.Matrix(data["annihilator_11_by_33"])
    assert M.shape == (33, 23) and J.shape == (11, 33)
    assert J*M == s.zeros(11, 23)
    matrix = [[sum((extension.convert(J[i, iv*11+k+j])*fcoeff[iv][j]
                    for iv in range(3) for j in range(3)), extension.zero)
               for k in range(9)] for i in MINOR_ROWS]
    minor = DomainMatrix(matrix, (9, 9), extension)
    determinant = -minor.charpoly()[-1]  # determinant = (-1)^9 constant term
    expression = extension.to_sympy(determinant)
    assert not expression.has(A)
    numerator, denominator = s.cancel(expression).as_numer_denom()
    assert s.degree(numerator, B) == 32
    assert s.degree(denominator, B) == 16
    rational_zero(denominator/((17*B+38)**6*Q**5)-1)
    assert s.gcd(P9, numerator) == 1
    assert s.gcd(P9, denominator) == 1
    print("PASS: rows 0,1,2,3,4,5,6,8,10 give a nonzero actual sextic symbol minor at all eighteen points")
    print("The six A=D=0 points and their symbol/cubic exclusions are covered by order_three_sextic_slice.py.")


if __name__ == "__main__":
    main()
