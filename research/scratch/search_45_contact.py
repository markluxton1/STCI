#!/usr/bin/env python3
"""Exact exploratory search for (4,5) contact along the monomial quartic.

Fix F=q^2+x*A on the affine chart w=1, so in normal coordinates
u=y-x^3, v=z-xy one has F=v^2-x*u.  Compute the subspace of all
homogeneous quintics through C0 whose restriction to F has order >=r in v.
"""

import sympy as sp

x, y, z, u, v = sp.symbols("x y z u v")


def monomials_affine_homogeneous_degree(d):
    """Dehomogenizations at w=1 of degree-d monomials in w,x,y,z."""
    out = []
    labels = []
    for bx in range(d + 1):
        for by in range(d + 1 - bx):
            for bz in range(d + 1 - bx - by):
                bw = d - bx - by - bz
                out.append(x**bx * y**by * z**bz)
                labels.append((bw, bx, by, bz))
    return out, labels


mons, labels = monomials_affine_homogeneous_degree(5)

# Restriction to C0: y=x^3,z=x^4.  Build the 21 x 56 coefficient matrix.
param = [sp.expand(m.subs({y: x**3, z: x**4})) for m in mons]
M = sp.zeros(21, len(mons))
for j, p in enumerate(param):
    pp = sp.Poly(p, x)
    for e in range(21):
        M[e, j] = pp.coeff_monomial(x**e)

ker = M.nullspace()
assert len(ker) == 35

# Each column below is one quintic-basis element, restricted to F by
# y=x^3+u,z=x*y+v,u=v^2/x.
restrictions = []
for vec in ker:
    g = sp.expand(sum(vec[j] * mons[j] for j in range(len(mons))))
    normal = sp.expand(g.subs({y: x**3 + u, z: x*(x**3 + u) + v}))
    on_f = sp.expand(normal.subs(u, v**2/x))
    restrictions.append(on_f)

# Collect all Laurent-x coefficients of v^1,...,v^r as linear equations.
def condition_matrix(max_v_order):
    rows = []
    row_keys = []
    data = {}
    for j, expr in enumerate(restrictions):
        expr = sp.expand(expr)
        for rv in range(1, max_v_order + 1):
            coeff = sp.expand(expr.coeff(v, rv))
            for term in sp.Add.make_args(coeff):
                pd = term.as_powers_dict()
                ex = int(pd.get(x, 0))
                scalar = sp.simplify(term / x**ex)
                key = (rv, ex)
                data.setdefault(key, {})[j] = data.setdefault(key, {}).get(j, 0) + scalar
    for key in sorted(data):
        rows.append([sp.simplify(data[key].get(j, 0)) for j in range(len(ker))])
        row_keys.append(key)
    return sp.Matrix(rows), row_keys


for r in range(1, 8):
    C, keys = condition_matrix(r)
    ns = C.nullspace()
    print(f"order >= {r+1}: dimension {len(ns)}")

# Extract a class vanishing through v^4 but not v^5, modulo the obvious
# multiples of F if one exists.
C4, _ = condition_matrix(4)
N4 = C4.nullspace()
print("candidate count", len(N4))
for idx, coeffs in enumerate(N4):
    g_coeff = sp.zeros(len(mons), 1)
    for j, c in enumerate(coeffs):
        g_coeff += c * ker[j]
    g = sp.factor(sum(g_coeff[j] * mons[j] for j in range(len(mons))))
    normal = sp.expand(g.subs({y: x**3 + u, z: x*(x**3 + u) + v}))
    on_f = sp.factor(normal.subs(u, v**2/x))
    if on_f != 0:
        print("NONZERO CANDIDATE", idx)
        print("G affine =", g)
        print("G|F =", on_f)
        break
else:
    print("all order>=5 candidates vanish identically on F")


