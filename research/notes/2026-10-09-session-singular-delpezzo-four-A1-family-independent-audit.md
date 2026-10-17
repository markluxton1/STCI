# Independent audit of the projected four-A1 family

Date: 2026-10-09. Auditor: `family2_quadratic_independent_audit`, independent of the construction owner. This bounded audit used no child agents and edited no original source or canonical frontier document.

## Verdict and exact scope

**PROVED HERE:** over an algebraically closed field of characteristic zero, every quartic in the displayed family with

```text
alpha*beta*gamma*delta*(alpha*delta-beta*gamma) != 0
```

fails to admit a mate of any degree whose set-theoretic intersection is the exact fixed curve `C0=[U^4:U^3V:UV^3:V^4]`.

The [owner proof](2026-10-09-session-singular-delpezzo-four-A1-family.md) is accepted at this scope. The universal coordinate identities are checked by a separate implementation and isolated replays. The mathematical proof is the algebra and geometry below, not agreement between agents or a numerical parameter sample. The singular surface, smooth lifted curve, finite birational quartic image, and extra normalization point are bound to the actual fixed coordinates.

This family is not asserted to exhaust all four-A1 embeddings or projections, all genus-one singular normalizations, genus-two normalizations, or the unrestricted STCI problem. The parameter boundary where the displayed transformation becomes singular is outside this construction and outside this theorem.

## 1. The standard surface is integral and normal

Put `S=V(ae-c^2,bd-c^2)` in `P4[a:b:c:d:e]`. Here is a direct domain proof supplementing the owner's quotient-cover argument. In lexicographic order `a>b>c>d>e`, the leading monomials are `ae` and `bd`, which are relatively prime. The two equations therefore form a Groebner basis. Map their quotient ring to a Laurent polynomial ring in independent `r,s,t` by

```text
a -> r, b -> s, c -> t, d -> t^2/s, e -> t^2/r.
```

A standard monomial `a^i b^j c^k d^l e^h` has `i*h=j*l=0`, and maps to `r^(i-h)s^(j-l)t^(k+2l+2h)`. Its Laurent exponents recover `i,h` and `j,l` uniquely, and then recover `k`. Distinct standard monomials have distinct images. The homomorphism is consequently injective, so the quotient is a domain. It has dimension three: it contains algebraically independent `a,b,c` and embeds in their fraction field. The two equations form a height-two complete intersection, and the projective surface is integral of degree four.

The two gradient rows are

```text
(e,0,-2c,0,a),   (0,d,-2c,b,0).
```

Their rank drops exactly at the four projective coordinate vertices with nonzero `a,b,d,e`. The independent source forms all ten minors and verifies that their ideal with the two quadrics contains `c^3`, `(ae)^2`, `(bd)^2`, and the other four cross products in `a,b,d,e`. Conversely every generator vanishes at all four vertices. Its radical is therefore the four-axis ideal. Equivalently, if `c!=0` the minors force all other coordinates to vanish, contradicting a surface equation; with `c=0`, all six cross products vanish and only the four vertices remain.

In the `a=1` chart, eliminate `e=c^2`; the remaining local equation is `bd-c^2=0`. The other three vertices have the same A1 model. The complete intersection is Cohen-Macaulay, hence S2, and its singularities are isolated, hence it is R1. Serre's criterion gives normality. For `H=O_S(1)`, complete-intersection adjunction gives `K_S=-H`, `H^2=4`, and sectional genus one.

## 2. The curve and the coordinate transformation are correctly bound

Write `Delta=alpha*delta-beta*gamma`, `m=alpha*delta+beta*gamma`, and `n=alpha*beta*gamma*delta`. The owner's five-by-five transformation from `Y0,...,Y4` to `a,b,c,d,e` has determinant `n*Delta^3`. It is invertible on the entire specified parameter open. Thus the image of `Y_i=U^(4-i)*V^i`, `i=0,...,4`, is a smooth embedded rational normal quartic, denoted `c_S`. It is a projective change of coordinates of the standard RNC, not a merely generic parametrization. Its actual formulas are

```text
a=UV*(gamma U+delta V)^2,
b=-U^2*(alpha U+beta V)*(gamma U+delta V),
c=-UV*(alpha U+beta V)*(gamma U+delta V),
d=-V^2*(alpha U+beta V)*(gamma U+delta V),
e=UV*(alpha U+beta V)^2.
```

