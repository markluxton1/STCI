# Independent audit: numerical residual capacity on normal carriers

Date: 2026-10-28. Reviewer: `blowup_linear_systems` research agent,
independent of the proposing `singular_carrier_construction` agent.
Source: [Residual-degree capacity on normal carriers](2026-10-28-residual-degree-singular-carriers.md).

**Outcome: PASS for the stated normal integral complex carrier bound,
including its non-Q-Cartier scope, marked singularity corrections, and
general-curve template.** These remain independently reviewed provisional
deductions. This audit does not promote them or endorse the earlier
October 17 pending endpoint-sufficiency claim.

## 1. Principalized ideal and effective numerical residual

The actual hypotheses are a fixed smooth quartic \(C\), a normal integral
degree-\(a\) carrier \(S\), and a proper mate of degree \(b\), with cycle
\(mC+R\). The residual is the full genuine residual cycle. It can be
weighted; no Cartier, locally free, reduced, or smooth residual hypothesis
is used.

I independently reconstructed the two essential geometric inputs. Choose
a smooth projective resolution also principalizing \(I_{C/S}\). Its
invertible image is \(\mathcal O_X(-Z)\), where
\(Z=\widetilde C+\text{exceptional}\). The coefficient of the nonexceptional
strict curve is one because the normal surface is a DVR at \(\eta_C\).
The ideal is the unit ideal off the inverse image of \(C\), so there are
no other nonexceptional components. The ambient generated ideal
\(I_C(3)\) maps onto \(I_{C/S}(3)\), and its evaluation remains surjective
onto the invertible image after pullback. Hence \(L=3H-Z\) is globally
generated and nef.

Separately, Mumford pullback preserves effectivity for **every** effective
Weil residual. If \(M=(E_iE_j)\) is the exceptional matrix and
\(v_i=\widetilde R E_i\ge0\), the correction vector satisfies
\((-M)q=v\). Here \(-M\) is positive definite, with nonpositive
off-diagonal entries. Splitting \(q=q_+-q_-\) into disjoint nonnegative
parts gives

\[
0\le q_-^t v
=q_-^t(-M)q_+-q_-^t(-M)q_-
\le -q_-^t(-M)q_-.
\]

Thus \(q_-=0\). This proves that \(R^{\rm num}\) is an effective
rational divisor even when the original Weil residual is not Q-Cartier.
The argument applies independently on each exceptional block and to all
positive cycle multiplicities.

I freshly opened [Schröer's primary surface-pullback discussion, §1](https://www.journalofsing.org/volume19/schroer.pdf),
which explicitly retains linearity, effectivity and exceptional
orthogonality for normal surfaces without a class-group assumption. I
also opened [Mumford's original paper](https://www.numdam.org/item/10.1007/BF02698717.pdf),
checking the negative-definiteness statement on printed p. 6. The source's
Springer link to Langer was inaccessible to this review tool; neither
the proof nor this audit depends on accessing that additional reference.

## 2. Quantitative inequality and division signs

Put \(T=C^{\rm num}\), \(t=T^2\). Numerical pullback of the actual
Cartier divisor of the mate gives
\(R^{\rm num}\equiv bH-mT\). The difference \(Z-T\) is exceptional,
whereas \(H\) and \(T\) are orthogonal to exceptional curves. Therefore

\[
\begin{aligned}
0\le(3H-Z)R^{\rm num}
&=b(3a-4)-m(12-t).
\end{aligned}
\]

No assertion that \(3H-C\) is a line bundle on the singular carrier is
needed. No effectivity statement about \(bH-m\widetilde C\) is substituted
for effectivity of the actual numerical residual.

Hodge index on the smooth resolution applies to the positive-square
nef class \(H\), giving \(t\le(H T)^2/H^2=16/a\). The quartic is
nonplanar, so \(a\ge2\), and hence \(12-t\ge4>0\). Division yields

\[
m\le\frac{b(3a-4)}{12-t},
\qquad
\deg R=ab-4m\ge\frac{b(16-at)}{12-t}.
\]

Taking the floor of the upper bound on \(m\) gives precisely the source's
integer version; it respects \(\deg R\equiv ab\pmod4\). The numerator
is nonnegative by Hodge index. It is positive only for a strict Hodge
gap. The equality case remains an allowed zero lower bound, not a
contradiction or a sufficient global divisor relation.

## 3. Marked A-type and general adjunction corrections

For \(ty-z^r=0\), \(C=(y,z)\), the strict curve on the minimal
A-type resolution meets an end of the \((-2)\)-chain transversely. Solving
the tridiagonal orthogonality equations gives correction coefficients
\((r-i)/r\), and numerical self-intersection correction \((r-1)/r\).
Crepancy and adjunction give \(\widetilde C^2=14-4a\), so

\[
t=15-4a-1/r.
\]

The inequality therefore has denominator \(4a-3+1/r\) and numerator
\(b(4a^2-15a+16+a/r)\), as in the source. This applies to every proper
mate on a carrier with those literal marked singularities, independently
of whether a sufficiently large mate was used in the earlier existence
construction.

For \(a\ge4\), replacing \(1/r\) by zero weakens the residual fraction.
The remaining comparison with \(5/13\) reduces to

\[
\frac8{13}-\frac{4(3a-4)}{a(4a-3)}
=\frac{4(a-4)(8a-13)}{13a(4a-3)}\ge0.
\]

Thus the coarse fraction is valid in this marked family. It is not an
optimality claim or a general local-index-only bound. The corrections
add for several disjoint end-curve points; substituting their sum gives
the displayed multiple-point formulas, with positivity of the denominator
already ensured by Hodge index.

For a marked curve meeting the \(i\)-th exceptional component, the
inverse Cartan diagonal is \(i(r-i)/r\), and its local class has index
\(r/\gcd(r,i)\). In particular the two numerical corrections at positions
1 and 6 for \(r=13\) are \(12/13\) and \(42/13\), with the same local
index. This correctly rejects an unmarked index-only substitution.

Finally write \(K_X=f^*K_S+\sum\alpha_iE_i\) and
\(v_i=\widetilde C E_i\). Adjunction gives
\(\widetilde C^2=14-4a-\alpha^t v\), while the numerical pullback adds
\(-v^tM^{-1}v\). Thus the source's general marked correction
\(-\alpha^tv-v^tM^{-1}v\) has the correct signs. It is not identified
with an attachment length, comparison module, or equation-module defect.

## 4. General-curve template and limitations

For degree \(c\) and a generated \(I_C(d_0)\), the identical calculation
gives

\[
0\le b(d_0a-c)-m(d_0c-t).
\]

When \(d_0c-t>0\), substituting \(\deg R=ab-cm\) gives
\(\deg R\ge b(c^2-at)/(d_0c-t)\). If the denominator vanishes,
the source correctly retains the undivided inequality. The smooth
quartic and the different twisted-cubic cone controls are consistent:
the former recovers the inherited smooth-carrier capacity argument;
the latter has zero Hodge gap and an actual sole-support example.

No proof step uses the October 17 pending equivalence between a Hodge
boundary and an endpoint construction. Normality is essential for the
numerical pullback used here. The source supplies no normality reduction
for arbitrary carriers, no strictly positive gap for all normal carriers,
and no unrestricted fixed-quartic STCI conclusion. The new quantitative
claim passes independent reconstruction exactly with those limitations.
