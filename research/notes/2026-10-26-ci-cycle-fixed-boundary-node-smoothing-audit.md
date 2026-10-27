# Independent final audit of node smoothing at fixed boundary

Date: 2026-10-26. Reviewer: independent cycle-notebook audit agent.
Status: exact tangent calculation and local deformation interpretation
reviewed; no canonical promotion.

This finishes review of the existing
[fixed-boundary node-smoothing calculation](2026-10-25-ci-cycle-fixed-boundary-node-smoothing.md).
The underlying line-plus-degree-eleven curve has its separate
[geometric audit](2026-10-25-ci-cycle-line-degeneration-audit.md).
No new investigation is started here.

**Outcome.** The ranks \(19,5,24\) are correct for the actual global quartic
source. The fixed-boundary fiber is locally smooth of dimension fourteen,
and its five residual node parameters have independent differentials.
After splitting and labelling the geometric nodes, its complete local ring
can be written \(k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]]\), with the
attachment divisor on the marked \(C\) exactly fixed. This is a local formal
existence statement, with the local algebraic interpretation in section 4;
it is not a displayed polynomial path or an all-pairs result.

## 1. Independent reconstruction from the global source

The reviewer rebuilt the calculation in a separate standard-library Python
program. It enumerates the thirty-five degree-four monomials, groups them
by \(w=m_1+3m_2+4m_3\), and uses the **last** monomial in each group as its
reference, rather than the verifier's first. The resulting eighteen
differences form another basis of the actual global kernel
\(H^0(I_C(4))\). All coefficients remain rational constants.

