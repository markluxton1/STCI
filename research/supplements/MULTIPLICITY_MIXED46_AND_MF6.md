# Multiplicity, mixed (4,6) cases, and MF6 pairing

Consolidated mathematical source material; conditional statements and independent audits retain their original status.

---

## 2026-10-05-audit-regular-pure

# Independent audit: the pure constant directions in regular degree (4,6)

Date: 2026-10-05. Status: **PASS**, with a small local-intersection
clarification recorded below. Scope is exactly characteristic zero,
the smooth monomial rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), and the regular-ratio branch. This audit
does not extend the result to arbitrary ratios, mixed constant directions,
degree-one horizontal directions, or all rational quartics.

The audited proof is
`research/notes/2026-10-05-mixed46-regular.md`, and its exact arithmetic
companion is `research/computations/verify_mixed46_regular.py`.
The conclusion is that, after globally subtracting a quadratic multiple of
the quartic from the sextic, a hypothetical set-theoretic pair cannot have
quartic first normal form \(hV\) or \(hU\) in the stated balanced frame.

## What was checked independently

The full exact script was run with

```
/private/tmp/stci-cas-venv/bin/python research/computations/verify_mixed46_regular.py
```

It passed its assertions. Before reading the complete proposed proof, the
audit independently derived the Segre residual

\[
\rho=b_0(c_0a_0^3+c_3a_0^2a_1+c_6a_0a_1^2+c_9a_1^3)
     +b_1(c_1a_0^3+c_4a_0^2a_1+c_7a_0a_1^2),
\]

where \(F|_Q=c\rho\) and \(c=a_1b_0^3-a_0b_1^3\). The eight-dimensional
pure quartic space and the formulas

\[
h=c_0+c_1z+c_3z^3+c_4z^4+c_6z^6+c_7z^7+c_9z^9,
\qquad
R=\kappa+c_6z-c_7z^2+3c_9z^4
\]

agree with the derived ideal-space calculation.

For a genuine pair, the forms have no common surface factor. Thus their
intersection is a degree-24 complete-intersection curve supported on
\(C_0\), and its generic transverse length is \(24/4=6\). This is sufficient
for the generic elimination argument; it does not assert uniform
curvilinearity at every point.

The ambient sextic reduction uses the proved symbolic-square description
from P-017/P-022:

\[
H^0(I_C^{(2)}(6))
=qH^0(I_C(4))+\langle A^2,AB,B^2,BD,D^2\rangle.
\]

Only \(D^2\) contributes to the coefficient of \(z^{10}U^2\), and its
coefficient is \(4\). Every \(qF_4\) term contributes to that coefficient
with degree at most nine. Therefore divisibility of the quadratic normal
form by \(V\) kills the \(D^2\) coefficient, and indeed makes
\(a_0\mid\sigma\) in \(G|_Q=c^2\sigma\). This is an exhaustive ambient
kernel argument, not an assumption that an arbitrary jet lifts.

## Boundary and contact-degree checks

If \(c_9=0\), the displayed residual has the factor \(a_0\). Since
\(a_0\mid\sigma\) too, the entire ruling \(a_0=0\) lies in both carriers.
It is an extra line, so this boundary is excluded without any smoothness
assumption.

If \(c_9\ne0\), let \(P=[0:0:0:1]\). In the chart \(x_3=1\), put
\((x_0,x_1,x_2)=(X,Y,W)\). At \(P\),

\[
dF=2c_9\,dX,\qquad dq=dX.
\]

Hence the two smooth surfaces \(F\) and \(Q\) have the same tangent plane.
On \(Q\), use \((a_0,b_0)=(Y,W)\), so

\[
c=W^3-Y,\qquad
\rho=c_9W+c_7Y+O((Y,W)^2).
\]

The tangent to \(C\) is the \(W\)-axis. The tangent to \(\rho\) is
\(c_9\,dW+c_7\,dY=0\), so these curves are transverse in the common
tangent plane. Consequently their local intersection multiplicity is one
on **both** \(Q\) and the smooth surface \(F\). This last observation is
the small clarification needed when passing from the intersection
calculation on \(Q\) to divisibility on \(F\); intersection multiplicity
on two unrelated containing surfaces should not be identified without
checking it.

In particular \(Y=a_0\) is a parameter on the smooth germ \(\rho\), and a
local Cartier equation \(v\) for \(C\subset F\) restricts to an element of
order one on \(\rho\). Generic order six along \(C\) implies
\(v^6\mid G\) in \(\mathcal O_{F,P}\). One can justify this by localizing
at the height-one prime \((v)\) in the regular local ring and then
contracting \((v^6)\); regularity makes this symbolic power ordinary.
Thus

\[
\operatorname{ord}_{\rho,P}(G)\ge6,
\quad
\operatorname{ord}_{\rho,P}(c)=1,
\quad
\operatorname{ord}_{\rho,P}(\sigma)\ge4.
\]

Since \(\sigma\) is a binary quartic, this forces
\(\sigma=\gamma a_0^4\), \(\gamma\ne0\). An initially considered
objection—that finite zeros of \(h\) might permit additional residual
rulings—is resolved by this local argument: the single smooth point
\(P\) already exhausts the degree-four vanishing allowance of \(\sigma\).
Support considerations alone would not have forced this concentration.

## Cubic identity and final contradiction

