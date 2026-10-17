# STCI Research Record

Started: 2026-09-30

This is a lightweight, evidence-labeled record for the research program. It is
not itself proof. Claims are promoted only after their proof or cited source has
been checked.

## Problem reconstruction

### Current repository statement

The root `README.md` asks whether every complete integral one-dimensional
subscheme \(X\subset \mathbf P^3_k\), over an algebraically closed field \(k\), is
the set-theoretic intersection of two surfaces.

In ideal language, with \(S=k[x_0,x_1,x_2,x_3]\) and saturated homogeneous prime
ideal \(I_X\subset S\), the question is whether

\[
  \operatorname{ara}_+(I_X)=2,
\]

meaning that there are homogeneous \(F,G\in S\) with

\[
  \sqrt{(F,G)^{\mathrm{sat}}}=I_X,
\]

equivalently \(X=V_+(F,G)\) as closed sets. Since the repository already
assumes \(k\) algebraically closed, the distinction between \(k\) and \(\bar k\)
is dormant in the main statement but remains important when importing results.

### Scope discrepancy to resolve

The prior archive at `/Users/l6zy/Projects/math-automation-portable` studies the
much narrower special case of a smooth rational quartic curve in
\(\mathbf P^3\). It is therefore evidence about a test case, not the authoritative
statement of the current repository.

### Terminology requiring care

- "Complete, integral subscheme of dimension 1" means a projective integral
  curve, possibly singular; it is stronger than the sometimes-cited question for
  smooth curves only and narrower than variants for connected or arbitrary
  reduced curves.
- "Set-theoretic complete intersection" means two homogeneous equations in
  projective space, not two local equations, not a scheme-theoretic complete
  intersection, and not merely cohomological dimension two.
- Because \(I_X\) has height two, Krull's height theorem gives the lower bound
  \(\operatorname{ara}(I_X)\ge 2\); the problem asks for equality.

### Verified status of the smooth complex subproblem

The statement

\[
  \text{every smooth irreducible }C\subset\mathbf P^3_{\mathbf C}
  \text{ is a set-theoretic complete intersection}
\]

is still open on the checked record as of 2026-09-30.  There is a particularly
sharp certificate of this status: Eisenbud and Harris, *The Practice of
Algebraic Curves* (AMS GSM 250, 2024), Example 3.13 and Proposition 3.14,
discuss the smooth monomial rational quartic

\[
 C_0=[s^4:s^3t:st^3:t^4]
\]

and explicitly describe the question whether its ideal is the radical of two
forms as one of the famous open problems in the theory of curves.  The curve is
smooth in every characteristic: on its two standard charts, the parameter is
respectively \(x_1/x_0\) and \(x_2/x_3\).  Thus an unresolved instance is
already smooth, irreducible, rational, and of degree four.

The subsequent search covered the 2024 residual-intersection literature, the
2025--2026 affine lci literature, and the 2026 toric/binomial literature.  It
found no paper claiming an unrestricted pair of equations for \(C_0\), no
smooth complex counterexample, and no theorem for all smooth complex space
curves.  The 2026 toric result located is confined to binomial arithmetic rank;
it does not decide arbitrary equations.  This is a dated and reproducible
literature assessment, not a logical proof that an unindexed result cannot
exist.

Concentrating substantial effort on the smooth case is therefore justified:

- one smooth counterexample settles P-001 negatively;
- a theorem for all smooth curves is already a major result and isolates the
  remaining difficulty to singularities;
- smoothness supplies a rank-two conormal bundle, finite-flat transverse
  thickenings, normal forms, blowups along a regular center, and the
  Ferrand--Szpiro construction;
- the smallest unresolved example \(C_0\) is explicit enough for exact
  computation.

But smoothness does not make the problem merely local.  P-005 shows that even
for a smooth rational quartic every successful pair must use carrier surfaces
with singular/non-Cartier behavior along the curve.  The affine theorem and
the projective obstruction are separated exactly by P-007 below.  Accordingly,
the research program gives the smooth case high priority without replacing the
general problem by it.

## Initial claim ledger

| Label | Claim | Status | Evidence / action needed |
|---|---|---|---|
| P-001 | The root problem is the general integral-curve question, not only the rational-quartic case. | PROVED (repository interpretation) | Direct comparison of `README.md` and the archive fixture. |
| K-001 | The general characteristic-zero question remains open. | KNOWN / CURRENT SEARCH CHECKED THROUGH 2026-09-30 | Hartshorne--Polini (2019), Hassanzadeh (2024), and a 2026 literature search all describe it as open; no claimed resolution surviving scope checks was found. This is necessarily a literature-search conclusion, not a proof that no unindexed result exists. |
| K-002 | Even the smooth complex case remains open: the monomial smooth rational quartic is an unresolved test case. | KNOWN / CURRENT SEARCH CHECKED THROUGH 2026-09-30 | Eisenbud--Harris (2024), Example 3.13 and Proposition 3.14, explicitly call the two-form radical question for this smooth curve a famous open problem; later searches found no unrestricted resolution. |
| P-002 | Every smooth nondegenerate rational quartic over an algebraically closed field lies on a unique smooth quadric and has type \((1,3)\) or \((3,1)\). | PROVED | Characteristic-free proof below, including the quadric-cone case. |
| P-003 | Every such quartic is cut out set-theoretically by its quadric and two cubics; hence its projective arithmetic rank is at most three. | PROVED | Explicit divisor/lifting proof below. |
| P-004 | The unique quadric cannot occur in any two-equation STCI presentation of the quartic. | PROVED | A degree-\(n\) hypersurface restricts to \((n,n)\), never a positive multiple of \((1,3)\). |
| P-005 | No surface in a hypothetical defining pair can be smooth along the entire rational quartic. | PROVED | Cartier-divisor intersection and adjunction give an impossible quadratic equation. |
| P-006 | For a broad low-genus range, including every smooth rational curve of degree at least three, the first normal forms of a defining pair must have a nontrivial common factor, giving a horizontal curve or multisection after one blowup. | PROVED | Flatness plus the normal-form resultant gives a numerical inequality; proof below. |
| P-007 | For a fixed hyperplane at infinity, projective STCI is equivalent to an affine STCI pair whose leading forms are relatively prime. | PROVED | Homogenization plus unmixedness of a two-hypersurface complete intersection; proof below. |
| P-008 | For the monomial quartic \([s^4:s^3t:st^3:t^4]\), a cubic/quartic pair works in characteristic 3, and explicit pairs work in every positive characteristic. | PROVED | Direct affine-chart and boundary calculation; exact symbolic identities independently checked in characteristics 2, 3, 5, and 7. |
| P-009 | The monomial quartic has normal bundle \(\mathcal O(7)^2\) in characteristic not 2 and \(\mathcal O(6)\oplus\mathcal O(8)\) in characteristic 2. | PROVED | Explicit two-chart conormal transition calculation; determinant and extension class checked symbolically. |
| P-010 | In characteristic zero, no smooth rational quartic admits an embedded primitive triple of type \(\mathcal O(-7)\); in particular none supports a \((3,4)\) complete intersection. | PROVED | Every quartic is the graph of a degree-three map; the \(z^3\) orbit and a surjective marked family \(z^2(z-1)/(z-\lambda)\) exhaust the left-right orbits.  The six Bănică--Forster obstruction cubics have no common zero for any \(\lambda\ne0,1\). Exact identities were independently audited and checked symbolically. |
| P-011 | Every degree-\(<6\) hypersurface singular along an entire smooth rational quartic is divisible by its unique quadric and therefore cannot occur in a defining pair; the first possible genuinely thick carrier has degree six. | PROVED | Use the saturated/symbolic square, restrict to the quadric, compare \((a,a)\) with \(2(1,3)\), and invoke P-004; proof below. |
| P-012 | Every smooth rational quartic over an algebraically closed field of characteristic \(p>0\) is an STCI of degrees \((3,4p)\). | PROVED and independently audited | Internal cuspidal projection plus explicit Frobenius descent on the weighted normalization of the cubic cone; a separate in-run audit checked every hinge, including characteristic two. No theorem of this generality was located in the checked literature. |
| P-013 | In a finite-type family of projective curves, the fibers admitting an STCI presentation of one fixed degree pair form a constructible locus.  Over a one-dimensional arithmetic base with infinitely many closed points (for example a nonempty open subscheme of the spectrum of the ring of integers of a number field), occurrence at infinitely many closed fibers is equivalent to occurrence at the generic fiber and to occurrence at all but finitely many closed fibers. | PROVED after correction | Universal coefficient spaces and two applications of Chevalley constructibility; the earlier wording “over a localized number ring” was too broad, since a semilocal localization can have only finitely many closed points. |
| P-014 | On the cuspidal cubic carriers used in P-012, the minimum exponent and second degree are exact: \((N,d)=(3p,4p)\) for the standard cusp when \(p\ne3\), \((3,4)\) for the standard cusp in characteristic three, and \((9,12)\) for the nonclassical characteristic-three cusp. | PROVED after proof repair and independent audit | Exact semigroup/hyperplane membership criteria for the two normalization rings.  The original \(P\ne R\) coefficient argument failed when \(h(R)=0\); a fixed-coordinate three-case argument using the \(z^N\) or \(z^{N-1}\) coefficient supplies necessity. |
| P-015 | In characteristic zero, a minimum-degree integral carrier that occurs in a defining pair and is generically smooth along a rational quartic canonically compresses to \(eC\sim nH\), where \(e\) is the lcm of its local Cartier orders, \(n=4e/a\ge a\), and \(e\ge a^2/4\). | PROVED | Almost-Cartier local-to-global sequence and torsion-freeness of \(\operatorname{Pic}X/\mathbf ZH\), followed by lifting and the integral-factor minimality argument. |
| P-016 | A hypothetical characteristic-zero \((4,5)\) pair on a smooth rational quartic must be quasiprimitive of exactly one of two numerical types: \((\deg L,\deg D)=(-7,3)\) or \((-6,1)\). | PROVED | Bănică--Forster/Boratyński multiplicity-five lci filtration, complete-intersection Euler characteristic, and the quotient bound from \(N_C^*=\mathcal O(-7)^2\). |
| P-017 | The vector space of sextics singular along a smooth rational quartic has dimension \(23\); modulo the \(18\)-dimensional \(q\)-divisible subspace it is the five-dimensional space \(H^0(Q,\mathcal O_Q(4,0))\). Non-\(q\)-divisible members have exact normal order two, and integral such sextics exist. | PROVED | Exact sheaf sequence on the unique quadric; for \(C_0\), a saturated symbolic-square basis and an explicit irreducible sextic with reduced singular locus exactly \(C_0\) are verified computationally. |
| P-018 | In characteristic zero, two non-\(q\)-divisible sextics both singular along a smooth rational quartic cannot cut out the quartic set-theoretically. | PROVED | Balanced normal bundle makes the exceptional divisor \(\mathbf P^1\times\mathbf P^1\); a common tangent-cone component must meet the \((1,1)\) quadric-direction section and hence forces a common residual ruling line. Independently audited, including vertical and degree-two common factors. |
| P-019 | A degree-six thick carrier in a defining pair is impossible when the reduced inverse image of the quartic on its normalization is irreducible and Cartier. | PROVED under the stated normalization hypothesis | Normal order is two, normalization branch degrees satisfy \(\sum s_i\delta_i=2\), and pullback of the mate forces \(\Gamma^2=16\delta^2/6\notin\mathbf Z\) for \(\delta=1,2\). Split and non-Cartier branches remain. |
| P-020 | If an integral thick sextic has a reduced, content-free split first-normal divisor \((d,1)+(10-d,1)\), then any mate forces, after exchanging the branches, exactly \(d=0\) with branch orders \((m_1,m_2,b)=k(5,1,4)\), or \(d=1\) with \((m_1,m_2,b)=k(11,1,8)\). If the two branches are Cartier on the normalization, neither case can occur. | PROVED under the stated split/no-vertical hypotheses | Intersections only with the Cartier divisors \(H,E\) give the finite reduction, so no smoothness assumption is hidden. Intersecting the mate with the branches then forces the nonintegral values \(\Gamma_1\Gamma_2=19/4\) or \(17/5\). An independent audit found and corrected the stronger but false claim that normality alone makes this intersection equal to ten. |
| P-021 | In the **regular-ratio branch** of a hypothetical characteristic-zero \((4,6)\) presentation, one may replace the sextic by a quadratic multiple of the quartic so that the normal orders are \((1,2)\); in that branch the common horizontal class satisfies \(e\le3\).  In the unrestricted order-\((1,1)\) branch the ratio of first normal forms may have poles, so the former global subtraction and finite list are not universal. | PROVED only for the regular-ratio branch; prior universal claim disproved | The local complete-intersection model \(F=tu+v^6,\ G=u\) over \(k[[t,u,v]]\) has radical \((u,v)\), constant transverse length six, and first-normal ratio \(1/t\).  Nonregular branches require a separate vertical-divisor stratification; their primitive common factor can have \(e\le8\) (with \(e=9\) automatically regular). |
| P-022 | The first-normal image of thick sextics has dimension \(22\), and for \(C_0\) it contains primitive split divisors of every type \((d,1)+(10-d,1)\), \(0\le d\le5\). A split exceptional divisor does not force the ambient sextic to factor. | PROVED / EXACT COMPUTATION | The universal kernel is \(H^0(I_C^{(3)}(6))=kq^3\). Exact row reduction gives eleven equations for the image, explicit representatives of all six split types, and integral sextics of the form \(PQ+\lambda q^3\) with split first normal form. |
| P-023 | A mate-compatible split sextic of type \(d=0\) or \(1\) cannot have a squarefree residual binary quartic. | PROVED under the split/no-vertical and squarefree-residual hypotheses | On a resolution, use Mumford numerical pullbacks and \(K_0=2H-E\), the pullback of the adjunction class. Hodge-index equality forces each of the four disjoint Cartier residual lines to meet the low-degree normalization branch in \((d+1)/4\), contradicting integrality. No smooth-locus hypothesis is needed. Repeated-root residuals remain. |
| P-024 | For the Hartshorne--Polini module \(M=H^2_{I_{C_0}}(S)\), the explicit classes \(u=xz/(qB)\) and \(v=yw/(qB)\) have no common homogeneous cyclic ancestor using constant or linear multipliers; the tempting all-stage \((A,C)\)-lift also does not exist. | PROVED, but not a non-quasi-cyclicity theorem | P-037 supersedes the former degree-two frontier: degrees \(0,1,2,3\) are excluded at every direct-limit stage. Degree four is the first unresolved multiplier degree; P-039 gives a first-symbol survivor and P-043 excludes that explicit family at all stages. |
| P-025 | For \(C_0\), both quasiprimitive multiplicity-five types \((\deg L,\deg D)=(-7,3)\) and \((-6,1)\) are impossible in characteristic zero. | PROVED and independently audited | Type A ends in a nonzero \(H^1(O(-9))\) class.  For type B, the dense final class is \([-128z^{-1}]\), the \(b_0=0\) boundary has a unit obstruction coordinate, and all three points in the formerly missed rank-zero corner fail flatness already at the double-to-triple extension. |
| P-026 | For the **regular-ratio sublocus** of a hypothetical \((4,5)\) pair on \(C_0\), the two quartic first-normal strata, the normalization \(g_1=z^2f_1\), and the seven-variable jet-consistency problem give exact conditional reductions; three one-parameter families in that sublocus are excluded. The normalization is not proved for an arbitrary pair. | PROVED conditionally; prior universal reduction disproved | If \(f_1=hL\) and \(g_1=kL\), the ratio \(k/h\) is generally rational and may have poles at vertical order jumps. The local model \(F=tu+v^5,\ G=u\) realizes the failure. The verifier's ranks and minors remain exact on the normalized sublocus. |
| P-027 | An integral sextic with smooth normalization and clean split conductor over a smooth rational quartic cannot admit an STCI mate. | PROVED under the smooth-normalization and clean-conductor hypotheses | The source double-point formula gives \(K_S+\Gamma_1+\Gamma_2=2H\); adjunction forces \(\Gamma_1\Gamma_2=10\), and the mate intersection equations have no rational positive solution. Extra conductor components, singular normalization, or point-supported noninvertibility are genuine loopholes. |
| P-028 | For the monomial quartic \(C_0\) over an algebraically closed field of every prime characteristic \(p\ge7\), an explicit pair of degrees \((4,p)\) cuts out \(C_0\) set-theoretically. | PROVED and independently checked | Choose \(b,c>0\) with \(3b+4c=p\), put \(a=p-b-c\), and use \(x_0x_3^3-x_2^4\) and \(x_0^a x_2^b x_3^c-x_1^p\). The affine normalization and the boundary point are checked below. |
| P-029 | For an integral curve \(C\subset\mathbf P^3_k\), \(C\) is an STCI iff \(\mathbf P^3\setminus C\) admits a nonconstant morphism to \(\mathbf P^1\), equivalently iff some positive line bundle \(O_U(d)\) is generated by two global sections. | PROVED after proof repair and independent audit | The class-group localization sequence and regularity give \(\operatorname{Pic}(U)\simeq\mathbf Z\); reflexive sections extend across codimension two. Before invoking purity of the common zero scheme one must prove the extended forms have no common factor. The Rees-graph statement uses the resulting regular-sequence/linear-type property. |
| P-030 | Under the split/no-vertical hypotheses of P-020 and P-023, residual binary-quartic root multiplicities are forced to be \([4]\) for \(d=0\), and \([4]\) or \([2,2]\) for \(d=1\). | PROVED and independently checked | Group the whole Cartier cluster over each distinct residual ruling root of multiplicity \(\mu\). Hodge proportionality gives branch intersection \(\mu/4\) for \(d=0\) and \(\mu/2\) for \(d=1\); integrality forces \(4\mid\mu\) or \(2\mid\mu\). |
| P-031 | In characteristic zero, the nonregular first-normal quotients in degrees \((4,5)\) and \((4,6)\) admit exact finite divisor stratifications.  The provisional seven type-B \((4,5)\) strata collapse under P-038 and are then excluded by P-040.  The preliminary 36 nonregular \((4,6)\) strata collapse under P-042 to 15 with horizontal degree \(e=0\) or \(1\). | PROVED as a reduction, not an exclusion | Write \(H=(h)_0=A+P\), \(K=(k)_0=A+Z\), where \(P\) is the pole divisor of \(k/h\).  Jaffe's characteristic-zero no-common-singularity theorem forces \(c=\deg A\ge1\).  Modulo generator change, the quotient is a finite principal-part space on \(H\). |
| P-032 | On any integral carrier \(X\), existence of a mate is equivalent to an effective Cartier divisor \(A=\sum_i m_i\Gamma_i\), with every \(m_i>0\), on the normalization, supported exactly over \(C\), whose canonical section descends through the full conductor square.  In characteristic zero, the numerical Cartier-index compression of P-015 extends to singular integral \(C\) whenever a minimum carrier \(X\) is regular at the generic point of \(C\). | PROVED after independent audit and module-level repair | The normalization exact sequence detects section descent, ambient restriction is surjective because \(H^1(\mathbf P^3,O(n))=0\), and intersection gives \(ab=\deg(C)\sum m_i\delta_i\).  A former torsion-free-module reformulation omitted factorization through \(O_X\); the corrected intersection module below retains exactly that conductor condition. |
| P-033 | Let \(C\) be integral of degree \(\delta\). If \(F,G\) have positive degrees \(a,b\), no common factor, and \(\delta\mid ab\), then \(V(F,G)_{\mathrm{red}}=C\) iff their universal-line resultant is \(\lambda\operatorname{Ch}_C^{ab/\delta}\).  For \(C_0\), its Pluecker-coordinate Chow form is the explicit 10-term quartic below. | KNOWN criterion, specialized and exactly computed here; independently audited | The twisted pushforward of the universal-line Koszul complex is the Sylvester bundle map; its determinant is the Chow form of the complete-intersection cycle.  This is a classical reformulation and computational certificate, not a new existence theorem. |
| P-034 | For \(U=\mathbf P^3\setminus C\), with \(C\) integral of degree \(\delta\) over an algebraically closed field, \(K_0(U)\simeq\mathbf Z[u]/(u^3,\delta u^2)\).  The \(K_0\) relation forced by a degree-\((a,b)\) Koszul pair is exactly \(\delta\mid ab\). | PROVED and independently audited | Localization from \(G_0(C)\) kills \(u^3\) and \(\delta u^2\).  This is only the ordinary \(K_0\) shadow of a pair; it is necessary and nowhere near sufficient. |
| P-035 | \(C\) is an STCI iff it supports a homogeneous \(I_C\)-primary height-two ideal \(J\) for which \(S/J\) is graded Gorenstein, equivalently an arithmetically Gorenstein codimension-two thickening. | KNOWN / classical; rederived and independently audited | A defining pair gives a graded complete intersection.  Conversely, Hilbert--Burch plus Gorenstein type one forces a height-two perfect ideal to have two generators.  Merely local or generic Gorensteinness is insufficient. |
| P-036 | A single Schubert-line pencil excludes every quartic in the 13-dimensional space \(I_{C_0}(4)\cap(x_1,x_2x_3,x_3^2)_4\) and every quintic in the 28-dimensional space \(I_{C_0}(5)\cap(x_1,x_3^2,x_2^2x_3)_5\) from any \((4,5)\) STCI pair; the coordinate-reversed spaces are excluded as well. | PROVED, exactly computed, and independently audited | On the pencil \([\gamma U:0:V:\beta U]\), a pair requires resultant \(\mu\beta^5\gamma^{15}\).  Dividing the forced \(\beta\)-factor still leaves a shared \(V\)-root of multiplicity at least one or two, so the resultant has \(\beta\)-order at least six.  An explicit irreducible quartic and quintic pass this pencil exactly but fail the reversed pencil, proving that one pencil alone is not exhaustive. |
| P-037 | Over an algebraically closed field of characteristic zero, P-024's classes \(u=xz/(qB)\) and \(v=yw/(qB)\) have no common homogeneous cyclic ancestor with multipliers of degree at most three. Any surviving equal-degree pair has degree at least four, lies in \(I_{C_0}\), and has proportional first conormal symbols. | PROVED and independently audited; still not non-quasi-cyclicity | A finite-Laurent completion at every zero of the common restriction factor forces both multipliers into \(I\).  Generically independent first symbols would give a nonzero section of \(O(9-4d)^2\); the cubic rank-one locus is exactly scalar pairs or pairs divisible by \(q\), both impossible. |
| P-038 | For every hypothetical type-B \((4,5)\) complete intersection on \(C_0\), the first-normal common vertical divisor is exactly twice the Bănică--Forster defect divisor: \(A=2D\) scheme-theoretically. Hence P-031's seven nonregular type-B strata collapse to \((c,p_{\mathrm{pole}},\deg Z)=(2,6,10)\). | PROVED and independently audited; reduction, not exclusion | The divisor-valued Fitting ideal of the first-normal cokernel is both \(O_C(-A)\) and \(O_C(-2D)\).  The local extension calculation gives \(\operatorname{Im}(I_4\to J/J^2)=M(-2D)\).  The available Bănică--Forster reprint drops an \(x\) in one generator; the flat corrected formula is recorded below. |
| P-039 | The degree-four rank-one conormal locus left by P-037 contains ambient-coprime, nonconstant-ratio pairs.  Explicitly, for \(\lambda\ne0\), \(F_\lambda=xA+\lambda y^2q\) and \(G_\lambda=yA+\lambda xzq\) are coprime and have first-symbol ratio \(t\). | PROVED / exact counterexample to a proposed shortcut | In the affine conormal frame \((A,q)\), their rows are \((1,\lambda t^2)\) and \((t,\lambda t^3)\).  Exact identities force every common factor to divide \(\gcd(A,yq)=1\).  P-043 proves that this entire candidate family nevertheless fails the higher direct-limit equations. |
| P-040 | Over an algebraically closed field of characteristic zero, the monomial smooth rational quartic \(C_0=[s^4:s^3t:st^3:t^4]\) has no set-theoretic complete-intersection presentation of degree \((4,5)\). | PROVED and independently audited | Any such pair would give a quasiprimitive multiplicity-five curve of one of P-016's two types. P-025 now excludes both types on every parameter chart. This is a new degree-pair exclusion within the project, not a non-STCI theorem. |
| P-041 | Under the split/content-free/no-vertical hypotheses of P-020 and P-030, every surviving residual quartic is a square and the sextic has form \(F=T^2+qK\) with \(T\in I_C(3)\), \(K\in I_C(4)\); every selected residual-root point is singular on the first strict transform.  For \(C_0\), a \(d=1,[4]\) root at either totally ramified ruling is impossible. | PROVED under the stated hypotheses and independently audited | A mate with scale \(k\) makes only \(4k\Gamma_{\mathrm{low}}\) or \(10k\Gamma_{\mathrm{low}}\) Cartier.  Cancelling \(k\) is invalid in torsion local class groups: an ordinary \(A_3\) two-simple allocation merely forces \(k\) even.  No broader ordinary-singularity exclusion is claimed. |
| P-042 | A hypothetical characteristic-zero \((4,6)\) pair on \(C_0\) is a quasiprimitive multiplicity-six lci whose Bănică--Forster pieces have the necessary shape \(O,L,L^2(D_2),L^3(D_3),L^4(D_2+D_3),L^5(D_2+D_3)\), with \(0\le D_2\le D_3\).  Exactly seven numerical types survive P-010. | PROVED as a necessary classification and independently audited | Gorenstein duality, \(\chi(O_X)=-72\), and \(O(-7)^2\twoheadrightarrow L\) give \(5\deg L+\deg D_2+\deg D_3=-26\) and \(\deg L=-7\) or \(-6\).  The horizontal degree is \(e=\deg L+7\), reducing P-031's nonregular \((4,6)\) list from 36 to 15 strata with \(e=0\) or \(1\).  No existence is asserted. |
| P-043 | For every \(\lambda\), the degree-four P-039 multiplier pair \(F_\lambda=xA+\lambda y^2q\), \(G_\lambda=yA+\lambda xzq\) has no common homogeneous ancestor for \(u=xz/(qB)\), \(v=yw/(qB)\), at any direct-limit stage. | PROVED and independently audited; family exclusion only | At every stage \(N\ge2\), two sparse coefficient functionals annihilate the \((q^N,B^N)\) correction ideals and all pairs \((F_\lambda h,G_\lambda h)\), but take value \(-1\) on the target pair.  The identities are integral in \(N,\lambda\) and transition-compatible.  Other degree-four and higher multiplier pairs remain open, so this is not a non-quasi-cyclicity theorem. |
| A-004 | First-blow-up / normal-factor numerics may obstruct a two-surface presentation. | PARTLY PROMOTED TO P-006 | The formerly missing flatness/resultant step is supplied in P-006; iteration beyond the first blowup remains open. |

