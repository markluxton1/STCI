# Intersections containing C: residual geometry, formal visibility, and construction

Date: 2026-10-27. Branch: **codex/intersections-containing-quartic-2026-10-27**, created from **main**. Integration of three research lanes and independent reviews. **All new deductions remain provisional and unpromoted.** This changes research framing and proposed experiments, not the canonical open status.

## The guiding question

For the fixed smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), what do proper intersections of two hypersurfaces containing \(C\) look like, and how can their residual geometry be used to construct particular intersections?

Start with an **actual homogeneous pair** \(F_a,G_b\) having no common surface factor, and write

\[
[V(F_a,G_b)]=m[C]+R,\qquad ab=4m+\deg R.
\]

Study thickness, residual components, attachment schemes, normalization genera, conductor/gluing, and global equation spaces together. The endpoint \(R=0\) is a construction question, with neither existence nor nonexistence assumed. Residual curves have a mathematical role throughout, rather than entering only as contradictions to sole support.

The accepted low-degree boundary [R-0001](../results/quartic_carrier_exclusion.md) remains a premise: any characteristic-zero STCI pair for this fixed curve has both degrees at least five. Its proof need not be rerun, and its exclusion need not organize residual geometry.

## Evidence and authority

| Lane | Output | Independent review | Scope |
|---|---|---|---|
| Global intersections | [All-degree residual and attachment geometry](2026-10-27-global-containing-intersections.md) | [Global audit](2026-10-27-global-containing-intersections-audit.md) | New all-degree deduction; R-0020–0021 plus explicitly reviewed provisional quartic differential/very-ampleness premises |
| Formal geometry | [Visibility and fixed-twist extension](2026-10-27-formal-neighborhood-residual-visibility.md) | [Formal audit](2026-10-27-formal-residual-visibility-audit.md) | Standard G3/Lefschetz consequence; preserves inherited residual detector |
| Positive characteristic | [All-\(\mu_q\) family](2026-10-27-positive-characteristic-construction-interface.md) | [Characteristic audit](2026-10-27-positive-characteristic-interface-audit.md) | Explanatory extension of R-0021 using reviewed historical all-prime construction |
| Integration | [Multiplicity strata and sextic starting locus](2026-10-27-intersection-multiplicity-strata.md) | [Integration audit](2026-10-27-intersections-integration-audit.md) | Fixed-degree finite-jet argument and construction-oriented deductions |

The [literature refresh](2026-10-27-containing-intersections-literature-refresh.md) records primary sources inspected and access gaps. Agreement, a merge, and successful calculations do not promote claims. Canonical records were not edited.

## 1. A flexible residual laboratory

Over algebraically closed characteristic zero, for all \(a,b\ge4\), a general pair containing \(C\) is the reduced union \(C\cup D\), with \(D\) smooth and integral and

\[
\deg D=ab-4,\qquad
g(D)=\frac{(a+b-4)(ab-8)}2,\qquad
\operatorname{length}(C\cap D)=4(a+b)-14.
\]

The numbers are classical liaison and adjunction. The new all-degree deduction in this pass is that the attachment map to
\(\mathbf P H^0(\mathbf P^1,\mathcal O(4(a+b)-14))\) is dominant. A **general** attachment divisor is realized by actual global forms, and on a dense open set with smooth integral residual. This does not prescribe every special divisor or residual isomorphism type.

| Degrees | General residual degree | Genus | Attachments | Supported endpoint arithmetically possible? |
|---|---:|---:|---:|---|
| \((5,5)\) | 21 | 51 | 26 | No: \(4\nmid25\) |
| \((6,6)\) | 32 | 112 | 34 | At \(m=9\); existence open |
| \((5,8)\) | 36 | 144 | 38 | At \(m=10\); existence open |

Sextic pencils have parameter dimension 114 and general attachment-fiber dimension 80. The boundary leaves substantial global equation freedom.

Liaison supplies information the boundary omits: the once-linked residual has Rao module \(k\) concentrated in degree \(a+b-5\). These are diameter-one arithmetically Buchsbaum curves in the same even liaison class as \(C\), after shift. This connects to curve moduli and basic double linkage without classifying curves or constructing a supported endpoint.

When thickness rises, the once-linked curve \((F,G):I_C\) still has degree \(ab-4\) and the displayed arithmetic genus, but may retain \(C\). Removing the **entire** \(C\)-primary component is a different operation, giving residual cycle degree \(ab-4m\). Subtracting \(m[C]\) does not choose an embedded multiple structure for linkage.

## 2. What the formal neighborhood sees

| Retained data | Information |
|---|---|
| Generic transverse algebra over \(k(C)\) | Thickness \(m\), and residual degree if actual degrees are supplied; loses attachments and residual geometry |
| Full embedded completion along all of \(C\) | Attached residual germs and local scheme structure; detects residual existence for an actual proper projective CI using connectedness |
| Full globally glued formal equations in specified ambient twists | Uniquely determines actual homogeneous equations through G3/Lefschetz extension |

The repository already proves

\[
R\ne0\quad\Longleftrightarrow\quad
\exists p\in C:\ e_p(V(F,G))>m,
\]

where \(e_p\) is Hilbert–Samuel multiplicity. A nonempty residual union meets \(C\) by connectedness; an individual residual component may instead connect through other residual components. This detector is inherited, not rediscovered. A generic pure-power transverse algebra can occur with or without a branch at a special point; full completion distinguishes them. Saturation \((F,G):I_C^\infty\) extracts residual germs, whereas a first-normal defect is a different object.

The consequential clarification uses the classical G3 theorem:

