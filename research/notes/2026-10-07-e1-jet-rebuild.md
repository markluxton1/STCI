# e=1 jet lane rebuild — 2026-10-07

Base: current remote main at `7662a2ebb1dd561c1fb5e3c8958799b37d962c41`.

Purpose: reconstruct the e=1 primitive-triple quartic-carrier calculation on a clean branch. The older branch `research/jet-discrepancy-order-one-2026-10-06` is retained only for provenance.

## Imported theorem-level input

Bănică–Forster gives the standard double-to-triple splitting obstruction in
[
H^1(O_C(-4)).
]
The project-specific exact obstruction coordinates are independently persisted in
`research/computations/verify_e1_triple_obstruction.py`.

Their resultant-open zero locus is:
- main component (b_0=-2a_1, a_0b_1=-8a_1^2);
- boundary (a_0=b_1=0), with (r=b_0/a_1) satisfying
  ((r+2)(3r^2+4r+12)=0).

## Rebuild target

On the main component normalize
[
A=1+tz,qquad B=-2t-8t^2z,qquad t
e0.
]
The new self-contained certificate `verify_e1_jet_rebuild.py` reconstructs:
1. (I_C(4)) from all 35 ambient quartic monomials;
2. the first-symbol condition defining (I_{C_2}(4));
3. the BF quadratic chart correction;
4. the second-contact matrix for (C_3);
5. its kernel as actual ambient quartics (F_0,F_1);
6. the gcd of (F_0,F_1) over (mathbf Q(t)).

## Status discipline

The script contains exact symbolic assertions for the previously obtained dimensions/rank, but this branch has not yet recorded a runtime transcript from an independent Python execution. Therefore:
- the BF obstruction locus is **ported exact certificate / previously audited**;
- the rebuilt quartic assertions are **PENDING RUNTIME VERIFICATION**;
- no new gcd or residual-base-locus conclusion is promoted yet.

After runtime verification, compute/saturate the ideal ((F_0,F_1)) against (I_C), preferably in Macaulay2, and record the residual scheme uniformly over the parameter (t). Only then interpret the geometry and literature-check linkage/contact antecedents.


## Runtime verification and main-component carrier exclusion

