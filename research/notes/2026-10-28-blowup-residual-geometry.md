# Two projections of containing intersections: a fixed nonnormal surface on V5

Date: 2026-10-28. Author: `blowup_linear_systems` research agent.
Status: **independently reviewed provisional deductions** in the
[separate audit](2026-10-28-blowup-residual-audit.md). No canonical
record is promoted. The cubic birational model is inherited, not a new
discovery; the all-degree section dictionary, fixed anticanonical image of the
exceptional divisor, and residual bookkeeping are the contribution of this
pass. No literature novelty is claimed.

## 1. Question, hypotheses, and prior evidence

Work over an algebraically closed field of characteristic zero, with

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\quad q=x_0x_3-x_1x_2,
\quad B=\operatorname{Bl}_C\mathbf P^3.
\]

The question is what proper intersections containing this **fixed embedded**
curve look like, including their actual residual components. A set-theoretic
complete intersection is one possible endpoint. It is not a premise.

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), and the contribution
checklist. The inherited inputs used here are:

- [R-0020](../results/quartic_conormal_characteristic_jump.md):
  \(N_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(7)^2\).
- [The October 21 cubic-image note, §§1–2](2026-10-21-conditional-2-12-cubic-image-and-conductor-interface.md)
  and [its independent review, §1](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md):
  the seven cubics below map \(B\) to a smooth quintic del Pezzo threefold
  \(V\subset\mathbf P^6\), and identify \(B\) with the blowup of a smooth conic
  \(\Gamma\subset V\). The five equations, smoothness certificate, graph proof,
  and section-ring resolution were already checked there and were not rerun.
  Those general geometric statements do not require the conditional
  \((6,16)\) pair discussed later in the source note. They remain reviewed
  provisional evidence, rather than a promoted result record.
- [The October 27 general-pair note, §2](2026-10-27-global-containing-intersections.md)
  and its audit: a general pair of degrees \(a,b\ge4\) gives
  \(C\cup D\), with smooth integral residual \(D\), degree \(ab-4\),
  genus \((a+b-4)(ab-8)/2\), and \(4(a+b)-14\) simple attachments.

A targeted repository search located the cubic model before any new
calculation. The independent primary literature check also found precisely
this quartic and the two blowups in
[Cheltsov–Przyjalkowski–Shramov, *Fano threefolds with infinite automorphism groups*, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).
Thus the birational model belongs to established Fano geometry. Its use here
is to reorganize a residual-construction question, not to claim a new model.

Write

\[
H=\pi^*\mathcal O_{\mathbf P^3}(1),\quad E=\pi^{-1}(C),
\quad L=3H-E,\quad Q'=2H-E.
\]

