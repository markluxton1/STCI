# Normalization, conductor descent, and projection of singular carriers

This dossier consolidates the **fixed-carrier** and **Cartier singleton-lift** questions for the rational quartic
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
It is an explanatory investigation, **not a new theorem authority**. Exact scopes and proofs remain in the linked canonical records. This first batch directly compares R-0002, R-0003, R-0004, R-0017, R-0034–R-0036 and Q-0001; additional historical sources remain to be integrated.

## 1. Two logically different problems

Fix an integral hypersurface \(X\subset\mathbf P^3\) containing \(C\), its finite normalization \(\nu:S\to X\), and \(H=\nu^*\mathcal O_X(1)\).

**Fixed carrier:** Does there exist a homogeneous form \(G\) whose restriction to \(X\) has zero support precisely \(C\)? This is a problem of descending an upstairs section through the *actual conductor*, not merely finding a divisor class on \(S\).

**Varying carrier:** Which normalizations \((S,H)\), inverse curves, and four-dimensional linear systems can actually produce such an \(X\)? Classification of numerical models is only necessary; it does not construct a projection, establish full inverse support, or solve conductor descent.

The distinction is decisive: a formally possible \(bH\sim\sum n_i\Gamma_i\) need not arise from a section of \(\mathcal O_X(b)\).

## 2. Full inverse support and the fixed-carrier criterion (R-0003)

Let \(X\) be integral Cohen–Macaulay projective, \(L\) ample, \(S\) its finite normalization, \(H=\nu^*L\), and \(W=(\nu^{-1}C)_{\mathrm{red}}\). An isolated inverse-image point outside the curve components of \(W\) already prevents a section with zero support exactly \(C\): its pullback would have a zero at an isolated point, whereas a nonzero Cartier section on the normal surface has pure codimension-one zero support.

Assume instead \(W=\Gamma_1\cup\cdots\cup\Gamma_s\), with no such isolated points. The candidate divisor classes form
\[
\Lambda=\ker\bigl[\mathbf Z^{s+1}\longrightarrow\mathrm{Cl}(S)\bigr],
\quad
(n_1,\ldots,n_s,b)\mapsto\sum n_i[\Gamma_i]-b[H].
\]
A lattice point determines a rational upstairs section with prescribed divisor. At each generic conductor curve away from \(C\), descent is controlled by the **full unit quotient** \(B_\eta^*/A_\eta^*\), not merely its reduced residue-field quotient. Write \(\Lambda_{\mathrm{desc}}\) for the kernel of the conductor-unit map after quotienting its target by torsion.

**Established fixed-carrier criterion (R-0003).** A positive power of \(L\) has a section with zero support exactly \(C\) if and only if \(\Lambda_{\mathrm{desc}}\) contains a vector with every \(n_i>0\). For a hypersurface of \(\mathbf P^3\), such sections lift to homogeneous forms.

**Why sufficiency is nontrivial.** The lattice relation constructs the upstairs divisor; torsion of off-\(C\) conductor classes allows a common power to descend there. Positivity along every inverse branch allows a further power to enter the actual conductor along \(C\). The normality/depth hypotheses are then used to pass from generic conductor control to global descent. Omitting either the nilpotent conductor units or the full inverse support breaks this argument.

In the singleton, generically regular case set \(a=H^2\), \(c=H\cdot\Gamma\), \(g=\gcd(a,c)\). If \(t\) is the order of \((a/g)[\Gamma]-(c/g)[H]\) and \(E\) the full conductor-unit order of the primitive upstairs section, a mate exists exactly when both orders are finite; its degrees are positive multiples of \(tEc/g\). This formula is **not** available without the singleton and generic-regularity hypotheses.

[Canonical R-0003](../results/fixed_carrier_conductor_criterion.md) · [source proof](../notes/2026-10-13-generalization-conductor-theorem.md)

## 3. Cartier singleton classification: necessity, not existence (R-0002)

Suppose characteristic zero, \(C\subset\mathbf P^3\) is smooth rational of degree \(d\), an **actual** STCI mate exists on integral \(X\) of degree \(a\), and the full reduced inverse support is a single smooth curve \(c\) mapping isomorphically to \(C\). Require \(c\) Cartier on \(S\). The mate yields \(mc\sim bH\), so \(c\) is ample and
\[
c^2=d^2/a.
\]
Regularity along the Cartier smooth curve, adjunction, surface classification, and the Cartier restriction sequence give \(h^0(S,\mathcal O_S(c))=c^2+2\) and a basepoint-free system. Thus \(|c|\) identifies \(S\) with a normal minimal-degree surface. The possibilities are:

