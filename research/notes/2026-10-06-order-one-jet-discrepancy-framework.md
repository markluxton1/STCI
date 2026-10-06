# Order-one jet discrepancy for quartic carriers

Date: 2026-10-06

Base audited commit: fa98d696da36c6a362afaf27d40cc0867fe9aa12 (main).

Status: structural research note. Statements are labelled individually. This note does **not** prove that the rational quartic is not an STCI.

## 0. Scope and audited starting point

Work in characteristic zero on the fixed smooth monomial rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3,
\]
with unique smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\). The audited order-one setup has
\[
N_C^*\simeq O_C(-7)^2\twoheadrightarrow L\simeq O_C(e-7),\qquad e=0,1,2
\]
for quartic carriers. The canonical audited-state file controls older notes.

The audited e=2 result is stronger than the older P-044-slice formulation: the universal fourth-extension obstruction has reduced zero locus
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on this whole resultant-open locus
\[
H^0(I_{C_3}(4))=H^0(I_{C_4}(4))=T\,H^0(O_{\mathbf P^3}(1)).
\]
This is certified by the universal primitive-quadruple verifier and independently reconstructed by the quartic-factor audit. The dx=1 P-044 saturation certificate is now closed, but it is not needed for the global e=2 carrier exclusion.

## A. Intrinsic setup

### A.1 Successive condition maps

Let \(C=C_1\subset C_2\subset\cdots\subset C_m\) be primitive with conormal line \(L\), so \(I_{C_j}/I_{C_{j+1}}\simeq L^j\). For degree \(a\), put
\[
V_j(a)=H^0(I_{C_j}(a)),\qquad W_j(a)=H^0(L^j(a)),
\]
and let \(\rho_j(a):V_j(a)\to W_j(a)\) be restriction.

**PROVED (formal).** Define
\[
\eta_j(a)=\dim W_j(a)-\operatorname{rank}\rho_j(a)
\]
(the target shortfall) and
\[
\delta_j(a)=\min\{\dim V_j(a),\dim W_j(a)\}-\operatorname{rank}\rho_j(a)\ge0
\]
(the intrinsic maximal-rank defect). Then
\[
\dim V_{j+1}(a)=\dim V_j(a)-\dim W_j(a)+\eta_j(a).
\]
Thus numerical budget and genuine dependence are separated. For quasiprimitive structures with saturated pieces \(E_j=L^j(D_j)\), use \(W_j(a)=H^0(E_j(a))\); the BF divisors \(D_j\) alter the targets and must not be conflated with rank defects.

### A.2 Quadric comparison divisor

The conormal sequence for \(C\subset Q\subset\mathbf P^3\) is
\[
0\to O_C(-8)\to N_C^*\to O_C(-6)\to0.
\]
Let \(M=\ker(N_C^*\twoheadrightarrow L)\). Since \(\det N_C^*=O(-14)\),
\[
M\simeq O_C(-e-7).
\]
The composite \(O_C(-8)\to N_C^*\to L=O_C(e-7)\) is a section \(r\in H^0(O_C(e+1))\). Let \(R=Z(r)\).

**PROVED.** The induced map \(M\to O_C(-6)\) is multiplication by the same section up to scalar. Hence
\[
M\simeq O_C(-6)(-R),\qquad \deg R=e+1.
\]

### A.3 First quartic source

Twisting by \(O_C(4)=O_C(16)\) gives
\[
M(4)=O_C(9-e)\xrightarrow{\cdot r}O_C(10).
\]
After restricting a quartic to \(Q\) and removing \(C\), its residual lies in \(H^0(O_Q(1,3))\), restricting to \(O_C(10)\). Define
\[
K_R=\{h\in H^0(O_C(9-e)):rh\text{ extends to }H^0(O_Q(1,3))\}.
\]

**PROVED.**
\[
K_R\simeq H^0(Q,I_{R/Q}(1,3)).
\]
If \(\operatorname{ev}_R:H^0(O_Q(1,3))\to H^0(O_R(1,3))\), define
\[
\epsilon_Q(R)=\ell(R)-\operatorname{rank}(\operatorname{ev}_R).
\]
Then
\[
\dim K_R=7-e+\epsilon_Q(R).
\]

