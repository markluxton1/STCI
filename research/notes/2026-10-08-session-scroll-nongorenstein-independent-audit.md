# Independent audit: the remaining nongorenstein scroll conductors

Date: 2026-10-08. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**, subject to the audited smooth
quartic-scroll hypotheses stated below. This completes that class of
carriers. It does not classify all nonnormal quartic surfaces or settle
the unrestricted STCI problem.

Audited owner sources:

- [Nongorenstein classification and triple-line proof](2026-10-08-session-scroll-nongorenstein-cubic-classification.md), sections 1--5.
- [Degenerate conductor proof](2026-10-08-session-scroll-degenerate-conductor.md), sections 14--16.
- [Independent differential obstruction](2026-10-08-session-normalization-differential-independent-audit.md).
- Earlier independent ACM, reduced-center, and locally Gorenstein audits.

## 1. Hypotheses and the exact conductor algebras

Work over an algebraically closed field k of characteristic zero. Let
X subset P3 be an integral quartic with finite smooth normalization
nu:S->X, where S=F_e, e=0 or 2, and

    H=C+a f,  a=e/2+2,  C^2=-e.

Here H=nu^*O_X(1) is ample and has degree one on a ruling fiber. The
actual entire conductor is a Cartier divisor D=-K_S upstairs and a
pure Cohen--Macaulay ACM cubic Gamma downstairs, with Hilbert polynomial
3m+1 and Hilbert--Burch resolution

    0 -> O(-3)^2 -> O(-2)^3 -> J_Gamma -> 0.

Absolute finite duality and the common conductor ideal give the exact
sequences retaining the entire nonreduced schemes

    0 -> O_X -> nu_*O_S -> omega_Gamma -> 0,
    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

No local freeness is inferred at a nongorenstein point. At a generic
point with residue field K, the second sequence says B/A=omega_A.
Since S is smooth and D Cartier, B is a product of truncated DVR
algebras L_i[t_i]/(t_i^a_i), with finite separable residue extensions
L_i/K. The multiplicity of the corresponding prime of D is a_i.
Coefficient fields compatible with K can be chosen in these Artin
algebras because the residue extensions are separable.

A mate for C0 supplies a smooth c~H, an isomorphism nu|c onto the
smooth embedded C0, singleton normalization fibers over every point
of C0, and the entire equality nu^*G=lambda f^n, div(f)=c. Every prime
of D is distinct from c and has positive H-degree. Every proper prime
E<D is a smooth rational curve: H1(O_E)=H0(O_S(E-D))*=0, and an integral
projective curve of arithmetic genus zero is smooth rational.

## 2. The nongorenstein classification is complete

For the linear 3-by-2 Hilbert--Burch matrix M, a rank-one point has a
unit entry and a local codimension-two complete intersection. At a
rank-zero point the resolution is minimal with last rank two, hence
canonical type two. Thus its entries' common projective zero locus
is exactly the nongorenstein locus.

Let W be the span of the linear entries. Its dimension is at least
two. If dim W=4 there is no projective rank-zero point. If dim W=3,
choose W=<x,y,z>; the ideal is a cone over a length-three subscheme Z
in P2. The ring k[x,y,z]/J is Cohen--Macaulay of dimension one, so J
is saturated, and J_1=0. This last statement, together with saturation,
proves that Z is noncollinear. Merely knowing h0(O_Z(1))=3 would not
prove noncollinearity; this repair has been supplied to the owner.

A noncollinear length-three scheme is either three distinct points,
a double point and a point off its tangent line, a curvilinear triple
point with a nonzero quadratic departure from its tangent line, or
a noncurvilinear fat point. Coordinates give the whole cone ideals

    (xy,xz,yz),
    (y^2,xy,xz),
    (x^2,xy,y^2-xz),
    (x^2,xy,y^2).

The last is the dim W=2 case: the three independent minors span
Sym^2(W), so its whole ideal is (x,y)^2. The remaining dim W=3 cases
have a unique nongorenstein vertex. This proves that the unresolved
nonreduced nongorenstein schemes are precisely double-line-plus-line,
curvilinear triple line, and fat triple line.

