# Rational-resolution normal quartic carriers: classification audit and Type D reduction

Date: 2026-10-07  
Branch: `research/normal-rational-carrier-classification`  
Base main: `7662a2ebb1dd561c1fb5e3c8958799b37d962c41`

## Status

This note does **not** claim a complete exclusion of the rational-resolution normal-quartic branch. It records an audit of the live canonical state and a sharper structural reduction for Type D suggested directly by Ishii--Nakayama's construction.

Labels used below: **PROVED**, **EXACT REDUCTION**, **CONDITIONAL**, **OPEN**.

## A. Audited starting point

The current authority is `research/STATE.md`, not the dated compatibility pointer `AUDITED_STATE_2026-10-06.md`.

The following are accepted on the current record.

1. **PROVED.** Normal quartic carriers with only rational singularities are excluded by Jaffe's quartic theorem.
2. **PROVED.** The positive-genus ruled irrational cases cannot contain a rational quartic of hyperplane degree four.
3. **PROVED.** If the rational quartic avoids the nonrational exceptional anticanonical locus, the numerical correction/rank budget is impossible.
4. **PROVED.** The simple-elliptic case (a single smooth reduced elliptic exceptional curve) is excluded.
5. **OPEN.** The surviving Ishii--Nakayama rational-resolution cases are B1, B2, B3, D with reducible, singular, or nonreduced anticanonical exceptional divisor.
6. **PROVED, conditional on existence of a mate on the fixed carrier.** If (ar C=c+Z) is the numerical pullback, denominator clearing compresses any mate to the least common denominator of (Z). The existing determinant argument gives finite but large upper bounds.
7. **Important scope.** The determinant bound is a mate-degree bound, not a classification of exceptional graphs and not an existence theorem.

For the four rational types the source gives
[
(ho(M),-E^2)=(12,2),(11,1),(11,1),(13,3)
]
for B1, B2, B3, D respectively.

## B. Source check

Ishii--Nakayama, *Classification of normal quartic surfaces with irrational singularities*, JMSJ 56 (2004), 941--965, is stronger for the present problem than the repository's coarse ((ho,-E^2)) summary.

The paper classifies via a basic triplet ((M,D,E)), with (D) the pullback of a general hyperplane and (E) an effective exceptional anticanonical divisor. Its Main Theorem says the examples in section 2 exhaust the normal quartics with irrational singularities.

In particular:

- B1 arises by separation from a generalized del Pezzo surface of degree two with (Bin|-2K_X|), (Gin|-K_X|). The quartic has equation
  [
  (X_0X_1-q(X_1,X_2,X_3))^2=d(X_1,X_2,X_3).
  ]
- B2 arises from a degree-one generalized del Pezzo construction and has two subcases B2-1/B2-2.
- B3 arises from a double cover of (mathbb F_1); its anticanonical divisor is explicitly tracked through the construction.
- D arises by separation of a smooth plane quartic (B=(F_4=0)) and an effective plane cubic (G=(F_3=0)), and the resulting quartic has the explicit monoid equation
  [
  X_0F_3(X_1,X_2,X_3)=F_4(X_1,X_2,X_3).
  ]

No later source located in the focused search gives a ready-made classification of rational quartic curves on the remaining B1/B2/B3/D carriers or an STCI exclusion for them.

## C. Intrinsic resolution identities

Let (H=pi^*O_S(1)), let (c) be the strict transform of the smooth rational quartic, and let (E=-K_M).

For an STCI mate on a quartic carrier,
[
ar C=c+Zequiv H,qquad H^2=4,qquad Hc=4,qquad H E=0.
]

Put (r=cE). Adjunction on (csimeqmathbb P^1) gives
[
-2=c^2+cK_M=c^2-r,
]
hence
[
oxed{c^2=r-2.}
]

Since (Har C=4) and (ar C^2=H^2=4), orthogonality of the numerical pullback to exceptional curves gives
[
Z^2=c^2-4=r-6,
]
so
[
oxed{-Z^2=6-r.}
]

Thus the former all-ADE correction (6) is only the special case (r=0). Any surviving nonrational passage consumes anticanonical intersection and lowers the total numerical correction.

