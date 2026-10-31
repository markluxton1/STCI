# Independent audit of transport, complement pencils, and bundle amplification

Date: 2026-10-31. Reviewer: `transport_pencil_strategy_review`.
Scope: §8 of [the unrestricted strategy assessment](2026-10-31-unrestricted-strategy-assessment.md), for
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), with \(k\) algebraically closed of characteristic zero.
Status: independent bounded review of provisional deductions and research allocation; no canonical promotion. **The unrestricted STCI question remains open.**

## Disposition

No material mathematical defect was found in the three deductions, within their stated scopes. The details below make explicit the generic-connectivity argument, projectivization convention, and characteristic-zero transfer. None supplies equations for C or an unrestricted nonexistence argument.

The recommendation to stop unmotivated model enumeration, cover classification, and everywhere nondegenerate fiberwise powering is supported. It is a local allocation decision about these mechanisms. It provides no evidence against existence and does not justify a general pause of constructive research. Requiring a specified mechanism and an informative outcome is reasonable; requiring evidence that it will succeed would be too strong. The assessment expressly adopts the former condition.

## 1. Ordinary Cremona transport

The primary definition in [Ciliberto–Cueto–Mella–Ranestad–Zwiernik, §2.2](https://people.math.osu.edu/cueto.5/CremonaLinearizations.pdf) requires both ambient rational maps to be defined at the respective general points. Their restrictions are inverse. Shrinking the two domains gives inverse ambient isomorphisms around those points: the compositions agree with the identity on a dense open set and hence on their common domains. Thus the two-dimensional regular local rings transverse to the curves are isomorphic, and so are quotients by the corresponding transformed equations. Their finite lengths agree.

In particular, transporting a reduced transverse complete intersection gives multiplicity one along C. Sole support would give \(ab=4\). Nonplanarity excludes a plane carrier; among the remaining possibilities, the only quadric through C is \(x_0x_3-x_1x_2\), so two distinct quadratic equations cannot give a proper intersection. The unique-quadric assertion can also be checked directly: pair sums of the parametrization exponents \(0,1,3,4\) cover all exponents 0 through 8, so the restriction from the ten quadrics to the nine binary octics has one-dimensional kernel.

Powers preserve each strict-transform support, and hence cannot remove an existing residual support. This argument says nothing against transporting a source whose transverse CI is already nonreduced; its multiplicity must also be preserved. It also says nothing about a transformation whose indeterminacy contains C. Such a centered transformation requires different local analysis.

[Mella–Polastri, Theorem 1/Corollary 1](https://arxiv.org/pdf/0906.4858) gives the reduced-embedding equivalence. The later paper supplies an effective construction and explicitly corrects the earlier proof in Remark 2.4. Neither result transports a global CI presentation.

The common-model warning matches [the existing blowup note, §§4–6](2026-10-28-blowup-residual-geometry.md): the actual strict intersection W must be supported on E, whereas the inverse image of its image surface also includes Q'. Rulings of Q' can map to genuine trisecants in the original space. This audit checks that logical distinction; it does not rerun the inherited construction or certificates of the V5 model.

Geometrically, an ambient isomorphism transports the entire transverse scheme, rather than manufacturing the extra thickness needed when a line becomes a quartic. The missing constructive datum is a suitable thickened source together with the actual exceptional corrections and absence of residual support.

## 2. The exact complement equivalence and its topological scope

Put \(U=\mathbf P^3\setminus C\). A supported pair F,G of degrees a,b gives the everywhere defined map
\([F^{b/g}:G^{a/g}]\), \(g=\gcd(a,b)\).
Conversely, a morphism \(U\to\mathbf P^1\) is given by two generating sections of its pulled-back \(\mathcal O(1)\). Regularity and removal of codimension two identify \(\operatorname{Pic}(U)\) with \(\operatorname{Pic}(\mathbf P^3)\), and extend both sections to A,B of \(\mathcal O(n)\). Negative n has no sections; n=0 gives a constant map. For n>0 the common zero set has no divisor component, is nonempty by projective intersection, and lies in C. Its dimension is at least one; irreducibility of C makes its support exactly C.

Each standard affine chart has inverse image \(D_+(A)\) or \(D_+(B)\); these are affine because A,B are positive-degree homogeneous forms and C lies in both zero sets. Consequently this morphism is affine and its surface fibers are affine. This is automatic once the embedded morphism exists, not a further numerical restriction.

For the topological conclusion, first choose irreducible factors F,G that still form a supported pair. This is legitimate: an irreducible factor and the other equation have a nonempty one-dimensional projective intersection contained in C; then choose a factor of the other equation. Write u=b/g, v=a/g, so \(\gcd(u,v)=1\).

Resolve the rational pencil and take its proper Stein factorization. If the finite degree is d>1, the intermediate smooth curve is rational because it is dominated rationally by \(\mathbf P^3\). Thus the rational function \(F^u/G^v\) is a composition R(h) with \(\deg R=d\). Write h as a quotient of coprime homogeneous forms of the same positive degree. Every fiber value of h has a nonempty hypersurface support. Since the zero divisor of R(h) has just the irreducible support F=0, R has a unique zero, totally ramified of order d. The same holds for its pole. Divisorial orders then give \(d\mid u\) and \(d\mid v\), a contradiction. Hence the resolved pencil, and its nonempty open generic fiber in U, are geometrically connected in characteristic zero.

Over \(\mathbf C\), general position makes U simply connected: a real two-dimensional disk filling a loop can avoid the real two-dimensional smooth curve in the real six-dimensional ambient manifold. [Artal Bartolo–Cogolludo, Definition 1.4 and Proposition 1.5](https://arxiv.org/pdf/1002.2097) applies to this smooth quasiprojective source and the connected generic fiber. Its orbifold multiplicity at a point is the gcd of multiplicities of the components of the actual fiber divisor on U. The resulting orbifold sphere must have trivial fundamental group. The standard presentation allows zero or one multiple fiber, or two with coprime multiplicities, and excludes three or more. The two displayed irreducible fibers have multiplicities u,v, consistent with this condition.

The topological proof is stated over C. For fixed algebraic data over another algebraically closed characteristic-zero field, descend to a finitely generated field, embed it in C, and compare geometric fiber multiplicities and connectivity after algebraically closed base extension. No topological assertion about the other field is needed.

The logarithmic differential has its carrier poles inside U. Its pole divisor is not supported only over C on a resolution. The equalized pencil ideal is \((F^u,G^v)\); one must not silently replace its blowup by that of \((F,G)\). The existing [exceptional-cover control](2026-10-30-four-streams-pencil.md) remains relevant and does not provide a quartic-specific obstruction.

The subsequent distinction from the [two-hyperplane projection, §4](2026-10-30-fixed-surface-configuration.md#4-the-plane-pencil-converts-every-admissible-pair-into-one-finite-cover) also checks out. If Z is the full proper supported CI, its support avoids \(M=V(x_0,x_3)\), and projection \([x_0:x_3]\) is finite flat of degree ab: fibers are proper hyperplane sections of the Cohen–Macaulay curve Z. The reduction is \([s:t]\mapsto[s^4:t^4]\), of degree four, separable in characteristic zero and odd characteristic and purely inseparable in characteristic two. Thus ab is the rank of the full, generally nonreduced fiber algebra, not the degree of a reduced cover. The two marked fibers on C have scheme length four; no separable Riemann–Hurwitz argument applies in characteristic two.

Geometrically, the equivalence describes a pencil whose whole base locus has been absorbed into C. It is a useful dictionary, but constructing this exact complement fibration is already the global existence problem. Multiple-fiber restrictions obtained from its fundamental group add no contradiction to the coprime equalization.

## 3. Homogeneous bundle amplification

Let E have rank two, and let P,Q be globally defined homogeneous polynomial maps to L1,L2 of fiber degrees r,s>0, with no common nonzero zero in any fiber. Use projectivization by **lines**: a line \(kv\subset E_x\) is sent to
\([P(v)^s:Q(v)^r]\) in the lines of \((L1^s\oplus L2^r)_x\).
Both entries scale by \(\lambda^{rs}\), making this well-defined and regular. Fiberwise they are degree-rs binary forms without common roots, so the induced map has degree rs. With the quotient convention the same map is written using E's dual and the target's dual; splitting of E is equivalent to splitting of its dual. There is no convention-dependent change to the conclusion.

[Amerik–Kuznetsova, Theorem 2](https://arxiv.org/pdf/1609.00910) concerns a morphism between **two** projective bundles over the same base; it does not require a self-map. Its base conditions hold on complex projective three-space. Therefore rs>1 forces E to split. If r=s=1, the map E to L1 direct-sum L2 is fiberwise an isomorphism directly.

The characteristic-zero transfer can be made without assuming that an arbitrary field embeds in C. Descend E and the maps to a finitely generated subfield k0 and embed k0 in C. If the resulting E over C is \(\mathcal O(a)\oplus\mathcal O(b)\), its first Chern class determines the same determinant over k0. Hom spaces commute with field extension. The determinant of a proposed homomorphism from this split bundle to E is therefore a scalar polynomial on a finite-dimensional k0-vector space. It is nonzero at the complex isomorphism, hence not identically zero. An infinite field k0 supplies a point where it is nonzero, giving an isomorphism already over k0 and after base change to k. This also verifies the transfer claimed through a splitting criterion in the assessment.

The characteristic-p comparison is correct: for rank-two E on B, relative Frobenius gives a B-morphism \(\mathbf P(E)\to\mathbf P(E)^{(p)}\simeq\mathbf P(F_B^*E)\), with purely inseparable fiber degree p, even if E is nonsplit; see [Stacks, §33.36](https://stacks.math.columbia.edu/tag/0CC6) for relative Frobenius and its degree on geometric fibers. This shows why the characteristic-zero splitting conclusion cannot simply be imported to characteristic p. It does not assert that the target splits or construct two line-bundle-valued equations from a section.

Geometrically, the two polynomial operations would eliminate every unwanted projective direction of E, not merely directions encountered by the particular section. The literature theorem rules out that uniform operation for a nonsplit bundle. It leaves operations with base directions or degeneration away from the section outside its scope. It also does not prove that an arbitrary STCI would arise by this operation from an arbitrary Ferrand bundle.

## 4. Research allocation and remaining inputs

These findings support three narrowly stated conclusions: reduced Cremona equivalence alone does not manufacture thickness; the complement-pencil condition alone reformulates existence; uniform nondegenerate homogeneous amplification of a nonsplit bundle is impossible. Their value is to prevent those specific unjustified shortcuts. They are not three new obstructions to arbitrary defining pairs.

No precise new constructive test follows from the cited theorems without additional input. A transport experiment needs an actual thickened source and a specified map permitting exceptional corrections to be calculated. A complement experiment needs an independently supplied embedded fibration or a specific sheaf comparison. A degenerate bundle operation needs a specified E, section, and map, with a way to test its base directions against the section. Naming these objects is not asking for a proof that they succeed.

The pre-existing proposal to move graph residuals into E in [the blowup note, §6](2026-10-28-blowup-residual-geometry.md) is not disproved here. That note does not yet supply a chosen family for this audit to test. The absence of such input supports stopping this selection assignment, not closing the constructive route. Replacing it with adjacent models or examples without a mathematical rationale would add an unjustified research expansion without resolving the missing datum. The user's broad authorization of continued research is not in question; the next recommendation should be reported before beginning another technical investigation.

Review coverage: independently reconstructed the three deductions and their geometric implications; inspected the cited primary definitions/theorem statements, the relevant projective-bundle proof, the existing graph-support criterion and pencil control; reused rather than reran their inherited certificates and canonical low-degree scope. No new equations, computations, curve classifications, canonical results, or unrestricted conclusions are claimed.
