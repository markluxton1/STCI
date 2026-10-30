# October 9 historical mathematics

Full original source text preserved. Hypotheses, counterexamples, unsuccessful arguments, and open questions retain their source status; no new independent audit or theorem promotion.

---

## Source: 2026-10-09-session-elliptic-conductor-quadratic-descent-independent-audit.md

# Independent audit: quadratic descent across an elliptic conductor

**PROVED conditional exclusion, in characteristic zero.** The argument below
excludes every mate for a carrier satisfying all the listed hypotheses. It
does not assert that these hypotheses cover every singular normalization, or
that the requisite section `Q` always exists.

Let `nu:S -> X` be the finite normalization of an integral quartic surface
`X` in `P3`, with `S` normal and `H=nu^*O_X(1)`. Assume:

1. A smooth rational curve `c` maps isomorphically to the fixed smooth rational
   quartic `C0`.
2. A global section `Q` of `O_S(2H)` has Weil divisor exactly `2c`.
3. The **actual** downstairs conductor scheme `Gamma` is a smooth conic.
4. The **actual** upstairs conductor scheme `D` is a smooth integral elliptic
   curve, avoids `Sing(S)`, and maps finite flat of degree two to `Gamma`.

The conductor scheme hypotheses, not merely equality of conductor supports,
are needed for the fiber-product descent step.

## A hypothetical mate has the required divisor

Suppose an ambient form `G` of degree `b` is a mate, so its zero support on
`X` is precisely `C0`. The restriction is nonzero. Since `C0` is not the
degree-two conductor curve, its generic point is outside the conductor;
there the normalization is an isomorphism. Every curve in `nu^{-1}(C0)`
dominates `C0` under the finite map, so `c` is the only such curve. All points
of the inverse image away from `c`, if any, are isolated in that inverse
image. Such points already contradict the zero support of a nonzero Cartier
section on the normal surface `S`.

Therefore a hypothetical mate forces
`div_S(nu^*G)=m*c` for some positive integer `m`. Intersecting with `H` gives

\[
4b=bH^2=m(H\mathbin{\cdot}c)=4m,
\]

so `m=b`. Thus `div_S(nu^*G)=b*c` follows from the mate and conductor
hypotheses; it need not be separately assumed as a generic-order statement.

The sections `(nu^*G)^2` and `Q^b` of the same invertible sheaf have identical
Weil divisors. Their ratio has no divisorial zeros or poles, so it is a unit
on the normal projective integral surface, hence a nonzero constant. Thus

\[
(\nu^*G)^2=\lambda Q^b,\qquad \lambda\in k^\times.
\]

## Even valuations exclude the anti-invariant case

Write `p:D -> Gamma` for the conductor map and `q=Q|D`. This is a nonzero
section because `D` is not the rational curve `c`. The invertible sheaf
`O_S(2H)|D` is naturally `p^*O_Gamma(2)`, and its pullback linearization gives
a canonical action of the double-cover involution `sigma` on `q`.

The displayed power identity shows that `q^b` is invariant: its restriction
comes from the downstairs section `G^2|Gamma`, up to the scalar `lambda`.
Hence the rational function `sigma(q)/q` has `b`th power one. In the function
field of the integral curve over the algebraically closed field this means
`sigma(q)/q=zeta` for a constant root of unity. Applying `sigma` twice gives
`zeta^2=1`, so `sigma(q)=q` or `sigma(q)=-q`.

Riemann--Hurwitz gives four ramification points for the separable degree-two
map from the elliptic curve to the smooth conic. At any ramification point,
choose a frame pulled back from `O_Gamma(2)`; it is invariant. In completed
local coordinates, the involution acts by `z -> -z`. An anti-invariant
section then has an odd power series and therefore an odd vanishing order.

On the other hand, `S` is smooth along `D`. Near any point of `D`, the
divisor identity `div_S(Q)=2c` makes `Q` a unit times the square of a local
equation of `c` (or a unit if the point is not on `c`). Its nonzero restriction
to the smooth curve `D` has even vanishing order. This includes tangential
intersections: the local intersection multiplicity is simply multiplied by
two. The anti-invariant possibility is therefore impossible. Consequently
`q` is invariant and descends to a section `qbar` of `O_Gamma(2)`.

## The actual conductor square gives global descent

For the actual conductor ideal `I`, the inclusion of local rings `A` in its
normalization `B` satisfies

\[
A=B\times_{B/I} A/I.
\]

This is literal: a member of `B` whose residue modulo `I` lies in `A/I`
differs from a member of `A` by an element of the common ideal `I`, hence
lies in `A`. Sheafifying and tensoring by the invertible sheaf `O_X(2)` gives

\[
0\longrightarrow O_X(2)
\longrightarrow \nu_*O_S(2H)\oplus O_\Gamma(2)
\longrightarrow p_*O_D(2H)\longrightarrow0.
\]

The pair `(Q,qbar)` is compatible on `D`, so left exactness of global
sections produces a global section of `O_X(2)` whose pullback is `Q`.
There is no additional `H1` obstruction to this compatible-pair descent.
The hypersurface sequence

\[
0\longrightarrow O_{P^3}(-2)\longrightarrow O_{P^3}(2)
\longrightarrow O_X(2)\longrightarrow0
\]

and `H1(P3,O(-2))=0` lift that section to an ambient quadric `K`.

## The fixed-curve quadric obstruction

The pullback of `K|X` has zero support exactly `c`; finite surjectivity of
`nu` therefore says that the zero support of `K|X` is exactly `C0`. This
support argument avoids any need to exchange intersection multiplicities
between the two surfaces.

The fixed curve `C0=[u^4:u^3v:uv^3:v^4]` has the unique ambient quadric
`rt-pq=0`. Indeed the ten degree-two coordinate monomials give the nine
binary monomials of degree eight, with only `rt` and `pq` coinciding. This
quadric is smooth, and `C0` has ruling class `(1,3)`, up to swapping the
rulings.

The nonzero quartic restriction `F|K` is an effective divisor of class
`(4,4)` supported only on this integral curve. Its degree is eight, so it
must equal `2C0`. But subtracting that divisor class leaves

\[
(4,4)-2(1,3)=(2,-2),
\]

which has no nonzero section on `P1 x P1`. Equivalently `(4,4)` is not the
class `2(1,3)`. This contradiction proves the conditional all-mate exclusion.

Audit outcome: global descent, parity at ramification, the passage from the
Weil divisor to local squares along the smooth conductor, and the final
quadric obstruction are all valid with the hypotheses stated above. The
existence of `Q` and the actual smooth conductor conditions remain hypotheses
to establish for each proposed carrier family.


---

## Source: 2026-10-09-session-elliptic-conductor-quadratic-descent.md

# Quadratic descent across a smooth elliptic double conductor

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the exact
hypotheses below. This is a conditional geometric exclusion, not a
classification of singular quartic normalizations. The universal
STCI problem and the unrestricted fixed-C0 problem remain open.

## 1. Theorem with actual conductor schemes retained

Let k be an algebraically closed field of characteristic zero. Let
X be an integral quartic surface in P3, let nu:S->X be its finite
normalization, and set H=nu^*O_X(1). Suppose the following hold.

1. There is a smooth integral curve c on S whose image is the fixed
   rational quartic C0=[s^4:s^3t:st^3:t^4], and nu|c is an
   isomorphism onto C0.
2. There is a nonzero global section Q of O_S(2H) whose Weil divisor
   is exactly 2c.
3. The actual downstairs conductor scheme Gamma is a smooth conic.
   The actual upstairs conductor scheme D is a smooth integral
   projective curve of genus one, and D avoids Sing(S).
4. The induced map p:D->Gamma is finite flat of degree two.

Then X has no homogeneous set-theoretic mate for C0, in any positive
degree.

Here “actual conductor” means the closed schemes defined by the
conductor ideal I=Ann_OX(nu_*O_S/O_X), respectively I O_S. Smoothness
of their supports alone does not satisfy hypotheses 3 and 4. The
theorem permits c to pass through singularities of S away from D.
It imposes no parity condition on the degree of a hypothetical mate.

## 2. A mate gives the divisor and the squared power identity

Assume G is a homogeneous mate of degree b>0, so the zero support
of G on X is exactly C0. It is not identically zero on X. Thus
h=nu^*G is a nonzero section of O_S(bH).

The curve C0 is distinct from the conic Gamma. At its generic point
the normalization is therefore an isomorphism: off the conductor
the finite ring extension is an equality. Every curve component of
nu^{-1}(C0) dominates C0 because nu is finite. Hence c is the only
curve component above C0. Consequently the Weil divisor of h is
m c for an integer m>0. Any isolated off-c inverse-image point would
already contradict the zero support of this Cartier section; that
obstruction need not be assumed absent in advance.

The intersection degree with H gives

    b H^2 = m (H.c).

The finite birational quartic normalization has H^2=4, and
H.c=deg(C0)=4. Therefore m=b and

    div_S(h)=b c.

