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

Write the exceptional locus as the disjoint union of the block over the irrational monoid point and the blocks over any rational double points met by c. The equality c.E=1 constrains only the irrational block. It implies that inside Supp(E), c meets exactly one coefficient-one component once. It does NOT imply that the full exceptional intersection vector m is supported there: c may also meet coefficient-zero exceptional curves over Du Val singularities. Accordingly the total correction 5 splits as

    delta_p + delta_ADE = 5,

where delta_p is the correction at the monoid point. The earlier draft's stronger assertion (A^(-1))_{jj}=5 for the irrational block alone was false and is superseded by this block decomposition.

### Scope

The calculation uses only the Type D separation construction, degree of the projected curve, H.c=4, K_M=-E, and adjunction. It does not assume B and G meet transversely, does not assume twelve distinct proper points, and does not yet determine the proximity graph of the twelve centers. That proximity graph is precisely what is needed to compute A^(-1)e_j and finish the Cartier-index test.


## I. Type D: literature compression and first-normal split

### I.1 External classification of quartic monoids

Johansen--Løberg--Piene, *Monoid hypersurfaces*, classify the complex tangent cubic of a quartic monoid into nine types: nodal cubic, cuspidal cubic, conic plus chord, conic plus tangent line, three general lines, three concurrent lines, double line plus line, triple line, and smooth cubic. Their Theorem 9 also gives the complete possibilities for singularities away from the monoid point. In every case those additional singularities are of type A_n, with n determined by residual intersection multiplicities of the tangent cubic and quartic.

Thus for Type D the rational exceptional blocks relevant to c are A-type only. This is stronger than the generic ADE allowance used in the earlier budget.

### I.2 Local expansion at the endpoint of C0

Take p=[1:0:0:0] and q=t/s. Near p,

    C0(q)=[1:q:q^3:q^4].

Put plane coordinates [x:y:z]=[X1:X2:X3]. Projection from p is

    [x:y:z]=[1:q^2:q^3]

after dividing by q. Let

    g(q)=Phi_3(1,q^2,q^3),
    b(q)=Phi_4(1,q^2,q^3).

The monoid containment equation X0 Phi_3=Phi_4 becomes

    g(q)=q b(q).                                    (D4)

Since g has no q^1 term, (D4) forces b(0)=0. Hence the smooth plane quartic B passes through the cusp point [1:0:0] of the projected cubic.

Because B is smooth there, its restriction b(q) has order either 2 or 3 according as its linear term contains y or only z. Consequently g(q) has order respectively 3 or at least 4.

In affine coordinates (u,v,w)=(X1/X0,X2/X0,X3/X0)=(q,q^3,q^4), the carrier equation is

    f(u,v,w)=Phi_3(u,v,w)-Phi_4(u,v,w).

If ord b=2, the identity permits an x^2 z term in Phi_3; then partial f/partial w can have order 2 along C0. If ord b>=3, all first partials have order at least 3 along C0. Therefore:

> **PROVED (endpoint first-normal split).** The Type D monoid point consumes first-normal order at least 2. It consumes at least 3 unless the smooth quartic B has order exactly 2 on the projected cusp.

The global quartic first-normal budget is at most 9 (or 9-e in the refined order-one notation). Thus the A-type singularities away from p have total first-normal budget at most 7 in the order-2 subcase and at most 6 in the order-at-least-3 subcase.

### I.3 Correction at the irrational block

Let A_p be the negative intersection matrix of the exceptional block over p and write E=sum a_i E_i there. Since c.E=1, c meets a unique component E_j with a_j=1, once, and no other component of Supp(E). Thus

    delta_p=(A_p^(-1))_{jj}.

The component met by c is the component reached by the tangent direction of the projected cubic after separation. At the initial cusp center it comes from a reduced local branch of the tangent cubic. For a coefficient-one strict-transform component R of plane degree d=1,2,3, adjunction/separation gives -E.R=K_M.R>=1. Since

    A_p a = (-E.E_i)_i >=0