def ideal_basis(degree):
    mns, _ = monomials_affine_homogeneous_degree(degree)
    restrictions_c = [sp.expand(m.subs({y: x**3, z: x**4})) for m in mns]
    mat = sp.zeros(4*degree + 1, len(mns))
    for jj, pp in enumerate(restrictions_c):
        pp = sp.Poly(pp, x)
        for ee in range(4*degree + 1):
            mat[ee, jj] = pp.coeff_monomial(x**ee)
    vectors = mat.nullspace()
    polys = [sp.expand(sum(vec[jj] * mns[jj] for jj in range(len(mns)))) for vec in vectors]
    return polys


quartics = ideal_basis(4)
quintics = ideal_basis(5)
assert len(quartics) == 18 and len(quintics) == 35


def normal_expand(poly):
    return sp.expand(poly.subs({y: x**3 + u, z: x*(x**3 + u) + v}))


quartic_normals = [normal_expand(f) for f in quartics]
quintic_normals = [normal_expand(g) for g in quintics]


def implicit_u_series(f_normal, max_order=7):
    """Solve f(u(v),v)=0 through v^max_order, assuming f_u(0,0)!=0."""
    lin_u = sp.expand(f_normal).coeff(u, 1).coeff(v, 0)
    if lin_u == 0:
        return None
    sol = 0
    cs = []
    for rr in range(1, max_order + 1):
        cr = sp.symbols(f"c{rr}")
        trial = sol + cr*v**rr
        eq = sp.expand(f_normal.subs(u, trial)).coeff(v, rr)
        value = sp.solve(sp.Eq(eq, 0), cr, dict=False)
        if not value:
            return None
        sol = sp.factor(sol + value[0]*v**rr)
        cs.append(value[0])
    return sol


def coefficient_constraint_matrix(exprs, max_v_order):
    data = {}
    for rv in range(1, max_v_order + 1):
        coeffs = [sp.cancel(sp.expand(expr).coeff(v, rv)) for expr in exprs]
        dens = [sp.Poly(sp.fraction(c)[1], x) for c in coeffs]
        common = sp.Poly(1, x)
        for den in dens:
            common = sp.lcm(common, den)
        for jj, coeff in enumerate(coeffs):
            cleared = sp.cancel(coeff * common.as_expr())
            num, den = sp.fraction(cleared)
            assert sp.Poly(den, x).degree() == 0
            poly = sp.Poly(sp.expand(num / den), x)
            for (ee,), scalar in poly.terms():
                data.setdefault((rv, ee), {})[jj] = scalar
    rows = [[data[key].get(jj, 0) for jj in range(len(exprs))] for key in sorted(data)]
    return sp.Matrix(rows)


def contact_profile(f_poly, label):
    print(label, "F =", sp.factor(f_poly))
    fn = normal_expand(f_poly)
    useries = implicit_u_series(fn, 5)
    if useries is None:
        print(label, "skipped: chosen u-direction not smooth")
        return
    gres = [sp.series(gn.subs(u, useries), v, 0, 6).removeO() for gn in quintic_normals]
    dims = []
    spaces = []
    for rr in range(1, 5):
        mat = coefficient_constraint_matrix(gres, rr)
        ns = mat.nullspace()
        dims.append(len(ns))
        spaces.append(ns)
    print(label, "contact dims order>=2..5", dims)
    # Multiples F times a linear form span at most four dimensions.  Any
    # fifth independent class vanishing through v^4 would be a (4,5) pair.
    if dims[3] > 4:
        print(label, "POTENTIAL ORDER-5 NONMULTIPLE", dims[3])


# A reproducible sample of quartic carriers.  These are exploratory only.
sample_vectors = [
    [1 if j == i else 0 for j in range(18)] for i in [0, 1, 2, 9, 17]
]
sample_vectors += [
    [((i + 2)*(j + 3) % 7) - 3 for j in range(18)] for i in range(2)
]

for ii, vec in enumerate(sample_vectors):
    ff = sp.expand(sum(vec[j] * quartics[j] for j in range(18)))
    contact_profile(ff, f"sample-{ii}")