| Normalization and inverse curve | Polarization \(H\) | Degree \(a\) |
|---|---|---|
| \(\mathbf P^2\), line | \(\mathcal O(d)\) | \(d^2\) |
| \(\mathbf P^2\), conic (\(d\) even) | \(\mathcal O(d/2)\) | \(d^2/4\) |
| Smooth scroll of degree \(n\ge2\), hyperplane section, \(n\mid d\) | \((d/n)c\) | \(d^2/n\) |
| Rational-normal cone of degree \(n\ge2\), smooth Cartier hyperplane section, \(n\mid d\) | \((d/n)c\) | \(d^2/n\) |

For \(d=4\), the integral-quartic exclusion R-0001 removes the degree-four cases. Three **necessary** higher-degree possibilities survive: a degree-eight smooth quadric \((c,H)=((1,1),(2,2))\); a degree-eight quadric cone with \(H=2c\); and a degree-sixteen plane with \(c\) a line, \(H=\mathcal O(4)\). None is thereby shown realizable.

Non-Cartier inverse curves, multiple inverse branches, and higher-degree maps \(c\to C\) are not classified by this theorem.

[Canonical R-0002](../results/cartier_singleton_lift.md) · [open Q-0001](../questions/cartier_projection_models.md)

## 4. Projection admissibility and full conductor phase (R-0004)

A four-section subsystem of \(H^0(S,H)\) must first be basepoint-free and induce a **finite birational** map to an integral hypersurface. Next the full reduced inverse support of \(C\) must be precisely \(c\), with no isolated extra points. Only then is the fixed-carrier conductor question applicable.

In characteristic zero, for a fixed normal \(S\), smooth ample Cartier \(c\), a section \(Q\in H^0(S,H)\) with \(\mathrm{div}(Q)=mc\), and a finite-type family of four-section projections restricting to the fixed embedded curve, R-0004 gives a finite stratification and finite surjective cover \(Z\to T_0\) with a phase morphism
\[
z:Z\to(\mathbf G_m)^D.
\]
An admissible carrier has a mate precisely when its **full-conductor** phase tuple is torsion. Finite Artinian calculations keep nilpotent conductor equations; flattening and monic normalization equations prevent loss of generic conductor components on specialization. The torsion image has a finite torsion-coset envelope, but the mate locus need not be constructible.

For the three quartic singleton families, the on-curve conductor thresholds are respectively \(M=5,5,13\). If the phase order is \(E\), every positive multiple of \(E\) at least \(M\) is a mate degree; any additional mate degrees must be smaller multiples. The actual admissible phase images and torsion cosets **have not been computed**. A finite-type reduction is not a completed elimination.

[Canonical R-0004](../results/projection_phase_reduction.md)

## 5. Explicit negative example: degree-sixteen plane projection (R-0017)

Consider the four quartics on \(\mathbf P^2\) with coordinates \([s:t:z]\):
\[
[s^4:s^3t:st^3+\alpha z^4:t^4+zP_3(s,t,z)],\qquad \alpha\ne0.
\]
For the stated birational open condition (the \(A_3\) or \(C_1\) coefficient of \(P_3\) nonzero), the map is basepoint-free, finite birational onto an integral degree-sixteen surface, and has full reduced inverse support of \(C_0\) exactly \(z=0\).

**Nevertheless, no positive-degree homogeneous mate exists for this family.** The all-degree derivative contradiction detects a first-order nilpotent conductor obstruction invisible in the reduced inverse support. A broader two-fixed-coordinate full-singleton sublane has the same exclusion.

This refutes the implication “singleton reduced inverse support + a suitable upstairs divisor implies a mate.” It does **not** eliminate all degree-sixteen plane projections, much less all Cartier singleton models. The exact derivative calculation and its assumptions remain in the source proof and independent reconstruction.

[Canonical R-0017](../results/singleton_plane_conductor_descent.md) · [underlying calculation](../notes/2026-10-19-singleton-projection-investigation.md)

