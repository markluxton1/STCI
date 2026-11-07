# Smooth quartic scrolls: nilpotent conductors and all mate degrees

Use the [whole actual conductor](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md) on
the smooth F0/F2 normalization. The reduced-conductor cases have their
[separate complete proof](QUARTIC_SCROLL_REDUCED_CONDUCTORS.md). Here the
locally Gorenstein and nongorenstein nonreduced schemes exhaust the rest.
The key measurements are generic Artin lengths, canonical-module
multiplication ranks, a Frobenius pairing on products of truncated DVR
algebras, actual effective divisor classes, and differential rank. The direct Artin/differential argument and a separate local-trace ending are both retained; neither silently extends a global involution through a nongorenstein point.

## 1. Locally Gorenstein entire conductors

### 1.1. The theorem and the substantive retained hypothesis

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
Gorenstein**. That class is outside Section1; Sections2--3 below exclude it.

Inherited whole-scheme inputs are Gamma pure ACM with polynomial
3m+1; D~-K_S; and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

Local Gorensteinness makes omega_Gamma invertible, hence p_*O_D
locally free of rank two. Trace in characteristic zero supplies
the global algebra involution sigma with fixed algebra O_Gamma.
No flatness assertion for the surface normalization itself is used.

### 1.2. Square compression when every prime is preserved

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

### 1.3. A locally Gorenstein triple line is impossible

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

### 1.4. The exact generic length partitions above the thick line

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

### 1.5. Exhaustive F0 cases

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

### 1.6. Exhaustive F2 cases

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

## 2. The remaining nongorenstein schemes