For a monomial difference of common weight \(w\), the first-normal
coefficients in \(X=x_3-u^4,Y=x_2-u^3\) are
\[
(m_3-m'_3)u^{w-4},\qquad
(m_2-m'_2)u^{w-3}.
\]
The base-pair symbols were reconstructed directly from the actual
\((a,b)=(1,1)\) forms:
\[
\sigma_f=(h_0-1)X+(-uh_0-1)Y,
\]
\[
\sigma_g=(h_1-3u^8-2u^9)X+
               (4u^9+3u^{10}-uh_1)Y,
\]
where \(h_0,h_1\) are the restrictions of the documented quadrics.
The affine boundary derivative is
\[
D(h,k)=\det(\sigma_h,\sigma_g)+\det(\sigma_f,\sigma_k).
\]
Every one of these thirty-six polynomial directions has degree at most
eighteen **before** extraction of its nineteen coefficients. Thus the matrix
representation does not silently discard a higher coefficient.

On the line \([-r:r:-1:1]\), the same global monomial restricts to
\((-1)^{m_0+m_2}r^{m_0+m_1}\). Reduction modulo
\[
P=4r^5-2r^4+9r^3+2r^2+3r+2
\]
gives the five-dimensional rational node algebra. Squarefreeness is sufficient;
the calculation does not need to assume this algebra is a field or to choose
five rational roots.

Using the independently reconstructed first symbols and a different echelon
elimination gives
\[
\operatorname{rank}D=19,\qquad
\operatorname{rank}S=5,\qquad
\operatorname{rank}(D,S)=24.
\]
The independent output also records highest boundary degree eighteen.
The durable
[verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py)
was read and replayed, and its five explicit rational tangent witnesses were
checked against the combined matrix. Its
[JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json)
preserves their thirty-six source coefficients and exact images.
The separate
[independent reconstruction audit](2026-10-25-ci-cycle-fixed-boundary-node-smoothing-audit.md)
records another reconstruction and the same quotient calculation.

## 2. Why the five-dimensional functional is the node map

The two relevant normal derivatives along the line are
\[
F_1=-r(r+1)(r+2),\qquad G_1=-4r^3+2r^2-9r-1.
\]
\(F_1\) is a unit modulo \(P\). At each node the complete gradient rows
are proportional with ratio \(G_1/F_1\). Eliminating the smooth first
carrier equation therefore gives the first-order smoothing constant
\[
k|_L-(G_1/F_1)h|_L.
\]
Multiplication by the unit \(F_1\) gives exactly
\[
S(h,k)=F_1k|_L-G_1h|_L\pmod P.
\]
This proves that the five-dimensional output is the direct sum of the five
geometric \(T^1\) directions, with harmless invertible scalings after base
extension. It is not merely a chosen list of polynomial evaluations.

The combined rank implies
\[
\operatorname{rank}(S|_{\ker D})=24-19=5.
\]
The displayed tangent witnesses satisfy \(D=0\) exactly and span that output.
Selecting just one labelled geometric node can require a splitting field;
surjectivity over the rational étale algebra is the appropriate rational
statement.

## 3. The Grassmannian quotient does not change the conclusion

The ordered source has dimension thirty-six. Its four-dimensional
infinitesimal change-of-basis space consists of
\[
(\alpha f+\beta g,\gamma f+\delta g).
\]
Every such direction has \(S=0\), since \(f\) and \(g\) vanish at each node.
Its boundary derivative is
\((\alpha+\delta)\Delta\), where \(\Delta\ne0\) is the base determinant.
Thus the trace part accounts for the scalar determinant direction.

Let \(D^{-1}(k\Delta)\) be the tangent space preserving the *projective*
boundary. It has dimension \(36-19+1=18\). Quotient by the four-dimensional
basis-change space gives the fourteen-dimensional tangent space to the
boundary fiber in \(\operatorname{Gr}(2,18)\).
Any member of \(D^{-1}(k\Delta)\) can be adjusted by a trace direction to lie
in \(\ker D\), without changing \(S\). The node output is therefore still
surjective on the Grassmannian fiber. Its common tangent kernel has dimension
\(14-5=9\).

This explicitly checks the distinction between zero affine derivative and
zero projective boundary derivative. Neither an extra node direction nor a
lost node direction comes from scaling the two equations.

## 4. The formal conclusion and its additional hypotheses

The proper-pencil parameter space is smooth of dimension thirty-two.
Surjective \(d\beta\) makes its boundary fiber smooth locally at the checked
point, of dimension fourteen. Work over an algebraically closed
characteristic-zero field, or first extend to split and label the five nodes.

The proper flat residual family required for the local node description
can be obtained on \(\operatorname{Bl}_C\mathbf P^3\): the two strict-transform
divisors of class \(4H-\mathcal E\) meet properly, and their relative regular
sequence is flat near the checked member. At the eighteen simple attachments
to \(C\), the residual blowdown is an isomorphism; these conditions remain
open. This is the family bridge reviewed in the line-degeneration audit,
not an inference from matrix rank alone.

For each split residual node the completed local family has equation
\(xy-\tau_i=0\). The relevant standard input is
[Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX), with the
[étale counterpart](https://stacks.math.columbia.edu/tag/0CBY).
The differential \(d\tau_i\) is the node functional above up to a unit.
Consequently the five \(d\tau_i\) on the fixed-boundary fiber are independent.
They can be extended to a regular system of formal parameters, giving
\[
\widehat{\mathcal O}_{\beta^{-1}(\beta_0),[f,g]}
\simeq k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].
\]

Hence one may prescribe the five node smoothing parameters independently in
this completed neighborhood while retaining the exact boundary value
\(\beta_0\). This uses regularity and the formal inverse-function argument,
in addition to the finite calculation. In particular the rank statement
does more than merely suggest possible independent smoothings.

The additional étale local algebraic interpretation in the contribution is
also valid. After one common étale base change supplying the five labelled
node charts, their parameters are regular functions. The map from the
fixed-boundary fiber to \(\mathbf A^5\) given by these parameters is smooth
near the marked point. Pulling back a pattern \(\tau_i=c_it\) gives a smooth
morphism over a neighborhood of zero on \(\mathbf A^1\). A smooth morphism
with the chosen rational point in its fiber admits a section after an
étale change of that base. This yields a local algebraic curve of pencils
with exactly fixed boundary and the prescribed smoothing pattern. It is
an existence deduction, not an explicit list of global quartic coefficients.

It does not mean that the first-order tangent witnesses themselves define
constant-boundary linear paths: the determinant has quadratic and higher
changes along \(f+th,g+tk\). Correcting higher coefficients or producing a
specific polynomial/rational path is an additional construction, expressly
not supplied by this result.

## 5. Final scope and completion

The local inference applies to the checked pencil and its marked boundary
fiber. It does not classify the entire fiber, determine all global topology
strata, or prove a residual component for every homogeneous pair. The
interpretation of partial smoothing by contraction of edges in the residual
dual graph is useful local geometry; an explicitly computed algebraic
subfamily remains a different deliverable.

The exact ranks, rational witnesses, quotient dimensions, and formal
fixed-boundary conclusion pass final independent review. No remaining defect
was found in the current calculation. No new experiment, commit, canonical
promotion, or push was undertaken by this reviewer.