\[
H^0(\mathbf P^3,\mathcal O(d))
\simeq H^0(\widehat{\mathbf P^3}_C,\widehat{\mathcal O(d)}).
\]

Once **full globally glued formal sections in prescribed ambient twists** exist, those sections have no further algebraization gap. Producing them from finite jets, arbitrary function-field symbols, or an unlabelled formal ideal is the difficult compatibility/lifting problem.

An STCI of positive degrees \(a,b\) is equivalently such a full twisted formal pair satisfying

\[
I_C^N\subset(\widehat F,\widehat G)\subset I_C
\]

for some \(N\). Mere formal topological support is insufficient: the completion already has underlying space \(C\). This is an exact reformulation with proof, not an existence theorem.

Finite-jet uniqueness also differs from liftability. The accepted conormal gives sufficient injectivity indices \(\lfloor4d/7\rfloor\) outside characteristic two and \(\lfloor2d/3\rfloor\) in characteristic two. Already the section \(s^2t^2\) on \(C\) in twist one cannot extend through all neighborhoods as an ambient linear section. Thus “finite data determine a possible answer” does not mean “finite data extend.”

## 3. Positive characteristic exhibits actual residual absorption

For \(q=3j+4\ell>0\), \(j,\ell\ge0\), put \(i=2j+3\ell\). The proper \((4,q)\) family

\[
S=x_0x_3^3-x_2^4,\qquad
G_q=x_1^q-x_0^i x_2^j x_3^\ell
\]

is flat over \(\mathbb Z\), with dense torus \(\mathbf G_m\times\mu_q\). In characteristic zero it is a reduced union of \(q\) rational quartics. In characteristic \(p\), writing \(q=p^e m_0\), \(p\nmid m_0\), there are \(m_0\) quartic components, each with multiplicity \(p^e\). Taking \(q=p^e\) gives sole reduced support \(C\), generic length \(q\).

Positive-characteristic existence is already known in every prime. The integration identifies the mechanism: torsion in the torus character lattice gives distinct sheets in characteristic zero and connected infinitesimal group schemes in characteristic \(p\); the semigroup condition extends the equation across the projective boundary. This connects toric descent, diagonalizable group schemes, and inseparability.

Odd-characteristic examples have the same conormal \(\mathcal O(-7)^2\) as characteristic zero. The characteristic-two splitting jump is therefore **not necessary** for this construction mechanism.

When the characteristic does not divide \(q\), the linked residual meets \(C\) in \((q+5)p_0+(3q-3)p_\infty\). At \(q=7\), the six separate component contacts sum to 18 at \(p_0\), while intersection with their scheme union has length 12 there. Component lists and pairwise contacts do not determine gluing.

This explains failure of **this binomial construction** in characteristic zero, with no inference against other equations. R-0012 also retains its prescribed marked-family and DVR scope.

## 4. A concrete constructive interface

For fixed degrees, the conditions \(m_C\ge r\) are relatively closed in the proper-pair space: a finite full multiplication matrix of actual normal jets gives coefficientwise minor equations over \(k\). Under specialization staying proper, residual degree can decrease by multiples of four. If \(4\mid ab\), STCI is the closed, possibly empty terminal stratum \(m_C=ab/4\).

Keep three operations separate: deforming residual geometry at fixed \(m_C\); transferring residual mass onto \(C\); and acquiring a common surface factor. Only the second raises thickness within the problem.

For sextics the surjective wedge map

\[
\bigwedge^2 V_6\longrightarrow H^0(\mathbf P^1,\mathcal O(34))
\]

cuts out \(m_C\ge2\) by 35 independent linear equations in Plücker space, restricted to \(\operatorname{Gr}(2,59)\) and the proper open locus. Every projective component has dimension at least 79; no exact dimension or transversality is asserted. The proper pair

\[
F_6=(x_0x_3-x_1x_2)x_0^4,\qquad
G_6=(x_0^2x_2-x_1^3)^2
\]

has exactly \(m_C=2\), residual cycle degree 28. This elementary reducible control is not claimed as a literature novelty. It gives a nonempty thickness locus from which to investigate deformation.

Proposed next experiments:

1. **Study an actual sextic thickness family.** Choose a component or controlled slice of the \(m_C\ge2\) linear section; impose the next full-jet condition \(m_C\ge3\); track properness, factorization, and the residual primary scheme. Seek an exact family or completed component calculation. Continue toward \(m_C=9\) only if intermediate geometry supports it.
2. **Retain the formal equation presentation.** Compute next global lifting classes with actual ambient twists for surviving jets, and saturate at attachments. If a full twisted formal pair with power containment is constructed, apply extension without inventing a further algebraization hurdle.
3. **Use characteristic-\(p\) positive controls.** Compare actual jets and higher relations in odd characteristic as well as two. Ask what could replace the radicial collapse in characteristic zero, allowing a different constructive mechanism.
4. **Check literature at each proposed bridge.** Retrieve the smallest canonical record and its evidence first, then inspect primary sources before claiming novelty or transferring a theorem. Keep projective/affine, characteristic, degree, and carrier assumptions literal.

These are selectable construction experiments. Carrier/conductor, projection-phase, and other approaches remain available when an actual family suggests them. No recurring automation is implied by this plan.

## Interpretation and limits

The residual is simultaneously a global linked curve with cohomological/gluing constraints, a collection of visible attached germs, and a cycle whose mass can specialize onto \(C\). These descriptions complement each other.

New reviewed provisional outputs are all-degree attachment dominance, the precise full-formal presentation interface, the all-\(\mu_q\) residual/thickness family, and the first sextic thickness locus. No terminal sextic stratum was computed, no uniform degree bound was proved, and neither a characteristic-zero STCI pair nor a general nonexistence theorem was obtained.