and its j-th entry is at least one, positivity of A_p^(-1) gives

    A_p^(-1)e_j <= a

componentwise. In particular

    delta_p <= a_j=1.

This comparison is valid when the component met by c is such a reduced strict-transform component. The remaining possibility that the tangent direction terminates on a coefficient-one (-2)-component created by a nonreduced/infinitely-near separation needs a separate check; it is not silently included.

### I.4 Harmonic consequence

Let N be the total A-root rank away from p and P their total first-normal order. Since rho(M)=13 and the irrational block has positive rank,

    N<=11.

The existing harmonic estimate gives

    delta_A <= N P/(N+P).

In the order-at-least-3 subcase, P<=6, hence

    delta_A <= 66/17 < 4.

If delta_p<=1 as in I.3, the mate relation requires

    delta_A=5-delta_p >=4,

a contradiction, with exact gap at least 2/17.

Therefore:

> **CONDITIONAL EXCLUSION.** Type D is excluded whenever (i) the endpoint monoid passage has first-normal order at least 3 and (ii) c meets a reduced coefficient-one strict-transform component of the tangent cubic.

The only endpoint configurations still requiring analysis are:
- the first-normal-order-2 case (ord b=2), where the coarse harmonic bound with P<=7 is not by itself contradictory; and
- any nonreduced/infinitely-near configuration in which the component met by c is a coefficient-one (-2)-curve, for which delta_p<=1 has not yet been justified.

This is now a small local problem. The monoid classification suggests treating it case-by-case through the nine tangent-cubic types rather than enumerating arbitrary negative-definite graphs.


## J. Type D: sharp Bezout correction bound

For a normalized quartic monoid, every isolated singularity away from the monoid point is A-type. If the tangent cubic G and quartic B have local intersection multiplicity m at the corresponding base point, the singularity is A_{m-1}. Hence for the off-vertex singularities met by c,

    sum (n_i+1) <= B.G = 12.

For Jaffe's A_n^k pair,

    delta(n,k)=k(n+1-k)/(n+1) <= (n+1)/4.

Therefore

    delta_off <= 3.                                (D5)

Since the total correction is 5,

    delta_p = 5-delta_off >= 2.                    (D6)

Thus every Type D STCI survivor must have correction at least two at the irrational monoid point.

### Endpoint order-two passage

In the endpoint notation, the first-normal-order-two case has ord b=2 and ord g=3 on the projected cusp (y,z)=(q^2,q^3). Smoothness of B makes its linear term a nonzero y-term, while the order-three identity makes G have a nonzero z-linear term. Thus B and G are smooth and transverse at the cusp, so their separation has exactly one blowup there.

The projected cusp is tangent to G. After the blowup, its strict transform still meets the reduced coefficient-one strict transform of G once. Hence the anticanonical comparison of I.3 applies and gives delta_p<=1, contradicting (D6).

> **PROVED (endpoint order-two exclusion).** No Type D STCI candidate with the irrational point at the endpoint [1:0:0:0] can lie in the first-normal-order-two branch.

Every endpoint survivor must therefore have first-normal order at least three and, by (D6), local irrational correction at least two. The remaining finite question is whether the cusp-following separation for one of the nine tangent-cubic types can land c on a coefficient-one exceptional component with inverse-matrix diagonal at least two. If such a component exists, its inverse column also gives the exact Cartier denominator for the compression test.


## K. Type D endpoint exclusion completed

This section finishes the Type D analysis when the irrational triple point is the endpoint p=[1:0:0:0] of C0.

### K.1 Exact local shape in the remaining branch

In the order-at-least-three branch of I.2, B is smooth at the projected cusp a and its restriction to R has order exactly three. Indeed the y-linear coefficient must vanish, while the z-linear coefficient is nonzero by smoothness. Thus

    ord_R(B)=3,
    ord_R(G)=4

by the containment identity g=q b.

In local cusp coordinates (y,z)=(q^2,q^3), order four for a cubic G means that its first nonzero term is a nonzero multiple of y^2. Hence G has multiplicity exactly two at a and has double tangent y=0. In particular the multiplicity-three tangent-cubic configurations (triple line, or the intersection point of a double line with another component) cannot occur at a.