## 6. Normal carrier indices and socle compatibility (R-0034–R-0036)

These are **different** restrictions from the preceding nonnormal-conductor problem.

**Local Cartier index (R-0034).** For a normal integral carrier, an actual mate with divisor \(nC\), actual local Cartier index \(r\mid n\), \(k=n/r\), and a curvilinear generic transverse complete intersection, the pointwise top ordinary-power socle defects satisfy
\[
D_{n,P}=(k-1)A_{F,P}+kD_{r,P},
\qquad
2\sum_i\operatorname{length}(T_i)_P=nD_{n,P}.
\]
The *actual local Cartier index* cannot be replaced by surface multiplicity. The equations impose compatibility, not an unconditional exclusion.

**Bounded-index exclusion (R-0035).** In characteristic zero, for the fixed \(C_0\), a normal integral hypersurface carrier satisfying the inherited normal-carrier torsion reduction and quadratic-direction obstruction and with every actual on-curve Cartier index at most four cannot admit a mate in any degree. Indices six, twelve and higher, and nonnormal or entirely-thick presentations, are not excluded by this result.

**Pointwise conductor–socle identity (R-0036).** In characteristic zero, for an actual supported complete intersection, integral carrier generically regular along \(C\), full singleton smooth Cartier inverse curve \(c\cong C\), normalization smooth along \(c\), and invertible conductor \(\mathcal O(-B)\) without a \(c\)-component, the transverse differential zero divisor \(A\) and the top socle defect satisfy
\[
D_n=(n-1)A-B|_c.
\]
This is an equality of actual divisors, not just degrees. It is not established for multiple branches, non-Cartier lifts, singular normalization along \(c\), or a generically singular carrier; its Jacobian proof does not automatically extend to characteristic dividing \(n\).

[Local index R-0034](../results/normal_carrier_index_socle.md) · [bounded index R-0035](../results/normal_carrier_bounded_index_exclusion.md) · [pointwise identity R-0036](../results/pointwise_conductor_socle_defect.md)

## 7. What the methods do and do not prove

- **Numerical equivalence upstairs** gives candidate divisors, not descent.
- **Reduced conductor residues** can miss nilpotent first-order obstructions; R-0017 provides an actual failure.
- **Finite-type phase reduction** does not calculate admissible phase images or torsion cosets.
- **A normal bounded-index exclusion** cannot be extended to all nonnormal carriers or arbitrary indices.
- **A smooth singleton Cartier lift** is a strong hypothesis, not an automatic consequence of STCI.
- **Generic formal or function-field equations** are not necessarily global homogeneous equations. The separate finite normal-jet/global-coefficient investigation supplies the appropriate realization tests and counterexamples; its full content belongs in another dossier.

## 8. Concrete frontier

1. For each of the degree-eight smooth quadric, degree-eight cone, and degree-sixteen plane models, parameterize admissible four-section projections; test basepoints, finiteness, birationality, and **full** inverse support before computing phases.
2. Compute actual conductor algebras (including nilpotent structure) and phase maps on each admissible stratum. Determine whether their images contain torsion points, not just whether the ambient torus does.
3. Extend the fixed-carrier analysis to non-Cartier inverse curves, multiple branches, and nonisomorphic inverse maps without assuming the singleton lattice formula.
4. Investigate actual local Cartier indices above four and determine whether the socle identities yield additional exclusions.
5. Seek explicit cuspidal and ruled-cubic conductor calculations and identify precisely which descent step fails. These historical examples are **not yet source-reconciled in this batch**.
6. Compare any surviving conductor model against actual global homogeneous section constraints and the separate finite-jet criteria.

## 9. Source-preservation boundary of this batch

**Directly examined:** R-0002, R-0003, R-0004, R-0017, R-0034, R-0035, R-0036, Q-0001, and the current MAP/FRONTIER navigation. Their principal mathematical statements, assumptions, proof mechanisms and counterexample setup are incorporated above; their full source proofs remain linked and should not be deleted.

**Still to compare directly:** the historical Ultra source proofs and audits linked from these records, detailed local conductor calculations (including cuspidal/ruled-cubic examples), relevant scratch scripts, projection and singular-carrier historical investigations, and other mathematical source material not enumerated by Phase 1. No completeness or redundancy certificate is asserted for these sources.