The complete classification of the whole nongorenstein cubic schemes is proved in [the structure theorem](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md#4-the-whole-nongorenstein-cubic-schemes). Its three nonreduced types are treated here.

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

Coefficient fields compatible with K can be chosen in these finite Artin algebras because the residue extensions are separable. Thus the field-trace pairing below is a pairing over the actual generic base field.

### 2.2. Curvilinear triple line: divisible-by-three obstruction

At its generic point, A=K[epsilon]/epsilon^3 and omega_A is free of rank one. The canonical exact sequence therefore makes B free of rank two over A. B has K-length six and multiplication by epsilon has rank four.

Write a generic conductor factor as K_i[t]/t^a, r=[K_i:K], and k=ord_t(epsilon), allowing k=a if the image is zero. Its K-length is ar and its multiplication rank is r(a-k). Since epsilon^3=0, a<=3k. The sum of the ranks reaches the upper bound (2/3)*6=4, so equality holds in every factor: a=3k. Every actual prime multiplicity of D is divisible by three. Then the divisor class of D is divisible by three in the torsion-free Picard group, contrary to its C-coefficient two. This excludes the actual curvilinear triple-line conductor before imposing a mate.

No reduced-cover interpretation or global flatness at its nongorenstein vertex is used.

### 2.3. Fat triple line: the canonical-module and annihilator steps

For the fat triple line, A=K+N with dim_K N=2 and N^2=0. In omega_A=Hom_K(A,K), multiplication by N has image the one-dimensional span of 1*. Let T=NB. The canonical exact sequence gives dim_K B=6, and the image of T in B/A is N omega_A, of dimension one.

The ideal T contains N. Since T^2=0, T intersect A contains no element with nonzero scalar part: such an element is a unit in A, hence a unit in B, contradicting square-zero. Thus T intersect A=N, and dim_K T=2+1=3.

B is a product of truncated DVR algebras over finite separable residue extensions of K. It is Frobenius over K: on K_i[t]/t^a the pairing takes the field trace of the coefficient of t^(a-1) in a product. It is nondegenerate, so every ideal T satisfies dim Ann_B(T)=dim B-dim T. Our T is square-zero and three-dimensional, hence

    T subset Ann_B(T), dim T=dim Ann_B(T)=3,
    T=Ann_B(T).

An ideal in a truncated DVR factor is (t^k), with annihilator (t^(a-k)). Equality forces a=2k separately in every factor. In particular no odd prime multiplicity or zero ideal factor is omitted. Every coefficient of the actual D is even, so

    D=2E, E~C+f on F0, E~C_min+2f on F2.

This Frobenius argument is applicable to B, which is a product of DVR quotients; it does not assert that the nongorenstein algebra A is Frobenius or that B is free of rank two over A.

### 2.4. Effective divisor and full-fiber exclusions for the fat line

A prime mapping to the support line with degree r has H-degree r. For r>=2 every point of c intersect that prime must be a totally ramified point, since the entire normalization fiber is a singleton. The ramification derivative annihilates its tangent, whereas nu|c is immersive, so c meets the prime transversely at each such point. There are consequently r distinct totally ramified points. Their contribution r(r-1) cannot exceed the Riemann--Hurwitz total 2r-2; r>=3 is impossible.

On F0 the effective class C+f is a prime of degree three or a horizontal C-prime plus one fiber. The prime is excluded above. In the split case, the degree-one fiber restriction of f has one zero on the common base line. Equality of the full descended n-th powers forces the zero divisor on the degree-two horizontal prime to be the pullback of that one zero. Singleton fibers make it one totally ramified point of multiplicity two, while immersion of c requires transverse intersection one. This is a contradiction.

On F2, any prime other than C_min has class a C_min+b f with b>=2a; fibers are individually prime only with class f. Thus C_min+2f is either a degree-three prime, C_min+F1+F2 for distinct fibers, or C_min+2F. The prime case is excluded by the ramification argument. The distinct fibers have proportional nonzero restrictions of f, because their n-th powers descend to the same line. Their equal zero on the base gives distinct points of c in one normalization fiber, impossible.

The remaining actual divisor is D=2C_min+4F. In its generic F-factor B_F=K[t]/t^4 the preceding self-annihilator computation gives NB_F=(t^2). Ambient coordinates normal to the support line have classes in N, so their actual pullbacks vanish to order at least two along F: the equality modulo the conductor (t^4) implies actual membership in (t^2). The longitudinal coordinate has nonzero derivative because F maps isomorphically to the line. Hence dnu has generic rank one on F. The [independent nonimmersion-prime lemma](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-nonimmersion-prime-independent-auditmd) excludes the mate. This step verifies derivative rank from the actual generic algebra; multiplicity four alone would not do so.

### 2.5. Doubled line plus reduced line, including the nongorenstein vertex

At the thick line L, A=K[epsilon]/epsilon^2 is generically Gorenstein, so B is free of rank two there. Its length four and epsilon-rank two give the complete partitions

    (a,r)=(4,1), (2,2), or (2,1)+(2,1),

with epsilon order a/2 in every factor. In the (4,1) factor, normal coordinates to L belong to the nilradical (epsilon) and therefore have actual valuation at least two on its prime. The nonimmersion lemma excludes this case under a mate.

At the reduced line M, total generic length two gives

    (a,r)=(2,1), (1,2), or (1,1)+(1,1).

In the doubled-prime case (2,1), normal coordinates to M vanish in A=K and thus belong to the actual conductor (t^2). This also gives generic rank at most one and is excluded. Hence all prime multiplicities over M are one under a mate.

On F0 the only H-degree-two prime is a horizontal C-prime and the only degree-one primes are fibers. The split thick-line partition consumes four fiber multiplicities, contrary to D~2C+2f. Thus L has 2C and the residual 2f over M must be two distinct multiplicity-one fibers. A degree-two prime cannot have fiber class, and a doubled fiber is already excluded. Their disjoint paired zeros contradict singleton fibers.

On F2 there is no degree-two prime. The thick-line split is either 2C_min+2F or 2F1+2F2. The first leaves class 2f over M, again forcing the excluded disjoint fiber pair. The second already has disjoint paired zeros over L; alternatively its residual 2C_min over M cannot be a degree-two prime, two distinct primes in the unique C_min class, or the excluded doubled prime. This exhausts the actual classes.

Every step takes place at the actual generic Artin scheme or on the smooth normalization. It does not extend a deck involution through the nongorenstein vertex, invoke flatness there, or assume a scheme-theoretically reduced conductor.

## 3. Alternative local trace bridge at the nongorenstein crossing

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

## 4. Why the reduced conductor is insufficient

### 4.1. Nonreduced D over the smooth integral conductor

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

## 5. Explicit generic countermodels

The following local algebras prevent overgeneralizing the compression
step; none is asserted to be a global quartic normalization.

- Let A=K[epsilon]/(epsilon^2) and B=K[t]/(t^4), epsilon=t^2.
  The quadratic trace-zero generator t has t^2=Delta=epsilon, which is
  nonzero although B is nonreduced.
- Let B=K(sqrt(d))[epsilon]/(epsilon^2) over A with d a nonsquare unit.
  Then Delta=d is a unit while B remains nonreduced through the base
  nilpotent epsilon.
- In B=A times A with the involution exchanging the two primes, take
  f=(1,zeta_3). Its cube descends to A but its square does not. Applying
  the involution twice does not force a square when it swaps primes.

The [exact generic-algebra checker](../computations/audit_session_scroll_gorenstein_generic_2026_10_08.py)
retains these models and their rank/length calculations. In particular
Section4's Delta=0 assertion uses smooth reduced Gamma, not an arbitrary
nonreduced base Artin ring.

## 6. A conditional transverse-plane explanation

This alternate transverse-plane proof is retained as an independent
research route, with its geometric slice passage conditional on the slice hypotheses below. The exact Artin proof in
[nongorenstein cubic classification](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md#4-the-whole-nongorenstein-cubic-schemes)
and its [independent audit](#2-the-remaining-nongorenstein-schemes)
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

### 6.1. Double-line-plus-line support

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

### 6.2. Triple-line support

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
prime of multiplicity two is excluded by Section2.4 above. For the
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



## Characteristic boundary and evidence

The exact finite-length module identities remain algebraic under their
hypotheses. Coefficient fields and the field-trace Frobenius pairing use
separability. Root-of-unity rigidity in a local Artin ring uses n invertible:
in positive characteristic, nilpotent corrections can be killed by p-powers.
The differential ending also uses n nonzero in the field. These arguments
therefore do not contradict the actual fixed-C0 quartic-carrier STCI
constructions in every positive characteristic. No generic module is
substituted for the entire conductor at a bad point. The full accepted proofs, explicit countercontrols and distinct conditional
transverse-plane route were independently compared with the retired sources
and accepted for consolidation. The slice passage retains those conditional hypotheses; no CAS rerun or wider exclusion is claimed.