Both h^2 and Q^b are nonzero sections of the same line bundle
O_S(2bH), with identical Weil divisor 2b c. Their quotient is a
rational function with neither zeros nor poles in codimension one.
Normality makes it an invertible regular function on S, and
projectivity and integrality make it a constant. Thus

    h^2=lambda Q^b,        lambda in k^*.

This is why an assumption that b is even is unnecessary. Squaring
the mate gives a descended power of Q for every positive integer b.

## 3. Power invariance gives a global sign on the conductor

Put M=O_Gamma(1). Since H is pulled back from X,

    O_D(H)=p^*M,
    q=Q|D is a section of p^*(M^2).

The section q is nonzero: D is integral of genus one and is distinct
from the rational curve c, while div_S(Q)=2c. Let sigma be the
nontrivial involution of the finite flat double cover p. Its action
on p^*M^2 is the canonical action on a pulled-back line bundle.

The section h|D is pulled back from G|Gamma. Restricting the power
identity to D shows that q^b is invariant under sigma. In the
function field k(D), the ratio r=(sigma q)/q therefore satisfies
r^b=1. The polynomial T^b-1 splits into linear factors over k, and
k(D) is a field. Hence r is a constant root of unity zeta in k.
Applying sigma twice gives zeta^2=1, so

    sigma q=+q       or       sigma q=-q.

These are global equalities of sections, because they hold
generically on the integral curve D. There is no independent sign
choice at different points, and no unexamined pole stratum in this
step. Only the ratio in the function field is used; the equality of
regular sections extends over their zero sets automatically.

## 4. The minus sign contradicts even ramification valuations

The conic Gamma is isomorphic to P1. Riemann--Hurwitz for the smooth
genus-one degree-two cover gives

    0 = 2(-2)+deg(R),       deg(R)=4.

In characteristic zero a degree-two ramification index is two and
its different exponent is one. Thus there are four distinct simple
ramification points. In particular there is at least one such
point P.

At P choose a local frame of M^2 downstairs, and pull it back. This
frame is sigma invariant. In the completed local ring of the smooth
curve D choose a uniformizer w such that sigma(w)=-w. For example,
the trace-zero coordinate of a quadratic algebra is a uniformizer
at a simple ramification point; its square is a base uniformizer
times a unit. Write q=a(w) in the chosen pulled-back frame.

If sigma q=-q, then a(-w)=-a(w). Since a is a nonzero regular power
series and the characteristic is not two, its first nonzero term
has odd degree. Therefore ord_P(q) is odd.

On the other hand S is regular along D. At every P in D, the prime
curve c is locally Cartier, even if it is not Cartier at some point
outside D. Let f be a local equation of c where P lies on it. The
equality div_S(Q)=2c gives locally Q=u f^2 with u a unit, after a
local frame for O_S(2H). Restricting to D makes its vanishing order
twice the local intersection multiplicity of c and D. If P does not
lie on c, its vanishing order is zero. Thus every valuation of q
on D is even:

    div_D(q)=2(c.D).

Changing to the pulled-back frame multiplies the representing
function by a unit and does not change this valuation. The odd
valuation forced by anti-invariance is impossible. Consequently

    sigma q=q.

The argument needs regularity of S along the actual D. It does not
discard non-Cartier behavior of c at singular points away from D.

## 5. Descent through the entire conductor square

For a finite flat double cover in characteristic not two, the trace
splitting gives

    (p_*O_D)^sigma=O_Gamma.

This also follows locally by choosing a trace-zero basis element
z with z^2 in the base ring and sigma(z)=-z. The projection formula
therefore identifies invariant sections of p^*M^2 with sections of
M^2. Hence q=p^*qbar for a global section qbar of O_Gamma(2).

The actual conductor square is a fiber-product square, not merely
a generic gluing prescription. Locally, if A is the ring of X, B
its normalization and I their conductor, then

    A = B x_(B/I) (A/I).

Indeed an element of B whose residue belongs to A/I differs from
an element of A by an element of I, and I is contained in A.
Globally this gives the exact sequence

    0 -> O_X -> nu_*O_S direct_sum O_Gamma -> nu_*O_D -> 0,

where the last map subtracts the two restrictions. Tensoring with
the invertible sheaf O_X(2) preserves exactness. The compatible pair
(Q,qbar) therefore comes from a global section Q_X of O_X(2), with

    nu^*Q_X=Q.

There is no H^1 obstruction to this descent: exactness identifies
the kernel already on global sections. Compatibility has been proved
on all of the smooth actual conductor D, including the ramification
points, rather than only at its generic point.

Finally the hypersurface exact sequence

    0 -> O_P3(-2) -> O_P3(2) -> O_X(2) -> 0

and H^1(P3,O(-2))=0 lift Q_X to a homogeneous ambient quadric q_X.
The lift is nonzero since Q is nonzero.

## 6. The fixed-C0 quadric contradiction

The fixed curve C0 lies on exactly one quadric, up to scalar:

    Q0 = V(x0 x3-x1 x2).

This is immediate by restricting the ten degree-two monomials to
[s^4:s^3t:st^3:t^4]: nine resulting monomials are independent and
the only repeated monomial is x0x3=x1x2=s^4t^4. Thus q_X is a
nonzero scalar multiple of this smooth quadric's equation.

The pullback of q_X has divisor 2c, so its zero support on S is
exactly c. Finite surjectivity then makes its zero support on X
exactly C0. Therefore the quartic equation of X, restricted to the
smooth quadric Q0, has an effective divisor supported only on C0.
Its degree is eight, so that divisor must be 2C0.

Under Q0=P1xP1 the fixed C0 has divisor class (1,3), up to swapping
the rulings. One Segre parametrization is

    [s^3:t^3] x [s:t]
        |-> [s^4:s^3t:st^3:t^4].

The divisor cut by a quartic has class (4,4). But 2C0 has class
(2,6), so it cannot be that divisor. Equivalently a residual divisor
after subtracting 2C0 would have class (2,-2), which is not
effective. This contradiction excludes the hypothetical mate G.

## 7. Applicability and boundaries

The explicit four-A1 degree-four del Pezzo projection in
`research/notes/2026-10-09-session-dp4-projection-local-lift.md`
satisfies all four hypotheses: its actual downstairs conductor is
a smooth conic, upstairs it has a smooth elliptic double cover
avoiding the four A1 vertices, and the displayed global quadric has
divisor 2c. That carrier was already excluded by its explicit
nonsingleton fibers. This theorem supplies a second exclusion and
extends to every carrier for which the same hypotheses are proved.

The theorem does not prove that every singular-normalization
quartic has this conductor or the global section Q. It does not
cover nonreduced actual conductor schemes, a singular upstairs
conductor, an upstairs conductor passing through Sing(S), or the
absence of a global doubled-curve quadric. Those hypotheses must
not be inferred solely from the reduced support, a local divisor
class, or a model family containing the explicit example.

## 8. Independent audit and primary inputs

The separate audit is saved in
`research/notes/2026-10-09-session-elliptic-conductor-quadratic-descent-independent-audit.md`.
It accepts the power reduction without a degree parity assumption,
the odd/even valuation contradiction, complete conductor-square
descent, and the final smooth-quadric divisor-class contradiction.
Independent agreement is audit evidence; the proof is the argument
above. No finite symbolic calculation is substituted for this
conditional theorem.

The primary general inputs used here are the
[Stacks Project Riemann--Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B)
for the four simple ramification points, and
[Stacks Project cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS)
for the ambient quadratic lift. The conductor fiber-product equality,
sign reduction and parity obstruction are proved explicitly above.
No literature novelty claim is made.


---

## Source: 2026-10-09-session-genus-one-delpezzo-reduction.md

# Every genus-one quartic normalization containing C0 is a degree-four weak del Pezzo model

Date: 2026-10-09. Owner: root. Status: **PROVED HERE, independently
accepted in the bounded audit below**. This establishes the hypotheses
of the del Pezzo root-lattice reduction. It does not exclude every
genus-one normalization or supply a mate on any of them.

Let k be algebraically closed of characteristic zero. Let X in P3 be
an integral nonnormal quartic containing the smooth rational quartic
C0, let nu:S->X be its finite normalization, and let
H=nu*O_X(1). Suppose its normalization sectional genus is pi=1.
The proof does not require a mate.

The accepted [nonrational-normalization theorem](NONRATIONAL_QUARTIC_NORMALIZATION_PROOF.md)
shows that S is rational. Let sigma:M->S be its minimal smooth
resolution and L=sigma*H. Then L is a nef and big Cartier divisor,
L^2=4, and a general smooth hyperplane curve of class L has genus
one. Adjunction gives

    K_M.L=-4,       (K_M+L).L=0.

## 1. The adjoint has a unique effective representative

