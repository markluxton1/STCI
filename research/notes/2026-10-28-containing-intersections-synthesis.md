# Intersections containing C: residual families and constructive global models

Date: 2026-10-28. Continued on
`codex/intersections-containing-quartic-2026-10-27`. Three complementary
research agents plus coordinator integration and separate independent
reviews. **New claims remain provisional and unpromoted.** No accepted
mathematics is rewritten and the unrestricted characteristic-zero STCI
question remains open.

The [quantitative follow-up on residual degree](2026-10-28-residual-degree-synthesis.md)
uses this construction picture to derive attachment-module and numerical
carrier-capacity lower bounds, alongside retrieved graph estimates and
their exact limitations. Its source proofs and audits retain genuine
residual, once-linked and full-primary distinctions.

## 1. The question we are organizing around

For the fixed smooth quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), what do proper
intersections of two hypersurfaces containing \(C\) look like, and how can
one construct hypersurfaces with a desired residual configuration?

Start with actual forms without a common surface factor. Retain

\[
Y=V(F_a,G_b),\qquad [Y]=m[C]+R,\qquad ab=4m+\deg R.
\]

Residual curves supply construction data: their embeddings, equations,
deformations, attachment and local divisor classes all matter. Sole support
is a possible endpoint. The broader geometry remains valuable regardless
of whether that endpoint exists.

The [October 27 vision](2026-10-27-containing-intersections-research-vision.md)
and [arbitrary-degree continuation](2026-10-27-arbitrary-degree-absorption-synthesis.md)
already provide general residual geometry, partial absorption, full-primary
attachment, formal lifting and characteristic comparison. This pass adds
construction tools and a more useful family to follow through a thickness
jump. It does not repeat those results or choose a compulsory bidegree.

## 2. What a general pair looks like

Without a prescribed curve, two general hypersurfaces meet in a smooth
integral complete-intersection curve of degree \(ab\) and genus
\(1+ab(a+b-4)/2\). Requiring both equations to contain the fixed
\(C\) changes this baseline: the general intersection in that constrained
parameter space separates into the marked component and an actual residual.

Over algebraically closed characteristic zero, a general pair of degrees
\(a,b\ge4\) gives \(Y=C\cup D\), with \(D\) smooth integral and

\[
\deg D=ab-4,\qquad
g(D)=\frac{(a+b-4)(ab-8)}2,\qquad
\operatorname{length}(C\cap D)=4(a+b)-14.
\]

The attachments are distinct transverse points for a general pair. These
are inherited [reviewed provisional general-pair deductions](2026-10-27-global-containing-intersections.md),
using classical liaison, adjunction and the previously audited blowup
embedding. For example the residual of two general quintics has degree
21 and genus 51, attached at 26 points. This substantial curve is part of
the starting geometry. The arithmetic genus of the whole intersection is
still the complete-intersection genus: \(p_a(Y)=g(D)+\operatorname{length}
(C\cap D)-1\). The residual's genus and its gluing to \(C\) together
account for it.

The word **general** must specify its parameter space:

| Parameter space | Typical geometry to study |
|---|---|
| All degree-\((a,b)\) forms through reduced \(C\) | Multiplicity one, smooth residual, simple attachments |
| Pairs through a fixed lower thickening of \(C\) | Forced lower thickness; remaining equation freedom and residual gluing |
| Carriers with prescribed isolated singularities on \(C\) | Local divisor classes compensated by residual curves |
| Carriers containing an ordinary power \(I_C^q\), \(q\ge2\) | Generically singular, nonnormal carrier geometry and conductor descent |

A conclusion for one row cannot automatically be used for another.

## 3. New positive freedom: prescribe the attachment, then choose equations

The [normal-jet and prescribed-attachment note](2026-10-28-prescribed-attachment-and-normal-jets.md)
and its [independent audit](2026-10-28-prescribed-attachment-audit.md) give
two constructive facts.

First, for ideal **sheaf** powers, over any field,

\[
H^1(I_C^r(d))=0\quad(d\ge3r-1),
\qquad h^1(I_C^r(3r-2))=2r-1.
\]

Thus compatible jets on \(V(I_C^N)\) lift to actual homogeneous forms
when \(d\ge3N-1\). Every first-normal section is available already
for \(d\ge5\). This makes finite jet design an actual construction
operation in the stated range. It does not assert fixed-degree all-order
compatibility or generation of a primary ideal by two sections.

