# 2. The simultaneous geometry of two surfaces

Let \(C=C_0=[s^4:s^3t:st^3:t^4]\) and let \(Y=V(F_a,G_b)\) be an
**actual proper** homogeneous intersection containing \(C\), over an
algebraically closed field. Write its fundamental cycle as
\[
[Y]=m[C]+R,\qquad \deg R=ab-4m.
\]
The effective residual cycle \(R\) has no \(C\)-component. The STCI question
asks whether \(R=0\) is possible in characteristic zero. Neither residual
support nor its absence is a premise for the general geometry below.

## 2.1 Generic length and common normal directions

At \(\eta_C\) the ambient local ring is regular of dimension two, with
residue field \(K=k(C)\). Complete it as \(K[[u,v]]\), retaining the choice
of coefficient field. The local ideal \(J=(F,G)\) is primary to \((u,v)\)
and
\[
m=\ell(K[[u,v]]/J).
\]
If \(r,s\) are the exact generic normal orders of the chosen equations,
then \(m\ge rs\), with equality precisely when their initial binary forms
have no common projective zero over \(\overline K\). This is about the
normal cone, not a common global surface factor. When the initial forms
share a factor, actual cancellation and successive transforms determine the
remaining length. For example \((u,u+v^N)=(u,v^N)\) has length \(N\)
although its displayed first symbols are unchanged as \(N\) varies.

The full initial **ideal** includes cancellation-generated equations; it
cannot be replaced by the ideal of the two displayed leading symbols. The
[filtration account](normal_filtration_boundary_obstructions.md) separates
that generic issue from a punctual failure of relations to extend along \(C\).

## 2.2 The common graph and its two contractions

