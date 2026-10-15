# Moving first relations: spectral descent criterion and elliptic gap examples

Date: 2026-10-14. Author: `moving_second_general/spectral_audit`.
Status: **NEW PROOF, independently derived for the parent moving-relation lane.**
No inherited pure-power, tower, or normal-carrier certificate was rerun.
The statement being audited is [Root-curve descent and the geometry of
moving binary relations](2026-10-14-generalization-spectral-root-curve-relations.md).

This note proves a criterion for an abstract graded algebra on a curve.
It does not construct a multiple structure in the actual formal neighborhood
of `C0`, and it does not produce a set-theoretic complete intersection in
projective space. In particular, a second generator in the quotient by the
first relation must be distinguished from a global line of polynomials.

## 1. Setup and the root divisor

Let `C` be a smooth connected projective curve over an algebraically closed
field, let `V` be a fixed two-dimensional vector space, and put

    E = H^(-1) tensor V,       S = Sym(E).

Suppose a saturated first relation is the line subbundle

    R = H^(-r) tensor M  ->  Sym^r(E),
    M -> Sym^r(V),             r >= 1.

Here subbundle means that the map is nonzero in every fiber; equivalently,
its cokernel is locally free. Write `deg(M)=-epsilon`.
Use the convention that the second factor in

    P = C x P(V*),       p:P->C,       q:P->P(V*)

has `H^0(O(1))=V`. The relation is a section

    f in H^0(P, p^*M^(-1) tensor q^*O(r)).

Its zero scheme `Z` is an effective Cartier divisor, finite flat of degree
`r` over `C`: no fiber of `p` is a component, and every fiber divisor has
length `r`. This assertion includes nonreduced root divisors. Denote the
finite flat projection by `pi:Z->C`, and set

    N = q^*O(1)|Z.

For `s>=r-1`, pushing forward the divisor sequence, with the usual
cohomology of `O(s-r)` on `P1`, gives an exact sequence

    0 -> M tensor Sym^(s-r)V -> Sym^s V -> pi_*N^s -> 0,       (1)

where the left term is zero when `s=r-1`. Consequently, for the degree-`s`
part of the quotient by the first relation,

    A = S/(R),
    A_s = H^(-s) tensor pi_*N^s,                s>=r-1.        (2)

The order convention in (1) makes the sign of the later descent degree
unambiguous.

## 2. Exact criterion for a coprime quotient relation

Fix `s>r` and a line bundle `T` on `C`. By finite adjunction and (2), a
map `T->A_s` is equivalent to a section

    sigma in H^0(Z, N^s tensor pi^*(H^(-s) tensor T^(-1))).   (3)

At a point `c in C`, choose local trivializations and a polynomial lift
`g` of this quotient relation. The following are equivalent:

1. `f_c` and `g_c` have no common projective root, including scheme
   structure at multiple roots of `f_c`.
2. The restriction of `g_c` to the finite scheme `Z_c` is a unit in its
   corresponding invertible module.
3. `sigma` is nonvanishing at every point of `Z_c`.

For a local Artinian ring an element is a unit exactly when its residue
at its closed point is nonzero, so this equivalence retains the full
nonreduced root scheme. It is unaffected by changing `g` by a multiple of
`f`.

It follows that a fiberwise coprime quotient relation `T->A_s` exists if
and only if

    N^s tensor pi^*(H^(-s) tensor T^(-1)) is trivial,

or, equivalently,

    N^s = pi^*(H^s tensor T) in Pic(Z).                      (4)

A trivialization gives such a map, and its image is a subbundle of `A_s`:
on every base fiber the adjoint map is nonzero, hence the cokernel of the
map from a line bundle to a vector bundle is locally free.

Allowing `T` to vary, the exact obstruction is the class

    alpha = [N] in Pic(Z)/pi^*Pic(C).

There is a coprime second quotient generator in degree `s` precisely when
`s alpha=0`. If `alpha` has finite order `m`, the possible degrees are
exactly the multiples of `m` that exceed `r`. If `alpha` has infinite
order, no such degree exists. This is a Picard-group obstruction, not
merely a numerical degree obstruction.

The norm provides a useful necessary condition. For this root divisor,
the determinant of (1), together with its degree-zero analogue, gives

    Norm_pi(N) = M^(-1),

up to a fixed one-dimensional `k`-vector space, which is a trivial line
bundle on `C`. Taking norms in (4) therefore gives

    (H^s tensor T)^r = M^(-s).                              (5)

