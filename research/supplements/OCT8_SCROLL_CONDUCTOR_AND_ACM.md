# October 8 historical mathematical investigations

Full original source text is preserved below, including calculations, qualifications, counterexamples, and unresolved questions. This compilation does not independently audit or promote claims.

---

## Source: 2026-10-08-session-scroll-acm-independent-audit.md

# Independent audit: the whole scroll conductor is an ACM cubic

Date: 2026-10-08. Status: **ACCEPTED proof audit** of the all-integer
cohomology and Hilbert--Burch lemma recorded in the Oct8 checkpoint.
This is a structural reduction of the degenerate-conductor problem,
not an exclusion of every smooth-scroll carrier.

Let nu:S->X be the finite normalization of an integral quartic surface
in P3 in characteristic zero, where S is a smooth rational quartic
scroll with H=nu*O_X(1). Let I be the actual entire conductor and
Gamma=Spec_X(O_X/I), including all of its scheme structure. Let
J_Gamma be its ideal sheaf in P3. The previously accepted finite-duality
argument identifies I with nu_*omega_S and makes the upstairs
conductor D an effective Cartier divisor linearly equivalent to -K_S.

## 1. The ideal sequence and its entire scheme scope

The conductor sequence in the ambient projective space is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0.

Its first term is the equation of the integral quartic X; the quotient
is exactly I, not the ideal of the reduced conductor support. Since
both H1 and H2 of every line bundle on P3 vanish, twisting gives

    H1(P3,J_Gamma(m)) = H1(S,K_S+mH)

for every integer m. Finite pushforward has no higher cohomology
correction. The separate MCM/depth proof makes Gamma a pure
Cohen--Macaulay curve, and its Hilbert polynomial is 3m+1. Thus no
isolated or embedded conductor component is silently discarded.

## 2. Cohomology on both smooth quartic scrolls, for all integers

Write S=F_e with e=0 or 2, minimal section C of square -e,
fiber f, H=C+a f with a=e/2+2, and
K_S=-2C-(e+2)f. Let pi:S->P1 be its ruling.

For a divisor kC+beta f with k>=0, ruling pushforward is

    pi_*O_S(kC+beta f)=sum_(j=0)^k O_P1(beta-j e),
    R1 pi_*O_S(kC+beta f)=0.

The formula has the minimal-section convention C^2=-e; no sign change
between the F0 and F2 calculations is hidden. If k=-1, both direct
images vanish, since every fiber has O_P1(-1) cohomology zero.

For m>=2, K_S+mH has k=m-2 and beta=ma-e-2. Its smallest ruling
summand degree is

    ma-e-2-(m-2)e = m(a-e)+e-2.

This is 2m-2 on F0 and m on F2. All summands therefore have H1=0,
and the higher ruling pushforward vanishes. At m=1 the fiber degree
is -1, so both direct images vanish. For m<=0, surface Serre duality
reduces H1(K_S+mH) to the dual of H1((-m)H). Writing n=-m>=0,
the latter pushforward has degrees na-j e, 0<=j<=n, whose minimum
is n(a-e)>=0; its higher pushforward vanishes. This includes n=0.

Thus H1(J_Gamma(m))=0 for every integer m. Together with purity and
saturation, this proves that the entire conductor coordinate ring is
arithmetically Cohen--Macaulay, not only that the conductor is locally
Cohen--Macaulay.

## 3. Minimal generators and the full graded resolution

The same sequence gives H0(J_Gamma(1))=0: K_S+H has fiber degree -1.
At m=2 its pushforward is O_P1(2), so H0(J_Gamma(2)) has dimension
three. There are also no degree-zero generators.

Let R be the saturated homogeneous coordinate ring of Gamma. Its
Krull dimension is two and it is Cohen--Macaulay. Two general linear
forms are an R-regular sequence over the infinite field k. An
Artinian reduction A has length deg Gamma=3. Its initial Hilbert
entries are A0=1 and A1=2, since J_Gamma has no linear forms. These
already sum to its length, so its h-vector is exactly (1,2).

Consequently A is k[u,v]/(u,v)^2. Its three quadratic generators
lift to the three independent quadrics of J_Gamma. Because the two
linear forms are R-regular, the Koszul Tor groups vanish and reduction
identifies J_Gamma/(ell1,ell2)J_Gamma with that reduced ideal. Graded
Nakayama therefore proves that the three quadrics generate the entire
ideal; higher-degree generators are not being guessed from the first
few Hilbert-function values.

Auslander--Buchsbaum gives projective dimension two for R and one
for its ideal. Its Hilbert series is

    Hilb_R(z)=(1+2z)/(1-z)^2,
    Hilb_J(z)=(3z^2-2z^3)/(1-z)^4.

With exactly three degree-two generators, the minimal first syzygy
module is therefore O_P3(-3)^2. This establishes

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The matrix is a 3-by-2 matrix of linear forms, and Hilbert--Burch
identifies its three maximal minors with the conductor quadrics.
The argument does not assume Gamma integral, reduced or Gorenstein.

## 4. What the resolution does not imply

The rank-two cover arguments for a smooth Gamma cannot be applied
merely because Gamma has this resolution. At a non-Gorenstein
conductor point its canonical module is not invertible. The upstairs
conductor algebra need not be locally free of rank two over Gamma;
the retained ordinary triple-line generic algebra is a concrete
warning. An involution on reduced component fields also does not
automatically provide descent through the entire conductor scheme.

The exact sequence under investigation by the degenerate-conductor
agent is

    0 -> O_Gamma -> nu_*O_D -> omega_Gamma -> 0.

It follows by dualizing the conductor sequence on the Gorenstein X:
the conductor I and normalization nu_*O_S are MCM dual modules,
Ext1(O_Gamma,O_X)=omega_Gamma, and the next Ext group of I vanishes.
Modding the normalization sequence by I gives the displayed sequence.
When Gamma is Gorenstein this makes nu_*O_D locally free of rank two,
since an extension of two invertible modules is locally split. At
non-Gorenstein points this conclusion is unavailable.

## 5. A false reduced-graph shortcut and its precise obstruction

The naive propagation of constant roots of unity along conductor
components needs to distinguish separate attachment points from a
triple meeting. Consider the local base node R=k[[x,y]]/(xy) and
rank-two algebra

    R[eta]/(eta^2-x-y^2).

Eliminating x embeds D on the smooth (y,eta)-surface as
y*(eta^2-y^2)=0. Its three smooth branches meet at one point. The
branch y=0 covers x=eta^2; the exchanged branches eta=+y and eta=-y
map isomorphically to x=0. A smooth curve alpha*y+beta*eta=0 has
contact one with all three branches for generic coefficients. Its
two exchanged restrictions have constant ratio
(alpha-beta)/(alpha+beta), which may be any nonzero root of unity.
On the stable branch the deck eigenvalue is -1.

Thus zeros consumed by the mutual intersection of the exchanged
line pair can also occur at both attachments to the rest of D.
The claim that f is necessarily nonzero at those attachments is
false without additional geometric information. This local example
is an obstruction to that proof strategy, not an STCI example of C0
and not a claim of global realization by a quartic projection.

The subsequent conic-component argument uses global intersection
degrees and ramification, and survives this local triple meeting.
Its completion and the nonreduced cases are separate proof
obligations; they must not be inferred just from the ACM resolution.


---

## Source: 2026-10-08-session-scroll-artin-independent-audit.md

# Independent audit of the nonreduced scroll-conductor Artin reductions

Date: 2026-10-08. Status: **ACCEPTED independent proof audit**, under
the exact smooth-scroll normalization and full-support hypotheses.
This file audits the written proof in
[nongorenstein cubic classification](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-cubic-classificationmd)
and records a direct completion for the double-line-plus-line case.
It makes no canonical frontier edits and no global STCI assertion.

## 1. Exact generic module and entire multiplicities

The canonical conductor sequence is

    0 -> A -> B -> omega_A -> 0

at each actual generic conductor scheme point. B is the product of
truncated DVR algebras along the conductor primes on smooth S.
Each multiplicity a is the actual Cartier-divisor multiplicity of D;
each residue extension degree r is the degree of that prime over the
support line. Characteristic zero makes the residue extensions
separable. This formulation does not approximate D or Gamma by their
reduced support.

The proper-prime cohomology argument makes every conductor prime a
smooth rational curve. All uses of c~H and the singleton-fiber
condition rely on the entire normalization inverse image, and not on
a generic fiber alone.

## 2. Curvilinear triple line

For A=K[epsilon]/epsilon^3, omega_A is free of rank one. Thus B is
free of rank two over A and multiplication by epsilon has K-rank four.
In a factor K_i[t]/t^a, write k=ord(epsilon). Its image rank is
r(a-k), while epsilon^3=0 implies a<=3k. Summing over factors gives
the upper bound four; equality forces a=3k in every factor. A factor
with epsilon=0 would make the inequality strict and cannot occur.
Every coefficient of the actual D is divisible by three. This
contradicts D~2C+(e+2)f in Pic(F_e), e=0 or 2.

This excludes the curvilinear triple-line conductor before assuming
a mate. The proof requires no plane-curve delta classification.

## 3. Fat triple line

For A=K+N, dim N=2,N^2=0, multiplication by N on omega_A has image
dimension one. NB contains N, and NB intersect A equals N: the ideal
NB is square-zero, so it cannot contain a nonzero scalar, and it
already contains both nilpotents of A. Its image in B/A is N omega_A.
Therefore dim_K NB=3 and dim_K B=6.

Each truncated DVR factor is Frobenius over K, using the field trace
of the top t-coefficient. Thus dim Ann_B(NB)=3. Since (NB)^2=0,
NB is its own annihilator. In each factor NB=(t^k), whose annihilator
is (t^(a-k)); equality makes a=2k. This proves every actual D
coefficient even.

The resulting half-conductor classes are C+f on F0 and C+2f on F2.
Their effective prime decompositions in the source note are exhaustive.
The irreducible degree-three case is excluded by the elementary
Riemann--Hurwitz/singleton-fiber obstruction. In the F0 two-component
case, pulling the sole zero of the degree-one prime's section to
the degree-two prime produces a double zero at one totally ramified
point; immersion of c forces intersection one there, a contradiction.
On F2 two distinct fiber components have proportional restrictions
and disjoint paired zeros, again contradicting singleton fibers.

The residual pattern 2C_min+4F has NB_F=(t^2). Both ambient normal
coordinates to the support line consequently vanish to order at
least two on F. The longitudinal coordinate has nonzero differential
since F maps isomorphically to the line, so nu has generic rank one
there. The
[independently audited differential lemma](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-normalization-differential-independent-auditmd)
excludes a mate, including at special junctions with other conductor
components. This validates the entire fat-line exclusion.

## 4. Direct Artin completion for double-line-plus-line support

At the doubled support line L, A=K[epsilon]/epsilon^2, and B is free
of rank two. Its total K-length is four and multiplication by epsilon
has rank two. Writing epsilon=t^k in each factor gives k>=a/2,
and the total rank equality makes a=2k in every factor. The only
patterns are

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