**PROVED.** For e=0 and e=1, \(\epsilon_Q(R)=0\) for every possible \(R\): \(O_Q(1,3)\) separates every length-one and length-two subscheme. Thus
\[
\dim K_R=7\ (e=0),\qquad \dim K_R=6\ (e=1).
\]
For e=2, length-three schemes can fail to impose three independent conditions. The audited ruling-fiber case has \(\epsilon_Q(R)=1\), hence \(\dim K_R=6\). The first source rank jump is therefore genuinely an e=2 phenomenon.

### A.4 The second primitive quartic condition localizes on 2R

Assume the primitive triple \(C_3\) exists. Then
\[
\rho_2:H^0(I_{C_2}(4))\to H^0(L^2(4))=H^0(O_C(2e+2)).
\]
The quadric square satisfies \(\rho_2(Q^2)=r^2\), up to normalization. Quotienting gives
\[
\bar\rho_2:K_R\to H^0(O_C(2e+2))/\langle r^2\rangle
\simeq H^0(O_{2R}(2e+2)).
\]

**PROVED.** Define
\[
\delta_2^Q(R,C_3)=\min\{\dim K_R,2e+2\}-\operatorname{rank}\bar\rho_2.
\]
For e=0,1,2 the generic source/target sizes are
\[
(7,2),\qquad(6,4),\qquad(5,6).
\]
Only e=2 is generically overdetermined at this stage.

## B. e=2 reconstruction

For e=2 write the quotient by binary quadratics \(A,B\). The comparison section is \(r=A+zB/2\). The exact universal fourth-obstruction locus is
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on it
\[
2r=2A+zB=2a_0+b_2z^3.
\]
Under the standard \(C\subset Q\) identification, the relevant ruling coordinate restricts as \(z^3\).

**PROVED.** Every basepoint-free e=2 quotient extending to the canonical primitive quadruple has
\[
R=C\cap F
\]
for a ruling fiber \(F\subset Q\). Thus the fourth-extension condition itself forces the first quartic source to jump from dimension 5 to 6. This is the intrinsic content behind the old P-045 ruling observation, now on the entire universal fourth-obstruction locus.

**EXACT COMPUTATIONAL CERTIFICATE.** On this locus both \(K_R\) and the finite target of \(\bar\rho_2\) have dimension six, but the audited universal contact matrix has rank exactly three everywhere. Two explicit 3x3 minors, \(-a_0^8\) and \(-b_2^8/256\), cover the parameter space, while all 4x4 minors vanish identically. Hence
\[
\operatorname{rank}\bar\rho_2=3,\qquad \delta_2^Q=3.
\]
In the seven-dimensional ambient pre-contact space (six \(K_R\) directions plus \(Q^2\)), the kernel is four-dimensional and
\[
\boxed{H^0(I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).}
\]

**OPEN CONCEPTUAL STEP.** The ruling condition explains the source jump. The further rank-three collapse is stronger: three of six finite \(2R\) conditions become dependent. The exact matrix proves this universally, but a coordinate-free factorization of \(\bar\rho_2\) through a natural rank-three space attached to the ruling and extension class is still missing.

**PROVED.** BF duality forces the canonical fourth layer to be primitive for the e=2 branches of (4,7) and (4,8). Hence every defining quartic is \(T\ell\). For any mate \(G\), \(V(\ell,G)\) contributes an extra projective curve (or the whole plane), so these e=2 branches are excluded.

## C. e=0 analysis

Here \(L=O(-7)\), \(M=O(-7)\), and \(R\) has length one.

The embedded primitive-triple obstruction lies in
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-7)),
\]
of dimension six.

**PROVED (standard primitive-extension obstruction calculation).** Unlike e=2, a primitive double of direction e=0 does not automatically extend to a triple. If it extends, uniqueness follows from \(H^0(O(-7))=0\). This is compatible with P-010: the defect-free primitive e=0 triple is globally excluded, so positive \(D_2\) is essential in a quasiprimitive carrier filtration.

**PROVED.** Every length-one \(R\) imposes one independent condition on \(|O_Q(1,3)|\), so \(\dim K_R=7\). If a primitive triple existed,
\[
\bar\rho_2:K_R\;(\dim7)\to H^0(O_{2R}(2))\;(\dim2).
\]
Maximal rank would still leave a five-dimensional kernel.

**PROVED NEGATIVE STRUCTURAL RESULT.** The e=2 overdetermined-jet mechanism cannot extend verbatim to e=0. The hard geometry moves to triple existence and, for actual quasiprimitive carriers, to the defect divisor \(D_2\).

