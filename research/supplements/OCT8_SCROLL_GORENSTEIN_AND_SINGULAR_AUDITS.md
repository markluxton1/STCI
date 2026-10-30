# October 8 historical mathematical investigations

Full original source text is preserved below, including calculations, qualifications, counterexamples, and unresolved questions. This compilation does not independently audit or promote claims.

---

## Source: 2026-10-08-session-scroll-gorenstein-independent-audit.md

# Independent audit: every locally Gorenstein scroll conductor is excluded

Date: 2026-10-08. Status: **ACCEPTED all-mate exclusion under the
smooth-scroll and locally Gorenstein entire-conductor hypotheses**.
This independently audits sections 11--12 of
`2026-10-08-session-scroll-degenerate-conductor.md`, including their
generic nilpotent length reduction. No canonical files are edited.

## 1. The theorem and the substantive retained hypothesis

Let X be an integral quartic in P3 over an algebraically closed
characteristic-zero field, with smooth rational quartic-scroll
normalization nu:S->X and H=nu*O_X(1). Let Gamma be its actual
entire downstairs conductor, and D the actual upstairs Cartier
conductor. If Gamma is locally Gorenstein, then **X has no STCI
mate for fixed C0 in any degree**.

The theorem does not assert that every ACM cubic conductor is locally
Gorenstein. The prior reduced-center theorem covers every reduced
Gamma, including its non-Gorenstein concurrent-line case. Combined
with that theorem, a hypothetical smooth-scroll mate requires an
actual downstairs conductor that is both **nonreduced and not locally
Gorenstein**. That remaining class is not excluded here.

Inherited whole-scheme inputs are Gamma pure ACM with polynomial
3m+1; D~-K_S; and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

Local Gorensteinness makes omega_Gamma invertible, hence p_*O_D
locally free of rank two. Trace in characteristic zero supplies
the global algebra involution sigma with fixed algebra O_Gamma.
No flatness assertion for the surface normalization itself is used.

## 2. Square compression when every prime is preserved

A mate gives a smooth c isomorphic to C0 as the entire inverse
support, c~H, and a global section f with div(f)=c and descended
power f^n. The restricted f is a unit in every generic local Artin
ring of D. If sigma preserves a reduced prime, the ratio
h=sigma(f)/f in its generic Artin ring satisfies h^n=1.

Since T^n-1 factors into distinct linear factors with constants in
the algebraically closed field, a root in a local Artin ring is
exactly one constant root zeta: the other factors are units. This
kills every nilpotent correction. Applying sigma twice in the same
ring gives zeta^2=1. Thus f^2 is invariant at that associated prime.
When all primes are preserved, Cohen--Macaulayness of the Cartier D
extends this invariance globally, including all intersection jets.
The entire conductor square descends f^2 to O_X(2), and the ambient
hypersurface sequence gives the impossible quadric mate for C0.

When sigma exchanges two primes, their constants may be reciprocal
roots of unity of arbitrary order. That exception must be handled
by the geometric cases below, not by applying sigma twice at a
single prime that it does not preserve.

## 3. A locally Gorenstein triple line is impossible

If a nonreduced pure cubic has one reduced support line L, its
generic multiplicity is three. For an invertible sheaf N on such
a curve, write N|L=O_L(k). Filter O_Gamma by powers of its nilradical.
Each quotient is a coherent sheaf on L; the sum of their generic
ranks is three. Tensoring this filtration by the invertible N
twists every quotient by O_L(k). On P1, that changes Euler
characteristic by rank times k; finite-support torsion contributes
no change. Additivity therefore gives

    chi(N)-chi(O_Gamma)=3k.

For a Gorenstein Gamma, N=omega_Gamma is invertible. Curve Serre
duality gives chi(omega_Gamma)=-chi(O_Gamma)=-1, since its polynomial
3m+1 gives chi(O_Gamma)=1. Thus the difference is -2, not divisible
by three. This contradiction excludes a locally Gorenstein triple
line, without requiring a particular embedded triple-line model.

A nonreduced pure degree-three conductor that is locally Gorenstein
therefore has support two distinct lines L,M with generic
multiplicities two and one. Its connectedness forces them to meet.
Nonreduced structures generically supported on a conic would have
degree at least four; purely finite nilpotent thickenings of a
degree-three reduced support are forbidden by the CM property.

## 4. The exact generic length partitions above the thick line

At the generic point of L, the base is the length-two local algebra
K[epsilon]/(epsilon^2), with K=k(L). The free rank-two upstairs
algebra has K-dimension four, and multiplication by epsilon has
rank two. The factors at the reduced primes of D are quotients of
DVRs by t_i^(a_i), with residue extension degrees r_i over K.

Let k_i be the order of the image of epsilon in such a factor;
take k_i=a_i if its image is zero. The equation epsilon^2=0 implies
k_i>=a_i/2. Multiplication by epsilon has K-rank
r_i*(a_i-k_i) in that factor. Hence

    sum r_i*a_i=4,  sum r_i*(a_i-k_i)=2.

These equalities force k_i=a_i/2 for every factor. In particular
every a_i is even, epsilon is nonzero in every factor, and the
only partitions are

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

This checks the actual nilpotent algebra. Interpreting reduced
support alone as a double cover would miss the first two cases.
For a prime mapping to a line, H-degree equals r. Above the reduced
line M the total generic upstairs length is two.

In the split (2,1)+(2,1) case, quotienting the upstairs algebra by
epsilon gives K times K: epsilon has order one on each length-two
DVR factor. The trace involution swaps these reduced factors, hence
exchanges the two reduced conductor primes globally. In either
single-factor case it preserves the unique prime above L.

## 5. Exhaustive F0 cases

On F0, H=C+2f and D~2C+2f. The only H-degree-one primes are
fibers and the only H-degree-two primes are horizontal C-sections.

The (4,1) case would put multiplicity four on a fiber, impossible
in the divisor class D. The split (2,1)+(2,1) case likewise uses
four fiber multiplicities, impossible. The remaining case (2,2)
is 2E for a horizontal C-prime, leaving a divisor of class 2f
above M.

If that remainder is two distinct fibers, they map isomorphically
to M and the restrictions of f have equal n-th powers there.
They are nonzero sections of O_M(1) with the same zero, giving two
distinct points of c in one normalization fiber. This excludes a
mate. Otherwise D=2E+2F, with each prime the unique one over its
base line. Sigma preserves both, and section 2 gives the impossible
quadric mate. These cases exhaust F0.

## 6. Exhaustive F2 cases

On F2, H=C_min+3f and D~2C_min+4f. The only primes of H-degree
at most two are C_min and ruling fibers, all of degree one. A
degree-two prime is impossible: a distinct nonfiber prime of class
alpha*C_min+beta*f has beta>=2alpha and therefore H-degree
alpha+beta>=3.

The (2,2) case is thus absent. In the (4,1) case the prime must
be a fiber F, since multiplicity four on C_min contradicts D's
class. The remainder is 2C_min above M. Each prime is unique over
its base line, sigma preserves both, and square compression applies.

For the split (2,1)+(2,1) case, the primes are either two distinct
fibers or C_min and a fiber F. Two distinct fibers map
isomorphically to L and their matching section zeros exclude a mate
as in section 5.