**Deletion policy:** no original mathematical source is removed in this batch. Ordinary correction chronology should not be imported into the final exposition; substantive failed mathematical mechanisms should.

## 10. Source-level expansions: explicit computations and finite reductions

### 10.1 An explicit plane normalization and its polynomial obstruction

The original R-0017 source gives the concrete map
\[
f([s:t:z])=[s^4:s^3t:st^3+z^4:t^4+s^3z].
\]
On \(s\ne0\), writing \(x=t/s\), \(n=z/s\), the image coordinates are \((x,x^3+n^4,x^4+n)\), so \(x\) and \(n\) are recovered rationally. The map is basepoint-free; since \(f^*\mathcal O(1)=\mathcal O_{\mathbf P^2}(4)\) is ample, it is finite. Its image has degree sixteen and is defined by
\[
F=(X_0^3X_3-X_1^4)^4-X_0^{13}(X_0^2X_2-X_1^3)=0.
\]
The pullbacks of the two bracketed forms are \(s^{15}z\) and \(s^8z^4\). The inverse image of \(C_0\) has full reduced support \(z=0\), including the boundary \(s=0\).

Suppose a degree-\(b>0\) mate \(G\) existed. Pullback and positivity force \(G(f)=\lambda z^{4b}\), rescaled to \(z^{4b}\). Restriction to \(s=0\), where \([t:z]\mapsto[z^4:t^4]\) is surjective, gives \(G(0,0,Z,T)=Z^b\). Differentiating \(G(f)=z^{4b}\) in \(s\) and then setting \(s=0\) gives
\[
0=b\,t^3z^{4b-4},
\]
a contradiction in characteristic zero. This is a **global polynomial proof**, not just a generic-point phase argument.

For the eleven-parameter family with \(U_2=st^3+\alpha z^4\), \(U_3=t^4+zP_3\), writing \(P_3=A_3+zB_2+z^2C_1+\delta z^3\), the generic map degree is respectively \(1,2,4\) according as \(A_3\) or \(C_1\) is nonzero; both vanish but \(B_2\ne0\); or all three vanish. This follows from the \(\mu_4\)-action on \(k(x,n)/k(x,n^4)\). Only the first locus gives degree-sixteen plane normalizations. The derivative contradiction persists across the entire family. The broader two-fixed-coordinate exclusion requires literal \(U_0=s^4,U_1=s^3t\) and full inverse support; it is **not** a normal form for all plane projections.

### 10.2 A reusable off-curve differential test

Let \(Q\in H^0(S,H)\) have divisor \(mc\), and suppose \(p\in S\setminus c\) is smooth. If \(v\in\ker(d\nu_p)\) and \(d(Q/\nu^*h)_p(v)\ne0\) for a local downstairs frame \(h\), no positive power of the polarization can descend with zero support precisely \(C\), in characteristic zero. Indeed a putative mate pullback must equal a scalar multiple of \(Q^b\), whereas differentials of downstairs functions annihilate \(\ker d\nu_p\). This detects an **off-curve infinitesimal conductor defect** even when the reduced residue class is trivial.

For the explicit map above, in \(z=1\), \(r=s/z,y=t/z\), take \(p=(0,1)\) and frame \(U_2\). Then \(q=Q/U_2=1/(1+ry^3)\), and \(v=\partial_r+\tfrac14\partial_y\) belongs to \(\ker d\nu_p\) while \(dq_p(v)=-1\).

### 10.3 The finite support-covering criterion

For the full conductor descent lattice \(\Lambda_{\mathrm{desc}}\), the monoid \(\Lambda_{\mathrm{desc}}\cap\mathbf N^{s+1}\) has a finite Hilbert basis. A fully positive vector exists exactly when the supports of the basis elements together cover all inverse branches \(\Gamma_j\); summing a support-covering collection gives a candidate. Equivalently one may test the extreme rays of the rational nonnegative cone. **An individual Hilbert-basis element need not be a mate**: it may omit some branches.

This is an abstract finite reduction, not an effective algorithm until the class group and full conductor-unit relations have been computed. In the singleton generically regular case, every candidate lies on the primitive ray \((a/g,c/g)\). If \(\mathrm{Cl}(S)\) is torsion-free and a mate exists, the primitive upstairs section has degree \(c/g\le c\). For a degree-four curve this gives upstairs base degrees among \(1,2,4\), not a bound on the actual descending mate degree.