## Research lanes used in this run

1. Current literature and precise status of the general problem.
2. Cohomological, étale, Picard, and arithmetic-rank obstructions.
3. Smooth rational quartics and their exact geometry.
4. Positive-characteristic mechanisms.
5. Audit and deduplication of the 24 prior research responses.
6. Symbolic verification of explicit quartic equations.
7. Multiple structures, blowups, normal bundles, and intersection numerics.
8. Alternative formulations (bundles, divisors, complements, liaison, Rees/blowup).

## Results proved in the current run

### P-002: characteristic-free geometry of a smooth rational quartic

Let \(C\simeq\mathbf P^1\subset\mathbf P^3_k\) be smooth, nondegenerate, and
of degree four, with \(k\) algebraically closed of arbitrary characteristic.

1. Since \(h^0(\mathbf P^3,\mathcal O(2))=10\) and
   \(h^0(C,\mathcal O_C(2))=h^0(\mathbf P^1,\mathcal O(8))=9\), at least one
   quadric contains \(C\).
2. There cannot be two independent quadrics. If they shared a plane
   component, integrality and nondegeneracy of \(C\) would force \(C\) into a
   plane or line. Otherwise their complete intersection \(Y\) has Hilbert
   polynomial \(4n\), whereas \(C\) has Hilbert polynomial \(4n+1\). The
   inclusion \(C\subset Y\) would give
   \(0\to K\to\mathcal O_Y\to\mathcal O_C\to0\), with \(K\) of finite length
   because both curves have degree four, and hence the impossible equality
   \(4n=4n+1+\operatorname{length}K\).
3. The unique quadric \(Q\) is integral: a reducible or doubled plane cannot
   contain an integral nonplanar curve.
4. It is not a quadric cone. This includes characteristic two: after putting a
   singular point at \([0:0:0:1]\), the value and first-derivative conditions
   show directly that the quadratic form involves only \(x_0,x_1,x_2\).
   Since it is integral, the resulting plane conic is irreducible and hence
   smooth over the algebraically closed field. Thus every integral singular
   quadric is the cone over a smooth conic. Resolve it by
   \(\pi:\mathbf F_2\to Q\), with exceptional section \(E^2=-2\), ruling \(f\),
   and pullback hyperplane \(H=E+2f\). If \(\widetilde C\sim aE+bf\), then
   \(b=H\cdot\widetilde C=\deg C=4\), while
   \(E\cdot\widetilde C=4-2a\) is even. If \(C\) avoids the vertex this
   intersection is zero. If it passes through the vertex, then
   \(\mathfrak m_v\mathcal O_{\mathbf F_2}=\mathcal O_{\mathbf F_2}(-E)\),
   while its pullback to the smooth branch is the maximal ideal of that point.
   The strict transform is the blowup along an invertible ideal and is
   isomorphic to \(C\), so \(E\cdot\widetilde C=1\), impossible by parity. In
   the former case \(\widetilde C=2E+4f=2H\), and adjunction on
   \(\mathbf F_2\) gives \(p_a(\widetilde C)=1\), contradicting
   \(\widetilde C\simeq C\simeq\mathbf P^1\).
5. Hence \(Q\simeq\mathbf P^1\times\mathbf P^1\). Write
   \(C\sim(a,b)\). Nondegeneracy and integrality give \(a,b>0\);
   \(a+b=\deg C=4\), and adjunction gives
   \(0=g(C)=(a-1)(b-1)\). Therefore \((a,b)=(1,3)\) or \((3,1)\).

### P-003: an explicit three-equation presentation

Assume \(C\sim(1,3)\) after exchanging the rulings. On \(Q\), the ideal of
\(C\) is \(\mathcal O_Q(-1,-3)\). A cubic hypersurface restricts to
\(\mathcal O_Q(3,3)\), so cubics through \(C\), modulo the quadric equation,
correspond to

\[
H^0\!\left(Q,\mathcal O_Q(2,0)\right).
\]

Choose two binary quadratics in this three-dimensional space with no common
zero (for example the squares of the two ruling coordinates). Multiplying
them by the defining section of \(C\) gives two sections of
\(\mathcal O_Q(3,3)\) whose common zero set is exactly \(C\). The restriction
map

\[
H^0(\mathbf P^3,\mathcal O(3))\longrightarrow
H^0(Q,\mathcal O_Q(3,3))
\]

is surjective, because its kernel sequence has
\(H^1(\mathbf P^3,\mathcal O(1))=0\). Lift the two sections to cubic forms
\(F,G\). If \(q\) defines \(Q\), then

\[
V_+(q,F,G)=C.
\]

Thus \(\operatorname{ara}_+(I_C)\le 3\) in every characteristic. The same
argument also shows that \(I_C\) is generated by \(q\) and three cubic forms:
the full three-dimensional space \(H^0(Q,\mathcal O_Q(2,0))\) globally
generates the residual line bundle.

### P-004: why the quadric cannot be one of two equations

If \(C=V_+(q,H)\), then on \(Q\) the divisor of \(H|_Q\) has support \(C\);
because \(Q\) is smooth and \(C\) is prime, it equals \(mC\) for some
\(m>0\). But a degree-\(n\) hypersurface restricts to class \((n,n)\), whereas
\(mC\) has class \((m,3m)\). This is impossible. Any two-equation solution
must therefore use a different, necessarily singular/non-Cartier carrier
mechanism.

### P-005: a smooth-carrier obstruction

Suppose a surface \(S=(F=0)\) of degree \(a\) in a hypothetical defining
pair is smooth at every point of \(C\), and the other surface has degree
\(b\). This already reduces to one reduced component near \(C\). Indeed, if
\(F=\prod F_i^{e_i}\), each projective surface \(V(F_i)\) meets the other
hypersurface in a curve; because the total set-theoretic intersection is
\(C\), every such component must contain \(C\). Two distinct components, or a
repeated component, would make \(F\) singular along \(C\). On the resulting
integral surface \(S\), the other equation cuts a divisor with support \(C\),
hence \(mC\) for some \(m>0\). Intersecting first with a hyperplane and then
with \(C\) gives

\[
ab=4m,
\qquad
b\deg C=mC^2,
\qquad
C^2=\frac{16}{a}.
\]

Adjunction is valid in a neighborhood of \(C\), and
\(K_S=(a-4)H|_S\). Since \(g(C)=0\), it yields

\[
-2=C^2+K_S\cdot C=\frac{16}{a}+4(a-4),
\]

or

\[
4a^2-14a+16=0.
\]

Its discriminant is \(-60\), a contradiction. Thus each defining hypersurface
is singular at at least one point of \(C\). This does not say that it is
singular at the generic point.

### P-006: persistence of an infinitely-near horizontal normal factor

The following argument applies more generally. Let \(C\subset\mathbf P^3\)
be a smooth curve of degree \(d\) and genus \(g\). Suppose degree-\(a\) and
degree-\(b\) forms cut it out set-theoretically. At the generic point of
\(C\), let their orders in the normal ideal be \(r,s>0\). Their first normal
forms are binary forms

\[
f_r\in H^0\!\left(C,\operatorname{Sym}^rN_C^*\otimes
\mathcal O_C(a)\right),
\quad
g_s\in H^0\!\left(C,\operatorname{Sym}^sN_C^*\otimes
\mathcal O_C(b)\right).
\]

These are genuinely global sections.  Indeed, because \(C\) is a regular
embedding,
\(\mathcal I_C^j/\mathcal I_C^{j+1}\simeq
\operatorname{Sym}^jN_C^*\) is locally free.  If any lower normal class of
one of the equations vanishes at the generic point, it vanishes globally;
induction puts that equation in the corresponding sheaf power.  At a special
point its order may therefore increase, but it cannot decrease.

Assume for contradiction that \(f_r,g_s\) are relatively prime over
\(k(C)\).  Fix \(p\in C\) and choose completed coordinates

\[
 \widehat{\mathcal O}_{\mathbf P^3,p}=k[[t,u,v]],\qquad
 \mathcal I_{C,p}=(u,v),\qquad \widehat{\mathcal O}_{C,p}=k[[t]].
\]

For the completed local equations \(A_p,B_p\), the hypothesis that the
set-theoretic intersection is \(C\) says
\(\sqrt{(A_p,B_p)}=(u,v)\).  Hence
\(k[[t,u,v]]/(A_p,B_p)\) is finite over \(k[[t]]\).  The two equations have
height two in the regular local ring, so they form a regular sequence; the
quotient is one-dimensional Cohen--Macaulay with the unique minimal prime
\((u,v)\).  Thus \(t\) is a nonzerodivisor.  The quotient is a finite
torsion-free, hence free, module over the DVR \(k[[t]]\), and its transverse
fiber length is constant.

Over \(k((t))\), coprimality of the initial binary forms makes that length
exactly \(rs\).  At the special point, plane intersection multiplicity is at
least the product of the two orders, hence at least \(rs\); equality holds
only when both orders remain \(r,s\) and their initial forms are relatively
prime.  Constancy forces equality at every point.  The resultant is therefore
nowhere zero on \(C\).

That resultant is a nowhere-vanishing section of

\[
(\det N_C^*)^{rs}\otimes\mathcal O_C(a)^s
\otimes\mathcal O_C(b)^r.
\]

Consequently its degree is zero. Bézout and the resultant degree give

\[
ab=drs,
\qquad
d(as+br)=(4d+2g-2)rs.
\]

Writing \(x=a/r\) and \(y=b/s\), one obtains

\[
xy=d,
\qquad
x+y=4+\frac{2g-2}{d}.
\]

The arithmetic--geometric mean inequality now shows that generic relative
primality is impossible whenever

\[
4+\frac{2g-2}{d}<2\sqrt d.
\]

In that range the strict transforms of the two defining surfaces must still
share a curve dominating \(C\) inside \(\mathbf P(N_C)\) after the first
blowup. For a rational quartic the two sides are \(7/2\) and \(4\), so the
obstruction applies. More generally it applies to every smooth rational curve
of degree at least three. The twisted cubic provides a useful sanity check:
its known quadric--cubic presentation indeed has excess tangency and generic
intersection multiplicity two. An elliptic quartic is the boundary equality
case and its transverse \((2,2)\) complete-intersection presentation realizes
\(x=y=2\).

This is a structural restriction, not a disproof: the horizontal common curve
or multisection in the exceptional ruled surface may persist through further
blowups, and positive-characteristic Frobenius constructions show that such
persistence can end in a valid presentation.

### P-007: an exact affine-to-projective boundary criterion

Let \(C\subset\mathbf P^3\) be an integral curve, let
\(H=(x_0=0)\) be a hyperplane not containing it, and put
\(C^\circ=C\cap D_+(x_0)\subset\mathbf A^3\).  For polynomials
\(f,g\in k[y_1,y_2,y_3]\), write \(F,G\) for their ordinary
homogenizations and \(f_{\rm top},g_{\rm top}\) for their top homogeneous
parts.  Then

\[
 C=V_+(F,G)
\quad\Longleftrightarrow\quad
 \left\{
 \begin{array}{l}
 C^\circ=V_{\mathbf A^3}(f,g),\\
 \gcd(f_{\rm top},g_{\rm top})=1.
 \end{array}
 \right.
\]

Here equality means equality of closed sets.  The forward implication is
immediate after dehomogenizing: a common nonconstant factor of the two leading
forms would define a curve in \(H\) contained in \(V_+(F,G)=C\), whereas
\(C\cap H\) is finite.

Conversely, the affine equality implies that \(f,g\), hence \(F,G\), have no
common hypersurface factor.  Thus \(V_+(F,G)\) is a codimension-two complete
intersection and is unmixed of dimension one.  Every irreducible component not
contained in \(H\) meets the affine chart, where its support is contained in
the integral curve \(C^\circ\); its closure is therefore \(C\).  A component
contained in \(H\) would be a plane curve on which both leading forms vanish,
contrary to their relative primality.  Unmixedness rules out an isolated
set-theoretic point at infinity.  Hence the only component is \(C\).

For a smooth curve, Ferrand--Szpiro supplies an affine STCI pair on
\(C^\circ\).  P-007 identifies exactly what that existence theorem does not
give: control of the leading forms so that no curve is created at infinity.
Equivalently, the global projective problem is the problem of choosing an
affine pair with relatively prime boundary data.

There is a related, but not equivalent, vector-bundle construction.  Ferrand
constructs a double structure supported on a projective lci curve as the zero
scheme of a section of a rank-two bundle \(E\) on \(\mathbf P^3\).  On
\(\mathbf A^3\), vector bundles are free, so the restricted section has two
polynomial components.  If this particular projective bundle splits, its
section gives two homogeneous equations; Horrocks' criterion tests that
splitting.  But an affine trivialization forgets the transition data across
the hyperplane at infinity, and homogenizing its components generally defines
a different projective extension.  Moreover, a projective STCI pair may
support a multiple structure of multiplicity greater than two.  Therefore
splitting the chosen Ferrand bundle is a sufficient route for its particular
double, not an equivalent formulation of projective STCI.  The exact general
boundary condition remains the relatively-prime-leading-form criterion above.

For the monomial quartic this defect is completely visible.  Write its affine
chart \(x_0=1\) as

\[
 x_2=x_1^3,\qquad x_3=x_1x_2.
\]

These two equations generate the affine ideal scheme-theoretically.  Their
minimal homogenizations are

\[
F=x_0^2x_2-x_1^3,\qquad G=x_0x_3-x_1x_2.
\]

The leading parts \(-x_1^3\) and \(-x_1x_2\) share \(x_1\), and indeed

\[
V_+(F,G)=C_0\cup V_+(x_0,x_1).
\]

Saturation by \(x_0\) removes this line and recovers \(I_{C_0}\), but that
saturation is the automatic closure identity and is not an STCI certificate.
More generally, no affine pair that generates the reduced affine ideal
scheme-theoretically can solve the projective quartic problem: if its leading
forms were coprime, its projective complete-intersection closure would be
generically reduced along \(C_0\); Cohen--Macaulay purity would then make it
the reduced curve scheme-theoretically, contradicting that \(C_0\) is not a
projective complete intersection.  A successful affine radical pair must
encode a nonreduced thickening.

The multiplicity-two Ferrand construction also cannot split for a smooth
rational quartic.  A split complete-intersection double would have
\(ab=2\deg C=8\).  Nondegeneracy excludes \((1,8)\), leaving \((2,4)\).
The quadric is unique; on it, a quartic section has class \((4,4)\), whereas
the cycle \(2C\) has class \((2,6)\) up to exchanging rulings.  Hence no
\((2,4)\) complete-intersection double exists.  Ferrand's guaranteed bundle
must therefore be indecomposable in this case, and any STCI presentation must
have generic multiplicity at least three.

## Computations

### P-008: exact positive-characteristic presentations of the monomial quartic

Let

\[
C_0=[s^4:s^3t:st^3:t^4]
\]

and put

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,\\
A&=x_1^3-x_0^2x_2,\\
B&=x_1^2x_3-x_0x_2^2,\\
D&=x_2^3-x_1x_3^2.
\end{aligned}
\]

Elimination on the two parameter charts, or the verified Hilbert--Burch
resolution, gives

\[
 I_{C_0}=(q,A,B,D).
\]

In characteristic three,

\[
 \sqrt{(A,\;x_0x_3^3-x_2^4)}=I_{C_0}.
\]

Indeed, on \(x_0=1\), the first equation gives \(x_2=x_1^3\), and the
second gives \((x_3-x_1^4)^3=0\); injectivity of Frobenius on a field gives
the affine parametrized curve.  At \(x_0=0\), the equations successively force
\(x_1=x_2=0\), leaving only the endpoint \([0:0:0:1]\).

There is also a uniform construction in every characteristic \(p>0\).  Choose
\(e=3\) for \(p=3\), and \(e=3p\) otherwise, and set \(N=4e/3\).  For
\(0\le j\le e\), put

\[
n_j=4(e-j),\qquad
b_j\equiv n_j\pmod 3,\quad 0\le b_j<3,
\]

\[
c_j=(n_j-b_j)/3,\qquad
a_j=N-b_j-c_j-j.
\]

The only negative exponent is \(a_1=-1\), but its coefficient
\(\binom e1=e\) vanishes in characteristic \(p\).  Therefore

\[
G_e=\sum_{\substack{0\le j\le e\\j\ne1}}
(-1)^{e-j}\binom ej
x_0^{a_j}x_1^{b_j}x_2^{c_j}x_3^j
\]

is a homogeneous form of degree \(N\).  Modulo \(A\), one has the exact
identity

\[
 q^e=x_0^{2e/3}G_e.
\]

On \(x_0=1\), this says \(G_e=(x_3-x_1^4)^e\).  On \(x_0=0\), the
\(j=0\) term becomes a nonzero scalar multiple of \(x_2^N\), so no boundary
line is introduced.  Consequently

\[
 \sqrt{(A,G_e)}=I_{C_0}.
\]

The degrees are \((3,4)\) in characteristic three and \((3,4p)\) otherwise.
The derivation is a proof; a separate exact-arithmetic script checked the
homogeneity, identity, boundary term, and power containments for
\(p=2,3,5,7\).  The computation also found the smaller characteristic-two
pair

\[
\sqrt{(x_1^4-x_0^3x_3,\;x_2^4-x_0x_3^3)}=I_{C_0}.
\]