At the reduced other line M, the rank-two algebra has patterns

    (a,r)=(2,1), (1,2), or (1,1)+(1,1).

A (4,1) factor over L has epsilon order two, so both ambient normal
coordinates to L vanish to order at least two on its prime; the
conductor ideal there vanishes to order four and does not change
this conclusion. The differential lemma excludes it. Similarly,
a doubled (2,1) factor over M has all ambient normal coordinates
in the actual conductor ideal (t^2), and is excluded by the rank-one
differential lemma. These exclusions are geometric consequences of
the whole Artin algebra, not a discarded nonreduced cover.

On F0, the only degree-two prime is horizontal C, and the degree-one
primes are fibers. The split thick-line case would use four fiber
multiplicities, exceeding D~2C+2f. Thus the cover over L is 2C.
The residual 2f over M cannot be the excluded doubled fiber and
cannot be one degree-two prime in a fiber class. It must be two
distinct fibers of multiplicity one, mapping to the same line.
Their proportional sections have disjoint paired zeros, excluding
a mate.

On F2 there is no degree-two prime. The cover over L is either
2C_min+2F or 2F1+2F2. The former leaves 2f over M, which again must
be two distinct fibers and is excluded by paired zeros. The latter
leaves 2C_min over M. It cannot be the excluded doubled prime,
one absent degree-two prime, or two distinct primes in the unique
C_min class. Therefore no mate exists in this case either.

The argument is valid at a nongorenstein intersection point, since
it uses no trace involution there. It avoids the earlier extra
square-descent obligation. Together with the accepted all-reduced
case and the two triple-line reductions, this supplies the proposed
full smooth rational quartic-scroll carrier exclusion. Promotion of
that combined theorem should use the written classification and the
independent differential audit together; it does not assert that
every nonnormal quartic has such a smooth scroll normalization.


---

## Source: 2026-10-08-session-scroll-conductor-adversarial.md

# Independent adversarial audit: scroll conductor compression

Date: 2026-10-08. Status: **ACCEPTED conditional exclusion**, including
the additional nonreduced rank-two case proved below. This audit makes
no canonical-record edits and does not assert that every scroll
projection satisfies the conductor hypotheses.

## 1. Precise theorem accepted by this audit

Let k be algebraically closed of characteristic zero. Suppose X is an
integral quartic surface in P3, its finite normalization nu:S->X is a
smooth rational quartic scroll, and C0 is the fixed smooth rational
quartic [s^4:s^3t:st^3:t^4]. Assume X is regular at the generic point
of C0. Write H=nu*O_X(1).

Let I be the **actual entire conductor ideal**, and define

    Gamma=Spec_X(O_X/I),   D=Spec_S(O_S/I*O_S).

Assume Gamma is a smooth twisted cubic and the induced map
rho:D->Gamma is finite flat of degree two. Then **X admits no STCI
mate for C0 in any degree**. Reducedness of D is unnecessary under
these exact assumptions.

The original proposed theorem assumed D reduced. Both its integral
and reducible cases are accepted. Section 7 proves the remaining
nonreduced case. The characteristic-zero and rank-two assumptions
are used explicitly; the statement does not cover thicker conductor
algebras or a singular, reducible or nonreduced Gamma.

## 2. Whole support and the global section f

If a mate G of degree b exists, its pullback is a nonzero section of
O_S(bH) whose zero set is the entire inverse image of C0. Over the
generic point of C0 normalization is an isomorphism. There is therefore
one curve component c finite birational over C0. Since C0 is smooth,
this map is an isomorphism. Any additional inverse-image points would
be isolated components and cannot be the support of a nonzero Cartier
divisor on S. Thus the mate forces the entire inverse support to be c.

In particular every normalization fiber above a point of C0 has one
point, and c is a smooth embedded curve. If div(nu*G)=n*c, then
intersecting with H gives 4n=4b, so n=b. The Picard group of a smooth
rational scroll is free abelian. Consequently b(c-H)~0 implies c~H.
There is a section f in H0(S,O_S(H)) whose divisor is precisely c.
The ratio nu*G/f^b has zero divisor, hence is a nonzero constant on
the normal proper integral S. Rescale G to arrange nu*G=f^b.

This argument uses the whole inverse support. A section with support
c alone could not suffice if there were other isolated inverse-image
points. No numerical-equivalence cancellation on an arbitrary
nonnormal surface is used.

## 3. Actual conductor descent and the rank-two algebra

For a finite normalization A subset B with conductor I, one has

    A = B x_(B/I) (A/I).

Indeed an element of B whose reduction modulo I comes from A differs
from an element of A by an element of I, and therefore belongs to A.
This gives the exact conductor square on sheaves. After tensoring
with O_X(d), a section upstairs descends precisely when its restriction
to the entire D agrees with a section on Gamma. Passing to the
reduced support alone would not justify this step.

In the present Gorenstein quartic setting, finite duality identifies
the conductor as a B-module with omega_S: Hom_A(B,A) is the conductor
inside the common function field, and omega_X is trivial. Since S is
smooth, the conductor is invertible and D is an effective Cartier
divisor with D~-K_S. This also rules out an additional isolated
conductor defect on S. Adjunction gives p_a(D)=1, or equivalently
chi(O_D)=0. The rationality of S and the exact sequence
0->omega_S->O_S->O_D->0 give H0(O_D)=k.

Identify Gamma with P1. In characteristic zero the trace map splits
the finite flat rank-two algebra:

    rho_*O_D = O_Gamma + N,

where N is an invertible tracefree module. Euler characteristic gives
deg N=-2, so N=O_P1(-2). A tracefree local generator eta satisfies
eta^2=Delta, with Delta a global section of O_P1(4). The involution
fixes O_Gamma and negates eta. Because H|D=rho*O_Gamma(1) and Gamma
is a twisted cubic, restrictions of f are sections of rho*O_P1(3).

All identifications use the actual conductor map, not a chosen
parametrization with an unspecified descent subalgebra.

## 4. Integral reduced D: quadratic compression

The deck action on rho*O_P1(3) is canonical, coming from the downstairs
line bundle. Since f^b descends, it is invariant under this action.
The restriction of f to D is not zero: its divisor c does not contain
a conductor component, since C0 is generically regular on X.

On the integral D the quotient r=sigma(f)/f is a rational function
and r^b=1. Over algebraically closed k, the polynomial T^b-1 splits
into distinct linear factors; an element of the function field
satisfying it is a constant root of unity zeta. Applying sigma twice
gives zeta^2=1. Hence f^2 is invariant on all of D. The rational
equality extends as equality of regular sections because D is
integral and reduced; a nodal or cuspidal D creates no gap here.

The invariant algebra of the rank-two cover is O_Gamma, so f^2|D
comes from a section of O_P1(6). The conductor square therefore
descends f^2 to a section of O_X(2). The hypersurface restriction
sequence and H1(P3,O(-2))=0 lift it to an ambient quadric Q.
Finite surjectivity shows V(Q) on X has exactly support C0.

The fixed C0 lies on its unique smooth quadric q and has class (1,3)
up to swapping the rulings. Thus Q is q up to a scalar. The quartic
equation of X restricts to class (4,4) on q. A divisor supported
only on C0 would have class n(1,3), which cannot equal (4,4).
This is the required contradiction in every mate degree.

## 5. Reducible reduced D: the actual gluing modulus

Reducibility of the reduced double cover means its generic algebra
splits. Thus Delta is the square of a rational section of O_P1(2).
The square root has no poles, because Delta is regular, so

    Delta=q2^2,   q2 in H0(P1,O(2)), q2!=0.

The two components D1,D2 each map isomorphically to Gamma. Under
the branch maps eta=+q2 and eta=-q2, their local algebra is the pairs
of regular functions congruent modulo q2. This follows explicitly:

    a+b*eta |-> (a+b*q2, a-b*q2),

whose image is exactly those pairs with difference divisible by q2,
because 2 is invertible. Hence the two smooth branches meet at each
zero of q2 with intersection multiplicity m=ord(q2), either one or
two. No ordinary-pinch or reduced-ramification assumption is made.

Let the restrictions of f be s,t in H0(P1,O(3)). Neither is identically
zero. Descent of f^b implies s^b=t^b, so t=zeta*s for a constant
b-th root of unity zeta. If zeta=1, f|D itself descends and the
conductor square gives an ambient hyperplane containing C0, impossible.

If zeta!=1, the gluing condition forces

    s=q2*ell,   ell in H0(P1,O(1)), ell!=0.

The single zero a of ell must be a zero of q2. Otherwise f vanishes
at two distinct points of the normalization over the same point of
Gamma; both points lie on c, contradicting c->C0 being an isomorphism.
At a, each branch restriction of f has order m+1.

## 6. The local contact contradiction

Two smooth branches D1,D2 on a smooth surface with intersection
multiplicity m admit completed regular coordinates (t,w) in which
D1 is w=0 and D2 is w=t^m*u(t), with u(0)!=0. The parameter t
may be chosen as a lift of the common Gamma parameter, because
its restrictions to both branches are uniformizers.

Let f also denote a local equation of c. If f has order m+1 on
both branches, then f(0,0)=0 and f_t(0,0)=0, since m+1>=2.
Smoothness of c forces f_w(0,0)!=0. But Taylor expansion gives

    f(t,t^m*u(t))-f(t,0)
      =t^m*u(0)*f_w(0,0) + terms of order greater than m.

The left side has order at least m+1 and the right side has order
exactly m, a contradiction. Thus no smooth third branch can have
contact greater than m with both D1 and D2. This proves the claimed
local obstruction for both a node (m=1) and a tangency (m=2).

This lemma does not say that conductor contact is bounded for every
smooth image curve. The retained degenerate-cusp counterexample permits
large contact with one branch while contact with the other stays at
the mutual branch intersection multiplicity. The present argument
requires both branch contacts to increase simultaneously, as forced
by the global section pair (s,zeta*s).

## 7. Nonreduced D: a conditional extension

Under the same finite flat rank-two assumptions, nonreduced D forces
Delta=0. If Delta were nonzero, its generic algebra would be reduced;
any nilpotent supported only at closed points would be torsion in the
locally free O_Gamma-module rho_*O_D, impossible. Thus its algebra is

    O_Gamma + O_Gamma(-2)*eta,   eta^2=0.

Write f|D=a+b*eta with a in H0(P1,O(3)) and b in H0(P1,O(1)).
Here a is not identically zero: otherwise c contains the reduced
conductor curve, whose image is Gamma of degree three, incompatible
with the generically regular degree-four C0. The power is

    (f|D)^n=a^n+n*a^(n-1)*b*eta.

Descent of the mate power forces its nilpotent coefficient to vanish.
Characteristic zero, the nonzero a and the torsionfree tracefree line
bundle imply b=0. Thus f itself descends through the entire conductor
square, giving the impossible hyperplane section. This argument was
also independently checked by `nonnormal_structural` on 2026-10-08.

It does not apply to arbitrary nonreduced conductor schemes: rank two,
smooth Gamma and the actual entire square are essential. In particular
it asserts no reduction of a higher-width cusp algebra to this one.