**PROVED CONNECTION TO MF6.** MF6 gives \(\deg D_2\ge3\) for e=0 saturated multiplicity-six lci/Gorenstein thickenings and excludes the nonregular (3,6) branch. The surviving (4,5) MF6 incidence lives in a modified target \(L^2(D_2)\), not the primitive target \(L^2\).

**OPEN.** Recast the MF6 type-(4,5) matrix as the quasiprimitive analogue of \(\bar\rho_2\) and identify its exceptional high-gcd locus geometrically.

## D. e=1 analysis

Here \(L=O(-6)\), \(M=O(-8)\), and \(R\) has length two.

\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-4))
\]
has dimension three, while \(H^0(O(-4))=0\).

**PROVED.** Triple existence is a three-coordinate obstruction and, when it exists, the embedded primitive triple is unique. Thus e=1 differs fundamentally from e=2 before quartic second-jet dependence is considered.

**PROVED.** Every length-two subscheme imposes two independent conditions on \(|O_Q(1,3)|\). Hence \(\dim K_R=6\) for every e=1 quotient direction; there is no e=2-style source jump. For an existing primitive triple,
\[
\bar\rho_2:K_R\;(\dim6)\to H^0(O_{2R}(4))\;(\dim4).
\]
Maximal rank leaves a two-dimensional quartic kernel, so quartic survival requires no rank defect.

**OPEN.** Determine the rank of \(\bar\rho_2\) on the actual three-obstruction-zero locus of e=1 primitive triples, and determine whether that locus forces a recognizable incidence condition on \(R\) or on the second-order extension class.

The audited BF/MF6 e=1 possibilities \((d_2,d_3)=(0,4),(1,3),(2,2)\) should be separated into: first solve the triple-extension obstruction in \(H^1(O(-4))\); then study the finite \(2R\) evaluation map, modified to \(L^2(D_2)\) when \(D_2>0\).

## E. General principle

**PROVED FRAMEWORK.** For a fixed filtration and carrier degree, the signed budget
\[
B_j=\dim V_j-\dim W_j
\]
and maximal-rank defect
\[
\delta_j=\min(\dim V_j,\dim W_j)-\operatorname{rank}\rho_j
\]
separate numerical over/underdetermination from genuine dependence. Rank-defect loci are determinantal loci of families of restriction maps.

**PROVED.** For e=0,1,2, the first two primitive quartic stages are controlled by
\[
R\in |O_C(e+1)|,\qquad
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)).
\]
The source discrepancy is exactly the failure of \(R\) to impose independent conditions on \(|O_Q(1,3)|\). It vanishes identically for e=0,1 and can occur for e=2. On the e=2 fourth-extension locus, extension compatibility forces \(R\) to be a ruling-fiber divisor and the second map has certified rank defect three.

**CONJECTURE.** On the e=2 fourth-extension locus, \(\bar\rho_2\) factors coordinate-freely through a natural rank-three space attached to the ruling fiber and extension class. Such a factorization would explain both rank three and the cubic-times-linear kernel.

**PROVED NEGATIVE RESULT.** There is no uniform theorem saying quartic survival for e=0,1,2 requires jet-rank degeneracy. It is false numerically for e=0 and e=1. A correct uniform theory must include extension-existence obstructions and BF defect divisors, not only containment-map ranks.

## F. Connections

**Local cohomology — PROVED CONCEPTUAL CONNECTION, not an identification theorem.** The local-cohomology quartic problem is also determinantal: an ancestor \(a\) defines a multiplication matrix \(L(a)\), and multiplier existence is \(\operatorname{rank}L(a)=\operatorname{rank}N(a)+2\). Exact local-cohomology work independently finds exceptional degree-two directions aligned with the e=2 fourth-zero family. A canonical identification with \(\bar\rho_2\) is **OPEN**.

**MF6 — PROVED CONCEPTUAL CONNECTION.** MF6 defect divisors record failure of the primitive associated graded algebra to remain pure powers of \(L\). They modify jet targets from \(L^j\) to \(L^j(D_j)\). MF6 pole/incidence calculations are a quasiprimitive refinement of the jet-budget framework, but the pole divisor is not itself the rank defect.

**P-044/P-045 — PROVED.** The old P-045 ruling condition is the dx=1 shadow of the universal e=2 statement that fourth-extension compatibility forces \(R\) to be a ruling-fiber divisor. The exact dx=1 saturation certificate closes that slice, but the universal primitive-fourth certificate is the stronger carrier input.

