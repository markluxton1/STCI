# Third intervention: surface-effective thresholds and the second normal resultant

Date: 2026-08-23

Operation: direct lead proof and synthesis.

## Question and reason for selection

The second intervention left common-leading-factor thick pairs as the hard generic
normal-contact branch. The next high-information question was whether the first blow-up
can be globalized far enough to produce a new obstruction, rather than merely renaming
the excess intersection multiplicity.

Two interfaces were combined:

1. a fixed containing surface on which \(C\) fails the APic/divisor proportionality
   test; and
2. the line quotient of the conormal bundle selected by a common first normal
   direction.

The rational quartic is used only after the general lemmas, because its smooth quadric
has an explicit effective cone and its balanced conormal bundle makes both sides exact.

## 1. A surface obstruction constrains every equation of a hypothetical pair

### Lemma: component exclusion

Let \(C\subset S\subset\mathbf P^3\) be an irreducible curve on an integral surface
\(S=V(Q)\). Suppose \(C\) is not an STCI on \(S\). If
\[
   \sqrt{(F,G)}=I_C,
\]
then neither \(F\) nor \(G\) is divisible by \(Q\).

Indeed, if \(Q\mid F\), then \(V(Q,G)\subset V(F,G)=C\) set-theoretically. Unless
\(Q\mid G\), which would give a common surface component, \(V(Q,G)\) is a projective
curve. Its support must therefore be \(C\), making \(C\) an STCI on \(S\), contrary to
the hypothesis.

### Effective-threshold consequence

Assume now that \(S\) is smooth, with hyperplane class \(H\). If
\(F\in H^0(\mathcal I_C^p(a))\) and \(Q\nmid F\), then the nonzero divisor
\(F|_S\) has class \(aH\) and contains \(pC\). Hence
\[
   aH-pC\quad\text{is effective on }S.
\]
Define the surface-effective threshold
\[
 \tau_S(C)=\inf\left\{\frac ap:aH-pC\text{ is effective},\ p>0\right\}.
\]
Every equation in every two-equation radical presentation of \(C\) then satisfies
\[
   \frac ap\geq\tau_S(C),
\]
provided \(C\) is not an STCI on \(S\). This is stronger than the raw symbolic
Waldschmidt slope when the latter is achieved by powers of \(Q\), since those powers
are incompatible with a radical defining pair.

If the two normal orders are \(p,q\) and their generic intersection multiplicity is
\(m\), then
\[
  ab=dm,
  \qquad
  \frac{m}{pq}=\frac{(a/p)(b/q)}d
      \geq\frac{\tau_S(C)^2}{d}.
\]
Thus a surface-specific APic failure can force quantitative excess contact in *every*
thick pair. It is not yet a global exclusion, but it is an intrinsic bridge from the
surface description to the normal-contact description.

## 2. Rational quartic: a uniform excess lower bound

Let
\[
 C_4:[s:t]\longmapsto[s^4:s^3t:st^3:t^4].
\]
It lies on the smooth quadric \(Q=V(xw-yz)\). Under
\(Q\simeq\mathbf P^1\times\mathbf P^1\), after choosing the rulings,
\[
   H=(1,1),\qquad C_4=(1,3).
\]
The class \(aH-pC_4=(a-p,a-3p)\) is effective exactly when \(a\geq3p\).
Moreover \(C_4\) is not an STCI on \(Q\), since no positive multiple of \((1,3)\)
is a multiple of \((1,1)\). The component-exclusion lemma therefore applies to
*both* equations of any hypothetical defining pair, and
\[
   a\geq3p,\qquad b\geq3q.
\]

Since \(d=4\), every hypothetical pair satisfies
\[
   m=\frac{ab}{4}\geq\frac94pq,
   \qquad
   m-pq\geq\left\lceil\frac54pq\right\rceil.
\]
For a thick pair \(p,q\geq2\), the generic excess is therefore at least five. This
substantially strengthens the second intervention's conclusion that the excess is
merely positive.

The distinction from the raw symbolic slope is instructive. Powers \(Q^p\) show that
\(H^0(\mathcal I_{C_4}^p(2p))\ne0\), but no equation divisible by \(Q\) can occur in
a radical defining pair. The pair-compatible slope is three, not two.

## 3. Recursive resultant for one common normal direction

The following proposition globalizes one further blow-up level.

### Setup

Let \(C\subset\mathbf P^3\) be smooth, let \(F_a,G_b\) have normal orders \(p,q\),
and blow up \(C\):
\[
  \pi:X_1=\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3,
  \qquad E=\mathbf P(\nu),
\]
where \(\nu=N^*_{C/\mathbf P^3}\) and
\(\mathcal O_E(1)=\mathcal O_{X_1}(-E)|_E\).

Assume the strict transforms have a single common horizontal curve
\(\Gamma\subset E\), that \(\Gamma\to C\) is a section, and that there are no other
curve components in their intersection. The section corresponds to a quotient
\[
  \nu\twoheadrightarrow T=\mathcal O_E(1)|_\Gamma.
\]
Let \(r,s\) be the normal orders of the two strict transforms along \(\Gamma\), and
assume their first normal forms there are coprime. Plane-curve multiplicity sequences
give \(1\le r\le p\) and \(1\le s\le q\).

### Proposition

