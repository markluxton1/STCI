# Nonnormal quartic carriers: smooth-locus reduction and ordinary projections

Date: 2026-10-07. Status: **PROVED lemmas and conditional exclusions;
classification scope and surviving singular strata retained**. The
unrestricted nonnormal-quartic lane remains open. No canonical frontier
file is edited by this note.

Throughout the proved lemmas, k is algebraically closed of characteristic
zero. Let X be an integral quartic containing a smooth rational curve C
of degree four, and assume X is regular at the generic point of C. This
includes the displayed MF6 carriers in the
[separate arbitrary-degree audit](2026-10-07-session-nonnormal-mf6-independent-audit.md).
Write nu:S->X for its finite normalization and H=nu*O_X(1).

## 1. Full support makes the lifted curve an embedded copy of C

Over the generic point of C the normalization is an isomorphism.
Consequently the full inverse image has exactly one curve component c,
finite and birational over C, together with possible isolated points.
The reduced curve c is isomorphic to C: an integral finite birational
extension of the integrally closed coordinate ring of a smooth curve
inside its function field is that coordinate ring itself.

If a mate G exists, its nonzero pullback is an effective Cartier divisor
whose full support is (nu^{-1}(C))_red. The
[full-support argument](2026-10-06-session-conductor-support.md) excludes
isolated inverse-image points. Therefore this entire support is c.
Every fiber above C has exactly one point, and nu|c is an isomorphism.

Write div_S(nu*G)=m c. If b=deg G, intersection with H gives

    4m=H.(m c)=H.(bH)=4b, hence m=b.

Thus b c is Cartier and linearly equivalent to bH as a Weil divisor.
This conclusion retains the support and finite-map hypotheses; it does
not assume all nonnormal carriers have a unique curve above C.

## 2. Smoothness is needed only along c

**Lemma.** If c lies entirely in the smooth locus of S, existence of a
mate forces the normalization's hyperplane sectional genus to be zero.

The divisor c is Cartier: near c the surface is smooth, and outside c
its defining ideal is the unit ideal. Thus b(c-H) is linearly trivial
and c is numerically equivalent to H. Choose a resolution sigma:M->S
which is an isomorphism near c, and let c# be its strict transform.
Then c# is a smooth rational curve and is numerically equivalent to
sigma*H. In particular c#^2=H^2=4. Adjunction gives

    K_M.c#=-6, so K_M.sigma*H=-6.

A general member of |H| is smooth, irreducible and avoids the finitely
many singular points of S; its inverse image in M has class sigma*H.
Its genus is therefore 1+(4-6)/2=0. This argument does **not** require S
to be globally smooth. No ADE or semi-log-canonical assumption is used.

**ADE variant.** Suppose instead that S has only ADE singularities and
take its minimal crepant resolution. Write its numerical pullback as
c#+Z equivalent to sigma*H, with Z the rational exceptional correction.
Put q=-Z^2=c#.Z. Since K_M is orthogonal to all exceptional curves,
K_M.c#=K_M.sigma*H. If pi is the hyperplane sectional genus, adjunction
gives

    c#^2=4-2pi, and q=2pi.

The formula is a necessary numerical condition. The existence of the
mate ensures that the correction is a rational divisor; no assertion of
Cartierness of c at the ADE points is made. Strict transforms of the
smooth curve stay isomorphic to C: the point-center ideals restrict to
nonzero invertible ideals on C during a resolution.

## 3. Source-scoped quartic classes