**Deformation/extension theory — PROVED.** The obstruction groups
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O(3e-7))
\]
explain why e=0,1,2 differ before any quartic rank count: their dimensions are 6,3,0.

## G. Single highest-value next attack

**OPEN / RECOMMENDED LEMMA.** Construct the e=1 triple-extension obstruction intrinsically as a map from the quotient pencil
\[
N_C^*\twoheadrightarrow O(-6)
\]
to
\[
H^1(O(-4))\simeq k^3,
\]
and determine its reduced zero locus together with
\[
\bar\rho_2:H^0(I_{R/Q}(1,3))\to H^0(O_{2R}(4)).
\]

The target is a geometric description of the obstruction-zero locus, followed by maximal-rank/rank-drop analysis of \(\bar\rho_2\) on its geometric strata. This directly tests whether e=2 has a genuine e=1 analogue while respecting the fact that e=1 is not dimensionally overdetermined.

A secondary target is the coordinate-free rank-three factorization of the e=2 map.

## Reproducibility / provenance

No new random-specialization computation is promoted here. New statements are deductions from exact sequences, line-bundle degrees, separation properties of \(O_Q(1,3)\), and already-audited universal e=2 certificates. Existing theorem-level computational inputs remain the universal primitive-quadruple verifier, the independent quartic-factor audit, the dx=1 saturation certificate, and the exact local-cohomology incidence certificates cited by the audited state.

No statement here upgrades an OPEN local-cohomology, MF6, e=0, or e=1 locus to an exclusion.


## H. Literature audit and novelty boundary

Literature search performed 2026-10-06 before continuing the e=1 calculation.

### H.1 Bănică--Forster: extension theory is established machinery

C. Bănică and O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64, is the primary antecedent for the embedded primitive/quasiprimitive filtration used here.

Their Proposition 2.4 states, in the present notation, that extending a primitive multiplicity-k structure \(Z'\) of type \(L\) to multiplicity \(k+1\) is equivalent to choosing a retraction of
\[
0\to L^k\to \nu_{Z'}|_C\to M\to0,
\qquad
M=\ker(\nu_C\twoheadrightarrow L).
\]
Their Corollary 2.5 identifies the splitting obstruction/torsor groups as
\[
H^1(\det(\nu_C)^*\otimes L^{k+1}),\qquad
H^0(\det(\nu_C)^*\otimes L^{k+1}).
\]
For the rational quartic, \(\det\nu_C=O(-14)\), so for double-to-triple extension (\(k=2\)) this is exactly
\[
H^1(O(14)\otimes O(3e-21))=H^1(O(3e-7)).
\]

**LITERATURE-ESTABLISHED, NOT NEW.** The obstruction groups of dimensions \(6,3,0\) for e=0,1,2 are a direct specialization of Bănică--Forster. Likewise their Section 3 already gives the CM filtration, quasiprimitive line bundles \(L_j=L^j(D_j)\), superadditivity \(D_i+D_j\le D_{i+j}\), and the interpretation of later quasiprimitive extensions as meromorphic retractions. These should be cited as the conceptual source of the BF language used throughout STCI.

Source: C. Bănică--O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64; electronic copy on O. Forster's LMU page.

### H.2 Drézet: modern intrinsic parametrization

Jean-Marc Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, develops primitive curves of arbitrary multiplicity by gluing \(U_i\times\operatorname{Spec}\mathbf C[t]/(t^n)\) and nonabelian \(H^1\). His later survey and papers develop extension, deformation, and moduli theory further.

**LITERATURE-ESTABLISHED, NOT NEW.** Treating primitive multiple curves intrinsically via their canonical filtration and associated line bundle, rather than by ambient coordinates, is standard. Any eventual general theorem should be phrased compatibly with this literature rather than advertised as a new theory of primitive multiple curves.

Relevant sources:
- J.-M. Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, arXiv:math/0605726.
- J.-M. Drézet, *Primitive multiple schemes*, Eur. J. Math. 7 (2021), 985--1045, arXiv:2004.04921.
- J.-M. Drézet, *Primitive multiple curves: classification, deformations and moduli spaces of sheaves* (survey, 2013).

### H.3 Rational-quartic STCI literature

The rational quartic is a classical unresolved characteristic-zero STCI problem. Relevant antecedents found in the search include:

- P. C. Craighero--R. Gattazzo (1986): the monomial rational quartic is not the set-theoretic intersection of two quartic surfaces.
- P. C. Craighero--R. Gattazzo (1989): no smooth rational quartic is an STCI on a cubic surface.
- D. B. Jaffe, *Applications of iterated curve blow-up to set theoretic complete intersections in P3*, J. reine angew. Math. 464 (1995), 1--46: finite numerical lists of possible degree pairs under the stated hypotheses; for \((d,g)=(4,0)\) the list includes \((4,7)\).
- Ph. Ellia, *Primitive set-theoretic complete intersections* (arXiv:1409.3801): numerical restrictions for primitive STCI structures. Corollary 16 leaves ten rational-quartic numerical cases, including \((a,b,l)=(4,7,5)\), and explicitly describes its improvement over Jaffe as numerical rather than a full rational-quartic exclusion.

**LITERATURE CHECKED / NO PRIOR IDENTIFICATION FOUND.** In the sources located in this search, no formulation was found of the STCI quartic-carrier problem as the pair
\[
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)),
\]
nor a derivation of the e=2 cubic-times-linear factorization from a determinantal rank collapse on the fourth-extension locus. Absence from this search is not a proof of novelty; a stronger novelty claim requires a targeted bibliography/citation-chain search.