Both surface quadrics vanish identically. The curve passes through all four A1 vertices at four distinct parameters:

| Vertex | Parameter `[U:V]` | Nonzero coordinate value |
|---|---|---|
| `b` | `[1:0]` | `-alpha*gamma` |
| `d` | `[0:1]` | `-beta*delta` |
| `a` | `[beta:-alpha]` | `-alpha*beta*Delta^2` |
| `e` | `[delta:-gamma]` | `-gamma*delta*Delta^2` |

All values are nonzero under exactly the stated hypotheses. Deleting `Y2` gives the exact curve `C0` in the exact retained coordinates. This parametrization is an embedding: on `U!=0`, `x1/x0=V/U`, and on `V!=0`, `x2/x3=U/V`. These two affine charts prove smoothness and injectivity at the endpoints as well.

## 3. The projected image is an integral quartic with this normalization

Put `(x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2)`. The complete uniform identities are

```text
Q1=Delta^2*(x1*x2-z^2),
Q2=((m^2-n)/Delta^2)*Q1+z*L+R,

L=alpha^2*gamma^2*x0-alpha*gamma*m*x1
  -beta*delta*m*x2+beta^2*delta^2*x3,

R=alpha*gamma*m*x0*x2+n*x0*x3-alpha^2*gamma^2*x1^2
  -n*x1*x2+beta*delta*m*x1*x3-beta^2*delta^2*x2^2.
```

The independent checker verifies the second identity after clearing only `Delta^2`. Neither `m` nor `m^2-n` is inverted, so their zero loci are included.

The projection center `P=[0:0:1:0:0]` is outside `S`, since `Q1(P)=-Delta^2!=0`. Projection is a morphism. Every fibre is finite: on its projective line, the nonzero quadratic coefficient `-Delta^2` in `z` bounds the fibre by two points, including multiplicities. Properness makes the morphism finite.

On `L!=0`, the inverse is `z=-R/L`, or homogeneously

```text
[x0:x1:x2:x3] -> [L*x0:L*x1:-R:L*x2:L*x3].
```

This is an isomorphism on that open of the image. The open is nonempty because the restriction of `L` to `c_S` has nonzero endpoint values. The map is therefore birational. Its hyperplane pullback is `H`, so the finite degree-one image has degree `H^2=4`. The image `X` is integral, and `S->X` is its normalization since `S` is normal.

The polynomial `F=R^2-x1*x2*L^2` vanishes on the image. Its `x0^2*x3^2` coefficient is `n^2!=0`, so it is a nonzero quartic in every allowed specialization. The integral hypersurface image has degree four, hence `F`, up to a nonzero scalar, is its actual irreducible equation. The exact identity `Res_z(Q1,Q2)=Delta^4*F` is checked separately; irreducibility and birationality do not follow from that resultant alone.

## 4. The extra normalization point excludes every mate

On the exact curve, the independent source verifies

```text
L_C=alpha^2*gamma^2*U^4-alpha*gamma*m*U^3*V
    -beta*delta*m*U*V^3+beta^2*delta^2*V^4,
R_C=-U^2*V^2*L_C.
```

Both endpoint coefficients are nonzero. Over the algebraically closed field this homogeneous quartic has a root `[U:V]`, and every root has `UV!=0`. No squarefreeness is assumed: repeated-root subloci are covered.

At any such root, both points

```text
y_plus =[U^4:U^3V:+U^2V^2:UV^3:V^4],
y_minus=[U^4:U^3V:-U^2V^2:UV^3:V^4]
```

lie on `S` and project to the same point of `C0`. Indeed `Q1` vanishes on both and `Q2(y_minus)=-2U^2V^2*L_C=0`. They are distinct since characteristic zero and `UV!=0` give `2U^2V^2!=0`.

The negative point is outside `c_S`: the quadratic `Y0*Y2-Y1^2` vanishes on the entire RNC, but its value at `y_minus` is `-2U^6V^2!=0`. This excludes membership through a different parameter as well.

