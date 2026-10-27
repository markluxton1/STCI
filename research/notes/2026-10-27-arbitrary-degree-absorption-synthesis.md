# Arbitrary-degree residual absorption: construction, attachment and equation lifting

Date: 2026-10-27. This continues the [containing-intersections vision](2026-10-27-containing-intersections-research-vision.md) after the user's explicit correction: put a general construction or geometric principle first; use a degree-specific example only to test it. **All new deductions are independently reviewed provisional evidence, not canonical promotions or claims of literature novelty.** The characteristic-zero STCI question for the fixed quartic remains open.

## 1. What changed in this pass

The question was whether residual geometry can specialize into thickness on the fixed \(C=[s^4:s^3t:st^3:t^4]\), and which local/global data govern that operation. The work now supplies a positive operation across degrees, a scope-specific capacity bound, a precise fiberwise attachment identity, and an obstruction to moving actual equations with a lower thickening. It supplies no reduction from arbitrary degrees to sextics.

| Interface | Result | Scope and limit |
|---|---|---|
| Actual absorption | Given \(1\le m<n\), a construction transfers \(4(n-m)\) units of residual degree onto \(C\) on a chosen smooth carrier, for \(b\ge3n+1\); a weaker large-twist version works on any normal integral carrier | Actual global homogeneous pairs; chosen families, not a deformation theorem for every given residual; smooth residual/Cartier gluing requires the stronger hypotheses |
| Smooth-carrier capacity | \(\deg R\ge ab/3\), with a sharper carrier-degree-dependent bound | Integral degree-\(a\) carrier smooth at every point of \(C\); singularities away from \(C\) allowed; not a bound for arbitrary singular carriers |
| Actual attachment | \(C\cap D=\operatorname{div}(\operatorname{tors}\mathcal E_T)+\operatorname{div}(\det\bar\rho)\) | Full primary component \(T\) of an actual proper CI, linked residual \(D\); no curvilinearity or lci hypothesis on \(T\); fiberwise, not a base-change assertion |
| Moving equations | A marked lower-thickening motion lifts to actual degree-\((a,b)\) equations exactly when two explicit connecting classes vanish | First-order criterion and conditional Artin-step extensions; a tangent need not integrate; larger degree can remove this particular obstruction |
| Characteristic comparison | Finite Frobenius repairs, semi-invariant powers and cancellation of conductor defects are distinct mechanisms | Exact local/conditional constructions; actual admissible carrier and global divisor relations for \(C\) remain to be constructed |

## 2. A positive characteristic-zero operation across multiplicities

Let \(S=V(F_a)\) be any smooth integral containing surface, \(H=\mathcal O_S(1)\). The ideal \(I_C(3)\) is globally generated, so \(L=3H-C\) is globally generated. If \(b\ge3n+1\), the line bundles

\[
bH-rC=rL+(b-3r)H,\qquad r=m,n,
\]

are very ample. Choose smooth integral residual divisors \(D_r=V(\tau_r)\) in them and form

\[
\sigma(t)=s_C^n\tau_n+t\,s_C^m\tau_m.
\]

Hypersurface restriction lifts these sections to **actual** homogeneous forms \(G_n+tG_m\) of degree \(b\). Every finite fiber is proper. Every nonzero parameter has exact generic multiplicity \(m\) on \(C\); the special fiber has exact multiplicity \(n\). The residual after removing the fixed lower divisor \(mC\) is a flat Cartier family whose special member is

\[
(n-m)C+D_n.
\]

For general nonzero parameters its residual is smooth and integral. Thus partial absorption with scheme-theoretic gluing actually occurs in characteristic zero. It is not an intrinsically Frobenius-only phenomenon.

This mechanism works for any smooth curve whose ideal is generated in some degree \(\delta\), with sufficient bound \(b\ge\delta n+1\). The quartic enters through \(\delta=3\), not a special coefficient calculation. The [construction proof and audit links](2026-10-27-absorption-deformation-interface.md) also distinguish this flat residual closure from re-extracting the full primary component at the special fiber.

The same nef bundle gives a uniform capacity bound. On any integral carrier smooth along \(C\), adjunction gives \(C^2=14-4a\). For \(bH=mC+D\),

\[
0\le(3H-C)\cdot D=b(3a-4)-m(4a-2),
\]

so

\[
m\le\frac{b(3a-4)}{4a-2},\qquad
\frac{4m}{ab}\le\frac23,\qquad \deg D\ge\frac{ab}{3}.
\]