Second, in characteristic zero, for **every** \(a,b\ge7\) and **every**
effective divisor \(A\) of degree \(4(a+b)-14\) on the marked \(C\),
there is an actual pair of smooth integral surfaces with
\(Y=C\cup D\), \(D\) smooth integral, and \(C\cap D=A\) exactly.
Seven is a sufficient uniform threshold, not a preferred degree.

This includes putting all attachment at one point. In degree \((7,7)\),
one can have a smooth degree-45 genus-205 residual meeting \(C\) in a
single length-42 scheme while the generic multiplicity on \(C\) remains
one. This is a proved existence construction, not a displayed rational
coefficient list. It shows that contact concentration can be made extreme
without transferring any residual degree into generic thickness.

## 4. The residual can recover the hypersurfaces

The [liaison note](2026-10-28-residual-liaison-construction.md) and
[independent review](2026-10-28-residual-liaison-audit.md) distinguish two
residual constructions:

\[
D_1=V((F,G):I_C),\qquad
[D_1]=(m-1)[C]+R;
\]

and the genuine residual \(R\) obtained after removing the **full**
\(C\)-primary component \(T\). At multiplicity one they agree; after a
jump \(D_1\) can contain \(C\).

For \(a,b\ge4\), the low equation spaces satisfy

\[
(I_{D_1})_n=(F,G)_n\quad(n\le a+b-4).
\]

Thus the embedded \(D_1\) uniquely recovers the complete intersection,
and linkage recovers its marked quartic partner. This is a genuine
construction coordinate system, beyond numerical degree/genus matching.
The source gives its all-degree minimal resolution. Applying Kleppe's
existing diameter-one deformation theorem shows these once-linked curves
are unobstructed in their Hilbert scheme; the incidence preserving the
low equations must still be retained. A quintic carrier gives an explicit
direction in which a Hilbert deformation can lose a required equation.

More usefully for absorption, \(D_1\) is flat in a family of proper pairs
with the fixed reduced \(C\), even when its supported part increases.
Relative linkage and its exact canonical-module sequence supply the
base-change statement. Its Hilbert polynomial stays fixed, whereas full
primary extraction can jump. This reconciles residual deformation with
the earlier warning that a flat family of *full* primary components cannot
change its generic length.

The appropriate construction problem is therefore a flag of an embedded
once-linked curve, its recovered pair, and the **fixed embedded** partner.
Arbitrary Hilbert deformations of a residual curve can move the partner
or lose the equations. Only the corresponding incidence directions answer
the original question.

## 5. A second global model connects to Fano geometry

The [blowup note](2026-10-28-blowup-residual-geometry.md) and
[independent audit](2026-10-28-blowup-residual-audit.md) use the already
known diagram

\[
\mathbf P^3\ \xleftarrow{\ \pi\ }\
B=\operatorname{Bl}_C\mathbf P^3
=\operatorname{Bl}_\Gamma V_5
\ \xrightarrow{\ \phi\ }\ V_5,
\]

where \(V_5\) is a smooth quintic del Pezzo threefold and \(\Gamma\) a
smooth conic. This model was already in the repository and primary Fano
literature. Its all-degree use here is the contribution, not its discovery.
For \(a\ge3r\), actual equation spaces become

\[
H^0(\mathbf P^3,I_C^r(a))
\cong H^0(V_5,I_\Gamma^{a-3r}(a-2r)).
\]

The source supplies the literal polynomial conversion, using the seven
known cubics and division by the prescribed power of \(q\). This opens
a different global construction space: sections around a conic in a Fano
threefold, with their actual coefficients retained.

The original exceptional surface \(E\) maps to a fixed nonnormal
anticanonical surface \(\Sigma\subset V_5\), given by one explicit
quadratic equation. Its normalization is \(E\cong\mathbf P^1\times
\mathbf P^1\); its full conductor upstairs is twice a smooth \((1,1)\)
curve, which maps three-to-one onto \(\Gamma\). This connects the
problem to anticanonical surface degenerations and conductor gluing.

Retain **both** projections. A trisecant residual line downstairs can be
contracted to a point on \(V_5\); a fiber exceptional over \(C\) can
become a line in \(\Sigma\). If \(W\) is the actual intersection of
strict transforms on \(B\), then

\[
R=0\quad\Longleftrightarrow\quad\operatorname{Supp}W\subset E.
\]

The weaker image condition \(\phi(W)\subset\Sigma\) also permits
trisecants from the other exceptional divisor and is insufficient. This
is a constructive support test on actual equations, not a conclusion
from leading symbols or an exceptional picture alone.

