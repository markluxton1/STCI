# Nonendpoint quintics: actual conormal and conductor modules

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md).

<a id="1-nonendpoint-conormal-cubic-reduction"></a>
<a id="3-nonendpoint-conormal-and-socle-independent-audit"></a>

## Correct conormal frames and the socle bound

### 2. Derivation from the actual moving target coordinates

Let s=r-delta, delta!=0, and use the actual section family in the
linked note. On c its restrictions are

    X0=r^4, X1=r^3*s, X2=r*s^3, X3=s^4.

Write Ai=(partial_T Xi)|c. Then

    A0=a-2r^2-r,
    A1=b+delta*r-2r^2-r,
    A2=g+3delta*r-2r^2-r,
    A3=d+4delta*r-2r^2-r.

On the target chart x0!=0 the actual moving support coordinate is
z=x1/x0, whose restriction is s/r. Define the balanced residuals

    V=x2/x0-z^3,
    U=x3/x0-(3/2)z*(x2/x0)+(1/2)z^4.

Differentiating all the target ratios, including z, gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3*A2-3r*s^2*A1+2s^3*A0,
    J=2r^3*A3-3s*r^2*A2+s^3*A1.

Expanding those identities yields exactly

    P=(g-3b+2a)r^3
      +[6delta(b-a)+delta^3-3delta^2]r^2
      +[delta^2(6a-3b)+2delta^3]r-2a delta^3,

    J=(2d-3g+b)r^3
      +[3delta(g-b)+5delta^3-3delta^2]r^2
      +[3bdelta^2+delta^3-delta^4]r-b delta^3.

The coefficients of U would be wrong if z were frozen to its value
on c before differentiating. The independent checker reconstructs
the entire section family and takes its actual ratio jets.

### 3. The opposite balanced frame has the same scalar transition

In the first target chart write, to first normal order,

    x0=1, x1=z, x2=z^3+V,
    x3=z^4+U+(3/2)zV.

On the opposite chart put the actual moving coordinate w=x2/x3 and

    a_inf=x1/x3-w^3, b_inf=x0/x3-w^4,
    Vraw_inf=a_inf, Uraw_inf=b_inf-(3/2)w*a_inf.

Expansion modulo I_C^2 gives

    a_inf=2z^(-7)U,
    b_inf=3z^(-8)U+(1/2)z^(-7)V.

Consequently the correct adjusted frame is

    Uop=Vraw_inf/2, Vop=2Uraw_inf,
    Uop=z^(-7)U, Vop=z^(-7)V modulo I_C^2.

Both components have the same scalar transition. In particular their
projective ratio glues as a map to a fixed P1, with no residual swap
or unequal twist. On the source r-chart this also gives

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Thus r=0, which maps to the opposite target endpoint, is covered
correctly. The intrinsic r=infinity point maps to target z=1;
it must also be retained when homogenizing the cubics.

### 4. Homogeneous gcd determines the saturated quotient degree

Let P_h(R,S)=S^3 P(R/S), J_h(R,S)=S^3 J(R/S), and let Gamma be
their homogeneous gcd, of degree h. The pair cannot be identically
zero when delta!=0. Indeed their constant coefficients force a=b=0,
after which P's r coefficient is 2delta^3. Equivalently the exact
denominator-free witness is

    delta*[r]P + 3*[1]P - 3*[1]J = 2delta^4.

After dividing by Gamma, the pair is basepoint free and consists of
binary forms of degree 3-h. Its induced P1 map therefore has degree

    e=3-h, with 0<=e<=3.

This includes a common zero at R/S=infinity and the case where
one polynomial is identically zero. Taking only an affine gcd could
miss a common infinity factor.

For a hypothetical quasiprimitive defining CI, the first saturated
BF quotient is a line bundle L with a surjection
`N_C^*=O(-7)^2 ->> L`. Its generic quotient images are precisely
the displayed U_T,V_T, up to one common rational scalar. Generic
regularity of the quintic and birational normalization identify these
with the actual transverse direction at the generic point. Saturating
the kernel globally determines this quotient uniquely. The adjusted
frame above makes its projective direction pair `[J_h:2P_h]`;
passing to the annihilating first-normal relation `[2P_h:-J_h]`
uses only a constant invertible change of basis. Thus both have the
same homogeneous gcd degree, and

    L=O_P1(e-7), e=3-deg Gamma.

This deduction uses the actual global saturated quotient, not a
choice of first-normal generators with a prescribed common scale.
It imposes no divisibility of one equation's first-normal scalar by
the other's; nonregular first-normal ratios remain permitted.

As an algebraic check that the coprime locus is not identically absent,
delta=1,a=1,b=g=d=0 gives

    P=2r^3-8r^2+8r-2, J=2r^2.

The only finite root of J is zero, where P=-2, and P's leading
coefficient is two, so the homogeneous pair has no infinity common
factor either. This is a polynomial-family check, not a declaration
that this particular projection center is admissible or gives a mate.

### 5. Socle inequality for every hypothetical CI(5,4k)

The quintic is regular at the generic point of C0, so a hypothetical
CI(5,4k) is generically curvilinear of multiplicity m=5k. Complete
intersection adjunction gives `omega_Y=O_Y(4k+1)`. Its top saturated
BF piece is

    E_(5k-1)=Ann_(O_Y)(I_C)
            =omega_C tensor (omega_Y|C)^(-1)
            =O_P1(-16k-6).

The generically nonzero multiplication of the first piece into that
top piece gives `E_(5k-1)=L^(5k-1)(D_top)` with D_top effective.
It follows that

    deg D_top=(5k-1)(7-e)-6-16k
             =(19-5e)k+e-13 >=0.

For k=2, the four possibilities e=0,1,2,3 give respectively
`25,16,7,-2`. Therefore a hypothetical (5,8) pair requires e<=2,
equivalently a nonconstant homogeneous common factor of P_h,J_h.

For coprime cubics e=3, the same condition is `4k-10>=0`, which
requires k>=3. It excludes degree eight and leaves degree twelve
and larger permitted by this one necessary inequality. It is not
an exclusion of generic mates in all degrees or an existence theorem
in the retained degrees. Closed-point defect divisors, nonregular
ratios, higher jets, center avoidance and entire conductor descent
still require their own arguments.


### 4. An explicit complete incidence cover of the necessary common-root locus

