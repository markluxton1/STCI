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
