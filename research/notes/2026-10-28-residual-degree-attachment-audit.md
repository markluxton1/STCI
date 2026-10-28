# Independent audit: residual degree from marked attachment

Date: 2026-10-28. Reviewer: residual-liaison agent, independent of the
source author. Source:
[marked attachment detector](2026-10-28-residual-degree-attachment-detector.md).
**Outcome: PASS within the stated any-characteristic, actual-proper-pair
scope; reviewed provisional work, not canonical promotion.**

This review independently reconstructed the Cartier-quotient bound and an
actual sharp homogeneous family. The October 27 attachment-module identity
was checked for matching hypotheses and used as an inherited reviewed
premise; its proof and accepted quartic certificates were not rerun.

## 1. Direct finite-scheme bound, including nonreduced residuals

The full residual \(Z\) has no component equal to the smooth integral
\(C\). Hence \(C\cap Z\) is finite. Local Cohen–Macaulayness and purity
mean that all associated points of \(\mathcal O_Z\) are the generic
points of its finitely many curve components. This is the exact reason
that avoiding those components suffices to make a section regular on
the full, possibly nonreduced, scheme.

At the generic point of each such component, the ideal of \(C\) is the
unit ideal. Global generation of \(I_C(3)\) therefore supplies a cubic
not vanishing on that component. The sections vanishing on it form a
proper linear subspace of \(H^0(I_C(3))\). The algebraically closed field
is infinite in every characteristic, so one cubic can avoid the finite
union of these subspaces. No reducedness, normality, or Gorenstein
hypothesis on \(Z\) enters this step.

For the resulting nonzerodivisor \(h\), the exact sequence is

\[
0\to\mathcal O_Z(-3)\xrightarrow{h}\mathcal O_Z
\to\mathcal O_{Z\cap V(h)}\to0.
\]

The Hilbert polynomial of the **actual** scheme \(Z\) has leading
coefficient \(\delta=\deg[Z]\); subtraction gives
\(\operatorname{length}(Z\cap V(h))=3\delta\). Since \((h)\subset I_C\),
the quotient by \(h\) surjects onto the quotient by \(I_C\). Thus

\[
\operatorname{length}(C\cap Z)\le3\delta.
\]

This argument retains the nilpotents and uses neither normalization nor
reduction. If no residual component is contained in \(Q\), its fixed
equation \(q\) is likewise a nonzerodivisor, and the same exact-sequence
calculation gives the factor two. If a residual component lies on \(Q\),
that replacement fails; the cubic argument still applies. The empty
residual has both sides zero, consistent with the stated inequality.

The reviewer opened [Stacks, degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ),
including the effective-Cartier-divisor and multiplicity statements. The
source's Hilbert-polynomial proof is sufficient on its own and has the
same nonreduced-scheme scope.

## 2. The equation-module substitution is literal

The source uses the full \(C\)-primary component \(T\) of an actual
complete intersection, with \(I=I_C\), \(J=I_T\), and \(E_T=J/IJ\).
Those are the hypotheses of the inherited
[attachment-module identity](2026-10-27-absorption-attachment-module.md),
not the weaker setting of an arbitrary lower thickening. At \(\eta_C\),
the two actual equations minimally generate \(J\), so their determinant
on the torsion-free rank-two quotient is generically nonzero. The inherited
identity therefore gives

\[
\operatorname{length}(C\cap Z)
=\operatorname{length}(\operatorname{tors}E_T)
 +\deg\operatorname{div}\theta.
\]

Substituting this equality in the direct bound is valid in any
characteristic. It does not omit a non-lci contribution: that contribution
is precisely the torsion term. It also does not add the normal-nilpotent
contribution in the full \(T\cap Z\), which is a different length.
No assertion that the numerator must be positive for every
characteristic-zero pair has been established or used.

## 3. Independent reconstruction of the sharp actual family

The bidegrees in the source already give the required global construction.
There is also a concrete reconstruction using the fixed cubic generators,
which verifies that the family concerns homogeneous equations rather
than abstract cycles. Write the Segre coordinates as

\[
x_0=u\alpha,\quad x_1=u\beta,\quad
x_2=v\alpha,\quad x_3=v\beta,
\qquad c=\alpha^3v-\beta^3u.
\]

Here \(C=V(c)\) on \(Q\). This labels the two factors oppositely to
the source's \((1,3)\) convention. The three actual cubics

\[
U=x_0^2x_2-x_1^3,\quad
V=x_0x_2^2-x_1^2x_3,\quad
W=x_2^3-x_1x_3^2
\]

restrict to \(u^2c,uvc,v^2c\). Choose \(s\) binary quadratics in
\(u,v\) whose combined \(2s\) linear factors are distinct, and realize
each quadratic as a linear combination of \(U,V,W\). Their product is
an actual degree-\(3s\) form \(G\) restricting to \(c^sP_{2s}(u,v)\).
Such choices exist over an algebraically closed field in every
characteristic; this does not rely on a potentially inseparable expression
such as a sum of two \(s\)-th powers.

The restriction of \(G\) to \(Q\) is nonzero, so \(q,G\) is a proper
pair. Its divisor on \(Q\) is exactly \(sC+B\), where \(B\) is the
union of the \(2s\) distinct ruling lines. In the source's convention
these have class \((2s,0)\). The full primary component is the Cartier
multiple \(sC\), and the residual is precisely \(B\), with no embedded
points. Therefore

\[
\deg R=2s,\qquad
\operatorname{length}(C\cap B)=C\cdot B=6s,
\]

which attains the factor-three estimate. Even in a characteristic in
which some attachments are nonreduced, this intersection **length** is
unchanged. Reduced attachments are neither needed nor asserted.

The complete thick attachment is instead

\[
\operatorname{length}(sC\cap B)=s(C\cdot B)=6s^2.
\]

One can compute it on each ruling line by quotienting by the \(s\)-th
power of the restricted Cartier equation of \(C\). For \(s>1\), this
exceeds \(3\deg R=6s\), so the family disproves substituting the full
attachment into the marked inequality. It also shows that the constant
three cannot be lowered for arbitrary proper pairs containing this fixed
quartic. The factor-two bound has its separate no-quadric-component
hypothesis, which this family deliberately does not satisfy.

## 4. Literature, utility, and exact limitation

The targeted repository check confirms that the October 19 and October 25
sources already bound valuative residual contact by \(3\deg R\). The
source correctly retains them as prior work. Its finite-scheme quotient
argument and equation-module substitution do not require identifying
marked intersection length with a normalization contact cycle, and no
claim of literature originality is made.

An independently controlled positive lower bound for the marked length
or for the module numerator yields a quantitative lower bound for the
genuine residual degree, including nonreduced residuals. The source
correctly explains that a completed full-primary extraction already
knows the multiplicity and hence the residual degree. The new inequality
is then a consistency check; its strategic use is with an independent
lower bound or a controlled family, not a circular re-expression of an
already known decomposition.

The congruence \(\deg R\equiv ab\pmod4\) can strengthen the integer
floor exactly as illustrated. Neither the inequality, its sharp family,
nor the module identity proves a universally nonzero numerator or rules
out a higher-degree sole-support endpoint. No substantive correction was
required by this audit.
