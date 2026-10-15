# Nef polarizations bound formal surface branches over arbitrary smooth curves

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **NEW SCOPE GENERALIZATION; targeted independent review requested**.
The independently audited branch-algebraization/ruled-surface argument in
[smooth-root formal nonexistence](2026-10-15-generalization-smooth-root-formal-nonexistence.md)
is a premise. This note isolates its intrinsic form and computes the new
genus and degree expressions when the base curve is not rational. It does
not replay that proof or any accepted CAS certificate.

## 1. The underlying geometric criterion is independent of the blowup

Let `X` be a smooth projective threefold over an algebraically closed
field of characteristic zero. Let `Z` be a smooth connected projective
curve of genus `g`. Suppose there is a smooth embedded formal surface
`Vhat subset Xhat_Z`, with reduced scheme of definition `Z`, and put

    nu=deg N_(Z/Vhat).

Assume

    nu>4g+5.                                             (1)

Let `A` be a nef line bundle on `X`, and put `h=A.Z`. The audited
argument gives an integral algebraic surface closure `W subset X` and a
projective resolution of its chosen branch preserving `Z`. If

    d=A^2.W>0,

then necessarily

    d<=max_(a integer,a>=1)(2ah-nu*a^2).                 (2)

For completeness, the already audited argument uses Bost's geometric
formal algebraicity theorem to algebraize the branch, excellence to
preserve its smooth formal neighborhood after normalization, and
Hartshorne's high-self-intersection theorem to replace that neighborhood
by a section of a geometrically ruled surface. Pushforward of the nef
class to that model has numerical class `a Z0+b f`, with `a>=1`,
`a*nu+b=h`, and square at least `d`; its square is exactly the expression
in (2). This repackaging requires neither a rational base curve nor a
blowup presentation. The condition `d>0` is automatic for ample `A`.

If `A` is merely nef and its algebraic surface closure is contracted,
`d` may vanish; no positive-degree contradiction may then be inferred.
The blowup application below proves positivity separately.

The imported primary inputs are [Bost, Theorem 3.5 and Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf)
and [Hartshorne, Theorem 4.1, with the neighborhood-equivalence definition
in Section 0](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
Their exact hypotheses and the branch-normalization details are covered
by the [accepted full audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md).

## 2. Apply it over a smooth curve of any genus

Let `C subset P3` be smooth of degree `e` and genus `gamma`. Assume the
actual normal bundle has the form

    N_(C/P3)=L direct_sum L,     deg L=lambda.            (3)

This is a specific vector-bundle hypothesis. Equal numerical slopes,
semistability, or a decomposition into two line bundles of the same
degree do not imply (3). Equivalently, the associated projective bundle
must be trivial as a `P1`-bundle **over `C`**.

The tangent and Euler sequences give

    2lambda=4e+2gamma-2,
    lambda=2e+gamma-1.                                   (4)

On `B=Bl_C(P3)`, write

    E=C x P1,
    O_E(-E)=L^(-1) boxtimes O(1).

Let `M` be a line bundle on `C`, of degree `epsilon`, and let

    Z in |M boxtimes O(r)|

be smooth, connected, and finite over `C` of degree `r`. Consider a
compatible embedded Cartier lift of this root through every exceptional
neighborhood of `E`, with all local equation units retained.

Exactly as in the accepted rational-base theorem, it gives a smooth
formal surface `Vhat` along `Z`, transverse to `E`, and

    N_(Z/Vhat)=O_Z(E).

The product intersection and adjunction calculations are now

    Z^2_E=2epsilon*r,
    K_E.Z=r(2gamma-2)-2epsilon,
    g_Z=r*gamma+(epsilon-1)(r-1),                        (5)
    nu=lambda*r-epsilon,
    h=e*r.                                              (6)

The arithmetic genus in (5) replaces the rational-base formula. It
retains the actual genus of the base and requires no separability
assumption on the degree-`r` map for these intersection identities.

If

    nu>4g_Z+5,                                          (7)

the intrinsic criterion applies. As before, the algebraic surface closure
is not `E`, so it maps birationally to an integral surface `S subset P3`.
For the nef pullback `A` of a hyperplane, `d=A^2.W=deg S>0` and
`A.Z=h`. Thus there must be an integer `d>=1` with

    d<=max_(a integer,a>=1)(2ah-nu*a^2),                 (8)
    (d-1)(d-2)>=e*r*(r-1).                             (9)

Equation (9) is the accepted multiplicity/plane-adjunction argument:
the actual exceptional intersection contains `Z`, so `S` has generic
order at least `r` along `C`. A general plane meets `C` transversely in
`e` distinct points, and blowing up those plane points lowers the
arithmetic genus by at least `e*r*(r-1)/2`. Its integral strict transform
has nonnegative arithmetic genus. The base genus `gamma` does not enter
this plane calculation.

## 3. One numerical condition incorporates the higher-genus cases

By (4)--(6), threshold (7) is exactly

    (2e-3gamma+3-4epsilon)*r+3epsilon-9>0.               (10)

If also

    (e+gamma-1)*r>=epsilon,                             (11)

then `nu>=h`, so the maximum in (8) is attained at `a=1` and gives

    1<=d<=(1-gamma)*r+epsilon.                          (12)

Writing `D=(1-gamma)*r+epsilon`, all formal lifts in this scope therefore
obey the single opposing pair of inequalities

    D>=1,
    (D-1)(D-2)>=e*r*(r-1).                             (13)

The right side can be positive even when the permitted algebraic degree
`D` is very small. In positive genus, the term `(1-gamma)r` strengthens
the upper bound. Any parameters satisfying (10)--(11) but contradicting
(13) have no all-orders smooth embedded Cartier lift. This states the
general criterion directly instead of splitting it into degree or
root-order profiles.

For `gamma=0`, (10)--(13) recover the accepted rational-base criterion.
For `epsilon=2`, `e>=4`, and `r>=2`, condition (11) holds for every
`gamma>=0`. Whenever (10) holds, every `gamma>=1` is already impossible:
for `gamma=1`, (12) gives `d<=2`, contradicting the positive right side
of (9); for `gamma>=2`, (12) gives `d<=0`. Together with the accepted
rational case, this excludes every smooth movement-two formal root
satisfying the high-self-intersection threshold, regardless of the base
genus, under the specific normal-bundle hypothesis (3).

## 4. Scope retained

This is a necessary condition for an infinite formal first-relation
lift, not an exclusion of every finite-gap supported complete
intersection. The actual-CI-to-root bridge still requires all of its
accepted saturation, joint-leading-generation, smoothness, and generic
initial-regular-sequence hypotheses. No claim is made that (3) holds for
an arbitrary smooth space curve.

The line bundle `M` and its sections are actual data on `C`, not only an
integer degree. The numerical obstruction is uniform in those data,
but it does not construct a finite-type family over varying Picard
schemes or assert a new explicit finite cutoff. The accepted formal
finite-tower theorem was proved for its specified rational-base
coefficient open; transferring its representability and all-order
uniqueness to this larger setting requires stating the corresponding
relative family and cohomology hypotheses.

The arbitrary-characteristic extension is left to the separately
reviewed scope statement for the underlying geometric argument. The
present note fixes characteristic zero. No accepted theorem or
computation was replayed, and no canonical record or commit was changed.