If the pair is C_min,F, the remaining class 2f is supported above
M. It is one doubled fiber or two distinct fibers, all different
from F. Sigma exchanges C_min and F and permutes the remaining
fiber primes. But C_min meets each remaining fiber, whereas F
meets none. An automorphism of the entire D cannot send a nonempty
intersection to an empty one. Thus this configuration cannot occur
for the global trace involution, even before the mate hypothesis.

These alternatives exhaust F2.

## 7. Audit decision

The triple-line obstruction uses an explicit Euler-characteristic
filtration, and the doubled-line partitions use free rank-two
nilpotent lengths. All resulting F0/F2 configurations are exhausted
using the actual effective classes. Prime exchange is either
excluded geometrically or handled by full paired-zero support;
prime preservation then permits the exact Artin square-compression
argument. The proof survives this independent adversarial audit.

The explicit principal MF6 p=8,r=1/2 carrier is a concrete
nonreduced locally Gorenstein example, independently checked in
`2026-10-08-session-mf6-rhalf-scroll-independent-audit.md`. This
general theorem extends beyond that example but retains the
locally Gorenstein hypothesis on the **actual entire** conductor.
The remaining smooth-scroll frontier is nonreduced downstairs
ACM cubics with failure of local Gorensteinness. No exclusion of
those schemes or of every nonnormal quartic is claimed.


---

## Source: 2026-10-08-session-scroll-nongorenstein-cubic-classification.md

# Nonreduced nongorenstein scroll conductors: classification and exclusions

Date: 2026-10-08. Status: **PROVED classification and exclusion of all
nonreduced nongorenstein actual cubic conductors under the smooth-scroll
hypotheses.** Sections 1--5 have passed independent audits by the
normal-global-adversarial and scroll-conductor agents. Section 7 gives a
separate double-line-plus-line proof whose independent audit is pending.
This note does not edit the canonical frontier or assert a universal STCI theorem.

Work over an algebraically closed field of characteristic zero. Let an integral
quartic X have finite smooth normalization nu:S->X, where S is F0 with
H=C+2f or F2 with H=C+3f, C^2=-2 in the latter case. Let Gamma be the **actual
entire downstairs conductor**, and D its Cartier inverse conductor divisor.
The [independent ACM audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-acm-independent-auditmd)
supplies D=-K_S, the full conductor Hilbert polynomial 3m+1, and the resolution

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The [scroll conductor note](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-degenerate-conductormd)
supplies the exact sequence retaining every nilpotent:

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

If X has a mate of degree n presenting the fixed smooth rational quartic C0,
the previously proved full-support reduction supplies a smooth c~H on S,
nu|c an isomorphism, every normalization fiber over C0 a singleton, and

    nu*G=lambda f^n, div(f)=c.

Here lambda is nonzero constant, and f is a section of O_S(H). Every proper
prime E<D is a smooth rational curve, even if D is nonreduced: the exact
sequence for O_E and Serre duality give H1(O_E)=H0(O_S(E-D))*=0.

## 1. Entire scheme classification of the nongorenstein ACM cubics

Let M be the 3-by-2 linear Hilbert--Burch matrix. At a point of Gamma where
M has rank one, a unit entry eliminates one ideal generator, leaving a
codimension-two complete intersection. At a rank-zero point the local
Hilbert--Burch resolution is minimal, and its last free rank is two; the
canonical module has two generators. Thus Gamma is nongorenstein exactly
on the common zero locus of the matrix entries.

The span W of these linear entries has dimension at least two (otherwise
the maximal minors cannot have height two). If dim W=4 there is no projective
rank-zero point. If dim W=3, choose W=<x,y,z>; no entry involves w, so Gamma
is the projective cone with vertex [0:0:0:1] over a length-three subscheme
Z of P2_[x:y:z]. Indeed k[x,y,z]/J has Hilbert series (1+2t)/(1-t);
Z has length three. The dimension-one homogeneous quotient is Cohen--Macaulay,
so J is saturated in k[x,y,z]. Since J is generated by quadrics, J_1=0,
which gives H0(I_Z(1))=0. Thus Z is not contained in a line. The equality
h0(O_Z(1))=3 by itself would not prove noncollinearity; it is saturation
and the absence of linear ideal elements that do so.

A noncollinear length-three scheme in P2 has one of four structures. Three
distinct points must be noncollinear. A double point and a distinct point
must have the latter off the tangent line of the double point. A single
curvilinear triple point must have a nonzero second-order departure from
its tangent line. Finally, a single noncurvilinear length-three point has
local ideal the square of its maximal ideal. Linear coordinates and scaling
give the following whole ideals of the corresponding cones:

| Structure | Entire cubic ideal in k[x,y,z,w] | Nongorenstein locus |
| --- | --- | --- |
| Three distinct noncollinear points | (xy,xz,yz) | the vertex |
| Double point plus another point | (y^2,xy,xz) | the vertex |
| Curvilinear triple point | (x^2,xy,y^2-xz) | the vertex |
| Noncurvilinear triple point | (x^2,xy,y^2) | the whole supporting line |

The final ideal has a Hilbert--Burch matrix involving only x,y, so actually
belongs to dim W=2. Conversely if dim W=2, the three independent maximal
minors form all of Sym^2(W), giving precisely (x,y)^2. This proves the
classification without assuming an external classification of quartic surfaces.
The reduced first case is already excluded by the all-reduced-conductor proof.
The nonreduced nongorenstein residual schemes are exactly the last three.