If (E=sum a_iE_i) and (m_i=cE_i), then
[
r=sum a_im_i,qquad Z=A^{-1}m
]
for (A_{ij}=-E_iE_j), and therefore
[
oxed{m^TA^{-1}m=6-sum_i a_im_i.}
]
This is the central finite-lattice equation once the actual exceptional graph is known. It must be combined with (m_ige0), effectivity/integrality, the first-normal zero budget, and the denominator/Cartier condition.

## D. New structural reduction for Type D

**PROVED from the cited classification.** Every Type D quartic can be written, after choosing coordinates with its irrational point at (p=(1:0:0:0)), as
[
S:quad X_0F_3(X_1,X_2,X_3)=F_4(X_1,X_2,X_3),
]
where (F_4=0) is a smooth plane quartic and (F_3=0) is an effective plane cubic. The resolution is the separation of these two plane divisors.

Consequently a rational quartic (Csubset S) through (p) is controlled by projection from (p). Let
[

u:mathbb P^1	o C,qquad gamma=operatorname{pr}_pcirc
u:mathbb P^1	omathbb P^2.
]
Away from the preimage of (p), containment is exactly
[
X_0circ
u=rac{F_4circgamma}{F_3circgamma}.
]

Therefore:

> **EXACT REDUCTION (Type D).** Classifying Type D carriers containing the fixed rational quartic is equivalent to classifying plane cubic/quartic pairs ((F_3,F_4)), with (F_4) smooth and satisfying the Ishii--Nakayama separation hypotheses, for which the missing projective coordinate of (C) descends as (F_4/F_3) along the projected rational plane cubic.

This converts Type D from an unspecified exceptional-graph problem into a concrete conductor/descent problem on the projected cubic.

For the endpoint (p=[1:0:0:0]) of
[
C_0=[s^4:s^3t:st^3:t^4],
]
projection is the rational cubic
[
[s:t]longmapsto[s^3:st^2:t^3].
]
Writing (A=s^3,B=st^2,C=t^3), the Type D containment equation is
[
s^4F_3(A,B,C)=t,F_4(A,B,C)
]
after removing the common powers contributed by the projection coordinates. This is a finite exact linear condition on the coefficients of (F_3,F_4).

An exact scratch linear-algebra check gives ranks
[
operatorname{rank}(operatorname{res}_3)=9,qquad
operatorname{rank}(operatorname{res}_4)=12,
]
and an 11-dimensional kernel for the combined coefficient equation before quotienting by equations vanishing identically on the projected cubic. This shows that **containment alone does not immediately eliminate Type D**. The next issue is the smoothness/separation condition on (F_4), followed by the Cartier/mate condition.

This scratch calculation is not yet promoted as a repository certificate.

## E. Type-by-type status after this audit

| Type | Source structure | Current status |
|---|---|---|
| B1 | degree-2 generalized del Pezzo; explicit double-cover quartic equation | OPEN; should be attacked through the explicit equation, not arbitrary graph enumeration |
| B2 | degree-1 generalized del Pezzo; B2-1/B2-2 | OPEN |
| B3 | double cover of (mathbb F_1); explicit anticanonical construction | OPEN |
| D | separation of plane quartic/cubic; monoid equation (X_0F_3=F_4) | EXACT REDUCTION to projected-cubic descent plus mate condition |

## F. What is not proved

- No B1/B2/B3/D type is excluded in full by this note.
- The exceptional intersection vector (m=(cE_i)) is not yet classified.
- The exact local Cartier index of (C) at the irrational point is not yet computed.
- The Type D coefficient calculation above establishes only the size of the linear containment incidence at one distinguished point of (C_0); it does not establish normality, the precise Ishii--Nakayama subtype conditions, or existence of an STCI mate.
- Numerical equivalence has not been silently upgraded to linear equivalence except where the existing rational-resolution denominator-compression theorem supplies that implication under a mate hypothesis.

## G. Recommended next attack

Do **not** begin with a free enumeration of negative-definite graphs.

1. Finish Type D first using the explicit monoid model. Compute the projected-cubic conductor condition for a general point (pin C_0), impose smoothness of (F_4), and identify the separation data met by the strict transform of the projected cubic.
2. From that separation, compute (m=(cE_i)), (Z=A^{-1}m), and the exact denominator. If the denominator is (<6), the existing compression theorem immediately contradicts the known mate-degree lower bound.
3. If Type D survives, impose the mate divisor directly on the separated plane model; this should be substantially smaller than searching mate forms in (mathbb P^3).
4. Treat B1 next through its explicit double-cover equation. B2/B3 should remain behind these because their source models are less immediately rigid.