The homogeneous common-root condition can be retained without expanding
a large resultant. For each actual delta!=0 it is exactly the union of:

* r=0: a=b=0;
* r=infinity: g=3b-2a and d=4b-3a;
* a finite nonzero root rho: P(rho)=J(rho)=0.

In the last case one may solve without losing a stratum:

    g=3b-2a-[6delta(b-a)+delta^3-3delta^2]/rho
      -[delta^2(6a-3b)+2delta^3]/rho^2
      +2a delta^3/rho^3,

    d=(3g-b)/2-[3delta(g-b)+5delta^3-3delta^2]/(2rho)
      -[3b delta^2+delta^3-delta^4]/(2rho^2)
      +b delta^3/(2rho^3).

Repeated roots and multiple common roots remain in this incidence
cover. It does not classify actual higher embedded jets or assert any
surviving parameter admits a mate. At a finite smooth source point
where both target chart and source transverse coordinate are regular, a common root records a transverse projection rank drop along c.
No root-count or contact bound is inferred from that first symbol.


<a id="2-nonendpoint-restricted-conductor-determinant"></a>
<a id="4-conductor-quadric-module-independent-audit"></a>

## The actual conductor quadric and all admissible center ranks

### 1. Actual ring, normality, finite graded module and its depth

Let T be the homogeneous coordinate ring of the literal anticanonical
degree-five A4 model S in P5. The accepted
[explicit model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit)
and [exact source](../computations/verify_session_quintic_a4_exact_ideal_2026_10_11.m2)
give a prime ideal generated by the five displayed quadrics. The source
actually asserts resolution length three, ranks (1,5,5,1), and shifts
(0,2,3,5), in addition to dimension three and the complete elimination
kernel. Its SHA-256 is
`3a48626539da961ca68edd3d3b13a33d39cb154020e52a19c292d06e9ce77ca9`.
The current source agrees with that accepted hash; no fresh replay of its
seventy-two-condition model audit is claimed here.

Auslander--Buchsbaum over the regular six-variable ring gives depth(T)=3,
so T is arithmetically Cohen--Macaulay. This conclusion does not follow
from normality of the projective surface alone. The projective charts are
normal by the accepted direct A2 and A4 chart arguments. Off the cone
vertex, the cone is locally a Gm bundle over those normal charts; its
height-one localizations are therefore normal. The vertex has codimension
three, and T is S2 by Cohen--Macaulayness. Serre's criterion gives normality
of T as well. Depth at least two also identifies T with the full section
ring of O_S(H), so the anticanonical model is projectively normal.

Set R=k[X0,X1,X2,X3] abstractly, with its action through the four actual
degree-one projection sections. Center avoidance says that
Proj(T/(R_+T)) is empty; hence rad(R_+T)=T_+. The quotient is a finite
graded k-vector space. Lifting a homogeneous basis and inducting on degree
expresses every element of T as an R-linear combination of those lifts.
Thus T is a finite graded R-module, without assuming it in order to use
graded Nakayama.