The smooth projective surface M is rational, so chi(O_M)=1.
Characteristic-zero Kawamata--Viehweg vanishing for the nef and big
L gives Hi(M,K_M+L)=0 for i>0. Surface Riemann--Roch therefore gives

    h0(M,K_M+L)=chi(K_M+L)
      =1+(K_M+L).L/2=1.

Choose the effective divisor D of that nonzero section. Thus
D~K_M+L and L.D=0. Since L is the pullback of an ample divisor
under sigma, any prime curve not contracted by sigma has positive
L-degree. Consequently every prime component of D is exceptional.
No rational-singularity or Gorenstein assumption on S was used here.

## 2. Minimality and negative definiteness force D=0

The exceptional intersection matrix of a resolution of a normal
surface is negative definite. Every exceptional integral prime E
therefore has E^2<0. Minimality excludes an exceptional smooth
rational curve of self-intersection -1, since it could be contracted
to give a smaller smooth resolution over S. Adjunction consequently
gives

    K_M.E=2 p_a(E)-2-E^2 >= 0.

Indeed, if p_a(E)=0 then E is a smooth rational curve, so E^2<=-2;
if p_a(E)>=1 then the displayed intersection is positive. Since
L.E=0, one also has D.E=K_M.E>=0 for every exceptional prime.
Writing the effective divisor as D=sum d_i E_i now gives

    D^2=sum d_i (D.E_i) >= 0.

This contradicts negative definiteness unless D=0. Hence the unique
adjoint section has no zeros and

    K_M~ -L,       K_M^2=4.

In particular M is a rational weak del Pezzo surface of degree four:
its anticanonical line bundle is nef and big. The curves contracted
by sigma have anticanonical degree zero.

## 3. The normalization is Gorenstein del Pezzo with ADE singularities

To make the crepant conclusion precise, choose an actual hyperplane
divisor H0 in |H|, whose pullback is L0 in |L|. The linear equivalence
K_M~ -L lets us choose a rational two-form omega on M with

    div_M(omega)=-L0.

Use the same rational two-form on S, which has the same function
field. Pushing its divisor forward gives the canonical Weil divisor

    K_S=div_S(omega)=-H0.

It is Cartier, and its negative is ample. Moreover these choices give
the actual equality of divisors

    K_M=sigma* K_S.