## 8. Source scope and audit decision

[Ducat's published treatment](https://d-nb.info/1317691679/34),
Proposition 3.3, Table 3 and §5.7, places smooth rational quartic
scroll normalizations over twisted-cubic double curves in the
semi-log-canonical classification and explicitly retains degenerations
of those double curves. It does not justify identifying every such
degeneration with a smooth Gamma, nor replacing the actual conductor
by its reduced support. The theorem above assumes and uses its
conductor hypotheses directly; it does not require an slc hypothesis.

The exclusion is accepted for integral, reducible reduced, and
nonreduced D whenever the entire conductor square has smooth twisted
cubic Gamma and a finite flat rank-two map. The local contact proof,
scheme-level section descent and nilpotent power calculation pass this
independent adversarial audit. Classification applicability to other
scroll projections remains a separate obligation.

## 9. The conductor hypotheses follow from smooth twisted-cubic support

The other auditor supplied a useful applicability argument, which this
audit independently checked. It strengthens section 1 as follows:

> A smooth rational quartic-scroll normalization of an integral quartic
> whose **entire nonnormal support is a smooth twisted cubic** cannot
> be an STCI carrier of C0 in characteristic zero, in any mate degree.

Here the actual conductor scheme need not initially be assumed reduced
downstairs or finite flat of rank two; those properties follow below.
This still does not encompass singular or reducible degenerations of
the twisted cubic.

First, I=nu_*omega_S is a maximal Cohen--Macaulay module over O_X.
At a closed point of X, a system of parameters in its two-dimensional
local ring is a system of parameters in each finite smooth local ring
upstairs, hence is a regular sequence there and on the invertible
omega_S. The same holds on the finite semilocal module. The quartic X
is itself Cohen--Macaulay. The depth lemma applied to
0->I->O_X->O_X/I->0 therefore makes the nonzero conductor quotient a
pure Cohen--Macaulay curve: no isolated or embedded point component
can remain.

Riemann--Roch on the rational scroll gives

    chi(I(m))=chi_S(K_S+mH)
             =1+(m^2*H^2+m*K_S.H)/2
             =2m^2-3m+1.

The quartic hypersurface Hilbert polynomial is chi(O_X(m))=2m^2+2.
Consequently the **actual** conductor-center polynomial is

    chi((O_X/I)(m))=3m+1.

Its degree equals the degree three of its assumed smooth
twisted-cubic support. Generic multiplicity along that support is
therefore one. A nilradical would be a submodule supported only at
finitely many points, contradicting the absence of embedded points in
the Cohen--Macaulay curve. Thus the actual conductor center is
precisely the reduced smooth twisted cubic, not a thickening with
undetected finite defects.

The upstairs conductor D is Cartier by section 3, hence a
Cohen--Macaulay curve. It maps finitely to this smooth Gamma. Every
component dominates Gamma: a finite map cannot contract a positive
dimensional component. A local Gamma parameter is therefore a
nonzerodivisor on O_D, so rho_*O_D is torsionfree over the regular
curve and is locally free. This proves flatness. Its generic rank r
is determined by

    H.D=r*deg O_Gamma(1),  namely 6=3r,

so r=2. All hypotheses used in sections 3--7 are now verified.

The argument needs no classification of branch points and no
semi-log-canonical hypothesis. Its substantive geometric scope
restriction is the smooth twisted-cubic nonnormal support.

The independently read companion
`../computations/verify_session_scroll_conductor_compression.py`
checks the exact trace involution, square-discriminant component
evaluations, initial Taylor coefficients for m=1,2, symbolic all-n
dual-number power coefficient, and the unique quadric through C0.
It was freshly replayed in this audit with the prescribed SymPy
runtime and returned PASS. The argument for all mate degrees is the
structural proof above; it is not inferred from sampling degrees.

## 10. Every integral quartic singular along a smooth twisted cubic

The applicability transition in
`2026-10-08-session-scroll-conductor-applicability.md` was independently
audited and is **ACCEPTED**. Its strongest statement is:

> Every integral quartic surface singular along a smooth twisted cubic
> is excluded as a characteristic-zero STCI carrier of fixed C0, in
> every mate degree. No semi-log-canonical hypothesis is used.

After a projective coordinate change the twisted cubic is
[s^3:s^2t:st^2:t^3]. Let its quadratic generators be
xi1=x0*x2-x1^2, xi2=x0*x3-x1*x2, xi3=x1*x3-x2^2. This projective
change also moves C0, but preserves its unique smooth quadric and
bidegree (1,3); the conductor contradiction is projectively invariant.

The derivative matrix checks *all* quartics singular along this cubic.
It has 35 quartic monomial columns and 40 coefficient rows from four
degree-nine restricted derivatives. The independent checker
`../computations/audit_scroll_twisted_cubic_equation_space_2026_10_08.py`
reconstructs its entries by symbolic differentiation and substitution,
not by importing the owner's coefficient formula. Fraction Gaussian
elimination verifies the stated literal 29-by-29 determinant
104509440, full matrix rank 29, and independence of all six kernel
products xi_i*xi_j. It also directly checks the two syzygies and Euler
identity. The six products therefore span the entire kernel. The
saved JSON from this checker records its exact scope and indices.

Consequently F=Q(xi1,xi2,xi3) for every quartic singular along the
cubic. Euler's identity in characteristic zero supplies F|Gamma=0
from the derivative condition. Integrality forces Q to be a smooth
conic: every singular ternary quadratic over the algebraically closed
field factors into linear factors, whose substitutions are nonzero
quadrics because xi1,xi2,xi3 are independent.

The incidence variety Y in P3 x P2 cut out by
x2*xi1-x1*xi2+x0*xi3=0 and x3*xi1-x2*xi2+x1*xi3=0 is a smooth
P1 bundle over P2. The displayed 2-by-4 matrix has rank two at every
point of P2. It is the graph of the quadratic map away from Gamma.
The smooth irreducible incidence variety is therefore the closure of
this dense graph, hence is the blowup of the ideal of Gamma. This
gives a scheme-level justification of the blowup identification, not
merely a comparison of generic fibers.

At a point [s^3:s^2t:st^2:t^3] of Gamma the exceptional fiber is the
line

    t^2*xi1-s*t*xi2+s^2*xi3=0

in P2. Its coefficient vector is nonzero for every [s:t]. A smooth
conic Q contains no such line. Thus S=pi^-1(Q) is a smooth P1 bundle
over Q=P1 and its map to X is proper with every exceptional fiber of
length two. It is finite everywhere, including all tangent line/conic
intersections, and birational because it is an isomorphism off Gamma.
The normal S is therefore the normalization of the integral X.

X is smooth off Gamma by that isomorphism. Every point of Gamma is
singular, and if a local ring of X there were normal, normalization
would be an isomorphism on its normal neighborhood and make it
regular, contrary to the derivative condition. Hence its entire
nonnormal support is exactly Gamma.

Writing H for the hyperplane pullback on Y and E for its exceptional
divisor, the quadratic-map line bundle is 2H-E. Therefore S has
class 4H-2E, with no missing exceptional component. Adjunction gives
K_S=-E|S; blowup intersections H^2.E=0 and H.E^2=-3 give H|S^2=4
and K_S.H|S=-6. Each ruling fiber maps isomorphically to its line in
P3, so H has degree one there. Since the normalization map is finite,
H is ample. For S=F_e, H=C_min+a*f, the equations 2a-e=4 and a>e
give e=0 or 2. Thus the normalization is precisely a smooth rational
quartic scroll with its standard polarization and free Picard group.

Section 9 now identifies the actual downstairs conductor with the
smooth Gamma and proves finite flat rank two upstairs. Sections 4--7
exclude every possible upstairs conductor case. This completes the
stronger applicability theorem independently of the slc literature
classification. Singular or reducible degenerations of Gamma are
still outside this conclusion.


---

## Source: 2026-10-08-session-scroll-conductor-applicability.md

# Entire conductor verification for the smooth twisted-cubic quartic class

Date: 2026-10-08. Status: **PROVED structural applicability**, with one
small exact linear-algebra certificate. No semi-log-canonical assumption
is made. This note does not classify every nonnormal quartic.

**Theorem.** Over an algebraically closed characteristic-zero field,
an integral quartic surface singular along a smooth twisted cubic cannot
be a carrier in a set-theoretic complete-intersection presentation of
C0=[s^4:s^3t:st^3:t^4], in any mate degree.

The proof verifies the precise hypotheses of the
[conductor compression criterion](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-irreducible-conductor-compressionmd).
It includes reduced, reducible, nodal, and nonreduced upstairs conductor
schemes inside this class. It does not infer a classification from
Ducat's semi-log-canonical Table 3.

## 1. A general smooth-scroll conductor lemma

Let nu:S->X be a finite normalization of an integral quartic in P3,
where S is a smooth rational quartic scroll and H=nu*O_X(1). Let I be
the actual conductor on X and Gamma_cond=V(I). Finite absolute duality
gives, as in section 2 of the criterion,

    I=nu_*omega_S,  O_S(-D)=omega_S,
    H^2=4, K_S.H=-6, chi(O_S)=1.

At a closed point of X, a system of parameters of its local ring A is
a system of parameters in each regular local ring of the finite
semilocal normalization B above it. That system is a regular sequence
on B and on the invertible B-module I. Hence I is a maximal
Cohen--Macaulay A-module. The depth lemma in

    0 -> I -> A -> A/I -> 0

shows that Gamma_cond is a pure Cohen--Macaulay curve: its local rings
at closed points have depth at least one. This excludes isolated and
embedded conductor components downstairs as well as the Cartier
argument excluding them upstairs.

Riemann--Roch on S gives

    chi(I(m))=chi(O_S(K_S+mH))=2m^2-3m+1.

The quartic hypersurface sequence gives chi(O_X(m))=2m^2+2. Therefore
the actual downstairs conductor has Hilbert polynomial

    chi(O_Gamma_cond(m))=3m+1.

This calculation includes its entire scheme structure. In particular,
if its support is a smooth twisted cubic Gamma, then its degree already
equals deg Gamma. Its generic multiplicity is therefore one. Its
nilradical, if nonzero, would be a finite-support submodule, contrary
to the depth-one Cohen--Macaulay property. Thus

    Gamma_cond=Gamma as schemes.

The actual upstairs D is Cartier, hence Cohen--Macaulay and pure. Each
of its components maps onto Gamma under the finite map. A nonzero local
parameter of the smooth Gamma therefore avoids every associated prime
of D. Thus p_*O_D is torsionfree over every local DVR of Gamma, hence
p:D->Gamma is finite flat. Its rank is

    (H.D)/(deg O_Gamma(1))=6/3=2.

This proves the exact entire-conductor, smooth-base, rank-two hypotheses
from smooth-scroll normalization plus smooth twisted-cubic nonnormal
support. It needs no assumption that D is reduced or nodal.

There is also a useful intrinsic variant: if the actual Gamma_cond is
integral, its polynomial 3m+1 gives arithmetic genus zero. Normalizing
it gives p_a=g(normalization)+length(normalization quotient), so both
nonnegative terms vanish. It is a smooth rational degree-three curve.
It cannot be planar, since a plane cubic has arithmetic genus one;
hence it is a smooth twisted cubic. The same criterion applies. This
variant does not assert that Gamma_cond is always integral.

## 2. The smooth twisted-cubic quartic equation, without slc

After a projective coordinate change write

    Gamma=[s^3:s^2t:st^2:t^3],
    xi1=x0*x2-x1^2,
    xi2=x0*x3-x1*x2,
    xi3=x1*x3-x2^2.

Every quartic singular along Gamma is of the form F=Q(xi1,xi2,xi3)
for a ternary quadratic Q. This is the algebraic equation statement in
[Ducat, section 5.7, equations (5.2)--(5.3), pages 24--25](https://d-nb.info/1317691679/34).
We verify it independently below, so its use does not transfer the
paper's log-canonical classification assumptions.

Use the 35 degree-four exponent vectors in the order

    (e0,e1,e2,4-e0-e1-e2),
    e0=0..4, e1=0..4-e0, e2=0..4-e0-e1.

The derivative-restriction matrix M has 40 rows, indexed by (i,j)
with 0<=i<=3 and 0<=j<=9; j is the s-degree of the restricted
degree-nine derivative. For a column e and weights w=(3,2,1,0),

    M[(i,j),e]=e_i if j=sum(w_k e_k)-w_i, and zero otherwise.

It records the restrictions of all four partial derivatives to Gamma.
The [exact companion verifier](../computations/verify_session_scroll_conductor_compression.py)
exhibits a rank-29 minor with determinant 104509440. Using zero-based
indices, its rows are

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
    20,21,22,23,24,25,26,27,28,30

and its columns are

    0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,
    21,22,23,24,28,29,30,31,32,33,34.

The six products xi_i*xi_j, i<=j, are independent and lie in its kernel.
Thus rank is at most 29 and the displayed nonzero minor proves it is
exactly 29. They span the entire six-dimensional kernel. Since Euler's
identity also gives 4F=sum x_i F_i, the kernel is precisely the space
of quartics singular along Gamma. This is an exact finite-dimensional
proof, not a generic-rank sample.

If F is integral, Q cannot factor into linear factors: their substitutions
would give two nonzero quadratic factors, since the three xi_i are
independent. Therefore Q is a smooth plane conic over k.

## 3. A smooth finite normalization of every such integral quartic

The two syzygies are

    x2*xi1-x1*xi2+x0*xi3=0,
    x3*xi1-x2*xi2+x1*xi3=0.

Let Y subset P3 x P2 be the corresponding incidence variety. The matrix
in the P3 variables, at a point [xi1:xi2:xi3] of P2, is

    [xi3, -xi2,  xi1,   0],
    [  0,  xi3, -xi2, xi1].

It has rank two everywhere: if xi1!=0 its last column distinguishes
the rows; if xi1=0 and xi3!=0 its first column does; in the remaining
case xi2!=0 and the rows involve distinct coordinates. Thus Y is a
P1 bundle over P2, and is smooth. Its map sigma:Y->P3 is the blowup
of the smooth twisted cubic. In fact the matrix in the P2 variables is
[x2,-x1,x0; x3,-x2,x1], whose rank-two minors are xi3,-xi2,xi1.
It has rank two off Gamma and rank one everywhere on Gamma. Off Gamma
the syzygies therefore specify the unique point
[xi1(x):xi2(x):xi3(x)]; over Gamma their kernel is a projective line
embedded as a line in P2. Since the smooth P1 bundle Y is irreducible,
this graph over the dense open P3 minus Gamma is dense in Y. Thus Y is
the graph closure of the ideal-generated rational map, equivalently
the blowup, with no omitted incidence component.

Let S be the inverse image of the smooth conic Q under Y->P2. Then S
is a smooth P1 bundle over Q=P1. Off Gamma, sigma|S is an isomorphism
onto X=V(F). Over a point of Gamma, the exceptional fiber maps to a
line in P2, and a smooth conic contains no line. Its intersection with
Q has length two, including tangent intersections. Hence sigma|S is
proper with finite fibers, and is finite. It is birational, so it is
the normalization of the integral X.

Moreover X is smooth off Gamma, since there it is isomorphic to S.
Every point of Gamma is singular on X, as F=Q(xi) has all first
derivatives zero there. Since S is smooth, none of these singular
local rings can already be normal: a finite birational map to a normal
local ring would be an isomorphism. Thus the nonnormal support is
exactly Gamma, with no extra isolated points.

Write H=sigma*O_P3(1)|S and E for the exceptional divisor on Y. The
quadratic leading normal form of F along Gamma is the restriction of
Q to the line of normal directions. It is nonzero, since the smooth
Q contains no line. Thus F has order exactly two along Gamma, the
strict transform S has class 4H-2E, and

    K_Y=-4H+E,  K_S=-E|S.

Intersection gives H^2=4 and H.E|S=6, since H^2.E=0 and H.E^2=-3 on
the blowup of the degree-three curve. Consequently K_S.H=-6.
The finite map makes H ample, and each ruling fiber maps to a secant
line of Gamma, so H has degree one on that fiber. If S=F_e and
H=C_min+a f, then 2a-e=4 and ampleness gives a>e. Hence e is even and
e<4, so e=0 or 2. This is a smooth rational quartic scroll, with its
standard degree-four polarization and torsionfree Picard group.

The general lemma in section 1 now identifies the actual entire
conductor downstairs with this smooth Gamma, and the entire conductor
cover upstairs is finite flat of rank two. The criterion therefore
applies to all such integral quartics, including the non-slc cases.

## 4. What remains outside this theorem

No assertion is made here that every smooth normalized quartic scroll
has smooth twisted-cubic nonnormal support. A reducible, nonnormal, or
nonreduced downstairs conductor remains outside this application. A
singular normalization also remains outside the argument, as do the
line/conic conductor classes with other sectional genera and possible
lifted curves meeting normalization singularities. The theorem proves
an entire explicit nonnormal class has no mate for C0; it does not
resolve the unrestricted STCI problem or exhaust all quartic carriers.

Independent checks: the Hilbert/CM conductor-scheme argument and the
rank-two descent criterion were separately checked by the
normal-global-adversarial agent. The equation-space certificate is
reproducible by the companion verifier, whose exact determinant is
recorded above. Its finite matrix verifies only that equation-space
step; the all-degree mate exclusion is the structural conductor proof.


---

## Source: 2026-10-08-session-scroll-conic-line-independent-audit.md

# Independent audit: conic-plus-line conductors exclude every mate

Date: 2026-10-08. Status: **PROVED and independently audited**, using
the recorded scroll conductor duality, ACM and full-support inputs.
This result includes nonreduced upstairs conductors. It does not
classify every degenerate conductor of a smooth quartic scroll.

## 1. The carrier class and exact conductor scheme

Work over an algebraically closed field of characteristic zero. Let
X be an integral quartic surface with finite normalization nu:S->X,
where S is a smooth rational quartic scroll polarized by
H=nu*O_X(1). Suppose its entire nonnormal support is the union of a
smooth conic A and a line B meeting in scheme length one.

Then **X cannot participate in an STCI presentation of fixed C0 in
any mate degree**. The hypotheses do not assume ordinary pinches,
reduced upstairs conductor, or semi-log-canonical singularities.

Let I be the actual conductor, Gamma=V(I) downstairs and D=V(I O_S)
upstairs. The audited ACM lemma gives Gamma pure Cohen--Macaulay with
Hilbert polynomial 3m+1. The support A union B has degree three,
so its generic multiplicities are one. Cohen--Macaulay purity rules
out a nilradical supported at finitely many points. Therefore the
actual Gamma is the reduced A union B, with no undisclosed thickening.
Its meeting is a node: B is outside the plane of A, and the two
smooth tangent directions are distinct. Gamma is Gorenstein.

Finite duality gives D~-K_S as an effective Cartier divisor, and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Here is a direct verification of the second sequence. Over the
Gorenstein X, I=Hom_X(nu_*O_S,O_X). Both modules are maximal
Cohen--Macaulay and double duality identifies Hom_X(I,O_X) with
nu_*O_S. Dualizing 0->I->O_X->O_Gamma->0 gives
0->O_X->nu_*O_S->omega_Gamma->0; the next Ext group of I vanishes.
Quotienting by the common conductor I gives the displayed sequence.

Since omega_Gamma is invertible, this extension makes p_*O_D locally
free of rank two. Thus p is finite flat, including at the node.
Trace in characteristic zero splits its algebra as O_Gamma plus an
invertible tracefree module L, with eta^2=Delta locally. The splitting
also identifies L with omega_Gamma. No flatness of nu:S->X itself is
assumed.

## 2. Curve support and every conductor prime

The mate hypothesis gives the entire inverse image of C0 with reduced
support one embedded smooth rational curve c isomorphic to C0. A
nonzero Cartier divisor upstairs cannot have extra isolated support.
Degree gives div(nu*G)=n*c for a degree-n mate. The scroll Picard
group is free, so c~H; choose f in H0(S,H) with div(f)=c. Rescaling
the mate gives nu*G=f^n.

On the rational S, every nonzero proper effective divisor E<D obeys

    H1(O_E)=H2(O_S(-E))=H0(O_S(E-D))^*=0.

The last equality follows because D-E is nonzero effective and its
negative ideal has no global section on the proper connected S.
Every conductor prime is proper: D maps onto both A and B, so D
cannot be an integral reduced single prime. Consequently every prime
of D is a smooth rational curve, even when other components of D
are nonreduced. Moreover H0(O_D)=k by the anticanonical sequence,
so its support is connected. Prime adjunction gives

    E.(D-E)=2.

At the generic point of A, the rank-two algebra has total length two.
Writing a_E for a conductor multiplicity and d_E for the degree of
the reduced prime's map to A, one has sum a_E*d_E=2. There are
exactly three possibilities: one reduced degree-two cover; two
distinct reduced degree-one components; or one doubled degree-one
component. The following sections exclude all three.

## 3. An irreducible degree-two conic cover

Suppose a prime E maps to A with degree two and multiplicity one.
It is P1 and its characteristic-zero map E->A=P1 is a separable
double cover. Riemann--Hurwitz gives exactly two simple ramification
points. Also H.E=2*deg A=4, hence c.E=4.

Every point of c intersecting E must be a ramification point of the
cover. At an unramified point there would be a second distinct
normalization point above the same point of A; the full inverse
support condition and c->C0 being an isomorphism forbid that.

At a ramification point, dnu annihilates the tangent line of E in
the ambient P3 because the derivative of E->A vanishes. The image
C0 is smooth and nu|c is an isomorphism, so dnu does not annihilate
the tangent line of c. These lines on the smooth surface S are
therefore different, and the intersection of c with E is transverse.
Each of the two possible points contributes one, giving c.E<=2,
contrary to c.E=4.

This derivative argument remains valid when the ramification point
also lies on other conductor components. It assumes no ordinary
pinch model and survives a triple meeting upstairs.

## 4. A pair of degree-one conic components

Suppose E and E' both map isomorphically to A and appear with
multiplicity one. Each has H-degree two. Descending f^n identifies
its two restrictions after these isomorphisms with A. Their quotient
in k(A) has n-th power one, so they are nonzero constant multiples
of one another. In particular their zero orders over each point of
A agree.

Every zero of f on E must lie on E intersection E'. Otherwise the
matching zero on E' would be a distinct point of c in the same
normalization fiber, impossible. At a common point let m be the
mutual branch intersection multiplicity and v the common zero order
of f. Both branches are smooth. The Taylor lemma in the conductor
audit shows v<=m: a smooth third branch cannot have contact greater
than m with both of them.

Summing gives

    2=c.E <= E.E' <= E.(D-E)=2.

Hence E.E'=2 and E has no intersection with any other component
of D. The symmetric equality for E' isolates the pair from the
remaining conductor. There must be remaining conductor above B,
contradicting connectedness of D. Multiplicities on those remaining
components cannot change this contradiction: every contribution to
E.(D-E) is nonnegative.

## 5. The doubled conic component

Suppose D contains 2E with E mapping isomorphically to A. Then
H.E=2. The two smooth rational quartic scrolls are

    F0: H=C+2f,   -K=2C+2f,
    F2: H=C_min+3f,   -K=2C_min+4f.

On F2 there is no irreducible H-degree-two curve. A prime different
from C_min with class alpha*C_min+beta*f satisfies beta>=2alpha
by nonnegative intersection with C_min, and H-degree alpha+beta.
If alpha>=1 this is at least three. If alpha=0, an effective divisor
is a sum of ruling fibers, and its only primes have degree one.
The prime C_min itself has degree one. Thus F2 is impossible here.

On F0 a degree-two prime is a section in class C: the alternatives
in 2alpha+beta=2 with alpha,beta nonnegative are C and 2f, and the
latter is not prime. Consequently D-2E has class 2f, and is either
F1+F2 for two distinct fibers or 2F for one fiber.

In the first case each Fi has H-degree one, maps isomorphically to B,
and intersects E in one point. The points E intersection F1 and
E intersection F2 are distinct, but both map into A intersection B,
the same node. This contradicts E->A being an isomorphism. Hence

    D=2E+2F.

The rank-two conductor algebra is generically nonreduced on both
components of the reduced Gamma. Its trace discriminant Delta
therefore vanishes generically on both and is identically zero.
Thus p_*O_D=O_Gamma plus L*eta with eta^2=0.

Write f|D=a+b*eta, with a a section of O_Gamma(1) and b a section
of L tensor O_Gamma(1). The section a is generically nonzero on
both components, since c is neither E nor F. It is therefore a
nonzerodivisor on the reduced Cohen--Macaulay Gamma. Descent of the
mate power gives

    (a+b*eta)^n=a^n+n*a^(n-1)*b*eta,
    n*a^(n-1)*b=0.

Characteristic zero and invertibility of L force b=0. Thus f itself
descends through the entire conductor square to O_X(1), and lifts
to an ambient hyperplane containing C0. This contradicts the
nondegeneracy of C0.

## 6. Audit decision and boundary

The three possibilities over the conic exhaust generic rank two.
Their exclusions use full scheme-level conductor descent, proper-prime
cohomology, the exact scroll effective classes, and the smoothness of
the image curve. The nonreduced argument is genuinely scheme-level;
it does not replace D by its reduced support or assume a rank-two
cover over a non-Gorenstein base.

The all-D extension in section 5 was proposed in this audit and
separately checked by `scroll_degenerate_conductor`; the conic-cover
and paired-conic reductions were supplied by that agent and separately
checked here. The ACM/Hilbert--Burch audit is recorded in
`2026-10-08-session-scroll-acm-independent-audit.md`. No agreement
between agents is substituted for the supplied proofs.

Reduced three-line conductors, non-Gorenstein multiple-line schemes,
and other degenerations of an ACM cubic remain separate. This note
does not exclude every smooth-scroll normalization or every quartic
carrier, and does not resolve the unrestricted C0 or universal STCI
problem.


---

## Source: 2026-10-08-session-scroll-degenerate-conductor.md

# Degenerate actual conductors on smooth quartic scroll normalizations

Date: 2026-10-08. Status: **PROVED all-mate exclusion for every reduced
actual downstairs conductor on a smooth rational quartic-scroll
normalization**, including every upstairs conductor scheme. The
nonreduced downstairs boundary remains open. No canonical frontier
file is edited here.

## 1. Actual scheme and normalization hypotheses

Let X be an integral quartic hypersurface over an algebraically closed
field of characteristic zero. Suppose its finite normalization
nu:S->X is a smooth rational quartic scroll, with H=nu*O_X(1). Let I be
the actual conductor, Gamma=V(I) on X, and D=V(I O_S) on S. In particular
D is the entire conductor Cartier divisor, not its reduced support.
Finite absolute duality gives

    I=nu_*omega_S, D~-K_S, H.D=6.

The [applicability note](#source-2026-10-08-session-scroll-conductor-applicabilitymd)
proves Gamma is pure Cohen--Macaulay with Hilbert polynomial 3m+1.
The [Oct8 checkpoint](2026-10-08-session-checkpoint.md) strengthens this
to an arithmetically Cohen--Macaulay cubic with the Hilbert--Burch
resolution

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The resolution retains every nonreduced structure. The matrix is a
2 by 3 matrix of linear forms; its three maximal minors are the entire
ideal of Gamma. A reduced reducible Gamma is either a smooth conic
meeting a line once, three noncoplanar lines forming a chain, or three
noncoplanar concurrent lines. This support list alone does not classify
the entire conductor morphism. In particular the concurrent case need
not be Gorenstein or admit a finite flat double-cover description.

## 2. Generic rank two follows without global flatness

There is an exact sequence of O_Gamma-modules

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Here is a local derivation that does not assume p flat. Write A for a
two-dimensional Gorenstein local ring of X, B for its finite smooth
normalization, and Q=B/A. A system of parameters is B-regular, so B is
maximal Cohen--Macaulay over A. The depth lemma shows Q is a
Cohen--Macaulay module of dimension one, unless it vanishes. Applying
Hom_A(-,A) to 0->A->B->Q->0 gives

    Ext_A^1(Q,A)=A/I,

because Hom_A(B,A)=I, Hom_A(Q,A)=0, and Ext_A^1(B,A)=0.
Canonical-module biduality for Cohen--Macaulay modules of codimension
one therefore gives Q=Ext_A^1(A/I,A)=omega_Gamma. Modding the original
normalization sequence by their common conductor ideal I gives the
displayed exact sequence. The canonical-module identifications are
relative to omega_X=O_X.

Consequently, when Gamma is reduced, at its generic points the total
conductor cover has degree two: the canonical module there is a
one-dimensional vector space over the corresponding function field.
This does not imply flatness over a nongorenstein closed point of
Gamma, and no such inference is used below.

## 3. The mate imposes smooth hyperplane-section and full-fiber data

Suppose X has a mate G of positive degree b with

    (X intersect V(G))_red=C0,
    C0=[s^4:s^3t:st^3:t^4].

Gamma has degree three, so C0 is generically in the normal locus. The
full pullback support argument in the
[compression note](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-irreducible-conductor-compressionmd)
gives a unique c subset S isomorphic to C0, with

    (nu^-1(C0))_red=c, div(nu*G)=b c, c~H.

Every fiber over C0 consists of exactly one point. If f is a section
of O_S(H) with divisor c, then nu*G=lambda f^b with lambda constant.
In particular the restrictions of f^b to all conductor branches
descend through the actual p:D->Gamma. Finally nu|c is an isomorphism,
so its differential along c never vanishes. This differential
condition remains valid at a point where several conductor components
meet on S.

## 4. Components of a connected reduced anticanonical conductor

Now suppose D is reduced. It is connected: from
0->O_S(K_S)->O_S->O_D->0 and H^1(O_S(K_S))=0,

    H^0(O_D)=k.

If D is reducible and E is one of its irreducible components, adjunction
gives

    E.(D-E)=(-K_S-E).E=2-2 p_a(E).

The left side is nonnegative, and is positive by connectedness.
Therefore p_a(E)=0 and E.(D-E)=2. Thus every component E is a smooth
rational curve. This argument uses the arithmetic genus of the actual
component, so it also excludes singular rational components here.

## 5. Reduced conic-plus-line conductor: every mate degree is excluded

**Theorem.** Retain the normalization hypotheses, and suppose Gamma is
reduced with a smooth conic component and a line component, while D is
reduced. Then X cannot be a carrier of a set-theoretic complete
intersection presenting C0, in any positive mate degree.

The generic rank-two result of section 2 leaves two possibilities over
the conic Q.

### One irreducible component over Q

There is a single conductor component E mapping to Q with degree two.
Since D has components above the line as well, section 4 shows
E is smooth rational. A separable degree-two map P1->P1 has exactly
two distinct simple ramification points in characteristic zero.

If a point P of E belongs to c, the singleton-fiber condition forces
p^-1(p(P)) on E to contain just P. Hence P is a ramification point of
E->Q. The differential of nu restricted to T_P E vanishes there,
because nu|E factors through this ramified map and the embedded conic.
Since nu|c is an immersion, T_P c differs from T_P E. Their local
intersection multiplicity is therefore one, even if other conductor
components meet at P. It follows that

    c.E <= 2.

But c~H and H|E=p*O_Q(1), giving

    c.E=H.E=2 deg(Q)=4,

a contradiction.

### Two components over Q

There are two components E,E', each mapping to Q with degree one. They
are smooth rational and their finite degree-one maps to the smooth
conic are isomorphisms. Identify their restricted hyperplane bundles
with O_Q(1). The mate relation gives

    (f|E')^b=(f|E)^b,

so f|E'=zeta f|E for a constant b-th root of unity zeta. Neither
restriction vanishes identically, since its image is the conic rather
than C0. Every zero on E must lie in E intersect E', because the same
zero occurs at the paired point on E', and a fiber over C0 is a
singleton. At such a mutual point both restrictions have the same
order a, since the maps to Q are isomorphisms.

If their local contact multiplicity is m and a>m, smoothness of c is
impossible. Indeed write E:w=0 and E':w=u(t)t^m, u(0)!=0. The first
restriction has order greater than m, so f_t(0)=0 and smoothness of c
gives f_w(0)!=0. Taylor subtraction then makes

    f(t,u(t)t^m)-f(t,0)

have order exactly m, whereas both restrictions have order greater
than m. Thus a<=m. Summing all zeros gives

    2=H.E=c.E <= E.E' <= E.(D-E)=2.

Equality forces E to have no intersection with any other component of
D. The same holds for E'. Thus E union E' is a connected component of
D, disjoint from the nonempty conductor above the line, contradicting
section 4. This proves the theorem.

The proof requires neither a global deck involution nor ordinary pinch
points. In particular it includes conductor triple points, where an
earlier proposed eigenvalue-propagation argument was insufficient.

## 6. Failed extension and a local countermodel

It is unsafe to assume that a paired line component's attachment to
the remaining conductor is a different point from its mutual
intersection with its paired component. For example, over the nodal
base R=k[[x,y]]/(xy), the rank-two algebra

    R[eta]/(eta^2-x-y^2)

is the planar reduced curve

    y(eta-y)(eta+y)=0.

Its three smooth branches meet at one point. The two exchanged
branches eta=+/-y map to one base component; the stable branch y=0
maps by x=eta^2 to the other. A smooth section
f=alpha*y+beta*eta has an arbitrary ratio
(alpha-beta)/(alpha+beta) on the exchanged branches, and vanishes at
the common attachment point. Suitable root-of-unity ratios, together
with an even power on the stable branch, give local descended powers.
Thus reducedness, singleton fibers, and local smoothness do not alone
force equal branch eigenvalues. This model does not assert a global
quartic realization, and does not contradict section 5: its global
conic component has degree four on its degree-two cover, which supplies
the extra intersection contradiction there.

## 7. The conic-plus-line theorem includes every upstairs scheme

The reduced-D hypothesis of section 5 can be removed. This extension
was proposed by the normal-global-adversarial agent and independently
checked by the present author and root. Its separate written proof is
the [all-D independent audit](#source-2026-10-08-session-scroll-conic-line-independent-auditmd).

For every proper prime E<D, even when D is nonreduced, the sequence
0->O_S(-E)->O_S->O_E->0 gives

    H^1(O_E)=H^2(O_S(-E))=H^0(O_S(E-D))*=0.

The final vanishing holds because E-D is the negative of a nonzero
effective divisor on the projective integral S. Thus every proper
conductor prime is a smooth rational curve, and adjunction still gives
E.(D-E)=2, with all residual multiplicities retained.

Over the conic, the generic rank-two alternatives are:

* one prime E of multiplicity one and covering degree two;
* two primes E,E' of multiplicity one and covering degree one;
* one prime E of multiplicity two and covering degree one.

The first two cases are excluded by section 5 verbatim, allowing a
nonreduced remainder of D. The remaining doubled-conic case has H.E=2.
Write the two scroll polarizations as

    F0: H=C+2f, C^2=f^2=0, C.f=1;
    F2: H=C_min+3f, C_min^2=-2, C_min.f=1.

On F2 there is no prime of H-degree two. A prime other than C_min has
class a C_min+b f with a>=0, b>=2a. For a=0 a prime is a single fiber,
of degree one; for a>=1 its degree a+b is at least three. On F0, a
prime of degree two must be C-horizontal: its class is C. Indeed a
prime of class a C+b f has nonnegative a,b, H-degree 2a+b, and a=0
gives a single fiber.

Therefore the doubled-conic case occurs only on F0 and has

    D=2E+2f.

The residual conductor is either two distinct fibers F1,F2 or one
doubled fiber 2F. If F1,F2 are distinct, the points E intersect F1 and
E intersect F2 are distinct and both map to the unique node of the
conic-plus-line conductor. But nu|E is an isomorphism to the conic,
which is impossible. Hence D=2(E+F).

The reduced conic-plus-line curve Gamma is nodal and Gorenstein.
The exact sequence of section 2 makes p_*O_D locally free of rank two
over Gamma, since its quotient omega_Gamma is invertible. Trace splits
this algebra as O_Gamma direct-sum L, for an invertible L, with a local
trace-zero generator eta satisfying eta^2=Delta. Over both generic
components the upstairs conductor is a doubled prime, so Delta
vanishes generically on both components. Reducedness of Gamma forces
Delta=0 everywhere.

Write f|D=a+eta b in this trace splitting. The section a is generically
nonzero on every base component, because c is not a conductor prime.
The descended-power equality gives

    n a^(n-1)b=0.

Characteristic zero and torsionfreeness of the invertible trace-free
summand imply b=0 globally. Thus f itself descends through the entire
conductor square to O_X(1), and then to an ambient hyperplane. That
hyperplane would contain C0, a contradiction.

This proves the conic-plus-line theorem for every upstairs conductor
scheme. If only its downstairs reduced support is initially known to
be a smooth conic plus a line meeting once, it suffices: the support
already has degree three, so the pure CM conductor with polynomial
3m+1 has generic multiplicity one everywhere and no finite-support
nilradical. Its actual scheme is consequently reduced.

## 8. Three-line conductors: complete finite reduction

The following extension was independently audited by root and the
normal-global-adversarial agent. Its proof uses the actual generic
ranks and scroll divisor classes, not an unproved flat-cover assertion
at the nongorenstein concurrent point.

Assume Gamma is reduced with three line components. The exact sequence
of section 2 implies generic degree two over each line. Every proper
conductor prime is smooth rational by section 7 and has H-degree at
most two.

On F0 the only such primes are horizontal C-curves, of H-degree two,
and fibers, of degree one. Since D~2C+2f, there must be two distinct
horizontal primes C1,C2, each occurring once and covering different
base lines with degree two. The remaining cover over the third line
is either 2F or F+F' for two distinct fibers. The latter is impossible
under a mate: restrictions of f to F,F' are proportional after their
degree-one identifications with the same base line, and therefore
their zeros give two distinct normalization points over a point of
C0. Thus

    D=C1+C2+2F.

Since nu|F is an isomorphism to its base line and C1 intersect F and
C2 intersect F are distinct points, the three base lines cannot be
concurrent. They form the reduced noncoplanar chain. This Gamma is
Gorenstein, so the exact sequence makes p finite flat of rank two.
The trace discriminant vanishes identically on the central base line,
because its inverse conductor is 2F. Thus over each of the two base
nodes the finite fiber is eta^2=0 and has just one point. Each C_i
therefore maps with ramification to its line at its intersection with
F.

For a degree-two map C_i=P1->P1 there are two simple ramification
points. The singleton and differential arguments of section 5 imply
all points of c intersect C_i are these points, with multiplicity one.
Since c.C_i=H.C_i=2, both ramification points occur. In particular c
passes through both distinct points C1 intersect F and C2 intersect F,
contradicting c.F=H.F=1.

On F2 the only primes of H-degree at most two are C_min and individual
fibers, each of degree one. The class D~2C_min+4f forces C_min with
multiplicity two, covering one base line with degree one. The remaining
four fiber multiplicities provide two degree-two covers of the other
two base lines. A pair of distinct fibers over the same line is
impossible under a mate by the same paired-zero argument. Hence

    D=2C_min+2F1+2F2,

where F1,F2 are distinct fibers mapping to different base lines.
Their distinct intersections with C_min, which maps isomorphically
to its base line, again force Gamma to be a chain. The trace
discriminant vanishes generically on every component and therefore
globally on this reduced Gamma. The nilpotent-power argument in
section 7 makes f descend to an impossible ambient hyperplane.

These two reductions exclude every reduced three-line conductor under
the smooth-scroll hypotheses.
The concurrent case is not silently treated as Gorenstein: it is
eliminated by the divisor/fiber reduction before using a trace algebra.

## 9. Combined all-reduced-conductor theorem

**Theorem.** Let X be an integral quartic over an algebraically closed
characteristic-zero field, whose normalization is a smooth rational
quartic scroll. If its actual entire downstairs conductor is reduced,
then X cannot be a carrier of a set-theoretic complete-intersection
presentation of C0, in any positive mate degree. No reducedness
assumption on the upstairs anticanonical conductor is made.

Indeed the ACM cubic classification leaves a smooth twisted cubic,
a smooth conic plus a line meeting once, or three lines in a
noncoplanar chain or concurrent configuration. The smooth twisted
cubic case is proved in the
[entire-conductor applicability theorem](#source-2026-10-08-session-scroll-conductor-applicabilitymd).
Sections 5 and 7 cover the conic-plus-line case with every upstairs
scheme. Section 8 covers the three-line cases with every upstairs
scheme. The proof is a classification of the reduced ACM conductor
and actual prime divisors of D; no classification of all nonnormal
quartic normalizations is asserted.

## 10. Precise retained boundary

Nonreduced Gamma remains unresolved here. The pure CM/ACM cubic
statement must retain nilpotents and the entire Hilbert--Burch ideal.
No extension of the trace algebra or deck involution is asserted at a
nongorenstein cubic point.

An immediate application target is the unique principal e=1,d2=1
quartic at (p,r)=(8,1/2), whose Jacobian support is a plane conic that
splits into two lines. Its Jacobian scheme is not the conductor scheme.
In particular a degree-two reduced singular support does not satisfy
the conic-plus-line hypothesis above; the actual degree-three
conductor and normalization must be identified first.

Independent audit: the normal-global-adversarial agent separately
checked section 5, including the ramification differential at a
conductor triple point. The ACM and Hilbert--Burch calculation has its
own independent audit. These agreements are audits of the written
proof, not substitutes for its hypotheses or arguments.

## 11. Generic-Artin square compression for a Gorenstein conductor

This reduction is valid for a locally Gorenstein actual Gamma,
including nonreduced Gamma. The section 2 exact sequence then makes
p_*O_D locally free of rank two, with its global trace involution
sigma. Suppose sigma preserves every reduced prime of D. For a mate,
f is generically nonzero on every such prime, and

    (sigma(f)/f)^n=1

in its generic Artin ring. The characteristic-zero polynomial T^n-1
has only simple roots. Each ratio is therefore an actual constant
root of unity, with no nilpotent correction. Applying sigma twice at
the same prime gives that root's square equal to one. Thus f^2 is
sigma invariant at every generic associated point of D. Since D is
a Cartier Cohen--Macaulay divisor with no embedded associated points,
f^2 is invariant globally. The fixed algebra is O_Gamma, so the
entire conductor square descends f^2 to O_X(2), then to an ambient
quadric, contradicting the unique-quadric geometry of C0.

The hypothesis that sigma preserves the primes is substantive. When
sigma exchanges two primes, their generic ratios may be arbitrary
reciprocal roots of unity; applying sigma twice alone does not bound
their orders. The paired-zero arguments elsewhere in this note are
used to handle exactly that exception.

## 12. Accepted all-Gorenstein-conductor extension

The following finite reduction has a completed
[independent audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-gorenstein-independent-auditmd).
It extends section 9 from reduced Gamma to every locally Gorenstein
actual Gamma, retaining arbitrary D. It does not claim a locally
Gorenstein property for every ACM cubic.

A nonreduced pure degree-three Gamma has support either one line
with multiplicity three, or two lines with multiplicities two and one.
Its connectedness forces the two lines to meet. If Gamma were a
Gorenstein triple line, omega_Gamma would be invertible with

    deg(omega_Gamma)=2p_a(Gamma)-2=-2.

For any invertible sheaf M on a pure triple line, devissage through
the reduced line gives

    chi(M)-chi(O_Gamma)=3 deg(M|L).

Taking M=omega_Gamma makes -2 divisible by three, impossible. Thus
a nonreduced locally Gorenstein cubic has generic multiplicities
two on a line L and one on a different line M.

At the generic point of L, the conductor algebra is a free rank-two
algebra over K[epsilon]/(epsilon^2), K=k(L). Its total K-length is
four, and multiplication by epsilon has rank two. Each upstairs
generic factor is a DVR quotient t^a with residue extension degree r.
If epsilon has order k there, epsilon^2=0 gives k>=a/2. The total
rank equality forces k=a/2 in every factor. Hence a is even and the
only partitions of the upstairs total length are

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

This uses actual generic nilpotent lengths, rather than interpreting
the reduced upstairs support as a rank-two cover. Above M the usual
length-two alternatives apply.

On F0, the generic (4,1) alternative would require a degree-one
fiber with multiplicity four, contrary to D~2C+2f. The split
(2,1)+(2,1) alternative would likewise require four fiber
multiplicities and is impossible. The (2,2) alternative is 2E with
E a horizontal C-prime. The residual class is 2f over M. If it is
two distinct fibers, their disjoint paired zeros exclude a mate.
Otherwise D=2E+2F. The trace involution preserves both reduced
primes, so section 11 excludes every mate.

On F2 there is no degree-two prime. For (4,1), D=4F+2C_min, and the
trace involution preserves both primes, so section 11 applies.
For (2,1)+(2,1), the degree-one pair is either C_min and a fiber F,
or two distinct fibers F1,F2. In the latter case disjoint paired
zeros exclude a mate. In the former case the residual class 2f over
M is a doubled fiber or a pair of distinct fibers. Sigma exchanges
C_min and F and permutes the remaining fibers. But C_min meets each
remaining fiber, whereas F meets none of them. An automorphism of D
cannot map those nonempty intersections to empty intersections.
Thus this configuration is impossible for the global trace
involution, before assuming a mate.

Thus every smooth rational quartic-scroll normalization with locally
Gorenstein actual conductor is excluded. The boundary of this
particular argument is an actual nonreduced nongorenstein ACM cubic;
later sections address that boundary using additional structural
information. A concrete successful nonreduced example is the
[MF6 (8,1/2) conductor proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-rhalf-scroll-conductormd).

## 13. A cover of a support line cannot have degree at least three

Let E be any proper prime component of the actual D and suppose its
reduced map to a line in P3 has degree r>=2. This lemma does not require
Gamma reduced or Gorenstein, nor a trace algebra. Section 7 makes
E a smooth rational curve. If c meets E, the singleton-fiber condition
makes its point the sole point of the entire degree-r fiber on E.
The finite map P1->P1 is separable in characteristic zero, so its
ramification index there is r. Its differential vanishes, and therefore
dnu annihilates the tangent line of E. The immersion of c into its
smooth image forces c transverse to E, with local intersection one.

Riemann--Hurwitz gives total ramification degree 2r-2. Each possible
intersection consumes r-1 of that budget, so at most two such points
exist. But c~H and E maps to a line, giving

    c.E=H.E=r.

Thus r<=2. Every prime cover of a support line of degree at least three
is excluded under a mate, including a degree-three prime in a
nonreduced triple-line conductor. This is a necessary geometric
obstruction; it does not classify the remaining degree-one and
degree-two prime configurations.

## 14. Generic descent extends across a nongorenstein conductor point

The normalization duality proof in section 2 gives the whole
normalization quotient

    0 -> O_X -> nu_*O_S -> omega_Gamma -> 0.

For every m it therefore identifies the descent obstruction of a
global section s of O_S(mH) with its image in omega_Gamma(m). The
canonical module of the pure CM curve Gamma is again Cohen--Macaulay
and has no nonzero finite-support submodule. Consequently, if s
descends at every generic point of the actual Gamma, with its full
Artin scheme structure retained, its global obstruction vanishes.
It descends everywhere on X.

This does not replace actual Gamma by its normalization or its reduced
support. It says that generic descent through the entire Artin
conductor algebra is enough for an existing global section on S.
It removes the need to construct a global deck involution at a
nongorenstein conductor point.

## 15. A doubled crossing forces squared eigenvalues to agree

Suppose E and E' are smooth transverse conductor primes, each with
multiplicity two, meeting at P. Assume their image lies in an open
Gorenstein part of Gamma and the local trace involution sigma exchanges
them. Choose regular parameters u,v at P with E={u=0}, E'={v=0}.
Suppose f defines the smooth c and its descended power gives generic
Artin-ring ratios

    sigma(f)=zeta f on 2E,
    sigma(f)=zeta^-1 f on 2E'.

These are equalities on the entire generic doubled schemes, not just
on their reduced fields. In the local ring of D, whose equation is
u^2 v^2, their differences belong respectively to (u^2) and (v^2).
Subtracting gives

    (zeta-zeta^-1) f in (u^2,v^2).

If zeta^2!=1, then f has no linear term, contrary to smoothness of c
at P. Hence zeta^2=1, and f^2 is generically invariant on both doubled
branches. This argument is stronger than the reduced crossing case,
where arbitrary reciprocal roots are locally possible.

## 16. Proposed exclusion for every double-line-plus-line conductor

The reduction in section 12 needs a global Gorenstein hypothesis only
to control the split C_min+fiber configuration on F2. Sections 14--15
suggest removing that hypothesis entirely for Gamma supported on two
lines with multiplicities two and one. The generic Artin partitions
still hold, since the actual multiplicity-two conductor is Gorenstein
at its generic point and the rank-two algebra is free there.

In the F0 and F2 configurations with a unique upstairs prime over each
base component, the generic trace action preserves both primes.
Section 11 therefore makes f^2 descend at each actual generic scheme
point. Section 14 extends that descent globally, without any global
trace involution.

The only additional configuration is

    S=F2, D=2C_min+2F+2F',

where C_min and F map isomorphically to the doubled line L, and F'
maps isomorphically to the other line M. Their restrictions of f have
the same zero, so c passes through P=C_min intersect F. The point
Q=C_min intersect F' maps to L intersect M. Since P and Q are
different and nu|C_min is an isomorphism, P maps away from the line
intersection. A pure CM double curve with smooth line support is a
ribbon away from M, hence locally Gorenstein there. Thus its local
trace involution exists near P and exchanges the two doubled primes.
Section 15 forces zeta^2=1. The remaining doubled fiber has an identity
reduced trace action and makes f descend generically there. Hence
f^2 descends at every actual generic scheme point and, by section 14,
globally. The usual quadric contradiction follows.

This extension was independently checked by the
normal-global-adversarial agent, while the direct Artin reduction in
[the independent audit](#source-2026-10-08-session-scroll-artin-independent-auditmd)
provides another route through this case. It retains the generic Artin
lengths and the local doubled branches; a reduced-support argument
alone would not prove it. Triple-line conductors remain outside this
extension.

## 17. Proposed entire smooth-scroll closure by the differential obstruction

This alternate transverse-plane proof is retained as an independent
research route, with its geometric slice passage still explicitly
unpromoted. The exact Artin proof in
[nongorenstein cubic classification](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-cubic-classificationmd)
and its [independent audit](#source-2026-10-08-session-scroll-artin-independent-auditmd)
avoid this passage. The
[differential obstruction audit](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-normalization-differential-independent-auditmd)
independently proves its first step: under a mate, nu must be
generically immersive along every proper conductor prime E. If its
generic differential rank were at most one, choose P in c intersect E
(nonempty since c~H is ample). Rank at P is also at most one. Rank zero
contradicts the immersion of c. For rank one, ker(dnu) restricted to E
is a regular line subbundle near P. Trivialize H by a nonvanishing
ambient hyperplane section. The identity nu*G=lambda f^n gives

    n f^(n-1) df(K)=0 on E.

Since f is not identically zero on E and characteristic is zero,
df(K)=0 on E, including P. Smoothness of c now makes its tangent equal
to ker(dnu), again contradicting the immersion of c.

At the generic point of a conductor support line, complete the
one-dimensional hypersurface local ring and extend its residue field
to an algebraic closure. This is a reduced plane-curve singularity
transverse to the line. Separability of the prime's map to the line
gives a nonzero longitudinal differential. Hence generic rank two of
nu means each geometric transverse branch is smooth: at least one
of its two normal coordinates has nonzero linear term.

The actual multiplicity m of Gamma along that support line equals
the transverse delta invariant. Indeed B/A=omega_Gamma has residue
field length m, the same length as the canonical module of the
Artin conductor quotient A/I. For smooth plane branches, delta is
the sum of pairwise intersection multiplicities, and the conductor
order on each branch is the sum of its intersections with the other
branches. These two formulas can be proved directly. The
Mayer--Vietoris sequence for a branch and the union of the others
adds its intersection multiplicity to the normalization defect.
For the conductor formula, choose a projection x which is a parameter
on every smooth branch fi. The hypersurface canonical generator
dx/(partial F/partial y), F=product fi, has on branch i a pole of
order sum_{j!=i} I(fi,fj); finite canonical duality gives precisely
that conductor order. No classification of arbitrary singular plane
branches is required, because the differential obstruction already
excludes them under a mate.

### Double-line-plus-line support

Here the generic deltas are two on L and one on M. At L, smooth
branches with total pair contact two must be two branches of contact
two, with conductor order two on each. At M, delta one means two
smooth transverse branches, with conductor order one on each.

On F0, the thick-line orbit of two branches is either a single
H-degree-two prime with multiplicity two, or two H-degree-one primes
of multiplicity two. The second would require four fiber
multiplicities, impossible in D~2C+2f. The first is 2C and leaves
2f. Since the other support line has a node, this residual cover must
be two distinct fibers with multiplicity one. Their paired zeros
contradict full singleton fibers.

On F2 there is no H-degree-two prime. The thick-line branches are two
degree-one primes with multiplicity two. If they are C_min and F,
the residual 2f over M is again a pair of distinct fibers and is
excluded. If they are two fibers, the residual 2C_min cannot realize
a nodal cover of M: it is neither one degree-two prime of multiplicity
one nor two distinct degree-one primes. Thus every double-line-plus-line
conductor is excluded, including nongorenstein points.

### Triple-line support

The generic delta is three. With all geometric branches smooth there
are only two possibilities: two branches with contact three, having
conductor order three each; or three branches with all pairwise
contacts one, having conductor order two each.

In the two-branch case, one degree-two prime of multiplicity three
would violate the C-coefficient bound on F0 and the absence of a
degree-two prime on F2. Two distinct degree-one primes of multiplicity
three would require either the unique C_min with coefficient three
on F2, or six fiber multiplicities on either scroll. All are
incompatible with D~-K.

For three ordinary branches, their residue-field orbits have sizes
three, two-plus-one, or one-plus-one-plus-one. A single degree-three
prime of multiplicity two is excluded by section 13. For the
two-plus-one orbit, only F0 permits the class: D=2E+2T with E a
horizontal degree-two prime mapping to the line and T a degree-one
fiber mapping to that same line. The two points of c intersect E
must be its two simple ramification points, with distinct branch
values. The mate vanishes at both values on the common base line,
so its pullback on the isomorphic T also vanishes at both points.
This contradicts c.T=H.T=1.

For three degree-one primes, only F2 permits the class:
D=2C_min+2F1+2F2. Each restricted f is a linear section pulled back
from the common support line. The descended power forces their zeros
to have the same base value. The two distinct fibers F1,F2 then
contain two different points of c in the same normalization fiber,
a contradiction.

Together with the accepted reduced-conductor theorem, this argument
would exclude every smooth rational quartic-scroll normalization in
any mate degree. The remaining audit is the exact passage from the
generic hypersurface ring to the geometric transverse branch
partition; all divisor and full-fiber cases above have been stated
with their actual conductor orders. This does not classify singular
scroll normalizations or all nonnormal quartic carriers.


---

## Source: 2026-10-08-session-scroll-entire-conductor-verification-audit.md

# Verification audit: all actual conductors on smooth rational quartic scrolls

Date: proof audited 2026-10-08; evidence record completed at the 2026-10-09 continuation. Auditor: `verification`. Status: **PROVED HERE**, independently accepted all-mate exclusion for the specified carrier class. No canonical frontier file is edited.

## Statement and antecedents

Let X be an integral quartic in P3 over an algebraically closed field of characteristic zero. Suppose its finite normalization is a smooth rational quartic scroll S with polarized class

    F0: H=C+2f, D~-K_S=2C+2f;
    F2: H=C_min+3f, D~-K_S=2C_min+4f.

Here D is the entire Cartier conductor divisor and Gamma is the entire downstairs conductor scheme. Then X has no mate of any positive degree presenting the fixed smooth rational quartic C0=[s^4:s^3t:st^3:t^4] as its set-theoretic intersection.

This audit uses the independently established conductor antecedents: Gamma is pure ACM with polynomial 3m+1, its ideal has the linear Hilbert--Burch resolution with three quadratic generators and two cubic syzygies, and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

A mate supplies a single smooth c~H, nu|c an isomorphism to C0, full singleton normalization fibers over C0, and the entire identity nu^*G=lambda f^n with div(f)=c. The reduction retains all conductor multiplicities. Every proper conductor prime E is smooth rational by H1(O_E)=H0(O_S(E-D))*=0. Since D has H-degree six while Gamma has degree three, its conductor prime configurations below are proper, rather than D itself.

The all-reduced-conductor theorem and the independently audited [all-locally-Gorenstein theorem](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-gorenstein-independent-auditmd) were accepted separately. This note checks the remaining nonreduced nongorenstein schemes directly, rather than invoking a classification of all quartic surfaces or the alternative transverse-completion argument in section 17 of the owner note.

## 1. Whole nongorenstein ACM cubic classification

For the 3-by-2 linear Hilbert--Burch matrix M, rank one at a point gives a unit entry and a local codimension-two complete intersection. Rank zero gives a minimal local resolution with last rank two and a canonical module with two generators. Thus the nongorenstein locus is exactly the common zero locus of the linear entries.

Let W be the span of the entries. Its dimension is at least two because the minors have height two. If dim W=4 there is no projective rank-zero locus, so the entire curve is locally Gorenstein and already excluded. If dim W=3, coordinates give W=<x,y,z> and the ideal is the cone, with vertex the w-point, over a length-three scheme Z in P2. The homogeneous ring k[x,y,z]/J is dimension one Cohen--Macaulay, hence J is saturated. Its Hilbert series is (1+2t)/(1-t), and J has no linear element. Saturation therefore makes Z noncollinear; merely knowing h0(O_Z(1))=3 would not suffice.

A length-three scheme on a smooth surface has three distinct points, one double point plus a distinct point, a curvilinear length-three point, or a length-three point with two-dimensional square-zero maximal ideal. Noncollinearity respectively means the points are noncollinear, the third point misses the double point's tangent line, or the curvilinear point has nonzero second-order departure from its tangent line. Projective coordinate changes and scaling give the four cone ideals

    (xy,xz,yz), (y^2,xy,xz), (x^2,xy,y^2-xz), (x^2,xy,y^2).

The first is reduced and already excluded. For the last case only two linear variables are needed. Conversely, if dim W=2, the three independent quadratic minors span Sym^2(W), giving exactly the final ideal. Independence follows from the Hilbert--Burch resolution and its three minimal quadratic generators. These arguments exhaust the whole nongorenstein ACM cubic schemes over the stated field.

## 2. Curvilinear triple line: divisible-by-three obstruction

At its generic point, A=K[epsilon]/epsilon^3 and omega_A is free of rank one. The canonical exact sequence therefore makes B free of rank two over A. B has K-length six and multiplication by epsilon has rank four.

Write a generic conductor factor as K_i[t]/t^a, r=[K_i:K], and k=ord_t(epsilon), allowing k=a if the image is zero. Its K-length is ar and its multiplication rank is r(a-k). Since epsilon^3=0, a<=3k. The sum of the ranks reaches the upper bound (2/3)*6=4, so equality holds in every factor: a=3k. Every actual prime multiplicity of D is divisible by three. Then the divisor class of D is divisible by three in the torsion-free Picard group, contrary to its C-coefficient two. This excludes the actual curvilinear triple-line conductor before imposing a mate.

No reduced-cover interpretation or global flatness at its nongorenstein vertex is used.

## 3. Fat triple line: the canonical-module and annihilator steps

For the fat triple line, A=K+N with dim_K N=2 and N^2=0. In omega_A=Hom_K(A,K), multiplication by N has image the one-dimensional span of 1*. Let T=NB. The canonical exact sequence gives dim_K B=6, and the image of T in B/A is N omega_A, of dimension one.

The ideal T contains N. Since T^2=0, T intersect A contains no element with nonzero scalar part: such an element is a unit in A, hence a unit in B, contradicting square-zero. Thus T intersect A=N, and dim_K T=2+1=3.

B is a product of truncated DVR algebras over finite separable residue extensions of K. It is Frobenius over K: on K_i[t]/t^a the pairing takes the field trace of the coefficient of t^(a-1) in a product. It is nondegenerate, so every ideal T satisfies dim Ann_B(T)=dim B-dim T. Our T is square-zero and three-dimensional, hence

    T subset Ann_B(T), dim T=dim Ann_B(T)=3,
    T=Ann_B(T).

An ideal in a truncated DVR factor is (t^k), with annihilator (t^(a-k)). Equality forces a=2k separately in every factor. In particular no odd prime multiplicity or zero ideal factor is omitted. Every coefficient of the actual D is even, so

    D=2E, E~C+f on F0, E~C_min+2f on F2.

This Frobenius argument is applicable to B, which is a product of DVR quotients; it does not assert that the nongorenstein algebra A is Frobenius or that B is free of rank two over A.

## 4. Effective divisor and full-fiber exclusions for the fat line

A prime mapping to the support line with degree r has H-degree r. For r>=2 every point of c intersect that prime must be a totally ramified point, since the entire normalization fiber is a singleton. The ramification derivative annihilates its tangent, whereas nu|c is immersive, so c meets the prime transversely at each such point. There are consequently r distinct totally ramified points. Their contribution r(r-1) cannot exceed the Riemann--Hurwitz total 2r-2; r>=3 is impossible.

On F0 the effective class C+f is a prime of degree three or a horizontal C-prime plus one fiber. The prime is excluded above. In the split case, the degree-one fiber restriction of f has one zero on the common base line. Equality of the full descended n-th powers forces the zero divisor on the degree-two horizontal prime to be the pullback of that one zero. Singleton fibers make it one totally ramified point of multiplicity two, while immersion of c requires transverse intersection one. This is a contradiction.

On F2, any prime other than C_min has class a C_min+b f with b>=2a; fibers are individually prime only with class f. Thus C_min+2f is either a degree-three prime, C_min+F1+F2 for distinct fibers, or C_min+2F. The prime case is excluded by the ramification argument. The distinct fibers have proportional nonzero restrictions of f, because their n-th powers descend to the same line. Their equal zero on the base gives distinct points of c in one normalization fiber, impossible.

The remaining actual divisor is D=2C_min+4F. In its generic F-factor B_F=K[t]/t^4 the preceding self-annihilator computation gives NB_F=(t^2). Ambient coordinates normal to the support line have classes in N, so their actual pullbacks vanish to order at least two along F: the equality modulo the conductor (t^4) implies actual membership in (t^2). The longitudinal coordinate has nonzero derivative because F maps isomorphically to the line. Hence dnu has generic rank one on F. The [independent nonimmersion-prime lemma](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-nonimmersion-prime-independent-auditmd) excludes the mate. This step verifies derivative rank from the actual generic algebra; multiplicity four alone would not do so.

## 5. Doubled line plus reduced line, including the nongorenstein vertex

At the thick line L, A=K[epsilon]/epsilon^2 is generically Gorenstein, so B is free of rank two there. Its length four and epsilon-rank two give the complete partitions

    (a,r)=(4,1), (2,2), or (2,1)+(2,1),

with epsilon order a/2 in every factor. In the (4,1) factor, normal coordinates to L belong to the nilradical (epsilon) and therefore have actual valuation at least two on its prime. The nonimmersion lemma excludes this case under a mate.

At the reduced line M, total generic length two gives

    (a,r)=(2,1), (1,2), or (1,1)+(1,1).

In the doubled-prime case (2,1), normal coordinates to M vanish in A=K and thus belong to the actual conductor (t^2). This also gives generic rank at most one and is excluded. Hence all prime multiplicities over M are one under a mate.

On F0 the only H-degree-two prime is a horizontal C-prime and the only degree-one primes are fibers. The split thick-line partition consumes four fiber multiplicities, contrary to D~2C+2f. Thus L has 2C and the residual 2f over M must be two distinct multiplicity-one fibers. A degree-two prime cannot have fiber class, and a doubled fiber is already excluded. Their disjoint paired zeros contradict singleton fibers.

On F2 there is no degree-two prime. The thick-line split is either 2C_min+2F or 2F1+2F2. The first leaves class 2f over M, again forcing the excluded disjoint fiber pair. The second already has disjoint paired zeros over L; alternatively its residual 2C_min over M cannot be a degree-two prime, two distinct primes in the unique C_min class, or the excluded doubled prime. This exhausts the actual classes.

Every step takes place at the actual generic Artin scheme or on the smooth normalization. It does not extend a deck involution through the nongorenstein vertex, invoke flatness there, or assume a scheme-theoretically reduced conductor.

## Audit decision and limits

The nongorenstein ACM classification, the generic canonical modules, the rank equalities, Frobenius annihilator argument, effective divisor exhaustion, full-fiber contradictions, and actual-coordinate differential conclusion all pass independent verification. Together with the accepted reduced and locally Gorenstein cases they prove the stated exclusion for every smooth rational quartic-scroll normalization.

The theorem is for carriers of this fixed C0 and this polarized normalization class. It does not prove that every integral nonnormal quartic has such a normalization, does not include singular normalizations, and does not resolve the global STCI problem. The supporting exact script checks concrete normal forms and finite ranks; its PASS is not the reason the complete geometric theorem is accepted.

Source and execution provenance are preserved in `research/validation/2026-10-09-scroll-entire-audit/audit-manifest.json`. The independent supporting generic-length source retains explicit countermodels showing that nonreduced Gamma need not have zero discriminant and a deck involution need not preserve every prime.