The uniform fraction is sharp. This proof uses no accepted STCI exclusion and works in every characteristic under its smooth-along-\(C\) hypothesis. Its meaning is a capacity statement for this Cartier-carrier geometry, not evidence that absorption is universally impossible. Passing beyond that capacity requires different on-curve carrier geometry; it does not imply a common singular point of the two carriers.

### Normal carriers: partial transfer is easier than the endpoint

The construction note also gives two extensions, with independent audit:

- If \(S\) is normal and \(hC\) is Cartier, Serre twisting makes \(\delta H-hC\) globally generated for some \(\delta\). The same construction works for \(m=hu<n=hv\), with sufficient \(b\ge\delta v+1\). General residuals avoid the finite singular locus and are smooth integral; the Cartier residual family retains scheme-theoretic gluing. Neither an actual new carrier nor a uniform bound on \(\delta\) is supplied.
- Even if \(C\) is not \(\mathbf Q\)-Cartier, the coherent divisorial ideals \(\mathcal O_S(-rC)\) become globally generated after sufficiently large twists. For fixed \(m<n\), choose sections with exact orders \(m,n\) at the DVR \(\eta_C\), then interpolate them and lift to homogeneous equations. This gives proper actual CI families and generic cycle transfer in any characteristic. It gives no asserted smooth residual or commuting/flat full-primary extraction.

The distinction is structural. Partial transfer can be arranged on any fixed normal integral carrier in high enough degree. A sole-support endpoint would instead require the positive global relation \(bH\sim nC\), which in particular makes \(C\) \(\mathbf Q\)-Cartier. Large-twist generation does not supply that relation or imply that all residual mass can disappear.

## 3. Residual attachment has three distinct contributions

For an arbitrary actual proper \(Y=V(F_a,G_b)\), let \(T\) be its full \(C\)-primary component, \(J=I_T\), \(I=I_C\), and \(D\) the residual linked to \(T\). Define

\[
\mathcal E_T=J/IJ,\qquad
\mathcal Q=J/((F,G)+IJ).
\]

The map of actual equation classes into \(\mathcal E_T\) is generically an isomorphism. Its torsion-free determinant \(\theta\) and its torsion contribution satisfy the exact divisor identity

\[
C\cap D=\operatorname{div}(\operatorname{tors}\mathcal E_T)
                    +\operatorname{div}\theta.
\]

This is an actual geometric residual intersection, not an exceptional vertical cycle. The torsion of \(\mathcal E_T\) detects the non-lci points of \(T\). It is distinct from the filtered comparison defect \(\Delta\) in R-0030.

The attachment to the full thick \(T\) is larger. With
\(\epsilon_{\mathrm{normal}}=\operatorname{length}(I_C\mathcal O_{T\cap D})\),
standard linkage gives the combined budget

\[
\operatorname{length}(\operatorname{tors}\mathcal E_T)
+\deg\operatorname{div}\theta+\epsilon_{\mathrm{normal}}
=(a+b-4)\deg T-2p_a(T)+2.
\]

The marked normal nilpotent ideal is not the whole nilradical: \(C\cap D\) may already have tangential nonreduced structure. A local falsification control has unit determinant, torsion length two and additional normal contribution four, so reduced-marked and full attachment have lengths two and six. It rules out a determinant-only attachment detector without initiating a case enumeration.

The [attachment-module proof](2026-10-27-absorption-attachment-module.md) and [independent audit](2026-10-27-absorption-attachment-module-audit.md) prove the formula even for non-Gorenstein residuals. The non-Gorenstein restriction-length comparison is explicitly reconstructed by Artinian duality.

## 4. A lower witness can move; the full primary component cannot stay flat through a jump

A flat projective family of full \(C\)-primary schemes fixes its Hilbert polynomial, hence its degree and generic multiplicity. It therefore cannot model an absorption jump by itself. In the construction of §2, the full component changes from \(mC\) to \(nC\), while the fixed lower witness \(mC\) remains available. Primary extraction and specialization do not commute there.

For a marked lower thickening with \(I^N\subset J\subset I\), motions preserving the two outer schemes have tangent space

\[
V_T=H^0\mathcal Hom(J/I^N,I/J).
\]

Given actual \(F_a,G_b\in J\), a motion \(\xi\) admits actual homogeneous coefficient corrections precisely when

\[
\bigl(\delta_a(\xi(F)),\delta_b(\xi(G))\bigr)=0
\quad\text{in }H^1(J(a))\oplus H^1(J(b)),
\]

where \(\delta_d\) comes from \(0\to J(d)\to I(d)\to(I/J)(d)\to0\).
This is separate from lifting \(T\) itself and from lifting proposed classes in \(J/IJ\), which uses \(H^1(IJ(d))\).