Independent execution of \`verify_e1_jet_rebuild.py\` reproduced:
\[
h^0(I_C(4))=18,\qquad h^0(I_{C_2}(4))=7,
\]
the second-contact rank
\[
\operatorname{rank}=5,
\]
and therefore
\[
h^0(I_{C_3}(4))=2.
\]
The two extracted ambient quartics \(F_0,F_1\) satisfy
\[
\gcd(F_0,F_1)=1\quad\text{over }\mathbf Q(t),
\]
so the pencil has no fixed surface factor.

A further exact calculation restricts the two quartics to the unique quadric
\[
Q=xW-yZ.
\]
On the affine chart \(x=1\), where \(Q\) gives \(W=yZ\), one obtains (up to nonzero scalars)
\[
F_0|_Q=
Z(-Z+y^3)(8t^3Z-1)(2ty+1),
\]
\[
F_1|_Q=
(-Z+y^3)(8t^3Z-1)(64t^6Z^2+1)(2ty+1).
\]
Hence
\[
\gcd(F_0|_Q,F_1|_Q)
\sim
(-Z+y^3)(8t^3Z-1)(2ty+1).
\]
The first factor is the quartic \(C\). The other two factors close to ruling lines
\[
L_1(t):\quad 2ty+x=0,\qquad 2tW+Z=0,
\]
\[
L_2(t):\quad 8t^3Z-x=0,\qquad 8t^3W-y=0.
\]
Direct symbolic substitution of the two line parametrizations into both generic
quartics gives zero identically. Thus
\[
\boxed{L_1(t)\cup L_2(t)\subset V(F)\quad
\text{for every }F\in H^0(I_{C_3}(4)).}
\]

Since \(t\ne0\), neither line is \(C\). Any positive-degree projective hypersurface
\(G\) meets each line (or contains it). Therefore
\[
V(F,G)
\]
has support outside \(C\) for every quartic carrier \(F\) through this primitive
triple.

**PROVED (exact symbolic certificate + direct substitution).**
The entire one-dimensional nonzero-comparison main component of the e=1
primitive-triple locus cannot occur in an STCI presentation having a quartic
carrier.

This mechanism differs from e=2: the ambient quartic pencil has no common
surface factor; instead it has a forced pair of ruling lines in its base locus.

The two isolated nonzero-comparison boundary directions remain to be checked
separately. The comparison-zero boundary direction was previously identified
as the quadric-contained case and should also be re-certified on this clean branch.


## Isolated e=1 boundary directions

### Nonzero-comparison conjugate pair

Set
\[
A=z,\qquad B=r,\qquad 3r^2+4r+12=0.
\]
The calculation was carried out over the exact quadratic field
\[
K=\mathbf Q[r]/(3r^2+4r+12),
\]
so both conjugate directions are handled simultaneously without numerical
specialization or radicals.

The reconstructed quartic-through-double source has dimension seven, the
second-contact map has rank five, and hence
\[
h^0(I_{C_3}(4))=2.
\]
The two ambient quartics have gcd one in \(K[x,y,Z,W]\): there is no fixed
surface factor.

Restricting the two quartics to the unique quadric \(Q=xW-yZ\), and using
\(W=yZ\) on \(x=1\), their common factor is
\[
(-Z+y^3)\,y\,Z.
\]
The factor \((-Z+y^3)\) is \(C\). The remaining factors close to the two
coordinate ruling lines
\[
L_y:\ y=W=0,\qquad
L_Z:\ Z=W=0.
\]
Direct substitution verifies that both quartics vanish identically on both
lines. Therefore
\[
L_y\cup L_Z\subset \operatorname{Bs}|I_{C_3}(4)|.
\]

**PROVED (exact quadratic-field calculation).** Both isolated
nonzero-comparison e=1 primitive-triple directions are excluded as quartic
STCI carriers: any positive-degree mate meets either fixed projective line
(or contains it), creating support outside \(C\).

### Comparison-zero point

At the remaining boundary direction
\[
A=z,\qquad B=-2,
\]
the comparison section \(A+zB/2\) vanishes identically. The quadric has chart
equation
\[
Q=u+\frac z2v.
\]
Under the primitive direction
\[
u=z\epsilon,\qquad v=-2\epsilon,
\]
this vanishes identically. The BF quadratic cocycle also vanishes, so the
canonical primitive triple lies on \(Q\):
\[
C_3\subset Q.
\]
The quartic source has dimension ten, while
\[
Q\cdot H^0(O_{\mathbf P^3}(2))
\]
also has dimension ten and is contained in \(H^0(I_{C_3}(4))\). Hence
\[
\boxed{H^0(I_{C_3}(4))=Q\cdot H^0(O_{\mathbf P^3}(2)).}
\]

**PROVED / RECERTIFIED.** This direction is excluded because every quartic
carrier has the fixed quadric factor.

## e=1 primitive conclusion — corrected status

The carrier geometry is completely classified at the triple stage:
- main one-dimensional component: a two-dimensional quartic pencil with two
  parameter-dependent fixed ruling lines and no fixed surface factor;
- two conjugate isolated points: a two-dimensional quartic pencil with two
  coordinate ruling lines and no fixed surface factor;
- comparison-zero isolated point: every quartic has the fixed quadric factor.

Only the comparison-zero point is excluded immediately by the fixed-surface
argument. The fixed-line cases remain **OPEN as STCI exclusions**. To close
them one must analyze the mate divisor on the forced ruling lines (including
the intersection divisor with C), or produce a stronger residual curve/surface
obstruction.

## Consequence for multiplicity-six quasiprimitive e=1

The audited MF6 classification on current main leaves e=1 numerical defect
types
\[
(d_2,d_3)=(0,4),(1,3),(2,2).
\]

The newly closed primitive-triple carrier calculation immediately excludes
the entire \((0,4)\) type: when \(d_2=0\), the triple is primitive. Every
quartic containing a later sextuple also contains its primitive triple, and
every such triple has already been shown to force either fixed ruling lines
or a fixed quadric factor. Later defects cannot remove a base curve already
contained in every quartic at the triple stage.

Therefore the e=1 MF6 frontier reduces to
\[
\boxed{(d_2,d_3)=(1,3)\text{ or }(2,2).}
\]

For these two types the second graded piece is
\[
E_2=L^2(D_2)=O(-12+d_2),
\]
so they are genuinely quasiprimitive already at the triple stage and are not
covered by the primitive classification.

The BF obstruction class before adding \(D_2\) lies in \(H^1(O(-4))\).
A defect section \(\delta\in H^0(O(d_2))\) must annihilate it under
multiplication
\[
H^1(O(-4))\xrightarrow{\cdot\delta}H^1(O(-4+d_2)).
\]
Thus:
- \(d_2=1\): two obstruction coordinates remain (\(H^1(O(-3))\));
- \(d_2=2\): one obstruction coordinate remains (\(H^1(O(-2))\)).

By Serre duality this is an apolarity problem for the binary quadratic dual
to the primitive BF obstruction. This is the recommended next exact
classification: solve the annihilator incidence \((A,B,\delta)\) first,
then impose ambient quartic containment on those low-dimensional strata.
