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
