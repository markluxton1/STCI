#!/usr/bin/env python3
"""Exact finite certificates for contact partitions [4], [3,1], [2,2].

This checks the displayed algebra in the companion proof.  It neither
reproves the preceding ribbon-net reduction nor tests arbitrary quartics.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import sympy as s


START = time.perf_counter()
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[2]
OUTPUT = ROOT / "research/scratch/session-ribbon-repeated-partitions-2026-10-09.json"
CHECKS: list[str] = []


def zero(label: str, value) -> None:
    if isinstance(value, s.MatrixBase):
        ok = all(s.cancel(v) == 0 for v in value)
    else:
        ok = s.cancel(value) == 0
    if not ok:
        raise AssertionError(f"{label}: {value}")
    CHECKS.append(label)


def truth(label: str, value: bool) -> None:
    if not value:
        raise AssertionError(label)
    CHECKS.append(label)


U, V, t, k, lam, a, b, h, r = s.symbols("U V t k lam a b h r")
Y = s.symbols("Y0:5")
E = [
    Y[0] * Y[2] - Y[1] ** 2,
    Y[0] * Y[3] - Y[1] * Y[2],
    Y[0] * Y[4] - Y[1] * Y[3],
    Y[1] * Y[3] - Y[2] ** 2,
    Y[1] * Y[4] - Y[2] * Y[3],
    Y[2] * Y[4] - Y[3] ** 2,
]


def matrix(c) -> s.Matrix:
    return s.Matrix([[c[0], c[1], c[2]],
                     [c[1], c[2] + c[3], c[4]],
                     [c[2], c[4], c[5]]])


def quadric(c):
    return s.expand(sum(ci * ei for ci, ei in zip(c, E)))


def derivative(c):
    return c[0] * U**4 - c[1] * U**3 * V - 2 * c[3] * U**2 * V**2 \
        - c[4] * U * V**3 + c[5] * V**4


rnc = {Y[i]: U ** (4-i) * V**i for i in range(5)}
for i, ei in enumerate(E):
    zero(f"literal RNC quadric E{i}", ei.subs(rnc))
c = s.symbols("c0:6")
zero("actual omitted-coordinate derivative", s.diff(quadric(c), Y[2]).subs(rnc) - derivative(c))
reverse = {Y[i]: Y[4-i] for i in range(5)}
for i, j in enumerate([5, 4, 2, 3, 1, 0]):
    zero(f"fixed-center coordinate reversal E{i}", E[i].subs(reverse, simultaneous=True) - E[j])

# [4]: all endpoint and eta-coordinate boundaries.
aa, bb = s.symbols("aa bb")
four = (aa*U + bb*V)**4
zero("fourth-power middle coefficient", s.Poly(four, U, V).coeff_monomial(U**2 * V**2) - 6*aa**2*bb**2)
c4 = [1, 0, k, 0, 0, 0]
zero("[4] determinant retaining E2 coefficient", matrix(c4).det() + k**3)
q4 = [0, lam, -1, 1, 0, 0]
eta4 = s.Matrix([0, 1, lam])
zero("[4] entire eta family", matrix(q4)*eta4)
zero("[4] Q2 at k=0 eta family", matrix(c4).subs(k, 0)*eta4)
zero("[4] offconic discriminant", eta4[1]**2 - eta4[0]*eta4[2] - 1)
zero("[4] singleton support condition", derivative(q4).subs(U, 0))
line4 = {Y[0]: 0, Y[1]: 0, Y[2]: 0}
zero("[4] singular line lies on Q1", quadric(q4).subs(line4))
zero("[4] singular line lies on Q2", E[0].subs(line4))
zero("[4] Q2 gradient vanishes on full line", s.Matrix([s.diff(E[0], yi).subs(line4) for yi in Y]))

# [3,1]: endpoint triple and nonendpoint diagonal orbit.
endpoint31 = [a, -b, k, 0, 0, 0]
zero("[3,1] endpoint determinant", matrix(endpoint31).det() + k**3)
zero("[3,1] endpoint nonzero minor", matrix(endpoint31).subs(k, 0)[:2, :2].det() + b**2)
zero("[3,1] endpoint unique conic kernel", matrix(endpoint31).subs(k, 0)*s.Matrix([0, 0, 1]))
simple_a, simple_b = s.symbols("simple_a simple_b")
mixed31 = (aa*U+bb*V)**3 * (simple_a*U+simple_b*V)
zero("[3,1] middle coefficient including endpoints", s.Poly(mixed31, U, V).coeff_monomial(U**2*V**2) - 3*aa*bb*(aa*simple_b+bb*simple_a))
c31 = [1, 2, k, 0, -2, -1]
zero("[3,1] nonendpoint normalized derivative", derivative(c31) - (U-V)**3*(U+V))
M31 = matrix(c31)
P31 = k*(k**2+9)
zero("[3,1] all E2 determinant roots", M31.det()+P31)
eta31 = s.Matrix([2*(1-k), -(1+k**2), 2*(1+k)])
zero("[3,1] polynomial kernel retaining all roots", M31*eta31 - s.Matrix([0, -P31, 0]))
truth("[3,1] rank two at every determinant root", s.gcd(P31, k**2+1) == 1)
delta31 = s.expand(eta31[1]**2 - eta31[0]*eta31[2])
truth("[3,1] no conic direction hidden at determinant roots", s.gcd(P31, delta31) == 1)
A, B, C = eta31
N31 = s.Matrix([[A, B, C], [0, A-C, B], [-C, -B, A]])
rhs31 = s.Matrix([0, -B, -2*C])
zero("[3,1] normalized singleton system determinant", N31.det()+4*k*(k**2+1)*(k**2+9))
adj_rhs31 = N31.adjugate()*rhs31
zero("[3,1] inconsistency certificate before reduction", adj_rhs31[2]-4*k*(k**2-3)**2)
zero("[3,1] inconsistency certificate at all determinant roots", s.rem(adj_rhs31[2], P31, k)-576*k)
c31a = s.Matrix([b/2+1, b, -1, 1, -b, 1-b/2])
zero("[3,1] complete k=0 solution family", matrix(c31a)*eta31.subs(k, 0))
truth("[3,1] affine solution has exactly one free variable", N31.subs(k, 0).rank() == 2)
c31base = [1, 0, -1, 1, 0, 1]
zero("[3,1] unique pencil modulo Q2", c31a-s.Matrix(c31base)-b/2*s.Matrix(c31).subs(k, 0))
T31 = quadric(c31base)
zero("[3,1] low-rank quadric factorization", T31-((Y[0]-Y[2])*(Y[2]-Y[4])-(Y[1]-Y[3])**2))
line31 = dict(zip(Y, [h, r, h, r, h]))
zero("[3,1] entire singular line lies on Q2", quadric(c31).subs(k, 0).subs(line31))
zero("[3,1] entire singular line lies on Q1", T31.subs(line31))
zero("[3,1] gradient vanishes on entire line", s.Matrix([s.diff(T31, yi).subs(line31) for yi in Y]))

# [2,2]: q^2 has zero middle coefficient only when all q coefficients are nonzero.
ac, bc, cc = s.symbols("ac bc cc")
q_general = ac*U**2 + bc*U*V + cc*V**2
zero("[2,2] missing middle condition", s.Poly(q_general**2, U, V).coeff_monomial(U**2*V**2)-bc**2-2*ac*cc)
q22 = U**2 + U*V - V**2/2
zero("[2,2] diagonal normalization fixes omitted center", q_general.subs({U: bc/ac*U, cc: -bc**2/(2*ac)}) - bc**2/ac*q22)
zero("[2,2] squarefree quadratic discriminant", s.discriminant(q22.subs(U, 1), V)-3)
x = s.symbols("x")
c22 = [1, -2, x, 0, 1, s.Rational(1, 4)]
zero("[2,2] actual L equals normalized square", derivative(c22)-q22**2)
M22 = matrix(c22)
P22 = (2*x+1)*(2*x**2-x+8)
zero("[2,2] determinant all three roots", M22.det()+P22/4)
eta22 = s.Matrix([x/4-1, x+s.Rational(1, 2), -x**2-2])
zero("[2,2] polynomial adjugate kernel", M22*eta22-s.Matrix([M22.det(), 0, 0]))
truth("[2,2] rank two at every determinant root", s.gcd(P22, x-4) == 1)
delta22 = s.expand(eta22[1]**2-eta22[0]*eta22[2])
truth("[2,2] all kernel directions off intrinsic conic", s.gcd(P22, delta22) == 1)
a0, a1, a2, a4, a5 = s.symbols("a0 a1 a2 a4 a5")
vars22 = [a0, a1, a2, a4, a5]
c_first22 = [a0, a1, a2, 1, a4, a5]
rem22 = s.Poly(s.rem(derivative(c_first22).subs({U: 1, V: t}), 1+t-t**2/2, t), t)
zero("[2,2] support remainder coefficient t", rem22.coeff_monomial(t)-(-a1-6*a4+16*a5-4))
zero("[2,2] support remainder constant", rem22.coeff_monomial(1)-(a0-4*a4+12*a5-4))
eq22 = list(matrix(c_first22)*eta22) + [rem22.coeff_monomial(t), rem22.coeff_monomial(1)]
A22, rhs22 = s.linear_eq_to_matrix(eq22, vars22)
aug22 = A22.row_join(rhs22)
P22quad = 2*x**2-x+8
minor22 = aug22[:, [1, 2, 3, 4, 5]].det()
zero("[2,2] determinant vanishes at both quadratic candidates", s.rem(A22.det(), P22quad, x))
zero("[2,2] augmented obstruction at both quadratic candidates", s.rem(minor22, P22quad, x)+243*x/4)
truth("[2,2] obstruction is nonzero at every quadratic root", s.gcd(P22quad, x) == 1)
c22family = s.Matrix([4*a5, 2-8*a5, -2*a5, 1, 4*a5-1, a5])
zero("[2,2] entire remaining affine solution", (matrix(c22family)*eta22).subs(x, -s.Rational(1, 2)))
zero("[2,2] entire remaining support remainder", s.rem(derivative(c22family).subs({U: 1, V: t}), 1+t-t**2/2, t))
truth("[2,2] no omitted extra affine direction", A22.subs(x, -s.Rational(1, 2)).rank() == 4)
c22base = s.Matrix([0, 2, 0, 1, -1, 0])
zero("[2,2] unique remaining pencil", c22family-c22base-4*a5*s.Matrix(c22).subs(x, -s.Rational(1, 2)))
zero("[2,2] eta2 boundary eta1=0 explicitly included", eta22.subs(x, -s.Rational(1, 2))+s.Rational(9, 8)*s.Matrix([1, 0, 2]))

# Independent [2,2] whole-conductor descent check using two points, not a sampled degree.
x0, x1, x2, x3, z = s.symbols("x0 x1 x2 x3 z")
xy = dict(zip(Y, [x0, x1, z, x2, x3]))
Q1 = quadric(c22base).subs(xy)
Q2 = quadric(c22).subs(x, -s.Rational(1, 2)).subs(xy)
L = x0+2*x1-x2+x3/4
R = -x1**2-2*x0*x2-(x0*x3-x1*x2)/2+x1*x3-x2**2/4
ell = 2*x1-x2
q = -2*x0*x2+x1*x3
AA = -ell
R1 = 2*x0*x2+x1*x2-x1*x3
zero("[2,2] Q2 actual projection equation", Q2-L*z-R)
zero("[2,2] Q1 actual projection equation", Q1-(-z**2+AA*z+R1))
zero("[2,2] third independent quadric reduction", E[3].subs(xy)-Q1-(ell*z+q))
truth("[2,2] third quadric independent of the surface pencil", s.Matrix.hstack(c22base, s.Matrix(c22).subs(x, -s.Rational(1, 2)), s.Matrix([0, 0, 0, 1, 0, 0])).rank() == 3)
on_plane = {x0: -2*x1+x2-x3/4}
RG = s.expand(R.subs(on_plane))
zero("[2,2] entire conductor conic", RG+(8*x1**2-36*x1*x2-16*x1*x3+18*x2**2-x3**2)/8)
zero("[2,2] smooth conic determinant", s.det(s.hessian(RG, (x1, x2, x3))/2)-s.Rational(243, 128))
trace = s.expand((2*q+AA*ell).subs(on_plane))
norm = s.expand((q*q+AA*q*ell-R1*ell**2).subs(on_plane))
disc = s.expand((AA**2+4*R1).subs(on_plane))
truth("[2,2] generic quadratic conductor is separable", s.rem(disc, RG, x1) != 0)
at_two_points = {x1: a, x2: 0, x3: 1}
p_two_points = a**2-2*a-s.Rational(1, 8)
zero("[2,2] two conductor points equation", RG.subs(at_two_points)+p_two_points)
zero("[2,2] norm at both points", norm.subs(at_two_points)-a**2)
zero("[2,2] trace at both points", trace.subs(at_two_points)-a*(-4*a+2))
truth("[2,2] two conductor points distinct", s.discriminant(p_two_points, a) == s.Rational(9, 2))
truth("[2,2] norm nonzero at both points", s.gcd(p_two_points, a) == 1)
zero("[2,2] nonconstant trace-square/norm certificate", s.rem((-4*a+2)**2, p_two_points, a)-(16*a+6))

result = {
    "status": "PASS",
    "scope": "Exact identities for complete partitions [4], [3,1], [2,2], conditional on the accepted genus-one ribbon-net and actual-conductor reductions.",
    "source": str(SOURCE),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "sympy_version": s.__version__,
    "checked_identities": len(CHECKS),
    "checks": CHECKS,
    "partitions": {
        "4": "Every endpoint and eta boundary reduces to a surface singular along a line.",
        "3,1": "Endpoint triple forces conic eta; both extra E2 roots are inconsistent; sole remaining pencil is singular along a line.",
        "2,2": "Both extra E2 roots are inconsistent; sole remaining pencil has no descending power of its Cartier double quadric.",
    },
    "two_point_certificate": {"minimal_polynomial": str(p_two_points), "trace_square_over_norm": "16*a+6", "linear_coefficient": 16},
    "elapsed_seconds": time.perf_counter()-START,
    "does_not_claim": "The universal STCI problem, arbitrary higher carrier degree, or a root canonical promotion.",
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": result["status"], "checked_identities": len(CHECKS), "source_sha256": result["source_sha256"], "output": str(OUTPUT), "elapsed_seconds": result["elapsed_seconds"]}, indent=2))
