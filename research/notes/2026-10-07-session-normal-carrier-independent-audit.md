# Independent audit of the reduced exceptional normal-quartic exclusion

Date: 2026-10-07. Status: **ACCEPTED PROOF AUDIT under the recorded inputs**.
This audit accepts the new conclusion in
`2026-10-06-session-normal-carrier-progress.md`: a normal quartic carrier
for the fixed C0 in characteristic zero that admits any mate must have
a reducible nonreduced exceptional anticanonical divisor. It does not
exclude those nonreduced configurations, nonnormal carriers, or C0 as STCI.

Later on the same date the nonreduced lane was also independently audited
and excluded. Its separate tree enumeration and Type-D ideal proof are in
`2026-10-07-session-normal-nonreduced-independent-audit.md`. The present
note is retained as the proof of the reduced/irreducible stage.

The independent numerical implementation is
`computations/verify_session_normal_independent_audit.py`, with output
`scratch/session_normal_independent_audit.json`. It does not import the
first normal-carrier companion. It independently constructs every ADE
root matrix, verifies the allowed correction columns and full column
denominators, enumerates the budgeted multisets, and scans every reduced
cycle with a marked passage vertex. It reproduced exactly the five rows
in the proposed note.

## 1. Source and inherited hypotheses

The audit refreshed [Ishii--Nakayama's primary preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf). It explicitly
uses the minimal resolution and an effective exceptional anticanonical
divisor; its classification includes the rational B1/B2/B3/D cases used
in the note. Proposition 1.1 supplies connectedness when the resolution
is rational. These source inputs, the existing exclusions of rational
and positive-genus ruled carriers, the checked C0 normal bundle, Jaffe's
smooth curve--ADE table, and the rational-resolution denominator
compression theorem remain explicit dependencies. This audit does not
claim to reprove the source classifications.

The geometric arguments below are new direct checks. The exact numerical
scan checks consequences of those arguments and the stated source table,
rather than using numerical agreement to certify the geometric inputs.

## 2. Smooth passage through an exceptional fibre

The passage lemma is valid even on a smooth resolution that has singular
exceptional prime curves or intersections that are not simple normal
crossings. The rational lift of a smooth curve C to the resolution
extends over each missing point by properness and the DVR valuative
criterion. It is a section of the base change over C, so its image c is
isomorphic to C as a closed subscheme.

At its unique point over a surface singularity p, every f in m_(S,p)
pulls back to a function vanishing on every exceptional prime over p.
The regular local ring of the resolution is factorial. The product of
the distinct local prime equations therefore divides the pullback.
After restriction to c, its order is at least the sum of the local
intersection lengths with these primes. The quotient map O_(S,p)->O_(C,p)
is onto and supplies an f restricting to a uniformizer. Thus the sum is
at most one. It is positive because the lift lies in the exceptional
fibre, and consequently equals one.

Each nonzero intersection length is integral and positive. The sole
prime met is smooth at that point, because a singular plane-curve germ
on a smooth surface has multiplicity at least two and cannot have
intersection length one with a smooth curve. The passage is transverse
and avoids every other exceptional prime. Hence the passage vector
really is a standard basis vector, rather than an arbitrary nonnegative
vector. No transversality hypothesis was inserted into the numerical
enumeration.

For the minimal rational resolution, the coefficient-zero exceptional
primes have arithmetic genus zero, square -2, and are disjoint from the
support of E. This follows from adjunction and relative nefness of K.
Connectedness of E and of each exceptional fibre therefore identify one
nonrational fibre with the full support of E; the other fibres are ADE.
The prior avoidance exclusion forces C through the nonrational fibre.

## 3. Passage arithmetic and irreducible support

Let A be minus the full exceptional intersection matrix, a its
anticanonical coefficient vector, and m the smooth passage vector.
Set z=A^(-1)m, t=a^T*m, q=m^T*A^(-1)*m, d=a^T*A*a.
Adjunction gives c^2=t-2. The mate relation gives c+Z numerically H
with square four and exceptional orthogonality, so t+q=6.
Cauchy--Schwarz in the positive definite A form gives

    t^2 <= d*(6-t).

The integer candidates are t<=2 for d=1,2 and t<=3 for d=3.
The equality cases (d,t)=(1,2),(3,3) force z=2a,a respectively.
Their denominator is one; the already checked global compression theorem
would give a plane mate, impossible for C0. Thus the retained t ranges
are exactly the ones stated in the proposed note.

If E=aP has irreducible support, d=a^2*(-P^2)<=3 forces a=1.
Adjunction gives arithmetic genus one for P. The passage lemma gives
t=1, even when P is a singular rational prime curve. Its correction is
P/d, contributing 1/d. The required ADE correction is 5-1/d and its
available rank is at most 8+d.

The new order-two lower bound at the nonrational hypersurface point is
valid in characteristic zero. Straighten C to the t axis. Common
first-normal order one would give a quadratic term t*(a*x+b*y)+Q(x,y)
with (a,b) nonzero; this quadratic form has rank at least two. Formal
splitting gives a node, or uv+h(w). Isolation forces h nonzero; a
one-variable change makes it a power, giving a rational A_n point.
This contradicts nonrationality. Therefore at most seven normal zeros
remain for ADE points.

Every allowed ADE pair satisfies q_i<=n_i*s_i/(n_i+s_i).
Summed Cauchy--Schwarz gives q_ADE<=N*P/(N+P). With
N<=8+d,P<=7 the exact gaps against 5-1/d are 1/16,13/34,7/18
for d=1,2,3. All are positive. This excludes every irreducible E,
including irreducible singular genus-one divisors.

## 4. Reduced support and independent enumeration

When E is reduced and connected with at least two components,
adjunction says that each component's total intersection with the
others is 2-2*p_a. Connectedness makes this positive, so every
component has arithmetic genus zero and is a smooth rational curve.
The resulting connected degree-two intersection multigraph is a cycle:
two vertices have an intersection of two, or at least three vertices
have the usual cyclic edges of weight one. Coincident intersection
points and tangencies are allowed by this matrix argument. The passage
lemma ensures that the marked smooth curve never passes through them.

Minimality gives each diagonal b_i>=2. The reduced coefficient vector
and E^2=-d give sum(b_i-2)=d. The rank bound is k<=9+d.
Thus weak compositions of d into k entries generate all permitted cycle
matrices. Their positive definiteness follows by adding a nonzero
nonnegative diagonal correction to the positive semidefinite cycle
Laplacian. Connectedness makes its constant-vector kernel disappear.

The independent checker built 1033 ADE multisets under total root rank
at most eleven and total first-normal order at most seven. It computes
the allowed A,D,E corrections and indices from complete inverse root
columns, including spin indices in odd D_n. For each cycle it checks all
marked columns and all applicable smaller rank budgets. It finds exactly:

| d | Diagonals starting at the marked prime | q_irr | ADE multiset | Full correction denominator |
|---:|---|---:|---|---:|
| 1 | (2,3) | 3/2 | seven A1 | 2 |
| 1 | (2,3) | 3/2 | five A1 and A3 at its middle vertex | 2 |
| 1 | (2,2,3,2) | 2 | six A1 | 2 |
| 2 | (2,2,4,2) | 3/2 | seven A1 | 2 |
| 3 | (2,2,5,2) | 4/3 | six A1 and A2 at an end vertex | 6 |

The first four denominators give actual degree-two mates by rational
resolution compression and are excluded by the fixed C0 quadric
argument. Full column denominators were used: the denominator of q_irr
alone would give an incorrect index in some marked cycle columns.

## 5. The remaining row and normal-sheaf defect

The final row spends all seven available ADE normal orders. Together
with the nonrational point's lower bound two, this uses the total normal
order nine, forcing e=0. The available global normal-sheaf defect is
deg N_(C/S)-(C#)^2=7-4=3.

Each of its six A1 passages contributes 1/2. The A2 contribution 1/3
is checked directly. On xy=z^3 with C=(x,z), the ordinary point blowup
is smooth. The y chart has y=t,z=t*u,x=t^2*u^3 and pulled-back ideal
(t*u). The z chart has x=z*X,y=z*Y,z=X*Y and ideal (X*Y). Therefore
the ideal exceptional coefficients are both one. The numerical inverse
column has coefficient 2/3 at the end met by the strict curve, so the
normal-sheaf defect there is 1-2/3=1/3. The source smooth A2 pair
classification identifies the two symmetric ends; no additional pair
was omitted.

The ideal-principalization comparison makes all other point
contributions nonnegative, independently of normality at all support
points in its more general theorem. Here the carrier is normal. Hence
the row would require

    3 >= 6/2+1/3=10/3,

which is impossible. This completes the independent audit of the reduced
exceptional exclusion.

## 6. Validation and remaining hypothesis boundary

The independent scan returned exactly five configurations with degrees
2,2,2,2,6. Reproduction:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_normal_independent_audit.py
```

The finite calculation does not prove existence of any configuration;
over-enumeration is harmless for these exclusions. The result retains
the source characteristic-zero classification and the previously proved
global rational-resolution compression as dependencies. It gives no
classification or exclusion of reducible nonreduced E, whose multiplicity
vector requires a separate graph and discrepancy analysis.
