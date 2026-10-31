# Independent audit: first-order missing-coordinate obstruction

Date: 2026-10-30. Reviewer: independent degeneration-audit agent (Sol/high),
continuing its bounded review of the opposite-limit proposal; no delegation.
Reviewed source: [the linear-series proposal](2026-10-30-four-streams-linear-series.md),
Propositions 2.1 and 4.1, Theorem 3.1, and their geometric conclusions.

**Disposition:** all stated mathematical claims pass independent hand
reconstruction. No material correction is required. The result is
**reviewed provisional**, with no canonical promotion. It settles
nonvanishing under specialization on the stated entirely-thick branch;
it neither excludes that branch nor settles the unrestricted STCI question.
No numerical computation, inherited verifier, or accepted proof was rerun.

## 1. Inputs and exact extension class

The curve is \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an
algebraically closed field of characteristic zero. Throughout this audit,
\(\mathcal O(d)\) on the curve means degree \(d\) on \(\mathbf P^1\),
so the ambient hyperplane bundle restricts to \(\mathcal O(4)\).
The balanced conormal \(E=\mathcal O(-7)^2\) is the precise promoted
input [R-0020](../results/quartic_conormal_characteristic_jump.md), not a
new conclusion here. Projection and the graph interpretation are prior
geometry in [the resolved-projection note](2026-10-24-p4-resolved-projection.md).

I checked [Bayer–Eisenbud, Appendix, Proposition 5A.2](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf):
its \(m=4,n=1\) case gives \(N_{D/\mathbf P^4}=\mathcal O(6)^3\).
There is also a direct hand verification in the present coordinates.
For \(f_i=s^{4-i}t^i\), the kernel of the derivative map
\(\mathcal O(-4)^5\to\mathcal O(-1)^2\) is the conormal bundle.
The three consecutive shifted vectors
\((t^2,-2st,s^2)\) are syzygies. Their band matrix has rank three
everywhere, using the first three rows when \(t\ne0\) and the last
three when \(s\ne0\); hence the kernel is \(\mathcal O(-6)^3\).
The characteristic-zero hypothesis supports the Euler/derivative
identification and the retained conormal splitting. No characteristic
extension is inferred here.

Because projection restricts to an isomorphism \(D\to C\), its tangent
map gives the exact normal sequence
\[
0\to\mathcal O(4)\to N_{D/\mathbf P^4}
\to N_{C/\mathbf P^3}\to0.
\]
Locally, a graph equation is \(w_i-e_i\), where \(e_i\) extends
the **specified section** \(e=s^2t^2\). The differences of these graph
equations on overlaps, accounting for the line-bundle frames, are
\(-(e_i-e_j)\). Reducing modulo \(I^2\) identifies them with the
section-lifting cocycle for \(L|_{V(I^2)}\), up to the stated sign.
Thus the extension
\[
0\to\mathcal O(-3)^2\to\mathcal O(-2)^3\to\mathcal O_C\to0
\]
represents this actual \(\delta_X(e)\), not merely some class having
the same ranks and degrees. On the endpoint overlap the explicit
expansion is indeed
\[
u^2-(u^3+a)^2/(u^4+b)=-2u^{-1}a+u^{-2}b
\pmod{(a,b)^2}.
\]

The zero global-section space of the middle bundle makes the boundary
of \(1\) nonzero. The four ambient sections lift, while
\(H^0(E\otimes L|_C)=0\), giving exactly four sections on \(X\).
If its tensor class in \(k^2\otimes H^1(\mathcal O(-3))\) had rank
at most one, a constant change of summands would split off one
\(\mathcal O(-3)\) from the middle bundle. That is impossible because
\(\operatorname{Hom}(\mathcal O(-2)^3,\mathcal O(-3))=0\).
This establishes rank two under every balanced splitting.

The comparison uses sheaf cohomology on the ambient space and vector
bundles on the support. It does **not** give \(\mathcal O_X\) an
\(\mathcal O_C\)-algebra structure or require a retraction.

## 2. Ordinary powers, initial ideals and pure hulls

For the regular codimension-two embedding, the successive layers of
ordinary powers are
\(I^j/I^{j+1}=\operatorname{Sym}^jE\). Their hyperplane twists are
\(\mathcal O(4-7j)^{j+1}\), with no global sections for every
\(j\ge1\). Therefore restriction on sections from each higher
ordinary neighborhood to the previous one is injective. The four
independent ambient sections extend through every order, proving the
all-order claim without a splitting of any structure sheaf.

