# Corrected h2 source coordinates and one sextic conductor-support incidence

Date: 2026-10-14. Status: **EXACT COORDINATE CORRECTION AND INCIDENCE
CAPTURE; independently audited** in the
[new factor and source-binding audit](2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit.md).
Accepted parameter covers,
the actual octic conductor, and previously closed quintic lanes are premises.
This note makes no support-emptiness, full-descent, whole-quintic or universal
STCI claim. The earlier attempt04 is retained as a coefficient capture with
an incorrect common-coordinate binding; it is not an actual h2 support test.

## 1. The necessary coordinate correction

The accepted finite h2 cover uses

```
x=r/delta,       H(x)=x^2+v*x+w,
P(x)=(A*x+B)H(x),       J(x)=(C*x+D)H(x).
```

The target parameter is `y=(r-delta)/r`, so the actual octic variable in
the frozen primitive polynomial is

```
p=1-y=delta/r=1/x.
```

Consequently the actual source-coordinate binary octic is

```
G(S,T)=Fdet(S,T),       G(1,x)=x^8 Fdet(1/x,1).       (1)
```

The source point at infinity is the intrinsic A4 point: its linear form
is `S`, and its target coordinate is `p=0`. Source `x=0` is target
infinity `p=infinity`. These are different points and neither is omitted.