Here is the full-support argument without presupposing a singleton-fibre rule. Because the map is finite and is an isomorphism on `L!=0`, every curve in the inverse image of `C0` must dominate `C0` and equal `c_S`: its generic point lies over the generic point where `L_C!=0` and the inverse is unique. Additional points can only lie over the finite zero set of `L_C`.

Suppose a mate `G` of any degree satisfied `V_X(G)_red=C0`. Its pullback is a nonzero section of `O_S(deg G)`, since otherwise `G` would vanish on all of `X`. It vanishes at `y_minus`, which maps into `C0`. Locally trivialize the line bundle there. A nonzero nonunit in the integral surface's local ring has a height-one zero prime by the principal ideal theorem. Hence a curve in the pullback zero support passes through `y_minus`. Its finite image is contained in `C0`, so that curve must equal `c_S`. This contradicts `y_minus` being outside `c_S`.

This excludes every mate degree simultaneously. It requires neither a conductor calculation nor a bound on the mate degree nor cancellation of a multiple curve divisor on a singular surface.

## 5. The auxiliary double-curve and non-Cartier claims also hold

The owner uses the finite quotient cover from `P1xP1` given by its five invariant `(2,2)` sections. They are basepoint free and their torus function field has index two under `(t,u)->(-t,-u)`. For its odd `(2,2)` section, setting `r=t/u` gives

```text
u^2=-(alpha+beta*r)/(r*(gamma+delta*r)).
```

The four branch points `0,infinity,-alpha/beta,-gamma/delta` are distinct under precisely the hypotheses. The double cover is connected and has genus one. No boundary coordinate fibre is a component, because all four coefficients are nonzero. Its integral `(2,2)` closure has arithmetic genus one, so it has no singular defect.

The stated quadric section `Q` pulls back exactly to the square of this odd section. The independent checker verifies that identity and `Q` vanishing on the actual RNC. The odd curve is irreducible, so its finite image is the entire support of `Q`; since the RNC is contained in that support, the image is exactly `c_S`. The cover is unramified at the generic point, as the involution has only four fixed points. Thus the divisor of `Q` is exactly `2c_S`, giving `2c_S~2H`.

At each A1 vertex the curve is non-Cartier. Its curve local ring is regular of dimension one, whereas the surface local ring has embedding dimension three. Quotient by one element could decrease embedding dimension by at most one, leaving at least two; the curve ideal therefore cannot be principal. Together with the Cartier divisor `2c_S`, its nonzero local class has order two. On the minimal resolution the smooth curve meets each exceptional `(-2)` curve once: its three A1 chart coordinates vanish to first order, so its tangent direction lifts to one transverse point on the exceptional conic. The correction is half the sum of the four exceptional curves, of square `-2`. This validates the auxiliary identity `q=2pi=2`. The exclusion itself is already proved in section 4.

## 6. Frozen evidence and reproduction

The independent [countercheck](../validation/2026-10-09-four-A1-family-audit/countercheck.py) uses universal parameters, not a sample. It verifies the coordinate, cancellation, resultant, actual curve, singular-locus, local A1, cover-square, branch-equation, and extra-point identities. Its SHA256 is

```text
9412835cf6ef3df5f0e1b9c9f3d5208a7bc89ed4e0d1bf904f0d1f0f7386317c
```

Its terminal result is in [countercheck-result.json](../validation/2026-10-09-four-A1-family-audit/countercheck-result.json). Both the frozen owner checker and this checker ran in an isolated snapshot with terminal exit code zero. Their deterministic reports were byte-identical to the corresponding saved repository reports, and snapshot inputs stayed unchanged. The owner replay took 0.580 seconds; the independent replay took 0.651 seconds. The [isolated replay manifest](../validation/2026-10-09-four-A1-family-audit/isolated-replay-manifest.json) preserves the execution record.

The original source is actually at [computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py](../../computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py), with SHA256 `0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4`. Its root-level computation path is preserved rather than silently rewritten.

Reproduce the independent controls:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-09-four-A1-family-audit/countercheck.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-09-four-A1-family-audit/isolated-replay.py
```

The frozen snapshot includes the owner proof as inspected, both exact sources, and both reports. The [aggregate audit manifest](../validation/2026-10-09-four-A1-family-audit/audit-manifest.json) binds this independent note and all evidence files. No process from this bounded audit remains running. The global question and singular-normalization strata outside the explicit family remain open.
