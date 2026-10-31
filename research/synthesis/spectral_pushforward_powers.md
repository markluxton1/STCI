# Spectral powers, syzygy determinants and graded constructions

**Status.** Independently reviewed provisional extension on
`codex/spectral-realization-2026-10-31`, based on consolidation `fd50fb6`. No canonical
result is promoted. The statements below concern actual spectral curves and
abstract graded algebras. They do not construct two ambient equations for C0.

The [fourth-power account](spectral_torsion_and_syzygy_splitting.md) gives the
existing actual second-obstruction application. The general
[spectral Picard criterion R-0008](../results/spectral_root_picard_criterion.md)
already constructs a fiberwise coprime graded second relation from a spectral
trivialization. The additional contribution here is a uniform coefficient
matrix for every power, together with recovery of that trivialization from
its kernel. The old [torsion and involution argument](../supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry)
and [arbitrary-order examples](../supplements/MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-relations)
are reused, rather than claimed as new constructions.

## 1. The pushforward of every power

Let k be algebraically closed, in any characteristic. Let
Z be a smooth divisor of bidegree (2,2) in
P1_base x P1_direction, and write

    pi = pr_base|Z,  A = O_Z(1,0),  B = O_Z(0,1),  eta = B tensor A^-1.

The curve is connected of genus one; pi is finite flat of degree two.
Both A and B have degree two. The line bundle eta is nontrivial: otherwise
their complete degree-two systems would identify the two projections up to
an automorphism, putting Z in a (1,1) graph.

**Theorem.** For every integer n>=2, put E_n=pi_*B^n. Then

    E_n = O(n-1) + O(n-1)       if eta^n is nontrivial;
    E_n = O(n-2) + O(n)         if eta^n is trivial.                 (1)

These are isomorphism classes, not chosen splittings. No separability,
division by n, or chosen origin on Z is used.

**Proof.** Push the divisor sequence

    0 -> O(-2,n-2) --f--> O(0,n) -> O_Z(0,n) -> 0

to the base. Direction-fiber H1 vanishes for n>=2, giving

    0 -> O(-2)^(n-1) -> O^(n+1) -> E_n -> 0.                       (2)

Thus E_n has rank two and degree 2n-2. Projection formula gives

    H0(E_n(-n)) = H0(Z,eta^n).                                    (3)

A degree-zero line bundle on a smooth integral projective curve has a
nonzero section precisely when it is trivial; that section is nowhere zero.
The dimension in (3) is therefore zero or one. Write
E_n=O(e1)+O(e2), with e1<=e2 and e1+e2=2n-2. Dimension zero implies
e2<=n-1 and hence both degrees n-1. Dimension one forces e2=n and
e1=n-2. This proves (1). Square.

## 2. One coefficient determinant for each power

Write

    f = a(z)u^2 + b(z)uv + c(z)v^2,

where a,b,c are homogeneous binary quadratics with no common base zero.
The dual of (2) is

    0 -> W_n -> O^(n+1) --T_(f,n)--> O(2)^(n-1) -> 0,
    W_n = E_n^*.

The matrix T_(f,n) has n-1 rows and n+1 columns; row i has a,b,c in
columns i,i+1,i+2 and zero elsewhere. Its transpose is multiplication
by the nonzero fiber polynomial f on direction forms of degree n-2,
so it has the indicated rank at every base point.

Twist by n-2 and take global sections. This gives a square coefficient map

    C_(f,n): H0(O(n-2))^(n+1) -> H0(O(n))^(n-1),
    dim(source) = dim(target) = n^2-1.                            (4)

Its entries are linear in the nine coefficients of f. Define
D_n(f)=det C_(f,n), after choosing monomial bases. Only its nonzero
scalar factor depends on those choices. By (1),

    dim ker C_(f,n) = h0(W_n(n-2))
                   = 0 if eta^n != O_Z, and 1 if eta^n = O_Z.     (5)

Consequently D_n detects eta^n=O_Z on the smooth-root locus and has
homogeneous degree n^2-1. It is nonzero in every characteristic: choose an
elliptic curve with a prime-to-characteristic torsion point of order not
dividing n and use the two-degree-two-bundles construction in section 4.
Formula (5) describes geometric fibers only:
no assertion about determinant multiplicities, reducedness of its parameter
scheme, or transverse intersection with an ambient compatibility locus is made.
This qualification is particularly important when char(k) divides n.
For n=2 and n=4, (4) recovers the existing 3-by-3 and 15-by-15 detectors.

The construction of the matrix and sequence (2) also makes sense for a
singular or nonreduced basepoint-free root. The independently reviewed
[full-root boundary analysis](spectral_pushforward_boundary.md) identifies
the additional hypotheses and the unbalanced reducible exception.

## 3. Recovering a positive graded object from the kernel

Suppose n>2 and D_n(f)=0 for a smooth root. A nonzero kernel vector in
(4) is a section of W_n(n-2). Since det E_n=O(2n-2), rank-two duality
identifies

    W_n(n-2) = E_n^*(n-2) ~= E_n(-n).                             (6)

