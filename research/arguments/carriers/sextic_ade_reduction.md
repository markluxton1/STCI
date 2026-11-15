# ADE sextic and quintic pencil reductions

<a id="sextic-pairs-with-an-ade-pencil-carrier"></a>

## Sextic pairs with an ADE pencil carrier

**Independently reviewed reduction.** Fix \(C_0=[s^4:s^3t:st^3:t^4]\) in characteristic zero.
If a proper supported sextic pair has a general normal pencil carrier
with only rational double points, its canonical filtration satisfies
\[
 \boxed{L=\mathcal O_{\mathbf P^1}(-6),\qquad D_2=0.}
\]
Its saturated triple is therefore an embedded primitive triple of type
\(\mathcal O(-6)\). This leaves a restricted case; it does not imply
that every normal pencil carrier is ADE or exclude every sextic pair.

The [all-pair sextic reduction](sextic_pair_reduction.md) owns the normal
pencil, smoothness off the curve and saturated divisor profile. Retain
\(L=\mathcal O(-l)\), \(l\in\{5,6,7\}\), \(D_8=2T\), and
\(\deg T=4l-17\). The full first-symbol divisor of a general member
\(S\) has degree \(l+10\). Its mate cuts \(9C_0\), so local Cartier
indices divide nine. All singularities of \(S\) lie on \(C_0\).

## Marked local models and exact defects