[Ducat, Quartic surfaces up to volume preserving equivalence (2024),
Proposition 3.3 and Table 3](https://d-nb.info/1317691679/34), pp.12-13,
records the following rational **semi-log-canonical** nonnormal classes,
using a smooth resolution M and H=d h-sum m_i e_i:

| Class | Double curve | H on M | K_M.H | pi |
|---|---|---|---:|---:|
| B1 | line | 4h-2e1-e2-...-e9 | -2 | 2 |
| B2 | conic | 3h-e1-...-e5 | -4 | 1 |
| B3 | twisted cubic | 3h-2e1-e2 | -6 | 0 |
| B4 | three concurrent lines | 2h | -6 | 0 |

These genera are derived here from H^2=4 and adjunction. Hence a B1 or
B2 carrier whose lifted C avoids normalization singularities is excluded
in every mate degree. For ADE normalizations the necessary values are
q=4 and q=2. The B3 normalizations are quartic rational scrolls; B4 uses
P2 polarized by O(2). The source theorem assumes semi-log-canonical
singularities over C; it is not an exhaustive theorem for arbitrary
nonnormal quartics. The original Urabe DOI/Project Euclid endpoints were
not readable in this audit, so broader classification is not promoted.

Two tempting transfers are invalid without further proof. A section of
a smaller degree on S need not descend through the conductor to X, so
the normal-carrier compressed mate exclusions cannot simply be reused.
An ADE singularity of S lying on its conductor is not an ADE local
hypersurface point of X; Jaffe's first-normal orders for X cannot be
assigned to it merely from the normalization graph.

## 4. Ordinary pinches force transverse conductor passage

In the ordinary pinch model the normalization is

    (u,v) -> (x,y,z)=(uv,u,v^2),
    X: x^2-y^2 z=0, D: u=0 upstairs.

At the pinch point the derivative of the image of a parametrized lifted
curve is (0,u',0). A smooth embedded image therefore requires u'!=0.
The lift meets D transversely, with local intersection multiplicity one.
At an ordinary double point there are two points in the normalization
fiber, contrary to section 1. The same full-support obstruction removes
ordinary triple points.

Consequently, if every singleton normalization fiber on the conductor
of a smooth normalized surface occurs at an ordinary pinch, and no
other singleton degeneration can meet C, a mate requires

    H.D <= number of ordinary pinch points.

This is an **ordinary-singularity hypothesis**, not a bound for all
semi-log-canonical degenerations.

For a projected quartic scroll with smooth anticanonical conductor D
mapping two-to-one onto its smooth twisted-cubic double curve, H.D=6.
The conductor is elliptic, and Riemann-Hurwitz gives four branch points.
If those points are ordinary pinches, section 4 requires six distinct
pinches and gives a contradiction. Thus this ordinary projected-scroll
subclass has no mate of any degree.

## 5. Ordinary projected Veronese surfaces

Suppose S=P2, H=O(2), and the normalization map is given by four
basepoint-free quadrics q0,...,q3. Assume its conductor is a reduced
anticanonical cubic and its singleton conductor fibers are ordinary
pinches; assume the homogeneous ideal of the maximal minors of the
4-by-3 derivative matrix has height two and defines reduced points.
These hypotheses describe the ordinary projection subclass. They do
not assert that every projected Veronese has ordinary singularities.

A mate forces the lifted c to be a conic: b c is linearly equivalent to
2b times a line and Pic(P2) is torsion free. Its conductor intersection
has degree six. Full inverse support and section 4 force six distinct
pinch preimages on c.

Let J=(partial q_i/partial x_j). Euler's formula gives J(x,y,z)^T=2q.
Since q never vanishes simultaneously, rank(J)<3 is exactly failure of
the projective differential to have rank two. Thus its maximal minors
cut out the ramification scheme R. The height-two hypothesis permits
the Hilbert-Burch resolution

    0 -> O_P2(-4)^3 -> O_P2(-3)^4 -> I_R -> 0.

It gives length R=6 and H0(I_R(2))=0. For example its Hilbert numerator
is 1-4t^3+3t^4, whose coefficient after division by (1-t)^2 at t=1
is six. Twisting the displayed sheaf resolution by two also directly
gives the no-conic assertion, since H1(P2,O(-2))=0. The
[author-hosted Hilbert-Burch statement with proof](https://ssather.people.clemson.edu/DOCS/HomAlgBook.pdf),
Theorem III.B.5.10, supplies this standard algebraic input.

The six distinct pinches are all six points of the reduced R. A conic
through them would contradict H0(I_R(2))=0. Therefore every carrier
meeting these ordinary-projection hypotheses is excluded in every
mate degree.

An explicit independent control is the standard Roman normalization

    [x:y:z] -> [yz:zx:xy:x^2+y^2+z^2].

This map is finite because its pullback O(1)=O(2) is ample and there is
no basepoint. On xyz!=0 its first three coordinates recover [x:y:z],
so it is birational and P2 is its normalization. The coordinate axes
are the conductor lines; their double maps have precisely the six
fixed points

    (0,1,+/-1), (1,0,+/-1), (1,+/-1,0).

The coordinate vertices have a common image and cannot meet C. Each
axis has exactly its two ordinary fixed pinches as singleton fibers.
A conic through the six fixed points has all cross coefficients zero
and its diagonal coefficients satisfy A+B=A+C=B+C=0. In characteristic
zero it is the zero form. Thus the explicit Roman carrier has no mate
for a smooth rational quartic, independently of the general resolution
calculation.

## 6. Why nodal conductor degenerations remain

At a degenerate pinch the normalization can be smooth with coordinates
(w,z) and map

    Y=-(w^2+z^2), X=wY, Z=z,
    X^2+Y^2(Y+Z^2)=0.

This is a finite birational normalization: w satisfies the monic
equation w^2+Y+Z^2=0 and equals X/Y in the common function field;
k[w,z] is integrally closed. The original hypersurface polynomial is
irreducible, for its expression as a quadratic in X has nonsquare
coefficient -(Y+Z^2) after removing the square factor Y^2.

The conductor upstairs is the nodal divisor w^2+z^2=0. Its two branches
map onto Y=X=0 with the same coordinate z, and the point w=z=0 has a
single normalization preimage. For every integer k>=2, the lifted curve
w=i z+z^k maps to a smooth curve, since Z=z is its parameter, but its
conductor intersection multiplicity is k+1. It has full inverse-image
support equal to that lifted curve locally: writing w_c=i z+z^k, the
pulled-back image ideal is

    (w-w_c)(w+w_c,Y_c), Y_c=-(w_c^2+z^2).

The cofactor's support at this germ is only (w,z)=(0,0), already on the
curve. Thus conductor contact at
a singleton degeneration can be arbitrarily large even for a smooth
embedded image.

This exact countermodel prevents replacing the hypotheses in sections
4-5 with just a count of branch-point supports, or replacing containment
of the full ramification scheme by passage through its reduced support.
The nonreduced ramification strata, degenerate cusps, singular
normalizations and non-semi-log-canonical carriers remain unresolved.

The companion [exact control verifier](../computations/verify_session_nonnormal_structural.py)
checks the four source-table genus calculations, Roman Euler/minor and
no-conic identities, and the degenerate-pinch contact calculation.
