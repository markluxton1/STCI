# Actual octics, lifted roots, and a small intrinsic comparison

Independently source-reviewed deductions and exact calculations,
consolidated from frozen commit
`a9209551f93a3ad3794645bce0af2f5ddcdafbaa` without a new computation. Sections 1–5 and the octic calculator were reviewed at
`28756229308313912eb5e98ab2b21c08d828f78c`; the added degree-six comparison
and conditional order-three consequence have the separate review scope stated
below. All source images here are images of actual homogeneous equations,
not freely chosen sections of their normal graded pieces.

Work over an algebraically closed field of characteristic zero, with exact
computations over \(\mathbf Q\). Fix
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), its ideal sheaf \(I\),
and its quadric equation \(q=x_0x_3-x_1x_2\). Ideal powers are sheaf powers.
Let \(B=\operatorname{Bl}_C\mathbf P^3\), with exceptional divisor
\(E\simeq\mathbf P^1\times\mathbf P^1\), and let
\(\Sigma=V(f)\subset E\) be a smooth \((2,2)\) root satisfying the first
compatibility condition \(K_1\) of
[R-0007](../results/quadratic_root_obstruction_model.md).

The result is an actual comparison map, beyond the separate source filters
in the [intrinsic equation-source account](global_equation_jets.md).
For a fixed root, first compatibility of octic equations reduces to a linear
map from 17 leading-multiplier coefficients to a quotient of dimension
between six and nine. For two equations passing this first comparison,
joint root generation is the remaining multiplier-space question: the
surviving sections may have a fixed divisor. An exact seed calculation produces
a proper pair with transverse length eight and residual degree 32; it is
not a sole-support pair.

## 1. Restriction to a lifted Cartier divisor gives the comparison

Write \(E_j=V(\mathcal I_E^{j+1})\). The first root condition supplies a
Cartier divisor \(\Sigma_1\subset E_1\) reducing to \(\Sigma\).
In the present smooth-root setting it is unique: the differences of first
lifts lie in \(H^0(\Sigma,\mathcal O_\Sigma(-5,3))=0\), as in the
[accepted first-lift proof](../supplements/QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md).

