# A universal residual-degree bound from the marked attachment module

Date: 2026-10-28. Author: root integration agent. **Provisional contribution,
independently reviewed in the [separate audit](2026-10-28-residual-degree-attachment-audit.md);
no canonical promotion.** This applies over an
algebraically closed field in any characteristic to the fixed smooth
quartic \(C=[s^4:s^3t:st^3:t^4]\).

## 1. Exact statement

Let \(Y=V(F_a,G_b)\) be an actual proper homogeneous intersection
containing \(C\). Let \(T\) be its full \(C\)-primary component and
\(Z\) its linked residual, sharing no component with \(C\). Write

\[
[Y]=m[C]+R,\quad [Z]=R,\quad \delta=\deg R=ab-4m,
\qquad A=\operatorname{length}(C\cap Z).
\]

The residual \(Z\) may be nonreduced, disconnected or non-Gorenstein.
It is a pure locally Cohen–Macaulay curve when nonempty. Then

\[
\boxed{\delta\ge\left\lceil\frac A3\right\rceil.}\tag{1}
\]

If no component of \(R\) lies on the unique containing quadric \(Q\),
then

\[
\boxed{\delta\ge\left\lceil\frac A2\right\rceil.}\tag{2}
\]

Neither bound assumes an integral or normal carrier, nor a reduced
residual. The attachment in these formulas is to **reduced marked**
\(C\), not the generally larger full \(T\cap Z\).

## 2. Direct proof and a module-to-degree bridge

The inherited global generation of \(I_C(3)\) lets us choose a cubic
\(h\) through \(C\) containing none of the finitely many components
of \(Z\). Indeed, at the generic point of any component distinct from
\(C\), global generation gives some section nonzero there; avoid the
finite union of proper linear subspaces. Purity makes \(h\) a
nonzerodivisor on \(O_Z\). Thus \(Z\cap V(h)\) is finite of length
\(3\delta\), by the exact Cartier sequence and the Hilbert polynomial.
Since \(h\in I_C\), there is a surjection

\[
O_Z/(h)\twoheadrightarrow O_Z/I_C O_Z=O_{C\cap Z}.
\]

Therefore \(A\le3\delta\). If \(Z\) has no component on \(Q\),
use its quadratic equation instead of \(h\) and get \(A\le2\delta\).
This proof does not reduce \(Z\) or replace it by its normalization.

The new use of the [reviewed attachment-module identity](2026-10-27-absorption-attachment-module.md)
and [independent audit](2026-10-27-absorption-attachment-module-audit.md)
is to make the numerator accessible from the full primary equation module.
Put \(I=I_C\), \(J=I_T\), and \(E_T=J/IJ\). The actual two equation
classes map into \(E_T\). Let

\[
\tau=\operatorname{length}(\operatorname{tors}E_T),\qquad
\eta=\deg\operatorname{div}\theta,
\]

where \(\theta\) is the determinant of their induced map into the
torsion-free rank-two quotient. Because \(T\) is the **full** primary
component, this determinant is generically nonzero. The inherited identity
is \(A=\tau+\eta\). Consequently

\[
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{3}\right\rceil,}
\quad\text{or}\quad
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{2}\right\rceil}
\quad(R\text{ has no component on }Q). \tag{3}
\]

This combines an already reviewed module identity with an elementary
scheme-theoretic Bézout estimate. It is not a new assertion of positivity
of \(\tau+\eta\) for every characteristic-zero pair. At a sole-support
endpoint \(Z\) is empty and both vanish. It also does not let one replace
\(A\) by the full attachment: the extra normal-nilpotent length in
\(T\cap Z\) is absent from (3).

## 3. A sharp actual family and the failure of the full-attachment substitution

On \(Q\cong\mathbf P^1\times\mathbf P^1\), use
\(C\sim(1,3)\). For any integer \(s\ge1\), choose a divisor
\(B\in |O_Q(2s,0)|\) consisting of \(2s\) distinct trisecant ruling
lines. The product of its section and the \(s\)-th power of the
Cartier equation of \(C\) is a section of
\(O_Q(3s,3s)=O_Q(3s)\). It lifts to an actual homogeneous form \(G_{3s}\)
because \(H^1(\mathbf P^3,O(3s-2))=0\). The proper pair \((q,G_{3s})\)
has, as a divisor on the smooth quadric,

\[
Y=sC+B,
\quad T=sC,
\quad R=B,
\quad \delta=2s,
\quad A=C\cdot B=6s.
\]

It attains \(A=3\delta\), proving that coefficient three cannot be
improved for arbitrary proper pairs in (1). This reuses the known smooth-
quadric construction principle; it does not reopen a closed STCI case.

The full attachment has length
\(\operatorname{length}(T\cap Z)=sC\cdot B=6s^2\).
For \(s>1\), substituting that length into \(A\le3\delta\) would be
false. This family therefore gives an actual fixed-quartic control for
both sharpness and the necessary marked/full distinction.

## 4. How to use the bound without making it circular

The inequalities are useful when geometry supplies an independent lower
bound \(A\ge A_0\), or a bound on \(\tau+\eta\), for a class of possible
primary structures. If one has already explicitly computed the entire
primary ideal and its degree, then \(m\), hence \(\delta\), is already
known; (3) is then a consistency check. It is not a shortcut around a
completed primary decomposition.

Every bound must also respect \(\delta\equiv ab\pmod4\). For example,
an independent estimate \(A\ge13\) gives \(\delta\ge5\); if
\(ab\equiv0\pmod4\), this strengthens to \(\delta\ge8\).

For any curve whose ideal is generated in twist \(d_0\), the same proof
gives \(\deg R\ge\lceil\operatorname{length}(C\cap Z)/d_0\rceil\).
Any independently known hypersurface through \(C\), avoiding all residual
components, gives its own degree in the denominator. The quartic's quadric
and cubics give the two especially simple alternatives above.

## 5. Retrieval and literature boundary

The [October 19 residual-contact bound](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md)
already proves \(E\cdot\widetilde R\le3\deg R\), and the
[October 25 valuative-contact note](2026-10-25-ci-cycle-valuative-contact-cycle.md)
states that estimate on normalized weighted residual branches. Neither is
being rediscovered here as new positivity. The present formulation is for
the finite **scheme** \(C\cap Z\), including nonreduced \(Z\), and
connects it explicitly to the full-primary equation module. The direct
Cartier-quotient proof avoids identifying that finite scheme with a
valuative cycle or the full conductor boundary.

The inputs are standard Bézout/Cartier intersection and the previously
reviewed module identity. A primary reference for the former is
[Stacks, degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ).
No literature novelty, universal nonzero residual, or additional
computational certificate is asserted.