The [formal lifting note](2026-10-27-absorption-formal-lifting-interface.md) gives the exact incidence tangent sequence, conditional higher Artin steps and a fixed-quartic ribbon control: a genuine three-dimensional family of ribbon motions fails to lift with a degree-two carrier. This tests an explicitly false general inference; it is not a reopened quadric STCI case. Large twists may remove section-lifting obstructions, but they do not make two sections generate \(J\), erase residual components or settle STCI.

The [flag audit](2026-10-27-absorption-flag-tangent-audit.md) covers the tangent and primary-flatness interfaces. The [formal addendum audit](2026-10-27-absorption-formal-addendum-audit.md) and [integration audit](2026-10-27-absorption-integration-audit.md) additionally reconstruct the Artin and fixed-quartic ribbon assertions added to that source. The notation \(\operatorname{Ext}^1_C\), rather than ambient \(\operatorname{Ext}^1_X\), is essential for the ribbon's vanishing obstruction group.

## 5. Characteristic zero has constructive alternatives to inseparable collapse

The conductor comparison in accepted R-0003 already distinguishes finite Frobenius annihilation from characteristic-zero logarithmic descent. This pass preserves that authority and makes its formal limit explicit:

\[
A_N=K+t^NK[[t]],\qquad (1+t)^q\in A_N
\iff p^{v_p(q)}\ge N
\]

in characteristic \(p\), whereas no positive power descends in characteristic zero. A descending exponent at every finite level need not give a single exponent for all levels.

Two other conditional mechanisms deserve attention:

- A finite-order semi-invariant can have an invariant power, with unchanged support. The classical twisted cubic on a quadric cone gives a corrected global square in characteristic zero. It uses a non-Cartier divisor-class relation, not Frobenius.
- Products of distinct actual conductor directions can cancel nonzero logarithmic defects in characteristic zero. Powers of a single fixed divisor ray cannot do that. Positivity, the entire inverse support and actual global sections on the same carrier are essential.

These are constructions or consequences of standard invariant theory and R-0003, not new quartic examples. The [characteristic/conductor note](2026-10-27-absorption-characteristic-conductor-interface.md) and [independent audit](2026-10-27-absorption-characteristic-conductor-audit.md) retain the bounded-index, APic and normalization restrictions. In particular the twisted-cubic benchmark's index-two geometry is not transferable to the fixed quartic.

## 6. Literature changed the interpretation

The [focused discrepancy-paper review](2026-10-27-absorption-discrepancy-literature.md) inspected current primary versions rather than relying on their abstracts. The numerical-invariants paper includes nonreduced CM generically-CI curves, so its full attachment identity applies to \(T\); it must not be dismissed as reduced-only. The families paper proves residual compatibility under a flat full-component-family hypothesis. Absorption deliberately crosses a boundary where that hypothesis fails, so it supplies no automatic commuting-primary-extraction theorem there.

The current proof inputs are standard linear systems and Bertini, linkage/canonical modules, Quot deformation theory, formal groups and divisor/conductor descent. The contribution is their precise constructive integration and the fiberwise attachment bridge, with literal scopes and independent review. No assertion of literature novelty or unrestricted theorem follows.

## 7. Direction after these results

Sextics are now one optional test of a proposed principle. There is no degree-by-degree agenda and no reduction to \((6,6)\).

The next useful general question is when plentiful partial transfer can be completed, with actual equation presentation and full residual gluing retained. Normal global divisor relations and Cartier-index data, and nonnormal full-conductor descent, are precise alternatives; neither is exhausted by a bounded list of equation degrees. Any proposed construction should state:

1. which lower witnesses can remain flat and what happens to the full primary component;
2. which actual section-lifting classes vanish and what still governs generation;
3. how marked attachment, non-lci torsion and normal nilpotent attachment change;
4. which global divisor relation or conductor descent condition could permit total absorption.

The last item remains a substantive construction problem. Partial transfer, a vanishing first-order obstruction, and finite positive-characteristic repairs do not solve it. Positive constructions and scoped capacity bounds are both retained; the characteristic-zero answer is not presumed.

## Review boundary

The [integration audit](2026-10-27-absorption-integration-audit.md) reviews the main synthesis and its source scopes. The subsequent weak normal-carrier Serre construction has separate coverage in §8 of the [deformation audit](2026-10-27-absorption-deformation-audit.md). The attachment, conductor and formal interfaces retain their own independently reconstructed evidence. No accepted result was rerun or rewritten to create these proposals, and no canonical record was promoted.