The possible local forms are therefore:
1. an irreducible cuspidal branch;
2. two reduced tangent branches (the conic-plus-tangent-line type);
3. a smooth point of a double line.

### K.2 The separation over a

Ishii--Nakayama separation uses

    B_{j+1}=rho^* B_j - Gamma,
    G_{j+1}=rho^* G_j - Gamma,

not merely the strict transform of G. Consequently B_j.G_j drops by exactly one at each blowup. Since B is transverse to the double tangent direction of G, I_a(B,G)=2. Exactly two separation blowups occur over a.

After the first blowup,

    G_1 = G_strict + F_1

in the reduced multiplicity-two cases. B_1 meets F_1 at the B tangent direction, while the strict transform of the projected cusp meets F_1 at the distinct G tangent direction. The second blowup is therefore at B_1 cap F_1 and misses c. After it, the component met by c is the coefficient-one curve F with

    F^2=-2.

Thus the exceptional (-2)-curve found in the previous section is real, but its correction can be computed explicitly from the adjacent strict transform(s) of G.

### K.3 Local correction in the three cases

**Irreducible cusp.** The strict transform Q of the cubic loses 2^2 at a and one square for each of the remaining ten units of B.G, hence

    Q^2 = 9-4-10 = -5.

Moreover Q.F=2. The relevant block is

    A = [[5,-2],[-2,2]],

so

    delta_p = (A^{-1})_{FF}=5/6.

**Two reduced tangent branches.** The branches are a line and a conic. The previous draft incorrectly asserted that adding negative-definite attachments could only decrease the diagonal Green value at F. That monotonicity statement is false and is superseded here.

Let r and s be the remaining separation lengths assigned to the line and conic branches after the two cusp blowups. Since the residual B.G intersection is ten, r+s=10. In the total-transform calculation the relevant three-vertex Schur block has diagonal entries r, s-3, 2 and F meets each branch once. Negative definiteness leaves r=1,...,6. Direct inversion gives respectively

    delta_p = 6/5, 10/13, 12/17, 12/17, 10/13, 6/5.

Thus in every admissible allocation

    delta_p <= 6/5 < 2.

This finite calculation replaces the false monotonicity argument. Infinitely-near distribution along a fixed branch does not change the Schur-complement value: successive separation curves contract back to the same effective self-intersection contribution determined by the total separation length on that branch.

**Double line.** At a smooth point of the doubled line, F meets the line once. The line strict transform has square at most -3. The two-vertex comparison gives

    delta_p <= ([[3,-1],[-1,2]]^{-1})_{FF}=3/5.

The other line does not pass through a (otherwise mult_a G=3); including its attachment to the doubled line does not approach the required value two.

Thus every admissible local multiplicity-two form satisfies

    delta_p <= 6/5 < 2.

But J.1 gives the necessary inequality delta_p>=2. Therefore:

> **PROVED (Type D endpoint exclusion).** No Type D normal quartic STCI carrier can have its irrational triple point at the endpoint p=[1:0:0:0] of C0.

The remaining Type D question is whether an arbitrary point p in C0 reduces to the same local pattern after projection, or whether interior points produce a nodal rather than cuspidal projected cubic and require a separate calculation.


## L. Type D at a general point of C0: nodal projection and contact tradeoff

Let p=C0(a) with a nonzero finite parameter, so

    C0(u)=[1:u:u^3:u^4].

Projection from p can be represented by the three linear forms

    X1-a X0,  X2-a^3 X0,  X3-a^4 X0.

After cancelling u-a, the projected cubic R has parametrization

    [1 : u^2+a u+a^2 : (u+a)(u^2+a^2)].

The two distinct parameters

    u=a omega,  u=a omega^2,   omega^3=1, omega!=1,

have the same image. Thus for a!=0,infinity the projected cubic is nodal. The marked image r of p itself is smooth: its parameter value u=a has no second preimage.