### P-009: characteristic jump in the normal bundle of \(C_0\)

This calculation closes an uncertainty in the prior archive.  On the
\(x_0\ne0\) chart write the curve as

\[
y=u,\qquad z=u^3,\qquad w=u^4,
\]

with conormal generators \(a=z-y^3\), \(b=w-y^4\).  On the \(x_3\ne0\)
chart put

\[
\alpha=Y-Z^3,\qquad\beta=X-Z^4.
\]

Modulo the square of the curve ideal, direct substitution on the overlap gives

\[
\binom{\alpha}{\beta}=
\begin{pmatrix}
-3u^{-6}&2u^{-7}\\
-4u^{-7}&3u^{-8}
\end{pmatrix}
\binom a b,
\qquad \det=-u^{-14}.
\]

Use the quadric conormal generator \(q_s=b-ua\), for which
\(q_t=u^{-8}q_s\), and take \(r_s=a,r_t=-\alpha\).  Then

\[
r_t=u^{-6}r_s-2u^{-7}q_s.
\]

Thus the extension class of

\[
0\longrightarrow\mathcal O(-8)
\longrightarrow N^*_{C_0/\mathbf P^3}
\longrightarrow\mathcal O(-6)
\longrightarrow0
\]

is represented by \(-2u^{-1}\in H^1(\mathcal O(-2))\).  It is nonzero
unless the characteristic is two.  Hence

\[
N_{C_0/\mathbf P^3}\cong
\begin{cases}
\mathcal O(7)\oplus\mathcal O(7),&\operatorname{char}k\ne2,\\
\mathcal O(6)\oplus\mathcal O(8),&\operatorname{char}k=2.
\end{cases}
\]

The transition identities and determinant were verified independently by exact
symbolic expansion.  In characteristic three, they also identify the
\((3,4)\) complete intersection above as a globally primitive triple:
locally its ideal is \((a,b^3)\) on the first chart and
\((\beta,\alpha^3)\) on the second, with

\[
\operatorname{gr}\mathcal O_X
=\mathcal O_C\oplus\mathcal O_C(-7)\oplus\mathcal O_C(-14).
\]
Its arithmetic genus is therefore \(19\), as required for a \((3,4)\)
complete intersection.

### P-010: a second-neighborhood obstruction for the monomial quartic

This result is independent of, and stronger in the formal-neighborhood
direction than, the already known exclusion of cubic carriers for \(C_0\): it
excludes every embedded primitive triple of the type forced by a \((3,4)\)
complete intersection, whether or not that triple is generated by global
equations of degrees three and four.

First, any \((3,4)\) complete intersection \(X\) supported on a smooth rational
quartic would be primitive everywhere.  At a point of the curve, complete the
ambient local ring as

\[
k[[t,x,y]],\qquad I_C=(x,y).
\]

The quotient by the two equations is finite over \(k[[t]]\), is a
one-dimensional Cohen--Macaulay ring with a unique associated prime, and is
therefore torsion-free and finite free over the DVR.  Its rank is
\(3\cdot4/4=3\).  Every transverse fiber is consequently a length-three Artin
complete intersection and hence Gorenstein.  Such a local algebra cannot have
embedding dimension two: then its Hilbert function would be \((1,2)\), its
square of the maximal ideal would vanish, and its socle would have dimension
two.  It is therefore \(k[\epsilon]/(\epsilon^3)\).  A local linear combination
\(H\) of the two equations has nonzero normal differential.  The surface
\(S=(H=0)\) is regular, and \(C\) is the Cartier divisor \((v=0)\) in the
two-dimensional regular local UFD \(\mathcal O_{S,p}\).  The other local
generator \(K\) has radical \((v)\), so unique factorization gives
\(K=\text{unit}\cdot v^n\).  The transverse length is three, hence \(n=3\),
and after changing coordinates

\[
 I_X=(u,v^3)
\]

inside that smooth surface.  Thus the triple is primitive at every point, with
no finite exceptional defects.

If \(L\) is its type line bundle, then

\[
\operatorname{gr}\mathcal O_X
=\mathcal O_C\oplus L\oplus L^2.
\]

Complete-intersection adjunction gives

\[
\omega_X|_C=\mathcal O_C(3)=\mathcal O_{\mathbf P^1}(12),
\]

while the primitive-triple formula gives
\(\omega_C\otimes L^{-2}\).  Thus

\[
 \mathcal O_{\mathbf P^1}(12)
 =\mathcal O_{\mathbf P^1}(-2)\otimes L^{-2}.
\]

Since \(\operatorname{Pic}(\mathbf P^1)\simeq\mathbf Z\) has no two-torsion,
\(L=\mathcal O(-7)\).  In characteristic zero every smooth rational quartic
has \(N_C^*=\mathcal O(-7)^2\), by the normal-bundle theorem of
Eisenbud--Van de Ven, so quotients to \(L\) exist and first-order data alone
do not obstruct the triple.

For \(C_0\), make the calculation intrinsic to the two standard embedded
charts.  On \(x_0\ne0\), put \(z=x_1/x_0\) and

\[
 a=x_2/x_0-z^3,\qquad b=x_3/x_0-z^4.
\]

On \(x_3\ne0\), put \(w=x_2/x_3\) and

\[
 a'=x_1/x_3-w^3,\qquad b'=x_0/x_3-w^4.
\]

On the overlap the exact coordinate changes include

\[
 w=\frac{z^3+a}{z^4+b},\qquad
 a'=\frac{z}{z^4+b}-w^3,\qquad
 b'=\frac1{z^4+b}-w^4.
\]

Choose the split conormal frames

\[
 u=b-\frac32za,\quad v=a,\qquad
 u'=\frac12a',\quad v'=-3wa'+2b'.
\]

Direct expansion of the exact changes through order two gives

\[
\begin{aligned}
u'={}&z^{-7}u-\frac52z^{-11}u^2-3z^{-10}uv-\frac38z^{-9}v^2,\\
v'={}&z^{-7}v+3z^{-12}u^2-z^{-11}uv-\frac94z^{-10}v^2
\end{aligned}
\pmod{I_C^3}.
\]

Every quotient \(N_C^*\twoheadrightarrow\mathcal O(-7)\) is parametrized by
a kernel line in \(\mathbf P^1\).  For the finite chart take
\(m=u+\theta v\), \(\ell=v\); the corresponding Ferrand double has ideal
\((m,\ell^2)\).  Bănică--Forster Proposition 2.4 says it extends to a primitive
triple exactly when

\[
0\longrightarrow L^2\longrightarrow
\nu_{C_2}|_C\longrightarrow M\longrightarrow0
\]

splits.  The Čech class of this extension is

\[
h_\theta=3\left(
\theta^3z^{-5}-\frac12\theta^2z^{-4}
+\frac14\theta z^{-3}-\frac18z^{-2}
\right)
\in H^1(\mathcal O(-7)).
\]

In the standard basis \(z^{-1},\ldots,z^{-6}\), its \(z^{-2}\) coefficient
is \(-3/8\), so it is nonzero for every finite \(\theta\) in characteristic
zero.  The missing kernel line, represented by \(m=v,\ell=u\), has class
\(3z^{-5}\ne0\).  These cases exhaust the quotient projective line.  Hence no
Ferrand double extends to a primitive triple of type \(\mathcal O(-7)\), and
there can be no \((3,4)\) complete intersection supported on \(C_0\).

The class is intrinsic in \(\operatorname{Ext}^1(M,L^2)\): changes of local
lifts add a Čech coboundary, frame changes act on the parameter projective
line, and changes of parameter transport cohomology.  Its overall factor of
three explains, at the level of the second formal neighborhood, why the
obstruction disappears in characteristic three, where P-008 supplies an actual
primitive \((3,4)\) complete intersection.

The obstruction in fact never vanishes for *any* characteristic-zero smooth
rational quartic.  By P-002 the curve is the graph, on
\(Q\simeq\mathbf P^1\times\mathbf P^1\), of a separable degree-three map
\(f:\mathbf P^1\to\mathbf P^1\).  Pre- and postcomposition by
\(\operatorname{PGL}_2\) come from automorphisms of the Segre quadric and do
not change the existence of a primitive triple.  Riemann--Hurwitz gives total
ramification four.  If there is no simple ramification, there are exactly two
totally ramified points and the map is equivalent to \(z^3\), the case just
computed.  Otherwise choose two simple ramification points.  Their branch
values are distinct, and source and target normalizations put the map in the
marked form

\[
 f_\lambda(z)=\frac{z^2(z-1)}{z-\lambda},\qquad \lambda\ne0,1.
\]

This parameter is a surjective marked cover of the remaining left--right
orbits; it is not asserted to be a unique coarse-moduli coordinate.

For this graph, explicit split conormal frames again identify
\(N_C^*=\mathcal O(-7)^2\).  Use the Čech cover

\[
 U=\mathbf P^1\setminus\{\infty,\lambda\},\qquad
 V=\mathbf P^1\setminus\{0,1\}.
\]

Reducing the exact quadratic chart transition by subtracting the principal
parts at \(\lambda\) and \(1\) gives the Bănică--Forster class in the standard
basis of \(H^1(\mathcal O(-7))\).  For a quotient point \([A:B]\in\mathbf
P^1\), multiply its six coordinates by the common unit
\(4\lambda^4(\lambda-1)^2\).  Four of the resulting homogeneous cubics are

\[
\begin{aligned}
G_1={}&(A\lambda+B)\bigl((5\lambda^3-3\lambda^2)A^2
 +(6\lambda^2-2\lambda)AB+(3\lambda-1)B^2\bigr),\\
G_2={}&\lambda(A\lambda+B)\bigl((3\lambda^3-\lambda^2)A^2
 +4\lambda^2AB+(3\lambda-1)B^2\bigr),\\
G_5={}&\lambda^4(A+B)\bigl((3\lambda-1)A^2
 +4\lambda AB+(3\lambda-1)B^2\bigr),\\
G_6={}&\lambda^4(A+B)\bigl((3\lambda-1)A^2
 +2(3\lambda-1)AB+(5\lambda-3)B^2\bigr).
\end{aligned}
\]

On \(A=1\), write \(T=B\), and divide \(G_2\) by \(\lambda\) and
\(G_5,G_6\) by \(\lambda^4\).  Exact subtraction gives

\[
 G_1-G_2/\lambda=2\lambda(\lambda-1)(\lambda+T)^2,
\]

and

\[
 G_5/\lambda^4-G_6/\lambda^4
 =-2T(\lambda-1)(T+1)^2.
\]

If all six obstruction coordinates vanished, the first identity would force
\(T=-\lambda\); the second difference would then be
\(2\lambda(\lambda-1)^3\ne0\), a contradiction.  At the missing point
\(A=0\), a direct calculation gives, up to the same unit,

\[
 (G_1,\ldots,G_6)=
 (3\lambda-1,\lambda(3\lambda-1),\lambda^2(3\lambda-1),
 \lambda^3(3\lambda-1),\lambda^4(3\lambda-1),
 \lambda^4(5\lambda-3)).
\]

Simultaneous vanishing would require both \(3\lambda-1=0\) and
\(5\lambda-3=0\), impossible in characteristic zero.  Hence the obstruction
has no zero on any quotient line for any degree-three map, proving P-010 for
all smooth rational quartics.  The marked-transition reduction, including the
discard of a \(z^{-7}\) Čech coboundary, is checked exactly in
`computations/verify_all_quartic_primitive_obstruction.py`.

### P-011: low-degree surfaces singular along the whole quartic

Let \(C\sim(1,3)\) on its unique smooth quadric \(Q=(q=0)\), and let
\(F\) be a degree-\(a\) hypersurface containing \(C\) and singular at every
point of \(C\). Since \(C\subset\mathbf P^3\) is a regular embedding,
singularity along \(C\) is equivalent to

\[
 F\in H^0(\mathbf P^3,\mathcal I_C^2(a)).
\]

In homogeneous coordinates this is membership in the saturated sheaf square
\((I_C^2)^{\mathrm{sat}}=I_C^{(2)}\), not necessarily in the unsaturated
ordinary ideal square.  Locally on the smooth quadric one may write
\(I_C=(q,h)\).  Reducing an element of \(I_C^{(2)}\) modulo \(q\) gives a
multiple of \(h^2\), so if \(q\nmid F\), the divisor \(F|_Q\) contains the
doubled Cartier divisor \(2C\).

The divisor \(F|_Q\) has class \((a,a)\), while \(2C\) has class \((2,6)\).
Its residual divisor
would have class

\[
 (a-2,a-6),
\]

which is not effective when \(a<6\). Hence every degree-\(<6\) hypersurface
singular along all of \(C\) is divisible by \(q\). Write \(F=qH\). Along
\(C\), the quadric is smooth and

\[
 dF|_C=H|_C\,dq|_C;
\]

therefore \(F\) is singular along \(C\) exactly when \(H\) also contains
\(C\).

This gives the complete low-degree list:

- there is no cubic singular along the entire curve;
- a quartic singular along the entire curve is a scalar multiple of \(q^2\);
- a quintic singular along the entire curve is \(qH_3\), where the cubic
  \(H_3\) contains \(C\).

In fact no \(q\)-divisible hypersurface can be a member of a successful pair.
For every second form \(G\),

\[
 V(q,G)\subseteq V(qH,G).
\]

P-004 says that \(V(q,G)\) strictly contains \(C\), so the extra locus survives
in \(V(qH,G)\).  This excludes the quintics as well as \(q^2\).  Thus a valid
quartic or quintic carrier has normal order one at the generic point of \(C\),
although P-005 forces every carrier to be singular at at least one closed point
of \(C\). In particular, the genuinely thick-carrier escape route cannot begin
below degree six.

### P-012: every smooth rational quartic is an STCI in positive characteristic

Let \(k\) be algebraically closed of characteristic \(p>0\), and let
\(C\subset\mathbf P^3_k\) be a smooth nondegenerate rational quartic. By
P-002 it has type \((1,3)\) on a smooth quadric. One ruling therefore induces
a degree-three morphism

\[
 f:C\simeq\mathbf P^1\longrightarrow\mathbf P^1.
\]

We first produce an internal cuspidal projection. If \(f\) is separable, the
different has degree four by Riemann--Hurwitz, including in the wild
characteristic-two case, so some ruling line cuts \(C\) in \(2R+P\) or in
\(3R\). If \(f\) is inseparable, necessarily \(p=3\), its inseparable degree
is three and every geometric fiber is \(3R\). If the chosen fiber is
\(2R+P\), project from \(P\). If it is \(3R\), project from \(R\), regardless
of whether \(f\) is separable.

Hyperplanes through the center, after removing their simple base point on
\(C\), give a basepoint-free three-dimensional subspace of
\(H^0(\mathbf P^1,\mathcal O(3))\). The associated map to
\(\mathbf P^2\) cannot have a line as image, since that would put \(C\) in a
plane. Its degree formula therefore shows that it is birational onto a plane
cubic.

The normalization map is not immersive at \(R\). In the \(2R+P\) case this
is the usual projection from a point on a line tangent to \(C\) at \(R\). In
the \(3R\) case, put the center at the affine origin and write

\[
 \gamma(u)=uv_1+u^2v_2+O(u^3).
\]

Triple contact with the ruling line means \(v_2\in kv_1\). After canceling
the simple base factor, the projected map is
\([v_1+uv_2+O(u^2)]\), whose derivative is the class of \(v_2\) modulo
\(kv_1\), hence zero.

Its fiber over that image is a singleton. For \(2R+P\), any further preimage
would lie on the line \(PR\), while the extended image of the center \(P\) is
its tangent direction and differs from \(PR\) because \(P\) occurs with
multiplicity one. For \(3R\), another preimage would lie on the same ruling
line, whose intersection with \(C\) is supported only at \(R\). Finally,
\[
 p_a(\text{plane cubic})-g(\mathbf P^1)=1,
\]
so the nonimmersive unibranch image at \(R\) accounts for the entire
\(\delta\)-invariant. It is the unique singularity and is a cusp rather than
a node.

Choose coordinates so the center is \([0:0:0:1]\), and let \(X\) be the cubic
cone over the projected cubic. In characteristic different from three the
cuspidal cubic has normalization

\[
 [s:t]\longmapsto[s^3:s^2t:t^3],
\]

and in characteristic three it has the possibly nonclassical normal form

\[
 [s:t]\longmapsto[s^3:s^2t:t^3+\alpha st^2].
\]

To see these normal forms, put the cusp preimage at \(s=0\) and its image at
\([0:0:1]\). Nonimmersion makes the first two pulled-back coordinates vanish
to order at least two; their span is
\(\langle s^3,s^2t\rangle\). Subtracting their multiples from the third
coordinate leaves \(t^3+\alpha st^2\). When \(3\ne0\), the substitution
\(t\mapsto t+\alpha s/3\), followed by target row operations, removes the
\(st^2\) term. This includes characteristic two. Thus \(X\) is defined
respectively by

\[
 Y^3-X^2Z=0
\]

or, in characteristic three, by

\[
 Y^3+\alpha XY^2-X^2Z=0.
\]

Let

\[
 \nu:\mathbf P(1,1,3)\longrightarrow X
\]

be the finite normalization, with weighted coordinates \(s,t,z\), given by
\([s^3:s^2t:t^3:z]\) in the first case and by
\([s^3:s^2t:t^3+\alpha st^2:z]\) in the second. The induced graded map is
finite: \(s,t\) satisfy monic cubic equations over the standard cusp ring,
and in characteristic three \(t\) satisfies
\[
 T^3+\alpha sT^2-Z=0
\]
after adjoining \(s\). It is birational, since on \(X\ne0\),
\[
 t/s=Y/X,\qquad z/s^3=W/X.
\]
Its geometric fibers are singletons: away from the vertex the cusp point
determines its unique normalization point and the fourth coordinate determines
\(z\) up to weighted scaling; the vertex has unique preimage
\([0:0:1]\). Thus the finite normalization is radicial and surjective, hence a
universal homeomorphism.

The three projected coordinates of the original quartic have a common linear
factor \(l(s,t)\), the point used as the projection center. Write its fourth
coordinate as a quartic \(h(s,t)\). Since the original map is defined at the
center \(P=(l=0)\), one has \(h(P)\ne0\). On
\(\mathbf P(1,1,3)\setminus\{[0:0:1]\}\), the set-theoretic inverse image of
\(C\) is the graph \(z=h/l\); there is no point over \(l=0\), and its closure
adds exactly the weighted vertex. It is the weighted degree-four hypersurface

\[
 D=(\phi=0),\qquad \phi=lz-h.
\]

Suppose first that \(p\ne3\). Put

\[
 R_0=k[s^3,s^2t,t^3].
\]

A binary monomial whose total degree is divisible by three belongs to \(R_0\)
unless its \(s\)-exponent is one. In characteristic \(p\),

\[
 \phi^{3p}=(l^pz^p-h^p)^3.
\]

Every binary coefficient in this expansion is the \(p\)-th power of one of
\(l^3,l^2h,lh^2,h^3\). Its total degree is divisible by three, while all of
its \(s\)-exponents are multiples of \(p\); because \(p\ge2\),
none can equal one. Hence

\[
 \phi^{3p}\in R_0[z].
\]

It has weighted degree \(12p\), so it descends through \(\nu\) to an ordinary
homogeneous form \(G\) of degree \(4p\) on the cubic cone.

In characteristic three put

\[
 R_\alpha=k[s^3,s^2t,t^3+\alpha st^2].
\]

Writing \(X=s^3,Y=s^2t,Z=t^3+\alpha st^2\), direct expansion gives

\[
 s^3t^6=XZ^2+\alpha Y^2Z+\alpha^2XYZ-\alpha^3Y^3,
\]

and \(Z^3=t^9+\alpha^3s^3t^6\). Thus \(s^9,t^9\in R_\alpha\), and the
freshman's-dream identity

\[
 \phi^9=l^9z^9-h^9
\]

lies in \(R_\alpha[z]\). It again has weighted degree \(36\), hence descends
to an ordinary form \(G\) of degree \(12=4p\).

In both cases

\[
 \nu^*G=\phi^{3p}.
\]

Because \(\nu\) is a universal homeomorphism, the zero set of \(G\) on \(X\)
is exactly \(\nu(D)=C\). If \(F\) is the cubic equation of \(X\), then

\[
 \boxed{\sqrt{(F,G)}=I_C,\qquad(\deg F,\deg G)=(3,4p).}
\]

Indeed, the pullback of \(V_X(G)\) is exactly \(D\); the universal
homeomorphism therefore identifies its support with \(C\). Equality of the
projective zero set also gives equality of the homogeneous affine cones, since
their common origin already lies on the cone over \(C\), so homogeneous
Nullstellensatz gives the displayed unsaturated radical equality.

The construction includes inseparable degree-three rulings in characteristic
three and wild separable ramification in characteristic two. P-008 gives
smaller equations for the monomial member in characteristics two and three;
the theorem here is uniform for the entire smooth rational-quartic family.
The checked literature contains Moh's positive-characteristic theorem for
projective monomial curves and a cuspidal-projection criterion, but no source
asserting this family-wide result. It is therefore recorded as **PROVED in
this run**, not as **KNOWN**.

### P-013: fixed-degree STCI is constructible in families

Let \(S\) be noetherian and let
\(\mathcal C\subset\mathbf P^3_S\) be a closed family.  Fix positive integers
\((a,b)\).  Then

\[
 \{s\in S:\ |\mathcal C_{\bar s}|=
 |V(F_a,F_b)|\text{ for some geometric forms }F_a,F_b\}
\]

is constructible.

Indeed, let \(Q\) be the product over \(S\) of the two projective coefficient
spaces, and on \(\mathbf P^3_Q\) let \(Z\) be the common zero scheme of the
two universal forms.  Put \(\mathcal C_Q=\mathcal C\times_SQ\).  Failure of
either set-theoretic inclusion is detected by a point of

\[
 \mathcal C_Q\setminus Z
 \quad\text{or}\quad
 Z\setminus\mathcal C_Q.
\]

