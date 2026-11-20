# Fixed quadratic-cover splitting and the conductor

**Setting.** Let \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed
field of characteristic different from two. Put \(r=2x_1x_2-x_0x_3\)
and \(X=V(z^2-r)\subset\mathbf P^4\). A carrier is **split in this
fixed quadratic cover** when \(r\) is square in its function field,
using an affine trivialization. This condition is distinct from splitting
of a first normal cone; no equivalence is asserted.

**Conductor theorem.** For a proper supported pair \(Y=V(F,G)\), with
\(F\) integral of degree \(a\ge5\), fixed-cover splitting forces
\(a=2m\) and \(F=P^2-rQ^2\), with \(\deg P=m\),
\(\deg Q=m-1\) and \(\gcd(P,Q)=1\). If \(Q|_C\ne0\), its signed
complete intersection is the separated branch and
\[
 B/A\simeq(S/(P,Q,G))(-1),\qquad
 J_\Delta=(P,Q,G),\qquad \delta=m(m-1)b.
\]
The upstairs conductor ideal is \((P,Q,G)\), whereas the conjugate-branch
intersection has ideal \((P,zQ,G)\). Their lengths differ as in the
[attachment formula](quadratic_covers_and_conductor_descent.md#8-attachment-and-a-global-lower-bound-on-boundary-length).
The zeros of \(Q|_C\) must be confined to the two marked endpoints;
an integral split carrier smooth at both endpoints has no mate in any degree.

**Proof map.** The [factorization and conductor proof](#split-carrier-the-conductor-is-an-actual-complete-intersection)
retains both schemes and their lengths. When \(P|_C=Q|_C=0\), the
[primary-piece postulation lemma](#two-lift-split-carriers-actual-primary-pieces-control-postulation)
replaces that complete-intersection branch presentation. For sextics the
stronger [two-lift exclusion](two_lift_sextic_exclusion.md#supported-exclusion-and-proof-map)
settles that entire sector; the primary-piece calculation remains an
explanation of postulation, and applies more generally in degree \(2m\).

**Review provenance.** The relocated proofs retain the scopes assessed in the
[consolidated review of PR #167](https://github.com/markluxton1/STCI/pull/167#issuecomment-7043663699),
reviewed head `4d1b03cdf4671a7b1e987cb641a3509de23e9a5c`. The present
organization separates those existing arguments; it does not extend their
source hypotheses or claim a fresh rerun of historical computations.

## Split carrier: the conductor is an actual complete intersection

Let \(Y=V(F,G)\) be a proper complete intersection with sole reduced
support \(C\), with \(F\) integral of degree \(a\ge5\) and \(G\) of
degree \(b\). This discussion does not require \(a\le b\). Work over
the algebraically closed ground field with \(2\) invertible. Write
\(X=V(z^2-r)\subset\mathbf P^4\) for the fixed smooth quadric
threefold and \(D,D'\) for its two reduced lifts of \(C\).
If \(r\) is square in \(k(V(F))\) in an affine trivialization,
the pullback of \(V(F)\) to \(X\) consists of two distinct conjugate
prime divisors, each with multiplicity one: the generic point is off
the branch quadric and the generic extension splits. Finiteness
excludes further divisors over lower-dimensional subsets. The
[SGA 2, Exposé XII, Corollary 3.7 (Grothendieck–Lefschetz)](https://arxiv.org/pdf/math/0511279)
gives \(\operatorname{Pic}(X)=\mathbf Z[\mathcal O_X(1)]\).
Conjugation preserves this generator, so \(a=2m\). A section cutting
out one divisor is \(P+zQ\), with \(\deg P=m\) and \(\deg Q=m-1\),
by the double-cover module decomposition. The product of the two
sections cuts out the full pullback. Rescaling \(F\), we have
\[
F=P^2-rQ^2,\qquad \gcd(P,Q)=1 .
\]
In particular, an integral odd-degree carrier is always nonsplit in
this cover.

Suppose \(Q|_C\not\equiv0\). Choose conjugate signs so that
\(P+zQ\) vanishes on \(D\). The other factor is a unit at the
generic Artin point over \(D\); on \(D'\) the roles reverse.
Thus \(W=V_X(P+zQ,G)\) and its conjugate are precisely the two
separated branch schemes. Indeed the equations cut a proper
complete intersection (the integral factor surface dominates
\(V(F)\)); its curve support can only be \(D\), and it has the
same full generic algebra as the separated branch. Both schemes are
locally Cohen–Macaulay, so equality at the generic point gives equality
everywhere, with their saturated homogeneous ideals. In particular,
\(W\) is ACM in this case, without an ACM hypothesis on the general
separated branch.

Here the conductor and the conjugate-branch intersection have
different scheme structures. With \(S=k[x_0,x_1,x_2,x_3]\) and \(A=S/(F,G)\),
the branch ring is \(B=S[z]/(z^2-r,P+zQ,G)\). Modulo the
image of \(S\) in \(B\), the coefficient of \(z\) is taken
modulo \(P,Q,G\): the two relations over \(S\) from the norm
factor are \(P+zQ\) and \(rQ+zP\). Consequently
\[
B/A=(S/(P,Q,G))(-1),\qquad J_\Delta=(P,Q,G).
\]
The upstairs conductor scheme is cut out by \((P,Q,G)\) in \(X\),
with the same equations defining the conductor downstairs. In contrast,
since two is invertible, the conjugate-branch intersection has ideal
\[
 I_{W\cap W',X}=(P+zQ,P-zQ,G)=(P,zQ,G).
\]
On \(W\), its ideal is \(z\mathfrak c\), whereas the conductor ideal
is \(\mathfrak c=(P,Q)\mathcal O_W\). Thus at endpoint \(i\) the
upstairs conductor has length \(2\delta_i\), while the branch attachment
has length \(2n+2\delta_i\), with \(n=ab/4\), exactly as in the
[attachment formula](quadratic_covers_and_conductor_descent.md#8-attachment-and-a-global-lower-bound-on-boundary-length).
Since \(B/A\) is nonzero with finite projective support, and
\(P,Q\) have no common component, \(P,Q,G\) form a homogeneous
regular sequence. This determines the **entire** conductor Hilbert
function, not just its low-degree onset:
\[
\delta=m(m-1)b,\qquad
\sum_{d\ge0} \dim_k(S/(P,Q,G))_d\,t^d
=\frac{(1-t^m)(1-t^{m-1})(1-t^b)}{(1-t)^4}.
\]
Its Artinian reduction is Gorenstein of socle degree
\(2m+b-4=a+b-4\); the [complementary inequality (7a)](quadratic_covers_and_conductor_descent.md#8-attachment-and-a-global-lower-bound-on-boundary-length) is an
equality in every degree by the symmetry of this h-vector.

Even before taking the mate section, the signed factor surface
is finite birational to \(V(F)\). The same two relation columns,
now without \(G\), identify the relative conductor as \((P,Q)\)
downstairs and as \((Q)\) upstairs, using \(P=-zQ\) there.
This is the conductor of the finite partial cover, not necessarily
of the normalization.

Set-theoretically \(V(P,Q,G)\) lies on \(C\), and on \(C\),
\(P=0\) wherever \(Q=0\). Off the two marked endpoints the
cover separates without any conductor. Hence **all** zeros of
\(Q|_C\) must lie at the two marked endpoints. In binary
coordinates on \(C\cong\mathbf P^1\), its restriction must be
a nonzero scalar times a monomial of degree \(4(m-1)\).
There is also an exact local split of the length. If \(h_i\)
is the order of \(Q|_C\) at the marked endpoint \(i\), then
\(\operatorname{length}(A_i/QA_i)=nh_i\), with \(n=ab/4\).
This follows from the determinant of multiplication by \(Q\)
on the free endpoint lattice: generically its reduction is the
scalar \(Q|_C\), and the remaining part is nilpotent. Locally
\(A_i/(Q)\) is cut out by \(P^2,Q,G\), so its length is
twice that of the conductor cut by \(P,Q,G\), by the two-step
filtration by \(P\) and regularity. Therefore
\(\delta_i=nh_i/2\); in particular \(h_i\) is even if \(n\) is odd.

Any zero of \(Q|_C\) gives \(P=Q=0\) there and makes
\(V(F)\) singular. Since \(4(m-1)>0\), an integral
split carrier smooth at both marked endpoints cannot have a mate
in **any** degree. This also covers the omitted case
\(Q|_C\equiv0\) for that smooth-endpoint assertion: then
\(P|_C\equiv0\) and the norm surface is singular along all of
\(C\). For the general split case, the binary-monomial restriction
remains necessary when \(Q|_C\not\equiv0\), not sufficient:
one still needs an actual mate with the prescribed local contact.
When \(Q|_C\equiv0\), both conjugate surfaces contain both
lifts, so cutting one factor surface by \(G\) no longer
isolates the branch. The complete-intersection presentation and
length formula do not extend by this argument.

The excluded locus is nonempty in every even degree \(2m\ge6\).
On \(X\), degree-\(m\) sections through \(D\) have base scheme
\(D\), since \(D\) is a rational normal quartic with ideal
generated by quadrics. Off \(D\) their linear system separates
general points and tangent vectors: on an open where one fixed
quadric through \(D\) does not vanish, it contains that quadric
times the complete degree-\((m-2)\) system. Bertini gives an
integral general divisor (irreducibility and generic smoothness
off \(D\)). The open condition that \(Q|_C\) be nonzero at both
endpoints is also nonempty: choose
\(Q=x_0^{m-1}+x_3^{m-1}\) and lift the prescribed restriction
\(-z|_D\,Q|_D\) to a degree-\(m\) form \(P\) downstairs.
The restriction in that degree is surjective for \(m\ge2\):
the weights of the quartic parameterization realize all binary
monomials of degree \(4m\). At either endpoint \(P=r=0\) and
\(Q\ne0\), so \(dF=-Q^2dr\ne0\) by smoothness of the branch
quadric. The general signed divisor and its
conjugate are distinct, as one contains \(D\) and the other does
not. Their norm defines an integral surface downstairs, because
the two reduced divisors have the same integral image and are
generically outside the branch quadric.

Both equations cannot be integral split carriers of the
nonzero-restriction type. Orient their signed factors so that the
positive factors contain \(D\) but not \(D'\). The positive factor
of \(F\) and the negative factor of \(G\) would cut a proper
intersection of two ample divisors on \(X\), hence a nonempty curve.
It lies in the pullback of \(Y\), but neither \(D\) nor \(D'\)
lies in both of those factors. This is impossible.

## Two-lift split carriers: actual primary pieces control postulation

Keep the norm factorization \(F=P^2-rQ^2\), but assume
\(P|_C=Q|_C=0\). For \(\epsilon=\pm1\) put \(S_\epsilon=P+\epsilon zQ\)
and let \(W_\epsilon\) be the \(D\)-primary piece of the actual
complete intersection \(V_X(S_\epsilon,G)\), defined by contraction
from the generic point of \(D\). The two generic lengths
\(\ell_\epsilon\) are positive and sum to \(n=mb/2\), by additivity
for the product of the two nonzerodivisors modulo \(G\) at that
point. Neither individual factor cuts the full generic branch.

For \(2d+2<b\), set \(k=d-m+1\). The space
\((J_\Delta)_d/(F)_d\) is the union of the two images of
\[
 \bigl(I_{W_\epsilon}/(S_\epsilon)\bigr)_k
 \longrightarrow (S/(F))_d,\qquad zA-\epsilon B\longmapsto AP+BQ.
\]
The source ideals are in the homogeneous coordinate ring of \(X\);
negative degrees are zero. Both maps are injective and at most one
source is nonzero in any given degree.

Indeed a conductor form \(h\) has a descent equation \(zh=P_h\)
on the separated branch. Its norm is zero modulo \((F,G)\), so
\(P_h^2-rh^2\) is in \((F)\) since its degree is below \(b\).
Multiplying by \(Q^2\) gives \(QP_h=\epsilon Ph\) in the carrier
domain for one sign. In the polynomial ring, reducing
\(QP_h-\epsilon Ph=FL\) modulo \(Q\) and using coprimality of
\(P,Q\) gives \(h\in(P,Q)\). Write \(h=AP+BQ\); cancellation
in the domain gives \(P_h\equiv\epsilon(ArQ+BP)\pmod F\).
On \(X\),
\[
 zh-\epsilon(ArQ+BP)=(zA-\epsilon B)S_{-\epsilon}.
\]
At the generic point of \(D\) cancel \(S_{-\epsilon}\) modulo \(G\)
in the ideal generated by \(S_\epsilon S_{-\epsilon}\); the two
factors are nonzerodivisors there. This gives exactly membership
in \(I_{W_\epsilon}\). Conversely such membership gives descent
by the generic calculation and saturation of the locally
Cohen–Macaulay separated branch.

The Koszul change \((A,B)\mapsto(A+QT,B-PT)\) changes the source
by \(\epsilon T S_\epsilon\). A multiple \(h=FL\) comes from
\(zL S_\epsilon\), after which the Koszul change gives the entire
kernel. Conversely multiplication by \(S_\epsilon\) maps to a
multiple of \(F\) by expanding in the basis \(1,z\). If a class
came from both signs, the two values of \(P_h\) would agree
by injectivity of \(A=S/(F,G)\) into the branch ring, and hence
agree modulo \(F\) because their degree is below \(b\).
The signed norm equations give \(2Ph=0\) in the carrier domain,
so the class is zero. The union is a vector space; it cannot
be a union of two proper subspaces. Thus at most one source
contributes.

A contributing degree-\(k\) section cuts a proper divisor on
the integral signed surface, contains \(W_\epsilon\), and has
degree \(2mk\) on \(X\). It follows that \(4\ell_\epsilon\le2mk\).
Since \(k<b/2-m\), the thicker piece never contributes. If
\(|\ell_+-\ell_-|\le m^2\), the thinner piece has length at least
\(mb/4-m^2/2\) and neither contributes in the norm range.
In this nearly balanced sector, \((J_\Delta)_d=(F)_d\) for
\(2d+2<b\), giving the same postulation lower bound as in the
nonsplit case. In general the onset holds for
\(k<2\min(\ell_+,\ell_-)/m\); it also holds for \(k\le1\)
because \(D\) has no linear equation. At equality in the degree
test the proper intersection has no residual and is precisely
\(W_\epsilon\), by purity and equality of generic ideals.
The nonzero source is then one-dimensional: its section is
determined up to scalar modulo the signed equation.

For a split sextic, \(m=3\), the first possible degree is \(d=4\)
in the norm range \(b>10\). The thinner piece must have length
at most three. At length one it is \(D\), and all five quadrics
through \(D\) on \(X\) contribute. At length two the source consists
of quadrics through the actual double structure, of dimension
at most four since the five quadrics generate the ideal of \(D\).
At length three a nonzero source is one-dimensional and requires
an actual degree-\((2,3)\) pair on \(X\) supported only on \(D\).
This lemma is a postulation and contact test in degree \(2m\).
For sextics, its short-primary-piece alternatives are explanatory controls:
the [two-lift theorem](two_lift_sextic_exclusion.md#supported-exclusion-and-proof-map)
excludes every actual mate, including those alternatives.
