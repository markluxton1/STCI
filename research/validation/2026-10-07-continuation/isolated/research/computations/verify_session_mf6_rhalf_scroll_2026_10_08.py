#!/usr/bin/env python3
"""Exact carrier, normalization, and entire-conductor algebra for MF6 (8,1/2).

The all-mate compression is a proof in the companion note, not a finite
search. This checker independently constructs the rational coefficients.
"""
import hashlib
import json
from pathlib import Path
import sympy as s

x, y, z, w, a, b, U, V = s.symbols("x y z w a b U V")
x0, x1, x2, x3 = s.symbols("x0 x1 x2 x3")
L = 96*w + x - 8*y + 4*z
F = (-1152*w*w*x*x - 24*w*x**3 + 192*w*x*x*y
     - 96*w*x*x*z + 192*w*x*y*z + x**3*y - x**3*z
     - 8*x*x*y*y + 10*x*x*y*z - 2*x*x*z*z
     - 16*x*y*y*z + 8*x*y*z*z - 8*y*y*z*z)/8
pull = {x: U*b*b, y: U*(b*b-a*a)/8, z: V*b*b,
        w: (U*(a*b-a*a)-V*(a*a+3*b*b))/96}
vp, up = U*a*b, V*a*b

def pl(f):
    return s.expand(f.subs(pull, simultaneous=True))

assert pl(F) == 0
G = x*L-8*y*z
assert s.expand(G*G-x**3*(x-8*y)+64*F) == 0
disc = s.factor(s.discriminant(F, w))
assert disc == 9*x**5*(x-8*y)
coeff = s.Poly(F, w).all_coeffs()
assert s.gcd_list(coeff) == 1
assert s.factor(pl(x*L-8*y*z)-pl(x)*vp) == 0
assert s.factor(pl(x)*up-pl(z)*vp) == 0
assert s.factor(pl(L)*vp-8*pl(y)*up-pl(x*x-8*x*y)) == 0
assert s.factor(vp*vp-pl(x*x-8*x*y)) == 0
assert s.factor(up*up - pl(z)*vp - pl(-96*z*w-x*z+8*y*z-3*z*z)) == 0
assert s.factor(vp*up - pl(x)*vp - pl(-96*x*w-x*x+8*x*y-3*x*z)) == 0

# These identities prove B=A+Av+Au: the span is an algebra, contains all
# six independent degree-one generators of the complete scroll ring,
# and is finite over A. The extra generators have monic quadratic equations.
quad = [x*x, x*y, x*L-8*y*z]
mon3 = [x**i*y**j*z**k*w**(3-i-j-k)
        for i in range(4) for j in range(4-i) for k in range(4-i-j)]
rows = [U**i*V**(3-i)*a**j*b**(6-j) for i in range(4) for j in range(7)]
M = s.Matrix([[s.expand(pl(q)).coeff(U, i).coeff(V, 3-i)
               .coeff(a, j).coeff(b, 6-j)
               for q in mon3] for i in range(4) for j in range(7)])
assert M.rank() == 20
cert = []
for q in quad:
    for name, extra in [("v", vp), ("u", up)]:
        target = s.expand(pl(q)*extra)
        vec = s.Matrix([target.coeff(U, i).coeff(V, 3-i)
                        .coeff(a, j).coeff(b, 6-j)
                        for i in range(4) for j in range(7)])
        sol, parameters = M.gauss_jordan_solve(vec)
        assert not parameters
        expression = s.expand(sum(c*m for c, m in zip(sol, mon3)))
        assert s.expand(pl(expression)-target) == 0
        cert.append({"conductor_quadric": str(q), "extra": name,
                     "ambient_cubic": str(expression)})

# Independent closed formulas supplied by root, avoiding a rank-solver
# dependency for the six conductor annihilator identities.
closed = [[x*G, z*G], [y*G, (L*G-x*x*(x-8*y))/8],
          [x*x*(x-8*y), x*z*(x-8*y)]]
for q, pair in zip(quad, closed):
    for extra, ambient in zip([vp, up], pair):
        assert s.expand(pl(q)*extra-pl(ambient)) == 0

# Hilbert--Burch maximal minors, height-two support x=0,yz=0.
hb = s.Matrix([[x, 0], [-z, x], [L, -8*y]])
minor = [s.expand(hb.extract([i, j], [0, 1]).det())
         for i, j in [(0, 1), (0, 2), (1, 2)]]
assert all(s.expand(g-h) == 0 for g, h in
           zip(minor, [x*x, -8*x*y, 8*y*z-x*L]))
# All matrix entries vanish only at the irrelevant origin because L=96w
# when x=y=z=0. Thus the entire projective conductor is locally Gorenstein.
assert s.expand(L.subs({x: 0, y: 0, z: 0})) == 96*w

# Exact entire upstairs ideal: pulled quadrics have common factor U^2 b^2,
# and the residual ideal (b^2,(b^2-a^2)/8,ab) is the unit sheaf on P1.
residual = [s.cancel(pl(q)/(U*U*b*b)) for q in quad]
assert residual == [b*b, -a*a/8+b*b/8, a*b]
assert s.expand(residual[0]-8*residual[1]) == a*a

# Bind the independently displayed carrier to the recorded MF6 fiber.
repo = Path(__file__).resolve().parents[2]
source = repo / "research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08_rational.json"
owner = json.loads(source.read_text())
old = s.sympify(next(t for t in owner["fibers"] if t["name"] == "rhalf_unique")["quartic_basis"][0])
transform = {x0: x-4*y+16*w, x1: s.Rational(3, 2)*y-z/2-8*w,
             x2: (y-z-16*w)/8, x3: w}
assert s.expand(old.subs(transform, simultaneous=True)-F) == 0

# The specific C0 lift uses base a/b=-(2t-1)/(2t+1).
t = s.symbols("t")
curve = {x: 1+4*t-16*t**3-16*t**4,
         y: t-4*t**3, z: t-12*t**3-16*t**4, w: t**4}
rr = -(2*t-1)/(2*t+1)
assert s.factor((x*L-8*y*z).subs(curve)/curve[x]**2-rr) == 0

out = {"status": "PASS", "scope": "MF6 e1,d2=1 principal fiber p8,r1/2, all exact algebra",
       "coordinate_transform": {str(k): str(v) for k, v in transform.items()},
       "carrier": str(s.expand(F)), "w_discriminant": str(disc),
       "factor_identity": "(xL-8yz)^2-x^3(x-8y)=-64F",
       "normalization_parameterization": {str(k): str(v) for k, v in pull.items()},
       "extra_linear_sections": {"v": str(vp), "u": str(up)},
       "conductor_ideal": [str(q) for q in quad],
       "hilbert_burch_matrix": [[str(hb[i, j]) for j in range(2)] for i in range(3)],
       "annihilator_certificates": cert,
       "cubic_restriction_rank": M.rank(),
       "upstairs_conductor": "2{U=0}+2{b=0}",
       "specific_C0_base_parameter": str(rr),
       "owner_json_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
       "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       "sympy_version": s.__version__}
dest = Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"status": out["status"], "output": str(dest),
                  "checker_sha256": out["checker_sha256"],
                  "conductor_ideal": out["conductor_ideal"]}, indent=2))