For Theorem 3.1, the relevant homogeneous ideal of the fixed first
neighborhood is the **saturated** ideal
\(K=H^0_*(\mathcal I_C^2)\). This distinction matters: it is not
necessary to assert that the ordinary square of the homogeneous curve
ideal is already saturated. Invariance of \(C\) implies invariance of
\(K\), so it equals its own full weight initial ideal. Thus
\[
J\subset K\quad\Longrightarrow\quad
\operatorname{in}_{\pm w}J\subset K\quad\Longrightarrow\quad
(\operatorname{in}_{\pm w}J)^{\mathrm{sat}}\subset K.
\]
The last implication uses saturation of \(K\). This proves containment
of the actual projective \(X\) in both limits, including limits with
additional initial generators or irrelevant-vertex torsion.

The first neighborhood is locally Cohen–Macaulay: locally its ring is
the regular ambient ring modulo \((x,y)^2\), and a parameter along
the smooth support is a nonzerodivisor. Equivalently its filtration has
the torsion-free curve sheaves \(\mathcal O_C\) and \(E\) as layers;
this filtration argument requires no curve-algebra splitting. The image
of the finite-support ideal \(T\subset\mathcal O_Z\) in
\(\mathcal O_X\) must vanish. Hence the quotient map to \(X\)
factors through the pure hull and gives
\(X\subset\overline Z\subset Z\).

Restriction from any \(W\) containing \(X\) carries
\(\delta_W(e)\) to the independently established nonzero
\(\delta_X(e)\). This proves all three nonvanishings in (5).
For a global defining pair, generic vanishing of both first normal
symbols suffices: those symbols are global sections of vector bundles
on the integral curve, so generic zero implies identically zero.
No new assertion is obtained for pairs with nonzero first normal image.

## 3. Quadric multiples and the higher-twist failure of ACM

The smooth quadric \(Q=(x_0x_3-x_1x_2)\) contains \(C\) as a smooth
Cartier divisor of class \((1,3)\), after choosing ruling labels.
For every \(n\ge2\), its divisor multiple \(W_n=nC\) is locally
cut out by the regular sequence \((q,f^n)\) in \(\mathbf P^3\).
It has generic multiplicity \(n\), sole support \(C\), and is
locally Gorenstein. Invariance follows from invariance of the marked
quadric and divisor, not just of the underlying point set.

At twist one, both entries of \((1-n,1-3n)\) are negative. Künneth
therefore gives \(H^0=H^1=0\) for this line bundle on \(Q\), including
the boundary case \(n=2\), where one entry is \(-1\). The restriction
sequence makes the four ambient sections all the sections of \(L|_{W_n}\).
Their restrictions to \(C\) omit \(e\), proving (6).

The ideal-sheaf sequence at ambient twist \(d\) is exactly
\[
0\to\mathcal O_{\mathbf P^3}(d-2)\to\mathcal I_{W_n}(d)
\to\mathcal O_Q(d-n,d-3n)\to0.
\]
Vanishing of the two intermediate line-bundle cohomology groups on
\(\mathbf P^3\) identifies its first cohomology with that on \(Q\).
At \(d=n\), the latter is
\(H^0(\mathcal O_{\mathbf P^1})\otimes
H^1(\mathcal O_{\mathbf P^1}(-2n))\), of dimension \(2n-1\).
Thus the examples fail ACM in exactly the asserted way. They are not
examples satisfying \(\mathcal I_{W_n}\subset I^2\), since they
contain the first-order quadric equation; they correctly serve a
different control, showing that local Gorensteinness does not force
the missing coordinate to lift.

## 4. Findings and frontier disposition

**Material findings: none.** The normal-bundle formulas and projection
model are inherited inputs. Identifying the particular obstruction,
proving its persistence through full limits and pure hulls on the
entirely-thick branch, and recording the explicit all-multiplicity
quadric control are the applications checked here. The contextual
[multiple-structures paper](https://arxiv.org/abs/1211.5458) does not
supply a smoothing or closedness premise to these proofs.

Geometrically the omitted fifth coordinate already fails to extend over
the fixed first neighborhood, with obstruction in both balanced normal
directions. Every entirely-thick translate, both limits, and their pure
hulls contain that same neighborhood. Its obstruction therefore cannot
disappear there. This resolves the earlier speculative nonvanishing
question **on this branch**, in the direction compatible with a
hypothetical supported complete intersection. The quadric examples
separately show that a pure locally Gorenstein multiple structure may
have this same four-section behavior in every multiplicity.

The argument neither constructs two global STCI equations nor gives a
contradiction to their existence. It does not establish a relation
between higher-twist cohomology, opposite limits and the actual two
generators that would exclude them. No unrestricted conclusion, and
no conclusion for the nonzero-first-normal-image branch, is warranted.