The norm identity `Norm_pi(pi^*D)=D^r` for finite locally free maps is
also recorded in [Stacks, Norms, Lemmas 31.18.2 and
31.18.6](https://stacks.math.columbia.edu/tag/0BCX).
Equation (5) is necessary; it does not replace (4).

## 3. On `P1`: the sign and the global-lift obstruction

Now take `C=P1` and `deg H=h`. Since `Z` has bidegree
`(epsilon,r)` in `P1 x P1`,

    deg N = epsilon,       deg(pi^*O(d)) = r d.

Thus (4) forces

    H^s tensor T = O(d),
    d = s epsilon/r,
    deg T = -s h + s epsilon/r.                            (6)

In particular `r` must divide `s epsilon`. The sign of `d` is positive
when the first relation moves (`epsilon>0`). This numerical divisibility
is only necessary; (4) also controls a degree-zero class on `Z`.

The exact sequence of degree-`s` relations of the resulting ideal is

    0 -> R tensor Sym^(s-r)E -> I_s -> T -> 0.              (7)

A global second polynomial line would be a lift `T->I_s->Sym^sE`.
Such a lift exists exactly when (7) splits. For `epsilon>0`, (6) shows
that a lift is impossible:

    Hom(T,Sym^sE)
      = Hom(O(s epsilon/r), Sym^sV tensor O)
      = 0.                                                (8)

Thus a moving first relation and a fiberwise coprime quotient second
relation necessarily have a nonsplit relation extension. An argument
that treats `T` as a subline of `Sym^sE` would discard these families.

Nevertheless, (4) does define a global graded ideal. Form in `A` the
ideal generated by the quotient line `T->A_s`, and take its inverse image
in `S`. Locally on `C` the map lifts to a polynomial `g`, so this ideal
is `(f,g)` locally; on overlaps two such lifts differ by a multiple of
`f`. Every fiber is a homogeneous complete intersection of degrees
`r,s`. The graded quotient is finite locally free of rank `rs`, with
the standard complete-intersection Hilbert function. This follows also
from the local Koszul resolution and fiberwise regularity. No assertion
of a global split two-generator resolution is needed.

## 4. Elliptic `(2,2)` examples with arbitrary second degree

Work in characteristic zero. Fix any integer `m>2`. Choose a smooth
elliptic curve `E0`, a line bundle `A0` of degree two, and a line bundle
`Q` of exact order `m` in `Pic^0(E0)`. Put

    B0 = A0 tensor Q.

Such `Q` exists because, over an algebraically closed field of
characteristic zero, the elliptic `m`-torsion is `(Z/mZ)^2`.
For the standard degree/separability input see [MIT 18.783, Lecture 6,
multiplication and torsion](https://math.mit.edu/classes/18.783/2022/LectureSlides6.pdf).
The construction can also be made in characteristic `p` for `m` prime
to `p`; the characteristic-zero version suffices here.

Riemann--Roch gives `h^0(A0)=h^0(B0)=2`, and both line bundles are
base-point-free: after removing a putative base point, a degree-one line
bundle would still have two sections, contrary to Riemann--Roch on a
genus-one curve. This is also the degree-`2g` global-generation case in
[Stacks, Lemma 53.22.3](https://stacks.math.columbia.edu/tag/0E3C).
Their complete linear systems give two degree-two maps and hence

    j:E0 -> P1 x P1.

Here is a proof that `j` is a closed immersion, rather than an assumption
about a generic pair. The degree of `E0` over its image divides two. If
it were two, both image projections would have degree one, so the image
would be a `(1,1)` graph and `A0=B0`, contradicting `Q!=O`. Thus `j` is
finite birational onto an integral `(2,2)` curve. A `(2,2)` curve has
arithmetic genus `(2-1)(2-1)=1`, while its normalization has genus one.
The normalization exact sequence therefore has zero quotient, proving
that the image is normal and `j` is an isomorphism onto that smooth
image. In particular the embedded curve is a smooth root divisor `Z`
with

    r=2,       epsilon=2,
    pi^*O(1)=A0,       N=B0.

For any `s>2`, descent of `N^s` to the first `P1` forces its descended
degree to be `s`. Hence

    N^s in pi^*Pic(P1)
      iff B0^s = A0^s
      iff Q^s = O
      iff m divides s.                                    (9)

The first possible coprime second quotient relation is therefore exactly
degree `m`. Choosing a trivialization for `s=m` and applying section 3
gives a finite locally free graded algebra with fiber type `(2,m)`.
The first relation has fixed order two and moving degree two, while the
gap `m-2` is arbitrarily large. These examples demonstrate that no bound
on the second degree can follow from `r` and `epsilon` alone.

## 5. Exact `C0` numerical boundary for these abstract families

Take `H=O(7)` on `P1`, as in the accepted balanced conormal bundle of
`C0`. In the elliptic construction at second degree `s=m`,

    E=O(-7)^2,      R=O(-16),      T=O(-6m),
    n=2m,          top graded degree=m.

The relative Artin complete-intersection socle line is

    Soc = R tensor T tensor det(E)^(-1) = O(-6m-2).        (10)

This formula is valid with the nonsplit relation extension (7): local
changes of the second generator by multiples of the first do not change
the determinant of the relation generators, and the local Koszul socle
identifications glue.

The Hilbert function is

    h_0=h_m=1,       h_j=2 for 1<=j<=m-1,

so its first moment is `m^2` and the accepted asymmetry is zero. The
normal-layer defects can be computed directly. For `2<=j<m`, sequence
(1) gives the normalized degree `2(j-1)` in rank two. In the top degree,
(10) gives defect `m-2`. The total is therefore

    Delta = 2 sum_(j=2)^(m-1)(j-1) + (m-2)
          = m(m-2).                                      (11)

Were this abstract algebra the associated graded algebra of an actual
complete intersection of degrees `a,b` supported on `C0`, its length and
socle would require

    ab=8m,
    14-4(a+b)=-6m-2,
    equivalently (3a-16)(3b-16)=64.                        (12)

For integers `a,b>=5`, the only solutions are

    (a,b,m)=(8,8,8), (6,16,12), (16,6,12).                (13)

Indeed the two factors in (12) are each congruent to two modulo three;
among positive factor pairs of 64 this leaves `(8,8)` and `(2,32)` and
their interchange. The negative-factor possibility with `a,b>=5` gives
only `(-1,-1)`, whose product is not 64.

For (13), the accepted full socle budget is satisfied exactly:

    mu=7m+14-4(a+b)=m-2,
    n mu=2m(m-2)=2 Delta,
    Asym=0.

Thus the full scalar socle budget and the abstract graded-CI condition
alone do not remove these two unordered degree pairs. Their existence
as abstract algebras is a boundary for that method. Realization in the
actual normal-neighborhood transitions, and then by two projective
equations, remain entirely unproved and may be obstructed.

## 6. The actual ambient lifting problem has a spectral obstruction group

The abstract examples identify an obstruction that the next step must use:
compatibility with the actual formal-neighborhood transitions. Here is
the target group for that problem, with the distinction between the
group and its actual obstruction class retained.

Fix local lifts of the first relation and suppose they have been made
compatible through normal degree `r+k-1`. Suppose also that the next
independent relation has degree `s>r+k`. In normal degree `r+k`, the
remaining mismatch, modulo multiples of the first relation, is a
1-cocycle with coefficients in

    Hom(R,A_(r+k))
      = pi_*(N^(r+k) tensor pi^*(H^(-k) tensor M^(-1))).

Changing local lifts changes the cocycle by a coboundary. Thus the
order-`k` first-relation obstruction lies in

    H^1(Z,L_k),
    L_k = N^(r+k) tensor pi^*(H^(-k) tensor M^(-1)).       (14)

Vanishing of this particular class is equivalent to correcting this
one order, once the lower-order choices have been fixed. Formula (14)
is a linearized lifting statement, not a claim that all such classes
occur for the fixed embedding of `C0`. At and above degree `s`, the
second relation changes the quotient target and must be included.

For `C=P1`, `deg H=h`, its degree is

    deg L_k = (2r+k) epsilon - r k h.                     (15)

Adjunction for the Cartier divisor `Z` gives the useful dual expression

    omega_Z = N^(r-2) tensor pi^*(omega_C tensor M^(-1)),
    omega_Z tensor L_k^(-1)
      = N^(-k-2) tensor pi^*(omega_C tensor H^k).         (16)

In the elliptic example with `r=epsilon=2`, `h=7`, and `k=1`,

    L_1 = N^3 tensor pi^*O(-5),
    deg L_1=-4,          h^0(L_1)=0,          h^1(L_1)=4.  (17)

There are four obstruction coordinates, and no global first-order
correction once a particular lower lift has been fixed. The existence
of this four-dimensional group does not say that the actual obstruction
class is nonzero. Conversely, the abstract algebra construction of
sections 3--5 does not force this class to vanish.

The contribution of the quadratic normal-coordinate transition has a
geometric factorization. Assume here that `Z` is smooth and `pi` is
generically separable. Restricting the relative derivative of `f` to `Z`
gives a section

    rho in H^0(Z,N^(r-2) tensor pi^*M^(-1)),              (18)

whose zero divisor is the ramification divisor of `pi`. A quadratic
normal vector field, modulo its radial component, gives a cubic
projective displacement. After restriction to `Z`, its coefficient is a
section of `N^3 tensor pi^*H^(-1)`. Applying the derivative to `f` is
multiplication by `rho`, producing a section of `L_1` exactly as in
(14). In binary coordinates this is the familiar factorization through
the cubic `x delta(y)-y delta(x)`; the radial part is a multiple of `f`
and vanishes in the quotient.

For a moving relation, normal-coordinate changes are not the entire
ambient cocycle. Changes in the base coordinate contribute derivatives
of the coefficient functions of `f`, and previous correction terms
contribute at later orders. Those terms must be retained in the actual
class in (14). The factorization (18) describes the pure normal
quadratic contribution only. For a nonreduced root divisor, it is not
permissible to treat `rho` as a nonzero divisor or replace the full
scheme by its reduced support.

This supplies a structural route forward: compute the actual class in
(14), or its Serre-dual pairing using (16), on the root curve. Counting
the dimension of its target, or using only the numerical defect, cannot
settle the lifting problem. The smooth elliptic examples have generically
two distinct root directions, so they also show why a theorem for a
moving pure power does not automatically cover an arbitrary moving
first relation.

## 7. Coordinate-free first class on the blowup

The owner's blowup interpretation gives a precise way to name that
actual first class. Let `X` be the actual smooth ambient threefold,
`Xtilde=Bl_C X`, and identify its exceptional divisor with
`P=C x P(V*)`. The conormal line of this divisor is

    J=O_P(-Exceptional)=p^*H^(-1) tensor q^*O(1).

This sign follows from the tautological normal line:
`N_(P/Xtilde)=p^*H tensor q^*O(-1)`. The square-zero first neighborhood
of `P` has an extension class

    kappa in Ext^1_P(Omega_P,J).

Since `P` is smooth, this is `H^1(P,T_P tensor J)`. Restrict this
extension to `Z` and pull it back along the conormal differential

    df:O_Z(-Z) -> Omega_P|Z.

The resulting class lies in

    Ext^1_Z(O_Z(-Z),J|Z)
      = H^1(Z,O_Z(Z) tensor J|Z)
      = H^1(Z,L_1).                                    (19)

It is the obstruction to extending the Cartier divisor `Z` into the
first neighborhood of `P`. A local equation proof identifies it with
the mismatch in section 6: lifting each local equation for `Z` and
comparing on overlaps applies the transition derivation to that
equation. Changing its lift changes only a coboundary. Consequently
(19) is the actual geometric class, rather than an unspecified element
of a group of the right dimension. It still needs to be evaluated for
the fixed ambient embedding.

For `C=P1` and `H=O(7)`, the product tangent splitting gives

    kappa_base in H^1(P,O(-5,1)),       dimension 8,
    kappa_direction in H^1(P,O(-7,3)),  dimension 24.     (20)

Both components contribute through `df`; retaining only the direction
component omits the derivative of a moving relation in the base.

For a smooth `(2,2)` root divisor, `L_1=O_Z(-5,3)` and its divisor
sequence is

    0 -> O_P(-7,1) --f--> O_P(-5,3) -> L_1 -> 0.

Both ambient `H^0` groups vanish, `H^2(P,O(-7,1))=0`, and
`H^0(Z,L_1)=0` by its negative degree. Thus there is an exact sequence

    0 -> H^1(P,O(-7,1)) --f--> H^1(P,O(-5,3))
      -> H^1(Z,L_1) -> 0,

with dimensions `12 -> 16 -> 4`. In particular, the four-dimensional
obstruction space in (17) is exactly this quotient. The middle
cohomology class, taken modulo the image under multiplication by `f`,
must be built from the actual `kappa` and `df`. The quotient description
does not itself say that the class vanishes or is nonzero.

## Audit conclusion

The spectral criterion (4), the positive sign in (6), the mandatory
nonsplitting (8), the arbitrary elliptic gap construction (9), and the
numerical boundary (13) all pass this independent derivation. The
criterion concerns a second relation modulo the first. It must not be
reported as the existence of two global polynomial line subbundles or
as an ambient STCI construction. The spectral obstruction bundle
(14), its dual (16), and the elliptic four-dimensional target (17) also
pass. The coordinate-free class (19), its base/direction decomposition
(20), and the exact `12 -> 16 -> 4` quotient pass as well. No value or
nonvanishing of the actual `C0` obstruction class has been asserted.
