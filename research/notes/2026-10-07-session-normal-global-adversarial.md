# Global adversarial audit of the normal-quartic carrier exclusion

Date: 2026-10-07. Status: **ACCEPTED under the recorded classification,
ADE-pair and prior small-mate exclusion inputs**. This audit found no
gap in the global geometry of the normal-quartic argument. It does not
replace the two independent numerical enumerations by a third run.

The audited statement is precisely:

> Over every algebraically closed field of characteristic zero, an
> integral normal quartic surface containing the fixed smooth curve
> C0=[s^4:s^3t:st^3:t^4] cannot participate in a set-theoretic
> complete-intersection presentation of C0, in any mate degree.

This statement does not say that C0 is not a set-theoretic complete
intersection. Nonnormal quartics, higher carrier degrees and the
entirely-thick branches retain their separate unresolved status.

The central proof is
`2026-10-06-session-normal-carrier-progress.md`; the numerical proof
audits are `2026-10-07-session-normal-carrier-independent-audit.md`
and `2026-10-07-session-normal-nonreduced-independent-audit.md`.
The present audit reread those notes, the normal-resolution compression
proof, the earlier normal-quartic classification reduction and the
normal-sheaf defect proof. It refreshed the published primary source.

## 1. Coverage of the surface classification

The [published Ishii–Nakayama paper](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf)
was checked at §1.1, §2.4, the Main Theorem, and §3.3.2–3.4.
The Main Theorem on printed p.955 gives exhaustive constructions.
Rational resolutions have types B1, B2, B3 or D. A possible apparent
exception is the rational ruled case considered during §3.3.2:
printed p.963 explicitly contracts its distinguished section and
identifies its separation with Type D. It supplies no omitted rational
Type-C class. The positive-genus ruled cases have hyperplane degree at
most three on the ruling; the cone case has degree one.

The distinction between a rational singularity and a rational *whole
resolution* is respected. Jaffe's accepted rational-singularity theorem
disposes of the K3/ADE quartics. On a resolution ruled over a
positive-genus curve, any morphism from the rational curve c to the base
is constant. Thus c is a component of a fiber. Nefness of H and its
fiber degree at most three forbid H.c=4, even on a reducible special
fiber. This does not require a mate and does not confuse a rational
component of a fiber with a section over the positive-genus base.

The remaining rational minimal resolutions have K_M linearly equivalent
to -E, with E effective and exceptional, d=-E^2 in {1,2,3}, and
Picard number 10+d. No assumption that E is reduced is introduced.

## 2. The strict curve and the actual passage vector

The rational lift C --> M is defined at the generic point, since a
normal surface is regular at the generic point of C and its singular
locus is finite. Properness of M -> S extends the lift at every point
of the smooth curve by the DVR valuative criterion. The resulting map
is a section of M x_S C -> C. Its image c is a closed embedded copy of
C; the image in M is the strict transform. Consequently c is smooth
rational, and exactly one point of c lies above each point of C.

At a singular point p, every f in m_(S,p) vanishes along every
exceptional prime in its fiber after pullback. In the regular local ring
of M at the point of c, the product of the distinct prime local
equations divides this pullback. Intersection multiplicities with c are
therefore bounded above by the order of f|C. The closed immersion
C -> S makes O_(S,p) -> O_(C,p) surjective, so there is an f whose
restriction is a uniformizer and has order one. The exceptional fiber
is nonempty at that lifted point. Hence the sum of the intersection
lengths is exactly one.

This proves, rather than assumes, that c meets precisely one
exceptional prime transversely at a smooth point away from other
primes. A singular prime germ or a crossing cannot contribute length
one to the required sum. It also proves that the vector m used in
the correction calculation is a standard basis vector at each
singular point. It is not permissible to replace it by an arbitrary
nonnegative vector; the enumerations do not do so.

## 3. Why coefficient-zero exceptional curves do not hide another fiber