The key conceptual change is that Ishii--Nakayama supplies **birational models with explicit separation data**, not merely four values of ((ho,-E^2)). The remaining classification should exploit those models before lattice enumeration.


## H. Type D separation arithmetic: a rigid multiplicity sequence

Ishii--Nakayama define separation by repeatedly blowing up a point of the current intersection of the transforms of B and G. At each step the intersection number B.G drops by one. Type D starts with a smooth plane quartic B and an effective plane cubic G, so B.G=12. Hence the separation consists of exactly twelve blowup steps, allowing infinitely-near centers.

Use the total-transform basis L,e_1,...,e_12 for Pic(M). Since B is smooth and every separation center lies on its current strict transform, the hyperplane pullback is

    H=D=4L-sum e_i.

The anticanonical exceptional divisor is

    E=3L-sum e_i=-K_M.

Let p be the Type D irrational point on the smooth rational quartic C. Projection from p has degree three, so its plane image R is a cubic. If n_i is the multiplicity of the successive strict transform of R at the i-th separation center, then

    c=3L-sum n_i e_i.

Because H.c=deg C=4,

    12-sum n_i=4,

hence

    sum n_i=8.                                      (D1)

Also

    c.E=9-sum n_i=1.                               (D2)

This already proves:

> **PROVED (Type D anticanonical passage).** Any smooth rational quartic of degree four through the Type D irrational point has strict transform meeting the exceptional anticanonical divisor with total intersection c.E=1.

Adjunction gives

    -2=c.(c+K_M)=c^2-c.E,

so c^2=-1. On the other hand

    c^2=9-sum n_i^2.

Therefore

    sum n_i^2=10.                                  (D3)

Subtracting (D1) from (D3),

    sum n_i(n_i-1)=2.

All n_i are nonnegative integers. Thus exactly one n_i equals 2, no n_i exceeds 2, and the remaining positive n_i are six 1's. Therefore:

> **PROVED (Type D multiplicity theorem).** In the twelve-step separation cluster, the projected cubic R meets exactly seven centers (counting infinitely-near centers): one with multiplicity two and six with multiplicity one. Equivalently the nonzero multiplicity sequence is
>
>     (2,1,1,1,1,1,1)
>
> up to order.

For the endpoint p=[1:0:0:0] of C0, the projected cubic is

    R: y^3=x z^2,

parametrized by [s:t] -> [s^3:s t^2:t^3]. Its unique double point is the image of t=0, i.e. the point corresponding to p. Thus in this endpoint model the multiplicity-two separation center must be that cusp if the separation cluster contains it. The containment identity

    s^4 Phi_3(s^3,s t^2,t^3)
      = t Phi_4(s^3,s t^2,t^3)

indeed forces Phi_3 restricted to R to vanish at t=0, so the cusp belongs to the B/G separation support. Hence the double center is the cusp.

Since E is effective and c.E=1, if E=sum a_j E_j in prime components, then c can meet only coefficient-one components, and the weighted total intersection is one. In particular c meets exactly one coefficient-one component transversely provided c is not itself contained in E (it is not, since H.c=4 while H.E=0).

### Consequence for the numerical correction

The universal intrinsic equation specializes in Type D to

    -Z^2=6-c.E=5,

or, for m_j=c.E_j and A=(-E_i.E_j),

    m^T A^(-1)m=5.

Moreover m is supported on a coefficient-one component of E with weighted sum one. This sharply reduces the remaining Type D lattice problem: one needs only the diagonal inverse entries (A^(-1))_{jj}=5 for coefficient-one components that can be met by c, together with the denominator of the corresponding column A^(-1)e_j.

This is the next exact target. A denominator below six would contradict the existing denominator-compression theorem plus the established lower mate-degree exclusions.

### Scope

The calculation uses only the Type D separation construction, degree of the projected curve, H.c=4, K_M=-E, and adjunction. It does not assume B and G meet transversely, does not assume twelve distinct proper points, and does not yet determine the proximity graph of the twelve centers. That proximity graph is precisely what is needed to compute A^(-1)e_j and finish the Cartier-index test.