For a degree-\(d\) equation of normal order at least two, remove its
exceptional factor of order two. The resulting section belongs to
\(\mathscr L_d=\mathcal O_B(dH-2E)\), where \(H\) is the pullback of a
hyperplane. The accepted balanced geometry gives
\[
\mathscr L_d|_E=\mathcal O_E(4d-14,2),\qquad
\mathcal O_E(-E)=\mathcal O_E(-7,1).
\]
Because \(\Sigma_1\) is a Cartier lift, its square-zero ideal over
\(\Sigma\) is \(\mathcal O_\Sigma(-E)\). Therefore
\[
0\to\mathcal O_\Sigma(4d-21,3)
\to\mathscr L_d|_{\Sigma_1}
\to\mathscr L_d|_\Sigma\to0.
\tag{1}
\]
This is the usual conormal restriction for a
[Cartier divisor](https://stacks.math.columbia.edu/tag/0C4S).
Locally, with exceptional parameter \(t\), the lift has equation
\(f+tg\) modulo \(t^2\); the kernel in (1) is the copy of
\(t\mathcal O_\Sigma\) with the indicated line-bundle twist.

Let \(V_d(f)\) be the actual global degree-\(d\) equations whose quadratic
symbol is a multiple of \(f\). The transformed section of such an equation
\(F\) restricts to zero on \(\Sigma\), hence its restriction to
\(\Sigma_1\) determines a unique residue
\[
\rho_f(F)\in H^0(\Sigma,\mathcal O_\Sigma(4d-21,3)).
\tag{2}
\]
Its vanishing is equivalent to the transformed equation vanishing on the
first lifted root. The map is linear and intrinsic to the specified
embedded lift. It incorporates the higher chart transition and equation
units. No division by the leading multiplier is used, so zeros of that
multiplier remain part of the problem.

This construction generalizes without the balanced splitting: for any
Cartier first lift in an exceptional neighborhood, use
\(H^0(\Sigma,\mathscr L|_\Sigma\otimes\mathcal O_\Sigma(-E))\).
The particular twists and dimensions here come from \(C_0\).

## 2. Quotient by every actual equation correction

Use the reviewed source spaces \(V_{d,r}=H^0(I^r(d))\). For octics,
\(\dim V_{8,2}=80\), and the quadratic symbol surjects onto the entire
57-dimensional \(H^0(E,\mathcal O_E(18,2))\). Thus
\[
0\to V_{8,3}\to V_8(f)
\xrightarrow{\sigma}H^0(\mathbf P^1,\mathcal O(16))\to0,
\qquad \dim V_8(f)=23+17=40.
\tag{3}
\]
Here \(\sigma(F)=\alpha\) means \(F_2=\alpha f\). The notation uses a
chosen scalar equation for the root; rescaling it just changes multiplier
coordinates.

The target in (2) is
\[
T_f=H^0(\Sigma,\mathcal O_\Sigma(11,3)),\qquad \dim T_f=28.
\]
The [quadric source recursion](global_equation_jets.md#the-two-degree-rows-use-the-source-filter-at-different-orders)
gives \(V_{8,3}=qV_{6,2}\). Let \(S_{6,2}\) be the 22-dimensional actual
sextic quadratic-symbol image, and let \(\ell\in H^0(E,\mathcal O_E(1,1))\)
be the first normal symbol of \(q\). On this correction space, (2) is
exactly cubic-symbol restriction:
\[
\rho_f(qH)=\operatorname{res}_\Sigma\bigl(\ell\,\sigma_{6,2}(H)\bigr).
\tag{4}
\]
Define
\[
Q_f=T_f/\operatorname{res}_\Sigma(\ell S_{6,2}).
\]
For a multiplier \(\alpha\), choose any actual octic \(F_0\) with
quadratic symbol \(\alpha f\), and set
\[
\kappa_f(\alpha)=[\rho_f(F_0)]\in Q_f.
\tag{5}
\]
Changing \(F_0\) changes its residue by (4), so (5) is independent of
that choice. It vanishes **if and only if** some actual octic with that
symbol vanishes on \(\Sigma_1\). The maps form the commutative diagram
\[
\begin{array}{ccccccccc}
0&\to&V_{8,3}&\to&V_8(f)&\to&H^0(\mathcal O(16))&\to&0\\
&&\downarrow\rho_f&&\downarrow\rho_f&&\downarrow\kappa_f&&\\
0&\to&\rho_f(V_{8,3})&\to&T_f&\to&Q_f&\to&0.
\end{array}
\tag{6}
\]
In particular,
\[
0\to\ker(\rho_f|_{V_{8,3}})\to\ker\rho_f
\to\ker\kappa_f\to0.
\tag{7}
\]
This is the [fixed-symbol lifting lemma](global_lifting_interfaces.md)
with its maps supplied geometrically. Local expressions such as
\(F_3-\alpha G_0\) represent its residue, but are not automatically global
sections of \(\operatorname{Sym}^3(I/I^2)(8)\). Equation (1), rather than
an arbitrary bound on local coefficients, establishes their gluing.

## 3. A quotient of dimension six to nine

The divisor sequence on \(E\) gives
\[
T_f=H^0(E,\mathcal O(11,3))/
fH^0(E,\mathcal O(9,1)),
\qquad 28=48-20,
\tag{8}
\]
since \(H^1(E,\mathcal O(9,1))=0\). Introduce the existing sextic
multiplier space
\[
H_f=\{\beta\in H^0(\mathbf P^1,\mathcal O(8)):
                       \beta f\in S_{6,2}\},\qquad h_f=\dim H_f.
\tag{9}
\]
It is the kernel of the established 11-by-9 multiplier matrix. Smoothness
of \(\Sigma\) makes \(f\) irreducible and coprime to \(\ell\). Divisibility
in the bihomogeneous polynomial ring then gives
\[
(\ell S_{6,2})\cap fH^0(E,\mathcal O(9,1))=\ell fH_f.
\]
Indeed, \(\ell s=f\lambda\) forces \(\lambda=\ell\beta\), where
\(\beta\) has bidegree \((8,0)\), and then \(s=f\beta\).
It follows that
\[
\dim Q_f=6+h_f,\qquad
\dim\ker(\rho_f|_{V_{8,3}})=1+h_f.
\tag{10}
\]
The extra one is the known symbol kernel \(kq^4\).

There is a uniform bound \(h_f\le3\) in this smooth-root setting. The
restriction \(D=f|_{\ell=0}\) is a nonzero section of degree four on
\(\ell\simeq\mathbf P^1\). The necessary
[sextic quadric restriction](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#1-eight-symbol-equations-are-a-norm-factorization)
says that \(\beta D\) must be the pullback of a quartic under the
degree-three ruling map \(\nu:\mathbf P^1\to\mathbf P^1\).
Let \(\Gamma\) be the least effective divisor downstairs with
\(\nu^*\Gamma\ge\operatorname{div}D\). Explicitly,
\[
\Gamma_y=\max_{x\in\nu^{-1}(y)}
\left\lceil\frac{\operatorname{ord}_xD}{e_x(\nu)}\right\rceil.
\]
Since \(3\deg\Gamma\ge4\), its degree is at least two. The map
\(\beta\mapsto P\), where \(\beta D=\nu^*P\), injects \(H_f\) into
\(H^0(\mathcal O(4)(-\Gamma))\), of dimension at most three. This handles
ramification, repeated roots, and infinity. It does not invoke the stronger
conditional claim that a particular canonical norm multiplier is necessary.

Consequently (5) has a 17-dimensional source and target dimension between
six and nine. Moreover
\[
\dim\ker\kappa_f\ge11-h_f\ge8,
\qquad \dim\ker\rho_f\ge40-28=12.
\tag{11}
\]
There are always actual octics of exact normal order two passing this
first comparison, **for a smooth root in \(K_1\)**. The existence of a
pair whose multipliers jointly generate the root is a further question:
the space \(\ker\kappa_f\subset H^0(\mathcal O(16))\) may have a fixed
divisor. Its dimension alone does not settle that question. In a varying
root family, changes of \(h_f\) and of the rank of \(\kappa_f\) must be
retained; these formulas alone do not give a constant-rank quotient bundle.

### Application to the 24 first-compatible order-three roots

The [complete affine four-parameter spectral slice](order_three_roots_and_sextic_lifts.md#5-completion-of-the-four-parameter-slice)
has 24 smooth roots satisfying \(K_1\): 22 have \(h_f=0\), and the other
two have \(h_f=1\). Applying (10) to their supplied unique first Cartier
lifts gives
\[
\dim\ker\kappa_f\ge17-\dim Q_f=17-(6+h_f),
\]
so the multiplier kernel has dimension at least eleven at the 22 roots and
at least ten at the other two. Every nonzero multiplier in these kernels
has an actual octic lift vanishing on \(\Sigma_1\), by (5); its nonzero
quadratic symbol makes that equation have exact normal order two.

These are lower bounds yielding individual actual equations, not computed
octic ranks, common-zero divisors, jointly generating multiplier pairs,
proper intersections or residual cycles. The sextic failures at these roots
therefore coexist with positive first-compatible octic source spaces.
Determining their exact multiplier kernels and fixed divisors is a distinct
constructive test; no subsequent root lift or sole-support pair is supplied.

## 4. Exact seed: global first compatibility and a proper residual pair

Use the accepted seed
\[
f=(z^2+4)u^2+(z^2-8)v^2,\qquad
G_0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.
\]
This is a control for the new comparison, not a renewed STCI candidate:
its second root obstruction is already nonzero by R-0007.

The [retained calculator](../computations/octic_first_root_source.py)
expands all 165 homogeneous octics in the actual balanced chart
\((1,z,z^3+v,z^4+u+3zv/2)\). Complete vanishing of normal orders zero and
one derives the actual 80-dimensional source. It then imposes
\[
F_2=\alpha f,\qquad F_3-\alpha G_0=f(\lambda u+\mu v).
\tag{12}
\]
Here \(\deg\alpha\le16\). The local cubic coefficients of the actual
source have degree at most 16, while \(\alpha G_0\) has degree at most 17.
The diagonal coefficients of \(f\) have degree two, so
\(\deg\lambda,\deg\mu\le15\) suffices. All resulting coefficients are
imposed; the polynomial quotient is not relaxed to a rational function.

| Exact quantity | Result |
| --- | ---: |
| Actual order-two source dimension | 80 |
| Quadratic symbol rank; kernel dimension | 57; 23 |
| Cubic symbol rank on that kernel | 22 |
| Variables; equations; rank in (12) | 129; 129; 117 |
| Actual first-compatible octic space \(\ker\rho_f\) | 12 |
| Leading multiplier space \(\ker\kappa_f\) | 10 |
| Zero-multiplier equation space | 2 |
| Common divisor of the multiplier space on \(\mathbf P^1\) | 0 |

The inherited sextic calculation has \(h_f=1\) at this seed. Thus
\(\dim Q_f=7\), and (12) realizes rank seven for \(\kappa_f\) and rank
28 for \(\rho_f\). The map is not a zero condition hidden by notation.

An independent implementation review expanded a basis of all twelve actual
octics and the two selected pair lifts on **both** affine charts. On
\(x_3=1\), it used
\[
(x_0,x_1,x_2,x_3)=(w^4+3wU+V/2,w^3+2U,w,1)
\]
and checked (12) against the accepted
\(G_\infty=-32wU^3+48U^2V+64wUV^2\), with
\(\alpha_\infty=w^{16}\alpha(1/w)\). This confirmed polynomial
divisibility at infinity for the entire computed kernel.

The calculator exposes exact homogeneous equations for a pair \(F,G\)
whose multiplier sections have no common zero, including infinity. The
pair has homogeneous polynomial gcd one, so it is proper. To certify its
generic transverse contact, cancel its quadratic and cubic common relation.
At \(z=0\) the resulting quartic, up to a nonzero scalar, is
\[
411880551u^4-2342929108u^2v^2+4609913792v^4.
\tag{13}
\]
Modulo \(u^2-2v^2\) it becomes \(1571577780v^4\), so it is coprime to
\(f|_{z=0}=4u^2-8v^2\). Hence the generic initial ideal is the coprime
binary complete intersection of degrees \((2,4)\), of length eight.
Degree exhaustion for this actual proper pair gives
\[
[V(F,G)]=8[C]+R,\qquad \deg R=8\cdot8-8\cdot4=32.
\tag{14}
\]
Here \(R\) is the effective residual curve cycle; no assertion that it is
reduced or irreducible is needed. This is actual residual support downstairs,
not exceptional vertical behavior.

The phenomenon extends to any pair in \(\ker\rho_f\) with jointly
generating nonzero multipliers. Since \(q^4\) has no quadratic or cubic
symbol, replacing \(G\) by \(G+tq^4\) preserves these first conditions.
The equation \(F\) is not divisible by \(q\). Each irreducible factor of
\(F\) divides \(G+tq^4\) for at most one constant \(t\), so properness
holds outside finitely many values. Over \(k(C)\), cancel the common first
root through cubic order. The quartic remainder changes by a nonzero
multiple of \(t\ell^4\) modulo \(f\). Since smooth \(\Sigma\) is integral,
\(f\) is irreducible over \(k(C)\); every nonzero quartic remainder class
is therefore coprime to \(f\). Outside at most one further value, the
initial type is \((2,4)\) and (14) follows. The formal row operation is
only a generic local calculation on the actual homogeneous pair.

## 5. Higher equation membership has a geometric degree budget

This comparison also separates two obstruction towers. Suppose compatible
primitive Cartier root lifts \(\Sigma_j\subset E_j\) have been supplied.
Let \(V_j\subset V_d(f)\) consist of actual equations whose transformed
sections vanish on \(\Sigma_j\). For \(j\ge1\), restriction gives
\[
r_j:V_{j-1}\to
H^0\!\left(\Sigma,\mathcal O_\Sigma(4d-14-7j,2+j)\right),
\qquad \ker r_j=V_j.
\tag{15}
\]
The target line bundle has degree \(8d-24-12j\). Thus:

| Equation degree | First residue target | Second | Third | Later |
| --- | ---: | ---: | ---: | ---: |
| 8 | 28 | 16 | 4 | 0 from \(j=4\) |
| 6 | 12 | \(h^0(\Sigma,\eta^4)\) | 0 | 0 |

Here \(\eta=\mathcal O_\Sigma(-1,1)\); the sextic second target is
\(H^0(\Sigma,\mathcal O_\Sigma(-4,4))\). Its dimension is one on
\(\eta^4=1\) and zero elsewhere. This is the same degree-zero line bundle
that controls the [torsion-four splitting jump](spectral_torsion_and_syzygy_splitting.md#four-torsion-determines-the-splitting).
It is not an identification of residue classes with \(K_2\).

For \(j>(2d-6)/3\), the negative-degree target has no sections. Further
equation-membership conditions then vanish **if the root tower continues**.
This supplies no root lift: the existence of \(\Sigma_j\) has its own
obstructions, including R-0007's nonzero second class at the seed. The
degree budget cannot be used to declare that tower unobstructed.

### The first sextic comparison and the order-three consequence

The same restriction construction has a smaller degree-six form. Keep a
smooth root in \(K_1\), its unique \(\Sigma_1\), and the multiplier space
\(H_f\) of (9). Let \(V_6(f)\) be the actual sextics with quadratic symbol
in \(H_f f\). The complete source gives
\[
0\longrightarrow kq^3\longrightarrow V_6(f)
\longrightarrow H_f\longrightarrow0,
\qquad \dim H_f\le3.
\]
First restriction has target
\(T_f^{(6)}=H^0(\Sigma,\mathcal O_\Sigma(3,3))\), of dimension twelve.
The residue of \(q^3\) is \(\ell^3|_\Sigma\ne0\): the smooth integral
\((2,2)\) curve is not a component of \(V(\ell)\). Consequently there is
a canonical linear map
\[
\kappa_f^{(6)}:H_f\longrightarrow
T_f^{(6)}/k(\ell^3|_\Sigma),\qquad
\dim\bigl(T_f^{(6)}/k\ell^3\bigr)=11.                 \tag{16}
\]
Choose any actual sextic lifting the symbol \(\alpha f\), restrict to
\(\Sigma_1\), and take its residue modulo \(k\ell^3\). Two choices
differ by \(q^3\), so the class is independent of that choice. It vanishes
exactly when an actual sextic with that symbol vanishes on \(\Sigma_1\).
That sextic is unique for each \(\alpha\), since the residue of \(q^3\)
is nonzero. In particular the first-compatible actual sextic space maps
isomorphically onto \(\ker\kappa_f^{(6)}\); a nonzero vector has exact
normal order two. No multiplier is divided out at its zeros.

This is an intrinsic quotient of the complete quadratic-and-cubic source
incidence, not a newly implemented small matrix solver. In a family the
source \(H_f\) can jump, so (16) is a fiberwise statement until suitable
rank strata and base change are established.

If additionally \(\eta\) has exact order three, then
\(H^0(\Sigma,\eta^4)=0\). Every later target in (15) has negative degree.
Thus, for **any supplied compatible primitive root tower**, a sextic that
passes (16) vanishes on every subsequent supplied lift. This removes later
equation-membership tests; it does not construct those root lifts, remove
\(K_2\), or supply a mate. The order-three branch comparison and its
precise numerical scope are recorded in the
[order-three realization account](order_three_roots_and_sextic_lifts.md).

Under all the saturation, movement-two and full generic coprime-CI hypotheses
of [R-0013](../results/saturated_actual_generator_movement.md) and
[R-0014](../results/movement_two_six_rows.md), order three retains
only \((r,s;a,b)=(2,12;6,16)\). With
[R-0006](../results/actual_ci_smooth_root_bridge.md)'s smooth full root and
everywhere joint generation, a sole-support pair requires root lifts through
exceptional order nine. The small sextic map supplies neither those lifts nor
the degree-sixteen mate. These are conditional constraints on the specified
root family, not a reduction of arbitrary STCI to it.

The degree-six quotient, its uniqueness claim, this conditional order-three
membership consequence, and the numerical/order-nine bridge scope were
independently reconstructed in the source review `synthesis_independent_review`
at the frozen checkpoint. That review reused the reviewed source dimensions
and bound on \(H_f\); it did not rerun their calculators or audit every
historical proof. No material finding remained in that stated scope. The
original calculator and its independent review below are unchanged.

## 6. Computational meaning and evidence

For a fixed first-compatible smooth root, (5) replaces a comparison with
many local coefficients by an intrinsic 17-to-at-most-9 linear map after
all actual equation corrections are removed. Solving for a root as well
still gives a nonlinear incidence. The actual computation used a larger
129-variable matrix to reconstruct the source and certify the seed; it
was not an implementation or benchmark of a generic compressed solver.

The seed shows that global first compatibility and joint root generation
can hold for proper actual pairs with substantial residual support. For
the \((8,8)\) sole-support question, the required transverse length would
be 16, twice the length in (14). Increasing contact and passing the root
tower remain substantive requirements. A large first-compatible equation
space is not evidence that those requirements can be met.

- `intrinsic_source_root_comparison` reconstructed the residue map, correction
  quotient, multiplier intersection, and bounds. The separate
  `octic_comparison_math_review` independently checked the exact sequences,
  all twists, the global divisor argument for \(h_f\le3\), the conditional
  tower (15), and the proper residual-pair perturbation. Smoothness and
  membership in \(K_1\) remain explicit; family ranks are not assumed fixed.
- `octic_first_lift_code_review` independently checked completeness of the
  homogeneous source and linear system, the safe quotient-degree bound,
  all twelve basis equations on both charts, multiplier basepoint freeness,
  the proper pair, and the quartic contact certificate. Accepted root-chart
  formulas were inherited premises. It separately reviewed the retained
  pair-certificate addition and confirmed that all earlier API outputs were
  unchanged, preserving the two-chart verification. No material finding
  remains open in the stated scope.
- Final reviewed calculator SHA-256:
  `ab3351b28f6ed49dcb359d811c7f48ff6eb59d8e472ba8522aa9ae7b9982857b`.
  The retained script ran successfully with Python and SymPy 1.14.0:

      python3 research/computations/octic_first_root_source.py

  Its compact JSON reports the source and kernel dimensions, homogeneous
  multiplier gcd, proper-pair gcd, and primitive quartic certificate.
  The `compute()` API returns all twelve actual homogeneous basis octics,
  their multipliers, and the explicit pair; no rounded coefficients or
  finite-field extrapolation are used. The independent second-chart
  expansion was a separate review check, not an execution mode of this
  calculator.
- No new global root-locus elimination or sole-support search was run. No
  metadata or priorities changed. The computation is a fixed
  laboratory for the general comparison, not an asymptotic complexity family.


### Archived exact certificate: `research/computations/octic_first_root_source.py`

The following original computational certificate is preserved verbatim, with its original hypotheses, limitations, and external dependencies. No additional mathematical conclusion is asserted by its archival transfer.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Exact first-root compatibility slice inside actual octic sources.

Diagnostic at the accepted smooth seed in the movement-two root model.
Expands every homogeneous octic in the balanced x0=1 chart, imposes
vanishing through normal order one, then imposes the seed first-lift
equation through normal order three. Rational linear algebra only.
This is a one-chart necessary filter; no global root-lifting equivalence
or STCI conclusion is asserted by this script.
"""
from fractions import Fraction as F
import json
import sympy as sp

# Sparse normal polynomial (u exponent, v exponent, z exponent) -> Q.
Poly = dict[tuple[int, int, int], F]


def clean(p):
    return {m: c for m, c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({m: c * v for m, v in p.items()})


def mul(p, q, max_normal=3):
    out = {}
    for (i, j, k), a in p.items():
        for (r, s, t), b in q.items():
            if i + j + r + s <= max_normal:
                key = (i + r, j + s, k + t)
                out[key] = out.get(key, F(0)) + a * b
    return clean(out)


def power(p, e, max_normal=3):
    out = {(0, 0, 0): F(1)}
    for _ in range(e):
        out = mul(out, p, max_normal=max_normal)
    return out


def monomials(total):
    """Exponent tuples (x0,x1,x2,x3) of total homogeneous degree."""
    return [(total-b-c-d, b, c, d)
            for b in range(total + 1)
            for c in range(total - b + 1)
            for d in range(total - b - c + 1)]


def expand_octic(mono, max_normal=3):
    _, b, c, d = mono
    z = {(0, 0, 1): F(1)}
    u = {(1, 0, 0): F(1)}
    v = {(0, 1, 0): F(1)}
    x1 = z
    x2 = add(power(z, 3, max_normal), v)
    x3 = add(power(z, 4, max_normal), u,
             scale(mul(z, v, max_normal), F(3, 2)))
    return mul(mul(power(x1, b, max_normal),
                   power(x2, c, max_normal), max_normal=max_normal),
               power(x3, d, max_normal), max_normal=max_normal)


def normal_keys(poly, order):
    return sorted({(i, j, k) for i, j, k in poly if i + j == order})


def matrix_for(keys, columns):
    return sp.Matrix([[col.get(key, F(0)) for col in columns]
                      for key in keys])


def as_poly(coeffs, start=0):
    return sp.Poly.from_dict({(i + start,): c for i, c in enumerate(coeffs)
                              if c}, sp.Symbol("z"), domain=sp.QQ)


def gcd_with_infinity(polys, degree):
    """Homogeneous gcd degree on P1, including the point at infinity."""
    z = sp.Symbol("z")
    gcd = None
    infinity_order = degree
    for coefficients in polys:
        p = as_poly(coefficients)
        gcd = p if gcd is None else sp.gcd(gcd, p)
        deg = p.degree() if not p.is_zero else -1
        infinity_order = min(infinity_order, degree - deg)
    if gcd is None:
        return {"all_zero": True, "finite_gcd": "0", "infinity_order": degree}
    return {"all_zero": gcd.is_zero,
            "finite_gcd": str(gcd.as_expr()),
            "finite_gcd_degree": max(0, gcd.degree()) if not gcd.is_zero else None,
            "infinity_order": infinity_order,
            "homogeneous_common_divisor_degree":
                (max(0, gcd.degree()) if not gcd.is_zero else 0) + infinity_order}


def basepoint_free_pair(alpha_basis, degree):
    """Find two multipliers with no common zero on P1, if present."""
    candidates = list(alpha_basis)
    for i in range(min(12, len(alpha_basis))):
        for j in range(i + 1, min(12, len(alpha_basis))):
            candidates.append([a + b for a, b in zip(alpha_basis[i], alpha_basis[j])])
    for i, first in enumerate(candidates):
        for second in candidates[i + 1:]:
            common = gcd_with_infinity([first, second], degree)
            if common["homogeneous_common_divisor_degree"] == 0:
                return [str(as_poly(first).as_expr()), str(as_poly(second).as_expr())]
    return None


def normal_component(poly, order):
    u, v = sp.symbols("u v")
    return sp.expand(sum(sp.Rational(c.numerator, c.denominator) * u**i * v**j
                         for (i, j, k), c in poly.items()
                         if i + j == order and k == 0))


def chart_expansion_from_homogeneous(coefficients, expansions):
    result = {}
    for coefficient, expansion in zip(coefficients, expansions):
        if coefficient:
            result = add(result, scale(expansion, F(coefficient)))
    return result


def pair_certificate(pair_coefficients, source_monomials):
    """Recompute ambient gcd and the seed's quartic relation at z=0."""
    x0, x1, x2, x3, u, v = sp.symbols("x0 x1 x2 x3 u v")
    homogeneous = []
    for coefficients in pair_coefficients:
        form = sum(sp.Rational(coefficient.numerator, coefficient.denominator) *
                   x0**a * x1**b * x2**c * x3**d
                   for (a, b, c, d), coefficient
                   in zip(source_monomials, coefficients))
        homogeneous.append(sp.Poly(form, x0, x1, x2, x3, domain=sp.QQ))
    ambient_gcd = sp.gcd(*homogeneous)

    # At z=0, f0=4u^2-8v^2 and G0=-3/4*u*v^2. Divide the residual
    # cubic exactly to recover the correction linear forms l_F,l_G.
    chart_four = [expand_octic(m, max_normal=4) for m in source_monomials]
    charts = [chart_expansion_from_homogeneous(coeffs, chart_four)
              for coeffs in pair_coefficients]
    f0 = 4*u**2 - 8*v**2
    g00 = -sp.Rational(3, 4) * u * v**2
    alpha, beta = [normal_component(p, 2).coeff(u, 2) / 4 for p in charts]
    # Directly derive both multipliers from the u^2 coefficient of F2,G2;
    # checking the full binary quadratics below guards the proportionality.
    quadratic_matches = [sp.expand(normal_component(p, 2) - a*f0) == 0
                         for p, a in zip(charts, (alpha, beta))]
    f3, g3 = [normal_component(p, 3) for p in charts]
    f4, g4 = [normal_component(p, 4) for p in charts]
    quotients, remainders = [], []
    for cubic, a in zip((f3, g3), (alpha, beta)):
        quotient, remainder = sp.div(sp.Poly(cubic - a*g00, u, v),
                                      sp.Poly(f0, u, v))
        quotients.append(quotient.as_expr())
        remainders.append(remainder.as_expr())
    lf, lg = quotients
    r4 = sp.expand(alpha**2*g4 - alpha*beta*f4
                   - (alpha*lg - beta*lf)*f3)
    r4_poly = sp.Poly(r4, u, v, domain=sp.QQ)
    content, primitive = r4_poly.primitive()
    f0_poly = sp.Poly(f0, u, v, domain=sp.QQ)
    primitive_gcd = sp.gcd(f0_poly, primitive)
    return {
        "ambient_gcd_degree": ambient_gcd.total_degree(),
        "proper_complete_intersection": ambient_gcd.total_degree() == 0,
        "quadratic_matches_seed_root": all(quadratic_matches),
        "first_cubic_division_exact": all(r == 0 for r in remainders),
        "alpha_z0": str(alpha),
        "beta_z0": str(beta),
        "lF_z0": str(lf),
        "lG_z0": str(lg),
        "quartic_primitive_content": str(content),
        "quartic_primitive_terms": {
            "u^%d*v^%d" % exponent: str(coefficient)
            for exponent, coefficient in primitive.terms()},
        "quartic_coprime_with_seed_f0": primitive_gcd.total_degree() == 0,
        "quartic_common_factor_degree": primitive_gcd.total_degree(),
    }


def compute():
    source_monomials = monomials(8)
    expanded = [expand_octic(m) for m in source_monomials]

    # Vanishing to order >= 2: every constant and linear normal coefficient
    # in the affine chart must vanish identically as a polynomial in z.
    base_keys = sorted({key for p in expanded for key in p
                        if key[0] + key[1] <= 1})
    base_matrix = matrix_for(base_keys, expanded)
    source_kernel = base_matrix.nullspace()
    source = []
    for vector in source_kernel:
        p = {}
        for coefficient, expansion in zip(vector, expanded):
            if coefficient:
                p = add(p, scale(expansion, F(coefficient)))
        source.append(p)

    quad_rows = sorted({(i, j, k) for p in source for i, j, k in p
                        if i + j == 2})
    quad_matrix = matrix_for(quad_rows, source)
    cubic_rows = sorted({(i, j, k) for p in source for i, j, k in p
                         if i + j == 3})
    cubic_matrix = matrix_for(cubic_rows, source)
    # The kernel of the quadratic projection is the actual order-three
    # octic source. Its cubic-symbol rank is an intrinsic source dimension.
    order_three_source = []
    for vector in quad_matrix.nullspace():
        p = {}
        for coefficient, expansion in zip(vector, source):
            if coefficient:
                p = add(p, scale(expansion, F(coefficient)))
        order_three_source.append(p)
    order_three_cubic_rows = sorted({key for p in order_three_source for key in p
                                    if key[0] + key[1] == 3})
    order_three_cubic_matrix = matrix_for(order_three_cubic_rows, order_three_source)

    # Seed root f and its accepted first cubic correction G0.
    z = sp.Symbol("z")
    f = [sp.Poly(z**2 + 4, z, domain=sp.QQ),
         sp.Poly(0, z, domain=sp.QQ),
         sp.Poly(z**2 - 8, z, domain=sp.QQ)]
    G0 = [sp.Poly(0, z, domain=sp.QQ),
          sp.Poly(z/8, z, domain=sp.QQ),
          sp.Poly(-sp.Rational(3, 4), z, domain=sp.QQ),
          sp.Poly(z/8, z, domain=sp.QQ)]

    # Coefficient rows for all source cubics and alpha*G0.
    max_cubic_degree = max(k for _, _, k in cubic_rows)
    alpha_degree = 16
    l_degree = m_degree = max(max_cubic_degree, alpha_degree + 1) - 2
    # Variables: source-section coefficients, alpha_0..alpha_16,
    # l_0..l_L, m_0..m_L.
    nsource, nalpha = len(source), alpha_degree + 1
    nl, nm = l_degree + 1, m_degree + 1
    total_vars = nsource + nalpha + nl + nm
    row_dict = {}
    # Source cubic terms.
    for col, p in enumerate(source):
        for key in normal_keys(p, 3):
            row_dict.setdefault(key, {})[col] = p[key]
    # - alpha * G0.
    for ai in range(nalpha):
        for (u_exp, v_exp), gp in zip([(3, 0), (2, 1), (1, 2), (0, 3)], G0):
            for (k,), coeff in gp.terms():
                row_dict.setdefault((u_exp, v_exp, k + ai), {})[nsource + ai] = -F(coeff)
    # F2 = alpha*f: these order-two equations keep the multiplier tied to
    # the actual source symbol, rather than imposing only the cubic match.
    for col, p in enumerate(source):
        for key in normal_keys(p, 2):
            row_dict.setdefault(key, {})[col] = p[key]
    for ai in range(nalpha):
        for (u_exp, v_exp), fp in zip([(2, 0), (1, 1), (0, 2)], f):
            for (k,), coeff in fp.terms():
                row_dict.setdefault((u_exp, v_exp, k + ai), {})[nsource + ai] = -F(coeff)
    # - f*(l*u + m*v).
    lstart, mstart = nsource + nalpha, nsource + nalpha + nl
    for i in range(nl):
        for (k,), coeff in f[0].terms():
            row_dict.setdefault((3, 0, k + i), {})[lstart + i] = -F(coeff)
        for (k,), coeff in f[2].terms():
            row_dict.setdefault((1, 2, k + i), {})[lstart + i] = -F(coeff)
    for i in range(nm):
        for (k,), coeff in f[0].terms():
            row_dict.setdefault((2, 1, k + i), {})[mstart + i] = -F(coeff)
        for (k,), coeff in f[2].terms():
            row_dict.setdefault((0, 3, k + i), {})[mstart + i] = -F(coeff)

    cubic_equation_keys = sorted(row_dict)
    cubic_equation_matrix = sp.Matrix(
        [[row_dict[key].get(j, F(0)) for j in range(total_vars)]
         for key in cubic_equation_keys])
    cubic_kernel = cubic_equation_matrix.nullspace()
    projected_forms = []
    projected_alphas = []
    for vector in cubic_kernel:
        projected_forms.append(sp.Matrix(vector[:nsource, :]))
        projected_alphas.append(sp.Matrix(vector[nsource:nsource+nalpha, :]))
    alpha_projection = (sp.Matrix.hstack(*projected_alphas)
                        if projected_alphas else sp.zeros(nalpha, 0))
    form_projection = (sp.Matrix.hstack(*projected_forms)
                       if projected_forms else sp.zeros(nsource, 0))
    source_coefficient_matrix = sp.Matrix.hstack(*source_kernel)
    homogeneous_root_forms = source_coefficient_matrix * form_projection

    alpha_image_basis = alpha_projection.columnspace()
    alpha_basis = [[F(vector[i]) for i in range(nalpha)]
                   for vector in alpha_image_basis]
    alpha_gcd = gcd_with_infinity(alpha_basis, alpha_degree)
    free_pair = basepoint_free_pair(alpha_basis, alpha_degree)

    def vector_poly(values):
        return sp.Poly(sum(value * z**i for i, value in enumerate(values)), z,
                       domain=sp.QQ)

    def lift_alpha(alpha_values):
        """Select the first exact lift of an alpha vector to full solutions."""
        solution, parameters = alpha_projection.gauss_jordan_solve(
            sp.Matrix(alpha_values))
        if parameters.rows:
            solution = solution.subs({parameter: 0 for parameter in parameters})
        return solution

    def homogeneous_form_dict(coefficients):
        return {"x0^%d*x1^%d*x2^%d*x3^%d" % monomial: str(value)
                for monomial, value in zip(source_monomials, coefficients) if value}

    root_basis = []
    for j in range(len(cubic_kernel)):
        alpha_values = [F(projected_alphas[j][i]) for i in range(nalpha)]
        form_values = homogeneous_root_forms[:, j]
        root_basis.append({
            "alpha": str(vector_poly(alpha_values).as_expr()),
            "octic": homogeneous_form_dict(form_values),
        })

    free_pair_lifts = None
    pair_coefficients = None
    if free_pair is not None:
        free_pair_lifts = []
        pair_coefficients = []
        for expression in free_pair:
            poly = sp.Poly(expression, z, domain=sp.QQ)
            alpha_values = [F(poly.nth(i)) for i in range(nalpha)]
            coordinates = lift_alpha(alpha_values)
            form_values = homogeneous_root_forms * coordinates
            pair_coefficients.append(form_values)
            free_pair_lifts.append({
                "alpha": expression,
                "octic": homogeneous_form_dict(form_values),
            })
    certificate = (pair_certificate(pair_coefficients, source_monomials)
                   if pair_coefficients is not None else None)

    return {
        "source_dimension": len(source),
        "source_quadratic_projection_rank": quad_matrix.rank(),
        "source_quadratic_kernel_dimension": len(source) - quad_matrix.rank(),
        "order_three_source_dimension": len(order_three_source),
        "order_three_symbol_rank": order_three_cubic_matrix.rank(),
        "all_source_local_cubic_coefficient_rank": cubic_matrix.rank(),
        "source_cubic_max_z_degree": max_cubic_degree,
        "base_equation_rows": len(base_keys),
        "base_equation_rank": base_matrix.rank(),
        "seed_first_lift_equation_rows": len(cubic_equation_keys),
        "seed_first_lift_equation_rank": cubic_equation_matrix.rank(),
        "full_variable_kernel_dimension": len(cubic_kernel),
        "projected_actual_octic_basis_dimension": len(form_projection.columnspace()),
        "projected_actual_octic_dimension": form_projection.rank(),
        "projected_alpha_dimension": alpha_projection.rank(),
        "alpha_degree_bound": alpha_degree,
        "l_m_degree_bound": l_degree,
        "alpha_gcd": alpha_gcd,
        "basepoint_free_alpha_pair": free_pair,
        "basepoint_free_actual_octic_pair": free_pair_lifts,
        "coprime_pair_certificate": certificate,
        "alpha_basis": [[str(x) for x in row] for row in alpha_basis],
        "root_compatible_actual_basis": root_basis,
        "source_kernel_basis": source,
    }


if __name__ == "__main__":
    result = compute()
    # Keep the command-line report compact; reviewers can import compute()
    # to inspect all 12 actual homogeneous vectors and their multipliers.
    result.pop("source_kernel_basis")
    root_basis = result.pop("root_compatible_actual_basis")
    alpha_basis = result.pop("alpha_basis")
    actual_pair = result.pop("basepoint_free_actual_octic_pair")
    result["root_basis_dimension"] = len(root_basis)
    result["alpha_basis_vectors"] = len(alpha_basis)
    result["coprime_multiplier_pair"] = result["basepoint_free_alpha_pair"]
    result["coprime_pair_octic_term_counts"] = [len(x["octic"]) for x in actual_pair]
    result.pop("basepoint_free_alpha_pair")
    print(json.dumps(result, indent=2))
```
</details>