In characteristic zero, set
\[
B=\operatorname{Bl}_C\mathbf P^3,\quad H=\pi^*\mathcal O(1),\quad
E=\pi^{-1}(C),\quad L=3H-E,\quad Q'=2H-E.
\]
The balanced normal bundle makes \(E\cong\mathbf P^1\times\mathbf P^1\).
The cubics through \(C\) give the other contraction
\(\phi:B=\operatorname{Bl}_\Gamma V_5\to V_5\), with exceptional \(Q'\)
over a smooth conic. The [two-blowup proof](blowup_residual_geometry.md)
contains the actual section dictionary, the anticanonical image
\(\Sigma=\phi(E)\), its normalization and conductor, and both projection
maps. In particular, for \(a\ge3r\),
\[
H^0(\mathbf P^3,I_C^r(a))
=H^0(V_5,I_\Gamma^{a-3r}(a-2r)).
\]
These are sheaf-power section spaces with actual constant coefficients,
not arbitrary function-field symbols.

The strict surfaces have classes \(aH-rE,bH-sE\) and intersect properly
in a curve \(W\). Its actual cycle satisfies
\[
\pi_*[W]=(m-rs)[C]+R.
\]
The coefficient \(m-rs\) follows from the local plane-germ blowup formula,
including residue degrees; equality of Chow classes alone would not prove
this cycle assertion. Horizontal curves in \(E\) record generic remaining
contact. Vertical curves map to points. Curves outside \(E\) are the actual
residual transforms, so
\[
R=0\quad\Longleftrightarrow\quad\operatorname{Supp}W\subset E.
\]
The weaker condition \(\phi(W)\subset\Sigma\) is insufficient:
\(\phi^{-1}(\Sigma)=E\cup Q'\), and trisecant residual lines in \(Q'\)
contract to points under \(\phi\). An exceptional curve is not automatically
an additional component downstairs.

## 2.3 Numerical capacity and its precise meaning

Put \(\delta=\deg R\) and
\[
K=16(as+br)-7ab-28rs.
\]
The effective exceptional cycle and nef \(L\) give \(5\delta\ge K\).
If no residual component lies on the containing quadric, the stronger
\(\delta\ge K\) holds. [Exact slack and equality proofs](blowup_residual_geometry.md#supporting-nef-bounds-exact-slack-and-equality-controls)
identify the role of trisecant rulings, the complete nef cone of this graph,
and the improvement obtainable only after supplying an actual lower bound
on horizontal root slope. No normality or integral-carrier assumption is
needed for these graph inequalities.

At a hypothetical supported endpoint, \(m=ab/4\), so \(4\mid ab\) and
\(K\le0\). Neither equation may contain the smooth quadric: restricting
its mate there would require a divisor of type \((b,b)\) supported on the
unbalanced \((1,3)\) curve. Restricting each equation with exact normal
order to that quadric therefore gives \(a\ge3r,b\ge3s\). These are
necessary conditions, not exhaustion of higher-degree pairs.

There is a uniform geometric consequence of \(K\le0\):
\[
\frac{m-rs}{m}\ge\frac{16\sqrt{15}-30}{49}>0.6524.
\]
The [derivation](blowup_residual_geometry.md#uniform-remaining-contact-after-the-first-blowup)
uses AM–GM and the local length inequality. Thus any supported pair must
retain over 65.2 percent of its generic length after the first blowup.
This is remaining generic contact, not residual degree or a contradiction.
The [generic contact-depth theorem](generic_contact_depth.md) gives a
different, power-invariant necessary condition with a quantitative tail;
its local examples explain why depth alone cannot prove nonexistence.

## 2.4 Three residual operations and three attachment quantities

Remove the **full** \(C\)-primary component \(T\) to obtain a linked
residual \(Z\) with cycle \(R\). By contrast the once-link \(Y:C\) has
cycle \((m-1)[C]+R\) and fixed degree \(ab-4\). It is flat through proper
CI multiplicity jumps; full-primary extraction need not be flat. The
[reverse-linkage proof](residual_liaison.md) recovers the defining equations
from the once-linked embedded curve and identifies the correct deformation
space.

The [full-primary equation module](residual_capacity_and_constructions.md)
gives the exact marked attachment divisor
\[
C\cap Z=\operatorname{div}(\operatorname{tors}E_T)+
\operatorname{div}(\det\bar\rho).
\]
The non-lci example there has a unit determinant but marked attachment
length two, all in torsion; full thick attachment has length six. Neither
may be substituted for the valuative branch-contact cycle. The general
scheme-theoretic estimate is
\(\ell(C\cap Z)\le3\deg R\), improved to coefficient two when the
quadric avoids residual components. Its sharp actual quadric family shows
why full attachment cannot replace marked attachment.

On an integral carrier, the [normalization capacity proof](normalization_residual_capacity.md)
uses the nef bundle from principalizing \(I_C\) to bound the actual valuation
vector. It includes normal, nonnormal singleton and multibranch cases,
positive-denominator checks and integer improvements. A zero Hodge gap is
left open, rather than treated as a construction. [Prescribed A-type
carriers](prescribed_singular_carriers.md) realize arbitrary local indices
and smooth class-cancelling residuals, demonstrating the separate local
class and global divisor-relation requirements.

## 2.5 Actual sources, finite jets, and formal visibility

A [general pair in every degree \(a,b\ge4\)](residual_global_models.md)
has a smooth integral residual of degree \(ab-4\), genus
\((a+b-4)(ab-8)/2\), and \(4(a+b)-14\) transverse marked attachments.
The attachment morphism is dominant. In the sufficient range \(a,b\ge7\),
**every** effective attachment divisor of that degree, including all contact
at one point, is realized by smooth integral residual geometry. These
constructions keep generic multiplicity one and do not absorb the residual.
The full proofs retain the actual homogeneous source and compatible-jet
lifting thresholds.

At fixed degrees there is an exact [finite normal-jet certificate](finite_normal_jets.md),
valid even for singular integral curves and with a weighted reducible
extension. It does not supply a bound on possible witness degrees.
[R-0025](../results/ci_fixed_sextic_jet_rigidity.md) is a concrete actual-source
kernel calculation for one sextic and degree-sixteen mates, giving
\(m\le22\) and \(\deg R\ge8\). Its proof retains the 23-dimensional
normal quotient, 969 constant-coefficient source, 286 multiples and good
specialization rank bridge; no statement about other sextics follows.

The [full formal criterion](formal_residual_visibility.md) distinguishes a
generic normal algebra from the completed embedded ideal and from two
fixed-twist formal equations. Globally glued all-order sections with uniform
power containment already algebraize by projective-space G3/Lefschetz;
arbitrary local formal generators or finite jets do not provide those data.
The point-multiplicity detector recognizes actual residual support, but
there is no theorem forcing its positivity for every characteristic-zero
pair.

The [explicit quartic laboratories](residual_intersections_and_jets.md)
illustrate the mechanisms without purporting to classify containing pairs.
Next: [jets and root schemes](03-infinitesimal-geometry.md).