After localizing R at its homogeneous maximal ideal, there is exactly one
maximal ideal of T above it, because rad(R_+T)=T_+. Its localization has
depth three. The finite-map depth equality therefore gives depth_R(T)=3;
see the freshly checked
[Stacks finite-map depth lemma 0AUK](https://stacks.math.columbia.edu/tag/0AUK).
Equivalently, local cohomology has the same support radical. The regular
four-variable R has finite global dimension, and
[Auslander--Buchsbaum 090U](https://stacks.math.columbia.edu/tag/090U)
gives pd_R(T)=1. A minimal graded resolution remains minimal after
localizing at R_+, so it has the same length one globally.

The kernel of R->T is the height-one prime (F), with F the irreducible
quintic equation of the image. Finite birationality gives rank one over
A=R/(F). At the level of fraction fields this is also a statement about
the cones: choose a nonzero projection coordinate X0. The projective
function fields agree, and both cone fraction fields are generated by
that common function field and X0. Thus Frac(A)=Frac(T).

### 2. Why the presentation determinant is F, not a power of F

The length-one resolution is a square free presentation

    0 -> F1 --M--> F0 -> T -> 0.

Its determinant is nonzero because T is torsion over R and the map is
injective between free modules of equal rank. Localize at the height-one
DVR R_(F). The module T_(F) is killed by F and is one-dimensional over
the residue field Frac(A), by the rank-one statement above. Its length
is exactly one. Smith normal form over this DVR consequently gives
valuation_F(det M)=1.

At every other height-one prime, F is a unit and T localizes to zero.
The presentation is then an isomorphism, so det M has no other prime
factor. Since R is a UFD,

    det M = nonzero scalar * F.

This proves the precise determinant assertion for every admissible
projection. It does not use an unspecified generic rank or identify a
support equation with a higher-power Fitting equation.

### 3. All center-restriction ranks and exact generator degrees

Choose complementary degree-one coordinates h,z. Modulo R_+, the entire
ring is exactly k[h,z] divided by the restrictions of the five defining
quadrics. Let C be their 5 by 3 coefficient matrix in h^2,hz,z^2, and
let s=rank(C). These are all the generators of the restricted ideal;
no unexamined higher defining equations occur.

Ranks zero and one leave a projective point on the binary center, so
center avoidance rules them out. At rank two, the two independent
quadrics have no common projective root. They therefore have no common
factor and form a regular sequence in k[h,z]. The entire Artinian
quotient has Hilbert series 1+2t+t^2. At rank three it is exactly
k[h,z]/(h,z)^2, with Hilbert series 1+2t.

The Hilbert numerator of T over R is

    1+2t-2t^2-t^3.

Graded Nakayama determines all minimal generators from the Artinian
quotient. Since pd_R(T)=1, subtraction from this numerator determines
all relation degrees, not merely their number:

    rank two: generators 0,1,1,2; relations 2,2,2,3;
    rank three: generators 0,1,1; relations 2,2,3.

At rank two, the row for the generator of degree two has entries
(0,0,0,L) in the minimal 4 by 4 presentation. The first three entries
have degree zero and must be zero by minimality. Thus det M has the
linear factor L. L and the complementary determinant are both nonzero,
since det M is nonzero. This contradicts the irreducibility of the
degree-five F. Therefore every admissible center has rank three.

This argument explicitly covers the base-point-free binary rank-two
pencil. It does not incorrectly rule it out by base-point freeness alone.
It also leaves no admissible higher-generator chart outside the proof.

### 4. Actual nonreduced conductor membership and a shorter existence proof

At rank three, T is generated by 1,h,z. Write its quadratic relations as

    a1+b1*h+c1*z=0,  a2+b2*h+c2*z=0,

with ai quadrics and bi,ci linear in X. Put D0=b1*c2-b2*c1. Then the
literal elimination identities give

    D0*h=c1*a2-c2*a1,
    D0*z=b2*a1-b1*a2.

Both right sides are cubic polynomials in R. Hence D0*T is contained
in A, because 1,h,z generate the whole T. This is membership in the
actual conductor A:T, not merely vanishing on its radical or on one
branch of the normalization.

If D0=0, the two companion cubics vanish in T. They lie in the kernel
(F), but have degree three, so they vanish as polynomials in R. All
2 by 2 minors of the first two columns of the 3 by 3 presentation then
vanish. Those columns have rank at most one over Frac(R), making the
full determinant zero, contrary to Section 2. Thus D0 is nonzero.

For a finite birational inclusion A subset T with the same fraction
field, Hom_A(T,A) is identified with A:T by evaluating at 1: every
homomorphism is multiplication by its generic scalar, and its value at
1 belongs to A. This is simultaneously an ideal of A and T. Therefore
the projective conductor ideals satisfy nu_*I_S=I_X exactly, including
nilpotent and branch structure.

The accepted actual canonical equalities are

    omega_X=O_X(H), omega_S=O_S(-H).

Finite duality gives the actual invertible conductor ideal
I_S=O_S(-2H). The finite-duality mechanism was freshly checked in
[Stacks 0AX1](https://stacks.math.columbia.edu/tag/0AX1); this uses the
dualizing sheaves and the finite Cohen--Macaulay map, not only a
numerical canonical divisor class. Twisting D0 by 2H now makes it a
nonzero global section of I_S(2H)=O_S. Proper integral S has only
constant global functions. This section is a unit, so D0 generates the
entire upstairs conductor, with every multiplicity.

There is an independent shorter proof of existence and uniqueness.
Projection formula and the exact conductor equality give

    H0(X,I_X(2))=H0(S,I_S(2H))=H0(S,O_S)=k.

Every section of O_X(2) comes from an ambient quadric: the quintic
hypersurface sequence has terms O_P3(-3), O_P3(2), O_X(2), and
H1(P3,O(-3))=0. This vanishing is the freshly checked
[projective-space cohomology formula 01XS](https://stacks.math.columbia.edu/tag/01XS).
Also H0(P3,O(-3))=0, so the lift is unique. Thus the unique ambient
conductor quadric, up to a nonzero scalar, exists directly from the
accepted actual conductor sheaf. The presentation proof additionally
supplies its formula and center-rank coverage.

The downstairs conductor is not generated by D0 alone. Its ideal is
D0*nu_*O_S, with the cubic companions D0*h and D0*z as additional
generators in compatible frames.

### 5. The universal determinant and an auxiliary exact conductor resolution

Write the five original quadrics as

    qi=ai(X)+bi(X)h+ci(X)z+Ci0*h^2+Ci1*h*z+Ci2*z^2.

On each chart where one of the ten 3 by 3 minors Delta of C is nonzero,
row elimination removes the three quadratic monomials h^2,hz,z^2.
The remaining two equations are independent quadratic relations: a
constant dependence between them would be a dependence between the
five original defining quadrics. The Hilbert calculation in Section 3
says there are exactly two independent degree-two relations, so these
form their basis.

Block determinant expansion gives

    det[C | b | c] = sign * Delta * D0.

The chosen Delta is a nonzero scalar at that particular projection.
Every admissible center lies in at least one such chart. Consequently
the universal 5 by 5 determinant is nonzero and gives the same entire
conductor divisor on all charts. A vanishing chosen minor causes no
omission: another minor applies. The universal expression itself has
no pivot denominator.

For clarity about the actual downstairs scheme, put

    E=a1*c2-a2*c1=-D0*h, K=a1*b2-a2*b1=D0*z.

The three generators of the downstairs conductor ideal are D0,E,K.
The full determinant expands as a3*D0-b3*E+c3*K=scalar*F. Thus F is
already in their ideal. Any irreducible common divisor of D0,E,K would
divide F, but cannot equal F because D0 is nonzero of degree two.
Their greatest common divisor is one.

There is a direct proof of the Hilbert--Burch resolution in this case.
The two columns (a1,b1,c1) and (a2,b2,c2) have rank two and are polynomial
syzygies of the signed minors. Over every height-one DVR at least one
minor is a unit, so every polynomial syzygy is an R_p-linear combination
of the two columns. Its uniquely determined coefficient pair belongs
to every height-one R_p. Since the UFD R is the intersection of those
DVRs inside Frac(R), the pair belongs to R itself. Hence these columns
generate the entire syzygy module, and

    0 -> R(-4)^2 -> R(-2) plus R(-3)^2 -> I_Gamma -> 0

is exact. The gcd-one condition gives height at least two; this
resolution and Auslander--Buchsbaum give height at most two and
Cohen--Macaulayness. The ideal is saturated, and the Hilbert series of
R/I_Gamma is

    (1-t^2-2t^3+2t^4)/(1-t)^4
      =(1+2t+2t^2)/(1-t)^2.

Thus the actual downstairs conductor is an arithmetically
Cohen--Macaulay degree-five genus-two determinantal curve. This is an
auxiliary proved consequence; it retains nonreduced cases and does
not assume a flat degree-two conductor cover.

### 6. The restriction to c and finite necessary incidence

The nonendpoint inverse coordinate substitution in owner equation (5)
is invertible for delta!=0. It divides only by powers of delta and by
the characteristic-zero scalar three. Its five-quadratic determinant
therefore covers the whole displayed parameter family, subject to
center avoidance.

The conductor does not contain c, independently of any mate or full
inverse-support assumption. Indeed the smooth target quadric containing
C0 has C0 of class (1,3), and the integral quintic restricts to a nonzero
section of class (5,5). Multiplicity at least two along C0 would leave
an effective divisor of negative second bidegree. The multiplicity is
therefore exactly one. At the generic point of C0, the regular local
ring of P3 has parameters q for the quadric and u for C0 within it.
F modulo q has u-order one, so F does not belong to the square of the
maximal ideal. The quintic local ring is regular there, and normalization
is an isomorphism. Hence its conductor cannot contain c.

The nonzero restriction of the conductor section is consequently a
homogeneous degree-eight binary form. Affine degree loss records a
root at target infinity, not the disappearance of an intersection.
The change r=delta*Q/P is invertible on the binary parameter line,
so it preserves every repeated common root of the homogeneous
conormal pair and correctly exchanges source r=0 with target Q=0.

Under a hypothetical mate, full inverse support makes the finite
normalization algebra local over every target point of C0. At a
smooth-source point with at least one conormal symbol nonzero, its
cotangent map is surjective. The two finite Nakayama steps in the
accepted conormal/conductor audit then give an exact local ring
isomorphism. At A4, the full three-dimensional cotangent determinant
is -3delta^3*Jbar, so the same conclusion holds if Jbar!=0. Both
single-preimage finiteness and the entire singular cotangent space
are retained.

Therefore the support of the restricted conductor form Fdet is contained
in the homogeneous gcd H of the transformed conormal cubics, together
with P=0 when Jbar=0. For a degree-eight binary form this support
inclusion is equivalent to

    Fdet divides (H*P^epsilon)^8,
    epsilon=1 if Jbar=0, and zero otherwise.

The exponent eight bounds each root exponent by the total degree of
Fdet. It does not equate conductor multiplicity with first-normal
multiplicity. The owner's finite incidence in H,A_P,A_J,K therefore
preserves every possible multiplicity distribution, including a single
root of order eight. The h0=epsilon=0 case is empty; all other displayed
degrees are nonnegative. This remains only a necessary incidence.

### 7. Compact norm: the apparent leading factor and every degree drop

The owner writes A2=A*r^2+b*r+c and
C3=p*A^2*r^3+d*r^2+e*r+f. Put K0=d-p*A*b and E0=e-p*A*c.
Modulo A2 the cubic has linear remainder

    ((A*E0-b*K0)*r+(A*f-c*K0))/A.

For A!=0, taking the quadratic norm gives the stated identity
Res(A2,C3)=A*N0. Expanding this expression gives exactly the seven
terms of the owner's compact N0. This independently explains the
apparently extraneous factor A rather than treating a zero resultant
as an off-c certificate on a leading-drop locus.

Write the leading two coefficients of the owner's N polynomial as
n2=3delta^2*p*(2-p) and n1=-delta^3*(6-p^2). Comparison of the
r^3 coefficients in Psi=(pr-delta)C3 gives

    d=A*(p*(2*n1+n2)+delta*A)-p*n2^2.

At A=0, Z=-n2, so on pZ!=0 one has d=-p*n2^2!=0.
The compact expression specializes to

    N0=d*(d*c^2-e*b*c+f*b^2).

For b!=0 the second factor is the exact linear/quadratic common-root
test. For b=0,c!=0 it is nonzero; for b=c=0 the genuine quadratic
C3 has a root over the algebraically closed field. All leading drops
are therefore retained. The normalized norm has exactly the claimed
affine common-root interpretation on pZ!=0, including a possible root
r=delta/p representing an allowed doubled c-fiber.

The literal comparison N0=p^2*delta^6*Z^2*Fdet, its scalar normalization
81delta^10, and the A4/endpoint special values are supplied by the
separate accepted fifteen-identity source. I inspected its exact
construction of the five quadrics, independent coefficient matrix,
quotient identities and captured PASS stream, and verified its source
and stream hashes. No separate fresh symbolic replay of that source
is claimed here. Its exact calculation supports the literal scalar
comparison; the structural proof in Sections 1--5 establishes why the
determinant is the actual conductor.

The endpoint identity retains its B=0 specialization explicitly, and
the geometric norm interpretation is not extended across Z=0, p=0
or target infinity. Those targets retain their separate exact fiber
equations. In particular Fdet=0 is not itself an off-c exclusion when
the common residual root is the allowed doubled c-fiber.


## Explicit inverse coordinates and the complete restricted octic

### 5. Explicit nonendpoint coordinates and the restricted binary octic

Use the actual parameters of the
[target-fiber note](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions):

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a, delta!=0.

Take h=T=Z2+Z3 and z=U1=Z4 as complementary coordinates. The exact inverse
linear substitution is

    U3=(X0-X1+B h)/delta,
    U2=(X2-3X1+2X0-G h+delta^3 z)/(3delta^2),
    U0=(X3-2X2+2X1-X0-Jbar h+2delta^3 z)/delta^4,
    Z0=X0-a h-U3, Z1=-U3, Z2=h-U2,
    Z3=U2, Z4=z, Z5=U0.                                 (5)

Only the stipulated nonzero delta, and the characteristic-zero scalar 3,
are divided out. Substituting (5) into the five displayed quadrics defines
the matrix N without any elimination or generic parameter specialization.

Define the homogeneous degree-eight binary form

    Fdet(P,Q)=81 delta^10
       D(Q^4,Q^3(Q-P),Q(Q-P)^3,(Q-P)^4).                 (6)

The fixed scalar is convenient for the fiber norm comparison. Its affine
chart Q=1 uses p=P/Q=1-z_target. The intrinsic A4 point is p=0; target
infinity is Q=0. The form is nonzero for every admissible projection. On the
smooth target quadric, the quintic restriction has class (5,5) and C0 has
class (1,3). Its multiplicity along C0 is one: multiplicity at least two
would leave an effective residual of negative second bidegree. At generic C0,
the regular two-dimensional local ring of P3 has parameters q,u, where q
defines the smooth quadric and u defines C0 on it. Since F modulo q has
u-order one, F is not in the square of the maximal ideal. Thus X is regular
at generic C0, and its normalization is an isomorphism there. The conductor
cannot contain c. This argument is independent of full inverse support.

Formula (6) includes all multiplicities of Dc|c. Its degree is exactly eight
as a homogeneous form, even if the affine p-polynomial loses leading terms.
The scalar delta is retained as a modulus. A polynomial expression with
integer rational coefficients can be obtained by clearing only the explicit
powers of delta in (5); no locus in a,B,G,Jbar is inverted.

The computed A4 value is

    Fdet(0,1)=-3 Jbar Delta1,

    Delta1=G(G+3delta^2)(G+delta^2+2B)
       +Jbar[(delta^2-5B)G-3B(delta^2+3B)]-B Jbar^2.      (7)

Thus conductor at this target can arise from either the actual A4 rank drop
Jbar=0 or the second-point condition Delta1=0. This is an exact value, not
an equality between the first-normal common divisor and the full conductor.
### 6. A finite necessary incidence retaining arbitrary conductor multiplicities

Suppose a mate exists. Its full inverse target support is exactly c.
At every finite smooth point of c where the two actual conormal symbols
do not vanish together, the cotangent map is surjective. The finite
single-fiber Nakayama argument in the
[conormal/conductor audit](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit)
makes the normalization a local isomorphism there, so Dc misses that point.
At A4 the same argument applies if Jbar!=0.

Let Pn(P,Q),Jn(P,Q) be the degree-three binary forms obtained from the actual
conormal cubics by the source change r=delta Q/P, explicitly by homogenizing
p^3 P(delta/p)/delta^3 and p^3 J(delta/p)/delta^3. This is an invertible
binary-coordinate change for delta!=0. It retains the finite source point
r=0 as Q=0, the intrinsic A4 point as P=0, and all repeated common roots.
Let H be their complete homogeneous gcd, of degree h0 from zero to three.
Let epsilon=1 when Jbar=0 and epsilon=0 otherwise. The support conclusion
just proved is exactly the necessary condition

    supp div(Fdet) subset supp div(H P^epsilon).          (8)

No local conductor multiplicity is bounded by h0, by the multiplicities of
H, or by a first-normal coefficient. Its total degree eight is used instead.
For binary forms over the algebraically closed field, (8) is equivalent to

    Fdet divides (H P^epsilon)^8.                        (9)

Indeed every root exponent of Fdet is at most eight, while every allowed
root occurs in H P^epsilon with exponent at least one. This gives a finite
denominator-free polynomial incidence: for each h0=0,1,2,3 and epsilon=0,1,
introduce binary forms H,A_P,A_J,K and impose

    Pn=H A_P, Jn=H A_J,
    (H P^epsilon)^8=Fdet K,
    deg A_P=deg A_J=3-h0,
    deg K=8(h0+epsilon-1).                              (10)

Impose nonzero H,Fdet and the stated Jbar condition. The case
h0=epsilon=0 is empty because a nonconstant Fdet cannot divide one.
Taking h0 equal to the complete gcd proves necessity; allowing a smaller
common H may add restrictions but cannot create a purported sufficient
STCI condition. One may alternatively factor Fdet into at most four
allowed linear factors with positive exponents summing to eight. Both
descriptions preserve all possible high contact at each allowed point.

This is a necessary incidence for the actual restricted conductor. It does
not certify full inverse support, full conductor-ring power descent, center
avoidance, or existence of a mate. In particular, the quadratic/cubic target
fiber equations on pZ!=0, their Z=0 and p=0 charts, the endpoint chart, and
the allowed doubled r=delta/p fibers remain separate necessary conditions.


<a id="5-nonendpoint-all-mate-conormal-conductor-independent-audit"></a>

## Coprime conormal cubics away from the A4 cotangent hypersurface

### 1. Hypotheses and the precise all-mate conclusion

Work over an algebraically closed field k of characteristic zero, for the
fixed curve C0 and the accepted genus-one degree-five A4 normalization pair
`(S,c)` of the
[intrinsic classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification).
Retain the nonendpoint parameters `delta!=0,a,b,g,d`, and actual center
avoidance. The resulting projection

    nu:S -> X subset P3

is finite birational and is the normalization of its integral quintic
image. Its restriction `c->C0` is an isomorphism. These admissibility
statements are justified explicitly in the
[pole-filtration audit](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#3-nonendpoint-pole-filtration-and-line-jet-independent-audit).

The accepted
[quintic conductor audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit)
gives the entire upstairs conductor as the actual invertible ideal

    I_cond,S=O_S(-2H) subset O_S.

Its effective zero divisor `D_cond` is Cartier and linearly equivalent to
`2H`, not merely a numerical conductor cycle. In particular

    deg O_c(D_cond)=2H.c=8.

Let P,J be the corrected cubic numerators in the owner note and let
`Ph,Jh` be their degree-three homogeneous forms on c. Set

    Jbar=d-2g+2b-a.

Then any actual mate, in **any** positive degree, necessarily satisfies

    Res_h(Ph,Jh)*Jbar=0.                     (A)

Equivalently, the locus where the homogeneous pair is coprime and
`Jbar!=0` has no mate in any degree. The proof uses no socle-degree
inequality and does not depend on a bound for the mate exponent.

### 2. P,J detect every smooth-source rank drop along c

On `S\ell=A2`, the coordinates `(r,T)` are regular, c is `T=0`, and
the restriction of the four projection sections is

    (r^4,r^3(r-delta),r(r-delta)^3,(r-delta)^4).

For `r!=0`, use the target chart `x0!=0` and set

    y=x1/x0, z2=x2/x0, w=x3/x0,
    V=z2-y^3, U=w-(3/2)y*z2+(1/2)y^4.

The ideal `(V,U)` equals `(z2-y^3,w-y^4)`; hence its differentials
are an actual basis of the normal cotangent space to C0 at every finite
value of y. In particular there is no extra exceptional finite y at which
this first-symbol test loses a normal direction.

The T derivatives of the actual four sections on c are

    L0=a-2r^2-r,
    L1=b-2r^2-r+delta*r,
    L2=g-2r^2-r+3delta*r,
    L3=d-2r^2-r+4delta*r.

Direct quotient and chain differentiation gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3 L2-3r(r-delta)^2 L1+2(r-delta)^3 L0,
    J=2r^3 L3-3r^2(r-delta)L2+(r-delta)^3 L1.

Thus these expressions include movement of y; they are not derivatives
taken with the image curve parameter artificially held fixed. Expansion
gives exactly the corrected cubics in the owner note. This audit uses
the corrected J, not the earlier rejected expansion.

The image tangent along c is nonzero: for `r!=0`, its y derivative is
`delta/r^2`. If at least one of P,J is nonzero at the source point,
the image of the transverse tangent vector is not in that tangent line.
Consequently the differential from the smooth surface S has rank two,
equivalently the target cotangent map onto the source cotangent space
is surjective.

The point `r=0` is not discarded. There `x3=delta^4!=0`, so use the
reversed target coordinates. If their raw balanced coordinates are
`Vraw,Uraw`, put `Uop=Vraw/2,Vop=2Uraw`. On the overlap, writing
`z2=y^3+V,w=y^4+(3/2)yV+U` and retaining terms modulo `(U,V)^2`
gives

    Uop=y^(-7)U, Vop=y^(-7)V.

Their actual T derivatives therefore extend as

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Both denominators are nonzero at r=0. The reverse image curve parameter
is `r/(r-delta)`, whose derivative is `-delta/(r-delta)^2`, also
nonzero there. Hence the same rank-two conclusion holds at r=0 whenever
P,J are not simultaneously zero. Explicitly the zero condition there
is `a=b=0`, since `P(0)=-2a delta^3` and `J(0)=-b delta^3`.

Every source point of c except its A4 point is one of these finite r
points. Homogeneous coprimality of Ph,Jh therefore implies immersion at
every smooth-source point of c, with no missing projection rank-one point
or missing opposite target frame.

### 3. The actual A4 cotangent matrix, including its full embedding dimension

At A4 use the accepted chart `Z0=1`, with

    alpha=Z1, beta=Z2, chi=Z3,
    dZ=alpha*beta-chi^2,
    eZ=beta^2-alpha*beta*chi+chi^3.

The local surface equation is

    beta*(chi-alpha^2)+alpha*chi^2=0.

It has no linear term, so the classes of alpha,beta,chi form a basis of
the full three-dimensional cotangent space at this singular point. Both
dZ and eZ lie in the square of its maximal ideal. Thus this calculation
does not replace the singular cotangent space by a smooth normal direction
or discard torsion in a curve conormal sheaf.

Here `U4=1-alpha`, `U3=-alpha`, `U2=chi`, `U1=dZ`,
`U0=eZ`, and `h=beta+chi`. The actual section X0 has value one, so
the target affine ratios are valid at this point. With `B=b-a`, the
linear parts of `Xi/X0-1`, for i=1,2,3, have coefficient matrix

    [ delta,  B,    B                ]
    [3delta,  g-a,  g-a+3delta^2     ]
    [4delta,  d-a,  d-a+6delta^2     ].

Subtracting three and four times the first row from the second and third
gives its determinant directly as

    -3delta^3*(d-2g+2b-a)=-3delta^3 Jbar.

Since `delta!=0` and the characteristic is zero, `Jbar!=0` makes the
target cotangent map surjective at A4 as well. It factors through the
cotangent space of X, because every equation of X pulls back to zero
on S. The singularity of S poses no obstruction to this implication.

### 4. Finite local cotangent lemma: where full inverse support is essential

**Lemma.** Let `A subset B` be a finite inclusion of Noetherian local
rings, with maximal ideals m,n, with equal residue fields. If the map
`m/m^2 -> n/n^2` is surjective, then `A=B`.

Indeed surjectivity gives

    n=mB+n^2.

The finite B-module `n/mB` therefore equals its product with n. Nakayama
over B implies `n=mB`. Equality of residue fields gives `B=A+n`, so

    B=A+mB.

The finite A-module `B/A` now equals `m(B/A)`. Nakayama over A gives
`B/A=0`. These are the ordinary finite-module forms of
[Nakayama's lemma, Stacks 00DV](https://stacks.math.columbia.edu/tag/00DV),
freshly inspected for this audit. No analytic inverse-function theorem,
formal power-series approximation or conductor flatness is used.

For application at a closed point `x in C0`, the finite algebra
`B=(nu_*O_S)_x` is initially allowed to be semilocal. A hypothetical
mate forces the **entire reduced inverse support**

    (nu^(-1)(C0))_red=c.

Because `c->C0` is an isomorphism, there is consequently exactly one
preimage point over x, including no extra isolated point. Thus B has one
maximal ideal and is the local ring of S at that point. Its residue field
and that of `A=O_X,x` are both k. Finiteness over A is retained.

This single-preimage step is indispensable. Localizing one branch of a
multi-preimage fiber and applying the lemma without proving finiteness
would not justify a normalization isomorphism. The mate's full support
supplies precisely the missing hypothesis here.

Under homogeneous coprimality and `Jbar!=0`, Sections 2 and 3 give the
required cotangent surjectivity at every such source point. The lemma
therefore makes nu a local isomorphism at every closed point of C0.
In particular the full actual conductor ideal is the unit ideal at
every point of c.

### 5. The conductor contradiction uses an actual restricted section

The actual effective Cartier conductor `D_cond~2H` would now have support
disjoint from c. Its canonical section restricts to a nowhere-vanishing
section of `O_c(2H)`. This would trivialize that line bundle, whereas

    deg O_c(2H)=2*deg H|c=8.

This is impossible on the complete smooth curve c. It does not require
c itself to be Cartier in S, reduced conductor branches, a smooth
downstairs conductor, or a rank-two flat conductor cover. It uses the
accepted entire invertible conductor ideal, not a replacement cycle.

The contradiction proves (A) in every possible mate degree. It is not
a first-normal upper bound on a later contact multiplicity: first
derivatives here prove cotangent surjectivity, and the finite local
lemma plus full support converts that into an exact ring equality.
### 6. Properness, retained exceptional loci and evidence

The necessary locus is proper. At

    delta=1, a=1, b=g=d=0

the corrected cubics homogenize to

    Ph=2(R^3-4R^2S+4RS^2-S^3), Jh=2R^2S,

and `Jbar=-1`. Their homogeneous roots have no common point. Hence
the product in (A) is a nonzero polynomial. This specific point need
not be asserted admissible: center avoidance is a nonempty open set,
so the complementary nonempty open intersects it in the irreducible
nonendpoint parameter family. The accepted center point lies outside
S, and the bad line extensions are the image of the two-dimensional
S in the four-dimensional extension space, which proves that assertion.

The homogeneous common-root-at-infinity locus already lies in
`Jbar=0`: the two leading coefficients give
`g=3b-2a,d=4b-3a`, hence Jbar vanishes. Thus one may equivalently
retain the A4 cotangent hypersurface together with the finite common-root
incidence. The proposed product formulation remains correct and keeps
all homogeneous frames explicit.

The remaining resultant and A4 cotangent loci are **OPEN** in this audit.
No assertion that they admit a mate is made. The earlier entire-line
ramification conditions satisfy `R3-2R2=Jbar`; their separate all-power
exclusion addresses a subfamily of this retained A4 hypersurface.


<a id="6-jbar-zero-coprime-conductor-phase-bound"></a>
<a id="7-jbar-zero-conductor-phase-independent-audit"></a>

## The coprime Jbar-zero stratum: full conductor powers

### 1. Precise scope and retained exceptional cases

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint genus-one quintic A4 pair. Retain arbitrary
`delta != 0,a,b,g,d`, actual center avoidance and finite birational
normalization `nu:S -> X`. The lifted c maps isomorphically to fixed C0.
Write

\[
\bar J=d-2g+2b-a=0,\qquad E=g-3b+2a.
\]

Assume the corrected degree-three homogeneous conormal forms Ph,Jh are
coprime, including their roots at infinity. Every supposed mate pulls
back to a scalar Q^k, where Q is an actual section of 4H with divisor
5c, and forces the full reduced inverse support to be c.

The two cubic leading coefficients both equal E on this hypersurface.
Thus E=0 is incompatible with homogeneous coprimality. The case
E=-3delta^2 is exactly the previously audited entire-line ramification
locus, since its second equation equals twice the first on Jbar=0.
Its separate characteristic-zero derivation obstruction excludes every
positive power. The rest of this proof assumes
`E(E+3delta^2) != 0`. It does not claim the following length-two fiber
calculation on the removed ramified-line locus.

Under a hypothetical mate, coprimality and the actual opposite target
frame give cotangent surjectivity at every finite point of c, including
r=0. Full support leaves one normalization point over each such image.
The finite local Nakayama lemma therefore makes nu a local isomorphism
there. The conductor divisor misses all finite points of c.

### 2. The actual A4 fiber and finite generation

Use the accepted A4 source chart

\[
B=k[\alpha,\beta,\chi]/
  (\beta(\alpha^2-\chi)-\alpha\chi^2),\quad
h=\beta+\chi,\quad d_Z=\alpha\beta-\chi^2,\quad
e_Z=\beta^2-\alpha\beta\chi+\chi^3.
\]

The actual target maximal ideal pulls back, after invertible row
operations and the unit X0, to

\[
f_1=\delta\alpha+(b-a)h,\quad
f_2=Eh+3\delta^2\chi-\delta^3d_Z,\quad
f_3=\delta^4e_Z-2\delta^3d_Z.
\]

These are exact section identities. The first two eliminate alpha,chi
formally, with nonzero linear determinant `3 delta^3`. Their leading
solution is

\[
\alpha=-(b-a)h/\delta+O(h^2),\quad
\chi=-Eh/(3\delta^2)+O(h^2),\quad
\beta=(1+E/(3\delta^2))h+O(h^2).
\]

The source equation then has nonzero leading coefficient
`E(E+3delta^2)/(9delta^4)` on h^2. It therefore generates `(h^2)`
in the one-variable completed ring. The third target generator has
order at least two and cannot remove its surviving first-order h.
The completed fiber is exactly `k[[h]]/(h^2)`, of length two.
Completion preserves this finite length.

Full inverse support implies that p is the only point above y=nu(p).
Consequently the normalization algebra at y is local, finite over
O_X,y, and is the actual source local ring used in that calculation.
Its fiber dimension two makes it a two-generated O_X,y-module by
Nakayama. The two generators extend to a surjection from O_U^2 on
some open neighborhood U of y. This is local module generation,
not flatness or a claim that all conductor algebras have length two.

Each conductor prime D_i meets c. It is not c, since the conductor
misses finite c. The nonzero restricted section Q|D_i has positive
line-bundle degree `4H.D_i`, so it has a zero on this complete integral
curve. Every such zero lies on c, and finite c was excluded. Hence
D_i contains p; its image curve contains y, and its generic point
belongs to U. The two-generator bound therefore applies at every
generic conductor point.

At such a point eta, the finite normalization fiber is an Artinian
k(eta)-algebra whose residue-field degrees sum to at most its dimension,
and that dimension is at most two. This bounds the sum of the reduced
field degrees. It does **not** bound the length of B/I: arbitrary
higher generic conductor exponents remain possible.

### 3. Complete low-degree prime classification

The normal complement S minus ell is A2 with r,t, where
`T=t+r^2` and `v=t^2-r^3`. The complete pole-order-five space is
`span(1,r,t,r^2,rt,v)`, by the already proved valuation filtration.
For a prime D_i other than ell, its affine generator f is irreducible,
and its only possible additional divisor is the boundary ell.
Thus `div(f)=D_i-n ell`, where intersection with H identifies
`n=H.D_i` as its exact pole order.

Avoidance of finite c says that f(r,-r^2) is a nonzero constant.
Writing

\[
f=A_0v+A_1rt+A_2r^2+A_3t+A_4r+A_5
\]

gives

\[
f|_c=A_0r^4+(-A_0-A_1)r^3+(A_2-A_3)r^2+A_4r+A_5.
\]

Constancy forces `A0=A1=A4=0,A2=A3`. A nonconstant prime therefore
has equation `A3 T+A5`, with both coefficients nonzero, and exact
degree four. This proves that among degrees at most five the only
allowed prime other than ell has degree four. It includes singular
projective primes and repeated occurrences of a prime in the conductor.

### 4. Excluding ell over the nonclosed generic residue field

The line ell maps isomorphically to a target line L: its four actual
sections are `(u-1,u-1+delta,u-1+3delta,u-1+4delta)`, which span
the full degree-one system. Its generic residue field is
`K=k(L)=k(u)`, not the algebraically closed constant field.

The required generic cotangent argument can be proved by an actual
target equation, avoiding any residue-field shortcut. In the target
X0 chart let

\[
\ell_2=X_2/X_0-3X_1/X_0+2.
\]

It vanishes on L. Its actual numerator is
`3delta^2 U2-delta^3 U1+E h`. In the fourth source chart,

\[
U_2=x(1+xu),\quad U_1=x^3(1+xu)^2,\quad
h=x(1+xu)+x^2(1+xu)^2,\quad X_0|_{x=0}=u-1.
\]

Consequently

\[
\ell_2=x\frac{E+3\delta^2}{u-1}+O(x^2).
\]

Its ell valuation is exactly one on the retained locus. If ell is
the sole normalization branch over generic L, the finite local
normalization ring B_eta is a DVR with residue K, equal to the
residue field of A_eta. The element ell_2 belongs to m_A and generates
the maximal ideal of B_eta up to a unit. Hence `m_A B=n_B`.
Residue equality gives `B=A+n_B=A+m_A B`; Nakayama on the finite
A-module B/A gives A=B. Thus a sole branch cannot be a conductor
branch. This proof works over K and requires neither an algebraically
closed residue field nor an inverse-function theorem.

If another branch exists, the actual two-generator fiber bound leaves
at most one additional branch and forces its residue-field degree to
be one. Its distinct source prime D' has
`H.D'=degree(map)*degree(L)=1`, contradicting uniqueness of ell.
All branches over a generic conductor point occur in the conductor:
I is proper in the target local ring, so its extension is proper in
each normalization maximal ideal. Thus no uncounted additional
branch can escape this argument. Ell is excluded.

### 5. Split reduced algebras are excluded by degree accounting

Now every conductor prime has degree at least four, and none has
degree five. If a generic full conductor algebra T has split reduction,
the field-degree bound makes it exactly `K x K`. Its two distinct
source primes D1,D2 map birationally onto the same image curve, so
their H-degrees equal its degree e. They occur with positive integer
coefficients in the actual Cartier divisor Dc of total degree ten.
Hence `2e<=10`, and the preceding prime classification forces e=4.

Their minimum contribution is eight; increasing either integer
coefficient makes it at least twelve. Minimum coefficients leave
degree two, which cannot be supplied by any remaining prime now that
ell and all primes of degree two or three have been excluded.
Therefore no split reduced generic conductor occurs.

This accounting does not replace nonreduced conductor schemes by
their reductions: the integer coefficients explicitly retain them.
The possible full generic Artinian algebra has one residue field
L/K of degree one or two. Its nilpotent length is unrestricted by
this field-degree statement.

### 6. Full arbitrary-power membership forces Q squared membership

Trivialize the actual downstairs line bundle O_X(4) at each generic
conductor point. The residue q of Q in T=B/I is a unit, because its
upstairs divisor 5c has no conductor prime. The supposed mate gives
full membership `q^k in R=A/I`, not only a tensor equalizer or reduced
membership.

Here R is Artinian local, Rred=K, and Tred=L is one field of degree
at most two. If alpha=qred belongs to K, its minimum reduced period
is one. Otherwise L/K has degree two and its nontrivial automorphism
sends alpha to zeta alpha, since alpha^k lies in K. All roots of unity
are already in K. Applying the automorphism twice gives zeta^2=1;
since alpha is not in K, zeta=-1. Thus alpha^2 belongs to K, the
minimum period is two, and k must be even. This is why odd successful
k cause no omitted parity case: they require period one.

The full nilpotent step is indispensable. Let d be this period, one
or two, choose a unit r in R lifting alpha^d, and put
`q^d/r=1+n` with n nilpotent in T. A successful k=dm implies
`(1+n)^m in R`. In characteristic zero the finite nilpotent logarithm
gives `m log(1+n) in R`; dividing by m and applying the finite
exponential gives `1+n in R`. Hence `q^d in R`, in every nilpotent
layer. Either value of d implies `q^2 in R`.

For comparison, the abstract split algebra `K x K` permits residues
`(1,zeta)` with arbitrary root-of-unity order; a two-branch bound alone
would not imply this conclusion. That algebra was excluded by the
actual geometry in section 5 before this power argument. Likewise,
two generators do not bound nilpotent conductor length: for
`A=K[[t^2,t^(2m+1)]]` inside `B=K[[t]]`, B has two generators over
A while the conductor quotient B/(t^(2m)) has length 2m. The proof
retains these potential nilpotent lengths rather than replacing T
by a quadratic reduced cover.

### 7. Purity, the actual ambient mate and the socle contradiction

The accepted entire quotient is
`nu_*O_S/O_X=omega_Gamma(-H)`, maximal Cohen--Macaulay on the
Cohen--Macaulay conductor curve, and hence pure of dimension one.
The obstruction class of Q^2 in this quotient twisted by O_X(8)
vanishes at every generic conductor point by full membership above.
Its generated coherent subsheaf would then have finite support;
purity makes it zero. Thus Q^2 descends globally to O_X(8), including
all special conductor points. Residue-only membership would not
justify this invocation of purity.

The quintic hypersurface sequence
`0 -> O_P3(3) -> O_P3(8) -> O_X(8) -> 0` and H1(O_P3(3))=0 lift
that section to an ambient degree-eight form G. Its pulled-back
zero divisor is 10c. Finite surjectivity of nu makes the zero support
of G on X exactly C0, so G is an actual degree-eight mate.

This mate gives a generically curvilinear CI(5,8), of multiplicity
ten. Coprimality fixes its first saturated quotient as
`L=O_P1(3-7)=O_P1(-4)`. Complete-intersection duality fixes the
top socle line as `E9=O_P1(-38)`. Generic curvilinear multiplication
gives a generically nonzero global map `L^9 -> E9`, but its Hom
space is H0(O_P1(-2))=0. Equivalently the effective top defect would
have degree -2. This is the accepted socle bound, now applied to an
actual forced mate rather than an assumed degree reduction.

The contradiction excludes every supposed mate power in this stratum.
Combined with the independently audited Jbar-nonzero obstruction, a
mate anywhere in this nonendpoint genus-one lane must satisfy the
complete homogeneous common-root condition `Res_h(Ph,Jh)=0`.
The common-root, higher-jet and full-conductor incidence remains open;
other quintic normalization genera and higher carriers are outside scope.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_conormal_cubics_2026_10_12.m2](../computations/verify_session_nonendpoint_conormal_cubics_2026_10_12.m2), [verify_session_nonendpoint_a4_cotangent_rank_2026_10_12.m2](../computations/verify_session_nonendpoint_a4_cotangent_rank_2026_10_12.m2), [verify_session_quintic_a4_exact_ideal_2026_10_11.m2](../computations/verify_session_quintic_a4_exact_ideal_2026_10_11.m2), [verify_session_nonendpoint_diagonal_norm_2026_10_12.m2](../computations/verify_session_nonendpoint_diagonal_norm_2026_10_12.m2), [verify_conormal.py](../validation/2026-10-12-nonendpoint-conormal-independent-audit/verify_conormal.py), [verify_session_jbar_zero_phase_audit_2026_10_12.m2](../computations/verify_session_jbar_zero_phase_audit_2026_10_12.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