Thus sigma is crepant. The standard surface characterization of
Du Val singularities by a crepant resolution applies. The primary
author-hosted statement is [Miles Reid, The Du Val singularities,
Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
Accordingly S has only ADE singularities and is a normal Gorenstein
del Pezzo surface of degree four. This conclusion comes from the
adjoint argument; it is not an assumed classification hypothesis.
The usual characteristic-zero form of this surface result applies;
equivalently the finite coefficients and resolution data descend to
a finitely generated field that embeds in C, where Reid's stated
characterization applies, and the resulting intersection and crepant
properties transfer back.

## 4. Relation to a hypothetical mate and the root-lattice task

Under a mate of degree b, the accepted full-support theorem gives a
smooth lifted curve c isomorphic to C0 and b c~bH on S. Its strict
transform c# on M is also smooth. The Cartier pullback supplies an
effective rational exceptional correction Z with

    c#+Z numerically equivalent to L,       -Z^2=2 pi=2.

The previous [sectional-genus proof](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
establishes this identity without assuming that c is Cartier. On the
rational weak del Pezzo M, the integral class L-c# realizes Z in
the saturation of the exceptional root lattice inside the
anticanonical orthogonal lattice D5. Thus the forthcoming D5 torsion
filter is applicable to every remaining genus-one normalization,
once its own lattice proof is accepted. The classification of that
lattice filter and the exclusion of any surviving conductor types
are separate obligations.

The displayed [four-A1 family](OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd)
already realizes the order-two correction in an actual normalization,
then fails the full-fiber condition. It does not represent every
possible projection of a four-A1 surface. Genus-two rational
normalizations, higher carrier degrees, and entirely thick
presentations are outside this theorem.

## 5. Audit and source scope

The independent auditor `normal_global_adversarial` accepted the
KV/Riemann--Roch calculation, exceptional support, all exceptional
prime adjunction inequalities on the minimal resolution, negative
definiteness, and the chosen-canonical-form crepant equality before
this owner note was written. Its standalone audit is recorded in
the October 9 acceptance record once frozen. No new computational
test is needed for these divisor arguments. The source inputs are
the standard characteristic-zero nef-big vanishing theorem, surface
Riemann--Roch, negative definiteness on a normal-surface resolution,
and the explicitly linked Du Val characterization.


---

## Source: 2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md

# Independent audit of the two-quadric Hilbert-series conductor proof

Date: 2026-10-09. Auditor: `singular_local_lift`.
Status: **CONDITIONAL ALGEBRA ACCEPTED**. This audits root's
`research/notes/2026-10-09-session-genus-one-entire-conductor.md`
through its actual coordinate-ring and conductor route. It does not
rederive the result from finite duality, and does not certify the
separately assigned anticanonical embedding or lifted-curve spanning
application to the full genus-one lane. The universal STCI problem
and unrestricted C0 problem remain open.

## 1. Hypotheses used in the audit

The algebra acceptance requires the stated normal integral
nondegenerate complete intersection S of two quadrics in P4, a
projection from a center outside S, and a finite birational integral
quartic image X. Its equations are exactly

    Q1=z^2-Az-R1,       Q2=Lz+R,
    F=R^2+ALR-R1 L^2,
    T=k[x0,x1,x2,x3],       A_X=T/(F),
    B=T[z]/(Q1,Q2),       C=T/(L,R).

Here A,L have degree one, R1,R degree two, and L is nonzero.
The characteristic-zero hypothesis permits the trace-zero
coordinate z-A/2. The argument up to that change of coordinate
uses no characteristic-specific cancellation.

The normalization of the pencil is justified conditionally from
these geometric assumptions: a center outside S supplies a nonzero
z^2 coefficient in one quadric; cancel it from the other. If the
remaining z coefficient were zero, the quartic image would lie in
a nonzero quadric, which is impossible for an integral quartic
surface. Thus L is nonzero. This statement does not establish the
geometric assumptions in the first place.

## 2. The injection and the complete-intersection Hilbert series

On L!=0, the equation Q2 gives z=-R/L. Substitution into Q1 gives
the displayed F. This open is nonempty because S is nondegenerate
and L is a nonzero linear form. If F were the zero polynomial, the
equations on that open would leave a three-dimensional image,
contrary to S being a surface. F is therefore nonzero.

Since X is assumed to be an integral degree-four hypersurface, the
degree-four equation F vanishing on it is its irreducible equation
up to scalar. This proves the graded injection A_X->B. It must be
established before taking HS(B)-HS(A_X); root's proof does so.

B is the actual complete-intersection coordinate ring under the
hypotheses, so its Hilbert series is the two-quadric series. The
normality and complete-intersection assumptions also justify using
this ring for normalization: its affine cone is Cohen--Macaulay,
and regular in codimension one away from the vertex by normality
of S. The vertex has codimension three. Thus the coordinate ring
is normal; monic Q1 makes B finite over A_X and z=-R/L makes their
fraction fields equal.

## 3. L,R are a regular sequence and retain all conic schemes

If R=L T1 for a linear form T1, then Q2=L(z+T1). B is a domain,
so either L or z+T1 would vanish in B. Either outcome puts S in a
hyperplane, violating nondegeneracy. Hence R is nonzero modulo L.

T/(L) is a polynomial domain in three variables. Thus the nonzero
quadratic R mod L is a nonzerodivisor, and L,R are a regular
sequence. C is consequently the entire homogeneous coordinate
ring of a plane conic complete intersection. It may be reducible
or nonreduced, but it has no additional embedded component. F lies
in (L,R), so C=A_X/J for J=(L,R) in A_X.

## 4. The signs and the exact quotient module

The identities in B are

    Lz=-R,       Rz=AR-LR1.

For the second identity, multiply Q2 by z, replace z^2 by Az+R1,
and replace Lz by -R. The minus sign before LR1 is essential.
These identities show that J kills B/A_X. Monic Q1 makes B
generated by 1,z over A_X. Thus there is a surjection

    C(-1) -> B/A_X,       a |-> az mod A_X.

With the injection from Section 2 already established, the actual
complete-intersection Hilbert series give

    HS(B)=(1+t)^2/(1-t)^3,
    HS(A_X)=(1+t+t^2+t^3)/(1-t)^3,
    HS(C)=(1+t)/(1-t)^2,
    HS(B)-HS(A_X)=t HS(C).

The surjection has zero kernel in every graded degree, not merely
an eventually vanishing kernel. Therefore

    B/A_X isomorphic to C(-1).

As a supplementary literal sign check, reduce modulo the monic
Q1 in the free T-basis 1,z. The ideal generated by Q2 has relation
columns (R,L) and (LR1,AL+R), with determinant F. Subtracting A
times the first column from the second gives (LR1-AR,R), exactly
the second identity above. This is consistent with the Hilbert-series
quotient proof and does not change its scope.

## 5. Actual conductor, upstairs scheme, and trace

The conductor is Ann_A_X(B/A_X). The annihilator of C(-1) is
exactly J, since C=A_X/J. Hence the actual entire conductor ideal
is (L,R). Equality of Hilbert series before sheafification leaves
no hidden finite-length module at the affine cone vertex and no
discarded conductor scheme structure. Sheafification gives

    nu_*O_S/O_X=O_Gamma(-1).

In B, R=-Lz, so JB=(L). L is a nonzero element of the domain B;
the upstairs scheme D=V_S(L) is therefore the actual Cartier
hyperplane conductor, including through singular points of S.
Its coordinate ring is exactly

    B/JB=C[z]/(z^2-Az-R1).

This is free of rank two over C, with basis 1,z and graded shifts
zero and one. It therefore gives

    p_*O_D=O_Gamma direct_sum O_Gamma(-1)

as modules, and proves finite flat degree two on every point of
the actual conic, including the double line. The equation determines
the entire multiplication, not just a generic extension.

The trace is A on the generator z. The involution z->A-z preserves
the monic equation. In the coordinate w=z-A/2 it is w->-w, with
w^2=A^2/4+R1. This remains valid over nonreduced C. Root explicitly
does not infer a single global sign from powers on a reducible or
nonreduced D; that retained boundary is correct.

## 6. Fixed-C0 signs and the squarefree subcase

Under the separately stated RNC coordinate hypothesis, all six
displayed quadrics vanish on
[U^4:U^3V:UV^3:V^4:U^2V^2]. The normalized coefficient formulas
give the exact restrictions

    R_C=-z_c L_C,
    R1_C=z_c^2-A_C z_c,       z_c=U^2V^2.

The second restriction has the minus sign before A_C z_c. Thus
at L_C=0 the roots are z_c and A_C-z_c, as root states.

The assertion that a mate forces them to coincide is justified
conditionally: Gamma is a conic distinct from degree-four C0,
so normalization is an isomorphism at the generic point of C0.
c is the sole curve component above C0. A second isolated point
in a fiber off c cannot belong to the zero support of a nonzero
Cartier mate without another curve component. Hence such a point
prevents a mate.

L_C is a nonzero binary quartic with middle coefficient zero.
A_C-2z_c has middle coefficient -2. If L_C has four distinct
projective roots, the forced coincidence requires the latter
quartic to vanish at all four, making the two quartics proportional.
Their middle coefficients rule that out in characteristic zero.
This accepts only the squarefree subcase. Repeated-root strata and
the global power-descent problem remain unresolved by this audit.

## 7. Replay provenance and the missing requested root manifest

At the first read and a subsequent recheck on 2026-10-09, the
requested path
`validation/2026-10-09-genus-one-conductor/root-replay/execution-manifest.json`
did not exist in this checkout. This audit does not claim to have
verified that intended root replay or infer whether some separately
running root tool is active. Its absence does not obstruct the
conditional mathematical audit.

I made a separate frozen-source bounded replay in
`validation/2026-10-09-genus-one-conductor-algebra-independent/`.
It began at 2026-10-09T18:23:13.649396+00:00 and returned exit 0,
`status: PASS`, with 17 literal symbolic checks. The original and
frozen source hashes matched after execution:

    19e0c6bcb1db999dc95c8a640463ecd722ced43b0694037fe20835bb112ebd2f.

The output SHA256 was

    700e0ac83877a4b9aa20f7de6505485fc5bdb6191bc108d78427ef5dbd1c4f52.

The independent execution manifest is
`validation/2026-10-09-genus-one-conductor-algebra-independent/execution-manifest.json`.
It records the frozen source, exact runtime, cwd, output and both
terminal stream hashes. No external scratch input is used by this
checker. Passing identities corroborate the displayed algebra;
they do not verify the geometric hypotheses or supply parameter
coverage for the application.

## 8. Acceptance boundary

Accepted: the conditional CI-projection algebra, regular-sequence
argument, exact quotient and actual conductor ideal, full upstairs
quadratic algebra, trace involution, and fixed-C0 restriction signs.
The squarefree-L necessary-condition exclusion is also accepted
under its stated RNC coordinate hypothesis.

Not audited here: the anticanonical CI embedding of every surface
in the proposed genus-one lane, projective spanning of every lifted
c needed to choose these RNC coordinates, the entire repeated-root
parameter space, or the doubled-curve power-descent obstruction.
Those separate application claims must not be certified by this
conditional algebra acceptance.


---

## Source: 2026-10-09-session-genus-two-adjoint-conic-model.md

# The genus-two adjoint conic model and its bounded exceptional locus

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE**. Sections 1--2 are independently accepted in
the [adjoint audit](#source-2026-10-09-session-genus-two-adjoint-independent-auditmd)
and its [degree-one counteraudit](#source-2026-10-09-session-genus-two-degree-one-counterauditmd).
Sections 4--5 and 7 are independently accepted in the
[null-curve and mate-strata audit](#source-2026-10-09-session-genus-two-nullcurve-mate-independent-auditmd).
Sections 3, 6 and 8 are supplied for a final bounded audit. This is a
structural reduction; neither the genus-two mate lane nor the
unrestricted STCI problem is excluded here.

Work over an algebraically closed field of characteristic zero. Let
X in P3 be an integral nonnormal quartic containing a smooth rational
degree-four curve C0. Let nu:S->X be its finite normalization,
sigma:M->S its minimal smooth resolution, H=nu*O_X(1), and L=sigma*H.
Assume normalization sectional genus pi=2.

The accepted [rationality theorem](NONRATIONAL_QUARTIC_NORMALIZATION_PROOF.md)
gives rational M, without a mate hypothesis. The basic data are

    L nef, big and globally generated,
    L^2=4,       K_M.L=-2,       chi(O_M)=1,
    h0(M,L)=h0(S,H)=4.

The four actual ambient sections span this complete space; the
complete |L| morphism has the actual quartic X as its image and is
birational. An integral prime E has L.E=0 exactly when it is
sigma-exceptional. Minimality forbids an exceptional smooth rational
(-1) curve, but does not forbid (-1) curves with positive L-degree.
No conductor classification or ADE hypothesis is assumed.

## 1. The adjoint is nef and has square zero

Set A=K_M+L. Nef-big Kawamata--Viehweg vanishing and Riemann--Roch give

    h0(M,A)=1+(A.L)/2=2,       A.L=2.

If A.E<0 for an integral prime E, effectiveness makes E a fixed
component and forces E^2<0. Adjunction gives

    K_M.E=2p_a(E)-2-E^2.

This is nonnegative for p_a(E)>=1 or E^2<=-2. The remaining case is
a smooth rational (-1) curve, and minimality then gives L.E>=1,
so A.E=-1+L.E>=0. Hence A is nef. Its square is

    A^2=K_M^2,

and Hodge index against L gives 0<=A^2<=1.

If A^2=1, the class T=L+2K_M is numerically zero: T.L=0 and T^2=0,
and L-perp is negative definite. A numerically trivial divisor N
on this rational M is linearly trivial by the following useful
direct argument. Riemann--Roch gives chi(N)=1; Serre duality gives
h2(N)=h0(K_M-N)=0 because (K_M-N).L=-2. Thus N has a nonzero section.
Its zero divisor is effective and numerically zero, hence zero by
intersection with an ample class. In particular T~0 and L~2A.

Two independent sections u,v of A give three independent square
sections u^2,uv,v^2 of L. Independence follows from the nonconstant
rational function u/v. Completing them to a basis of h0(L)=4 puts
the |L| image in the nonzero quadric X0 X2-X1^2=0, contrary to its
being an integral quartic hypersurface. Therefore

    A^2=K_M^2=0.

The independent degree-one counteraudit verifies this exact
contradiction. An anticanonical classification theorem is not needed.

## 2. The entire adjoint system is a rational pencil without base points

Write |A|=|P|+D, where D is fixed and |P| has no fixed curve.
Then h0(P)=2. Nefness of A gives A.P=A.D=0. Two general members of
|P| have no common curve, hence P^2>=0. Subtracting the appropriate
rational multiple of A makes P orthogonal to L; Hodge index then
gives P^2<=0. Thus P^2=0 and P is numerically proportional to A.
Any base point would give a positive local intersection multiplicity
between two general members, so |P| has no base points.

The associated map to P1 has connected fibers. Its Stein base is P1
because M is rational. If its finite map to the original target had
degree d, then h0(P)=h0(P1,O(d))=d+1, so d=1. A general fiber F is
smooth and integral. Since K_M=A-L and A.P=0,

    2g(F)-2=K_M.P=-L.P<0.

Therefore F is P1 and L.P=2. Comparing with L.A=2 shows P is
numerically equivalent to A; the effective fixed part D is
numerically zero and is therefore zero. Consequently

    f:=K_M+L,       |f| is a basepoint-free connected rational pencil,
    f^2=0,         L.f=2,       K_M.f=-2.

The general fiber is mapped by the actual complete |L| isomorphically
onto a smooth plane conic in X. Its degree-two line bundle uses at
most three independent sections. A two-dimensional subspace would
give a degree-two map onto a line, contradicting birationality on
the general fiber. Thus all three sections of O_P1(2) occur.

This fibration is on M. It need not descend as a morphism to S,
because some curves contracted by sigma can be horizontal for it.

## 3. A marked eight-blowup ruled model

Contract vertical (-1) curves until the smooth rational fibration
is a relatively minimal ruled surface F_n. A smooth relatively
minimal P1 fibration over P1 is a P1 bundle, so this is a Hirzebruch
surface. The resulting factorization M->F_n consists of point
blowups, including possibly infinitely near centers. Since K_M^2=0
and K_Fn^2=8, there are exactly eight point blowups.

Write C_min^2=-n and C_min.f=1 on F_n, and use total transforms
e1,...,e8 for the blowup classes. Every contracted vertical (-1)
curve E has f.E=0, K.E=-1, and therefore

    L.E=(f-K).E=1.

At each contraction the pushed-down L remains nef; intersecting
strict transforms proves this directly, as in the rationality note.
The canonical blowup formula therefore gives the actual marked class

    L=2C_min+(n+3)f-sum_{i=1}^8 e_i.

On F_n the pushed-down L has intersection 3-n with C_min. Nefness
forces

    0<=n<=3.

All multiplicities are one in this total-transform marking. This
does not mean that all eight centers are distinct points of F_n.
For a direct numerical control, the pushed-down class has square
twelve and canonical intersection minus ten; subtracting the eight
blowup classes gives L^2=4 and K_M.L=-2 as required.

This model uses only the adjoint fibration. It does not assert that
the normalization is itself the strict transform of X in a blowup
of an ambient line, or that the original conductor is a reduced line.

## 4. All contracted prime curves have tightly bounded types

Let E be any integral sigma-exceptional prime. Put

    d=f.E=K_M.E>=0,
    Q=K_M+L/2.

The inequality d>=0 follows from nefness of f. The projection Q
lies in L-perp and has square -1. Since L-perp is negative definite,
Cauchy--Schwarz there gives

    d^2=(Q.E)^2<=-E^2.

Adjunction gives

    -E^2=d+2-2p_a(E),
    d^2<=d+2-2p_a(E).

If d=0, the negative square forces p_a(E)=0 and E^2=-2. Thus every
vertical contracted prime is a smooth rational (-2) curve.

If d>0, the inequality leaves only d=1 or d=2. For d=1 the map
E->P1 induced by f has degree one. It is finite birational, and the
target P1 is normal, so it is an isomorphism. Hence E is a smooth
rational section and E^2=-3.

For d=2 the inequality forces p_a(E)=0 and E^2=-4. Equality in
Cauchy--Schwarz gives E numerically equivalent to -2Q=-2K_M-L.
The numerical-to-linear argument of section 1 gives

    E~ -2K_M-L,       L~2f+E.

Multiplying three independent sections u^2,uv,v^2 of 2f by the
nonzero section of E gives three independent sections of L with
the same quadric relation. This contradicts the actual quartic
image. Thus the (-4) bisection cannot occur.

**Conclusion.** Every contracted prime is either a vertical smooth
(-2) curve or a horizontal smooth (-3) section. No positive-genus
exceptional prime has been omitted by an ADE assumption.

## 5. There are at most two horizontal curves, and they are disjoint

For two distinct horizontal (-3) sections E1,E2 put t=E1.E2>=0.
For T=E1+E2, one has K_M.T=2 and T^2=-6+2t. Cauchy--Schwarz on
L-perp gives 4<=6-2t, so t<=1.

If t=1, equality gives T numerically equivalent to -2Q, hence
T~-2K_M-L and L~2f+T. The effective divisor T gives the same
three-section quadric contradiction as section 4. Therefore t=0:
two such sections are disjoint.

Suppose three such curves existed. For their sum T, pairwise
disjointness gives T^2=-9 and K_M.T=3. Cauchy equality gives

    T equivalent to -3Q,       2T~-6K_M-3L.

The upgrade to the displayed linear equivalence uses the same
numerically-trivial-divisor argument. It implies L=2B in Pic(M),
with the explicit integral class B=-3K_M-T-L. Then

    B^2=1,       K_M.B=-1.

Riemann--Roch gives chi(B)=2. Also h2(B)=h0(K_M-B)=0 because its
L-degree is negative. Hence h0(B)>=2, and the square sections of
two independent sections of B again put the |L| image in a quadric.
This contradiction proves that there are at most two horizontal
(-3) sections.

They can still meet vertical (-2) curves in their exceptional fiber.
No claim that all singularities of S are ADE is made.

## 6. The vertical root lattice is the explicit D8 lattice

In the marked ruled model of section 3, a Picard class orthogonal
to both f and L has the form

    v=b f-sum_i d_i e_i,       2b=sum_i d_i.

Its square is -sum_i d_i^2. Thus the integral lattice

    f-perp intersect L-perp

is the negative D8 lattice: integer vectors (d1,...,d8) with even
coordinate sum. Its roots are the 112 vectors +/-u_i+/-u_j, bound
geometrically to

    +/- (e_i-e_j),       +/- (f-e_i-e_j).

Every vertical contracted (-2) curve is one of these roots. The
negative definite lattice of all vertical exceptional primes is
therefore an embedded root subsystem of D8, and its total rank is
at most eight. The signed-coordinate argument from the
[D5 filter](OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd) applies
to root sublattices here as well: coordinate-connected components
are A or D, including D2=2A1 and D3=A3. This is an exact lattice
identification, not a claim that every embedded D8 configuration
is geometrically realized in the given conic model.

If there are no horizontal exceptional curves, every exceptional
prime is (-2) and the canonical divisor is crepant on the minimal
resolution; the standard Du Val criterion then gives ADE singularities
of S. With horizontal sections present that inference is unavailable.

## 7. A mate retains two correction strata, not just the ADE one

Now add a hypothetical mate. Its full support supplies a smooth
embedded c=P1 on S and an effective rational exceptional correction Z,

    c# + Z equivalent to L,       Z=sum_i a_i E_i,       a_i>=0.

The class Z=L-c# is integral, although its coefficients in the
exceptional basis may be fractional. Put

    q=-Z^2>0,       lambda=K_M.Z.

The general adjunction identity from the sectional-genus record is

    q+lambda=2pi=4.

Since K_M.E is zero on every vertical prime and one on each
horizontal (-3) section,

    lambda=sum of the horizontal correction coefficients.

It is a nonnegative integer, because K_M and Z are integral classes.
Cauchy--Schwarz with Q in section 4 gives

    lambda^2<=q=4-lambda.

Therefore exactly two necessary numerical strata remain:

| lambda | q | c#^2 | f.c# | Type of lifted rational curve on M |
| --- | --- | --- | --- | --- |
| 0 | 4 | 0 | 2 | Bisection |
| 1 | 3 | 1 | 1 | Section |

The lambda=1 stratum must not be discarded by setting Z^2=-4 in
advance. That equality presupposes K_M.Z=0, which is automatic in
the ADE lane but has not been established in the non-ADE lane.
An attempted audit shortcut making that substitution was corrected
before acceptance. Effectiveness alone permits lambda=1.

In the lambda=0 stratum, Z has zero coefficient on all horizontal
sections. It is supported on vertical (-2) components and belongs
to D8. For a horizontal section E, positivity gives Z.E>=0 while
the mate gives Z.E=-c#.E<=0. Consequently Z.E=c#.E=0. Thus both
the correction support and c# avoid the horizontal sections in this
stratum. This avoidance is conditional on lambda=0.

As in the D5 proof, Z is not in the integral exceptional lattice R:
otherwise c~H downstairs would be Cartier, so embedded smoothness
forces c to avoid Sing(S), and negative definiteness then forces
Z=0. Under a degree-b mate, bZ belongs to R. Determining which
D8 root sublattices and exceptional configurations can contain the
required missing norm-four or norm-three class remains open here.

## 8. The two strata have concrete moving systems

In the lambda=0 stratum, the smooth P1 c# has square zero. The
restriction sequence

    0 -> O_M -> O_M(c#) -> O_c#(c#) -> 0

and H1(O_M)=0 give h0(c#)=2. The system is basepoint free: its
restriction to c# is O_P1, and the canonical section is nonzero
away from c#. Thus c# is a fiber of a second rational pencil.
The two rational pencils have fiber intersection f.c#=2.

In the lambda=1 stratum, c#^2=1. The same sequence restricts to
O_P1(1), gives h0(c#)=3, and proves basepoint freeness. The complete
|c#| map has two-dimensional image in P2 and generic degree one,
because c#^2=1. It is therefore a birational morphism M->P2.
As K_M^2=0, it consists of nine point blowups.

Mark c# by the pullback h of a line and the nine total exceptional
classes e0,...,e8. The nef class L has the form

    L=4h-sum_{i=0}^8 m_i e_i,       m_i>=0.

Nefness of its successive pushdowns ensures these nonnegative
integer multiplicities, including infinitely near centers. The
two intersection identities give

    sum_i m_i=10,       sum_i m_i^2=12,
    sum_i m_i(m_i-1)=2.

Exactly one m_i is two and the other eight are one. Renaming the
double center e0, the actual marked classes are

    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K_M+L=h-e0,
    c#=h,
    Z=L-c#=3h-2e0-sum_{i=1}^8 e_i.

This is a stronger marked reduction for the retained lambda=1
mate stratum. It does not show that the effective rational
exceptional representative of Z has integral coefficients, nor
that it descends to a mate on X. In particular the smooth lifted
curve and its singleton normalization fibers remain necessary
conditions in addition to these marked identities.

## 9. Relationship with a double-line blowup, retaining its hypotheses

For comparison only, if an actual carrier X has a line ell of
generic multiplicity two, put B=Bl_ell(P3), with pulled-back
hyperplane H_B and exceptional divisor E_B. Its strict transform is

    T~4H_B-2E_B=2H_B+2f_B,       f_B=H_B-E_B.

When T is normal, adjunction gives K_T=-E_B|T. The exceptional
intersection is a (2,2) scheme in E_B=P1 times P1, with arithmetic
genus one. The numerical identities are H_B^2|T=4,
H_B.E_B|T=2, and (E_B|T)^2=0. This is consistent with the adjoint
model, but it is a conditional ambient realization.

[Dolgachev, Monoidal and submonoidal surfaces, and Cremona transformations](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/monoidal.pdf),
section 3, explicitly imposes conditions before identifying the
normalization with this strict transform. Definition 3.6 retains
that identification, discriminant multiplicity bounds and smoothness
of the small discriminant; Proposition 3.7 gives the resulting
normalization geometry. Its nondegenerate model must not be used
as coverage of arbitrary genus-two normalizations. Sections 1--8
above do not use those extra hypotheses or an asserted reduced
downstairs conductor line.

## 10. Continuation-ready boundary

The intrinsic adjoint argument produces a connected rational conic
fibration, K_M^2=0, an explicit eight-blowup ruled marking, and a
bounded exceptional locus: vertical D8 roots and at most two
disjoint horizontal (-3) sections. For a mate it retains exactly
the two numerical correction strata of section 7, and section 8
gives a concrete marked plane model in the non-ADE stratum.

The next finite task is to classify smooth-lift correction vectors
in these exceptional configurations. Downstairs smoothness is stronger
than smoothness of c# alone; for example meeting multiple exceptional
branches or tangency to an exceptional prime may prevent a uniformizer
of c from descending. A necessary local condition must be proved
before it is used as a lattice exhaustion. The actual conductor,
full inverse-image support, and descent of sections to the original
quartic remain separate obligations.

No exhaustive genus-two mate exclusion, no conductor purity theorem,
and no universal STCI conclusion is claimed. No canonical frontier
file has been edited by this owner.


---

## Source: 2026-10-09-session-genus-two-adjoint-independent-audit.md

# Independent audit: the genus-two adjoint pencil is a rational conic fibration

Date: 2026-10-09. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted as a structural reduction**.
This note audits the proposed genus-two reduction of
`delpezzo_d5_torsion_filter`. It does not classify every singular
normalization or exclude mates in this lane. No canonical frontier
file was edited.

Work over an algebraically closed field of characteristic zero. Let
X in P3 be an integral nonnormal quartic containing a smooth rational
degree-four curve C. Let nu:S->X be its finite normalization,
sigma:M->S its minimal smooth resolution, H=nu^*O_X(1), and
L=sigma^*H. Assume that a general curve of class L has genus two.
Then the entire complete adjoint system

    |K_M+L|

is a basepoint-free pencil with connected general fiber a smooth
rational curve F and L.F=2. The complete |L| morphism maps its general
fiber isomorphically to a plane conic in the actual quartic X. The
assertion is about the smooth resolution M; it does not assert that
the fibration descends to S or that S has rational or ADE
singularities.

## 1. Inputs and the exact scope of minimality

The accepted [nonrational-normalization audit](2026-10-09-session-nonrational-normalization-independent-audit.md)
establishes that M is rational without requiring a mate. The general
plane-section and pullback calculations give

    L nef, big, and globally generated,
    L^2=4,     K_M.L=-2,     chi(O_M)=1,     h0(M,L)=4.

The four pulled-back ambient sections span all of H0(M,L), so the
complete |L| map is sigma followed by the actual finite birational
normalization map nu. Its image is the given integral quartic X,
not a projection chosen after the calculation.

For an integral prime E on M,

    L.E=0  if and only if E is sigma-exceptional.

Indeed H is ample on S. Minimality of sigma excludes an exceptional
smooth rational (-1)-curve. It does not exclude (-1)-curves with
positive L-degree, which will be treated explicitly below. No
assumption about rational singularities of S is used.

## 2. The adjoint is effective and nef

Put A=K_M+L. Characteristic-zero Kawamata--Viehweg vanishing for the
nef and big L gives H^i(M,A)=0 for i>0. Surface Riemann--Roch yields

    h0(M,A)=1+(A.L)/2=2,     A.L=2.

Suppose that A.E<0 for an integral prime E. Since A is effective,
E occurs in every effective member of |A|. Choose one such member
and write it nE+B, with n>0 and E not a component of B. Distinct
effective curves have nonnegative intersection, so

    0>A.E=nE^2+B.E

forces E^2<0. Adjunction, valid also for an integral possibly
singular curve on the smooth M, gives

    K_M.E=2p_a(E)-2-E^2.

If p_a(E)>=1 this is positive. If p_a(E)=0, E is a smooth rational
curve, and E^2<=-2 gives K_M.E>=0. The only remaining possibility
is a smooth rational (-1)-curve. If its L-degree were zero it would
be exceptional, contradicting minimality. Therefore L.E>=1 and

    A.E=K_M.E+L.E=-1+L.E>=0.

Every case contradicts A.E<0. Thus A is nef. In particular

    A^2=K_M^2+2K_M.L+L^2=K_M^2>=0.

Hodge index applied to L gives

    (A.L)^2 >= A^2 L^2,

so 0<=A^2<=1. Its square is an integer, hence A^2 is zero or one.

## 3. Square one would put the image in a quadric

Assume A^2=1. Set N=L-2A=-L-2K_M. Then

    N.L=0,     N^2=0.

Since L^2>0, Hodge index is negative definite on its numerical
orthogonal complement. Thus N is numerically zero. We upgrade this
to linear equivalence directly, avoiding any shorthand inference
from torsion-freeness of the Picard group.

Let T=L+2K_M=-N. Riemann--Roch gives chi(T)=1 because T is
numerically trivial and chi(O_M)=1. Serre duality gives

    h2(T)=h0(K_M-T)=0:

an effective representative of K_M-T would have negative
L-intersection -2, impossible for nef L. Hence
h0(T)=1+h1(T)>=1. A nonzero section has an effective divisor
numerically equivalent to zero; intersection with any ample
divisor forces that divisor to be zero. Therefore T~0 and

    L~ -2K_M,     A~ -K_M.

There are two independent sections u,v of A since h0(A)=2. The
three sections u^2,uv,v^2 of 2A=L are linearly independent: on the
open where v is nonzero, a dependence would make u/v algebraic
over the algebraically closed field k, hence constant, contradicting
the independence of u and v. Complete these sections to a basis
of the four-dimensional H0(L). In the resulting coordinates the
complete |L| image satisfies the nonzero equation

    X0 X2-X1^2=0.

An integral two-dimensional quartic in P3 cannot be contained in
a quadric: its homogeneous prime ideal is generated by its
irreducible degree-four hypersurface equation. This contradicts
the actual image being X. The square-one case is excluded.

This bounded argument was counteraudited independently by
`degree_one_anticanonical_counteraudit`; its
[separate note](#source-2026-10-09-session-genus-two-degree-one-counterauditmd)
also checks the numerical-to-linear upgrade and the independence
of the square sections. Consequently

    A^2=K_M^2=0.

## 4. The adjoint has no fixed divisor and no base points

Write the complete system as |A|=|P|+D, with D its fixed effective
divisor and |P| having no fixed curve. Multiplication by the fixed
section gives h0(P)=h0(A)=2. Nefness of A and A^2=0 give

    A.P=A.D=0.

Two general distinct members of |P| have no common curve, so P^2
is the sum of their nonnegative local intersection multiplicities.
Thus P^2>=0. Put lambda=(P.L)/(A.L) and N0=P-lambda A.
Then N0.L=0 and, since A.P=A^2=0,

    N0^2=P^2.

Hodge index for the positive-square L gives P^2<=0. Therefore
P^2=0 and N0 is numerically zero; in particular P is numerically
proportional to A. Every base point of |P| would give a positive
intersection multiplicity to the two general members. Hence
|P| has no base points and defines a morphism g:M->P1.

Take its Stein factorization M->B->P1. The normal projective curve
B is smooth, and H1(O_B) injects into H1(O_M)=0 because the first
map has connected fibers and direct image O_B. Thus B is P1. If
the finite map B->P1 has degree d, then P is the pullback of
O_B(d). Connected fibers and the projection formula give

    h0(P)=h0(P1,O(d))=d+1.

As h0(P)=2, d=1. The original g therefore has connected fibers,
and P is the class of one fiber, not a multiple fiber class used
as a composite pencil. A general fiber F is smooth and integral
in characteristic zero; generic smoothness and connectedness
suffice here.

Since A.P=0 and K_M=A-L, adjunction gives

    2g(F)-2=K_M.P=-L.P<0.

The strict inequality holds because P is a nonzero effective
moving class: it cannot have zero degree against the nef and big
L, as Hodge index and P^2=0 would make P numerically zero. Thus
g(F)=0 and L.P=2. Since A.L=2, the numerical proportionality is
P equivalent to A, and D is numerically zero. An effective
numerically-zero divisor is zero by ample intersection. Hence

    D=0,     A~P,     |K_M+L|=|F|.

This handles fixed exceptional components and infinitely near
points without selecting a particular blowup model.

## 5. The general fiber is an actual plane conic

The restriction of L to F=P1 has degree two and is globally
generated. Its induced map into P3 comes from a subspace of
H0(P1,O(2)), of dimension at most three. It cannot have dimension
one, because L.F>0 and the |L| morphism does not contract F.
If its dimension were two, F would map with degree two onto a
line. The surface morphism is birational and is an isomorphism
on a dense open of M, so its restriction to the general fiber
is generically one-to-one. The degree-two line map is impossible.
The restriction therefore uses all three sections of O(2) and
embeds the general F as a smooth plane conic in the actual X.

## 6. Accepted reduction and unresolved obligations

The proposed adjoint reduction passes independently, including
all fixed-part, relative-minimality, and numerical-to-linear
issues. No smoothness or ADE conclusion for S was inferred.
In particular a sigma-exceptional curve may be horizontal for
the adjoint ruling, so this proof does not by itself descend
the ruling to S. Identifying exceptional configurations, the
entire conductor, full normalization fibers above C, and descent
of a hypothetical mate remain separate obligations.

The argument applies to every rational genus-two normalized
quartic model satisfying the stated complete birational |L|
hypotheses, with no mate required. The prior accepted rationality
theorem establishes these hypotheses for an integral nonnormal
quartic containing any smooth rational degree-four curve. The
unrestricted C0 and universal STCI problems remain open.

Source scope: the vanishing input is the same primary
[Hacon characteristic-zero nef-big vanishing account](https://www.math.utah.edu/~hacon/Kyoto2016talks.pdf)
already checked in the rational and genus-one audits. The
remaining tools are surface Riemann--Roch, Serre duality,
adjunction, Hodge index, intersection positivity on a smooth
surface, Stein factorization, and generic smoothness. The
degree-one and fixed-part conclusions above are proved here
rather than imported from an ample-polarization classification.
[Lanteri and Mallavibarrena, Rational conic fibrations of sectional genus two](https://arxiv.org/abs/2005.11415)
is a relevant primary classification reference, but its ample
polarization hypotheses are not substituted for the nef
pullback hypothesis needed here.


---

## Source: 2026-10-09-session-genus-two-degree-one-counteraudit.md

# Bounded counteraudit: the genus-two adjoint square-one case is impossible

Date: 2026-10-09. Owner: degree-one-anticanonical counteraudit agent.
Status: **PROVED HERE; accepted bounded argument**. This note excludes
only the square-one adjoint configuration specified below. It does not
establish the nefness of an adjoint in any broader normalization problem.

Let k be algebraically closed of characteristic zero, let M be a smooth
rational projective surface, and write K=K_M. Let L be a nef, globally
generated, big Cartier divisor satisfying

    L^2=4,       K.L=-2,       h0(M,L)=4.

Assume that the complete morphism phi_|L|:M->P3 is birational onto an
integral degree-four surface. Put A=K+L. The configuration A^2=1 is
impossible. The stated additional assumption that A is nef is allowed
but is not needed for this bounded exclusion.

## 1. Hodge equality gives L numerically equivalent to -2K

We have A.L=K.L+L^2=2. Set D=L-2A. Then

    D.L=4-2(2)=0,
    D^2=4-4(2)+4(1)=0.

The Hodge index theorem says that the orthogonal complement of the
positive-square class L in the real numerical divisor space is negative
definite. Thus D is numerically zero. Consequently

    L numerically equivalent to -2K,
    A numerically equivalent to -K,
    K^2=A^2-2K.L-L^2=1.

The first displayed conclusion uses L=2(K+L) numerically, rearranged
to L numerically equivalent to -2K.

## 2. Riemann--Roch upgrades the numerical equality to linear equivalence

The usual rational-surface facts imply that numerical and linear
equivalence coincide. However, the bare statement that Pic(M) is
torsionfree does not by itself prove this: the numerical kernel must
also be addressed. The following direct proof avoids that shortcut.

Put N=L+2K, which is numerically trivial by Step 1. Rationality gives
chi(O_M)=1. Surface Riemann--Roch and Serre duality give

    chi(O_M(N))=1+N.(N-K)/2=1,
    h2(M,N)=h0(M,K-N).

An effective divisor in the class K-N would have intersection
(K-N).L=K.L=-2 with the nef divisor L, which is impossible. Hence
h2(M,N)=0 and h0(M,N)=1+h1(M,N)>=1. Choose a nonzero section of
O_M(N), with effective zero divisor E. Since E is numerically trivial,
E.H=0 for any ample divisor H. A nonzero effective divisor has strictly
positive intersection with an ample divisor, so E=0. This nowhere-zero
section trivializes O_M(N). Therefore

    L linearly equivalent to -2K,
    A linearly equivalent to -K.

In particular -K is nef and big with (-K)^2=1. These conclusions follow
from numerical equivalence to L/2; no anticanonical classification is
being assumed.

## 3. The anticanonical system has exactly two sections

Apply characteristic-zero Kawamata--Viehweg vanishing to the nef and
big Cartier divisor L. It gives

    Hi(M,K+L)=0 for every i>0.

The precise primary-source statement used here is [Osamu Fujino,
Kawamata--Viehweg vanishing theorem, Theorem 0.1](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf), applied
with the morphism to a point and integral D=L. Its fractional part is
zero, so the normal-crossings condition is automatic.

Since K+L is linearly equivalent to -K, Riemann--Roch gives

    h0(M,-K)=chi(O_M(-K))
      =1+(-K).(-2K)/2=1+K^2=2.

This is the only vanishing-theorem use in the argument. It makes no
assumption that |-K| is free of base points or fixed divisors.

## 4. Two independent sections force a quadratic equation for the image

Let s,t be a basis of H0(M,-K). At the generic point, the ratio f=s/t
is an element of k(M). It is nonconstant: otherwise s and t would be
linearly dependent. Because k is algebraically closed, every element
of k(M) algebraic over k lies in k. Therefore f is transcendental over
k.

If a s^2+b st+c t^2=0 as a section of O_M(-2K), division by t^2 at
the generic point gives

    a f^2+b f+c=0.

Transcendence forces a=b=c=0. Thus s^2,st,t^2 are linearly independent
sections of O_M(-2K). Choose the isomorphism O_M(-2K)=O_M(L) supplied
by Step 2 and extend these three sections to a basis

    (s^2, st, t^2, u)

of H0(M,L), which has dimension four by hypothesis. In the corresponding
coordinates of P3, the complete morphism satisfies

    X0 X2-X1^2=0,

because (s^2)(t^2)=(st)^2 as sections of O_M(2L). This is a nonzero
homogeneous polynomial of degree two.

The calculation at the generic point is valid even if s and t have
a common fixed divisor or base points. At a common zero of s and t,
the three product coordinates vanish; global generation of L makes
u nonzero there, and the morphism sends the point to the quadric
vertex [0:0:0:1]. There is therefore no undefined evaluation or
fixed-component exception to the quadratic equation.

An integral degree-four surface in P3 has a principal homogeneous
ideal generated by an irreducible polynomial of degree four. It cannot
be contained in the zero set of a nonzero quadratic polynomial. This
contradicts the assumed image. Equivalently, the image is the quadric
cone and the degree formula L^2=deg(phi) deg(image) forces deg(phi)=2,
contradicting birationality.

## 5. Audit boundaries and characteristic

All steps above are accepted under the stated characteristic-zero
hypotheses. Rationality was used for chi(O_M)=1, and the direct
Riemann--Roch argument gives the required numerical-to-linear upgrade.
Neither a weak del Pezzo classification nor a base-point-free
anticanonical pencil is required.

The square-product independence and the quadratic identity work over
an algebraically closed field in every characteristic. The exact
equality h0(-K)=2 above uses characteristic-zero vanishing. For the
contradiction itself, even that equality can be weakened: Riemann--Roch
and h2(-K)=h0(2K)=0, since 2K.L=-4, already give h0(-K)>=2. Together
with h0(L)=4, any independent pair supplies the same quadratic
equation. Thus no positive-characteristic conclusion about exact
anticanonical cohomology is being inferred from Kawamata--Viehweg.

The square-product lemma was also checked independently by a separate
bounded algebraic audit. That agreement is an audit record; the proof
is the explicit generic-point argument in Step 4.


---

## Source: 2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md

# Independent audit: exceptional curves and the two genus-two mate strata

Date: 2026-10-09. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted as bounded structural
reductions**. This extends the [independent adjoint audit](#source-2026-10-09-session-genus-two-adjoint-independent-auditmd).
No canonical frontier file was edited. The genus-two mate problem
remains open.

Keep the characteristic-zero hypotheses and notation of that audit.
Thus M is a smooth rational minimal resolution of the normal
quartic normalization S, L is the pulled-back ample hyperplane,
L^2=4, K.L=-2, K^2=0, h0(L)=4, and

    f=K+L

is the class of a connected rational conic-fibration fiber. Its
complete |L| map is birational onto the actual integral quartic X.

## 1. A useful numerical-to-linear and quadratic-product lemma

If N is a numerically trivial integral divisor class on M, then
chi(N)=1 and h2(N)=h0(K-N)=0: (K-N).L=-2 excludes an effective
representative. Thus h0(N)>=1. Its effective representative is
numerically zero, so ample intersection forces it to be zero.
Consequently N~0. This direct argument establishes every
numerical-to-linear upgrade below without relying on an incomplete
Picard torsion-freeness assertion.

If L~2B+T for an integral divisor class B with h0(B)>=2 and an
effective divisor T, two independent sections u,v of B give three
independent sections s_T u^2,s_T uv,s_T v^2 of L. Independence
follows by dividing at the generic point by s_T v^2 and using that
u/v is nonconstant and transcendental over the algebraically closed
ground field. Extending them to a basis of H0(L) imposes the
nonzero relation X0X2-X1^2=0 on the actual quartic image. This is
impossible. Fixed components of B or T and common zeros of u,v
do not invalidate a global identity of sections.

In particular L is not divisible by two in Pic(M). If L~2B, then
B^2=1, K.B=-1, and

    chi(B)=1+(B^2-K.B)/2=2,
    h2(B)=h0(K-B)=0

because (K-B).L=-4. Hence h0(B)>=2 and the preceding contradiction
applies.

## 2. Exceptional primes are vertical (-2)-curves or horizontal (-3)-sections

Let E be an integral sigma-exceptional prime. Then L.E=0 and
E^2<0. Relative minimality and adjunction give K.E>=0 as in the
genus-one audit. Put

    d=f.E=K.E>=0,     Q=K+L/2.

The rational numerical class Q belongs to L-perpendicular and has
Q^2=-1. The Hodge pairing is negative definite on this
perpendicular space. Cauchy--Schwarz for its negative gives

    d^2=(Q.E)^2 <= -E^2.

Adjunction gives -E^2=d+2-2p_a(E), so

    d^2 <= d+2-2p_a(E).

For d=0, negative self-intersection and adjunction force p_a(E)=0
and E^2=-2. Thus E is a smooth rational vertical (-2)-curve.

For d>0 the inequality gives d<=2. If d=1, the restriction of the
adjoint ruling to E is a finite degree-one map E->P1. It is an
isomorphism since the target is normal and both curves are
integral. Thus E is a smooth rational section and E^2=-3.

If d=2, the inequality forces p_a(E)=0, E^2=-4, and equality in
Cauchy--Schwarz. Consequently E is numerically -2Q=-2K-L.
The numerical-to-linear lemma upgrades this to E~-2K-L, or

    L~2f+E.

Here E is effective and h0(f)=2, so the quadratic-product lemma
excludes this case. Therefore every exceptional prime is either
a vertical smooth rational (-2)-curve or a horizontal smooth
rational (-3)-section.

## 3. There are at most two horizontal exceptional sections, and they are disjoint

Let E1,E2 be distinct horizontal exceptional sections and t=E1.E2.
Distinct curves on smooth M give t>=0. Their sum T satisfies

    Q.T=2,     T^2=-6+2t.

Cauchy--Schwarz gives 4<=6-2t, so t<=1. If t=1, equality gives
T numerically -2Q. The same numerical-to-linear upgrade yields

    L~2f+T,

contradicting the quadratic-product lemma. Thus t=0: all
horizontal exceptional sections are pairwise disjoint. This is
stronger than the preliminary bound t<=1.

Suppose that three such sections E1,E2,E3 exist. Their disjoint
sum T has T^2=-9 and Q.T=3. Equality in Cauchy--Schwarz gives

    T numerically -3Q,
    2T numerically -6K-3L.

The integral divisor 2T+6K+3L is numerically trivial and therefore
linearly trivial. Rearranging gives

    L~2(-3K-T-L).

This contradicts the nondivisibility of L proved in section 1.
There are consequently at most two horizontal exceptional
(-3)-sections, and they are disjoint.

## 4. The correct mate identity retains two different strata

Assume now that an ambient mate of degree b exists. The accepted
[full-support and smooth-lift identities](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
give a smooth embedded curve c in S isomorphic to the degree-four
rational C and an effective pullback divisor on M

    div_M((nu sigma)^*G)=b c# + W ~ bL,

where W is supported on the sigma-exceptional locus and c# is the
smooth strict transform. Put Z=W/b, an effective rational
exceptional divisor, so c# is numerically L-Z and L.Z=0. Define

    q=-Z^2,     lambda=K.Z.

Here q>0 by negative definiteness. Also lambda>=0 by section 2,
and lambda is an integer since it equals K.(L-c#). Adjunction
to c# gives the actual general relation

    -2=c#^2+K.c#=(4-q)+(-2-lambda),
    q+lambda=4.

In particular one must not assert q=4 before proving lambda=0.
The noncrepant horizontal (-3)-curves make the distinction
material. As Q.Z=lambda, Cauchy--Schwarz gives lambda^2<=q.
Together with q+lambda=4 and integral lambda>=0 this leaves
exactly

    lambda=0, q=4, c#^2=0, f.c#=2;
    lambda=1, q=3, c#^2=1, f.c#=1.

The first stratum has a rational bisection c# and Z supported
only on vertical (-2)-curves. For any horizontal exceptional
section E, effectivity gives Z.E>=0, while

    Z.E=(L-c#).E=-c#.E<=0.

Thus c#.E=Z.E=0 in the first stratum: the bisection and the
support of its correction avoid the horizontal exceptional
sections.

The second stratum has a rational section c#. The sum of the
coefficients of horizontal exceptional sections in Z equals one;
vertical correction components can still occur. Section 3 shows
there are at most two such horizontal primes. No argument here
excludes this section stratum.

The auditor initially sent an unsaved informal proposal that
started from Z^2=-4 in all genus-two cases. The owner and root
immediately identified the omitted K.Z term. That proposal was
retracted before any record promotion. The two-stratum identity
above is the corrected accepted assertion; this audit preserves
the surviving noncrepant section case explicitly.

## 5. A smooth embedded lift meets an exceptional fiber transversely at one prime

The curve c is smooth and the proper birational map c#->c is
finite and hence an isomorphism. Therefore above each point p of
c, the strict transform has one point P.

If p is singular on S, choose a local function a in m_(S,p)
whose restriction to c is a uniformizer. Such a function exists
because O_(S,p)->O_(c,p) is surjective. Its pullback to M vanishes
with positive integral coefficient along every exceptional prime
above p. The smooth local ring O_(M,P) is factorial. Restriction
of the pullback to c# has order exactly one at P, whereas its
order is at least the sum of the local intersection
multiplicities of c# with all exceptional local branches through
P. Every such multiplicity is positive. It follows that:

* exactly one exceptional prime passes through P;
* that prime is smooth at P and meets c# transversely;
* c# meets no other point of the same exceptional fiber.

In particular c#.E is zero or one for every exceptional prime E,
and there is at most one positive intersection in each connected
exceptional fiber. This constraint uses the smooth embedded lift,
not a Cartier assumption on c. It can be applied to both mate
strata, but alone it is not a classification of the exceptional
intersection graph or a proof that lambda=1 is impossible.

## 6. Accepted boundary

Sections 1--5 are exact divisor and local-ring arguments. They do
not assume that S has ADE singularities or that the adjoint
ruling descends to S. They do not identify the conductor or prove
that every possible normalization fiber has been exhausted. The
vertical (-2) exceptional configurations and their integral
saturation, the noncrepant section stratum, and descent of a
hypothetical mate all remain separate obligations. No numerical
or computational enumeration is asserted here.