### 10.4 The characteristic-zero nilpotent defect

For the actual Artinian conductor extension \(A\subset B\), the relevant obstruction is \(B^*/A^*\). In characteristic zero, after separating reduced residue classes, a nilpotent unit has a logarithm, and its class has finite order only when its logarithmic defect vanishes. Thus torsion of reduced residue phases does **not** imply descent of a chosen power. With several residual branches, relative root-of-unity phases can have unbounded order even for fixed small residual degree (e.g. \((1,\zeta)\) in \(k\times k\) modulo diagonal \(k^*\)). In characteristic \(p\), sufficiently large \(p\)-powers kill nilpotent units; this does not kill non-torsion residual ratios.

### 10.5 Local conductor–Jacobian contact

The source for R-0036 supplies a useful intermediate identity. In completed local coordinates \(C=(y,z)\), \(S=(t,u)\), with \(\nu(t,u)=(t,Y(t,u),Z(t,u))\), let \(h\) generate the invertible conductor. Finite duality and hypersurface residues yield, up to a common unit,
\[
F_z\circ\nu=hY_u,\qquad F_y\circ\nu=-hZ_u.
\]
Restricting to \(u=0\) gives the **ideal identity**
\[
(F_y,F_z)|_c=(h|_c)(Y_u,Z_u)|_c.
\]
Consequently, if \(D_F\) is the common-zero divisor of the actual first normal symbol and \(A\) the zero divisor of the transverse differential, then
\[
D_F=B|_c+A.
\]
This explains why the differential divisor alone does not measure conductor contact. For the three necessary quartic models, the source computes \(B\cdot c=20,20,51\) (smooth quadric, cone, plane respectively), using \(B\sim(a-4)H-K_S\) and adjunction. These are necessary numerical contacts, not existence certificates.

### Source status for this expansion

Directly inspected source proofs: `notes/2026-10-13-generalization-conductor-theorem.md`, `notes/2026-10-19-singleton-projection-investigation.md`, and `notes/2026-10-14-generalization-projection-conductor-jacobian-bridge.md`. This expansion preserves their concrete calculations and argument mechanisms. Their independent audit files, other historical conductor examples, and source-complete proof reconciliation remain outstanding. No historical files are deleted.

## 11. Normal-carrier index mechanism (source-level reconstruction)

The full proof of R-0034/R-0035 distinguishes the actual local Cartier index r of C on a normal carrier from both surface multiplicity and tangent-cone data. If the mate multiplicity is n=kr and h locally cuts rC, normality and height-one valuations give (h^k:I)=h^(k-1)(h:I) and Soc(W_n)=h^(k-1)Soc(W_r). The relative complete-intersection Jacobian and Gorenstein duality then yield the pointwise identity D_n,P=(k-1)A_F,P+kD_r,P. For ordinary J-adic torsion layers T_i, the Frobenius pairing also gives 2 sum_i length(T_i)_P=n D_n,P. This latter statement does not erase saturated BF-filtration multiplication defects.

For C0, let a=deg F, b=deg G, n=ab/4 and first free normal quotient O(-ell), ell<=7. The proof computes deg D_n=(n-1)ell-4(a+b)+14 and deg A_F=4a-14+ell. A bound s on every actual on-curve index gives s(ell-16/a)>=4a-14+ell, hence 4a^2-(7s+7)a+16s<=0. This bounds carrier degree in terms of s, not uniformly without an index bound.

For s=4, inherited torsion/index and low-degree results reduce to the minimal pair (a,b)=(6,8), n=12. For an octic, deg(D_n-2A_F)=9ell-78 is negative. For a sextic, 9ell-62 forces ell=7, deg D_n=35, deg A_F=17, and total slack one. The local expression D_n,P-2A_F,P=(k-3)A_F,P+kD_r,P then excludes index-two points and positive primitive socle defects at index-three/four points. The remaining primitive triples glue to an embedded primitive triple with constant first-normal direction O(-7)^2 -> O(-7), contradicting the inherited P-010 quadratic obstruction. Thus R-0035 excludes all normal integral carriers with actual on-curve indices at most four, subject to the explicit inherited results. Index six and twelve (k=2 and 1), higher indices, nonnormal carriers, and entirely thick presentations remain outside this exclusion.