Each image in \(Q\) is constructible by Chevalley's theorem.  Taking their
complements and intersection gives a constructible subset \(W\subset Q\) on
which the two supports agree.  Its image in \(S\), again constructible by
Chevalley, is exactly the displayed locus.  Properness is not needed, and the
locus need not be open or closed.

Now take a model over a one-dimensional arithmetic base with infinitely many
closed points, for example a nonempty open subscheme of the spectrum of the
ring of integers of a number field.  A constructible subset that omits the
generic point is finite, while one that contains the generic point contains a
nonempty open set and therefore all but finitely many closed points.
Consequently, for a fixed pair \((a,b)\), the following are equivalent:

1. the geometric generic fiber has such a pair;
2. infinitely many geometric closed fibers have such a pair;
3. all but finitely many geometric closed fibers have such a pair.

The infinite-closed-point hypothesis is essential for the equivalence with
item 2.  The earlier wording "over a localized number ring" was too broad:
for a semilocal localization such as \(\mathbf Z_{(p)}\), "infinitely many
closed fibers" can be vacuous.  The constructibility theorem itself is
unchanged.

The same is true with both degrees bounded by a fixed \(B\), since only
finitely many pairs occur.  This explains rigorously why P-012 does not force a
characteristic-zero presentation: its second degree \(4p\) is unbounded.  In
particular, Craighero--Gattazzo's characteristic-zero exclusion of every cubic
carrier implies that for each fixed \(B\), only finitely many reductions of a
number-field rational quartic can have a \((3,d)\) presentation with
\(d\le B\), even though P-012 supplies a \((3,4p)\) presentation at every
prime.

### P-014: sharp degree on the cuspidal cubic carriers

The Frobenius degree in P-012 is not merely an artifact of that proof on the
chosen cubic carrier.  First consider the standard cusp ring

\[
 R_0=k[s^3,s^2t,t^3]\subset k[s,t].
\]

Its ordinary degree-\(m\) piece consists of all binary forms of degree \(3m\)
except for the one missing semigroup monomial \(st^{3m-1}\).  Thus membership
is equivalent to vanishing of that single coefficient.  If a second surface
on the cone has support equal to the graph \(D=(\phi=lz-h=0)\), unique
factorization upstairs forces its pullback to be \(c\phi^N\).  Homogeneity
forces \(3\mid N\), with second degree \(d=4N/3\).

For \(\phi^N\) to descend coefficientwise, it is necessary and sufficient
that \(p\mid N\).  Sufficiency follows because an \(N\)-th power with
\(p\mid N\) is a polynomial in \(p\)-th powers, so every relevant binary
\(s\)-exponent is a multiple of \(p\) and cannot equal one.

For necessity, keep the standard cusp coordinates fixed with
\(R=[0:1]\), and write \(l=as+bt\).  Assume the homogeneous condition
\(3\mid N\) and \(p\nmid N\).  There are three cases.

1. If \(b=0\), then \(P=(l=0)=R\).  The coefficient of \(z\) in
   \(\phi^N\) has missing-monomial coefficient
   \(\pm Na h(R)^{N-1}\ne0\).
2. If \(a,b\ne0\), the coefficient of \(z^N\) is \(l^N\), whose missing
   \(st^{N-1}\) coefficient is \(Na b^{N-1}\ne0\).
3. If \(a=0\) and \(b\ne0\), smoothness of the original quartic at \(R\)
   forces the \(st^3\) coefficient \(h_1\) of \(h\) to be nonzero.  The
   coefficient of \(z^{N-1}\), namely \(-N l^{N-1}h\), has missing
   \(st^{N+2}\) coefficient \(-Nb^{N-1}h_1\ne0\).

Thus descent fails whenever \(p\nmid N\).  The earlier proof's attempt to move
\(P\) while retaining the displayed semigroup coordinates was unjustified,
and its use of the constant coefficient failed when \(h(R)=0\); the
three-case argument above repairs both defects.  Therefore

\[
 N_{\min}=\operatorname{lcm}(3,p),\qquad
 d_{\min}=4N_{\min}/3.
\]

This is \((N,d)=(3p,4p)\) for \(p\ne3\) and \((3,4)\) for the standard cusp
in characteristic three.

There is a genuinely different characteristic-three cusp.  For
\(\alpha\ne0\), put

\[
 R_\alpha=k[s^3,s^2t,t^3+\alpha st^2].
\]

If \(f=\sum_{i=0}^{3m}c_i s^{3m-i}t^i\), then

\[
 f\in(R_\alpha)_m
 \quad\Longleftrightarrow\quad
 c_{3m-1}=m\alpha c_{3m}.
\]

To prove this, note that
\(Y^3+\alpha XY^2-X^2Z\) is the full kernel of the normalization map, so
\(\dim(R_\alpha)_m=3m\), one less than the full binary space.  Among generator
monomials, only \(Z^m\) contributes to the two top \(t\)-coefficients, and

\[
 Z^m=t^{3m}+m\alpha st^{3m-1}+O(s^2).
\]

The displayed relation is therefore both necessary and, by dimension,
sufficient.

Only \(N=3,6,9,\ldots\) are homogeneous possibilities.  If
\(P\ne R=[0:1]\), write \(l=as+bt\) with \(b\ne0\).  Freshman's dream makes
the next-to-top coefficient of \(l^3\), respectively \(l^6\), zero while the
top coefficient is \(b^3\), respectively \(b^6\); the membership relation
fails for \(m=1\), respectively \(m=2\).  If \(P=R\), then \(l=s\) and
\(h(R)\ne0\); the same argument applied to \(h^3\) and \(h^6\), with
\(m=4,8\), excludes \(N=3,6\).  But

\[
 \phi^9=l^9z^9-h^9
\]

always descends because the relevant values \(m=3,12\) vanish in the field.
An explicit lift is obtained from

\[
 U=XZ^2+\alpha Y^2Z+\alpha^2XYZ-\alpha^3Y^3,
 \quad S_9=X^3,
 \quad T_9=Z^3-\alpha^3U,
\]

whose pullbacks are \(s^3t^6,s^9,t^9\).  If
\(l=as+bt\) and \(h=\sum h_i s^{4-i}t^i\), set

\[
 L_9=a^9S_9+b^9T_9,
 \qquad
 H_9=\sum_{i=0}^4h_i^9S_9^{4-i}T_9^i.
\]

Then the ordinary degree-twelve form

\[
 G=L_9W^9-H_9
\]

pulls back exactly to \(\phi^9\).  Hence on the nonclassical cusp carrier

\[
 \boxed{N_{\min}=9,\qquad d_{\min}=12.}
\]

These are minima on the specified cubic cone; they do not claim that no
different carrier can give a lower-degree presentation of the same quartic.

### P-015: canonical compression by the carrier Cartier index

This reduction applies beyond any fixed degree pair.  Work in characteristic
zero and define

\[
 \alpha(C)=\min\{\deg X:\ X\subset\mathbf P^3\text{ is integral and some }
 Y\text{ satisfies }|X\cap Y|=C\}.
\]

If \(C\) is an STCI, the set is nonempty.  Indeed, after factoring either
defining equation, every irreducible factor meets the other hypersurface in a
curve; that curve is contained in the irreducible support \(C\), and hence has
support exactly \(C\).  This factor lemma is why minimality must be taken
among carriers that actually occur in a defining pair, not among all surfaces
containing \(C\).  The unique smooth quadric is an immediate counterexample
to the latter, incorrect formulation.

Let \(X\) attain \(\alpha(C)=a\), suppose \(X\) is generically smooth along
the rational quartic \(C\), and let a degree-\(b\) surface \(Y\) be a mate.
Write \(H=\mathcal O_X(1)\).  At the generic point of \(C\), the Cartier
divisor \(Y|_X\) has a positive multiplicity \(r\), so

\[
 r[C]=b[H]\quad\text{in }\operatorname{APic}X,
 \qquad 4r=ab.
\]

At each of the finitely many points
\(p\in C\cap\operatorname{Sing}X\), let \(e_p\) be the order of the local
almost-Cartier class \([C]_p\), and put \(e=\operatorname{lcm}_p(e_p)\), with
the empty lcm equal to one.  The displayed relation shows \(e_p\mid r\).
Hartshorne--Polini's local-to-global sequence for almost-Cartier divisors then
shows that \(eC\) is Cartier.  Write \(r=qe\).  In \(\operatorname{Pic}X\),

\[
 q[eC]=b[H].
\]

Thus the class of \(eC\) is torsion modulo \(\mathbf ZH\).  In characteristic
zero, Hartshorne--Polini Lemma 7.6 says that
\(\operatorname{Pic}X/\mathbf ZH\) is torsion-free.  Consequently

\[
 eC\sim nH,
 \qquad n=\frac{4e}{a}\in\mathbf Z_{>0},
 \qquad b=qn.
\]

The canonical section of \(\mathcal O_X(eC)\simeq\mathcal O_X(n)\) lifts to
an ambient degree-\(n\) form, since

\[
 H^1(\mathbf P^3,\mathcal O_{\mathbf P^3}(n-a))=0.
\]

It cuts out the Cartier divisor \(eC\) on \(X\).  If \(n<a\), factor this
lift.  No factor is \(X\), and the factor lemma makes every irreducible factor
another integral carrier occurring in a defining pair, of degree below
\(a\).  This contradicts the definition of \(\alpha(C)\).  Therefore

\[
 \boxed{a\mid4e,\qquad n=4e/a\ge a,
 \qquad e\ge a^2/4.}
\]

The exact compression relation is \(n=be/r\).  If \(b\) was already minimal
among mates for this fixed \(X\), then necessarily \(e=r\) and \(n=b\).
Away from the finite singular set of \(X\), the compressed multiple structure
is locally \((u,v^e)\), hence primitive there and quasi-primitive globally.

For a minimal degree-six carrier that is generically smooth along \(C\), this
forces

\[
 3\mid e,\qquad e\ge9,\qquad
 (a,n)=(6,2e/3).
\]

The first canonical possibility is therefore \(e=9\) and a \((6,6)\) pair.
Local Cartier indices \(e=3\) or \(6\) would compress to a quadric or quartic
carrier and cannot represent a genuinely sextic-minimal phenomenon.

### P-016: the exact quasiprimitive \((4,5)\) classification

For the monomial quartic, the known \((4,4)\) exclusion and the
Craighero--Gattazzo exclusion of every cubic carrier made \((4,5)\) the first
unresolved degree pair before P-025 and P-040 closed it.  More generally,
P-011 says that both a quartic and a
quintic carrier have generic normal order one.  P-006 makes their first normal
forms proportional, so a hypothetical complete intersection of generic
multiplicity

\[
 \frac{4\cdot5}{\deg C}=5
\]

is quasiprimitive.

The Bănică--Forster filtration, together with Boratyński's lci duality for a
quasiprimitive multiplicity-five curve, has graded pieces

\[
 \mathcal O_C,\quad L,\quad L^2(D),\quad
 L^3(2D),\quad L^4(2D),
\]

where \(D\) is effective.  Hence, writing \(l=\deg L\) and \(d=\deg D\),

\[
 \chi(\mathcal O_X)=5+10l+5d.
\]

A \((4,5)\) complete intersection has arithmetic genus

\[
 1+\frac{20(4+5-4)}2=51,
\]

so \(\chi(\mathcal O_X)=-50\), and therefore

\[
 2l+d=-11.
\]

The first layer is a line-bundle quotient
\(N_C^*=\mathcal O(-7)^2\twoheadrightarrow L\), which forces \(l\ge-7\),
while \(d\ge0\).  There are exactly two solutions:

\[
 \boxed{(l,d)=(-7,3)\quad\text{or}\quad(-6,1).}
\]

The primitive-triple obstruction P-010 does not by itself remove these cases:
the positive defect divisor \(D\) is precisely the finite locus where both
carriers may be singular.  Jaffe's disjoint-singular-locus theorem likewise
shows only that such a pair must have common singular points.  Thus the two
displayed types, rather than arbitrary multiplicity-five structures, are the
correct finite formal-neighborhood target.

### P-017: the first thick carriers, in degree six

Let \(q\) define the unique quadric \(Q\), with
\(C\sim(1,3)\).  Reduction modulo \(q\) gives an exact sequence

\[
 0\longrightarrow \mathcal I_C(4)
 \xrightarrow{\cdot q}\mathcal I_C^{(2)}(6)
 \longrightarrow\mathcal O_Q(4,0)\longrightarrow0.
\]

Indeed, the restriction of a double sextic is \(h^2R\), where \(h\) defines
\(C\) on \(Q\) and

\[
 R\in H^0(Q,\mathcal O_Q((6,6)-2(1,3)))
 =H^0(Q,\mathcal O_Q(4,0)).
\]

The kernel consists of \(qH\) with \(H\in I_C(4)\), and
\(H^1(I_C(4))=0\).  Since

\[
 h^0(I_C(4))=h^0(\mathcal O_{\mathbf P^3}(2))
 +h^0(\mathcal O_Q(3,1))=10+8=18,
\]

one obtains

\[
 \boxed{h^0(I_C^{(2)}(6))=23,\qquad
 H^0(I_C^{(2)}(6))/qH^0(I_C(4))\simeq H^0(O_Q(4,0)).}
\]

Every non-\(q\)-divisible member has exact normal order two, because
\(H^0(I_C^{(3)}(6))=kq^3\).  Its quadric section is

\[
 X\cap Q=2C+D_R,
\]

where \(D_R\) is the union, with multiplicities, of the four ruling lines
selected by the binary quartic \(R\).

For \(C_0\), with