The other projection is
\(\phi:B=\operatorname{Bl}_\Gamma V\to V\), with
\(L=\phi^*M\), \(M=\mathcal O_V(1)\), and exceptional divisor \(Q'\).
Its fibers on \(Q'\cong\mathbf P^1\times\mathbf P^1\) are the trisecant
ruling lines of the original quadric \(Q=V(q)\). The useful change of basis is

\[
\boxed{H=L-Q',\qquad E=2L-3Q'.}\tag{1}
\]

## 2. Actual equation spaces become sections with prescribed conic vanishing

Here and below \(I_C^r\) and \(I_\Gamma^e\) are **ideal sheaf powers**.
Their global sections are not being identified silently with an unsaturated
homogeneous ideal power.

**Section dictionary.** For integers \(r\ge0\) and \(a\ge3r\), there is a
natural vector-space identification

\[
\boxed{
H^0(\mathbf P^3,I_C^r(a))
\cong H^0\bigl(V,I_\Gamma^{\,a-3r}(a-2r)\bigr).
}\tag{2}
\]

Indeed the left side is \(H^0(B,aH-rE)\). By (1),

\[
aH-rE=(a-2r)L-(a-3r)Q'.
\]

For the blowup of a smooth codimension-two center,
\(\phi_*\mathcal O_B(-eQ')=I_\Gamma^e\) for \(e\ge0\).
This follows directly on a regular-parameter chart from the Rees algebra;
the same fact for \(\pi\) gave the first equality. The projection formula
proves (2). See also the primary [Stacks blowup construction](https://stacks.math.columbia.edu/tag/01OF).

This correspondence retains actual global constant coefficients. It is not
merely a correspondence between symbols over \(k(C)\).

For completeness the other region has a simple interpretation. If
\(2r\le a\le3r\), put \(k=a-2r\), \(j=3r-a\). Then

\[
H^0(\mathbf P^3,I_C^r(a))\cong H^0(V,\mathcal O_V(k)),
\quad aH-rE=kL+jQ'.\tag{3}
\]

Here \(\phi_*\mathcal O_B(jQ')=\mathcal O_V\): a rational function allowed
to have poles only above a codimension-two subset extends on normal \(V\).
Every section has the fixed factor \(q^j\) downstairs. If \(a<2r\), the
space is zero, since the same calculation leaves a negative multiple of
the ample class \(M\). For example, the familiar spaces of order-two forms
in degrees four, five and six become respectively constants times \(q^2\),
\(q\) times the seven cubics, and all quadric sections of \(V\). These are
checks of the dictionary, not new claims about those previously computed
spaces.

There is an explicit polynomial construction behind (2). Let

\[
(c_0,\ldots,c_6)=(qx_0,qx_1,qx_2,qx_3,
x_0^2x_2-x_1^3,x_0x_2^2-x_1^2x_3,x_2^3-x_1x_3^2).
\]

Take a section \(P\in H^0(V,I_\Gamma^e(k))\). Projective normality of the
inherited cubic model represents it by a degree-\(k\) polynomial in the
\(y_i\). Then

\[
F(x)=\frac{P(c_0(x),\ldots,c_6(x))}{q(x)^e}\tag{4}
\]

is a polynomial of degree \(a=3k-2e\), vanishing to order at least
\(r=k-e\) on \(C\), when \(k\ge e\ge0\). Divisibility by \(q^e\) can be
checked at the generic point of \(Q\), where \(\phi\)'s transverse order to
\(\Gamma\) is the \(q\)-order; polynomial unique factorization then gives
global divisibility. Formula (2) supplies the coordinate-free justification.
No claim about a chosen nonsaturated ideal presentation of
\(I_\Gamma^e(k)\) is required.

If \(P\) has exact generic order \(e\) on \(\Gamma\), then \(F\) has no
quadric factor. If its divisor does not contain the surface \(\Sigma\) of
§3, then \(F\) has exact order \(r\) on \(C\). Conversely, a form of exact
order \(r\) with no quadric factor gives exactly these conditions. Thus this
is an equation-construction dictionary with explicit order checks.

## 3. The original exceptional divisor has a fixed anticanonical image

The image of \(E\), which was not identified in the retrieved source notes,
is particularly useful. Set

\[
\Sigma=V\cap V(y_0y_3-y_1y_2)\subset\mathbf P^6.
\]

**Provisional proposition.** \(\Sigma\) is an integral nonnormal
anticanonical surface on \(V\). Its normalization is the finite birational
map

\[
\nu=\phi|_E:E\cong\mathbf P^1\times\mathbf P^1\longrightarrow\Sigma.
\]

Put \(B_0=E\cap Q'\), to distinguish this curve from the threefold \(B\).
Then

\[
\boxed{\phi^*\Sigma=E+3Q',\quad B_0\sim(1,1)\text{ on }E,
\quad I_{\mathrm{cond},E}=\mathcal O_E(-2B_0).}\tag{5}
\]

The map \(B_0\to\Gamma\) has degree three and, in the displayed coordinates,
is \([s:t]\mapsto[s^3:t^3]\) followed by the conic embedding. In particular
its two totally ramified values retain the marked endpoint geometry of \(C\).

**Proof.** Substitution of the seven cubics gives the literal identity

\[
c_0c_3-c_1c_2=q^3.
\]

The divisor of this section of \(2L=6H-2E\) on the blowup is
\(3Q'+E\). The nonexceptional component is \(E\), with coefficient one;
hence its image is precisely the integral reduced quadratic section
\(\Sigma\), and the equality in (5) is scheme-theoretic at the divisor
level. Since \(K_V=-2M\), adjunction gives \(\omega_\Sigma=\mathcal O_\Sigma\).
The morphism \(\phi\) is an isomorphism off \(Q'\), so \(\Sigma\) is smooth
off \(\Gamma\).

No contracted ruling of \(Q'\) lies in \(E\): its intersection with \(E\)
is its length-three intersection with \(C\) on \(Q\). Thus \(\phi|_E\) has
finite fibers and is finite, as it is proper. It is birational, since it is
an isomorphism outside \(B_0\). Smooth \(E\) is therefore the normalization.

Use the product coordinates on \(E\) given by R-0020 and the lines convention
for \(\mathbf P(N_C)\). Then

\[
H|_E=\mathcal O(4,0),\quad E|_E=\mathcal O(7,-1),
\quad L|_E=\mathcal O(5,1),\quad Q'|_E=\mathcal O(1,1).
\]

The curve \(B_0\) is the section of the normal projective bundle supplied by
the smooth quadric, so is smooth and isomorphic to \(C\). On \(Q'\), take
coordinates with
\(x_0=ua,x_1=ub,x_2=va,x_3=vb\). Then \(C\) has equation
\(va^3-ub^3=0\), and the last three cubic coordinates restrict, after
removing this equation, to \([u^2:uv:v^2]\). This proves the degree-three
map and its endpoint assertion.

Finally finite duality for the normalization of a Gorenstein surface gives

\[
\nu_*\omega_E=
\mathcal Hom_\Sigma(\nu_*\mathcal O_E,\omega_\Sigma),
\]

which, with \(\omega_\Sigma=\mathcal O_\Sigma\), identifies the conductor
ideal on \(E\) with \(\omega_E\cong\mathcal O_E(-2,-2)\). Its support is
contained in the single smooth irreducible curve \(B_0\); an invertible
ideal with this support is \(\mathcal O_E(-dB_0)\). Comparison of classes
forces \(d=2\), proving the full ideal assertion in (5), including the
absence of an additional punctual correction. The finite-duality formula
is the same standard input already independently reconstructed in the
[October 21 review, §2](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md);
see also [Stacks, finite morphisms](https://stacks.math.columbia.edu/tag/0FKW).

At a general point of \(\Gamma\), the three preimages in \(B_0\) are
distinct. The transverse curve singularity of \(\Sigma\) is therefore an
ordinary triple point; \(2B_0\) is the expected conductor on its three
branches. No assertion of this transverse type is made at the ramified
endpoint values.

This produces an actual, explicitly marked nonnormal anticanonical surface
associated to the quartic. It is not a containing surface in the original
\(\mathbf P^3\), and no fixed-carrier STCI result is transported to it.

## 4. Residual curves and the two different ways a curve can disappear

Let \(F_a,G_b\) be an actual proper pair with exact generic normal orders
\(r,s\) along \(C\), and write

\[
[V(F,G)]=m[C]+R.
\]

On \(B\) their strict transforms have classes
\(A=aH-rE\), \(A'=bH-sE\) and have no common surface component. Their
scheme intersection \(W\) is a proper complete-intersection curve. There is
an identity of actual cycles, stronger than an equality of Chow classes:

\[
\boxed{\pi_*[W]=(m-rs)[C]+R.}\tag{6}
\]

Off \(C\), the actual residual cycles agree because \(\pi\) is an
isomorphism. At \(\eta_C\), work in the two-dimensional regular local ring
\(\mathcal O_{\mathbf P^3,\eta_C}\). Its blowup at the maximal ideal has
exceptional \(\mathbf P^1_{k(C)}\). The local blowup intersection formula is

\[
i_{\eta_C}(F,G)
=rs+\sum_{z\in\mathbf P^1_{k(C)}}
[\kappa(z):k(C)]\,i_z(F',G').
\]

This formula follows by separating the exceptional orders \(r,s\) in the
intersection of two plane germs; the exceptional contribution is their
product and the remaining local intersections are those of their strict
transforms. The weighted sum is exactly the coefficient of \(C\) in
\(\pi_*[W]\), proving (6) coefficient by coefficient. The projection formula
and \(\pi_*(E^2)=-[C]\) give a separate check of its Chow class; that check
alone would not prove the actual-cycle assertion.

The components of \(W\) outside \(E\) are precisely the strict transforms
of actual residual components. Components contained in \(E\) can dominate
\(C\) or map to isolated points. Consequently

\[
\boxed{R=0\quad\Longleftrightarrow\quad\operatorname{Supp}W\subset E.}\tag{7}
\]

For (7), use that \(\pi\) is an isomorphism off \(E\) and \(W\) is pure
one-dimensional. This criterion concerns the actual strict-transform
intersection, not the common zeros of two leading symbols alone.

The second projection gives complementary visibility:

| Curve on the graph \(B\) | Image in \(\mathbf P^3\) | Image in \(V\) |
|---|---|---|
| A fiber of \(E\to C\) | A point | A line in \(\Sigma\) |
| A ruling fiber of \(Q'\to\Gamma\) | An actual trisecant line | A point of \(\Gamma\) |
| A curve in \(E\) dominating \(C\) | Thickness along \(C\) | A curve in \(\Sigma\) |
| A curve outside \(E\cup Q'\) | Residual curve | Its birational transform |

Thus even an actual curve in \(\Sigma\) need not be a residual curve in the
original space; conversely an actual residual trisecant can vanish to a point
on \(V\). The weaker condition \(\phi(W)\subset\Sigma\) does **not** replace
(7), since \(\phi^{-1}(\Sigma)=E\cup Q'\). Retain the graph and both
projections whenever residual support matters.

The numerical record of the two polarizations, useful without any generic
coprime-symbol assumption, is

\[
\begin{aligned}
H\cdot W&=ab-4rs,\\
E\cdot W&=4(as+br)-14rs,\\
L\cdot W&=3ab-4(as+br)+2rs,\\
Q'\cdot W&=2ab-4(as+br)+6rs.
\end{aligned}\tag{8}
\]

These follow from \(H^3=1,H^2E=0,HE^2=-4,E^3=-14\).
An intersection number with \(E\) or \(Q'\) is not a point count if \(W\)
has a component in that divisor. Nor does its sign by itself assert a
residual component downstairs.

## 5. General residuals acquire a second constructive description

For a general \((a,b)\) pair, \(a,b\ge4\), use the inherited multiplicity-one
theorem of §1. Then \(W\cong D\) and \(r=s=1\). The corresponding divisors
\(T_a,T_b\) on \(V\) have

\[
T_a\in |(a-2)M|,\quad\operatorname{ord}_\Gamma T_a=a-3,
\qquad
T_b\in |(b-2)M|,\quad\operatorname{ord}_\Gamma T_b=b-3.
\]

Their intersection has a conic-primary component of generic multiplicity
\((a-3)(b-3)\), and residual image \(D'=\phi(W)\) of degree

\[
\boxed{\deg_M D'=3ab-4a-4b+2.}\tag{9}
\]

The multiplicity is the product because the general normal forms along
\(\Gamma\) have no common projective root at its generic point. Equivalently,
subtract (9) from the total \(M\)-degree \(5(a-2)(b-2)\) and divide by the
conic degree two. The general transformed residual is smooth, and isomorphic
to \(D\), for the following reason. On \(Q'\cong Q\), restrictions of the
two strict equations are general sections of
\(\mathcal O_Q(a-1,a-3)\) and \(\mathcal O_Q(b-1,b-3)\); restriction is
surjective by the quadric sequence. Their common zeros are transverse and
finite. No two lie in the same contracted ruling for a general pair: at two
chosen distinct points of one ruling each equation imposes two independent
linear conditions, while the ruling and its two points vary in dimension
three. The four conditions exceed this dimension. At a transverse meeting
with \(Q'\), the blowdown restricted to \(W\) is an immersion in the standard
two-parameter blowup chart. These two facts exclude both identifications and
ramification. Hence \(\phi|_W\) is a closed immersion.

The reduced conic attachment divisor has length

\[
\operatorname{length}(D'\cap\Gamma)
=Q'\cdot W=2ab-4a-4b+6.\tag{10}
\]

This is attachment to **reduced** \(\Gamma\); it is not the attachment length
to the full conic-primary component when \((a-3)(b-3)>1\).

| Original bidegree | \(\deg D\) in \(\mathbf P^3\) | \(\deg_M D'\) on \(V\) | Generic conic multiplicity | Reduced conic attachments |
|---|---:|---:|---:|---:|
| \((4,4)\) | 12 | 18 | 1 | 6 |
| \((5,5)\) | 21 | 37 | 4 | 16 |
| \((5,6)\) | 26 | 48 | 6 | 22 |
| \((6,6)\) | 32 | 62 | 9 | 30 |

These are examples of one formula, not a proposed degree-by-degree agenda.
They show that the same smooth residual curve can be interpreted either as
linked to the quartic in \(\mathbf P^3\), or as linked to a multiple conic on
the quintic del Pezzo threefold. The full primary schemes and attachment
budgets in these two presentations differ.

## 6. Constructive consequence and exact remaining task

The useful new search space is now explicit: take actual sections of
\(I_\Gamma^e(k)\) on the fixed smooth \(V\), recover equations by (4), and
retain the intersection on the graph. General choices produce residual
curves. Deliberate choices can impose components, special attachments, or
additional contact with the fixed surface \(\Sigma\). These conditions can
be expressed with the five known quadrics of \(V\) and the one fixed
quadratic equation of \(\Sigma\), rather than with only a prospective
generic initial algebra along \(C\).

The next bounded experiment is to construct a family of two sections on
\(V\) in this dictionary for which part of the graph residual crosses into
\(E\), and track the actual common ideal, \(E\)-components, and
\(Q'\)-rulings throughout. The invariant question is which residual curves
can occur and move in this presentation, with attachment and conductor data
retained. Complete absorption would require (7), not merely an intersection
image in \(\Sigma\). No such complete-absorption pair is constructed here.

The connection to Fano birational geometry and anticanonical normalization
gives a second global vocabulary for the construction problem. It does not
make all section spaces freely generated, commute primary extraction with
specialization, or settle the characteristic-zero STCI question.

## Review and verification boundary

The independent audit reconstructs (2)–(10), especially the full conductor
ideal in (5), the exact-support criterion (7), and the general-pair
blowdown/attachment assertion in §5. It required one proof repair: the
actual-cycle equality (6) uses the generic local blowup formula, whereas a
Chow-class calculation alone would not establish it. The inherited cubic-image verifier and
accepted normal-bundle calculation were not rerun. The polynomial identity
\(c_0c_3-c_1c_2=q^3\) and all displayed intersection formulas are literal
algebra, not a finite sample or a substitute for a global existence proof.
Independent review must check the powers are sheaf powers, the two
exceptional divisors are not interchanged, and the \(\Sigma\) condition is
not mistaken for a criterion for residual support without the graph.