Under these hypotheses,
\[
   m=pq+rs,
   \qquad
   ab=d(pq+rs),
\]
and, with \(\lambda=ps+qr-rs>0\),
\[
  T^{\lambda}\simeq
  \omega_C^{rs}\otimes
  \mathcal O_C(4rs-as-br).
\]

### Proof

Noether's blow-up formula for two plane curve germs gives
\(i_C(F,G)=pq+i_\Gamma(F_1,G_1)=pq+rs\). The complete-intersection cycle then
gives the degree equality.

The strict-transform line bundles restrict to
\[
  \mathcal O_{X_1}(aH-pE)|_\Gamma
       \simeq\mathcal O_C(a)\otimes T^p,
  \qquad
  \mathcal O_{X_1}(bH-qE)|_\Gamma
       \simeq\mathcal O_C(b)\otimes T^q.
\]
If \(K=\ker(\nu\twoheadrightarrow T)\), then
\[
  N_{\Gamma/E}\simeq K^*\otimes T
       \simeq T^2\otimes(\det\nu)^{-1},
  \qquad
  N_{E/X_1}|_\Gamma\simeq T^{-1}.
\]
Therefore
\[
  \det N^*_{\Gamma/X_1}\simeq(\det\nu)\otimes T^{-1}.
\]
Applying the first-normal resultant theorem on \(X_1\) to the two strict transforms
gives
\[
 (\det\nu)^{rs}\otimes\mathcal O_C(as+br)
 \otimes T^{ps+qr-rs}\simeq\mathcal O_C.
\]
Adjunction \(\det\nu\simeq\omega_C^{-1}(-4)\) yields the claim.

This relation connects the excess-contact direction to a quotient of the conormal
bundle, equivalently to a line subbundle of the normal bundle. It is the first explicit
bridge from the thick contact tree back to the line-bundle data used for primitive
multiple structures.

## 4. Rational quartic: the one-section/two-level stratum is empty

For \(C_4\), Ellia records
\[
  \nu\simeq\mathcal O_{\mathbf P^1}(-7)^{\oplus2}.
\]
Every quotient line bundle \(T\) has \(\deg T\geq-7\). Taking degrees in the recursive
resultant gives
\[
  (ps+qr-rs)\deg T=14rs-4(as+br).
\]
The surface-effective threshold gives \(a\geq3p\), \(b\geq3q\), hence
\[
  14rs-4(as+br)\leq14rs-12(ps+qr).
\]
On the other hand \(\deg T\geq-7\) would require
\[
 -7(ps+qr-rs)\leq14rs-12(ps+qr),
\]
or
\[
   5(ps+qr)\leq7rs.
\]
But \(r\leq p\) and \(s\leq q\) imply
\(ps+qr\geq2rs\), making the left side at least \(10rs\). This is impossible.

Therefore no hypothetical thick defining pair for the rational quartic can have its
entire generic excess supported on one global normal-direction section and become
first-normal-transverse after the next blow-up, regardless of the four normal orders.

The conclusion is deliberately narrower than non-STCI. A remaining pair could have:

- several common first normal directions;
- a horizontal multisection that becomes a section only after a finite cover;
- ramification or nonreduced common-direction data;
- additional vertical exceptional components; or
- contact persisting through two or more further blow-ups.

These are now mathematically forced alternatives, not an undifferentiated list of
singular possibilities.

## Evidence boundary and failed routes

- The component-exclusion lemma uses failure of STCI on the chosen surface; it does not
  say that failure on one surface globally excludes the curve.
- The threshold \(\tau_S(C)\) is useful only when the effective cone of \(S\) is
  controlled and equation components supported on \(S\) have been excluded.
- The recursive proposition assumes a single smooth section and no other curve support
  after the first blow-up. It is not yet the multisection or branching formula.
- A direct numerical scan before using the surface-effective threshold left many
  admissible tuples. The decisive improvement came from recognizing that powers of the
  quadric cannot occur in a radical pair; raw symbolic-degree numerics were too weak.

## Research delta and strategic consequence

- **New bridge:** a surface APic failure can constrain all defining equations through
  the effective cone, forcing a lower bound on thick excess multiplicity.
- **New recursive invariant:** a common normal-direction section carries a conormal
  quotient \(T\) satisfying an exact second resultant relation.
- **Rational-quartic consequence:** every thick pair has generic excess at least five,
  and no one-section contact cluster can resolve at the second level.
- **More plausible:** the right global thick object is a branched normal-contact tree
  decorated by line bundles on finite covers of \(C\).
- **Less plausible:** a two-level computation on a single section will settle even the
  smallest unresolved curve; the geometry is forced into branching, monodromy, or
  longer contact.
- **Next discriminating intervention:** derive the multisection version, including its
  norm, ramification, and normal-bundle terms, before returning to any explicit equation
  search.

## Source anchors

- C. Bănică and O. Forster, *Multiplicity Structures on Space Curves*, Contemp.
  Math. 58 (1986), especially the filtration and conormal-discriminant constructions.
- P. Ellia, *Complete intersections primitive structures on space curves*,
  arXiv:1409.3801, Lemma 4 for the rational-quartic normal bundle.
- R. Hartshorne and C. Polini, *Divisor class groups of singular surfaces*,
  arXiv:1301.3222, Proposition 7.1 for the surface STCI criterion.