### L.1 Local monoid identity at the marked smooth point

Put q=u-a. In projection coordinates the normalization near r is

    [1 : 3a^2+3a q+q^2 : 4a^3+6a^2 q+4a q^2+q^3].

The coordinate along the line through p has a simple pole in q. Hence the Type D equation again restricts to

    g(q)=q b(q),                                   (D7)

where b=B|_R and g=G|_R.

Unlike the endpoint cusp, the local ring of R at r is regular, so there is no semigroup gap forcing b(0)=0.

If b(0)!=0, then g has a simple zero. Thus G is smooth and transverse to R at r, while B misses r. No B/G separation blowup occurs over r. The strict transform c meets a reduced coefficient-one component of the anticanonical divisor directly, so the anticanonical comparison gives

    delta_p<=1.

This contradicts the universal Type D necessity delta_p>=2 from (D6). Therefore every general-point survivor must satisfy

    b(0)=0.

### L.2 Local normal form and contact accounting

Because R is smooth at r, choose local coordinates with R=(y=0), x=q. Since B is smooth, after a local coordinate normalization write

    B = y + beta(x),

where h=ord_x beta>=1 is the contact order I_r(B,R).

Equation (D7) says G(x,0)=x beta(x). Therefore locally

    G = x B + y A

for some local function A (after absorbing units/signs). In particular

    I_r(R,G)=h+1.                                  (D8)

Since deg R=deg G=3,

    R.G=9,

so

    1<=h<=8.                                       (D9)

This is the correct finite parameter for the general-point Type D problem.

There is also a compensation with the off-vertex correction. Let mu=I_r(B,G), i.e. the number of Ishii--Nakayama separation steps over r. Then only 12-mu units of the global B.G=12 intersection remain available away from r. The monoid A-type estimate sharpens from (D5) to

    delta_off <= (12-mu)/4.                        (D10)

Hence the mate relation forces

    delta_p >= 5-(12-mu)/4 = 2+mu/4.              (D11)

So increasing the local B/G contact makes the required irrational correction grow linearly. The remaining task is to bound the actual local Green value delta_p from above in terms of the same separation length mu (or the contact h). If one proves

    delta_p < 2+mu/4

for every 1<=h<=8 and every cubic local form compatible with G=xB+yA, Type D is excluded for every point of C0.

This is now a finite local inequality rather than a global quartic-carrier classification problem.

### L.3 Audit note

Earlier conversational exploration incorrectly suggested that (D7) forces B through r in the nodal case. It does not; that conclusion used the cusp semigroup at the endpoint. The present note records the corrected distinction explicitly.


## M. General-point Type D: local separation algebra

Continue with the local normal form

    R=(y=0),
    B=y+beta(x),    ord beta=h>=1,
    G=xB+yA.

Restricting G to B gives

    G|_B = -beta(x) A(x,-beta(x)).

Hence, provided B is not a component of G,

    mu=I_r(B,G)=h+alpha,                            (D12)

where

    alpha=ord_x A(x,-beta(x))>=0.

This identifies the separation length directly from the two local contacts.

### M.1 Reduced one-branch case

Suppose the component of G followed by c is reduced and locally irreducible at r, and the B/G separation over r does not branch. Successive separation blowups then give a linear chain attached to the strict transform Q of that component. After contracting the portions of the chain not met by c, the negative intersection matrix is represented by the continued fraction with initial diagonal at least 3 and mu successive 2's.

The largest possible Green value occurs for initial diagonal 3. Direct inversion gives

    delta_p <= (2 mu+1)/(2 mu+3) < 1.              (D13)

For mu=1,...,8 the values are

    3/5, 5/7, 7/9, 9/11, 11/13, 13/15, 15/17, 17/19.

But the global Bezout tradeoff (D11) requires

    delta_p >= 2+mu/4 >2.

Therefore:

> **PROVED (general-point, unbranched reduced local form).** No Type D STCI candidate can have the marked smooth point r lying on a locally irreducible reduced branch of G whose B/G separation tree over r is linear.