The identification is up to the scalar choice of determinant frame. By
(3), this gives a nonzero section of eta^n, hence a trivialization of eta^n
and a nowhere-zero morphism A^n -> B^n on Z. Adjunction supplies the
corresponding subbundle O(n) -> E_n. On each length-two root fiber its
value is a unit, including at a ramification point with nonreduced fiber.

This is the missing input for the already proved R-0008 construction. In
its notation, for any line bundle H on the rational base, set

    E = H^-1 tensor k^2,  R = H^-2 tensor O(-2),
    Q_n = Sym^n E / (R Sym^(n-2)E) = H^-n tensor E_n.

The kernel-derived line is

    T = H^-n tensor O(n) -> Q_n.                                  (7)

Take the ideal generated by T in Sym E/(R), then its inverse image in
Sym E. Locally T lifts to a binary form g_n; the fiber ideals
(f_2,g_n) are regular sequences because the value of g_n is a unit on
the full root fiber. Their graded quotient is finite locally free of
rank 2n, with fiber type (2,n). This constructs an abstract graded
complete-intersection family directly from a coefficient kernel.

For the characteristic-zero quartic's balanced conormal frame H=O(7),
T=O(-6n). A global lift T->Sym^n E would lie in
H0(O(-n))^(n+1)=0. Thus the quotient line has local polynomial lifts
but no nonzero global polynomial-line lift. This is an actual feature
of the constructed graded family, not a contradiction to its existence.
Neither (6) nor (7) realizes it in the embedded formal neighborhood of C0,
and neither supplies a proper projective pair.

## 4. Exact-order and periodicity certificates

On the smooth-root locus put T[n]={f:D_n(f)=0}. The established Picard
interpretation and (5) give, set-theoretically,

    T[m] intersect T[n] = T[gcd(m,n)],  T[1] = empty.              (8)

Indeed eta is killed by m and n precisely when it is killed by their
greatest common divisor. For N>=2, eta has exact order N precisely when

    D_N=0 and D_(N/ell)!=0 for every prime ell dividing N,          (9)

where the index-one condition is omitted because eta is nontrivial.
These are finite exact-order tests using coefficients of the actual root.
They are not scheme-theoretic intersection or ideal-generation identities.

The reused involution argument identifies the composition of the two
ruling involutions with translation by eta on the genus-one curve. Thus
(9) is also an exact-period test for this automorphism, without computing
an elliptic group law. Its periodicity interpretation is inherited; the
uniform determinant and kernel extraction are the new coefficient realization.

The existing construction from a degree-two bundle A0 and a distinct
bundle A0 tensor eta on an elliptic curve realizes every exact torsion
order N>=2 in characteristic zero. The source's arbitrary N>2 argument
also works for N=2: nontriviality, rather than N>2, proves the product
map is a closed immersion. The rank sequence of (4) then drops exactly
at multiples of N. In characteristic p the same construction works
whenever an actual geometric torsion point of the required order is given;
prime-to-p orders are always available. No existence of geometric p-torsion
on every elliptic curve is assumed.

Within the unequal-degree first-relation convention of R-0008, we retain
n>2. The first allowed degree is therefore N for N>2, and 4 for exact
order two. Degree-two second relations lie outside this convention and
are not excluded by the determinant calculation.

## 5. An explicit order-three root

Over characteristic zero, take the smooth elliptic cubic

    y^2+y=x^3,  O=infinity,  P=(0,0).

The tangent y=0 meets the curve to order three at P, so P has exact
order three. The functions x and u=y/x define degree-two systems
with bundles A=O(2O) and B=O(O+(-P)), respectively. For u, the
apparent pole at P cancels, while the simple poles are O and -P.
Their ruling difference is eta=O((-P)-O), of exact order three.
Eliminating y=ux gives the biquadratic root

    x^2 - x u^2 - u = 0,
    f(s,t;u,v) = -st*u^2 - s^2*u*v + t^2*v^2.                    (10)

The two distinct degree-two bundles embed the elliptic curve as this
smooth (2,2) divisor by the reused product-map argument. Hence the
matrices C_(f,n) have corank one exactly when 3 divides n. In particular
n=3 supplies a graded family of type (2,3), and n=6 one of type (2,6).
These are deductions from the torsion construction and the theorem,
not a claimed computer-algebra execution or an ambient realization on C0.

## Review and remaining realization question

Independent review on 2026-10-31 by `review_spectral_powers` (GPT-6.1 Sol,
high reasoning) reconstructed the characteristic-free pushforward proof,
coefficient-map orientation, determinant/kernel identification, quotient-ideal
construction, exact-order tests and explicit example against R-0008 and its
retained proof. The review passed after clarifying that n>2 is the
unequal-degree convention, not a nonexistence claim for degree-two second
relations. No mathematical computation was needed or run.

The new construction ends at an abstract graded family. The next embedded
question is which of these families admit successive lifts in the actual
neighborhood of C0, with the fixed conormal embedding and all allowed higher
corrections retained. The order-three example with second degree six gives
a concrete starting object; one root does not cover its torsion stratum.
The inherited actual n=4 obstruction model keeps all hypotheses stated in
its owning chapter. No all-n ambient obstruction model, formal lift,
projective pair or change to C0's STCI status is asserted here.