Attempt02 inserted the accepted coefficient map into `Fdet(1-x,1)`, while
attempt04 applied the Hamiltonian action for `H(x)=x^2+vx+w` to those
coefficients. Those use different coordinates on the same P1. The computed
matrices exist, but their rank locus does not express the intended support
condition. No emptiness or quintic-closure conclusion had been derived from
that capture. The [original attempt04](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
and its earlier failures remain preserved.

Let `B(t)=sum c_i t^i` be the saved polynomial from attempt02, after its
common denominator and nonzero `delta^4` content were removed. Then

```
G(1,x)=x^8 B(1-1/x)
      =sum_(i=0)^8 c_i (x-1)^i x^(8-i).              (2)
```

This is an invertible constant linear transformation on binary octics.
It preserves the nonzero form condition, the common coefficient content,
and all projective degree-drop strata. Explicitly, its coefficients are

```
g_j=(-1)^(8-j) sum_(i=8-j)^8 binomial(i,8-j)c_i.
```

The inverse is `B(t)=(1-t)^8 G(1,1/(1-t))`. The new
[attempt05 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt05.m2)
asserts both literal polynomial transformations, then asserts the quadratic
and A4-cubic Hamiltonian coefficient identities. Its
[captured execution](../validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate/execution-record.json)
has exit zero and empty stderr. It reuses all nine saved coefficients;
neither the accepted octic nor the rational inverse map is reconstructed.

## 2. Remove the forced differential factor before testing support

The new [conductor--differential factor proof](2026-10-14-generalization-quintic-h2-conductor-quotient.md)
shows, on the entire actual h2 locus,

```
G=H Q,                 degree Q=6.                  (3)
```

The proof uses the actual conductor annihilation of relative differentials
at finite smooth source points, and the accepted A4 value and complete
infinity cover for the sole singular source point. It is a lower bound on
conductor contact. It places no upper bound on later contact or conductor
multiplicity and gives no descent assertion.

For any nonzero H,Q and any nonzero permitted linear form P, one has

```
supp(HQ) subset supp(H P^epsilon)
 iff supp(Q) subset supp(H P^epsilon).               (4)
```

Thus the degree-eight support condition reduces to the degree-six quotient,
without losing a high-contact or repeated-root stratum. Put `j=Jbar`,
`P=S` and define `D_A=A_T partial_S-A_S partial_T`. The exact shared
support incidence is

```
D_(HP) Q = L Q,        L a homogeneous linear form,
j D_H Q = mu Q,        mu a scalar.                 (5)
```

If j is nonzero the second equation says precisely that Q is supported
on H; the first then follows. If j is zero, Q nonzero forces mu=0 and
the first equation permits exactly the additional intrinsic A4 point.
The equation uses homogeneous forms, so infinity, a repeated H, and every
fixed-degree leading drop remain present together.

There is also a direct product-action check. Since `D_H H=0` and
`D_(PH)H=-H D_H P`,

```
D_H(HQ)=H D_H Q,
D_(PH)(HQ)=H [D_(PH)Q-(D_H P)Q].                    (6)
```

The last correction is linear and is absorbed into the free L in (5).

## 3. Captured sextic coefficient system on the accepted inverse-map open

On the monic finite chart write `Q=sum_(i=0)^6 q_i x^i`, with
`q_i=0` outside `0<=i<=6`. The two Hamiltonian images in (5) have
coefficients

```
d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),  0<=i<=6,
e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1),  0<=i<=7.
```

Here `d` is the degree-preserving quadratic action and `e` is the
degree-seven cubic action, because `P=S` has affine dehomogenization one.
For `L=ell0*S+ell1*T`, (5) is the single fifteen-equation system

```
e_i=ell0 q_i+ell1 q_(i-1),       0<=i<=7,
j d_i=mu q_i,                  0<=i<=6.             (7)
```

For the nonzero-j part, all two-by-two minors of the stored seven-by-two
matrix `(q,d)` express the second line after removing its scalar unknown.
The characteristic polynomial of the action on Sym^6, with eigenvalue
`nu=mu/j`, is

```
nu*(nu^2-4 Delta)*(nu^2-16 Delta)*(nu^2-36 Delta),
Delta=v^2-4w.
```

Equivalently the shared scalar variable satisfies
`mu*(mu^2-4*j^2*Delta)*(mu^2-16*j^2*Delta)*(mu^2-36*j^2*Delta)=0`.

This is one representation equation, including its nilpotent repeated-root
boundary; the spectral identity is not an assertion that the actual family
has an eigenvector at any parameter.

The new [attempt06 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt06.m2)
divides the corrected G by the monic H, asserts the literal identity G=HQ,
and asserts both coefficient formulas and both product-action formulas.
Its [captured execution](../validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/execution-record.json)
has exit zero and empty stderr. It saves all seven q_i, the seven-by-two
quadratic matrix and all eight A4-cubic coefficients. This is exact
incidence data, not an emptiness certificate.

The rational coefficient map is valid only off

```
(v^2-4w)*(v^2+2w+6vw+6w^2)=0.
```

Its stored denominator and delta^4 content retain those restrictions.
The written factor proof and homogeneous system (5) do not use that inverse.

## 4. One polynomial system retains every h2 chart

To avoid every inverse denominator, take all forms in the source homogeneous
coordinates `(S,T)` and use the literal accepted octic coefficient map. Use
quadratic H, independent linear cofactors A,C, sextic Q, linear L and scalar
mu as auxiliary variables. Impose coefficientwise

```
Psource=H A,        Jsource=H C,
Gactual=H Q,
D_(SH)Q=L Q,       j D_HQ=mu Q.                     (8)
```

Require `delta!=0`, H and Q nonzero, and the determinant of A,C nonzero.
The last condition makes the homogeneous gcd exactly two. Add the original
center-avoidance and finite-birational hypotheses when interpreting this as
an actual normalization projection. No quadratic leading coefficient, H
discriminant, center pivot, or cofactor coefficient is inverted in (8).
The accepted h2 cover proves that finite monic, repeated finite and
infinity-once loci are all represented; its exceptional K locus is already
inconsistent and double infinity is already impossible.

The support part of (8) is necessary and sufficient for the actual
restricted conductor to have only the permitted roots, under the actual
h2 geometric hypotheses. It is not sufficient for full inverse support or
for power descent through the full conductor algebra. The precise remaining
task is to prove this finite incidence incompatible with the original
projection and fiber equations, or describe its surviving geometric family
and test the complete conductor logarithm. No partition of the six or eight
contact multiplicities is required to state or investigate it.

## 5. Scalar-free shared matrices and the intrinsic contact bound

The scalar unknowns in (5) may be removed without choosing a root or a
coefficient of Q. In coefficient spaces the same incidence is

```
rank[Q | j D_HQ] <= 1,               a 7-by-2 matrix,
rank[S Q | T Q | D_(SH)Q] <= 2,      an 8-by-3 matrix.       (9)
```

The first column Q is nonzero. Multiplication by S and T gives two
linearly independent columns for nonzero Q, so the second rank condition
is exactly membership in their span; it does not add a hidden leading
coefficient assumption. At j=0 the first rank condition is automatic.
Thus all two-by-two minors of the first matrix and all three-by-three
minors of the second form one homogeneous coefficient ideal.

The separately audited
[intrinsic A4 contact bound](2026-10-14-generalization-quintic-intrinsic-a4-contact-bound.md)
proves that after accepted G=j=0 mate closure, every j=0 full-support
candidate has actual A4 conductor contact one or two. Therefore every
surviving h2 mate candidate, including j=0, satisfies `Res(H,Q)=0`.
On the captured finite inverse-map chart this is the single necessary
condition `N12*N18=0` from the
[bounded norm calculation](2026-10-14-generalization-quintic-h2-conductor-quotient.md).
Neither factor is separately declared impossible.

This contact bound also gives one coefficient-open condition useful for
the shared matrix ideal. H has no A4 root in a surviving lane, since its
infinity leading equations would give accepted-closed G=j=0. For j
nonzero, the accepted A4 target-fiber criterion makes F(A4) nonzero, so
q6 is nonzero. For j=0, source-infinity contact one or two makes Q have
affine degree five or four. Consequently

```
(q4,q5,q6) != (0,0,0)                                    (10)
```

on every surviving finite-chart candidate. Condition (10) is a single
ideal-open locus. Saturating by a product q4*q5*q6 would be wrong: it
would remove the entire j=0 locus. A future exact shared ideal certificate
may use saturation by the ideal `(q4,q5,q6)`, together with the stipulated
delta, inverse-map determinant and exact-h2 cofactor determinant units.
The j factor in the first matrix's minors must be retained.