Source: research/notes/2026-10-14-generalization-normal-index-socle-theorem.md. The separate filtered-compatibility proof has not been independently reconstructed in this consolidation pass.

## 12. Audited local first-order obstruction for the plane family

The independent review of R-0017 gives an exact generic conductor-local calculation. In the source chart z=1, write r=s/z, y=t/z. At the generic boundary D=(r=0), the normalization DVR is B=k(y)[r]_(r), with residue E=k(y). For the eleven-parameter family, the target residue field is K=k(g(y)/alpha), where g(y)=y^4+P(0,y,1); the extension E/K has degree four. On the target chart X2 nonzero, the local coordinate functions are a0=r^4/(alpha+r y^3), a1=r^3 y/(alpha+r y^3), and w=(y^4+P(r,y,1))/(alpha+r y^3).

Modulo r^2, any target-local element, including fractions with denominators invertible at the generic boundary, is represented by R(w) for a rational function R. If its residue is constant, injectivity of K into E forces R to be constant, so its first r-coefficient vanishes. In contrast, the candidate ray unit q^b=(alpha+r y^3)^(-b) has expansion alpha^(-b)-b alpha^(-b-1)y^3 r modulo r^2, whose linear coefficient is nonzero in characteristic zero for every b>0. Therefore no power descends even though the reduced residue phase is trivial. This is a concrete counterexample to replacing the full conductor-unit test by reduced residue torsion.

The independent review in research/notes/2026-10-19-singleton-plane-projection-independent-audit.md confirms the explicit map, full inverse support, family birationality criterion, all-degree exclusion, differential-kernel test, local first-order defect, and the literal two-fixed-coordinate sublane. It does not classify arbitrary plane projections or determine the complete conductor phase image.

## 13. Historical cuspidal and ruled-cubic examples

The imported Space Curves III examples illustrate distinct obstructions within the fixed-carrier criterion, and should not be conflated.

* Cuspidal cubic: on the carrier y^3-x^2 z=0, the necessary divisor proportionality holds on normalization, but the nonreduced conductor quotient has a nonzero additive polar term -3 z^(-2). This prevents descent of every positive power in characteristic zero. The symbolic companion checks an explicit Cartier identity and a conductor restriction, but does not independently prove the global conductor identification.
* Ruled cubic: on x z^2-y^2 w=0, local pinch-point torsion is compatible with descent of a power, but normalization classes H=(2,1) and lifted C=(2,0) are not positively proportional. Here the obstruction is already in the normalization divisor lattice, not in the local conductor unit group.

These are historical examples, not new exclusions of unaddressed carrier degrees. Source: research/archive/space-curves-2026-10-19/README.md, section 4, and its linked Space Curves III artifacts and symbolic companion. The imported status is historical/source-reviewed, not independently promoted.

## 14. A stronger but bounded scroll-conductor exclusion

The October 8 adversarial source proves a conditional result for an integral quartic carrier normalized by a smooth rational quartic scroll, generically regular along C0. If the actual conductor center is a smooth twisted cubic Gamma and its upstairs conductor D maps finite flat of rank two to Gamma, there is no mate in any degree. Crucially D need not be reduced.

Finite duality gives the actual upstairs conductor divisor D linearly equivalent to -K_S. The rank-two algebra on Gamma=P1 splits by trace as O + O(-2) eta, with eta^2=Delta, Delta a quartic section. The proof separates:

* Integral reduced D: invariance of a descending power forces the square of the upstairs primitive section to descend. This produces a quadric cutting C0 on the quartic carrier, contradicting the unique smooth quadric's bidegree (1,3) against the carrier intersection class (4,4).
* Reducible reduced D: Delta=q2^2. The two branches glue modulo q2, including tangencies. Their section restrictions differ by a root of unity. Nontrivial phase forces simultaneous branch contact exceeding their mutual intersection multiplicity, impossible for a third smooth branch by a local Taylor expansion.
* Nonreduced D: Delta=0, eta^2=0. If f=a+b eta, descent of f^n forces n a^(n-1)b=0; characteristic zero and a nonzero force b=0, so f itself descends, producing an impossible hyperplane.