This includes the generic smooth-G situation and any reduced singular branch once its resolution/separation path followed by c is unbranched.

### M.2 Remaining local configurations

A general-point Type D survivor must therefore make the anticanonical separation tree branch at r. For a plane cubic this means that, locally at r, G is one of:

- two reduced branches (node or two components);
- three reduced branches;
- a double component plus another branch;
- a triple component.

The marked curve R itself is smooth at r. Equation I_r(R,G)=h+1 and the cubic degree constrain the sum of contacts of these branches with R. Together with (D12), this leaves a finite list of contact partitions.

The next computation should enumerate those partitions, build the corresponding star/chain negative matrices, and compare each exact diagonal Green value with 2+mu/4. This is substantially smaller than the nine global tangent-cubic types because only the local branch multiplicities at r matter.


## N. General-point branching bound

This section closes the local branching alternatives left in M.2, subject to the matrix interpretation stated there.

Because R is not a component of G, I_r(R,G) is finite. If mult_r(G)=3, then a plane cubic has no terms of degree below three at r; its local equation is its cubic tangent cone. Restriction to the smooth branch R=(y=0) therefore has order exactly three unless y divides G, which would make R a component. Hence

    h+1=3, so h=2.                                 (D14)

Thus multiplicity-three local forms do not generate arbitrarily long contact sequences.

### N.1 Reduced branching

Suppose the coefficient-one (-2)-curve F met by c is adjacent to k reduced branches of G. A reduced cubic branch, after the full B/G separation, contributes an effective negative diagonal at least 3 at the attachment. The Green value at F is therefore bounded by the corresponding star Schur complement.

For two branches,

    delta_p <= 1/(2-1/3-1/3)=3/4.

For three branches,

    delta_p <= 1/(2-1/3-1/3-1/3)=1.

The endpoint finite calculation shows how further separation along a branch is absorbed into its effective diagonal; with fixed cubic self-intersection and the B.G budget it does not make a reduced branch contribution exceed the extremal 1/3 used above.

Hence every reduced branching configuration has

    delta_p<=1.                                    (D15)

### N.2 Nonreduced adjacency

If F is adjacent to a doubled component, the corresponding intersection entry can have magnitude two. The worst negative-definite two-vertex block is

    A=[[3,-2],[-2,2]],

whose inverse has

    (A^{-1})_{FF}=3/2.

Larger branch diagonal only decreases this value. Thus

    delta_p<=3/2                                   (D16)

for doubled adjacency before any further constraints are imposed.

A triple adjacency would require an off-diagonal magnitude three. With F^2=-2 and a cubic-component diagonal in the available range, the corresponding principal minor fails negative definiteness; it cannot occur as such an exceptional block. Multiplicity-three cubic configurations are in any case constrained by (D14).

### N.3 Consequence

Combining the unbranched reduced estimate (D13), reduced branching (D15), and nonreduced estimate (D16), every general-point local configuration satisfies

    delta_p<=3/2.

But the global B/G Bezout tradeoff requires

    delta_p>=2+mu/4>2.

Therefore:

> **PROVED, subject to independent audit of the branch-effective-diagonal lemma.** No Type D normal quartic STCI carrier can have its irrational point at an interior point p=C0(a), a!=0,infinity.

Together with the endpoint exclusion, this would remove Type D completely for C0. Before promoting this to the canonical STATE, the branch-effective-diagonal assertion used in N.1 should be checked directly from the Ishii--Nakayama proximity basis (or by a small exhaustive proximity-matrix certificate). That check is preferable to relying on electrical-network intuition.

### N.4 Next audit target

Build an exact certificate enumerating the admissible separation/proximity matrices for a degree-three G with total B.G=12, marking the component reached by c, and verify:
1. negative definiteness;
2. E=-K coefficient vector;
3. the relevant diagonal of A^{-1};
4. the maximum is at most 3/2 in the general-point cases and at most 6/5 in the endpoint cases.

A successful certificate would promote the Type D exclusion from branch-level geometric proof to independently checked PROVED status.