\[
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

the five classes

\[
 A^2,\ AB,\ B^2,\ BD,\ D^2
\]

give a complement to \(qH^0(I_C(4))\).  The missing-looking class satisfies

\[
 AD-B^2=-x_1x_2q^2.
\]

The exact verifier proves that \(I_C^{(2)}=I_C^2\) here and constructs

\[
 F_*=A^2+B^2+D^2+q^2(x_0^2+x_1^2+x_2^2+x_3^2)
\]

with reduced Jacobian locus exactly \(C_0\).  This also forces absolute
irreducibility: a nontrivial factorization would put the curve of intersection
of two factors in the singular locus.  Thus integral sextics singular along
the whole quartic genuinely exist; the problem is finding a mate, not finding
the first carrier.

### P-018: two thick sextics cannot be the pair

Assume characteristic zero, so
\(N_C\simeq\mathcal O(7)^2\), and suppose two non-\(q\)-divisible double
sextics \(F,G\) cut out only \(C\).  Their complete intersection has degree
36, hence generic transverse length nine along the degree-four support.  In
the transverse ring \(k(C)[[x,y]]\), both equations have order two.  Relatively
prime quadratic initial forms would have intersection length four, so the two
quadratics have a common nonconstant factor.

On the exceptional divisor

\[
 E=\mathbf P(N_C)\simeq\mathbf P^1\times\mathbf P^1,
\]

each quadratic normal divisor has class \((10,2)\).  The generic common factor
closes to a horizontal common component
\(T\sim(a,e)\), where \(a\ge0\) and \(e=1\) or \(2\); vertical factors caused
by closed-point order jumps do not remove this horizontal component.

The first normal form of \(q\) vanishes on the section

\[
 S_q=\mathbf P(N_{C/Q})\sim(1,1).
\]

The class is not \((0,1)\): after twisting the normal inclusion
\(N_{C/Q}=\mathcal O(6)\hookrightarrow\mathcal O(7)^2\) by
\(\mathcal O(-7)\), it is given by two independent linear forms, so its graph
has base degree one.

On \(Q\), write

\[
 F|_Q=h^2R_F,\qquad G|_Q=h^2R_G,\qquad
 R_F,R_G\in H^0(O_Q(4,0)).
\]

Restriction of the quadratic normal divisors to \(S_q\) is exactly the pullback
of the zero divisors of \(R_F,R_G\).  If \(T=S_q\), both residual quartics
vanish identically, so both sextics are divisible by \(q\), contrary to the
hypothesis.  Otherwise

\[
 T\cdot S_q=a+e>0.
\]

At an intersection point the two residual binary quartics have a common root.
The corresponding ruling line of \(Q\) is then contained in both \(F\) and
\(G\), giving an extra curve outside \(C\).  This contradiction proves

\[
 \boxed{\text{no thick--thick \((6,6)\) defining pair exists in
 characteristic zero}.}
\]

The balanced-normal hypothesis is essential to this proof.  In characteristic
two, \(N_{C_0}=\mathcal O(6)\oplus\mathcal O(8)\), so
\(E\simeq\mathbb F_2\) has a negative section disjoint from \(S_q\).  Exact
examples show that two tangent quadratics can share that section while their
residual quartics are coprime; those examples have other extra curves and are
not STCI pairs, but they prevent an invalid characteristic-two extension of
the argument.

### P-019: normalization obstruction for a thick sextic

There is a complementary obstruction for one integral thick carrier.  Let an
integral degree-\(a\) surface \(X\) have generic normal order \(\mu\) along
\(C\).  Restricting to \(Q\) gives an effective residual class

\[
 (a,a)-\mu(1,3)=(a-\mu,a-3\mu),
\]

so \(a\ge3\mu\).  A thick sextic therefore has \(\mu=2\).

Let \(\nu:S=X^\nu\to X\) be the normalization, write the components of
\((\nu^{-1}C)_{\mathrm{red}}\) as \(\Gamma_i\), and put
\(\delta_i=[k(\Gamma_i):k(C)]\).  At the generic point of \(C\), the
one-dimensional hypersurface local ring has multiplicity \(\mu\).  The
normalization multiplicity formula gives

\[
 \mu=\sum_i s_i\delta_i,
\]

with positive integers \(s_i\).  Hence for a sextic
\(\sum_i\delta_i\le2\).

Suppose the reduced inverse image is one irreducible Cartier curve \(\Gamma\)
of degree \(\delta\) over \(C\), and suppose a degree-\(b\) mate exists.
Pulling its Cartier divisor to the normalization gives

\[
 q\Gamma\sim b\widetilde H
\]

for some \(q>0\), where \(\widetilde H=\nu^*O_X(1)\).  Projection formula
gives

\[
 \widetilde H^2=a,\qquad \widetilde H\Gamma=4\delta.
\]

Intersecting the displayed equivalence first with \(\widetilde H\) and then
with \(\Gamma\) yields

\[
 \boxed{\Gamma^2=\frac{16\delta^2}{a}.}
\]

For \(a=6\), the multiplicity formula permits only \(\delta=1,2\), giving
\(8/3\) or \(32/3\).  This contradicts integrality of the self-intersection of
a Cartier curve.  Thus a thick sextic in a defining pair can survive this
argument only if the normalized preimage splits into two degree-one branches,
or its irreducible preimage is non-Cartier.  Those are genuine gaps: the
split-branch intersection equations have consistent integral numerical
solutions, so one cannot silently assume equal branch multiplicities or
iterate the same fractionality argument.

### P-020: the split-sextic branch has only two extreme numerical types

Let

\[
 \pi:B=\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3,
 \qquad E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

and use the bidegree convention in which

\[
 H|_E=\mathcal O_E(4,0),\qquad
 \mathcal O_E(E)=\mathcal O_E(7,-1).
\]

An integral sextic of exact normal order two has strict transform
\(D\sim6H-2E\), and hence

\[
 D|_E\sim(10,2).
\]

Assume this divisor is the reduced sum of two distinct integral, content-free
sections, with no vertical component:

\[
 Z_1\sim(d,1),\qquad Z_2\sim(10-d,1).
\]

After exchanging them, take \(0\le d\le5\).  The no-vertical hypothesis makes
the blowdown of the normalized strict transform quasi-finite over the sextic;
the two curves \(\Gamma_i\) above \(Z_i\) are therefore exactly the two
divisorial branches over \(C\).  If a degree-\(b\) mate exists, its pullback to
the normalization has divisor

\[
 bH\sim m_1\Gamma_1+m_2\Gamma_2,
 \qquad m_1,m_2>0.
\]

This equality is an equality of Weil divisors with Cartier left side.  It may
be intersected with the Cartier divisors \(H\) and \(E\), even when the
individual branches are not Cartier.  The ambient blowup intersections are

\[
 H^2D=6,\qquad HED=8,
\]

and

\[
 H\Gamma_i=4,\qquad
 E\Gamma_1=7-d,\qquad E\Gamma_2=d-3.
\]

Consequently

\[
 m_1+m_2=\frac{3b}{2},
\]

\[
 (7-d)m_1+(d-3)m_2=8b.
\]

Put \(\Delta=m_1-m_2\).  Eliminating \(m_2\) gives

\[
 \Delta(5-d)=5b,
 \qquad
 \frac{m_2}{b}=\frac{5-3d}{4(5-d)}.
\]

The case \(d=5\) is impossible, and positivity of \(m_2\) leaves only

\[
 \boxed{d=0,\quad(m_1,m_2,b)=k(5,1,4)}
\]

or

\[
 \boxed{d=1,\quad(m_1,m_2,b)=k(11,1,8)}.
\]

This is a finite reduction, not yet an unconditional exclusion.  It becomes
an exclusion if the two branches are Cartier on the normalization.  Writing
\(z=\Gamma_1\Gamma_2\), one then has

\[
 \Gamma_1^2=7-d-z,\qquad
 \Gamma_2^2=d-3-z.
\]

Intersecting the mate divisor with each branch forces respectively

\[
 d=0:\quad z=\frac{19}{4},
 \qquad
 d=1:\quad z=\frac{17}{5},
\]

both impossible for Cartier curves on a smooth surface.  In particular, if
the first strict transform is smooth at the ten collision points, its branch
intersection is the ordinary value

\[
 Z_1Z_2=10,
\]

and the contradiction is immediate.

The qualification is essential.  On the normal local surface

\[
 xy=e^n,
\]

the two components of \((e=0)\) meet with Mumford intersection \(1/n\), not
one.  Thus normality alone does **not** imply \(z=10\); isolated local
class-group corrections are exactly the remaining split-sextic escape route.
The two forced values above quantify those corrections.  In transverse
\(A_{r-1}\) models they require total differents \(21/4\) and \(33/5\),
respectively.

### P-021: corrected first-normal reduction for the mixed \((4,6)\) pair

Let \(F,G\) have degrees four and six.  The quartic cannot have normal order
two by P-011.  If both equations initially have order one, P-006 makes their
normal linear forms proportional over \(k(C)\).  Write them on the exceptional
surface as

\[
 f_1=H_F L,\qquad g_1=H_G L,
\]

where \(L\) is the primitive horizontal factor.  The quotient \(H_G/H_F\)
is a **rational**, not automatically regular, section of
\(O_C(2)=O_{\mathbf P^1}(8)\).  A global subtraction is available only on the
regular-ratio branch
\(\operatorname{div}(H_G)\ge\operatorname{div}(H_F)\).  On that branch,

\[
 H^0(\mathbf P^3,O(2))\longrightarrow H^0(C,O_C(2))
\]

is surjective.  Subtracting a quadratic multiple of \(F\) from \(G\) therefore
puts the pair, without changing its ideal, in normal orders \((1,2)\).

The regularity condition cannot be omitted.  In the complete local ring
\(k[[t,u,v]]\),

\[
 F=tu+v^6,\qquad G=u
\]

generate \((u,v^6)\), whose radical is \((u,v)\) and whose quotient is finite
free of transverse length six over \(k[[t]]\), but the first-normal ratio is
\(1/t\).  This disproves the formerly stated universal subtraction.

On

\[
 E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

the first normal divisors have classes

\[
 D_F\sim(9,1),\qquad D_G\sim(10,2).
\]

Write the saturated horizontal component common to them as
\(R\sim(e,1)\), retaining every closed-point order jump as a vertical divisor:

\[
 D_F=V_B+R,\qquad V_B\sim(9-e,0),
\]

\[
 D_G=R+V_W+T,\qquad
 V_W\sim(w,0),\quad T\sim(10-e-w,1).
\]

Let \(S_q\sim(1,1)\) be the section defined by the normal direction of the
unique quadric.  On that quadric, with \(C\sim(1,3)\), neither equation can be
\(q\)-divisible, and

\[
 F|_Q=C+\rho,\qquad \rho\sim(3,1),
\]

\[
 G|_Q=2C+\sigma,\qquad \sigma\sim(4,0).
\]

The common horizontal section cuts

\[
 D_0=R\cap S_q,\qquad \deg D_0=e+1,
\]

and the exceptional-divisor identities show scheme-theoretically that

\[
 D_0\subset\rho\cap\sigma.
\]

If \(\rho\) and \(\sigma\) have no common component, their proper intersection
on \(Q\) has length

\[
 (3,1)\cdot(4,0)=4.
\]

Hence \(e+1\le4\).  If \(e\ge4\), the two residuals share a component; since
\(\sigma\) is a sum of four ruling fibers, that component is an extra ruling
line contained in both ambient equations.  Therefore every pair in the
regular-ratio branch must
satisfy

\[
 \boxed{e\in\{0,1,2,3\}},
\]

so the vertical singularity divisor of the quartic has degree
\(9-e\ge6\).

For the omitted nonregular order-\((1,1)\) branch, the original divisors have
classes \((9,1)\) and \((17,1)\).  A primitive common horizontal factor may
have \(e\le8\); the endpoint \(e=9\) has constant \(H_F\) and is therefore
regular.  These pole/vertical-divisor strata are not covered by the finite
list below and are now a separate open problem.

This bound is sharp at first-normal order.  For \(C_0\), exact linear algebra
identifies the quartic normal image as a rank-17 subspace of
\(H^0(O(9))^2\), and the sextic quadratic-normal image as a rank-22 subspace
of \(H^0(O(10))^3\).  For each \(e=0,1,2,3\), their common-factor incidence
has a nonempty full-rank locus, even after imposing non-\(q\)-divisibility and
the absence of a common residual ruling on \(Q\).  One explicit \(e=0\)
example is

\[
\begin{aligned}
F={}&A(x_0+x_1+x_2+x_3)+B(x_2+x_3)+Dx_2\\
 &+q(x_1x_3+x_2^2+2x_3^2)+2q^2,\\
G={}&A^2+4q^3.
\end{aligned}
\]

Its normal forms are \(H_9a\) and \(a^2\); neither equation is
\(q\)-divisible and the residual divisors on \(Q\) share no ruling.  Yet its
generic transverse length is three rather than six, leaving residual degree
twelve.  Within the regular-ratio branch, the next decisive conditions are
the vanishing,
after formal elimination by the quartic, of the cubic, quartic, and quintic
transverse coefficients, followed by nonvanishing of the sextic coefficient.
The first blowup cannot replace those higher-jet equations.

### P-022: the actual thick-sextic first-normal image

For any characteristic-zero smooth rational quartic, the quadratic
first-normal map is

\[
 H^0(I_C^{(2)}(6))\longrightarrow
 H^0\bigl(C,\operatorname{Sym}^2N_C^*\otimes O_C(6)\bigr).
\]

P-017 gives a 23-dimensional source.  Its kernel is exactly
\(H^0(I_C^{(3)}(6))=kq^3\): restriction to the unique quadric would otherwise
give a section of \(O_Q(3,-3)\).  Thus its image \(W\) has dimension 22.
If \(U\) is the seven-dimensional first-normal image of cubics through \(C\),
then

\[
 W=\langle U\cdot U\rangle.
\]

For \(C_0\), in the balanced frame

\[
 z=x_1/x_0,\qquad a=x_2-z^3,\qquad b=x_3-z^4,
 \qquad \xi=b-\tfrac32za,\quad\eta=a,
\]

an exact row reduction gives eleven independent linear equations cutting out
\(W\subset H^0(O(10))^3\).  Writing a normal quadratic as

\[
 \alpha(z)\xi^2+\beta(z)\xi\eta+\gamma(z)\eta^2,
\]

the equations are

\[
\begin{aligned}
-\alpha_9+2\beta_{10}&=0,&-\beta_0+2\gamma_1&=0,\\
\alpha_0-2\beta_1+4\gamma_2&=0,
&-3\alpha_1+2\beta_2+4\gamma_3&=0,\\
\alpha_2-2\beta_3+4\gamma_4&=0,
&\alpha_3-2\beta_4+4\gamma_5&=0,\\
-\alpha_4+4\gamma_6&=0,
&\alpha_5-2\beta_6+4\gamma_7&=0,\\
\alpha_6-2\beta_7+4\gamma_8&=0,
&-\alpha_7-2\beta_8+12\gamma_9&=0,\\
\alpha_8-2\beta_9+4\gamma_{10}&=0.
\end{aligned}
\]

Solving them produces primitive split
quadratics

\[
 (p\xi+r\eta)(u\xi+v\eta)
\]

of every type \((d,1)+(10-d,1)\), \(0\le d\le5\).  Therefore the actual
ambient image, and not merely the complete space of normal quadratics, permits
all split types.

Exact affine representatives \((p,r),(u,v)\) for the two factors are:

\[
\begin{array}{c|c|c}
d&(p,r)&(u,v)\\\hline
0&(1,0)&(-z^{10}-2,-z)\\
1&(1,z)&(2+6z+2z^8,z+z^2+z^9)\\
2&(1,z^2)&(2+4z+24z^7,z+2z^2+z^5+2z^6+4z^7+12z^8)\\
3&(1,z^3)&(8-2z+8z^3+24z^5+8z^6,4z-3z^2+4z^6+4z^7)\\
4&(1,z^4)&(4+2z+12z^4+4z^5,2z+3z^2+2z^5+2z^6)\\
5&(z^5,1)&(-z^5,1).
\end{array}
\]

This also falsifies a tempting inference.  A square discriminant on the
exceptional divisor forces the *normal divisor* to split, but not the ambient
sextic.  Exact integral examples are

\[
 (A+x_3q)(A-x_3q)+q^3
\]

and

\[
 (A+x_3q)(2A+D)+q^3.
\]

The second has smooth first strict transform at all collisions of its two
normal sections.  Thus any later argument must use the mate, higher normal
coefficients, or normalization intersection theory; first-normal
factorization alone is insufficient.

### P-023: Hodge exclusion for squarefree split-sextic residuals

Retain the split/no-vertical hypotheses of P-020 and let \(S\) be the
normalization of the strict transform of the sextic.  Work on a resolution
\(\widetilde S\), using Mumford numerical pullbacks for the two branch curves.
Write

\[
 K_0=2H-E.
\]

This is the pullback of the adjunction class cut by the unique quadric; it
must not be silently identified with the canonical divisor of a singular
normalization or of its resolution.  The ambient intersections are

\[
 H^2=6,\quad HE=8,\quad E^2=4,
 \quad HK_0=4,\quad K_0^2=-4.
\]

For the low-degree branch \(\Gamma\) of type \((d,1)\), P-020 gives

\[
 K_0\Gamma=d+1,\qquad
 \Gamma^2=\begin{cases}9/4&d=0,\\13/5&d=1.\end{cases}
\]

Put

\[
 L=H+K_0,\qquad
 T=\Gamma^\#+\frac{d+1}{4}K_0,
\]

where \(\Gamma^\#\) is the numerical pullback.  Then \(L^2=10\),
\(LK_0=TK_0=0\), and equality holds in Hodge index:

\[
 (LT)^2=L^2T^2.
\]

Consequently

\[
 T\equiv\tfrac12L\quad(d=0),\qquad
 T\equiv\tfrac35L\quad(d=1).
\]

If the residual binary quartic is squarefree, the quadric section of \(K_0\)
is a sum of four pairwise-disjoint reduced ruling lines \(R_j\).  Each \(R_j\)
is Cartier on the normal surface, even if it passes through a singular point:
locally it is the only component of the reduced Cartier divisor through that
point.  Moreover

\[
 HR_j=1,\qquad K_0R_j=-1,\qquad LR_j=0.
\]

Intersecting the numerical proportionality with \(R_j\) yields

\[
 \Gamma R_j=\frac{d+1}{4},
\]

equal to \(1/4\) or \(1/2\), contrary to integrality of intersection with the
Cartier curve \(R_j\).  Hence neither surviving split type can have a
squarefree residual quartic.  This proof was independently audited for signs
and for the use of Hodge index on a resolution.  What remains is precisely the
highly non-squarefree residual locus; squarefreeness does not follow merely
from a reduced, content-free split first-normal divisor.

For \(C_0\), exact next-jet calculations are consistent with this boundary.
For every \(d=0\) factor, imposing both first-normal divisibility and vanishing
of the next normal coefficient makes the collision polynomial have affine
degree at most five and forces a square factor in the residual binary quartic.
A large \(d=1\) chart has the same behavior.  The full projective space of
\((1,1)\)-factors has not been eliminated.

### P-027: conditional closure of the clean split-conductor case

There is a separate global exclusion which should not be conflated with the
Mumford-intersection analysis above.  Let \(X\subset\mathbf P^3_{\mathbf C}\)
be an integral sextic, let \(\nu:S\to X\) be a **smooth** normalization, and
suppose that \(X\) is generically nodal along a smooth rational quartic \(C\).
Assume the two degree-one conductor branches are \(\Gamma_1,\Gamma_2\) and
that the source conductor is clean:

\[
 I_C O_S=O_S(-\Gamma_1-\Gamma_2),
\]

with no additional conductor component meeting them.  The source
double-point formula of Kleiman--Lipman--Ulrich gives

\[
 K_S+\Gamma_1+\Gamma_2=2H.
\]

Each branch is isomorphic to \(C\simeq\mathbf P^1\).  Smooth adjunction on
\(S\) therefore forces

\[
 \Gamma_1\Gamma_2=10.
\]

The conductor square gives

\[
 0\longrightarrow O_X\longrightarrow\nu_*O_S
 \longrightarrow O_C(-Z)\longrightarrow0,
 \qquad \operatorname{length}Z=10,
\]

and hence

\[
 \chi(O_S)=2,\qquad p_g(S)=1,\qquad q(S)=0.
\]

The blowup identities give, for a split first-normal type
\((d,1)+(10-d,1)\),

\[
 \Gamma_1^2=-d-3,\qquad \Gamma_2^2=d-13.
\]

If a degree-\(b\) mate pulls back as
\(bH=m_1\Gamma_1+m_2\Gamma_2\), its two branch intersections force

\[
 d^2-10d-35=0,
\]

which has no integral solution \(0\le d\le5\).  Equivalently, the required
ratio \(m_1/b\) would be \((9\pm\sqrt{15})/12\), not rational.  Thus the clean
split-conductor case is impossible.

The same hypotheses yield

\[
 K_S^2=-4,\qquad c_2(S)=28,
\]

matching the classical ordinary-sextic formulas; in an ordinary model the
degree-20 discriminant gives twenty pinch points and a connected genus-nine
conductor cover, so it cannot split.  These numerical identities cannot be
imported into the unresolved case.  The exact loopholes are a singular
normalization, an extra conductor curve meeting a branch, or a finite-length
factor in \(I_CO_S\).  Those corrections, rather than an unrecorded
"different" on a smooth normalization, are where a survivor must live.

### P-024: a bounded local-cohomology obstruction

Let

\[
 S=k[x,y,z,w],\quad q=xw-yz,\quad
 A=x^2z-y^3,\quad B=xz^2-y^2w,\quad C=yw^2-z^3,
\]

\(I=(q,A,B,C)\), and \(J=(q,B)\).  The Hartshorne--Polini module is

\[
 M=H_I^2(S)=\Gamma_I H_J^2(S),\qquad
 H_J^2(S)=\varinjlim_n S/(q^n,B^n).
\]

Consider

\[
 u=\frac{xz}{qB},\qquad v=\frac{yw}{qB}.
\]

At a residual-line endpoint, the completed local model is
\(R=k[[c,q,r]]\), with \(e=1/(qr)\), and the two classes map, up to a common
sign, to

\[
 u\longmapsto c^2e,\qquad v\longmapsto e.
\]

The \(c\)-adic valuations then give all-stage contradictions to a common
ancestor with the natural \((A,C)\) multipliers.  Solving the degree-one
compatibility equations shows that the only linear multiplier pair is
proportional to \((y,z)\), and its required local ancestor would satisfy
\(c\alpha=e\), again impossible.  Constant multipliers are also impossible.

This is a genuine obstruction to these bounded multiplier classes, not a
proof that \(M\) is non-quasi-cyclic.  P-037 below supersedes the former
degree-two computational frontier by excluding every multiplier pair of
degree at most three at every direct-limit stage.  One correction remains
important for future finite-stage work: the relevant primary approximation is

\[
 (q^2,\ a(ac+2q),\ a^2q,\ a^3),
\]

not the overly simple monomial ideal \((q^2,a^2)\).

The formerly tempting compatible quadratic pair

\[
 f=x^2+z^2,\qquad g=y^2+w^2,
\]

does satisfy

\[
 g\,xz-f\,yw=q(zw-xy).
\]

On the normalization its restrictions are \((s^2h,t^2h)\), with
\(h=s^6+t^6\).  P-037 turns any zero of \(h\) into a characteristic-zero
finite-Laurent contradiction, so the earlier inconsistent stage-three system
over \(\mathbf F_{32003}\) is now only a superseded corroborative experiment.

Likewise, the former modular experiments for the natural multiplier pair
((B^{2t},q^{3t})) failed exact-residual-primary correction systems modulo
32003 for (t=1,2,3), with respectively 20, 220, and 816 correction
coefficients.  Those experiments do not prove characteristic-zero
inconsistency; the exact all-stage statements are the ones proved in P-037.

### P-025: formal-neighborhood exclusion of the two \((4,5)\) types

The Bănică--Forster transition calculation was carried through separately for
the two types in P-016 on the explicit curve \(C_0\).

For type A, \((\deg L,\deg D)=(-7,3)\), the lower extension and epimorphism
conditions exhaust all parameter strata.  The unique epimorphic route through
multiplicity four has final obstruction in \(H^1(O(-9))\) with coordinates

\[
 \left(-\frac{15}{512},-\frac5{256},\frac5{128},-\frac5{64},
 \frac5{32},-\frac5{16},\frac58,\frac{15}{4}\right),
\]

which is nonzero.  Therefore type A cannot support a \((4,5)\) complete
intersection on \(C_0\).

For type B, \((\deg L,\deg D)=(-6,1)\), a crucial correction is that transition
coefficients must be evaluated at the moving ambient coordinate

\[
 W=\frac{z^3+a}{z^4+b},
\]

not frozen at \(1/z\).  On the dense chart \(b_0b_1\ne0\), normalized by
\(b_0=b_1=1\) with parameters \((r,s)=(a_0,a_1)\), the second-neighborhood
class has Laurent coefficients \(c_1,c_2,c_3\).  Its required rank-one
condition is

\[
 c_1c_3-c_2^2=0.
\]

Exact elimination through the next extension gives the eliminant

\[
 (2s-1)^3(2s+1)(12s^2+20s+11)^3.
\]

After the corresponding chart and epimorphism checks, the only dense-chart
point reaching multiplicity four is

\[
 (r,s)=(0,-1/2).
\]

At that point one may take

\[
 \delta_U=-4z,\quad\delta_V=-4,
\]

\[
 \gamma_U=\tfrac32z^2+3z+2,\quad\gamma_V=0,
\]

\[
 \rho_U=-(36z^4+108z^3+136z^2+72z+16),\quad\rho_V=0.
\]

The required final generator on the other chart is not the old \(E_V\) but
\(F_V=-64m_V\).  Put

\[
 Q=3z^2+6z+4
\]

and

\[
\begin{aligned}
 P={}&81z^8+486z^7+1341z^6+2160z^5+2204z^4\\
    &+1464z^3+656z^2+224z+64.
\end{aligned}
\]

Exact moving-\(W\) reduction modulo the multiplicity-four ideal gives the
final cocycle

\[
 h_4=-\frac{8P(z)}{Q(z)z}.
\]

If

\[
 R=81z^7+486z^6+1341z^5+2160z^4+2204z^3
   +1464z^2+608z+128,
\]

then \(P-16Q=zR\), so

\[
 h_4+\frac{128}{z}=-\frac{8R}{Q}.
\]

On the cover \(D(Q)\subset\mathbb A^1_z\) and
\(\mathbb P^1\setminus\{z=0\}\), the right-hand term is regular on the first
chart and no second-chart coboundary can remove \(z^{-1}\).  Hence

\[
 [h_4]=[-128z^{-1}]\ne0\quad\text{in }H^1(O(-12)).
\]

This independently audited computation excludes the unique dense survivor.

On the boundary \(b_0=0\), normalize \(a_0=b_1=1,a_1=t\).  The exact
second-neighborhood rank equation is

\[
 q(t)=1-8t^2+12t^4-72t^6=0.
\]

A separate exact moving-\(W\) implementation through the next neighborhood
gives a class in \(H^1(O(-7))\) whose first coordinate is

\[
 H_1=-24t(36t^4+3t^2+1).
\]

With \(x=t^2\), the identity

\[
 3(20x+3)(1-8x+12x^2-72x^3)
 +4(30x^2-3x+2)(36x^2+3x+1)=17
\]

shows that \(H_1\) is a unit on the full rank-one boundary scheme in
characteristic zero.  Thus every point with \(b_0=0\) is excluded.  The
durable script `computations/verify_typeb45_boundary.py` reproduces the full
moving-frame calculation and all six Cech coordinates.

One former conclusion was nevertheless false: the coordinate-reversing
involution does not simply reverse the quotient coefficients in the canonical
split frames.  Its actual action is, up to common scale,

\[
 (a_0,a_1,b_0,b_1)\longmapsto
 \left(\frac{b_1}{2},\frac{b_0}{2},2a_1,2a_0\right).
\]

It sends the part of \(b_1=0\) with \(a_0\ne0\) into the now-excluded dense
chart, but preserves the genuine corner

\[
 a_0=b_1=0,\qquad a_1b_0\ne0.
\]

Normalize \(b_0=1,a_1=t\).  Its second-neighborhood class has

\[
 c_1=c_3=0,\qquad
 c_2=\frac{(2t+1)(12t^2+4t+3)}8.
\]

Therefore exactly three rank-zero parameters remain:

\[
 \boxed{t=-\frac12\quad\text{or}\quad12t^2+4t+3=0.}
\]

The involution fixes the first and exchanges the two quadratic roots by
\(t\mapsto1/(4t)\).  At each of these three parameters the raw
second-neighborhood representative \(h_2\) vanishes identically, not merely
in cohomology.  Let \(\delta\in H^0(O(1))\) be any nonzero proposed killing
section for the double-to-triple extension.  In the exact moving frames the
compatible correction satisfies

\[
 \delta_Uh_2+\gamma_U=z^{-3}\gamma_V.
\]

Thus \(\gamma_U=z^{-3}\gamma_V\) is a global section of \(O(-3)\), so
\(\gamma_U=\gamma_V=0\).  Every nonzero section of \(O(1)\) has a zero
\(P\).  At that point the proposed transverse triple has ideal

\[
 (m\ell,m^2,\ell^3),
\]

whose quotient has basis \(\{1,m,\ell,\ell^2\}\) and length four.  Away from
\(P\), \(\delta\) is a unit and the quotient has the required basis
\(\{1,\ell,\ell^2\}\) and length three.  The unavoidable length jump means
that the extension map is not epimorphic and the proposed triple is not flat.
No one of the three rank-zero corner points therefore extends to an
admissible triple.  This closes the corner and excludes type B on all charts.

The durable script `computations/verify_typeb45_corner.py` reproduces the
full moving-\(W\) second-order coefficient, the rank-zero factorization, and
the special-fiber length calculation.  Its finite-degree \(\gamma\) and
hard-coded monomial checks are only witnesses; the exhaustive proof is the
line-bundle argument \(H^0(O(-3))=0\) and the displayed quotient basis.  The
older frozen-frame `typeb_generic.py` remains invalid,
and the rejected simple coefficient-reversal argument must not be reused.

### P-026: a conditional ambient finite-jet reduction for \((4,5)\)

There is a complementary reduction directly in the ambient quartic and
quintic coefficient spaces.  In the balanced frame \((U,V)\), a quartic first
normal form is

\[
 P(z)U+Q(z)V,\qquad \deg P,\deg Q\le9.
\]

Its image has rank 17 and is cut out by

\[
 P_1=2Q_2,\qquad P_4=2Q_5,\qquad P_7=2Q_8.
\]

The quintic first-normal map is surjective onto
\(H^0(O(13))^2\), with seven-dimensional kernel \(qI_C(3)\).  P-016 becomes
the following two quartic strata:

\[
 \begin{array}{c|c|c}
 \text{type}&L_1&\gcd(P,Q)\text{ degree}\\\hline
 A&O(-7)&9\\
 B&O(-6)&8.
 \end{array}
\]

Write the proportional first normal forms as \(f_1=hL\) and \(g_1=kL\).
The previous version asserted, without proving the necessary vertical-divisor
inequality, that after subtracting an ambient linear multiple of the quartic a
genuine mate must satisfy

\[
 g_1=z^2f_1.
\]

That assertion is valid only on the sublocus where the rational quotient
\(k/h\) is regular and can be normalized by ambient linear sections.  It is
not automatic.  The local multiplicity-five model

\[
 F=tu+v^5,\qquad G=u
\]

has radical \((u,v)\), constant transverse length five, and first-normal
ratio \(1/t\).  Proper residual intersection on the quadric constrains the
total intersection divisor but does not force \(h\mid k\); multiplicity may
concentrate at vertical order jumps.  Consequently the universal P-026
reduction is disproved, while the calculation below remains exact on its
regular-ratio sublocus.

On that sublocus the factor \(z^2\) represents the unique missing section in
\(H^0(C,O_C(1))/H^0(\mathbf P^3,O(1))\).  Once a quintic with this first form
is chosen, all others are obtained by adding seven coefficients in
\(qI_C(3)\).  Eliminating the quartic formally, contact at least five is
equivalent to a finite linear system in those seven variables, with the
coefficients of the transverse terms \(t^2,t^3,t^4\) as equations.  The
conditional problem is therefore equality of the ranks of this matrix and its
augmented matrix, including lower-rank boundary strata.  The missing
nonregular-ratio strata require a separate vertical-divisor parameterization.

The exact verifier proves three family exclusions by explicit augmented
minors:

\[
 F=x_1A+\lambda q^2:\quad 2\lambda^3,
\]

\[
 f_1=(z^9+1)U:\quad -72,
\]

\[
 f_1=(z^8+1)(U+zV):\quad -48.
\]

Thus every nonreducible member of each displayed family in the normalized
sublocus fails order-five contact.  These certificates neither establish the
normalization for an arbitrary pair nor replace elimination within the
conditional strata.  The durable script is
`research/scratch/degree6/verify_mixed45_reduction.py`, with recorded SHA-256
`862ec150664459fc94187164bcaa1d25e87c5f815e589fff1608a28efc6a89d5`.

### P-028: a degree-(4,p) pair for the monomial quartic in every prime characteristic p at least 7

Let the ground field be algebraically closed of prime characteristic \(p\ge7\).
Choose positive integers \(b,c\) with

\[
 3b+4c=p
\]

and put \(a=p-b-c=2b+3c\).  Such a choice always exists: if
\(p\equiv3\pmod4\), take \(b=1,\ c=(p-3)/4\); if
\(p\equiv1\pmod4\), take \(b=3,\ c=(p-9)/4\).  Define

\[
 F=x_0x_3^3-x_2^4,\qquad
 G=x_0^a x_2^b x_3^c-x_1^p.
\]

Both vanish on

\[
 C_0=[s^4:s^3t:st^3:t^4],
\]

because \(4a+b=3p\), which follows from \(a=2b+3c\) and
\(p=3b+4c\).

On the affine chart \(x_0=1\), the cusp equation \(F=0\) has normalization
\(x_2=v^3,\ x_3=v^4\).  The second equation becomes
\(v^{3b+4c}=x_1^p\), hence \(v^p=x_1^p\).  In characteristic \(p\) this is
\((v-x_1)^p=0\), so the reduced common zero set is the affine part of \(C_0\).
On the boundary \(x_0=0\), \(F=0\) forces \(x_2=0\), and then \(G=0\) forces
\(x_1=0\); the only projective point is \([0:0:0:1]\), the missing point of
\(C_0\).  Therefore

\[
 \sqrt{(F,G)^{\mathrm{sat}}}=I_{C_0}.
\]

This improves the second degree of the general Frobenius construction for
this explicit curve from \(4p\) to \(p\).  It is a positive-characteristic
result and supplies no specialization argument in characteristic zero.

### P-029: complement morphisms and two-generated positive line bundles

Let \(C\subset\mathbf P^3_k\) be an integral curve and put
\(U=\mathbf P^3_k\setminus C\).  Then the following are equivalent:

1. \(C\) is the set-theoretic intersection of two surfaces;
2. \(U\) admits a nonconstant morphism \(U\to\mathbf P^1\);
3. for some \(d>0\), the line bundle \(O_U(d)\) is generated by two global
   sections.

If \(C=V(F,G)\) set-theoretically, replace \(F,G\) by suitable powers to give
them the same degree.  The pair has no common zero on \(U\), so
\([F:G]\) defines a map \(U\to\mathbf P^1\) and generates \(O_U(d)\).  The map
is nonconstant: if its value were \([a:b]\), then \(bF-aG\) would vanish on
the dense open set \(U\), hence everywhere, making \(F,G\) proportional and
their common zero set a hypersurface rather than \(C\).

Conversely, the class-group localization sequence has no boundary divisor
term because \(C\) has codimension two, and therefore gives

\[
 \operatorname{Pic}(U)=\operatorname{Cl}(U)
 \simeq\operatorname{Cl}(\mathbf P^3)\simeq\mathbf Z.
\]

Here regularity of \(U\) identifies its Picard and class groups.  Moreover,
reflexive extension across the codimension-two complement gives

\[
 H^0(U,O_U(d))=H^0(\mathbf P^3,O_{\mathbf P^3}(d))
\]

for every integer \(d\).  Thus the pullback of \(O_{\mathbf P^1}(1)\) is
\(O_U(d)\) for some integer \(d\).  It cannot have \(d<0\), because then it
has no global sections; if \(d=0\), its two defining sections are constants
and the morphism is constant.  Hence \(d>0\).

The two pulled-back coordinate sections extend uniquely to homogeneous
degree-\(d\) forms \(F,G\) on \(\mathbf P^3\).  They have no common zero on
\(U\), hence \(V(F,G)\subseteq C\).  They cannot have a common nonconstant
factor, because its hypersurface would be contained in the one-dimensional
curve \(C\).  Therefore \((F,G)\) has height two, the forms are a regular
sequence, and their projective common zero scheme is nonempty and pure
one-dimensional.  Its support is a one-dimensional closed subset of the
integral curve \(C\), hence all of \(C\).

Conversely, two global sections generating \(O_U(d)\) define a morphism
\(U\to\mathbf P^1\).  If \(d>0\), this line bundle is nontrivial in
\(\operatorname{Pic}(U)\simeq\mathbf Z\), so the morphism cannot be constant.
This completes all three implications.

Let \(\mathcal J=(F,G)\) be the resulting ideal sheaf.  Since \(F,G\) form a
regular sequence, \(\mathcal J\) is of linear type.  The closure of the graph
of \([F:G]\) is therefore the blowup
\(\operatorname{Bl}_{\mathcal J}\mathbf P^3\), embedded in
\(\mathbf P^3\times\mathbf P^1\) by the single bihomogeneous equation
\(uG-vF=0\).  Without the regular-sequence hypothesis that single-equation
Rees description can acquire an extraneous component.  The reformulation is
exact, but by itself it does not construct the morphism or a two-section
generating pair.

### P-030: residual-root multiplicities in the split sextic cases

Assume the split/no-vertical hypotheses of P-020 and P-023.  Let
\(K_i\) be the full Cartier cluster lying over a distinct root of the residual
binary quartic, including its root multiplicity and every exceptional
component required by resolution, and let that multiplicity be \(\mu_i\).
The four total units satisfy \(\sum_i\mu_i=4\).

With \(K_0=2H-E\), the intersection identities on the resolved normalization
are

\[
 H\cdot K_i=\mu_i,\qquad E\cdot K_i=3\mu_i,\qquad
 K_0\cdot K_i=-\mu_i,\qquad L\cdot K_i=0.
\]

The same Hodge-index equality used in P-023, now applied to the full cluster
rather than to a reduced branch, forces the low-degree normalization branch
to meet \(K_i\) in

\[
 \Gamma_{\mathrm{low}}\cdot K_i=
 \begin{cases}
   \mu_i/4,&d=0,\\
   \mu_i/2,&d=1.
 \end{cases}
\]

These are intersections of Cartier divisors and therefore integers.  In the
\(d=0\) case every \(\mu_i\) is divisible by four, so the only partition is
\([4]\).  In the \(d=1\) case every \(\mu_i\) is even, leaving only
\([4]\) and \([2,2]\).  The conclusion concerns full Cartier clusters; it
must not be applied to only the reduced visible branch over a multiple root.

This removes the squarefree residual case already excluded in P-023 and all
partitions except the three displayed possibilities.  It does not yet exclude
the surviving multiple-root configurations.

### P-031: finite pole-divisor strata for the nonregular mixed pairs

The ratio gap in P-021 and P-026 is not an arbitrary infinite-dimensional
phenomenon.  It has an exact divisor parameterization.  Let \(b=5\) or \(6\)
and put \(\delta=4(b-4)\), so \(\delta=4\) or \(8\).  On
\(E=\mathbf P(N_{C_0}^*)\), an order-one degree-\(d\) normal divisor has
class \((4d-7,1)\).  Write the primitive common horizontal factor and its
vertical coefficients as

\[
 f_1=hL,\qquad g_1=kL,\qquad L\sim(e,1),
\]

\[
 \deg h=m=9-e,\qquad \deg k=m+\delta.
\]

For the zero divisors \(H=(h)_0\) and \(K=(k)_0\), define their coefficientwise
common part and the remaining pole and zero divisors by

\[
 A=H\wedge K,\qquad P=H-A,\qquad Z=K-A.
\]

Then

\[
 H=A+P,\qquad K=A+Z,\qquad P\wedge Z=0,
\]

\[
 c=\deg A,\qquad p=\deg P,\qquad
 c+p=9-e,\qquad \deg Z=p+\delta.
\]

The quotient \(k/h\) is a rational section of \(O_{\mathbf P^1}(\delta)\)
with divisor \(Z-P\).  It is regular exactly when \(p=0\).  Thus \(A\) records
the common vertical order jumps and \(P\) records precisely the poles omitted
by the former reductions.

Generator changes give finite principal-part quotients.  For \((4,6)\),
restriction of ambient quadrics to \(C_0\) is all of \(H^0(O(8))\), and

\[
 H^0(O(m+8))/hH^0(O(8))\simeq H^0(O_H(m+8))
\]

has dimension \(m\).  On an affine chart whose point at infinity avoids
\(H\), polynomial division and subtraction of a quadratic multiple of \(F\)
give the representative

\[
 \boxed{k=r,\qquad \deg r<m.}
\]

and \(c=\deg\gcd(h,r)\), \(p=m-c\).  This polynomial remainder is a chartwise
description of the intrinsic principal part, not a preferred global
coordinate.  For \((4,5)\), the restrictions of ambient linear forms in the
standard monomial coordinate are

\[
 W_5=\langle1,z,z^3,z^4\rangle\subset H^0(O(4)),
\]

with missing section \(z^2\).  Intrinsically there is an exact sequence

\[
 0\longrightarrow H^0(O(4))/W_5
 \longrightarrow H^0(O(m+4))/hW_5
 \longrightarrow H^0(O_H(m+4))
 \longrightarrow0.
\]

Thus the quotient has dimension \(m+1\): one missing-restriction coordinate
and an \(m\)-dimensional principal part on \(H\).  After choosing a lift \(r\)
of that principal part, it has the representative

\[
 \boxed{k=\lambda z^2h+r,\qquad \deg r<m.}
\]

Here vanishing of the principal part, equivalently \(r=0\) in any such
splitting, is exactly the regular-ratio slice used in P-026; a nonzero
principal part is the full nonregular locus.  On a chart avoiding \(H\), the
lift can be taken with \(\deg r<m\).  The invariant data are its class on
\(H\) and the pole divisor \(P\), not the chosen polynomial remainder.

For \((4,5)\), P-016 leaves gcd types \(e=0,m=9\) and \(e=1,m=8\), and P-025
eliminates the first type without any regular-ratio assumption.  Jaffe's
checked no-common-singularity theorem forces a genuine \((4,5)\) pair to
have a point where both carriers are singular.  Since \(L\) is primitive,
this is exactly \(A\ne0\), or \(c\ge1\).  Hence every remaining nonregular
candidate satisfies

\[
 \boxed{e=1,\qquad 1\le p\le7,\qquad c=8-p,\qquad
 \deg Z=p+4.}
\]

There are seven numerical pole-length strata.

For \((4,6)\), nonregularity first gives \(0\le e\le8\) and \(p\ge1\).
The pair \((4,6)\) is likewise absent from Jaffe's list for carriers with no
common singular point, so again \(c\ge1\).  Before using the global
multiplicity-six filtration, the exact first-normal reduction is

\[
 \boxed{0\le e\le7,\qquad 1\le p\le8-e,\qquad
 c=9-e-p,\qquad \deg Z=p+8.}
\]

This is a triangle of \(8+7+\cdots+1=36\) preliminary numerical strata, while
the regular branch has P-021's preliminary list \(p=0,\ e=0,1,2,3\).  P-042
later imposes the global lci condition \(e\in\{0,1\}\), leaving only 15 of the
nonregular strata and only the first two regular values.

Finite flatness controls special transverse orders but not pole length.  At a
common singular point a length-five fiber forces orders \((2,2)\); a
length-six fiber permits \((2,2),(2,3),(3,2)\).  Nevertheless, for every
\(\alpha\ge1\),

\[
 F=t^\alpha u+v^n,\qquad G=u
\]

defines \((u,v^n)\), which is free of rank \(n\) over \(k[[t]]\), while its
first-normal ratio is \(t^{-\alpha}\).  No bound on \(p\) can therefore follow
from flat transverse length alone.

The unique quadric gives useful exact tangency budgets.  If
\(D_0=L\cap S_q\), then

\[
 R_4|_{C_0}=D_0+H,\qquad R_b|_{C_0}=D_0+K,
\]

and their common restriction has degree
\(\deg(D_0+A)=10-p\).  The residual intersections on the quadric have total
length ten for \((4,5)\) and fourteen for \((4,6)\).  If

\[
 \epsilon_x=i_x(R_4,R_b)-\operatorname{ord}_x(D_0+A),
\]

then \(\epsilon_x\ge0\) and

\[
 \boxed{\sum_x\epsilon_x=p\quad\text{for }(4,5),}
\]

\[
 \boxed{\sum_x\epsilon_x=4+p\quad\text{for }(4,6).}
\]

These are exact constraints, not contradictions.  They show that every unit
of pole length must reappear as residual excess tangency.  P-038 completes the
formerly conjectural defect comparison in the opposite direction:
\(A=2D\) scheme-theoretically.  Hence the type-B \((4,5)\) list collapses to
the single stratum \((c,p,\deg Z)=(2,6,10)\).  P-042 subsequently restricts
every hypothetical \((4,6)\) lci to horizontal degree \(e=0\) or \(1\), so
only 15 of the 36 preliminary nonregular strata remain live.

### P-032: normalization and conductor criterion for singular support

Let \(C\subset\mathbf P^3_k\) be an integral curve of degree \(d\), let
\(X=V(F)\) be an integral carrier of degree \(a\), and let
\(\nu:S=X^\nu\to X\) be its finite normalization.  Put
\(H=\nu^*O_X(1)\), and write

\[
 (\nu^{-1}C)_{\mathrm{red}}=\Gamma_1\cup\cdots\cup\Gamma_s,\qquad
 \delta_i=[k(\Gamma_i):k(C)].
\]

Let \(Q_X=\nu_*O_S/O_X\), let
\(\mathfrak c=\operatorname{Ann}_{O_X}(Q_X)\), and define the full,
potentially nonreduced conductor schemes

\[
 \Delta=V_X(\mathfrak c),\qquad
 \widetilde\Delta=S\mathbin{\times}_X\Delta.
\]

For a fixed
\(b>0\), the following are equivalent:

1. there is a degree-\(b\) form \(G\), not divisible by \(F\), with
   \(|V(F,G)|=C\);
2. there are positive integers \(m_i\), an effective Cartier divisor
   \(A=\sum_i m_i\Gamma_i\), and an isomorphism
   \(\phi:O_S(A)\xrightarrow{\sim}O_S(bH)\) such that the transported
   canonical section \(s_A=\phi(1_A)\in H^0(S,O_S(bH))\) maps to zero in
   \(H^0(X,Q_X\otimes O_X(b))\);
3. the same divisor data exist and there is a section
   \(t_\Delta\in H^0(\Delta,O_\Delta(b))\) such that
   \(s_A|_{\widetilde\Delta}=\nu_\Delta^*t_\Delta\).

The choice of \(\phi\) changes \(s_A\) only by a scalar, so the descent
condition is independent of that choice.  It is essential here that \(A\),
not necessarily each prime \(\Gamma_i\), is Cartier.

A mate restricts to a section on \(X\), and its pullback divisor has support
exactly \(\nu^{-1}C\), giving condition 2.  Conversely, zero normalization
defect means that \(s_A\) descends to a section of \(O_X(b)\).  The restriction

\[
 H^0(\mathbf P^3,O(b))\longrightarrow H^0(X,O_X(b))
\]

is surjective because \(H^1(\mathbf P^3,O(b-a))=0\), so the descended section
has an ambient lift \(G\).  Finite surjectivity of \(\nu\) shows that its zero
support on \(X\) is exactly \(C\).  Conditions 2 and 3 are equivalent by the
conductor fiber-product sequence

\[
 0\longrightarrow O_X\longrightarrow
 \nu_*O_S\oplus O_\Delta\longrightarrow
 \nu_*O_{\widetilde\Delta}\longrightarrow0,
\]

tensored by \(O_X(b)\).

Every such mate satisfies

\[
 \boxed{ab=d\sum_i m_i\delta_i,}
\]

because

\[
 ab=(bH)\cdot H=A\cdot H
 =\sum_i m_i(H\cdot\Gamma_i)
 =d\sum_i m_i\delta_i.
\]

Indeed \(H^2=a\) because normalization is finite birational and \(X\) has
degree \(a\), while

\[
 H\cdot\Gamma_i
 =\deg((\nu|_{\Gamma_i})^*O_C(1))
 =\delta_i d.
\]

The degree \(\delta_i\) is the full function-field degree; no separability is
required.  Because normalization is finite, there are no omitted divisors
contracted to closed points.

The conductor condition is indispensable.  At the generic point of a
transversely cuspidal carrier, take

\[
 K[[t^2,t^3]]\subset K[[t]],\qquad K=k(C).
\]

The normalized divisor \(t=0\) is Cartier, but its section \(t\) does not
descend; only valuations in the semigroup
\(\{0,2,3,4,\ldots\}\) do.  Thus positivity, normalized divisor support, and
linear equivalence on \(S\) do not suffice.  The valuation vector must belong
to the multibranch value semigroup and pass conductor gluing.

There is also a module formulation, but it must retain conductor descent.  Set

\[
 M_A=\nu_*O_S(-A),\qquad
 I_A=O_X\cap M_A
\]

inside the total quotient sheaf \(K(X)\).  A mate with normalized divisor
\(A\) is equivalently an inclusion

\[
 O_X(-b)\hookrightarrow I_A\subset O_X
\]

whose induced map upstairs has image exactly \(O_S(-A)\).  Equivalently, one
may map first to \(M_A\), but the composite into \(\nu_*O_S\) must factor
through \(O_X\).  The conductor-supported quotient

\[
 M_A/I_A\hookrightarrow Q_X
\]

is exactly the missing descent information.  Omitting this factorization is
false already for
\(K[[t^2,t^3]]\subset K[[t]]\): the map \(1\mapsto t\) lands in \(tK[[t]]\)
and has the desired normalized divisor, but it does not land in the cusp
ring.  Thus normalized rank-one data alone are not a substitute for the
conductor condition.

The numerical Cartier-index compression in P-015 extends further than originally
stated.  Assume characteristic zero, allow \(C\) to be any integral curve,
and let \(X\) be a minimum-degree integral carrier occurring in a defining
pair.  If \(X\) is regular at the generic point of \(C\), then
\(C\cap\operatorname{Sing}X\) is finite and the same almost-Cartier argument
gives

\[
 eC\sim nH,\qquad n=\frac{de}{a}\in\mathbf Z_{>0},\qquad
 n\ge a,\qquad e\ge\frac{a^2}{d}.
\]

At the generic point the mate first gives a scalar relation
\(r[C]=b[H]\) in \(\operatorname{APic}X\), with \(dr=ab\).  Here \(e\) is the
lcm of the local orders of \([C]\) in the almost-Cartier groups at those
finitely many singular points, so \(e\mid r\) and \(eC\) is Cartier.  The
proof then uses the same
characteristic-zero torsion-freeness of
\(\operatorname{Pic}X/\mathbf ZH\) as P-015.  Intrinsic singularities of
\(C\) on the regular locus of \(X\) cause no problem, since a height-one
prime on a regular surface is Cartier.  What fails when \(X\) is singular at
the generic point of \(C\) is the scalar relation \(r[C]=b[H]\); it must be
replaced by the branch-valuation vector and conductor condition above.

Finally, let
\(\mathcal J=(F,G)O_{\mathbf P^3}\) have no common factor, let
\(B=\operatorname{Bl}_{\mathcal J}\mathbf P^3\), and let \(W=B^\nu\).
Call a prime divisor \(E\subset W\) exceptional when
\(\operatorname{ord}_E(\mathcal J)>0\).  Then

\[
 \sqrt{(F,G)^{\mathrm{sat}}}=I_C
 \quad\Longleftrightarrow\quad
 \text{the set of exceptional-prime centers on \(\mathbf P^3\) is
 exactly \(\{C\}\)}.
\]

This follows because a height-two two-generated ideal is an unmixed lci and
its exceptional divisor dominates every reduced curve component.  It checks
the support of a proposed pair but, like the graph formulation in P-029, does
not construct one.

### P-033: the global Chow-resultant certificate

Let \(\mathbb G=\operatorname{Gr}(2,4)\) be the Grassmannian of lines in
\(\mathbf P^3\), with tautological rank-two bundle \(\mathcal S\).  For forms
\(F,G\) of positive degrees \(a,b\), restrict them to the universal line.
Twisting the universal-line Koszul complex by \(O(a+b-1)\) and pushing forward
gives the square Sylvester bundle map

\[
 \Phi_{F,G}:
 \operatorname{Sym}^{b-1}\mathcal S^\vee\oplus
 \operatorname{Sym}^{a-1}\mathcal S^\vee
 \longrightarrow
 \operatorname{Sym}^{a+b-1}\mathcal S^\vee.
\]

Its determinant is the binary resultant

\[
 R_{F,G}\in H^0(\mathbb G,O_{\mathbb G}(ab)).
\]

The raw Koszul complex does not itself have one ordinary matrix determinant;
the twisted pushforward above is the precise construction.

For \(a,b>0\), \(R_{F,G}\not\equiv0\) exactly when \(F,G\) have no common
factor.  In that case \(Y=V(F,G)\) is an unmixed complete-intersection curve.
If

\[
 [Y]=\sum_i m_i[C_i]
\]

is its fundamental cycle, the resultant is its Chow form:

\[
 R_{F,G}=\lambda\prod_i\operatorname{Ch}_{C_i}^{m_i}.
\]

Consequently, for an integral curve \(C\) of degree \(\delta\),

\[
 \boxed{
 V(F,G)_{\mathrm{red}}=C
 \quad\Longleftrightarrow\quad
 R_{F,G}=\lambda\operatorname{Ch}_C^{ab/\delta}.
 }
\]

The equality is one of sections on \(\mathbb G\), or of Pluecker polynomials
modulo the Pluecker relation.  It detects support and generic multiplicity,
not the special-point nilpotent structure of the primary thickening.

For \(C_0=[s^4:s^3t:st^3:t^4]\), orient

\[
 p_{ij}=A_iB_j-A_jB_i.
\]

Direct exact calculation gives the 10-term Chow quartic

\[
\begin{aligned}
\operatorname{Ch}_{C_0}={}&
 -p_{02}^3p_{23}
 +2p_{02}^2p_{13}^2
 -4p_{02}p_{03}^2p_{13}
 -5p_{02}p_{03}p_{12}p_{13}\\
&-p_{02}p_{12}^2p_{13}
 +p_{03}^4
 +3p_{03}^3p_{12}
 +3p_{03}^2p_{12}^2
 +p_{03}p_{12}^3
 -p_{01}p_{13}^3.
\end{aligned}
\]

The verifier expands the resultant of

\[
 A_0s^4+A_1s^3t+A_2st^3+A_3t^4
\]

and its \(B\)-analogue and proves exact equality with this formula after
substituting the six minors.  The durable check is
research/computations/verify_chow_form.py.  Thus a \((4,5)\) pair must satisfy

\[
 R_{F,G}=\lambda\operatorname{Ch}_{C_0}^{5}.
\]

This is a genuinely global computational representation, independent of the
chosen first-normal frame.  Mathematically it is the classical Chow form of a
complete-intersection cycle, hence a reformulation and certificate rather
than a new existence theorem.

### P-034: ordinary K-theory retains only the Bezout divisibility

Let \(U=\mathbf P^3\setminus C\), where \(C\) is integral of degree
\(\delta\) over an algebraically closed field, and put

\[
 u=1-[O_U(-1)].
\]

Localization in coherent \(G\)-theory, together with regularity of
\(\mathbf P^3\) and \(U\), gives

\[
 G_0(C)\longrightarrow
 K_0(\mathbf P^3)=\mathbf Z[u]/(u^4)
 \longrightarrow K_0(U)\longrightarrow0.
\]

A closed point contributes \(u^3\), while

\[
 [O_C]=\delta u^2+(\chi(O_C)-\delta)u^3.
\]

Every coherent sheaf on the integral curve has \(u^2\)-coefficient equal to
its generic rank times \(\delta\).  Because the field is algebraically closed,
the image is exactly \((\delta u^2,u^3)\).  Therefore

\[
 \boxed{K_0(U)\simeq\mathbf Z[u]/(u^3,\delta u^2).}
\]

If a degree-\((a,b)\) pair has no common zero on \(U\), its Koszul sequence
forces

\[
 (1-t^a)(1-t^b)=0,\qquad t=[O_U(-1)]=1-u.
\]

Modulo \(u^3\), this is \(ab\,u^2=0\), equivalently

\[
 \delta\mid ab.
\]

This is only the \(K_0\) class relation of a pair.  It does not detect whether
the sections exist or generate, extension classes, unstable cancellation,
Euler-class or higher-\(K\) obstructions, or the formal neighborhood.  Thus
ordinary \(K_0\) is exhausted as a uniform obstruction but no broader
statement about all stable invariants is justified.

### P-035: arithmetically Gorenstein thickening criterion

Let \(S=k[x_0,x_1,x_2,x_3]\) and \(P=I_C\).  Then

\[
 C\text{ is an STCI}
\]

if and only if there is a homogeneous \(P\)-primary ideal \(J\) of height two
such that \(S/J\) is a graded Gorenstein ring.

A defining pair gives \(J=(F,G)\), a height-two graded complete intersection.
Conversely, a height-two graded Gorenstein quotient is Cohen--Macaulay, so
\(J\) is a grade-two perfect ideal.  In its Hilbert--Burch resolution the
Cohen--Macaulay type is \(\mu(J)-1\).  Gorenstein type one therefore forces
\(\mu(J)=2\), so \(J\) is a complete intersection and
\(\sqrt J=P\).

Equivalently, \(C\) supports an arithmetically Gorenstein codimension-two
thickening.  The adjective is essential: a merely locally or generically
Gorenstein thickening need not be ACM or have a two-generated homogeneous
ideal.  In particular every smooth curve is locally Gorenstein, so that weaker
condition cannot decide the present problem.

### P-036: an unconditional Chow-pencil exclusion at \((4,5)\)

For

\[
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

consider the Schubert pencil

\[
 L_{[\beta:\gamma]}:\quad x_1=0,\quad
 \gamma x_3-\beta x_0=0,
\]

parametrized by

\[
 [x_0:x_1:x_2:x_3]=[\gamma U:0:V:\beta U].
\]

The only nonzero Pluecker coordinates are
\(p_{01}=\beta\) and \(p_{13}=\gamma\).  Substitution into P-033's exact
Chow quartic, or direct computation of
\(\operatorname{Res}(s^3t,\gamma t^4-\beta s^4)\), gives

\[
 \operatorname{Ch}_{C_0}|_L=-\beta\gamma^3.
\]

Consequently any degree-\((4,5)\) pair supported on \(C_0\) must satisfy

\[
 \operatorname{Res}_{U,V}(F|_L,G|_L)
 =\mu\beta^5\gamma^{15},\qquad \mu\ne0.
\]

Exact degree-component linear algebra gives

\[
 \dim I_{C_0}(4)=18,\qquad \dim I_{C_0}(5)=35,
\]

and the stronger intersections

\[
\begin{aligned}
 J_4&=I_{C_0}(4)\cap(x_1,x_2x_3,x_3^2)_4,
 &\dim J_4&=13,\\
 J_5&=I_{C_0}(5)\cap(x_1,x_3^2,x_2^2x_3)_5,
 &\dim J_5&=28.
\end{aligned}
\]

For the first dimension, the quotient by
\((x_1,x_2x_3,x_3^2)\) has degree-four basis

\[
 x_0^4,\ x_0^3x_2,\ x_0^2x_2^2,\ x_0x_2^3,\ x_2^4,\ x_0^3x_3.
\]

The image of \(I_{C_0}(4)\) is the five-dimensional hyperplane omitting
\(x_0^4\), with representatives
\(x_0A,x_0B,x_0D,x_2D,x_0^2q\).  This gives \(18-5=13\).
Similarly, the quotient by \((x_1,x_3^2,x_2^2x_3)\) has eight degree-five
basis monomials, and the image of \(I_{C_0}(5)\) is the seven-dimensional
hyperplane omitting \(x_0^5\), with representatives

\[
 x_0^2A,\ x_0^2B,\ x_0^2D,\ x_0x_2D,\ x_2^2D,\ x_0^3q,\ x_0^2x_2q.
\]

Hence \(\dim J_5=35-7=28\).

If \(F\in J_4\), then \(F|_L=\beta\widehat F\), and at \(\beta=0\) the
residual form \(\widehat F\) is divisible by \(V\).  Since
\(F|_{L_0}=0\), support equality would force \(G|_{L_0}=cV^5\).
Scaling the quartic contributes \(\beta^5\) to the resultant, while the
shared residual \(V\)-root contributes at least one more order.  Thus the
resultant has \(\beta\)-order at least six, not five.

If \(G\in J_5\), write \(G|_L=\beta\widehat G\).  At \(\beta=0\),
\(\widehat G\) is divisible by \(V^2\), while support equality forces
\(F|_{L_0}=cV^4\).  Scaling the quintic contributes \(\beta^4\), and the
specialized Sylvester matrix has corank at least two, so the residual
determinant contributes at least two further orders.  Again the total
\(\beta\)-order is at least six.  Therefore no member of \(J_4\) or \(J_5\)
can occur in a \((4,5)\) pair.  In particular, the simpler contained spaces
\(I_4\cap(x_1,x_3^2)\) and \(I_5\cap(x_1,x_3^2)\), of dimensions 10 and 25,
remain excluded, as does the whole family

\[
 F=x_1A+\kappa q^2
\]

is excluded against every quintic mate, without the regular-ratio assumption
used by P-026.  The involution

\[
 (x_0,x_1,x_2,x_3)\longmapsto(x_3,x_2,x_1,x_0)
\]

gives the symmetric excluded spaces

\[
 I_4\cap(x_2,x_0x_1,x_0^2)_4,\qquad
 I_5\cap(x_2,x_0^2,x_0x_1^2)_5,
\]

again of dimensions 13 and 28, including
\(F=x_2D+\kappa q^2\).

One pencil is nevertheless not exhaustive.  The explicit forms

\[
\begin{aligned}
F={}&x_0^3x_2-x_0^3x_3+x_0^2x_1x_2-x_0x_1^3
      -x_1^2x_3^2+x_1x_2^3,\\
G={}&x_0^4x_2-x_0^4x_3+x_0^3x_1x_2-x_0^2x_1^3\\
   &-x_1x_2^2x_3^2-x_1x_2x_3^3+x_2^5+x_2^4x_3
\end{aligned}
\]

both lie in \(I_{C_0}\), and on the displayed pencil their resultant is
exactly

\[
 -2\beta^5\gamma^{15}.
\]

The quartic \(F\) is absolutely irreducible in characteristic zero: as a
quadratic in \(x_3\), its discriminant has odd degree three in \(x_2\) over
\(\overline{k}(x_0,x_1)\), and so is not a square.  Yet on the
coordinate-reversed pencil both restricted forms share the projective factor
\(U\), and the homogeneous resultant is identically zero.  This pair is a
route-limitation certificate, not an STCI candidate.

For comparison,

\[
 \dim(I_4\cap(x_1,x_3)_4)=14,\qquad
 \dim(I_5\cap(x_1,x_3)_5)=30.
\]

If both members lie in these spaces, both contain the line
\(V(x_1,x_3)\), and their restricted binary forms share the factor \(U\);
the resultant is identically zero.  This simultaneous case is therefore a
common-line exclusion, not merely a lower bound on \(\beta\)-adic order.

The exact script `computations/verify_chow_pencil_45.py` checks the dimensions,
the stronger monomial-ideal intersections, the Chow restriction, the
coefficient-factor claims, and the explicit one-pencil survivor and reversed
failure.  Passing one pencil is only necessary; P-036 is a methodological
family exclusion, while P-040 closes degree \((4,5)\) by the independent
multiple-structure route.

### P-037: all-stage local-cohomology obstruction through degree three

Continue with the notation of P-024 and suppose

\[
 F\alpha=u,\qquad G\alpha=v,qquad F,G\in S_d
\]

for an arbitrary element \(\alpha\in H_I^2(S)\); no finite direct-limit stage
is fixed.  Associativity gives \(Gu=Fv\).  On
\(C_0=[s^4:s^3t:st^3:t^4]\), the first-socle symbols of \(u,v\) are,
up to a common scalar, \((s^2,t^2)\).  Hence

\[
 s^2G|_{C_0}=t^2F|_{C_0}.
\]

Unique factorization gives either both restrictions zero or

\[
 F|_{C_0}=s^2h,\qquad G|_{C_0}=t^2h,\qquad \deg h=4d-2.
\]

If \(h\ne0\), choose any projective zero \(P\) of \(h\).  After completing
along the curve at \(P\), write

\[
 R=A_P[[\xi,\eta]],\qquad A_P\simeq k[[c]],\qquad
 E=H^2_{(\xi,\eta)}(R).
\]

Every element of \(E\) has finite negative \(\xi,\eta\)-support.  If
\(K=k((c))\) and \(e=[1/(\xi\eta)]\), then

\[
 E\hookrightarrow E\otimes_{A_P}K,qquad E\cap Ke=A_Pe.
\]

Over \(K\), the nonzero curve restriction of the appropriate multiplier is a
unit, and the ancestor equation uniquely forces the coefficient of the socle
term to be a unit times \(h^{-1}\).  Since \(h\) vanishes at \(P\), this has
negative \(c\)-valuation and cannot lie in \(A_Pe\).  The same cancellation
handles the two endpoints.  Therefore

\[
 \boxed{F,G\in I_{C_0}.}
\]

This is the exact finite-Laurent obstruction; it is not the false assertion
that a normal parameter cannot divide a local-cohomology socle class.

Now suppose the first conormal symbols of \(F,G\) are generically independent.
With

\[
 \mathcal T_n=(0:_{\mathcal H_C^2(O_{\mathbf P^3})}I^n),
\]

the ancestor then lies in \(\mathcal T_2\) but not \(\mathcal T_1\), and its
second-principal-part symbol gives a nonzero section of

\[
 (\mathcal T_2/\mathcal T_1)\otimes O_C(-d-3)
 \simeq N_C\otimes\det N_C\otimes O_C(-d-3)
 \simeq O_{\mathbf P^1}(9-4d)^2.
\]

For \(d\ge3\) this space has no global sections.  Thus every possible pair in
those degrees has proportional first conormal symbols.

The remaining low degrees close exactly.  Since \(I_2=kq\), a quadratic pair
would give, after setting \(\beta=q\alpha\), constant multiples of one class
equal to the linearly independent pair \(u,v\).  For cubics, every element is
uniquely

\[
 F=qL+aA+bB+cC.
\]

On the chart \([1:t:t^3:t^4]\), with conormal basis \((q,A)\), put

\[
 Q_F=a+bt^3-ct^6,qquad
 P_F=L|_C-bt^2+2ct^5.
\]

Writing \(T=t^3\) separates the wedge identity
\(P_FQ_G-Q_FP_G=0\) into the three residue classes modulo three.  In
characteristic zero it yields exactly two cases:

\[
 G=\lambda F,
 \qquad\text{or}\qquad
 F=qL,\ G=qM.
\]

The first would make \(v=\lambda u\); the second makes
\(L(q\alpha)=u\) and \(M(q\alpha)=v\), contradicting P-024's linear case.
Therefore no quadratic or cubic pair exists.

The sharp current conclusion is

\[
 \boxed{
 d\ge4,\qquad F,G\in I_d,\qquad
 \sigma(F)\wedge\sigma(G)=0
 }
\]

for any surviving common ancestor.  The last condition is only conormal
rank one; it does not imply scalar proportionality or a common ambient factor.
Hence P-037 is still not a proof that \(H_I^2(S)\) is non-quasi-cyclic.

### P-038: the type-B Fitting divisor is exactly \(2D\)

Let \(X=V(F_4,F_5)\) be a hypothetical type-B multiplicity-five complete
intersection supported on \(C=C_0\).  Put

\[
 J=\mathcal I_C,qquad I=\mathcal I_X.
\]

The first-normal map is

\[
 \phi:I/JI\longrightarrow J/J^2=N_C^*.
\]

It has generic rank one.  In a local conormal basis adapted to the primitive
horizontal line, if the two first forms are \(h\ell,k\ell\), its matrix is

\[
 \begin{pmatrix}h&k\\0&0\end{pmatrix}.
\]

Thus the divisor-valued Fitting ideal is

\[
 \operatorname{Fitt}_1(\operatorname{coker}\phi)
 =(h,k)=O_C(-A),
\]

where \(A=(h)_0\wedge(k)_0\).  The index is \(1\), not \(0\), because the
cokernel has generic rank one.  This Fitting ideal is invariant under all
source, target, and primitive-line basis changes.

For type B the filtration is

\[
 O_C,\quad L,\quad L^2(D),\quad L^3(2D),\quad L^4(2D),
\]

with ideals

\[
 J=I_0\supset I_1\supset I_2\supset I_3\supset I_4=I.
\]

At a point where \(D\) has local equation \(a=t^d\), the corrected
Bănică--Forster local form is

\[
 J=(x,y),\qquad I_1=(x,y^2),\qquad B=ax-y^2,
\]

\[
 I_3=(P,Q,R),qquad
 P=aB-xy,\quad Q=yB,\quad R=x^2.
\]

Modulo \(J^2\), only \(P\equiv a^2x\) remains, so

\[
 \operatorname{Im}(I_3\to J/J^2)=a^2M,qquad M=I_1/J^2.
\]

The available typeset reprint prints \(y(a-y^2)\) for the second generator,
dropping the \(x\) in \(y(ax-y^2)\).  Read literally that ideal is not flat
and is generically multiplicity one, whereas the corrected \(Q=yB\) is forced
by the preceding extension construction and gives length four.  All uses here
refer to this flat corrected formula.

The final extension is an epimorphism

\[
 \beta:I_3/JI_3\twoheadrightarrow L^4(2D),
 \qquad \ker\beta=I_4/JI_3,
\]

compatible with the natural inclusion \(L^4\hookrightarrow L^4(2D)\).  The
exact identity

\[
 y^4=a^2R-yR-xP-yQ
\]

gives \(\eta(y^4)=a^2\bar R\) modulo \(JI_3\).  Compatibility and cancellation
in the locally free target imply \(\beta(\bar R)\) is a unit.  If
\(\beta(\bar P)=\alpha\beta(\bar R)\), then a lift
\(T\in I_4\) of \(\bar P-\alpha\bar R\) satisfies

\[
 T\equiv P\equiv a^2x\pmod{J^2}.
\]

Together with \(I_4\subset I_3\), this proves the equality

\[
 \operatorname{Im}(I_4\to J/J^2)=a^2M.
\]

It globalizes to \(\operatorname{Im}\phi=M(-2D)\), so locally

\[
 \operatorname{coker}\phi\simeq O_C\oplus O_C/(a^2),qquad
 \operatorname{Fitt}_1(\operatorname{coker}\phi)=O_C(-2D).
\]

Comparison with \(O_C(-A)\) yields the scheme-theoretic identity

\[
 \boxed{A=2D.}
\]

Since type B has \(\deg D=1\), P-031's notation becomes

\[
 \boxed{c=2,\qquad p_{\mathrm{pole}}=6,\qquad \deg Z=10.}
\]

Thus the earlier conjectural direction \(A\le D\) was false; the correct
relation is \(D<A=2D\), with equal support.  This is a sharp first-normal
structural identity; by itself it is a reduction rather than an exclusion.
The separate higher-neighborhood argument in P-025, summarized in P-040,
excludes the degree pair.

### P-039: degree-four conormal rank one does not force a common factor

P-037 leaves degree four as the first possible multiplier degree.  Its
17-dimensional first-symbol space admits the sparse description

\[
 r\in\langle1,t,t^3,t^4,t^6,t^7,t^9,t^{10}\rangle,
 \qquad \deg k\le9,qquad k_9=-2r_{10},
\]

with the other row written \((R,K)\).  In the former coordinates

\[
 p=t^2r+t^3k,qquad P=t^2R+t^3K,
\]

and the wedge equation is simply

\[
 pR-rP=t^3(kR-rK)=0.
\]

The tempting claim that every polynomially coprime solution has constant
symbol ratio is false.  For any \(\lambda\ne0\), put

\[
 F_\lambda=xA+\lambda y^2q,\qquad
 G_\lambda=yA+\lambda xzq.
\]

On the affine normal chart

\[
 x=1,\qquad y=t,\qquad z=t^3+a,\qquad w=t^4+ta+b,
\]

one has the exact identities \(A=a\), \(q=b\).  Thus the conormal rows are

\[
 (r,k)=(1,\lambda t^2),\qquad
 (R,K)=(t,\lambda t^3)=t(r,k).
\]

The ratio is nonconstant, and neither form is \(q\)-divisible.  They are
nevertheless ambient-coprime.  The exact identities

\[
 xzF_\lambda-y^2G_\lambda=A^2,\qquad
 -yF_\lambda+xG_\lambda=\lambda Aq
\]

force any common irreducible divisor to divide \(A\), then to divide
\(y^2q\); but \(\gcd(A,yq)=1\).  Therefore

\[
 \gcd(F_\lambda,G_\lambda)=1.
\]

The primitive direction \((1,\lambda t^2)\) is also outside the
seven-dimensional cubic first-symbol image when \(\lambda\ne0\), so this is
not a disguised pair \(xD,yD\) with \(D\in I_3\).  The fixed ratio-
\(t\) slice already has dimension 12 before projectivizing.

P-039 is a counterexample to a reduction strategy, not evidence that an
ancestor \(\alpha\) exists.  At this point a degree-four exclusion required
second normal symbols or the global direct-limit equations; the exact
stage-two saturation already showed that the first potentially populated
stage was \(N=3\).  P-043 subsequently supplies a uniform coefficient
certificate at every stage and excludes this entire explicit family.

The exact script `computations/verify_localcoh_degree4_counterexample.py`
verifies curve membership, the two first-normal rows, the polynomial
identities, and generic coprimality over \(\mathbb Q(\lambda)\).  The written
identity/UFD argument proves coprimality for every nonzero specialization.
The script does not construct or assert a common ancestor.

### P-040: no degree-\((4,5)\) presentation of \(C_0\) in characteristic zero

Let the base field be algebraically closed of characteristic zero.  Suppose
that quartic and quintic forms \(F,G\) cut out \(C_0\) set-theoretically.
They have no common surface factor, so \(X=V(F,G)\) is an unmixed
complete-intersection curve of degree \(20\), supported on the degree-four
curve \(C_0\).  Its generic multiplicity along \(C_0\) is therefore five.

By P-011, neither degree-\(<6\) carrier can be thick along all of \(C_0\);
P-006 makes their first normal forms proportional, so the generic transverse
algebra is curvilinear of length five.  The multiplicity-five lci structure
is consequently quasiprimitive.  P-016's
exhaustive Bănică--Forster/Boratyński filtration and Euler-characteristic
calculation leave exactly the two numerical types

\[
 (\deg L,\deg D)=(-7,3)\quad\text{or}\quad(-6,1).
\]

P-025 excludes the first type by its terminal nonzero
\(H^1(O(-9))\) class.  It excludes the second on a complete parameter-chart
cover.  If the quotient is represented by
\((a_0+a_1z,b_0+b_1z)\), epimorphy requires
\(\Delta=a_0b_1-a_1b_0\ne0\).  The cases \(b_0b_1\ne0\), \(b_0=0\),
\(b_1=0,a_0\ne0\), and \(a_0=b_1=0,a_1b_0\ne0\) are respectively the
dense chart, the audited boundary, its involutive image, and the residual
corner.  The unique dense survivor has terminal class
\([-128z^{-1}]\ne0\) in \(H^1(O(-12))\); the \(b_0=0\) boundary has an
obstruction coordinate which is a unit on its rank-one scheme; the
coordinate-reversing involution covers the remaining \(b_1=0,a_0\ne0\)
part; and the three rank-zero points in the residual
\(a_0=b_1=0\) corner fail the required double-to-triple epimorphism and
flatness.

Both exhaustive types are impossible.  Hence

\[
 \boxed{\text{\(C_0\) has no characteristic-zero STCI presentation of
 degrees \((4,5)\).}}
\]

This is a degree-pair exclusion.  It does not rule out a presentation in
higher degrees and therefore is not a proof that \(C_0\) is not an STCI.
It is proved internally here; no novelty or priority claim is made.

### P-041: torsion-corrected sharpening of the surviving split sextics

Retain the split, reduced, content-free, no-vertical hypotheses of P-020,
P-023, and P-030.  The only residual binary-quartic root partitions are
\([4]\) for \(d=0\), and \([4]\) or \([2,2]\) for \(d=1\).  Over an
algebraically closed characteristic-zero field every such quartic is a square.
Writing \(h\) for the equation of \(C\) on its unique quadric \(Q=(q=0)\),

\[
 F|_Q=h^2P_2^2=(hP_2)^2.
\]

The bidegree-\((3,3)\) form \(hP_2\) lifts to a cubic
\(T\in I_C(3)\).  Hence \(F-T^2=qK\) for a quartic \(K\), and locally
\((I_C^2:q)=I_C\) gives

\[
 \boxed{F=T^2+qK,\qquad T\in I_C(3),\quad K\in I_C(4).}
\]

Every residual root selected by the low first-normal branch is also met by
the high branch.  On the exceptional divisor the first strict transform has
equation \(\ell m=0\), so its differential vanishes along the exceptional
tangent directions at such a point.  On the strict transform of \(Q\), the
residual root has multiplicity at least two, so the differential vanishes
along those tangent directions as well.  These two divisors are transverse in
the smooth blowup; consequently the first strict transform is singular at
every selected residual-root point.

The mate relations must retain their common scale \(k>0\).  They imply

\[
\begin{array}{c|c|c}
d&(m_{\mathrm{low}},m_{\mathrm{high}},b)&
\text{Cartier multiple forced by the mate}\\\hline
0&k(5,1,4)&4k\Gamma_{\mathrm{low}},\\
1&k(11,1,8)&10k\Gamma_{\mathrm{low}}.
\end{array}
\]

One cannot cancel \(k\): local class groups may have torsion.  In an
independently established ordinary \(A_{\mu-1}\) model
\(xy=t^\mu\), a low branch of contact \(\alpha\) represents
\(\alpha\in\mathbb Z/\mu\), has local Mumford intersection
\(\alpha^2/\mu\), and contributes correction
\(\alpha(\mu-\alpha)/\mu\).  Thus a two-simple \(d=1,[4]\) allocation with
ordinary \(A_3\) germs forces only \(k\) even; it is not unconditionally
excluded.  This corrects the invalid stronger inference from
\(10k[\Gamma]=0\) to \(10[\Gamma]=0\).

There is one further exact exclusion for \(C_0\).  At a totally ramified
ruling, normalize \(d=1,[4]\) so the low factor restricts to \(z^2\).
In the balanced frame its global form is

\[
 (p_0-2z)\xi+\frac{p_0z}{2}\eta.
\]

Write the high factor as

\[
 u(z)\xi+\left(z^{10}+\frac z2u(z)\right)\eta.
\]

The eleven exact first-normal image equations force \(u_9=-2\) and
\(u_0=u_3=u_6=0\).  In particular both high coefficients are divisible by
\(z\), creating forbidden vertical content.  Coordinate reversal gives the
same conclusion at the other totally ramified ruling.  The general
\(d=0,[4]\), non-totally-ramified \(d=1,[4]\), and \(d=1,[2,2]\) loci remain
open.  The last locus genuinely contains a missed projective boundary at
first-normal order.  In the balanced frame with quadric direction
\(q_1=\xi+z\eta/2\), the content-free factors

\[
 \ell=\xi+\frac32z\eta,
 \qquad
 m=(1-3z^4+z^8)\xi+
   \left(\frac z2-\frac{z^5}{2}+\frac{z^9}{2}\right)\eta
\]

have evaluations \(z\) and \(z^5\) on \(q_1\).  Their product therefore has
the required boundary evaluation \(z^6\), homogeneously \(s^6t^6\), and its
quadratic coefficients

\[
 \alpha=z^8-3z^4+1,\qquad
 \beta=2z^9-5z^5+2z,\qquad
 \gamma=\frac34(z^{10}-z^6+z^2)
\]

satisfy all eleven P-022 image equations.  This is an exact, content-free
first-normal survivor, not an ambient integral sextic or an STCI pair.  It
shows why the \([2,2]\) boundary must remain in the search.  Unsaved
higher-jet samples are not promoted beyond computational evidence.

### P-042: the necessary multiplicity-six types for a mixed \((4,6)\) pair

Let \(k\) be algebraically closed of characteristic zero and suppose
\(X=V(F_4,G_6)\) is supported set-theoretically on \(C_0\).  The forms have no
common surface factor, so \(X\) is a degree-24 lci curve of generic length six
over \(C_0\).  By P-011 the quartic has normal order one at the generic point.
In the completed transverse regular local ring it can therefore be taken as
one parameter; modulo it the other equation is a unit times the sixth power of
the remaining parameter.  Thus \(X\) is quasiprimitive.

Write the Bănică--Forster pieces as \(E_i=L^i(D_i)\), with \(D_1=0\).  For a
quasiprimitive multiplicity-six lci, the Gorenstein multiplication pairings

\[
 E_i\otimes E_{5-i}\longrightarrow E_5
\]

are isomorphisms.  The natural multiplication maps encode the inequalities
\(D_i+D_j\le D_{i+j}\).  The pairings give
\(D_4=D_5=D_2+D_3\), while \(2D_2\le D_4\) gives
\(0\le D_2\le D_3\).  The pieces therefore have the necessary form

\[
 O_C,\quad L,\quad L^2(D_2),\quad L^3(D_3),\quad
 L^4(D_2+D_3),\quad L^5(D_2+D_3).
\]

Put \(l=\deg L\) and \(d_i=\deg D_i\).  Since \(C_0\simeq\mathbf P^1\),
additivity of Euler characteristic gives

\[
 \chi(O_X)=6+15l+3(d_2+d_3).
\]

A \((4,6)\) complete intersection has

\[
 p_a(X)=1+\frac{24(4+6-4)}2=73,
 \qquad \chi(O_X)=-72,
\]

and hence

\[
 \boxed{5l+d_2+d_3=-26.}
\]

The first piece is a line-bundle quotient
\(O_{\mathbf P^1}(-7)^2\twoheadrightarrow L\), so \(l\ge-7\); effectivity
and the displayed equation give \(l\le-6\).  The eight raw numerical types are

\[
\begin{array}{c|c}
l&(d_2,d_3)\\\hline
-7&(0,9),(1,8),(2,7),(3,6),(4,5),\\
-6&(0,4),(1,3),(2,2).
\end{array}
\]

When \((l,d_2)=(-7,0)\), the canonical multiplicity-three member of the
filtration has pieces \(O,L,L^2\) and is a global primitive triple of type
\(O(-7)\), contrary to P-010.  Exactly seven necessary numerical types remain.
No existence or compatibility among these numerical candidates is asserted.

Finally, the quotient \(O(-7)^2\twoheadrightarrow O(l)\) is represented by a
basepoint-free pair of sections of degree

\[
 e=l+7\in\{0,1\}.
\]

This is precisely the horizontal degree in P-031.  In the nonregular branch,
P-031 gives \(1\le p\le8-e\), \(c=9-e-p\), and \(\deg Z=p+8\).  Therefore
only \(8+7=15\) of the former 36 coarse pole-divisor strata remain.  The seven
Bănică--Forster numerical types and the fifteen pole strata record different
necessary data; no unproved correspondence between them is being assumed.

### P-043: an all-stage obstruction for the P-039 multiplier family

Retain

\[
 S=k[x,y,z,w],\quad q=xw-yz,\quad A=x^2z-y^3,\quad B=xz^2-y^2w,
\]

and put

\[
 F=xA+\lambda y^2q,\qquad G=yA+\lambda xzq.
\]

The pair is genuinely compatible with the target classes.  An exact identity
is

\[
\begin{aligned}
 xzG-ywF={}&q\bigl(\lambda x^2z^2-\lambda wy^3-x^2yz+xy^3\bigr)\\
 &+B(x^2y-xy^2),
\end{aligned}
\]

so \(Gu=Fv\) in \(H^2_{(q,B)}(S)\).  Thus the associated Koszul class is a
cycle; the question is whether it is a boundary.

At stage \(R_N=S/(q^N,B^N)\), the classes
\(u=xz/(qB)\) and \(v=yw/(qB)\) are represented by

\[
 u_N=xz(qB)^{N-1},\qquad v_N=yw(qB)^{N-1}.
\]

A common ancestor can be replaced by its homogeneous component of degree
\(-7\).  The diagonal stages \((q^N,B^N)\) are cofinal in the usual two-index
Čech direct system, so after promotion to a common diagonal stage \(N\) it
would be
represented by \(h\in S_{5N-7}\) and would give

\[
\begin{aligned}
 Fh-u_N&=q^Na+B^Nb,\\
 Gh-v_N&=q^Nc+B^Nd,
\end{aligned}
\]

with \(a,c\in S_{3N-3}\) and \(b,d\in S_{2N-3}\).  Stage \(N=1\) is
impossible because it would require a numerator of degree \(-2\), so take
\(N\ge2\).  For a polynomial \(P\), let \([i,j,k,l]P\) denote the coefficient
of \(x^iy^jz^kw^l\), and define

\[
\begin{aligned}
 \Phi_N(P)={}&-(N-1)\lambda[2N,0,2N-2,N-1]P\\
 &-\lambda[2N-1,1,2N-1,N-2]P\\
 &-[2N-1,0,2N-1,N-1]P,
\end{aligned}
\]

\[
 \Psi_N(P)=N[2N-1,0,2N-2,N]P
  +[2N-2,1,2N-1,N-1]P.
\]

Direct support checks give

\[
 \Phi_N(q^Na)=\Phi_N(B^Nb)=0,
 \qquad
 \Psi_N(q^Nc)=\Psi_N(B^Nd)=0.
\]

Expanding

\[
\begin{aligned}
 F&=x^3z-xy^3+\lambda xy^2w-\lambda y^3z,\\
 G&=x^2yz-y^4+\lambda x^2zw-\lambda xyz^2
\end{aligned}
\]

shows, for every \(h\in S_{5N-7}\), that

\[
 \boxed{\Phi_N(Fh)+\Psi_N(Gh)=0.}
\]

Only three coefficient positions of \(h\) can contribute; their total
coefficients are respectively
\(-\lambda(N-1)+\lambda N-\lambda=0\), \(-1+1=0\), and
\(-\lambda+\lambda=0\).  On the target pair, however,

\[
 \boxed{\Phi_N(u_N)+\Psi_N(v_N)=-1,}
\]

because the \(y\)-free leading term of \(u_N\) has coefficient one at
\((2N-1,0,2N-1,N-1)\), while the other requested target coefficients vanish.
Applying the two functionals to the proposed ancestor equations gives the
contradiction \(0=-1\).

The certificate is compatible with the direct-system transition
\([P]\mapsto[qBP]\): the four-term expansion of \(qB\) gives

\[
 \Phi_{N+1}(qBP)=\Phi_N(P),\qquad
 \Psi_{N+1}(qBP)=\Psi_N(P).
\]

In any event, an equality in the direct limit must become an equality at some
common finite stage, where the displayed contradiction applies; no injectivity
of a transition map is assumed.  The identities lie in \(\mathbf Z[\lambda]\)
and use no division, so the certificate is valid over every field and for
every \(\lambda\).  For P-039's coprime, nonconstant-ratio family one retains
\(\lambda\ne0\).

Thus the entire explicit P-039 family is eliminated as a source of common
ancestors.  Other degree-four rank-one pairs and all higher-degree pairs remain
untreated.  This is not a non-quasi-cyclicity theorem.

## Failed or exhausted approaches

The following negative conclusions are themselves part of the mathematical
map.

- **Ordinary local cohomological dimension is exhausted as a first
  obstruction.** Hartshorne's second vanishing theorem already gives
  \(\operatorname{cd}_S(I_C)=2\) for every homogeneous prime defining an
  integral projective curve. It cannot distinguish arithmetic rank two from
  three. The sharper Hartshorne--Polini criterion uses codepth of
  \(H^2_{I_C}(S)\), but no integral-curve example in \(\mathbf P^3\) violating
  it is known.
- **Constant-coefficient topology is too coarse.** Purity and the Gysin
  sequence compute the complement cohomology, but the first potentially
  nonzero group occurs in the highest degree still compatible with a cover by
  two principal affine opens. Neither ordinary singular cohomology nor the
  checked constant-coefficient étale groups crosses the required bound.
- **Picard, Chow, and ordinary \(K_0\) are too coarse by themselves.**
  P-029 gives \(\operatorname{Pic}(U)\simeq\mathbf Z\), while P-034 gives
  \(K_0(U)=\mathbf Z[u]/(u^3,\deg(C)u^2)\). The Koszul class relation is only
  the Bezout divisibility \(\deg(C)\mid ab\). Any bundle obstruction must
  detect unstable generation or cancellation, not only stable classes.
- **Smooth or ordinary carrier surfaces are too restrictive.** P-005 and the
  almost-Cartier divisor-class results strongly constrain such carriers, but a
  hypothetical pair may be singular along all of \(C\) or have nonordinary
  finite singularities. P-011 shows that this escape route starts only in
  degree six for a rational quartic; it does not eliminate it.
- **The binomial obstruction is route-specific.** Characteristic-zero
  results excluding two binomial equations for a monomial curve do not exclude
  two arbitrary forms. The distinction is exactly the unresolved one for
  \(C_0\).
- **Naive homogenization and saturation are not a solution.** P-007 shows
  that saturation by the hyperplane variable merely discards boundary
  components after they have appeared. It does not supply two projective
  equations.
- **The reduced curve's Rao module is not an obstruction.** Smooth STCI
  curves with nonzero Rao module are known. What must be controlled is the
  ACM, subcanonical multiple structure supported on the curve.
- **The first blowup alone is not decisive.** P-006 forces a horizontal
  common curve or multisection in the low-genus range, but positive-characteristic
  presentations demonstrate that such a common factor can persist through
  further infinitesimal neighborhoods and still terminate in an STCI pair.
- **Normality does not restore ordinary branch intersection.**  The local
  normal surface \(xy=e^n\) has Mumford intersection \(1/n\) between the two
  components of \(e=0\).  The former shortcut \(\Gamma_1\Gamma_2=10\) is valid
  under smooth/Cartier collision hypotheses, not from normality alone.
- **A split normal cone need not come from a reducible carrier.**  P-022 gives
  integral sextics with square discriminant and split exceptional divisor,
  and the actual 22-dimensional first-normal image permits every split type
  \(d=0,\ldots,5\).  Neither square discriminant nor membership in the ambient
  image is an exclusion by itself.
- **First-normal incidence for \((4,6)\) is nonempty in every preliminary
  regular-ratio class.**  Exact examples exist for \(e=0,1,2,3\), but P-042
  proves that \(e=2,3\) cannot extend to a multiplicity-six lci.  For the viable
  classes \(e=0,1\), only computing the common section repeats an exhausted
  representation; cubic through sextic transverse jets are the next data.
- **A proportional first-normal pair need not have a regular quotient.**
  The complete-intersection models \(F=tu+v^m,\ G=u\) have radical
  \((u,v)\), constant transverse length \(m\), and ratio \(1/t\).  Therefore
  residual-intersection degree counts do not by themselves justify global
  subtraction.  The former universal forms of P-021 and P-026 are false.
- **Frozen transition coordinates give false formal-neighborhood equations.**
  In the type-B \((4,5)\) calculation the quotient coordinate is the moving
  \(W=(z^3+a)/(z^4+b)\), not \(1/z\).  Calculations based on the frozen frame,
  including `/private/tmp/typeb_generic.py`, are invalid.
- **The endpoint primary ideal is not monomial.**  Replacing the exact
  finite-stage ideal by \((q^2,a^2)\) loses mixed terms and invalidates the
  intended local-cohomology shortcut; P-024 records the corrected ideal.
- **The archived multi-agent wave did not produce 24 independent mathematical
  representations.** Direct auditing found roughly ten substantive lines,
  with many cosmetic variants. Its formulas were retained only after
  independent proof or computation; its orchestration claims have no
  evidentiary role here.

## Open decisions and questions

- **Central characteristic-zero test.** Is
  \(C_0=[s^4:s^3t:st^3:t^4]\) the radical of two arbitrary homogeneous forms?
  P-010 eliminates primitive triples for every characteristic-zero smooth
  rational quartic, while P-025 and P-040 eliminate every degree-\((4,5)\)
  presentation of \(C_0\).  The unrestricted question remains open in higher
  degree, beginning with the mixed \((4,6)\) and thick-sextic frontiers.
- **Mixed \((4,6)\) two-track analysis.** P-042 restricts every hypothetical
  multiplicity-six lci to \(e=0\) or \(1\).  For those two regular-ratio
  values, impose the cubic, quartic, and quintic transverse-jet identities and
  require a nonzero sextic coefficient.  Separately attack the 15 nonregular
  order-\((1,1)\) pole strata with \(e=0\) or \(1\).  The exact first-normal
  incidences at \(e=2,3\) cannot extend to a multiplicity-six lci.
- **Surviving split-sextic roots.** Analyze partition \([4]\) for \(d=0\) and
  partitions \([4]\), \([2,2]\) for \(d=1\). P-030 closes every other residual
  binary-quartic root partition under the split/no-vertical hypotheses.
- **Higher-degree local-cohomology multipliers.** P-037 excludes every degree
  at most three.  Start at degree four on the proportional first-conormal
  locus.  P-039 shows that first-symbol rank alone does not finish the
  argument, while P-043 excludes its explicit coprime nonconstant-ratio family
  at every direct-limit stage.  Classify the remaining degree-four rank-one
  pairs before moving to higher degrees.  No non-quasi-cyclicity theorem has
  yet been obtained.
- **Jaffe-sequence control remains structurally important but less bounded.**
  Jaffe already performs the iteration; the missing theorem is monotonicity,
  or a substitute, in the presence of common singularities.  Positive
  characteristic shows that any nontermination principle must detect
  Frobenius.
- **Beyond rational quartics.** Can the internal-cuspidal-projection/Frobenius
  descent of P-012 be extended to other smooth curves admitting a birational
  projection with only unibranch singularities? The obstruction is no longer
  simply one weighted equation when the normalized plane image has several
  singularities or positive genus.
- **Singular integral curves.** Even a complete solution of the smooth case
  would leave the general repository problem. The conormal-bundle and regular
  blowup tools used here fail at singular points; conductor and normalization
  data should replace them.
- **Field descent.** The main statement assumes an algebraically closed base.
  Over a nonclosed field, geometric STCI need not automatically yield two
  equations over the ground field; that arithmetic variant is separate.

## Research discipline

The status vocabulary is:

- **PROVED**: complete argument checked in this run.
- **KNOWN**: checked statement in the literature, with exact source and hypotheses.
- **COMPUTATIONAL EVIDENCE**: reproducible calculation, not a general proof.
- **CONJECTURAL**: supported conjecture with stated evidence.
- **SPECULATIVE**: potentially useful but weakly supported idea.
- **ARCHIVE CLAIM**: inherited lead that has not yet survived current verification.