## 6. Singularities can be constructed together with their residuals

The [singular-carrier note](2026-10-28-singular-carrier-construction.md)
and [independent review](2026-10-28-singular-carrier-audit.md) construct
actual sufficiently high-degree complex carriers with a prescribed
\(A_{r-1}\) singularity at a chosen point of \(C\), for every
\(r\ge2\). The marked curve generates the local class group
\(\mathbf Z/r\). High local index is therefore available geometry.

For \(1\le m<r\), actual sufficiently high-degree mates have cycle
\(mC+D\), with \(D\) smooth integral. The local model is

\[
F=ty-z^r,\qquad G=y+z^m,
\]

so the residual is the smooth curve
\((y+z^m,t+z^{r-m})\). Its local class is \(-m\) and cancels that of
\(mC\). It meets reduced \(C\) in length one, but the full primary
component in length \(m\). Residual curves are doing explicit geometric
work at the singularity, rather than merely surviving elsewhere.

The same local construction tests the graph interpretation directly. For
\(2\le m<r\), the \(z\)-chart of the blowup has
\(y=uz\) and strict intersection
\((u+z^{m-1},z^{m-1}(t+z^{r-m}))\). Its cycle is
\((m-1)e+\widetilde D\), where \(e\) dominates \(C\) and
\(\widetilde D\) is the actual residual transform. The other chart has
no extra vertical component. This identifies exceptional thickness and
residual support in one explicit calculation; see the source's §4.1 and
the root addendum to its audit.

Local index and the global positive relation \(n[C]=b[H]\) are separate
construction problems. A standard base-locus Noether–Lefschetz theorem
computes \(\operatorname{Cl}(S)=\mathbf ZH\oplus\mathbf ZC\) for the
very general members of this specified complex family. Special carriers
with a global relation require additional construction data; these general
members do not classify all carriers.

The [literature refresh](2026-10-28-containing-intersections-literature.md)
also records Brevik–Nollet's paper published online October 19, 2026. For
very general sufficiently high-degree complex surfaces containing an
ordinary thick neighborhood \(I_C^q\), it computes the Picard group.
It does not identify every almost-Cartier divisor with a line bundle or
settle our construction endpoint. Its exact parameter space and divisor
theory must remain visible.

## 7. How this changes the next step

There are now three distinct geometric operations to investigate:

1. **Change attachment and residual shape at fixed thickness.** We have
   every-divisor constructions and substantial actual equation freedom.
   Test residual singularities or splitting while keeping the recovered
   partner and chosen attachment data.
2. **Move residual support into thickness.** Follow the flat once-linked
   \(D_1\), allow it to acquire a \(C\)-supported part, and recompute
   the full primary component and genuine residual in each fiber. The
   two projections supply an alternative way to engineer and detect this
   operation with actual equations.
3. **Construct a global endpoint mechanism.** On a normal carrier retain
   the global divisor relation; on a nonnormal one retain full inverse
   support and conductor descent. Prescribed local singularities, finite
   jet surjectivity and contact concentration do not by themselves supply
   that extra global data.

The next integrated experiment should use the second operation: design a
family in the fixed-partner liaison incidence, express it also in the
conic section spaces on \(V_5\), and track which components of its graph
intersection enter \(E\). A proposed family must provide the actual
homogeneous forms, properness, the once-linked flat family and fiberwise
full-primary extraction. The question is which residual configurations
can reach one another and what global geometry permits the transition.
Its degrees should follow from the construction being tested; there is
no reduction to sextics and no assumption of eventual impossibility.

## Evidence and remaining limitations

The four source notes above each have a separate independently reconstructed
audit, and the [integration audit](2026-10-28-containing-intersections-integration-audit.md)
checks their combination, including relative once-link flatness. The new
normal-layer verifier checks 15 exact rational ranks; the
new liaison verifier checks canonical-module matrix ranks over \(\mathbf Q\)
and five proper links over a finite field. Universal statements rely on
the written proofs and cited theorems, not finite extrapolation. Detailed
commands, logs and navigation checks are in the
[validation record](../validation/2026-10-28-containing-intersections/README.md).

The inherited conormal splitting is promoted R-0020. The inherited general
residual theorem and cubic graph model are reviewed provisional premises.
The new normal-jet calculation, all-divisor construction, relative liaison
family, section dictionary, conductor identification and singular-carrier
families are reviewed proposals, with their stated characteristic and
generality restrictions. No source here constructs a characteristic-zero
STCI pair for \(C\), excludes arbitrary pairs, or claims literature novelty.