The source also proves that assuming the *entire nonnormal support* is a smooth twisted cubic suffices to recover the conductor hypotheses: the actual conductor center has Hilbert polynomial 3m+1, is pure Cohen-Macaulay and therefore reduced on its smooth degree-three support; upstairs D is finite flat of rank two by torsion-freeness over Gamma and H.D=6. A further applicability argument proves every integral quartic singular along a smooth twisted cubic has this scroll normalization: the space of quartics singular along the cubic is the six-dimensional span of products of its three quadratic generators, and integrality gives a smooth conic in the associated quadratic-map target. The incidence blowup identifies its normalization as a smooth quartic scroll. The source reports independent exact symbolic checks of the derivative matrix and rank. These statements remain scoped to a smooth twisted-cubic singular support; singular or reducible degenerations are not covered. Moreover quartic carriers are already excluded for C0 by R-0001, so this is valuable mechanism and geometry rather than a newly open quartic case.

Source: research/notes/2026-10-08-session-scroll-conductor-adversarial.md and its cited applicability and computation companions. The argument is retained without generalizing its rank-two conductor hypotheses to arbitrary scroll projections.

## 15. A nonreduced ramification counterexample

The exact local model X: X^2+Y^2(Y+Z^2)=0 has normalization k[w,z] via X=-w^3-wz^2, Y=-w^2-z^2, Z=z. Its actual conductor is YB and its relative differential Fitting ideal is (w,z^2), a length-two ramification scheme. The smooth image curve X=-2Z^3, Y=-2Z^2 has lift c=(w-z), and the full pulled-back curve ideal is (w-z)(w+z,z^2), so the *full reduced inverse support* is c. Nevertheless the ramification scheme is not contained scheme-theoretically in c, since w-z maps to -z modulo (w,z^2).

More generally for c_f=(w-f(z)), h=ord(f) and r=ord(f^2+z^2), the source computes length(R intersect c_f)=min(h,2), with scheme containment exactly when h>=2. Choosing f=iz+z^k gives unbounded conductor contact r=k+1 but ramification intersection length one. The local Jacobian factorization J_X B=(Y) I_R yields first-normal vanishing order s=r+min(h,2). This blocks the unsupported inference from smooth image plus full inverse support to containment of nonreduced ramification. It is a local counterexample, **not** an STCI presentation or a global normalization classification.

Source: research/notes/2026-10-07-session-ramification-scheme-counterexample.md, with its exact symbolic verifier. These local distinctions should be preserved in future conductor/ramification arguments.

## 16. Remaining Phase 2 coverage

The historical Space Curves III artifact proofs and scripts, the October 8 scroll applicability companion, the October 21 conditional (2,12) singular-gluing analysis, and the October 24 cubic-scroll/P4 normalization work require a separate scope decision or closer source reading. The latter two may belong primarily to other investigation families, rather than being absorbed wholesale into this dossier. No claim of exhaustive coverage is made, and no original mathematical sources are deleted.


## 17. Ruled-model and conditional conductor continuation

The companion [Phase 2 addendum](normalization_conductor_phase2_addendum.md) consolidates the paired-secant cubic's finite F1 normalization and double-line conductor, the nonnormal projection cone and its F4 resolution, the four-section quartic's nonreduced conductor, and the reviewed conditional (6,16) singular-root/conductor frontier. Crucially, the October 21 independent continuation audit verifies the previously conditional cubic-model contraction in the exact actual-pair setting and forces a multiple base zero of alpha or a zero of alpha at a spectral-root node. This does not eliminate those exceptional strata or prove an STCI exclusion. The original historical sources remain retained; the separate codex branch is excluded.


## 18. Effective conductor phase framework

The independently reviewed October 15 torsion-coset theorem constructs a finite-type admissible phase family retaining full nilpotent conductor equations. Mate existence on a carrier is equivalent to an actual torsion phase tuple. Across the family, the retained constructible torsion-coset envelope distinguishes absence of mates, uniformly bounded least mate degrees, and unbounded least mate degrees. A separate independently reviewed rational-phase theorem gives an in-principle terminating decision algorithm using constructible stratification, elimination, Mann partitions, and Smith normal forms. Neither theorem computes the phase images or determines the alternative for the three fixed quartic projection families. Sources: research/notes/2026-10-15-generalization-projection-torsion-coset-reduction.md and research/notes/2026-10-15-generalization-effective-rational-phase-bound.md, with their independent reviews. See phase2_closeout_checks.md for source reconciliation.