### H.4 Ropes/ribbons literature

The ribbon/rope literature (Bayer--Eisenbud for ribbons; later Gallego--González--Purnaprajna and Drézet for ropes/primitive multiple curves and deformations) confirms that embedded multiple structures, conormal bundles, and deformation maps are mature subjects.

**NOVELTY BOUNDARY.** The potentially project-specific contribution is therefore not:
1. the canonical filtration;
2. conormal quotient \(L\);
3. extension obstruction groups;
4. defect divisors for quasiprimitive structures; or
5. determinantal loci in the abstract.

The candidate new ingredient is their **specific coupling for the rational quartic carrier problem**:
\[
\text{BF extension data}
\longrightarrow R\subset C\subset Q
\longrightarrow K_R
\longrightarrow \text{finite jet evaluation on }2R
\longrightarrow \text{ambient factorization}.
\]
The universal e=2 computation supplies a nontrivial instance where extension compatibility forces a special incidence locus for \(R\), and that incidence is followed by an additional rank-three collapse of the ambient quartic jet map.

### H.5 Revised status of the framework

**PROVED + LITERATURE-ALIGNED.** The two-layer organization
\[
\text{existence/splitting of the multiple structure}
\quad+\quad
\text{rank of ambient containment maps}
\]
is the correct framework, but the first layer is Bănică--Forster/Drézet theory.

**PROJECT-SPECIFIC PROVED RESULT.** For the rational quartic and quartic carriers, the quadric comparison converts the ambient first-symbol problem into evaluation of \(O_Q(1,3)\) on \(R\), and the next primitive containment condition into a finite map on \(2R\). The e=2 fourth-extension locus forces \(R\) to be a ruling divisor and has exact ambient rank three.

**OPEN NOVELTY QUESTION.** Determine whether this \(R/2R\) ambient-carrier reduction, or an equivalent construction, already occurs in the older literature on contact of surfaces along curves (notably Gallarati), infinitesimal neighborhoods, or Rees/principal-parts methods. Search should continue before publication-level novelty claims.

## I. Revised next attack after literature audit

The highest-value mathematical calculation remains e=1, but it should now be posed explicitly as a **Bănică--Forster splitting problem plus ambient carrier map**, not as invention of a new obstruction theory.

Let \(L=O(-6)\), \(M=O(-8)\). Starting from the Ferrand double \(C_2\), compute the BF extension
\[
0\to L^2=O(-12)\to \nu_{C_2}|_C\to M=O(-8)\to0.
\]
Its class lies in
\[
\operatorname{Ext}^1(M,L^2)=H^1(O(-4)).
\]
The next exact target is:

1. express this extension class intrinsically in terms of the quotient \(N_C^*\twoheadrightarrow O(-6)\) and comparison divisor \(R\in|O_C(2)|\);
2. determine its reduced splitting locus in the resultant-open quotient parameter space;
3. only on that locus, form the ambient map
   \[
   \bar\rho_2:H^0(I_{R/Q}(1,3))\to H^0(O_{2R}(4));
   \]
4. determine whether its rank-drop locus has a geometric incidence description.

This cleanly separates standard extension theory from the genuinely unresolved ambient-STCI geometry.