The smooth marked rational-double-point classification in
[Jaffe, Theorem 4.1 and Propositions 5.2–5.3](https://arxiv.org/pdf/alg-geom/9410008)
lists \(A_{r-1}^{c}\), the two marked \(D\) families, \(E_{6,1}\)
and \(E_{7,1}\). The \(D\) and \(E_7\) indices are two or four,
which cannot divide nine. There is no smooth marked \(E_8\) case.
A smooth Cartier curve cannot pass through a singular hypersurface point:
quotienting an embedding-dimension-three surface ring by one equation
leaves embedding dimension at least two.

For \(A_{r-1}^{c}\), the first-symbol order is \(c\), with
\(1\le c\le r/2\), and the actual index is \(r/\gcd(r,c)\).
Use coordinates
\[
 S:(UV+t^r=0),\qquad C_0:(U,V)=(-t^{r-c},t^c).
\]
Since \(9C_0\) is Cartier, \(k=9c/r\) is an integer in
\(\{1,2,3,4\}\). The exact local divisor coefficients are
\[
 D_8=(k-1)c,\qquad T=\frac{(k-1)c}{2},\qquad
 D_2=\max\{0,3c-r\}.                                  \tag{1}
\]

For the socle formula, put \(v=V-t^c\) and let \(D\) be the axis
prime \((V,t)\). Then \(\operatorname{div}(v)=C_0+cD\) and
\(\operatorname{div}(V)=rD\). The rational function \(h=v^9/V^k\)
has divisor \(9C_0\), and is regular by normality. An actual local mate
differs from it by a unit. The reviewed
[local Jacobian/socle identity](normal_index_socle_and_torsion.md) gives
\[
 c+D_8=\operatorname{ord}_t((v^9/h)|_{C_0})
      =\operatorname{ord}_t(V^k|_{C_0})=kc.
\]
For the second defect, put \(u=U+t^{r-c}\). The carrier equation is
\(uv+t^cu-t^{r-c}v=0\), and its saturated first direction is
\(m=u-t^{r-2c}v\). Generically,
\[
 m=-t^{r-3c}v^2+O(v^3).
\]
The [actual-pole identification](sextic_pair_reduction.md#the-constant-direction-triple-and-its-actual-defects)
is local and does not require a constant global direction. It identifies
the second defect with the pole order of this quadratic coefficient,
proving (1).

The remaining non-\(A\) type \(E_{6,1}\) has first-symbol order two
and index three, with model
\[
 x^2-2xt^2-y^3=0,\qquad C_0:(x,y)=0.
\]
Here \(x\) cuts \(3C_0\), giving a primitive triple on the smooth
surface \(x=0\). Its primitive-index defect is zero. The local
power-socle formula gives \(D_8=4,T=2\), and its saturated triple has
\(D_2=0\).

The complete local numerical list is:

| Type | Parameters | First-symbol order | \(T\) | \(D_2\) | Root rank \(\rho\) |
|---|---|---:|---:|---:|---:|
| \(A\), \(k=1\) | \(r=9c\) | \(c\) | 0 | 0 | \(9c-1\) |
| \(A\), \(k=2\) | \(c=2h,r=9h\) | \(2h\) | \(h\) | 0 | \(9h-1\) |
| \(A\), \(k=3\) | \(r=3c\) | \(c\) | \(c\) | 0 | \(3c-1\) |
| \(A\), \(k=4\) | \(c=4h,r=9h\) | \(4h\) | \(6h\) | \(3h\) | \(9h-1\) |
| \(E_{6,1}\) | — | 2 | 2 | 0 | 6 |

All parameters are positive integers. The first row has no defect, hence
is locally primitive. For a general pencil member its singularities in
that locus are simple moving zeros, so \(c=1\). The inequalities below
also hold for every listed \(c\), without this refinement.

## The rank budget and the surviving row

An ADE sextic resolution has \(h^{1,1}=86\). Its negative-definite
exceptional root lattices are independent of the positive-square hyperplane
class, giving total root rank at most 85. This is also Jaffe's Lemma 11.3
specialized to degree six. No such bound is asserted here for arbitrary
normal singularities or in positive characteristic.

Every local row satisfies \(8c-\rho\le8T\). Summing over all
singularities, including moving ones, yields
\[
 \rho_{\rm total}\ge8(l+10)-8(4l-17)=216-24l.          \tag{2}
\]
For \(l=5\), this is 96, exceeding 85 and excluding the row.

For \(l=6\), a positive \(D_2\) requires a \(k=4\) point. The
budget \(\deg T=7\) permits only one, with \(h=1\). It consumes
first-symbol order four and \(T=6\), and contributes rank eight. The
other points have total first-symbol order twelve and \(T=1\), hence
rank at least 88 by the local inequality. Total rank would be at least
96, so \(D_2=0\).

For \(l=7\), the global triple obstruction requires \(D_2>0\).
The budget \(\deg T=11\) permits exactly one positive-second-defect
point, necessarily \(k=4,h=1\). Thus \(D_2=3[P]\). The reviewed
global actual-pole restrictions exclude this: axis directions have no
actual degree-three defect, and mixed directions require three distinct
points. This excludes the last row.

Only \(l=6,D_2=0\) remains. Its saturated triple has local basis
\(1,v,v^2\) with \(v^3=0\), so is primitive even at nonprimitive
points of the length-nine structure.

Independent reconstruction accepted the marked classification coverage,
actual-index restrictions, both defect formulas, the \(E_6\) contribution,
rank budget and all three row dispositions. Existing surface and triple
results were reused within their established scopes. The proof uses exact
formulas and inequalities rather than a finite search. The
\(\mathcal O(-6)\) primitive-triple case and non-ADE carriers remain open.

## Three remaining primitive-triple orbits

The surviving primitive triples have an existing complete classification.
The independently audited
[primitive-direction calculation](../normal-geometry/mf6_and_nonnormal_structures.md#independent-audit-and-all-degree-exclusion-of-primitive-e1-quartic-triples),
subsection “Every basepoint-free primitive triple direction,” uses only
the embedded curve, \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\),
and its quadratic transition class. Its four actual ambient torus orbits
are represented by
\[
 (A,B)=(1+z,-2-8z),\qquad
 (A,B)=(rz,1),\quad (2r+1)(12r^2+4r+3)=0.
\]
Here \(A,B\) describe the conormal quotient in the source's balanced
frame. The triple in each fixed direction is unique, since
\(H^0(\operatorname{Hom}(M,L^2))=H^0(\mathcal O(-4))=0\).
The classification has no quartic-ancestor hypothesis. The source's later
degree-four carrier exclusions do not transfer automatically to sextics.

The \(r=-1/2\) orbit is excluded for sextics directly. In the actual chart
\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]
the containing quadric is \(q=U+zV/2\). For
\((A,B)=(-z/2,1)\), the kernel direction \(BU-AV\) is exactly
\(q\). Its quadratic cocycle has the identically zero factor
\(2A+zB\), so the unique primitive correction is zero. The triple is
precisely the Cartier divisor \(3C_0\) on \(Q\).

A sextic containing it restricts to a section of
\[
 \mathcal O_Q(6,6)(-3C_0)=\mathcal O_Q(3,-3),
\]
which has no nonzero sections. Both sextics would therefore be divisible
by \(q\), contradicting properness. Only the principal orbit and the
two roots of \(12r^2+4r+3=0\) remain.

Independent reuse review checked the classification's complete curve-only
scope, the actual torus action, frame convention, unique triple, and
quadric restriction. These three orbits classify the remaining triples.
Their full degree-six equation spaces and first further contact condition
are computed below; higher extensions and sole support remain unresolved.

## Full sextic spaces and the first further contact equation

The [exact source-space computation](https://github.com/markluxton1/STCI/blob/9deae1cc7f4b008fb287d13bdb2776faa1e75bf5/research/computations/audit_sextic_triple_spaces_2026_10_31.py)
uses all ambient monomials and the accepted triple substitution
\[
 U=Ay-T_0\gamma y^2,\qquad V=By+S_0\gamma y^2,
 \qquad AS_0+BT_0=1.
\]
For the principal orbit,
\((S_0,T_0,\gamma)=(4/3,1/6,96+192z)\); for the algebraic
orbits, \((S_0,T_0,\gamma)=(0,1,0)\).
Vanishing of every coefficient of \(y^0,y^1,y^2\) is exactly
containment of the triple. Its purity makes the dense affine calculation
sufficient for a global section: no nonzero image section can be supported
only at infinity.

| Exact quantity in characteristic zero | Principal orbit | Either algebraic orbit |
| --- | ---: | ---: |
| Dimension of containing quartics | 2 | 2 |
| Dimension of containing quintics | 11 | 11 |
| Dimension of containing sextics | 27 | 27 |
| Span of quartic-source multiples by quadrics | 20 | 20 |
| Additional sextic directions modulo that span | 7 | 7 |
| Rank of the first-normal map \(h\) | 17 | 17 |
| Rank of the cubic-contact map \(\Theta\) | 18 | 12 |
| Rank of the joint map \((h,\Theta)\) | 23 | 24 |

To define the last maps, use the linear coordinates
\(U=T_0m+Ay,\ V=-S_0m+By\). The relevant terms of a containing
sextic are
\[
 F=h_Fm+\gamma h_Fy^2+E_Fmy+K_Fy^3+\cdots,
 \qquad \Theta_F=\gamma E_F-K_F.
\]
The omitted terms do not affect the cubic coefficient after eliminating
\(m\), whose order along the triple is two. With
\(q'=m+\gamma y^2\), the expansion begins
\(F=h_Fq'-\Theta_Fy^3+\cdots\). If \(h_F\ne0\) generically,
eliminating \(q'\) from \(F,G\) leaves cubic coefficient
\[
 \frac{h_G\Theta_F-h_F\Theta_G}{h_F}.
\]
Thus a generically curvilinear supported sextic pair necessarily satisfies
\[
 \boxed{h_G\Theta_F-h_F\Theta_G\equiv0.}
\]
Otherwise its generic transverse length is three, instead of nine.
At least one first-normal coefficient is nonzero in the length-nine
curvilinear setting. The next coefficients through order eight must also
vanish; those conditions and properness have not been solved here.

The script uses exact rational arithmetic and
\(\mathbb Q(\sqrt{-2})\). Conjugation transports the complete algebraic
source and contact matrices to the other root, preserving the ranks.
An independent review reconstructed the substitution, global-source
coverage and contact sign, ran the exact calculation, and added a direct
rank-and-containment check for all twenty quartic-times-quadric products.
Run `PYTHONDONTWRITEBYTECODE=1 python3 research/computations/audit_sextic_triple_spaces_2026_10_31.py`.
This completes the stated linear calculation and first necessary contact
test; it does not exclude the remaining sextic pairs.

## Necessary ADE arithmetic census for a normal quintic with direction degree one

The historical finite enumeration was **necessary-only**, not a geometric existence or exclusion proof. Its inputs are the smooth marked ADE pairs in Jaffe's classification, target quadratic defect `46/5`, total ADE rank at most `44`, and total marked order at most `12` for direction degree one (the auxiliary degree-zero option uses order at most `13`). For `A_n^k` it assigns rank `n`, marked order `k`, defect `k(n+1-k)/(n+1)`, and local index `(n+1)/gcd(n+1,k)`. For marked `D_n` vector/spin and `E_6,E_7` it uses the corresponding Jaffe table. It enumerates multisets with exact total defect `46/5`, pruning by the rank/order budgets and the upper bound `q <= nr*pr/(nr+pr)` on the remaining defect. Every surviving numerical row for direction degree one has **marked order exactly 12 and rank at least 40** (the looser degree-zero enumeration has order at least 12 and rank at least 32). The local-index lcm yields only a necessary mate divisibility `4*index/gcd(index,5)`. These numerical rows are not asserted to be realized by a normal quintic or by a global supported pair.


### Archived certificate: `research/computations/audit_sextic_triple_spaces_2026_10_31.py`

Original finite calculation preserved verbatim with its stated scope and historical relative paths.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Exact degree-four-to-six source spaces for the three O(-6) triples.

Standard-library only. Reuses the moving-chart/second-order substitution of
audit_mf6_e1_primitive_2026_10_07.py. Computes the coefficient-map ranks and,
in degree six, the images of h and Theta=gamma*E-K in the first contact test.
Fixed C0, characteristic zero; the algebraic directions are over Q(sqrt(-2)).
"""
from fractions import Fraction as F

# Q(a), a^2=-2; pairs are (rational part, a-coefficient).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def q(n, d=1):
    return (F(n, d), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] - 2 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    norm = a[0] * a[0] + 2 * a[1] * a[1]
    assert norm
    return (a[0] / norm, -a[1] / norm)


def scale(a, c):
    return {i: mul(v, c) for i, v in a.items() if mul(v, c) != ZERO}


def padd(a, b):
    out = dict(a)
    for i, v in b.items():
        w = add(out.get(i, ZERO), v)
        if w == ZERO:
            out.pop(i, None)
        else:
            out[i] = w
    return out


def pmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            k = i + j
            w = add(out.get(k, ZERO), mul(x, y))
            if w == ZERO:
                out.pop(k, None)
            else:
                out[k] = w
    return out


def yadd(a, b):
    return tuple(padd(x, y) for x, y in zip(a, b))


def ymul(a, b):
    out = ({}, {}, {})
    for i in range(3):
        for j in range(3 - i):
            row = list(out)
            row[i + j] = padd(row[i + j], pmul(a[i], b[j]))
            out = tuple(row)
    return out


def ypow(a, n):
    out = ({0: ONE}, {}, {})
    for _ in range(n):
        out = ymul(out, a)
    return out


def monomials(d):
    return [(i, j, k, d - i - j - k)
            for i in range(d, -1, -1)
            for j in range(d - i, -1, -1)
            for k in range(d - i - j, -1, -1)]


def rank_columns(cols):
    if not cols:
        return 0
    a = [[v for v in row] for row in zip(*cols)]
    nrow, ncol, pivot_row = len(a), len(cols), 0
    for c in range(ncol):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrow:
            break
    return pivot_row


def rref_kernel(matrix, ncols):
    a = [row[:] for row in matrix]
    nrow, pivot_row, pivots = len(a), 0, []
    for c in range(ncols):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivots.append(c)
        pivot_row += 1
        if pivot_row == nrow:
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [ZERO] * ncols
        v[f] = ONE
        for r, c in enumerate(pivots):
            v[c] = neg(a[r][f])
        basis.append(v)
    return len(pivots), basis


def orbit(name):
    z = {1: ONE}
    if name == "principal":
        A, B = {0: ONE, 1: ONE}, {0: q(-2), 1: q(-8)}
        S0, T0 = q(4, 3), q(1, 6)
        gamma = {0: q(96), 1: q(192)}
    else:
        # One root r=(-1+2*sqrt(-2))/6; the other is its conjugate.
        r = (F(-1, 6), F(1, 3))
        assert add(add(mul(q(12), mul(r, r)), mul(q(4), r)), q(3)) == ZERO
        A, B = {1: r}, {0: ONE}
        S0, T0, gamma = ZERO, ONE, {}
    x2 = ({3: ONE}, B, scale(gamma, S0))
    x3 = ({4: ONE}, padd(A, scale(pmul(z, B), q(3, 2))),
          padd(scale(gamma, neg(T0)),
               scale(pmul(z, scale(gamma, S0)), q(3, 2))))
    return A, B, S0, T0, gamma, z, x2, x3


def source_matrix(degree, data):
    _, _, _, _, _, z, x2, x3 = data
    columns = []
    for i, j, k, l in monomials(degree):
        col = ymul(ypow((z, {}, {}), j), ymul(ypow(x2, k), ypow(x3, l)))
        columns.append(col)
    keys = sorted({(n, e) for col in columns for n in range(3) for e in col[n]})
    matrix = [[col[n].get(e, ZERO) for col in columns] for n, e in keys]
    return columns, keys, matrix


def contact_map(degree, data, kernel):
    A, B, S0, T0, gamma, z, _, _ = data
    xm = scale({0: S0}, q(-1))
    xy = B
    x2 = {(0, 0): {3: ONE}, (1, 0): xm, (0, 1): xy}
    xm3 = padd({0: T0}, scale(pmul(z, {0: S0}), q(-3, 2)))
    xy3 = padd(A, scale(pmul(z, B), q(3, 2)))
    x3 = {(0, 0): {4: ONE}, (1, 0): xm3, (0, 1): xy3}

    def bmul(a, b):
        out = {}
        for (m, y), p in a.items():
            for (mm, yy), qpoly in b.items():
                if m + mm + y + yy <= 3:
                    key = (m + mm, y + yy)
                    out[key] = padd(out.get(key, {}), pmul(p, qpoly))
        return out

    def bpow(a, n):
        out = {(0, 0): {0: ONE}}
        for _ in range(n):
            out = bmul(out, a)
        return out

    hcols, ecols, kcols = [], [], []
    for i, j, k, l in monomials(degree):
        value = bmul(bmul(bpow({(0, 0): {0: ONE}}, i), bpow({(0, 0): z}, j)),
                    bmul(bpow(x2, k), bpow(x3, l)))
        hcols.append(value.get((1, 0), {}))
        ecols.append(value.get((1, 1), {}))
        kcols.append(value.get((0, 3), {}))

    h_out, theta_out = [], []
    for v in kernel:
        h = e = k = {}
        for c, col in zip(v, hcols):
            h = padd(h, scale(col, c))
        for c, col in zip(v, ecols):
            e = padd(e, scale(col, c))
        for c, col in zip(v, kcols):
            k = padd(k, scale(col, c))
        theta = padd(pmul(gamma, e), scale(k, q(-1)))
        h_out.append(h)
        theta_out.append(theta)
    h_degrees = sorted({i for p in h_out for i in p})
    t_degrees = sorted({i for p in theta_out for i in p})
    joint_degrees = sorted({("h", i) for p in h_out for i in p}
                           | {("theta", i) for p in theta_out for i in p})

    def vectors(polys, degrees):
        return [[p.get(i, ZERO) for i in degrees] for p in polys]

    h_rank = rank_columns(vectors(h_out, h_degrees))
    theta_rank = rank_columns(vectors(theta_out, t_degrees))
    joint = [[h_out[j].get(i, ZERO) if tag == "h" else theta_out[j].get(i, ZERO)
              for tag, i in joint_degrees] for j in range(len(kernel))]
    return (h_rank, theta_rank, rank_columns(joint),
            (min(h_degrees), max(h_degrees)),
            (min(t_degrees), max(t_degrees)))


def quadric_multiple_span(quartic_kernel, sextic_matrix):
    """Check the actual quartic-times-quadric subspace in sextic columns."""
    quartics, sextics = monomials(4), monomials(6)
    indexes = {mon: i for i, mon in enumerate(sextics)}
    products = []
    for vector in quartic_kernel:
        for quadric in monomials(2):
            product = [ZERO] * len(sextics)
            for coefficient, mon in zip(vector, quartics):
                dest = tuple(x + y for x, y in zip(mon, quadric))
                product[indexes[dest]] = coefficient
            products.append(product)
    for product in products:
        for row in sextic_matrix:
            total = ZERO
            for x, y in zip(row, product):
                total = add(total, mul(x, y))
            assert total == ZERO
    rank = rank_columns(products)
    assert rank == 20
    return rank


def report(name):
    data = orbit(name)
    quartic_kernel = None
    for degree in (4, 5, 6):
        columns, keys, matrix = source_matrix(degree, data)
        rank, kernel = rref_kernel(matrix, len(columns))
        print(f"{name} d={degree}: rows={len(keys)}, rank={rank}, dim={len(kernel)}")
        if degree == 4:
            quartic_kernel = kernel
        if degree == 6:
            product_rank = quadric_multiple_span(quartic_kernel, matrix)
            print(f"  quartic-times-quadric span={product_rank}; "
                  f"additional sextic directions={len(kernel)-product_rank}")
            h_rank, theta_rank, joint_rank, hrange, trange = contact_map(degree, data, kernel)
            print(f"  h: deg={hrange}, rank={h_rank}; Theta: deg={trange}, rank={theta_rank}; "
                  f"joint rank={joint_rank}, joint kernel={len(kernel)-joint_rank}")


if __name__ == "__main__":
    report("principal")
    report("algebraic")
```
</details>