For any exceptional prime P on the minimal resolution, let b=-P^2>0.
Adjunction gives K_M.P=b+2p_a(P)-2. This is nonnegative: the only
negative possibility is a smooth rational (-1)-curve, forbidden by
minimality. If the coefficient of P in E is zero, then
K_M.P=-E.P<=0 because distinct effective curves intersect
nonnegatively. Equality follows, forcing b=2 and p_a(P)=0.
Furthermore E.P=0 forces P to be disjoint from every positive
coefficient component of E.

Since E is connected on the rational surface and exceptional fibers
of a proper resolution of a normal surface are connected, its support
is the full exceptional fiber of one nonrational singular point.
Every other fiber consists only of coefficient-zero (-2)-curves and
has zero canonical discrepancy. The accepted Gorenstein surface
classification identifies these fibers with ADE fibers. Thus the
decomposition into one E-fiber and separate ADE fibers is justified;
there is no attached discrepancy-zero curve omitted from the E matrix.

The prior avoidance argument uses the same distinction correctly:
if c avoids E, its square is -2 and its mate correction has square
six; the ADE rank bound then contradicts that correction. Hence a
hypothetical mate forces an actual passage through E.

## 4. Numerical pullback, compression and necessity

An ambient mate of degree b restricts to an effective Cartier divisor
whose full support is C. Because both C and S have degree four, that
divisor is bC. On M its pullback is b*c plus integral exceptional
coefficients. Its intersection with each exceptional prime is zero.
Thus those coefficients are b times the unique numerical correction
Z, and c+Z is numerically equivalent to H.

Write A for minus the full exceptional intersection matrix,
z=A^-1*m, t=c.E and q=m^T*A^-1*m. Adjunction gives c^2=t-2;
orthogonality and H^2=4 give t+q=6. The Cauchy inequality
t^2<=d*q follows in the *full* positive definite matrix, including
the separate ADE blocks and the zero coefficients of E on them.
Equality forces z to be proportional to the coefficient vector of E;
its stated proportionalities are integral, so the plane compression
in the equality cases is valid.

Compression is conditional on the original mate and uses the
rationality of the entire resolution. If n clears every coefficient
of Z, then n(H-c-Z) is an integral numerically trivial divisor on M.
On a smooth projective rational surface numerical equivalence equals
linear equivalence: this holds on a minimal rational surface and is
preserved by each blowup. Pushing a principal divisor down gives
nC linearly equivalent to nH on the normal S. In particular nC is
effective Cartier. Its section lifts to an ambient form by
H^1(P^3,O(n-4))=0. This gives an actual degree-n mate with full
support C, so the accepted small-mate exclusions apply.

This step neither asserts that numerical coincidence constructs a mate
on an arbitrary carrier nor cancels torsion on a nonrational surface.
The use of the *full inverse-column denominator*, including the ADE
blocks, is essential. Extra exceptional fibers not met by c have zero
correction and do not change that denominator.

## 5. The reduced and nonreduced reductions are necessary supersets

For an irreducible E=aP, the integer d=a^2*(-P^2)<=3 forces a=1.
The passage lemma applies even if the arithmetic-genus-one prime is
nodal or cuspidal: c cannot meet its singular point. The nonrational
point uses at least two first-normal orders. Indeed order one would
give a quadratic term x*(a*y+b*z)+Q(y,z) with (a,b) nonzero after
straightening C. Its rank is at least two because the x-axis is
contained in the hypersurface. Formal splitting produces an A_n
isolated singularity, contrary to nonrationality. Thus the stated
ADE budget at most seven is justified without a cusp classification.

For reduced reducible E, component adjunction gives a connected
degree-two intersection multigraph. Arithmetic genus and connectedness
force smooth rational primes and the stated cycle matrices, including
the two-component intersection-two case. Tangencies are not silently
discarded: only the matrix is used, and smooth passage avoids their
intersection points. The independent enumeration eliminates the
necessary cycle/ADE superset. Its last row is excluded by the accepted
normal-sheaf defect formula; the direct A2 chart calculation genuinely
principalizes the curve ideal and gives the contribution 1/3. Together
with six node contributions 1/2, this exceeds the global allowance
three. Further point contributions are nonnegative.

