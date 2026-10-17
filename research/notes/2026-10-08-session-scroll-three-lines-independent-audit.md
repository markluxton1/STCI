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