As a literature consistency check, the three ideals are the minors
of matrices A^(6), A^(7), A^(8) listed on printed page 4 of
[Lehn--Lehn--Sorger--van Straten, Twisted cubics on cubic fourfolds](https://www.math.sciences.univ-nantes.fr/~sorger/assets/pdf/twistedcubicscubicfourfolds.pdf).
The elementary classification above supplies the field-independent
proof needed here.

## 3. Curvilinear triple line: impossible even before a mate

Its generic algebra is A=K[epsilon]/(epsilon^3), which is Gorenstein.
The canonical module is free of rank one, so B/A=omega_A makes B free
of rank two over A. Its K-dimension is six and multiplication by
epsilon has rank four.

In a factor L_i[t]/(t^a), let epsilon have valuation k. The equality
epsilon^3=0 implies a<=3k. Its multiplication rank is
[L_i:K](a-k), at most (2/3)[L_i:K]a. Summing these inequalities gives
equality, since the total rank is four and total length is six.
Therefore equality holds in every factor and a=3k throughout.
A zero epsilon in a nonzero factor has strictly smaller rank and
cannot occur. Every multiplicity of D is divisible by three.

Thus D is three times an integral divisor. But
D=2C+(e+2)f has C-coefficient two in the free Picard group, a
contradiction. This entire-conductor impossibility does not assume a
mate.

## 4. Fat triple line: the exact annihilator calculation

Here A=K+N, dim_K N=2, N^2=0. Its canonical module is Hom_K(A,K).
The image N omega_A is one-dimensional: for basis 1,x,y, multiplication
by x sends x* to 1*, and multiplication by y sends y* to 1*.

Put T=NB. It contains N, satisfies T^2=0, and has T intersect A=N:
the ideal is nilpotent and cannot contain a nonzero scalar. Its image
in B/A=omega_A is N omega_A. Consequently

    dim_K B=6,       dim_K T=2+1=3.

Each truncated DVR factor is a Frobenius K-algebra, using the field
trace of the highest coefficient; so is their product B. Therefore
dim Ann_B(T)=dim B-dim T=3. Since T^2=0, T is contained in this
annihilator and equality follows. On a factor L[t]/(t^a), writing
T=(t^k) gives Ann(T)=(t^(a-k)); equality forces a=2k. No factor has
T=0, since its annihilator would be the whole nonzero factor.

All prime multiplicities are even, so D=2E with

    E~C+f on F0,        E~C+2f on F2.

This argument uses the nongorenstein canonical module directly. It
does not assume a rank-two locally free conductor algebra over A.

## 5. Every fat-line divisor pattern is excluded under a mate

A prime mapping to the support line with degree r>=2 is smooth P1.
Every c-intersection must be a totally ramified point, by singleton
fibers. The immersion of c forces it transverse to that prime there,
because the differential kills the prime's tangent. Thus c.E=r
requires r distinct totally ramified points. Riemann--Hurwitz supplies
total ramification 2r-2, while these points require r(r-1). Hence
r<=2. In particular prime E of degree three is excluded.

On F0 the remaining E=C+F has a degree-two horizontal prime and an
isomorphic ruling fiber above the same line. The fiber's restriction
of f has one simple zero. The equality of descended powers forces
the degree-two restriction's entire zero divisor to be the pullback
of that zero: singleton fibers make it one double zero at a ramified
point. This contradicts the transverse intersection required by the
immersion. Equivalently, the degree-two prime needs both simple
branch values, forcing at least two zeros on the degree-one fiber.

On F2 the remaining E=C_min+F1+F2 either has distinct fibers or has
F1=F2=F. For distinct fibers, both isomorphic maps to the same support
line give the same single zero of the descended power at two
disjoint normalization points, contradicting singleton fibers.

The last pattern is D=2C_min+4F. Its generic F-factor is K[t]/(t^4),
and the exact annihilator result gives NB_F=(t^2). The ambient linear
coordinates normal to the supporting line have classes in N. Their
pullbacks therefore vanish to order at least two along F, not just
on its reduced support. Only the coordinate along the line has a
nonzero differential at the generic point; nu|F is an isomorphism.
Thus dnu has generic rank one along F. The independently proved full
power-and-immersion differential lemma excludes this last pattern.

No identification of a plane transverse singularity is needed.

## 6. Direct Artin proof for every double-line-plus-line center

The classifier's added section 7 and the conductor owner's separate
[exact Artin audit](2026-10-08-session-scroll-artin-independent-audit.md)
give a shorter proof, which this auditor independently accepts. It
uses only generic entire schemes and avoids a trace at the vertex.

Over the doubled line L, A=K[epsilon]/(epsilon^2) and B is free rank
two. The rank-two nilpotent multiplication makes the complete factor
list (a,r)=(4,1), (2,2), or (2,1)+(2,1), with epsilon valuation a/2
in each factor. The (4,1) factor gives both ambient normal coordinates
valuation at least two; the differential lemma excludes its prime.
Over the reduced other line M, the factor list is (2,1), (1,2), or
(1,1)+(1,1). In the (2,1) case both ambient normal coordinates belong
to the actual conductor ideal and have valuation at least two, so
the same differential lemma excludes it. Thus primes over M must
have multiplicity one.

On F0 the remaining thick-L factor is a horizontal prime of degree
two and multiplicity two, consuming class 2C. Two degree-one fibers
of multiplicity two would already exceed the 2f coefficient of D.
The residual class 2f over M must consequently be two distinct
multiplicity-one fibers; no degree-two prime has class 2f, and the
single doubled fiber has just been excluded. Their paired zeros
contradict singleton fibers.

On F2 there is no degree-two prime. The remaining thick-L split
case is either 2C_min+2F or two doubled distinct fibers. The latter
has disjoint paired zeros over L. The former leaves class 2f over
M, again forcing two distinct multiplicity-one fibers with disjoint
paired zeros. This covers every pattern. It works for the locally
Gorenstein as well as nongorenstein double-line-plus-line centers.

For clarity, both valuation arguments concern actual functions on
the smooth normalization: membership modulo (t^a) in (t^2), with
a>=2, implies the actual pullback is divisible by t^2. They do not
infer valuations solely from a reduced-support map.

## 6a. Alternative nongorenstein local trace bridge also passes

At its generic double-line point A=K[epsilon]/(epsilon^2), hence B is
free rank two over A. The previously audited even-multiplicity Artin
partitions and F0/F2 divisor analysis apply at these generic points.
The configurations with a unique prime over each support line have
local trace involutions preserving each prime. A mate makes
sigma(f)/f an n-th root of unity in each complete generic Artin
factor. Such a root is exactly one constant root in k: T^n-1 has
distinct constant roots and all the other factors are units in the
local Artin ring. There is no nilpotent correction. A preserved
prime and sigma^2=1 imply that constant has square one. Thus f^2
descends at both actual generic conductor schemes.

The only configuration previously using a global trace involution is

    S=F2,       D=2C_min+2F+2F',       F != F'.

C_min and F map isomorphically to the doubled line L; F' maps
isomorphically to the other line M. Their descended-power zero on L
and singleton fibers force c through P=C_min intersect F. The point
Q=C_min intersect F' maps to L intersect M. These points are distinct,
and C_min is isomorphic to L, so nu(P) is away from L intersect M.
For the classified ideal (y^2,xy,xz), the only nongorenstein point is
that vertex; locally away from it the doubled component is a ribbon
complete intersection. Hence a local rank-two trace involution exists
near P and exchanges its two doubled branches.

In regular parameters u,v at P, the local D equation is u^2 v^2.
The full generic Artin root equalities extend along the respective
doubled branches and have constants zeta,zeta^-1. Subtraction gives

    (zeta-zeta^-1) f in (u^2,v^2).

If zeta^2 !=1, f has no linear term at P, contradicting the smooth
curve c through P. Thus f^2 descends generically over the double
line. The other doubled fiber has identity action on its reduced
field, so its Artin root constant is one and f itself descends there.

Finally the obstruction of the already existing global section f^2
to descent is a section of omega_Gamma(2). This canonical module is
Cohen--Macaulay on the pure curve Gamma and has no finite-support
submodule. Vanishing at all generic points with their entire Artin
structures therefore implies global vanishing. Thus f^2 descends
through the nongorenstein vertex as well.

The descended section of O_X(2) lifts to an ambient quadric, whose
set-theoretic intersection with X is C0: a zero pulls back to f^2=0
and conversely. The unique quadric containing C0 cannot be such a
mate, by the already audited (1,3) divisor-class obstruction. This
excludes the entire double-line-plus-line case.

## 7. Accepted combined theorem and exact boundary

The previous reduced-center and locally Gorenstein proofs, together
with the complete nongorenstein classification and exclusions above,
cover every actual ACM cubic conductor of a smooth rational quartic
scroll normalization. Therefore:

**No integral quartic surface with smooth rational quartic-scroll
normalization can participate in a set-theoretic complete-intersection
pair presenting C0, in any mate degree, over an algebraically closed
field of characteristic zero.**

This strengthens the previous reduced-or-Gorenstein boundary. It
does not cover nonnormal quartics with other normalization types and
does not establish a counterexample to the universal STCI question.
The classification and Artin arguments above are mathematical proofs;
agreement of agents and finite parameter sampling are not being used
as substitutes for them.

## 8. Supporting exact replay

The owner supporting verifier
`research/computations/verify_session_scroll_nongorenstein_cubic_2026_10_08.py`
was inspected and replayed independently with the repository SymPy
runtime. It passed with source SHA256
`a290cf18cef0a5ae53b7a2d1e69d4c0f2aa76039ca7b945f8370b1e019147b9d`.
Its literal minors, Hilbert functions through degree nine, generic
Artin presentations, nil-image rank, finite integer constraints, and
explicit cusp-projection formulas support the proof. The computation
does not itself classify all embedded conductors or replace any of
the geometric arguments above. `git diff --check` passed after this
independent audit was saved.