For comparison, [Lehn--Lehn--Sorger--van Straten, section 1, printed page 4]
(https://www.math.sciences.univ-nantes.fr/~sorger/assets/pdf/twistedcubicscubicfourfolds.pdf)
list eight linear-matrix ACM twisted-cubic types. Their matrices A^(6),
A^(7), A^(8) give respectively the three nonreduced nongorenstein ideals
above after renaming variables. This is a primary-source check, not a
substitute for the rank-locus argument over the stated field.

## 2. Generic curvilinear triple line cannot be an actual scroll conductor

For J=(x^2,xy,y^2-xz), the generic conductor algebra is

    A=K[epsilon]/epsilon^3, K=k(Gamma_red).

It is Gorenstein. The exact canonical sequence makes B=(p_*O_D)_eta free
of rank two over A (the local extension of A by its free canonical module
splits). Therefore dim_K B=6 and multiplication by epsilon has rank four.

Each factor of B is a truncated DVR algebra K_i[t]/t^a, for a finite
separable residue extension K_i/K; a is the multiplicity of its conductor
prime on S. If epsilon has valuation k in this factor, epsilon^3=0 gives
a<=3k, and its multiplication rank is (a-k)[K_i:K]. This rank is at most
(2a/3)[K_i:K], with equality precisely when a=3k. A factor on which
epsilon is zero has strictly smaller rank. Since the total rank is exactly
4=(2/3)*6, equality holds separately in every factor. Consequently every
prime multiplicity of D is divisible by three.

Thus D is three times an integral divisor on S. This is impossible in the
free Picard group of either scroll because

    D=-K_S=2C+(e+2)f, e=0 or 2,

and the coefficient of C is two. Hence this curvilinear triple line cannot
be the actual conductor under the smooth-scroll hypotheses, before a mate
is assumed. No reduced-cover approximation is used.

## 3. Generic fat triple line forces an even entire conductor divisor

For J=(x,y)^2 the generic algebra is A=K+N, where dim_K N=2 and N^2=0.
Its canonical module is the K-dual of A. Multiplication by N on that dual
has one-dimensional image: if 1,x,y is a basis, x sends x* to 1* and y
sends y* to 1*. The exact sequence B/A=omega_A therefore gives

    dim_K B=6, dim_K NB=3.

For completeness, NB contains N, its intersection with A is exactly N
(it is nilpotent, so cannot contain a nonzero scalar), and its image in
B/A is N omega_A of dimension one. Thus the dimension claim is exact.
Also (NB)^2=0 because N^2=0.

B is a product of truncated DVR algebras over finite separable extensions
of K. It is a Frobenius K-algebra: on each K_i[t]/t^a use the field trace
of the coefficient of t^(a-1) as its nondegenerate pairing. For every ideal
T, dim Ann_B(T)=dim B-dim T. Applying this to T=NB gives dimension three.
Square-zero gives NB contained in Ann_B(NB), so equality follows.

In a factor K_i[t]/t^a write NB_i=(t^k). Equality with its annihilator
(t^(a-k)) forces a=2k. Every prime multiplicity of the entire D is even.
Therefore

    D=2E,   E~C+f on F0,   E~C+2f on F2.

This argument retains the non-Gorenstein generic canonical module and
does not replace B by a flat double-cover algebra.

## 4. Singleton fibers rule out all but one fat-line divisor pattern

If a proper conductor prime E maps to the supporting line with degree
r>=2, every point of c intersect E must be a totally ramified point:
the fiber over its image is a singleton. Characteristic zero makes the
map separable. Its differential on T_E vanishes there, while nu|c is an
immersion. Consequently c meets E transversely at each such point.
Since c.E=H.E=r, it requires r distinct totally ramified points, contributing
r(r-1) to Riemann--Hurwitz; the total is 2r-2. Thus r>=3 is impossible.

On F0, E~C+f is either a smooth prime of H-degree three or a horizontal
C-prime and one fiber. The prime is excluded by the preceding argument.
In the latter case the horizontal prime covers the line with degree two,
and the fiber covers it with degree one. Restricting f^n to both primes,
using their common descended section on the line, makes the zero divisor
of f on the degree-two prime the pullback of the single zero on the fiber.
The singleton condition makes this a twice-counted totally ramified point,
where smoothness and immersion require intersection multiplicity one.
This is impossible.

On F2, a divisor E~C+2f is either a degree-three prime, C_min+F1+F2 for
distinct fibers, or C_min+2F. The prime is excluded by Riemann--Hurwitz.
Two distinct fibers each map isomorphically to the same supporting line;
the descended-power equality gives their restrictions proportional, so
their zeros lie in one base fiber but at two disjoint normalization points.
This contradicts the singleton condition. The only residual pattern is

    S=F2,   D=2C_min+4F.

Both reduced primes map isomorphically to the same downstairs line.

## 5. A generic differential obstruction excludes the residual pattern

**Lemma (power and immersion).** Suppose a conductor prime T on a smooth
normalization has rank(d nu)<=1 generically. Under the mate hypotheses
above, this is impossible if H.T>0.

All two-by-two differential minors vanish along T, hence rank<=1 at every
point of T. Choose P in c intersect T, which exists because H is ample.
If d nu has rank zero at P, nu|c cannot be an immersion. Otherwise its
restriction along T has rank one near P and its kernel is a regular line
subbundle K of T_S|T there. Trivialize H by a pulled-back ambient coordinate
which is nonzero at nu(P), and let h represent f. The pulled-back mate is
lambda h^n. At generic points of T, h is nonzero because c is not T.
For a local generator v of K, differentiation gives

    0=v(nu*G)=lambda*n*h^(n-1)*v(h).

Characteristic zero gives v(h)=0 generically. The regular kernel section
extends this equality to P. Since h(P)=0 and c is smooth, T_P c=ker(dh_P)
is exactly K_P. Thus d nu annihilates T_P c, again contradicting immersion.
The argument uses the entire power equality on S, rather than a first-normal
approximation of conductor descent.

In the residual fat pattern D=2C_min+4F, the generic factor along F is
K[t]/t^4. Section 3 gives NB_F=(t^2). Ambient normal coordinates defining
the supporting line have images in N, so their pullbacks vanish with
order at least two along F. The coordinate on the line has nonzero
differential along F because nu|F is an isomorphism. Thus d nu has rank
exactly one generically along F, and the lemma applies. This excludes the
last fat-line case in every mate degree.

**Conclusion.** Every actual fat triple-line conductor (x,y)^2 is excluded
as a carrier of a mate presenting C0 on a smooth rational quartic-scroll
normalization. Together with section 2 this excludes both triple-line
nongorenstein cubic schemes. The nongorenstein double-line-plus-line
case is treated in section 7; agreement of agents does not replace the
written arguments.

## 6. Realizable cusp-plus-line projection: a shield against a false shortcut

The residual pattern is not excluded merely because its two reduced
primes map isomorphically to a line. There is a concrete finite birational
projection of F2 with H=C+3f:

    x0=Y a,
    x1=Y b+X(r a^3+s a^2 b),
    x2=X a b^2,
    x3=X b^3,                       r != 0.

Here the six full H-sections are Ya,Yb,Xa^3,Xa^2b,Xab^2,Xb^3.
These four sections have no base point. H is ample, so the morphism has
no contracted curve and is finite onto its image. On the dense open
x2*x3 !=0, b/a=x3/x2 and the remaining fiber coordinate is recovered;
the map is birational. Its integral quartic image has equation

    x1*x2*x3^2-x0*x3^3-r*x2^4-s*x2^3*x3=0.

Its actual conductor has not been asserted here solely from this equation.
The family is recorded to prevent the invalid claim that every such
projection must be immersive along the ruling fiber b=0. In the chart
a=Y=1, put t=b/a, u=Xa^2/Y. Then

    nu(t,u)=[1:t+u(r+s t):u t^2:u t^3].

Along t=0 its Jacobian has rank one at generic u: the u-derivative is
(r,0,0), and the t-derivative is (1+s u,0,0). This is precisely the
cuspidal differential addressed by section 5.

One can verify the power obstruction explicitly. A general H-section in
this chart is h=alpha+beta t+u(P+Qt+Rt^2+St^3). Full singleton zeros on
the two identified reduced primes force alpha=0. At fixed image line
coordinate rho=t+u(r+s t), write u=(rho-t)/(r+s t). The coefficient of t
in h is beta-P/r+rho*(Q/r-Ps/r^2). Every ambient mate has zero coefficient
of t, because x1=rho is held fixed and x2,x3 begin with t^2,t^3.
For h^n, its nonzero generic constant makes this coefficient vanish only
when P=beta*r and Q=beta*s. Then

    h=beta*x1+R*x2+S*x3

is itself a pulled-back ambient hyperplane, incompatible with C0. The
generic differential lemma is the invariant version of this calculation.

## 7. Double-line-plus-line: nilpotent ranks and disjoint fibers

Now let the actual Gamma be the nongorenstein cubic (y^2,xy,xz). Its
underlying support is L union M, and its generic multiplicities are two
on L and one on M. The closed nongorenstein vertex is retained, but no
flatness across that vertex is used below.

At the generic point of L the algebra is A=K[epsilon]/epsilon^2, and the
canonical sequence gives a free rank-two B over A. Thus B has K-length
four and multiplication by epsilon has rank two. The same individual
rank inequality as section 2 forces every upstairs multiplicity a even
and valuation(epsilon)=a/2. The complete residue-degree/multiplicity list is

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

In the first case the ambient normal coordinates to L have nilpotent
classes in (epsilon) and pull back with valuation at least two along the
degree-one conductor prime. Its differential rank is at most one, so
the power-and-immersion lemma excludes this case under a mate.

At the generic point of the reduced line M, B has K-length two. The
complete list is (a,r)=(2,1), (1,2), or (1,1)+(1,1). The first case has
both ambient normal coordinates vanishing in the conductor quotient
and hence order at least two along its doubled conductor prime. It is
likewise excluded by the differential lemma. Thus all primes over M
must occur with multiplicity one.

On F0, a prime of H-degree two is a horizontal C-prime, and a prime of
H-degree one is a fiber. The thick-L case (2,2) therefore consumes 2C,
leaving class 2f over M. The split thick-L case would consume four fiber
multiplicities, exceeding the coefficient two in D=2C+2f. The remaining
conductor over M can only be two distinct fibers of multiplicity one:
a degree-two prime cannot have class 2f, and a doubled single fiber has
already been excluded. The two fibers map isomorphically to M, and the
descended-power relation makes their restrictions proportional. Their
zeros contradict full singleton fibers because the fibers are disjoint.

On F2 there is no prime of H-degree two. The degree-one primes are only
C_min and individual fibers. The thick-L split case is either 2C_min+2F
or 2F1+2F2 with F1,F2 distinct. The latter already has disjoint paired
zeros over L and is impossible under a mate. The former leaves class
2f over M, again forcing two distinct multiplicity-one fibers, which
are excluded by the same argument. The (4,1) case was excluded by the
differential lemma, and (2,2) is absent on F2.

This proves all-mate exclusion for the nongorenstein double-line-plus-line
conductor. In fact this section uses only the generic schemes 2L+M and
the scroll divisor classes; it also applies when that actual conductor
is locally Gorenstein. The nongorenstein vertex never needs a global
trace involution or a rank-two flat-cover description.

## 8. Exact supporting computation and audit boundary

[verify_session_scroll_nongorenstein_cubic_2026_10_08.py]
(../computations/verify_session_scroll_nongorenstein_cubic_2026_10_08.py)
checks the literal three Hilbert--Burch ideals, their degree-zero through
degree-nine Hilbert functions 3m+1, entry-span dimensions, generic Artin
rings, the fat canonical-module nil-image rank, finite integer rank
constraints, and the explicit projection differential/power coefficient.
It passed using the repository's exact SymPy runtime. The output
[JSON](../scratch/session-scroll-nongorenstein-cubic-checks-2026-10-08.json)
records source SHA256 and its deliberately limited scope. These checks
support the proof; they do not computationally classify every conductor
embedding or infer a conductor from a Jacobian scheme.


---

## Source: 2026-10-08-session-scroll-nongorenstein-independent-audit.md

# Independent audit: the remaining nongorenstein scroll conductors

Date: 2026-10-08. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**, subject to the audited smooth
quartic-scroll hypotheses stated below. This completes that class of
carriers. It does not classify all nonnormal quartic surfaces or settle
the unrestricted STCI problem.

Audited owner sources:

- [Nongorenstein classification and triple-line proof](#source-2026-10-08-session-scroll-nongorenstein-cubic-classificationmd), sections 1--5.
- [Degenerate conductor proof](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-degenerate-conductormd), sections 14--16.
- [Independent differential obstruction](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-normalization-differential-independent-auditmd).
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
[exact Artin audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-artin-independent-auditmd)
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


---

## Source: 2026-10-08-session-scroll-three-lines-independent-audit.md

# Independent audit: three-line scroll conductors and the reduced-center corollary

Date: 2026-10-08. Status: **PROVED and independently audited**. The
three-line proof was supplied by `scroll_degenerate_conductor` and
checked here. It includes nonreduced upstairs conductors and does not
apply a rank-two involution at a non-Gorenstein concurrent-line point.

## 1. Exact theorem and inherited inputs

Let X be an integral quartic in P3 over an algebraically closed
characteristic-zero field with smooth rational quartic-scroll
normalization nu:S->X and H=nu*O_X(1). Suppose its actual entire
downstairs conductor Gamma is reduced and has three distinct lines
as its components. Then X has no STCI mate for fixed C0 in any degree.

The inherited structural inputs, proved in the separate audits, are:

    Gamma is pure ACM with Hilbert polynomial 3m+1;
    D~-K_S is the actual upstairs Cartier conductor;
    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0;
    every proper conductor prime E<D is a smooth rational curve.

For the last input, the direct rational-surface cohomology proof is
H1(O_E)=H0(O_S(E-D))^*=0. It remains valid when D is nonreduced.
At each generic point of the reduced Gamma, its canonical module has
dimension one over its function field. Thus the exact sequence gives
the upstairs algebra dimension two there. If a conductor prime E
maps to that line with degree d and has multiplicity a in D, its
contribution is a*d and these contributions sum to two. In particular
H.E=d<=2. This generic statement does not assume local freeness at
a non-Gorenstein point of Gamma.

If a mate exists, the full inverse support is one smooth c isomorphic
to C0 and every normalization fiber over C0 is a singleton. Picard
torsionfreeness gives c~H and a global f with div(f)=c, whose mate
power f^n descends. Every conductor prime is different from c.

## 2. A split pair of ruling fibers is impossible before trace

Two distinct ruling fibers F,F' are disjoint and each has H-degree
one. If both map isomorphically to the same conductor line L,
descent of f^n makes their restrictions have equal n-th powers as
sections of O_L(n). Both restrictions are nonzero sections of O_L(1).
Their ratio is a constant root of unity, so they have the same zero
on L. Upstairs these zeros are two distinct points because F and F'
are disjoint. Both belong to c, contradicting the singleton-fiber
condition. This uses restrictions on L, and is valid even when Gamma
has a concurrent non-Gorenstein point.

## 3. F0 forces a chain and then too many intersections with one fiber

On F0 take H=C+2f and D~2C+2f. The only H-degree-one primes are
ruling fibers f; the only H-degree-two primes are sections in class C.
Indeed a prime class alpha*C+beta*f has alpha,beta nonnegative and
H-degree 2alpha+beta; a multiple of a fiber is not prime.

The coefficient two of C in D requires two distinct horizontal
sections C1,C2 with multiplicity one. A doubled section would have
generic cover contribution 2*2=4 over its image line, impossible.
Each Ci maps with degree two to a different base line Li. They
cannot cover the same line, which would likewise have total degree
four. The remaining divisor of class 2f is supported over the third
line L0. Section 2 rules out two distinct fibers, leaving

    D=C1+C2+2F.

The doubled F maps isomorphically to L0. The points Pi=Ci intersection
F are distinct, so their images pi on L0 are distinct. Thus the
three lines cannot be concurrent under the mate hypothesis. They
also cannot form a planar triangle, whose Hilbert polynomial is
3m rather than 3m+1. Hence L1 and L2 are disjoint, and Gamma is a
nodal chain with distinct junctions p1,p2.

Only now is the whole conductor algebra made locally free of rank
two: the chain is Gorenstein, so the extension by omega_Gamma is an
extension of invertible modules. Trace gives the local algebra
O_Gamma[eta]/(eta^2-Delta). Its discriminant vanishes generically on
L0, since the corresponding conductor component is 2F, hence
vanishes identically on that line and at both junctions. Its fiber
at either junction is k[eta]/(eta^2), supported at one point.

Consequently the degree-two cover Ci->Li is ramified at Pi; an
unramified cover would have a second distinct point in that fiber.
It has exactly two simple ramification points in characteristic
zero. Full inverse support places all c intersection Ci at those
points, and smoothness of C0 forces transverse intersection there:
dnu annihilates the tangent of Ci at a ramification point and cannot
annihilate the tangent of c. Since c.Ci=H.Ci=2, c must pass through
both ramification points, including Pi.

It follows that c intersects F at the two distinct points P1,P2,
giving c.F>=2, contrary to c.F=H.F=1. This excludes the F0 case.

## 4. F2 forces a chain and then a nilpotent descent contradiction

On F2 take H=C_min+3f and D~2C_min+4f. The only primes of
H-degree at most two are C_min and ruling fibers, all of degree
one. For any prime distinct from C_min with class alpha*C_min+beta*f,
nonnegative intersection with C_min gives beta>=2alpha. If alpha
is positive its H-degree alpha+beta is at least three; if alpha is
zero it is a fiber. There is no degree-two prime.

Therefore D contains 2C_min, mapping isomorphically to one base line
L0 with generic conductor multiplicity two. The remaining divisor
of class 4f is divided between the other two lines with generic
contribution two on each. Split fiber pairs are impossible by
section 2, so

    D=2C_min+2F1+2F2,

where F1,F2 are distinct fibers over distinct base lines L1,L2.
Their intersections with C_min are distinct, and C_min->L0 is an
isomorphism. The junctions on L0 are therefore distinct. As in
section 3, Gamma must be a nodal chain rather than concurrent lines
or a planar triangle.

The rank-two algebra is locally free on this Gorenstein chain, and
its trace discriminant vanishes generically on all three lines.
Because Gamma is reduced, Delta=0 globally. Thus its algebra is
O_Gamma plus an invertible tracefree nilpotent module L*eta,
eta^2=0. If f|D=a+b*eta, the section a is generically nonzero on
every component because c is not a conductor prime. It is a
nonzerodivisor on the reduced Cohen--Macaulay Gamma. Descent of f^n
forces n*a^(n-1)*b=0 and therefore b=0 in characteristic zero.

The entire conductor square descends f itself to O_X(1), producing
an ambient hyperplane containing C0. Its nondegeneracy gives the
contradiction. This excludes F2.

## 5. Corollary: all reduced downstairs conductors on smooth scrolls

Together with the separate smooth twisted-cubic and conic-plus-line
theorems, the three-line result yields:

> An integral quartic with smooth rational quartic-scroll normalization
> whose **actual downstairs conductor is reduced** admits no STCI
> mate for fixed C0 in characteristic zero, in any degree.

To see that the cases exhaust this reduced scope, Gamma has degree
three and arithmetic genus zero. If integral, normalization and the
genus formula force it smooth rational; it cannot be a plane cubic,
so it is a smooth twisted cubic. If reducible with two components,
their degrees are two and one, hence a smooth conic and a line. The
genus polynomial forces their intersection scheme length to be one.
If it has three components they are distinct lines, treated above.
There are no remaining positive degree partitions of three.

The corollary's reducedness assumption is **downstairs only**.
Upstairs multiplicities were retained in both scroll cases and in
the conic-plus-line proof. Nonreduced downstairs cubic schemes,
such as multiple-line conductor structures, remain outside it.
At their non-Gorenstein points the normalization algebra may not
be locally free of rank two. No involution or nilpotent-power
argument is transferred there without a separate proof.


---

## Source: 2026-10-08-session-singular-degree-and-singleton-hessian-audit.md

# Reduced singular support and singleton normalization fibers

Date: 2026-10-08. Status: **PROVED HERE**, with an independent audit of
the planar-cubic argument. These are structural necessary conditions;
they do not resolve the unrestricted quartic-carrier or STCI problem.
No canonical frontier file is edited here.

Throughout, k is algebraically closed of characteristic zero. A
quartic means a geometrically integral hypersurface X in P3 unless
another hypothesis is expressly stated. The reduced curve support of
Sing(X) is denoted Sigma. Its degree is distinguished from the degree
of the Jacobian scheme and from the actual conductor scheme.

## 1. The reduced curve support has degree at most three

**Proposition.** For an integral quartic X, deg(Sigma) <= 3. If X is
nonnormal, Sigma is nonempty, so 1 <= deg(Sigma) <= 3.

Choose a general plane H. Bertini irreducibility makes Y=X intersect H
geometrically irreducible; Bertini smoothness on X_reg makes Y smooth
at its generic point. The plane hypersurface Y is Cohen--Macaulay, so
irreducibility plus generic reducedness makes it integral. The plane
can simultaneously avoid the isolated singular points of X, the
finitely many singular points and component intersections of Sigma,
and be transverse to every component at each point of H intersect
Sigma. Consequently H intersect Sigma consists of exactly deg(Sigma)
distinct geometric points. For the Bertini inputs, see the primary
[Stacks irreducibility theorem](https://stacks.math.columbia.edu/tag/0G4C)
and [smoothness theorem](https://stacks.math.columbia.edu/tag/0FD4).

Every one of those points is singular on Y: all ambient first
derivatives of its quartic equation vanish there, hence the two plane
derivatives vanish. Let nu_Y:Y_tilde -> Y be the finite normalization.
The exact sequence

    0 -> O_Y -> (nu_Y)_* O_Y_tilde -> T -> 0

has T of finite length, with length at each singular point at least
one. (An integral curve over this perfect field is regular exactly
where it is normal.) Both proper integral curves have H0=k. Taking
Euler characteristics gives

    p_a(Y) = g(Y_tilde) + length(T).

The arithmetic genus of a plane quartic is three, directly from
0 -> O_P2(-4) -> O_P2 -> O_Y -> 0. Hence

    deg(Sigma) <= length(T) <= 3.

An integral hypersurface is S2. If it were regular in codimension one,
Serre's criterion would make it normal. Thus a nonnormal quartic has a
singular curve component. This proves the lower bound.

If deg(Sigma)=3, the same proof gives g(Y_tilde)=0 and exactly delta=1
at each of the three general singular section points. It does not
identify the global normalization, classify special fibers, or bound
the degree of the Jacobian scheme.

**Irreducible-support corollary.** If Sigma is irreducible of degree
three, it is a smooth twisted cubic. Section 2 excludes the planar
case. For a nonplanar integral degree-three curve, pull O(1) to the
smooth normalization Z. The resulting line bundle L has degree three
and at least four independent sections, since the four ambient
coordinates are linearly independent on a nondegenerate curve. If Z
had positive genus, every effective divisor of degree d>0 would have
h0 at most d: h0(O_Z(p))=1 for any point p (a second section would give
a degree-one map to P1), and adding the other d-1 points increases h0
by at most one each. A nonzero section of L supplies such a divisor,
contradicting h0(L)>=4. Hence Z=P1, L=O(3), and the four coordinates
give the complete degree-three embedding. The image is consequently
a smooth twisted cubic. Reducible degree-three support is not covered
by this irreducible corollary.

## 2. Every reduced planar cubic singular support is impossible

**Proposition.** If a quartic form F has all its first derivatives
vanishing on a reduced planar cubic C, then its plane equation divides
F. More precisely, after writing the plane as z=0 and its squarefree
cubic equation as g(x0,x1,x2)=0, one has

    F = z (lambda*g + z*Q2).

In particular an integral quartic cannot have such a cubic in its
singular support.

Write

    F = A4(x0,x1,x2) + z*B3(x0,x1,x2) + z^2*Q2(x0,x1,x2,z).

Support containment gives g|A4, g|partial_i(A4) for i=0,1,2,
and g|B3 from the normal derivative partial_z F. If an irreducible
factor q of g occurs only once in a nonzero A4=q*a, choose a nonzero
partial_i q. Its degree is smaller than deg(q), so q does not divide
partial_i q. Reducing partial_i A4 modulo q gives

    partial_i A4 = (partial_i q)*a mod q,

which is nonzero in the domain k[x0,x1,x2]/(q), a contradiction. Each
factor of the squarefree g therefore occurs at least twice in A4.
Thus g^2|A4; degree six exceeds degree four, so A4=0. Since g and B3
have the same degree, B3=lambda*g, giving the displayed formula.

This treats irreducible cubics (including singular cubics), a conic
and line, and three distinct lines with any planar arrangement. It
also gives the ordinary-ideal certificate

    F in (z^2,z*g)_4 = (I_C^2)_4.

No symbolic-power equality or unproved absence of embedded primes is
needed. A repeated or embedded thickening of the Jacobian scheme does
not affect the support-based proof. A **nonreduced degree-three plane
scheme whose reduced support has degree one or two** is outside this
cubic assertion. In particular, a Jacobian scheme of degree three is
not itself evidence of a reduced planar cubic.

The subagent planar_cubic_audit supplied a separate complete factor
argument and reached the same exact formula. Agreement supplements
the written proof; it is not substituted for it.

### Complete reduced degree-three support list

**Corollary.** If the reduced singular curve support Sigma has degree
three, it is connected and nonplanar. Its underlying reduced curve
has one of exactly four forms:

1. A smooth twisted cubic.
2. A smooth plane conic together with a line outside its plane,
   meeting the conic.
3. A chain of three lines, with the two endpoint lines skew.
4. Three concurrent lines spanning P3.

This is a list of possible reduced supports, not an existence claim
for quartics realizing every entry, and not a conductor-scheme
classification.

Nonplanarity follows from the proposition above. The irreducible case
is the corollary in section 1. An irreducible degree-two component is
a smooth plane conic: normalization and the degree-two line-bundle
section bound exclude a nondegenerate embedding in P3, and a reduced
integral plane conic is smooth over this field. Thus the only other
degree partitions are a conic plus a line, or three distinct lines.

Suppose a line L is disjoint from a conic K in its plane P. Double
vanishing of F on the reduced conic gives

    F|P = lambda*q2^2,

by the same irreducible-factor derivative proof used above. The line
cannot lie in P, and its intersection p with P is off K. Since
F(p)=0, lambda=0 and P divides F, contradicting integrality. Therefore
the conic-plus-line case is connected. If the line also lay in the
conic's plane, their union would be the forbidden planar cubic.

For three lines, if one pair intersects and the third is disjoint
from that pair, let P be the plane of the intersecting pair and let
q2 be their squarefree degree-two product. Again F|P=lambda*q2^2.
The third line meets P at a point off the pair, forcing lambda=0 and
a plane factor. Thus this disconnected case is impossible.

If the three lines are pairwise skew, put them by a projective change
of coordinates into

    L1: x2=x3=0,
    L2: x0=x1=0,
    L3: x2=x0, x3=x1.

They lie on the smooth quadric Q: x0*x3-x1*x2=0, and they are in the
same ruling. The restriction of the quartic to Q has class (4,4).
Because F and all its first derivatives vanish on each line, its
restriction vanishes to order at least two along each line. If this
restriction were nonzero, subtracting those three doubled ruling
lines would give a section of O_Q(-2,4), which has no sections.
Therefore Q divides F, another contradiction. This removes the last
disconnected three-line case.

Connected nonplanar three-line arrangements are precisely a chain
with skew endpoints or three concurrent lines spanning P3. Three
pairwise intersecting lines with three distinct intersection points
are a planar triangle and were already excluded. This exhausts the
list. The independent planar_cubic_audit subagent checked the
disconnected cases, the smooth-quadric restriction, and the line
incidence exhaustion without finding a gap.

## 3. The Jacobian scheme can have larger degree

For a concrete distinction, take

    F = x^2*z^2 + y^3*w.

This quartic is integral: viewed as a polynomial in w it is primitive
and linear over k[x,y,z], with coprime coefficients y^3 and x^2*z^2;
Gauss's lemma gives irreducibility. Its derivatives give the Jacobian
ideal, up to nonzero constants,

    (x*z^2, y^2*w, x^2*z, y^3).

The reduced singular support is the union of the two lines
(x,y)=0 and (y,z)=0, of degree two. At the first line's generic point,
z and w are units and the Jacobian ideal is (x,y^2), of length two.
At the second, x and w are units and it is (z,y^2), also of length two.
Thus the one-dimensional Jacobian scheme has degree four. Embedded
points, if present, do not change this leading degree computation.
The degree-at-most-three theorem must not be applied to that scheme.

## 4. A nonnormal singleton-fiber surface point has Hessian rank at most one

**Local proposition.** Let x be a closed point of an integral
hypersurface surface X over k, and let nu:S -> X be its finite
normalization. If X is nonnormal at x and nu^{-1}(x) has exactly one
point, the rank of the local hypersurface Hessian at x is at most one.

Suppose instead that the rank is at least two. Formal splitting in
characteristic zero puts the completed local equation into the form

    u*v + g(w),  g in k[[w]].

One can obtain this with the formal implicit function theorem for two
variables with invertible quadratic Hessian block, followed by the
formal Morse lemma with parameter w. This uses a formal coordinate
change and multiplication by a unit; it does not require convergent
or analytic coordinates. A primary precise statement allowing
non-isolated singularities is [Greuel--Pfister, The Splitting Lemma in
any Characteristic, Theorem 2.1(2)](https://arxiv.org/html/2507.17078v2).
If g is nonzero, its derivative is also
nonzero. The hypersurface is Cohen--Macaulay and its singular support
is isolated (the derivatives are v,u,g'(w)). It is therefore normal
by S2+R1. Normality of the completion descends along the faithfully
flat map to the completion, so X is normal at x, a contradiction.

If g=0, the completed ring is

    A_hat = k[[u,v,w]]/(u*v),

with two nonzero zero divisors u and v. Set A=O_X,x and let B be its
finite normalization algebra. The singleton fiber means B has just
one maximal ideal, so it is a local normal ring. Rings essentially
of finite type over a field, their localizations, and finite algebras
over them are excellent. Exact completion of the finite injection
A -> B gives an injection

    A_hat -> B tensor_A A_hat = B_hat.

Here completion at the maximal ideal of B agrees with completion at
m_A*B because the two adic topologies are equivalent for a finite
local algebra. The completed local ring B_hat is normal, hence a
domain. A ring with the displayed nonzero zero divisors cannot inject
into a domain. This is the required contradiction. The exact
excellence inputs are [Stacks Proposition 15.53.3 and Lemmas
15.53.2](https://stacks.math.columbia.edu/tag/07QS) and the precise
[normal-completion Lemma 15.53.6](https://stacks.math.columbia.edu/tag/0C23).

This argument avoids treating formal branch counting as automatically
equal to normalization fiber counting, and avoids any unqualified
claim that normalization commutes with arbitrary completion.

At a singular point, Hessian rank is invariant under regular or
formal coordinate changes and multiplication of the equation by a
unit. For a homogeneous equation, Euler's identity places the radial
vector in the Hessian kernel once all first derivatives vanish.
Thus the rank of the homogeneous four-variable Hessian at a
projective representative equals the rank of the three-variable
Hessian in any affine chart.

## 5. A mate forces a conductor intersection with Hessian rank at most one

**Global proposition.** Let X be an integral nonnormal hypersurface
surface in P3 and C a smooth integral projective curve in X, with X
regular at the generic point of C. If a hypersurface mate cuts out C
set-theoretically on X, then some point x in C where X is nonnormal
has Hessian rank at most one.

Let G be a mate and b its degree, with nu:S -> X the finite
normalization and H=nu^*O_X(1), an ample Cartier divisor. The full
inverse support of C is the support of the nonzero effective Cartier
divisor defined by nu^*G. Because nu is an isomorphism at the generic
point of C, there is just one curve c above C. Its finite birational
map to the smooth curve C is an isomorphism. The zero support of a
nonzero section of a line bundle on a normal surface is pure of
codimension one, so no isolated inverse-image point can remain.
Hence

    (nu^{-1}(C))_red = c,  nu|c:c -> C is an isomorphism,
    div(nu^*G) = m*c linearly equivalent to b*H

for a positive integer m. In particular every fiber over C is a
singleton. When deg(X)=deg(C)=4, intersecting with H gives m=b.

Since X is an S2 nonnormal hypersurface, its nonnormal locus contains
a curve. Choose a prime curve D on S in the inverse image of that
locus. It is distinct from c, since X is regular at the generic point
of C. Restrict the section defining m*c to D. It is a nonzero section
of O_D(b*H), which has positive degree by ampleness. It must have a
zero: pull the restricted section to the smooth normalization of
the integral curve D, where this is the ordinary positive divisor
degree statement. Therefore c intersects D, even if S is singular at that
intersection and even if c is only a Weil divisor: m*c is Cartier,
which is all the restriction argument uses.

The image x of such an intersection is nonnormal on X and has a
singleton normalization fiber. Section 4 now gives Hessian rank at
most one. No smoothness hypothesis on the normalization, no ADE
assumption, and no reducedness hypothesis on the conductor is used.
Here singleton means a singleton underlying set; no assertion that
the finite scheme fiber is reduced is needed. The independent
planar_cubic_audit subagent also audited sections 4--6, including the
finite-algebra completion topologies and the Cartier restriction,
and found no substantive gap.

Consequently, an exact computation showing that C has **no** singular
point of X at which all two-by-two Hessian minors vanish excludes a
mate in every degree. The condition is necessary; the existence of
a rank-at-most-one point does not establish a mate.

## 6. First-normal consequences and the defect-chart boundary

Suppose along C the first-normal equation factors as h times a
nowhere-zero local normal direction. At a point x choose formal
coordinates (z,y,m) with C=(y,m), z a local parameter on C, and that
normal direction represented by m. Then

    F = h(z)*m + a(z)*y^2 + b(z)*y*m + c(z)*m^2
        + terms of (y,m)-order at least three.

The point is singular precisely when h(x)=0. At such a point the
Hessian is

    [ 0      0       h'(x) ]
    [ 0    2a(x)      b(x) ]
    [ h'(x) b(x)     2c(x) ].

If h has a simple zero, the z,m minor has determinant -h'(x)^2,
so the rank is at least two. By section 5, a nonnormal carrier with
a mate must therefore have a **repeated zero of h**. This applies
in both charts of C; multiplicity is unchanged by a nonvanishing
change of frame. In the MF6 e=1 quartic lane h is a section of O_C(8),
but its degree is not needed for the local argument.

At a repeated zero, the remaining rank-at-most-one condition is

    4*a(x)*c(x) - b(x)^2 = 0.

If a contact identity separately gives a(x)=0, this reduces to
b(x)=0. For example this holds on an ordinary triple chart where
a is a multiple of h by a regular scalar. A contact expression
a=Gamma*h/delta does **not** justify that simplification at a zero
of delta unless the completed two-chart contact identity is also
checked. Thus a proposed gcd(h,h',b) filter must retain its defect
points or prove a(x)=0 there. The general homogeneous Hessian-minor
filter in section 5 has no such frame or denominator boundary.

These lemmas reduce possible mates to a precisely specified
singularity/contact locus. They do not yet show that the corresponding
parameter locus is finite, determine it for the unique principal
quartic family, or exclude its surviving fibers.


---

## Source: 2026-10-08-session-veronese-allmate-independent-audit.md

# Independent audit: all P2,O(2)-normalized quartic carriers

Date: 2026-10-08. Status: **PROVED by independent structural audit of
the supplied argument**. The audit includes non-slc Jordan projections;
no semi-log-canonical assumption is required. It does not exclude all
nonnormal quartic carriers: normalizations other than P2 with H=O(2)
remain outside its scope. No novelty claim is made.

**Theorem.** Over an algebraically closed characteristic-zero field,
let X be an integral quartic in P3 with finite normalization
nu:P2->X and nu*O_X(1)=O_P2(2). Then X cannot be a carrier in a
set-theoretic complete-intersection presentation of any smooth rational
quartic C in P3, regardless of mate degree or common singular points.

This note independently audits the strengthened argument developed in
[the pencil classification note](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-veronese-pencil-classificationmd).
That note is being upgraded from its earlier slc-only form; this audit
states the complete hypotheses and proof independently of edit timing.

## 1. Classification and its omitted-stratum checks

The normalization is defined by four independent sections of O_P2(2).
Its center line is a two-dimensional pencil of symmetric quadratic
tensors, using the pairing trace(P Q) against symmetric coefficient
matrices of the four quadrics. The off-diagonal coefficient convention
is essential: a cross-term coefficient is twice that matrix entry.
Basepoint freeness is equivalent to the center containing no rank-one
matrix. The center basis is independent, so no nonzero pencil parameter
gives the zero matrix.

I independently checked all cases of the direct three-dimensional
linear-algebra argument. If a center member A is invertible, the
operator A^(-1)B is self-adjoint for the nondegenerate symmetric form A.
Distinct generalized eigenspaces are orthogonal and nondegenerate.
The possible Jordan partitions are:

- Three distinct simple eigenvalues: after an orthogonal basis change,
  the annihilator contains xy,xz,yz and a diagonal quadric with all
  coefficients nonzero. Rescaling source coordinates gives the Roman
  map [yz:zx:xy:x^2+y^2+z^2].
- A repeated diagonalizable eigenvalue, or a size-two Jordan block with
  its size-one block sharing the same eigenvalue: subtracting that
  eigenvalue times A produces a rank-one center member, forbidden.
- A size-two Jordan block plus a distinct eigenvalue: chain rescaling
  and a pencil basis change give the map
  [y^2:xz:yz:z^2-xy-x^2].
- A single size-three Jordan block: its antidiagonal chain Gram matrix
  gives [x^2:xy:z^2:y^2-xz].

The chain Gram transformations in the classification note are exact:
for size three, replacing the cyclic vector v by v+a Nv+b N^2v changes
the two unwanted Gram entries by delta->delta+2a gamma and
epsilon->epsilon+2a delta+(a^2+2b)gamma, where gamma!=0. These operations
remove them without losing the Jordan chain. For size two the
corresponding isotropic chain has nonzero cross pairing, and its single
diagonal entry is removable. No diagonalizability assumption is made
for a symmetric matrix over an algebraically closed field.

For an identically singular center pencil, every member has rank two.
The primitive adjugate argument gives adj M=h vv^T, with deg h=2-2deg v.
No projective zero of adj M is possible, so h is constant and v is
linear with independent coefficient vectors. Putting v=(s,t,0) directly
forces the Kronecker pencil, up to removable diagonal terms. Its
projection has quadric image and generic degree two, contradicting the
finite birational quartic hypothesis. I checked this against the
[separate singular-pencil proof](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-veronese-singular-pencilmd).

Thus Roman, Jordan2 and Jordan3 exhaust the hypotheses. The two Jordan
cases were previously discarded using slc; the arguments below exclude
their mates without that assumption.

## 2. A mate requires a smooth lifted conic, with full inverse support

Each of the three normal forms has singular support consisting of
lines. For Jordan2 the image equation is

    c^4-a d c^2-a^2bc-a^2b^2=0.

Its derivative with respect to d is -a c^2. If a=0, the equation forces
c=0; if c=0, it forces a=0 or b=0. Its singular support is the union
of the two lines a=c=0 and b=c=0. For Jordan3 the equation is

    (b^2-a d)^2-a^3c=0;

its derivative with respect to c forces a=0 at a singular point, then
the equation forces b=0. The Roman equation has three coordinate
double lines, as the derivative in the fourth coordinate forces the
product of its first three coordinates to vanish.

An integral degree-four C cannot be one of these lines. Hence the
normalization is an isomorphism at its generic point. Its dominant
curve preimage c is finite birational over the smooth C and therefore
isomorphic to C. A mate's nonzero pullback has full zero support equal
to the entire reduced inverse image. Its plane divisor cannot have an
isolated component. Thus the entire reduced inverse image is c, each
fiber over C has just one point, and the map c->C is injective and an
isomorphism.

The hyperplane pullback has degree 2 on a plane curve, whereas its
restriction to c has degree 4. Therefore c has plane degree 2. It is
a smooth integral conic, defined by an irreducible homogeneous form f.
If a mate G has degree n>0, the polynomial G(q0,q1,q2,q3) is homogeneous
of degree 2n, nonzero, and has support exactly V(f). Unique
factorization gives

    G(q0,q1,q2,q3)=c0 f^n, c0 in k*.

This scalar is a genuine global constant. Arbitrary units from an
affine localization must not be inserted into this equality. These
facts are what permit the descent tests below.

## 3. Roman case

For [yz:zx:xy:x^2+y^2+z^2], the coordinate vertices have one common
image, so c avoids them. On each coordinate line the double-cover
involution interchanges the other two coordinates. Its only singleton
fibers are the two points with those coordinates equal or opposite.
At each such ordinary pinch a smooth embedded image requires transverse
passage through that coordinate line.

The conic must consequently contain all six points

    (0,1,+/-1), (1,0,+/-1), (1,+/-1,0).

Evaluating a general conic shows all three cross coefficients vanish
and its diagonal coefficients satisfy A+B=A+C=B+C=0. In characteristic
zero it is the zero form. This excludes Roman in every mate degree.
The direct no-conic certificate is retained in the
[structural verifier](../computations/verify_session_nonnormal_structural.py).

## 4. Jordan2: one available transverse point cannot supply degree two

Use q=[y^2:xz:yz:z^2-xy-x^2]; this is the source-coordinate swap of the
equivalent [x^2:xz:yz:z^2-xy-y^2] used in the other audit. Let L:z=0.
On its chart y=1, put r=x/y. Its image is

    [1:0:0:-r-r^2].

The two parameters r and -1-r have the same image. The only finite
singleton is r=-1/2. The point at infinity [1:0:0] has the same image
as [0:0:1], so it is not a singleton of the **full** normalization
fiber. Full support and injectivity of c->C therefore allow c to meet
L only at p=[-1/2:1:0].

Near p, with source coordinates (r,z), use the target chart q0=1. Its
three coordinates are

    (r z,z,z^2-r-r^2).

At p its differential annihilates the r direction and sends the z
direction to (-1/2,1,0), a nonzero vector. Since c->C is an isomorphism
and C is a smooth embedded curve, its differential must be nonzero.
Thus c is transverse to L at p, with intersection multiplicity one.
An integral conic not containing L has total intersection two with L.
Only one point of multiplicity one is available, a contradiction.

No ordinary-pinch or reduced-conductor assumption was used here. The
explicit normalization differential and the entire fiber count suffice.

## 5. Jordan3: first-order conductor descent excludes every power

Use q=[x^2:xy:z^2:y^2-xz] and L:x=0. The entire preimage of its
singular line is L, whose map is [y:z]->[z^2:y^2]. Its only singleton
fibers are p=[0:0:1] and p'=[0:1:0]. At p, on z=1, the differential
of (x^2,xy,y^2-x) is nonzero only in the x direction. At p', on y=1,
the analogous target chart has differential nonzero only in the x
direction. Therefore a smooth image curve passes transversely through
L at either singleton.

The conic has to meet both points once, so its equation has the form

    f=alpha x^2+beta xy+gamma xz+delta yz, delta!=0.

The absence of y^2,z^2 terms is exactly passage through p,p'; if
delta=0 the conic would contain L and be reducible.

On z=1, the image coordinate ring is

    A=k[x^2,xy,y^2-x] subset k[x,y].

Work in T=k[y,y^(-1),x]/(x^2). Define

    iota(x)=-x, iota(y)=-y+x/y.

The image of y is a unit, and direct substitution proves iota^2=id.
It fixes x^2, xy and y^2-x modulo x^2. Thus every original coordinate
function, including the restriction of G, is fixed by iota in T.
The global equality from section 2 requires f^n to be fixed as well.

Modulo x^2 one has

    f=delta y+x(beta y+gamma),
    iota(f)=-delta y+x(delta/y+beta y-gamma).

The constant term of f^n first forces (-1)^n=1, so n is even. Its
coefficient of x is then, after division by the nonzero scalar
n delta^(n-1)y^(n-1), incompatible with invariance unless

    2 beta y+delta/y=0,
    equivalently 2 beta y^2+delta=0 in k[y,y^(-1)].

This identity forces delta=0, a contradiction. The use of n!=0 is
precisely where characteristic zero matters. This is an argument for
all positive mate degrees, not a finite collection of power tests.

The involution is a first-order conductor descent test. It does not
assert scheme containment of nonreduced ramification in c, the general
claim refuted by the
[local counterexample](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-ramification-scheme-counterexamplemd).

## 6. Audit outcome and reproducibility

The strengthened theorem passes the full independent audit: center
classification, rank-one exclusion, singular-pencil boundary,
normalization maps, regularity at the generic point of C, full inverse
purity, smooth lifted conic, actual global units, all exceptional fibers,
endpoint differentials, and arbitrary-degree first-order descent have
all been checked. No slc assumption remains in the result.

The [independent exact verifier](../computations/verify_session_veronese_allmate_independent.py)
checks the Jordan2 fiber identity and differential, both Jordan3 endpoint
differentials, the actual order-two involution and its fixed generators,
and the normalized symbolic coefficient contradiction for all even n.
It also checks the gradient identities identifying the Jordan singular
supports. The source normal-form and singular-pencil verifiers cover
the classification identities; their PASS results do not replace the
proof of exhaustiveness given in section 1.