For nonreduced E, each proper effective D<E has
H1(O_D)=H0(O_M(D-E))^*=0 on the rational M. The reduced support is a
proper connected subdivisor, so has arithmetic genus zero. Prime
adjunction and connectedness force a smooth rational SNC tree with
unit intersection edges; a triple meeting would give a triangle and
is impossible. Minimality gives b_i>=2. The equations
A*a=b-2 and d=sum a_i*(b_i-2)<=3 imply total diagonal excess at most
three and at most 9+d vertices. This is the finite necessary graph
space used by both enumerations. No geometric realizability of a
retained graph is assumed. The independently verified surviving
property d=3,t=2 is therefore a legitimate necessary restriction.

## 6. Type D is an ideal calculation, not just a divisor-class prediction

The published source on p.955 provides the Type-D hyperplane basis:
xi0=phi4 and xi1,xi2,xi3=phi3*rho^*(x,y,z), where phi3 defines the
entire divisor E and phi4 defines D. Condition C makes D disjoint
from E. The source identifies its image as p=(1:0:0:0).

Consequently xi0 is a unit near E in a local trivialization of H.
The three affine coordinates of S at p pull back to
(phi3/phi4)*rho^*(x,y,z). The latter coordinate sections have no
common zero on M; locally one is a unit. Therefore the pulled-back
maximal ideal is exactly the invertible ideal O_M(-E), with all
multiplicities retained. This is stronger than equality of reduced
zero sets and is the required conclusion.

Restriction to the embedded smooth c takes the maximal ideal of p to
the order-one maximal ideal of the curve. Restricting O_M(-E) has order
c.E. Thus t=1 for *every* smooth curve through this Type-D point.
The d=3 classification is exhaustive, so this contradicts every
remaining nonreduced graph row t=2. No assumption about the first-normal
Jacobian order of a coefficient-two passage is used.

## 7. Transfer to every algebraically closed characteristic-zero field

Let a hypothetical pair and its normal integral quartic carrier exist
over such a field K. Descend its finitely many coefficients together
with finite radical-equality witnesses to a finitely generated subfield
k0: F and G belong to the fixed ideal of C0, and a positive power of
each generator of that ideal belongs to (F,G). These are polynomial
identities and survive every field extension.

An algebraic closure k0bar embeds into K. Since the carrier becomes
integral and normal over K, faithful-flat descent gives those
properties over k0bar. Thus it is geometrically integral and normal
over k0. The field k0 embeds into C, and that embedding extends to
k0bar. Base changing to C preserves geometric integrality and normality,
as well as the finite radical-equality identities. C0 itself is defined
over Q and remains the same smooth quartic. This produces the forbidden
complex pair.

This argument does not specialize arbitrary parameters, infer a
resolution's rationality after specialization, or impose an
uncountability hypothesis on K. The classification and the analytic
ADE inputs may therefore be used over C and transported by
contradiction. Characteristic p is outside this statement.

## 8. Audit decision and remaining scope

The global implications are accepted with their explicit antecedents:
the primary normal-quartic classification; Jaffe's rational-singularity
and smooth ADE-pair inputs; the audited C0 normal bundle; the prior
mate-degree exclusions through five; the normal-sheaf comparison; and
the two independent finite cycle/tree enumerations. Agreement of
agents or scripts is not substituted for any of these geometric inputs.

The classification coverage, smooth passage, coefficient-zero
separation, denominator compression, Type-D ideal equality and field
transfer each survive the adversarial checks above. No actual gap was
found. The conclusion remains confined to integral normal quartic
carriers of fixed C0 in characteristic zero, with no global STCI or
novelty claim.