The residual equality gives
\(G=\gamma A^2+qF'\). Because \(G\) has normal order at least two and
\(q\) has order one generically, the quotient quartic lies in \(I_C(4)\).
Divisibility of \(G_2\) by \(V\) then forces the first normal form of
\(F'\) to be \(h'V\). No quartic quotient is omitted.

The elimination \(V=-(R/h)U^2+O(U^3)\) gives cubic coefficient
\(R'-h'R/h\). After subtracting the scalar multiple of \(F\) that removes
\(c'_9\), the coefficients in the necessary identity
\(hR'-h'R=0\) successively give

\[
[z^{11}]=-4c_9c'_7,\quad
[z^{10}]\big|_{c'_7=0}=-2c_9c'_6,\quad
[z^9]\big|_{c'_7=c'_6=0}=c_9\kappa'.
\]

Thus \(c'_7=c'_6=\kappa'=0\), then \(R'=0\), then \(h'=0\) since
\(R\ne0\). The quartic space has no further first-normal kernel beyond
\(kq^2\), already killed by \(\kappa'=0\), so \(F'\) was a scalar
multiple of \(F\). Modulo \(F\), the sextic is \(\gamma A^2\).
Since \(A=V\) on the affine chart and \(R\ne0\), its generic transverse
order is exactly four, contradicting six.

Finally the coordinate reversal can be checked directly, without importing
an orbit assertion. Put

\[
w=\frac{z^3+V}{z^4+U+\tfrac32zV},\qquad
\widetilde V=\frac z{z^4+U+\tfrac32zV}-w^3,
\]

\[
\widetilde U=\frac1{z^4+U+\tfrac32zV}-w^4-\tfrac32w\widetilde V.
\]

To first normal order,

\[
\widetilde V=2z^{-7}U,
\qquad
\widetilde U=\tfrac12z^{-7}V.
\]

Thus the reversal exchanges the two pure constant directions and preserves
the regular-ratio condition. The pure-\(U\) conclusion follows from the
fully audited pure-\(V\) case.

No counterexample or missing parameter stratum was found within the stated
scope. The productive remaining branch is the mixed constant direction,
where both coefficients are nonzero; the proof above gives no conclusion
there.


---

## 2026-10-05-mf6-further-audit

# MF6 audit and higher-jet exclusions for the mixed (4,6) pole branch

Started 2026-10-05; completed and resumed 2026-10-06. Characteristic zero
for the global application to `C0=[s^4:s^3t:st^3:t^4]`. The local MF6
identity and the lattice lemma below do not use characteristic zero.
No global sextuple structure or STCI pair is constructed here.

**Proved in this note:** the local identity MF6 is valid with its stated
finite-flat quasiprimitive lci hypotheses. Every hypothetical `(4,b)` pair
on C0 with constant normal quotient `e=0` has `deg D2>=3`. For `(4,6)` the
numerical type `(e,d2,d3)=(0,3,6)` can only have a regular first-normal
ratio. Thus the e=0 nonregular branch is reduced to `(d2,d3)=(4,5)`, with
pole length 3 or 4. The e=1 branches are not excluded here.

The independent prerequisite audit is
`2026-10-05-mf6-pairing-audit.md`. The exact companion programs are
`../computations/verify_mf6_defect12.py` and
`../computations/verify_mf6_type3.py`; both derive complete parameter spaces
and test the exceptional members symbolically. The low-defect exclusion,
including the second pure direction and the degree-five caveat, was also
independently checked by the local-pairing auditor. The completed separate
type-three audit in `2026-10-06-mf6-type3-independent-audit.md` confirms the
cubic-pole argument, its quotient-chart exhaustion, and its direct infinity
calculation; no gap was found under the stated hypotheses.

## 1. MF6, including the torsion and generation steps

Let R be a completed DVR along the smooth reduced support, B its rank-six
finite-free embedded lci algebra, and `N_i=B intersect (y^i) B_K` its
saturated BF ideals, where `B_K=K[y]/(y^6)`. Finite-flat Gorenstein duality
gives actual perfect multiplication pairings on the saturated pieces. In
particular

    E_i=L^i(D_i), D4=D5=D2+D3, 0<=D2<=D3.

This is stronger than a degree equality; its proof and the precise
Gorenstein and saturation boundaries are in the pairing-audit note.

Choose ambient normal coordinates y and x with y mapping to a local unit
of `E1=L` and x in N2. Replacing the second normal coordinate by its
difference with an R-multiple of y achieves this. B is generated over R
by x,y: their images come from the two formal ambient normal parameters,
and nilpotence reduces all formal series to finite sums of words.

Write `a=ord D2`, `b=ord(D3-D2)`. In a triangular adapted basis
`1,y,b2,b3,b4,b5`, multiplication by y has successive valuations
`0,a,b,a,0`. The final unit relation kills b5 in `B/yB`. The remaining
nilpotent torsion ideal `T=N1/yB` has the triangular presentation

    t^a b2+c b3+d b4,
    t^b b3+z b4,
    t^a b4.

Units have been absorbed in each leading coefficient. Its length is
`2a+b`. The image of N4 is exactly `R/(t^a) b4`: a linear combination of
the first two relations giving a relation on b4 alone has zero first,
then zero second coefficient, since R is a domain.

The quotient algebra `B/yB` is generated by x, so T is the ideal (x).
Since x lies in N2 and N6=0, x^3=0. Consequently T^2 is the R-cyclic
module generated by x^2, with no unaccounted higher products. Write
`x=u b2 mod N3`. If a>0 then u is a unit: modulo N3, the only words
capable of generating E2 are x and y^2, and y^2 has nonunit leading
coefficient t^a. Otherwise the ambient generators would fail to generate
E2 modulo t. If a=0 the image of N4 in T is already zero.

The map `E2^2->E4` has valuation b. Thus
`x^2=unit*u^2*t^b*b4 mod N5`, giving

    length T^2=max(a-b,0),
    length T/T^2=2a+b-max(a-b,0)=a+b+min(a,b).

Finally, `T/T^2=N1/(N1^2+yB)` is the torsion kernel-direction part of
the first-normal cokernel. The primitive normal kernel coordinate x has
relations `t^A x`; the Fitting exponent is therefore exactly this length.
This proves the pointwise divisor identity

    A=D3+(D2 wedge (D3-D2)).                 (MF6)

Every term is intrinsic, so the local identity globalizes. No subtraction
of a globally regular multiple of the quartic is used. Neither `A=D3` nor
`A=D2+D3` holds universally: the exact examples in the original pole note
remain necessary safeguards. In particular the global degree of a
coefficientwise minimum cannot be replaced by the minimum of two degrees.

## 2. The complete embedded triple obstruction when e=0

Use the balanced affine conormal coordinates

    U=x3-z^4-(3/2)z(x2-z^3), V=x2-z^3,

on x0=1. On the other chart the exact moving-coordinate transition is

    W=(z^3+a)/(z^4+b),
    a'=z/(z^4+b)-W^3, b'=1/(z^4+b)-W^4,
    U'=a'/2, V'=-3W a'+2b',
    a=V, b=U+(3/2)zV.

Both first-order frames transform by z^-7. For the constant kernel
direction `m=U+theta V`, put `ell=V`. The obstruction to the first
embedded triple is the exact Laurent cocycle

    h2=3theta^3 z^-5-(3/2)theta^2 z^-4
       +(3/4)theta z^-3-(3/8)z^-2.

At the missing point use `m=V,ell=U`; its cocycle is `3z^-5`.
These are derived from the moving coordinate, not from a linear-only
transition.

If `d=deg D2`, the triple has pieces `O,L,L^2(D2)`, with `L=O(-7)`.
Its canonical multiplication divisor has a nonzero section
`delta in H0(O(d))`. Necessarily multiplication by delta kills h2 in
`H1(O(-7+d))`, whose Laurent coordinates are
`z^-1,...,z^(-6+d)`. Local solutions satisfy

    delta_U h2+gamma_U=z^(-7+d) gamma_V,
    I3=(delta m-gamma ell^2,m ell,m^2,ell^3).

The latter ideal describes the required embedded triple; flatness demands
that delta and gamma have no common zero. For d<=5, the solution gamma is
unique because `H0(O(-7+d))=0`. These necessities do not assume the final
multiple curve is primitive everywhere.

For d=1, the first two rows of the finite-chart killing matrix have
determinant `-9/64`, independent of theta. The missing-chart matrix also
has rank two. There is no nonzero killing section. This excludes d=1.

For d=2, a three-row minor is `-(27/32)theta^4`, so all theta!=0 fail.
At theta=0 the sole projective solution is

    delta_U=z^2, delta_V=1, gamma_U=3/8, gamma_V=0.

At the missing point it is

    delta_U=1, delta_V=w^2, gamma_U=0, gamma_V=3.

Both triples are flat; their defect divisors are twice an endpoint. Their
existence as triples is retained, rather than incorrectly excluded by
endpoint flatness.

## 3. A quartic containing either degree-two triple has a plane factor

Write the first-normal form of a pure-U quartic F as hU, and its V^2
coefficient as Q. Membership in the first degree-two triple forces

    z^2 Q+(3/8)h=0.

Indeed substitute the generic triple relation `U=(3/8)z^-2 V^2` and
take the V^2 coefficient. Clearing z^2 is valid as a rational identity on
the generic curve; it loses no boundary chart, since the actual global
triple is already fixed and membership is necessary everywhere.

The complete quartic ideal space is derived from

    q=x0x3-x1x2, A=x0^2x2-x1^3,
    B=x0x2^2-x1^2x3, D=x2^3-x1x3^2.

The forms `q*S2 + <A,B,D>*S1` have dimension 18 and span `I_C(4)`.
The exact first-normal and quadratic coefficient equations give the full
compatible space

    <x0D,x1D,x2D,x3D>.

At the other pure direction, direct equations `coeff_U F=0` and
`coeff_U^2 F=0` give `<x0A,x1A,x2A,x3A>`. This direct check avoids reliance
on an unstated frame involution. Thus every nonzero compatible quartic is
a cubic times an ambient linear form.

Such a quartic cannot belong to a defining pair supported on the nonplanar
integral C0. If its plane factor is contained in the mate, there is a
common surface. Otherwise the mate restricts to a nonzero positive-degree
form on that plane and cuts out a nonempty curve there. This curve would
have to lie in C0, which is impossible because C0 is integral and is not
contained in a plane. This excludes d=2 for every positive mate degree b.

Together with P-010 and the uniform `deg D2<=5` bound for e=0, every
hypothetical characteristic-zero `(4,b)` pair on C0 has

    e=0 => deg D2 in {3,4,5}.

The claim is mate-independent but specific to the monomial quartic C0;
it is not asserted for every rational quartic orbit.

## 4. The exact third-piece lattice lemma

This lemma retains the higher-normal coefficient missing from first-normal
arguments. Let the canonical length-four quotient be generated over a DVR
R by m,y, with generic embedding into `K[y]/(y^4)` given by

    m=f2*y^2+f3*y^3.

This is the actual quotient `B/N4`, which is R-free because N4 is
saturated, and its image equals `R[m,y]`. Hence the following generating
words give its exact lattice rather than a chosen sublattice:
`1,y,y^2,y^3,m,ym`.

If f2 is regular, subtract f2*y^2 from m. Then

    ord D2=0, ord D3=max(0,-val f3).

If `val f2=-a<0`, use m as the degree-two pivot. Subtracting
`f2^-1*m` from y^2 gives `-(f3/f2)y^3`, while ym=f2*y^3. The saturated
degree-three lattice is generated by `y^3,f2*y^3,(f3/f2)*y^3`. Therefore

    ord D2=a, ord D3=max(a,-a-val f3).

This exact formula does not require B/N4 to be Gorenstein. It uses
two-generator embeddedness, saturation, and the full cubic coefficient.
It also shows why the multiplicity-five type-A terminal calculation
cannot be imported into a sextuple: its fourth piece is different.

## 5. The d2=3 quartic pencil and all of its cubic poles

For degree three, the two pure directions fail triple flatness: every
killing section contains an additional homogeneous linear factor common
to delta and gamma. For theta!=0 the complete killing matrix has unique
projective kernel

    delta_U=z(z+2theta), delta_V=w+2theta w^2,
    gamma_U=3/8, gamma_V=6theta^4.

The divisor includes infinity despite the affine degree two. The torus
`z->lambda z` carries theta to theta/lambda, so normalize theta=1.
Then D2 consists of the three simple points `0,-2,infinity`.

In the complete eight-dimensional quartic space with first form `h(U+V)`,
the triple-membership equation

    delta*Q+(3/8)h=0,
    Q=coeff_ell^2 F(U=-ell,V=ell)

has kernel dimension two. Its quartics are a pencil `alpha F0+beta F1`.
The members F0,F1 are uniquely specified by these conditions and first
coefficients

    h0=-2[z(z+2)]^3,
    h1=-2z(z+2)(z^2+4)(z^4+16).

Uniqueness follows because the first-normal kernel in `I_C(4)` is `<q^2>`,
and q^2 fails triple membership. The verifier derives both full homogeneous
quartics, rather than assuming existence from these prescribed first forms.

Put

    P=alpha z^2(z+2)^2+beta(z^2+4)(z^4+16),
    N=alpha z(z+2)(z+4)
      +beta(z^5+2z^4+16z^2-16z+96).

Generic formal elimination of F in coordinates `m=U+V,y=V` gives

    m=f2 y^2+f3 y^3+..., f2=3/[8z(z+2)],
    f3=-N/[16z^2(z+2)^2 P], h=-2z(z+2)P.

The first and second canonical pieces force these coefficients in any
hypothetical sextuple supported on C0; later coefficients cannot change
its saturated length-four quotient.

If beta!=0, P has degree six, is nonzero at 0 and -2, and as a section of
O(6) is nonzero at infinity. All its zeros lie off D2. The exact resultant
is

    Res_z(P,N)=2^34 beta^10(alpha+4beta).

If alpha+4beta!=0, the divisor of poles of f3 off D2 has degree six.
The lattice lemma gives that exact contribution to D3; since D3>=D2,
`deg D3>=6+3=9`.

The exceptional value alpha=-4beta is checked separately, not discarded:

    P/beta=(z-2)^2(z^2+2z+4)^2,
    gcd(P,N)=z-2 up to a unit.

There is precisely one canceled pole unit; the polar divisor off D2 has
degree five, so `deg D3>=5+3=8`. These inequalities include repeated
roots with their exact multiplicities. They are incompatible with d3=6.

Thus beta=0 is necessary for the numerical type `(d2,d3)=(3,6)`. At its
finite chart

    f3=-(z+4)/[16z^3(z+2)^3].

It has pole order three at both 0 and -2, where f2 has pole order one.
The lattice lemma gives `ord D3=2` at both points and zero away from them.
The remaining support point is verified directly in the moving second
chart, not inferred from degrees. Put

    x3=1, x2=w, x1=w^3+2U', x0=w^4+V'/2+3wU'.

For F0 the first coefficient is `h'=-2w^3(1+2w)^3`; solving in
`m'=U'+V',y'=V'` gives

    f2'=6/[w(1+2w)],
    f3'=-8(18w^2+8w-1)/[w^3(1+2w)^3].

At w=0 the cubic numerator is a unit. Thus infinity also contributes
`ord D3=2`, and

    D3=2D2, H=3D2.

MF6 gives `A=D3+(D2 wedge (D3-D2))=3D2=H`. Hence the pole divisor
`P_pole=H-A` is zero. This excludes the **entire nonregular** e=0,
`(d2,d3)=(3,6)` branch; beta=0 remains a regular-ratio possibility.
No sextuple existence or exclusion of that regular member is claimed.

## 6. Surviving strata and a failed uniform shortcut

Combining these exclusions with MF6 leaves the following coarse nonregular
strata for `(4,6)`:

| e | defect type | allowed pole length |
|---|---|---|
| 0 | (d2,d3)=(4,5) | 3 or 4 |
| 1 | (0,4) | 4 |
| 1 | (1,3) | 4 or 5 |
| 1 | (2,2) | 6 |

These are five coarse pole-length strata and six numerical-type incidences.
The reductions are necessary; they do not realize or exclude these entries.

It is tempting to strengthen the endpoint argument to exclude every pure
e=0 quotient for every multiplicity. This is false at the triple stage.
For d=3,4, the pure-U solution is `delta_U=z^2 r`,
`gamma_U=3r/8,gamma_V=0`, so the positive-degree homogeneous factor r
supplies a common zero and prevents flatness. At d=5, the Cech target is
`H1(O(-2))`, and its single coordinate only forces the z^1 coefficient
of delta to vanish. The correct solutions are

    delta_U=d0+z^2 r(z), deg r<=3,
    gamma_U=3r/8, gamma_V=-3d0/8.

When d0!=0 the pair delta,gamma has no common zero. For example d0=1,r=0
gives `delta_U=1,delta_V=w^5,gamma_U=0,gamma_V=-3/8`. The nonzero quartic

    -2x0^3x3+3x0^2x1x2-x1^4

has pure-U first form and zero V^2 coefficient, so it passes this triple
membership condition. It is a retained exact triple-compatible model;
it does not provide a global STCI mate. This is why the uniform claim is
`d2>=3`, rather than blanket exclusion of all pure quotient directions.

## 7. Reproducibility and continuation

Run with SymPy 1.14.0:

    /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_defect12.py
    /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_type3.py

Both pass. The second reruns the first and uses its independently derived
complete quartic ideal basis. The local lattice lemma is proved above
rather than inferred from sampling. The next e=0 target is d2=4,d3=5:
derive all flat degree-four killing sections and intersect them with the
complete quartic space, retaining the canonical cubic-pole divisor and
all exceptional quartic members. The regular type-three member, the e=1
branches, and all higher carrier degrees remain unresolved by this note.


---

## 2026-10-05-mf6-pairing-audit

# MF6 prerequisite audit: perfect pairings on the saturated filtration

Date: 2026-10-05. Independent local-algebra audit of P-042 and
`research/notes/2026-10-05-mixed46-poles.md`. The assertion audited here is
proved below for arbitrary multiplicity and arbitrary characteristic. This
does not construct a global multiple curve or an STCI representation.

## 1. Verdict and exact hypotheses

Let R be a DVR, K its fraction field, and B a commutative finite-free local
R-algebra. Suppose

1. B_K is isomorphic as a K-algebra to K[v]/(v^n); and
2. B is a relative Frobenius algebra: there is an R-linear functional
   lambda:B -> R such that b -> (c -> lambda(bc)) is an isomorphism
   B -> Hom_R(B,R).

Define the saturated filtration

    N_i = B intersect (v^i)B_K,  0 <= i <= n,
    E_i = N_i/N_{i+1},           0 <= i < n.

Then all E_i are free of rank one and the actual multiplication maps

    E_i tensor_R E_{n-1-i} -> E_{n-1}

are isomorphisms. Finite-flat Gorenstein, and hence finite-flat local complete
intersection, implies condition 2. Relative embedding dimension two is not
needed for this pairing theorem. It is a separate hypothesis needed for the
subsequent MF6 argument that B is generated by the two ambient normal
coordinates.

In the completed smooth-support setup of P-042, B is the quotient of
k[[t,x,y]] by a regular sequence of two equations, supported on (x,y).
It is finite over R=k[[t]], and t is a nonzerodivisor because B is
Cohen--Macaulay with one-dimensional support. Therefore B is finite-free over
R. Its special fibre is an Artin complete intersection and is Gorenstein, so
the Frobenius condition follows. No characteristic-zero argument is used
in this local deduction.

## 2. Elementary proof over the DVR

Each N_i is an ideal. B/N_i is torsion-free over R: if t b belongs to N_i,
then b belongs to (v^i)B_K as well, hence to N_i. Thus B/N_i is free and
N_i is an R-direct summand of B. Likewise E_i embeds into
(v^i)B_K/(v^{i+1})B_K, so E_i is torsion-free and has rank one. Multiplication
satisfies N_i N_j subset N_{i+j}.

N_1 is exactly the nilradical: its elements have nth power zero in B_K,
and hence in B. The constant-coefficient image B/N_1 embeds into K and is
integral over R, so it equals R because a DVR is integrally closed. Thus
E_0=B/N_1=R follows already from the stated hypotheses.

The generic algebra gives the exact annihilator identity

    Ann_B(N_i) = N_{n-i}.

Indeed, it gives the identity after tensoring with K; torsion-freeness of B
then implies both inclusions integrally. Equivalently, this follows directly
by multiplying in K[v]/(v^n).

For an ideal J of B, let J^perp consist of those b with lambda(bJ)=0. The
Frobenius property gives

    J^perp = Ann_B(J).

The nontrivial inclusion is worth spelling out. If lambda(bj)=0 for all
j in J, then lambda((bj)c)=0 for every c in B because jc belongs to J.
Nondegeneracy of the pairing on B implies bj=0.

Consequently N_i^perp=N_{n-i}. Fix i. A functional on
E_{n-1-i}=N_{n-1-i}/N_{n-i} extends to an R-linear functional on B, because
the filtration consists of R-direct summands. Represent the extension by an
element b in B using the Frobenius isomorphism. Its vanishing on N_{n-i}
forces b into N_i. The kernel of restriction from N_i is

    N_i intersect N_{n-1-i}^perp = N_{i+1}.

This proves

    E_i isomorphic to Hom_R(E_{n-1-i},R)

via the multiplication followed by lambda. Taking i=0 proves that
lambda restricts to an isomorphism N_{n-1}=E_{n-1} -> R: E_0=R, since
B_red=R. Hence the original multiplication map with target E_{n-1} is
perfect, not only its composition with a scalar-valued functional.

For completeness, finite-free local Gorenstein algebras admit the functional
used here without choosing a trace. The special fibre A=B/tB is local Artin
Gorenstein. Choose a k-linear functional on A nonzero on its one-dimensional
socle. Its product pairing is nondegenerate: every nonzero ideal of A meets
the socle. Lift this functional to B using a free R-basis. The determinant
of its product-pairing matrix is nonzero modulo t, hence is a unit in R.
This is the required lambda. The usual algebra trace is generally degenerate
on nilpotent algebras and must not replace this Frobenius functional.

## 3. Consequence in multiplicity six

For n=6, write E_i=L^i(D_i), D_1=0, where D_i are the divisors of the
generically invertible maps L^i -> E_i. Because these maps arise from the
same multiplication, the pairings imply equalities of divisors, not only
equalities of line-bundle classes or degrees:

    D_i + D_{5-i} = D_5.

Thus D_4=D_5=D_2+D_3. Effectivity and the multiplication E_2^2 -> E_4 give
2D_2 <= D_4, equivalently 0 <= D_2 <= D_3. This verifies the precise
prerequisite used in P-042 and MF6.

An adapted triangular basis with b_1=y gives coefficients of multiplication
by y with valuations

    0, ord(D_2), ord(D_3-D_2), ord(D_2), 0,

as asserted in the MF6 note. The unit in the last position follows from a
perfect pairing; it does not need an extra assumption about the degeneration
of the special fibre.

## 4. A countermodel when Gorenstein is omitted

Let R=k[[t]] with char(k)=0, and inside K[y]/(y^6) put

    x = t^-1 y^2 + t^-2 y^3,
    B = R[x,y].

The following is an R-basis:

    1, y, x, z=y^3/t, w=y^4/t^2, u=y^5/t^3.

All its members belong to B, since

    z=t x-y^2,  w=x y-z,  u=(x^2-w)/2.

The relevant multiplication table is

    y^2=t x-z,  x y=z+w,  x^2=w+2u,
    y z=t w,    y w=t u,  x z=t u,

and all products of x or y with u, of x with w, and among z,w,u vanish.
This exhibits B as finite-free of rank six, generated by two nilpotent
normal coordinates, with generic algebra K[y]/(y^6). Its saturated defect
sequence, measured relative to y, is

    (D_1,D_2,D_3,D_4,D_5)=(0,1,1,2,3) at t=0.

In particular, E_1 E_4 -> E_5 and E_2 E_3 -> E_5 both have coefficient t.
They are not perfect. At t=0, the maximal ideal has square spanned by z,w,u
and cube zero. The special-fibre Hilbert function is (1,2,3), and its socle
has dimension three. Thus B is not Gorenstein and cannot be a local complete
intersection. This example shows that finite-flat quasiprimitivity and two
ambient generators are insufficient by themselves.

The existing exact lattice program confirms the basis invariants and socle:

    /private/tmp/stci-cas-venv/bin/python research/scratch/mixed46/local_lattice.py

Its case (1,2,0,0) reports ((0,0,1,1,2,3),2,3), meaning the complete defect
sequence including E_0, first-normal Fitting exponent 2, and socle dimension
3. These are local examples, not global candidates on C0.

## 5. Saturation is essential even for a local complete intersection

Take the length-six finite-flat complete intersection

    B=R[x,y]/(t x-y^2, x^3).

An adapted basis is 1,y,x,xy,x^2,x^2y. Its saturated defects are
(0,0,1,1,2,2), and E_1 E_4 and E_2 E_3 both map with unit coefficient to
E_5. A Frobenius functional is the coefficient of x^2y in this basis.

However, the ordinary nilradical power N^2 contains t x but not x; its
saturation N_2 does contain x. Hence N/N^2 has a nonzero R/(t) summand and
is not the line bundle E_1. A claim about ordinary powers must not be
silently substituted for the saturated BF claim proved above.

## 6. Primary-source cross-check and continuation boundary

The direct argument is consistent with Nicolae Manolache, *Duality for
Gorenstein multiple structures on smooth algebraic varieties*, Rev. Roumaine
Math. Pures Appl. 68 (2023), 141--148, DOI 10.59277/RRMPA.2023.141.148.
The theorem on page 143 identifies the canonical multiplication dualities;
Remark 2 on page 145 identifies all three filtrations in the quasiprimitive
case. The publisher's primary text is
[available here](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf).
The earlier preprint is [arXiv:0706.2204](https://arxiv.org/abs/0706.2204).

This audit closes the pairing prerequisite. It does not audit every later
MF6 length calculation and does not turn its necessary divisor identity into
global existence or exclusion. The next local-to-global step must retain
the complete saturated ideals, defect divisors, and higher normal jets.


---

## 2026-10-05-mixed46-poles

# Mixed (4,6): the first-normal Fitting divisor and the multiplicity-six defects

Date: 2026-10-05. Characteristic zero for the application to C0; the local
algebra argument below works in any characteristic in which the stated
quasiprimitive Gorenstein filtration and pairings hold. This note does not
assert existence of a global sextuple structure or an STCI pair.

## 1. What was checked before continuing

The starting data are P-031, P-038, and P-042 in
`research/RESEARCH_RECORD.md`, and the mixed-(4,6) frontier in
`research/SUCCESSOR_HANDOFF.md`. A pair supported on the monomial smooth
rational quartic C0 would be a finite-flat quasiprimitive multiplicity-six
lci. P-042 gives pieces

    O, L, L^2(D2), L^3(D3), L^4(D2+D3), L^5(D2+D3),
    0 <= D2 <= D3.

The conormal quotient has L=O(-7+e), e=0 or 1. The seven necessary numerical
types are e=0 with (d2,d3)=(1,8),(2,7),(3,6),(4,5), and e=1 with
(d2,d3)=(0,4),(1,3),(2,2). P-031 writes first forms f1=h*ell,
g1=k*ell, H=(h)_0=A+P, K=(k)_0=A+Z, and obtains

    deg A + deg P = 9-e,  deg Z = deg P + 8.

The divisor A is coordinate-independent: it is Fitt_1 of the cokernel of
the first-normal map. The quotient k/h may have poles. None of the argument
below subtracts a globally regular multiple of the quartic from the sextic.

The important prerequisite is P-042's *perfect multiplication pairings* for
the BF filtration, not merely equality of the degrees of its pieces. The
local proof uses those pairings, local freeness of all BF pieces, finite
flatness over the support, and embedding dimension at most two relative to
the support.

## 2. Exact local identity (proved; independent audit requested)

Let R be the completed DVR of the smooth support at a point, let B be the
finite-flat length-six local algebra, and let N be its nilradical. Write
N_i for the saturated BF ideal whose generic fiber is (v^i) in
K[v]/(v^6). Thus N_0=B, N_1=N, and N_6=0. Choose a triangular R-basis
b0,...,b5 adapted to this flag, with b0=1 and b1=y, where y maps to a
generator of E1=N_1/N_2. Choose the other ambient normal parameter x so
that x lies in N_2. The algebra B is generated over R by x and y, since
these are ambient normal coordinates and all their sufficiently high
products vanish.

Put

    a=ord(D2), b=ord(D3-D2), so a,b>=0.

The five successive leading coefficients of multiplication by y on the BF
flag have valuations

    0, a, b, a, 0.

This follows from E_i=L^i(D_i), D4=D5=D2+D3, and the fact that y generates
L. In particular y*b4 has a unit coefficient in b5, so the image of N_5
vanishes in B/yB. After killing b1 and b5, the torsion module
T=N/yB in B/yB has a triangular presentation, up to unit coefficients,

    t^a b2 + c b3 + d b4,
    t^b b3 + z b4,
    t^a b4.

Its length is 2a+b=ord(D2+D3). The image of N_4 in T is *exactly* the
cyclic module R/(t^a): no combination of the first two displayed relations
can give an additional relation on b4 alone, because their nonzero leading
coefficients force their coefficients to be zero over the DVR domain.

The square T^2 is generated by the image of x^2. Indeed, B/yB is generated
by x, so T is the ideal (x) and its square is (x^2). Write
x=u*b2 modulo N_3. Multiplication E2^2 -> E4 has coefficient of valuation
b, hence

    x^2 = unit*u^2*t^b*b4 modulo N_5.

If a>0, u is a unit. Otherwise neither x nor y^2 would generate b2 modulo
t, and all other words in x,y have BF degree at least three; that would
contradict generation of B by x,y. If a=0, the image of N_4 in T is already
zero, so the value of u is immaterial. Consequently

    length(T^2)=max(a-b,0).

On the other hand T/T^2 is the torsion part of N/N^2. In adapted ambient
normal coordinates the first-normal relations are (t^A*x), where A is the
Fitting exponent. Thus length(T/T^2)=A. The calculation gives

    A = 2a+b-max(a-b,0) = a+b+min(a,b).

Globalizing the coordinate-independent Fitting ideal proves the divisor
identity

    A = D3 + (D2 wedge (D3-D2)).                         (MF6)

Here wedge is the coefficientwise minimum. Equivalently,

    (D2+D3)-A = (2D2-D3)_+.

In particular D3 <= A <= D2+D3. Neither A=D3 nor A=D2+D3 is universal.
There is no claim that the pole divisor P itself equals (2D2-D3)_+;
only its degree is determined by this identity and the quartic degree.

## 3. Matching the seven types with the pole strata

Let tau=deg(D2 wedge (D3-D2)). Necessarily

    0 <= tau <= min(d2,d3-d2),
    c=deg A=d3+tau,
    p=9-e-d3-tau.

Using d2+d3=9 when e=0 and d2+d3=4 when e=1 gives

    p=d2-tau                  (e=0),
    p=4+d2-tau                (e=1).

The resulting *necessary* nonregular incidences are:

| e | (d2,d3) | possible tau in nonregular branch | pole length p |
|---|---|---|---|
| 0 | (1,8) | 0 | 1 |
| 0 | (2,7) | 0,1 | 2,1 |
| 0 | (3,6) | 0,1,2 | 3,2,1 |
| 0 | (4,5) | 0,1 | 4,3 |
| 1 | (0,4) | 0 | 4 |
| 1 | (1,3) | 0,1 | 5,4 |
| 1 | (2,2) | 0 | 6 |

Thus the fifteen coarse nonregular strata reduce to seven:

    e=0, p=1,2,3,4;  e=1, p=4,5,6.

These seven strata still represent twelve numerical-type incidences; this is
a reduction, not realization or exclusion of the degree pair. In the regular
branch e=1 is impossible. For e=0, types (1,8),(2,7),(3,6) are numerically
compatible only when D2<=D3-D2, or equivalently 2D2<=D3 scheme-theoretically.
The e=0 type (4,5) cannot be regular, because tau would have to be four
although deg(D3-D2)=one.

The coefficientwise minimum must be retained: replacing its degree by the
minimum of the two total degrees is false when the defect divisors have
different supports. In particular the numerical types alone cannot justify
collapsing the seven coarse strata further.

## 4. Exact local laboratory and failed shortcuts

`research/scratch/mixed46/local_lattice.py` realizes B=R[x,y] as an
R-sublattice in K[y]/(y^6), with x a Laurent-coefficient polynomial starting
in degree two. It computes the BF lattice by DVR Gaussian operations, the
first-normal Fitting exponent as length(N_2/N^2), and the Gorenstein condition
as the socle dimension of the exact special-fiber multiplication matrices.
All row operations have coefficients in R. The examples are local and say
nothing about embedding them globally on C0.

Two simple exact models disprove A=Dtop universally:

    I=(t^r*x-y^2, x^3): D2=D3=r, D4=D5=2r, A=r.

Likewise

    I=(t^r*x-y^3, x^2): D2=0, D3=D4=D5=r, A=r.

The latter agrees with A=Dtop; the former does not. Their first-normal map
can be represented by two order-one generators by replacing the second
generator by its sum with the first, so the examples genuinely test the
coordinate-independent divisor comparison relevant to order-(1,1) pairs.

A second candidate shortcut, A=D3, is false. The lattice with

    x=t^-1*y^2+t^-3*y^3+2t^-5*y^4+4t^-7*y^5

has defects (D2,D3,D4,D5)=(1,2,3,3), first-normal exponent A=3, and
Gorenstein special fiber. An independently derived exact CI presentation is

    Q=x^2-t*x*y+y^3,
    P=t^3*x-t^2*y^2-2t*x*y+y^3.

Both equations vanish under that parametrization modulo y^6. At t=0 the
ideal is (x^2,y^3), of length six. This example confirms the overlap term
in (MF6).

The initial finite coefficient scan tested 256 Laurent polynomial choices,
200 of which were Gorenstein. They only gave D2=0 or D2=D3, and all happened
to satisfy A=D3. That scan was insufficient: tuned higher coefficients
produce the displayed counterexample. It is preserved here precisely because
it shows why first-normal or untuned finite scans cannot replace higher-jet
control.

## 5. Highest-value continuation

The next global test should couple (MF6) to the actual first-normal incidence
space and the quadric residual intersection, while retaining the full divisors
D2,D3 and the pole principal parts. The smallest e=0 stratum p=1 forces
tau=d2-1; the e=1,p=4 branch comprises (0,4) and (1,3) with tau=1.
These are sharply constrained divisor profiles and are appropriate finite
laboratories for higher transverse jets. A global regular-ratio normalization
is not available for these pole strata.


---

## 2026-10-05-mixed46-regular

# Regular-ratio degree-(4,6) pairs: a pure horizontal direction is impossible

Date: 2026-10-05. Scope: characteristic zero, the monomial rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\). This note is independent of the main ledgers.
It addresses the **regular-ratio branch only**: after subtracting an ambient
quadratic multiple of the quartic, the sextic has normal order at least two.
The quotient regularity cannot be inferred for a general pair.

## Result and exact hypotheses

**PROVED here and independently audited.** Suppose forms \(F_4,G_6\)
cut out \(C_0\) set-theoretically in characteristic zero, the first normal
quotient is regular, and the common primitive horizontal direction has degree
\(e=0\). In the balanced affine conormal frame

\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]

the first normal form of \(F\) cannot be a multiple of \(V\), and cannot
be a multiple of \(U\). Thus both coefficients of its constant horizontal
factor must be nonzero. This excludes the entire two-point boundary of the
constant-direction parameter line, including all its quartic parameters;
it is not just a generic-rank computation.

The proof uses the global residual divisor on the unique quadric, and only the
cubic and quartic transverse jets after that restriction. No claim is made
about the mixed direction or \(e=1\), or about the nonregular branch.

## Dependencies rechecked

Set

\[
 q=x_0x_3-x_1x_2,\quad A=x_0^2x_2-x_1^3,
 \quad B=x_0x_2^2-x_1^2x_3,\quad D=x_2^3-x_1x_3^2.
\]

The script derives the degree-four ideal space from these generators and
checks its dimension 18 and normal-image rank 17. Its first-normal kernel is
\(kq^2\). It also verifies that the 18 forms \(qI_C(4)\) together with
\(A^2,AB,B^2,BD,D^2\) have rank 23. The fact that these span the full
symbolic-square sextic space is P-017/P-022; the existing `verify_degree6.py`
independently proves saturation and the dimension. The present script checks
all linear-algebra identities actually used below.

P-021 permits subtracting a quadratic multiple of \(F\) in the regular
branch. Thus take \(G\in I_C^{(2)}(6)\). A genuine pair has neither carrier
\(q\)-divisible: otherwise its intersection with the other equation has an
extra residual curve on the quadric. Generic transverse length is six, since
\(\deg(F)\deg(G)=24=6\deg C_0\). Formal elimination of the generically
smooth quartic therefore makes every transverse coefficient through order
five vanish. In particular the quadratic normal form of \(G\) is divisible
by the linear normal form of \(F\).

## Complete pure-direction quartic space

Define

\[
\begin{aligned}
 P_6&=x_0x_1x_3^2+x_0x_2^3-2x_1^2x_2x_3,\\
 P_7&=2x_0x_2^2x_3-x_1^2x_3^2-x_1x_2^3,\\
 P_9&=2x_0x_3^3-3x_1x_2x_3^2+x_2^4.
\end{aligned}
\]

Exact linear algebra proves that every quartic with first normal form
\(h(z)V\) has the unique expression

\[
 F=A(c_0x_0+c_1x_1+c_3x_2+c_4x_3)
       +c_6P_6+c_7P_7+c_9P_9+\kappa q^2.
\]

In the affine normal coordinates,

\[
 h=c_0+c_1z+c_3z^3+c_4z^4+c_6z^6+c_7z^7+c_9z^9,
\]

and the \(U^2\) coefficient of \(F\) is

\[
 R=\kappa+c_6z-c_7z^2+3c_9z^4.
\]

Thus \(F=hV+RU^2+\text{other terms of normal order at least two}\).
The term “other” here includes terms involving \(V\); after the formal
solution \(V=-(R/h)U^2+\cdots\), these do not affect that quadratic
coefficient.

## The quadric forces the sextic residual

Use Segre coordinates

\[
 (x_0,x_1,x_2,x_3)=(a_0b_0,a_0b_1,a_1b_0,a_1b_1),
 \qquad c=a_1b_0^3-a_0b_1^3.
\]

On \(Q\), \(A=a_0^2c\), \(B=a_0a_1c\), \(D=a_1^2c\).
Write \(F|_Q=c\rho\), \(G|_Q=c^2\sigma\), where \(\rho\) has
bidegree \((3,1)\), and \(\sigma\) is a nonzero binary quartic in
\((a_0,a_1)\).

Because the coefficient of \(U^2\) in a general \(qI_C(4)\) sextic has
\(z\)-degree at most nine, while the coefficient of \(U^2\) in \(D^2\)
has leading term \(4z^{10}\), divisibility of \(G_2\) by \(V\) forces
the \(D^2\) coefficient to be zero. Therefore \(a_0\mid\sigma\).
The exact residual identity on the ruling \(a_0=0\) is

\[
 \rho(0,a_1;b_0,b_1)=c_9a_1^3b_0.
\]

If \(c_9=0\), both \(\rho\) and \(\sigma\) contain the ruling
\(a_0=0\). That line is then contained in \(V(F,G)\), and is not \(C_0\).
This excludes the full \(c_9=0\) boundary.

Suppose henceforth \(c_9\ne0\). At
\(P=C_0\cap\{a_0=0\}=\{a_0=b_0=0\}\), the affine chart
\(a_1=b_1=x_3=1\) has
\(x_0=a_0b_0,x_1=a_0,x_2=b_0\). The ambient derivative
\(\partial F/\partial x_0\) at \(P\) is \(2c_9\), so \(F\) is smooth
there. Moreover \(\rho=c_9b_0+O((a_0,b_0)^2)+O(a_0)\), and
\(c=b_0^3-a_0\), so \(C_0\) and \(\rho\) intersect with multiplicity
one on \(Q\). Both \(F\) and \(Q\) project formally isomorphically
to the \((x_1,x_2)=(a_0,b_0)\) plane at this point, because their
\(x_0\) derivatives are nonzero. The same two curve germs consequently
have intersection multiplicity one on the smooth surface \(F\). In
particular \(a_0\) is a parameter on the smooth germ \(\rho\).

On the smooth surface \(F\), let \(v\) be a local equation of \(C_0\).
Generic transverse order at least six implies \(v^6\mid G\) in the local
ring at \(P\): the coefficients of smaller powers vanish identically along
the integral curve. Restrict to the smooth germ \(\rho\). Since
\(i_P(C_0,\rho)=1\), \(G|_\rho\) has order at least six. The identity
\(G|_Q=c^2\sigma\) then forces \(\sigma|_\rho\) to have order at least
four. But \(a_0\) is a parameter on \(\rho\), and \(\sigma\) is a
binary quartic. Consequently

\[
 \sigma=\gamma a_0^4,\qquad\gamma\ne0.
\]

Equivalently,

\[
 G=\gamma A^2+qF',\qquad F'\in I_C(4).
\]

Divisibility of \(G_2\) by \(V\) forces \(F'\) to have pure first normal
form \(h'V\), so \(F'\) belongs to the same eight-dimensional quartic
space. Here no cancellation of a torsion class, no smooth-normalization
assumption, and no sextic normalization argument is involved.

## A universal cubic-jet rigidity identity

Let \(R'\) be the \(U^2\) coefficient associated to \(F'\). Eliminating
\(F\) gives

\[
 V=-\frac RhU^2+O(U^3),
\]

and the cubic coefficient of \(G\) is

\[
 R'-\frac{h'}hR.
\]

It must vanish. Thus \(hR'-h'R=0\).
Subtract a scalar multiple of \(F\) from \(F'\) so that \(c'_9=0\).
This does not affect \(hR'-h'R\). Its \(z^{11}\) coefficient is then
\(-4c_9c'_7\), so \(c'_7=0\). Its \(z^{10}\) coefficient becomes
\(-2c_9c'_6\), so \(c'_6=0\). Its \(z^9\) coefficient then becomes
\(c_9\kappa'\), so \(\kappa'=0\). Hence \(R'=0\), and since
\(R\ne0\), the polynomial identity gives \(h'=0\). All eight quartic
coefficients are zero. Thus the original \(F'\) was a scalar multiple of
\(F\).

Modulo \(F\), therefore, \(G=\gamma A^2=\gamma V^2\). Because
\(R\) has leading coefficient \(3c_9\ne0\), \(V\) has transverse order
exactly two on \(F\) at the generic point of \(C_0\). Consequently
\(G\) has order exactly four, contrary to the required six. This excludes
\(c_9\ne0\), and completes the pure-\(V\) proof.

The coordinate reversal \((x_0,x_1,x_2,x_3)\mapsto(x_3,x_2,x_1,x_0)\)
preserves \(C_0\), and exchanges the two pure constant directions up to
nonzero scale in the balanced frames (its coefficient action is already
verified in P-025). Hence the pure-\(U\) case is excluded too.

## Computation, epistemic boundary, and next investigation

Run

```
/private/tmp/stci-cas-venv/bin/python research/computations/verify_mixed46_regular.py
```

with SymPy 1.14.0. The script derives the full pure quartic space, checks the
residual identity and smoothness derivative, detects the sextic \(D^2\)
coefficient, checks the three successive polynomial coefficients proving
rigidity, and independently checks the formal cubic coefficient. It does not
substitute finite sampling for the exhaustive polynomial argument.

The remaining degree-zero directions have both coefficients nonzero. The
torus \(z\mapsto\lambda z\) acts on \(U,V\) with weights four and three,
so all these directions form one orbit; normalize the direction to \(U+V\).
This substantially reduces the degree-zero regular frontier, but does not
settle it. The most valuable immediate continuation is the corresponding
mixed-direction residual restriction plus cubic-contact rigidity, preserving
all quartic parameters and exceptional cases. The \(e=1\) regular branch
remains separate.


---

## 2026-10-05-uniform-multiplicity

# Uniform quasiprimitive restrictions with a quartic carrier

Status: proved numerical consequences of checked quasiprimitive Gorenstein
duality; exact exploratory calculation for the primitive `(4,7)` branch.
Work in characteristic zero with a smooth rational quartic
`C ⊂ P³`; the formal computations below use
`C0=[s⁴:s³t:st³:t⁴]`. These restrictions do not address pairs whose
two carriers have degree at least six and are thick along the whole curve.

## Checked duality input

The full, unbounded multiplicity statement is justified by Nicolae Manolache,
[Duality for Gorenstein multiple structures on smooth algebraic varieties,
Rev. Roumaine Math. Pures Appl. 68 (2023), 141–148](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf),
theorem on p.143, embedded specialization and Remarks 1–2 on pp.144–145.
The preprint is [arXiv:0706.2204](https://arxiv.org/pdf/0706.2204).
For curves the free-type condition is automatic. Quasiprimitivity makes the
three canonical filtrations coincide. The original Boratyński article was
not independently fetched in this investigation.

An independent local check removes any reliance on a finite-multiplicity
classification. Complete at a support point, put `A=k[[t]]`, and let `B` be
the local finite flat Gorenstein algebra. Quasiprimitivity gives
`B⊗K ≅ K[z]/(z^n)`, `K=Frac(A)`. Its saturated BF ideals are
`B_i=B∩z^i B_K`. They satisfy `ann(B_i)=B_{n-i}`: this holds generically,
and torsionfreeness detects equality inside `B`. A perfect Gorenstein
multiplication functional `B→A` has orthogonal complement of each ideal
equal to its annihilator. Passing to successive quotients gives perfect
pairings

`E_i ⊗ E_{n-1-i} ≅ E_{n-1}`.

Writing `L=E_1`, the iterated multiplication `L^i→E_i` has a canonical
effective zero divisor `D_i`, so `E_i=L^i(D_i)`, with `D_0=D_1=0`.
Associativity and perfect complementary multiplication give actual divisor
identities and inequalities

`D_i+D_j ≤ D_{i+j}`, and `D_i+D_{n-1-i}=D_{n-1}`.

The top piece is the annihilator of the support ideal. CM duality therefore
gives `E_{n-1}=ω_C⊗(ω_X|C)^(-1)`. None of these statements assumes the
multiple curve is primitive everywhere.

## Proved uniform bounds for `(4,b)`

Suppose `X=V(F_4,G_b)` is supported on `C`, with `b≥4`. The quartic has
normal order one generically by project result P-011. The generic transverse
CI is therefore curvilinear of length `b`, so `X` is quasiprimitive.
Adjunction and `O_C(1)=O_P1(4)` give

`deg E_{b-1}=-4b-2`.

The quotient `O(-7)^2→L` has `deg L=e-7`, where `e≥0` is the degree of
its basepoint-free pair of binary forms. Hence, putting `s=b-1`,

`deg D_s = (3-e)s-6 = (3-e)b+e-9`.

Effectivity implies **`e≤2` for every `b≥4`**, with `e≤1` when `b≤6`.
Thus arbitrarily large mate degree does not produce arbitrarily complicated
horizontal normal directions. The exact top-defect degrees are

| e | deg L | deg D_(b-1) |
|---|---|---|
| 0 | -7 | 3b-9 |
| 1 | -6 | 2b-8 |
| 2 | -5 | b-7 |

More strongly the **first defect degrees remain uniformly bounded**:

| e | permitted deg D_2 | upper bound for deg D_3 |
|---|---|---|
| 0 | 1 through 5 | 8 |
| 1 | 0 through 3 | 5 |
| 2 | 0 or 1 | 2 |

To prove the second column, put `s=2q+r`, `r∈{0,1}`. Superadditivity
gives `q deg D_2≤(3-e)s-6`, which is strictly less than
`q·2(3-e)` for `e=0,1,2`. Thus `deg D_2≤2(3-e)-1`.
For `e=0`, `D_2=0` would give the prohibited primitive triple of
conormal type `O(-7)` from P-010, giving the positive lower bound.
For the third column write `s=3q+r`. If `e=1,2`, the remainder
`(3-e)r-6` is negative, giving `deg D_3≤3(3-e)-1`.
For `e=0,r=2`, use the stronger inequality
`q deg D_3+deg D_2≤deg D_s`; the positive lower bound for `deg D_2`
again yields `deg D_3≤8`.

This is a useful uniform reduction, not an upper bound on `b`. In particular,
it suggests classifying admissible embedded triples and quadruples with
these few defect degrees before repeating higher-multiplicity numerics.
For `e=2,b=7` the top defect is zero and the whole structure is primitive;
for `e=2,b=8` one has `D_2=D_3=0`, so the canonical quadruple is primitive.
An obstruction to primitive quadruples of type `O(-5)` would thus close both
these branches and potentially larger cases with small early defects.

## A tempting false first-normal identity

The identity `A=D_top`, where `A` is the common vertical Fitting divisor
of the defining differentials, is false in arbitrary multiplicity. Over
`A=k[[t]]`, take the finite flat CI

`B=A[[x,y]]/(tx-y^r,x^s)`, with `r,s≥2`.

It has rank `n=rs`, generic curvilinear algebra, and radical `(x,y)`.
The first-normal image is `t·x`, so `A=[t=0]`. The basis
`x^i y^j`, `0≤i<s, 0≤j<r`, identifies

`D_k=floor(k/r)[t=0]`.

In particular `D_top=(s-1)[t=0]`. Complementary divisor duality is satisfied,
but the differential divisor only equals the top defect when `s=2`.
The example is a local finite flat model, not a global projective candidate.

## Exact primitive-fourth calculation, exploratory status

The script
`research/scratch/primitive47/obstruction.py` computes the obstruction to
extending the unique primitive triple of type `L=O(-5)` to a primitive
quadruple on `C0`. Input is a coprime pair of binary quadratics `A,B`,
describing the quotient `u↦A,v↦B` in the repository's split normal frame.
Set `m=Bu-Av` and choose polynomial Bezout coefficients to get a quotient
coordinate `ell`. The kernel line is `M=O(-9)`.

Since `Hom(M,L²)=O(-1)`, the primitive triple extension has no obstruction
and no free extension parameter. Its quadratic gluing correction is the
unique Laurent splitting of the moving-coordinate cocycle. The next
obstruction lies in `H¹(Hom(M,L³))=H¹(O(-6))` and has five Laurent
coordinates. All coefficient functions on the second chart are evaluated
at the exact moving coordinate `W=(z³+a)/(z⁴+b)` before truncation.

For example the quotient `A=z²,B=1` has fourth obstruction coordinates

`(-35,-3,15,-3/4,-35/16)`.

This nonzero vector excludes primitive quadruples, and hence primitive
seventuples, **for that particular quotient direction**. Several additional
sample pairs also give nonzero vectors. The calculation has not yet
classified all coprime quadratic pairs and is not a no-`(4,7)` theorem.
