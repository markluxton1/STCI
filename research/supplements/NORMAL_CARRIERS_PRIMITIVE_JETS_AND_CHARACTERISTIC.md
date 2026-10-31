# Primitive quartic structures: extension, contact, and factorization

The first unit develops the distinct extension obstruction and ambient
contact maps, including their exact e=1 coordinates and the geometric
limits of a naive jet budget. The second proves the full universal e=2
primitive-fourth classification and cubic factorization. The third gives
a separate parity classification with its bounded fourth-layer defect
obstruction. These statements retain their exact filtration hypotheses;
the [all-degree quartic-carrier theorem](../synthesis/quartic_carrier_proof.md)
is proved independently of the remaining explanatory questions.

---

<a id="2026-10-06-order-one-jet-discrepancy-framework"></a>

## Extension and quartic contact maps on the quadric

Status: structural research note. Statements are labelled individually. This note does **not** prove that the rational quartic is not an STCI.

### 0. Scope and audited starting point

Work in characteristic zero on the fixed smooth monomial rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3,
\]
with unique smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\). In the ruling convention used here, C has class (3,1), and the residual quartic restriction has class (1,3). The audited order-one setup has
\[
N_C^*\simeq O_C(-7)^2\twoheadrightarrow L\simeq O_C(e-7),\qquad e=0,1,2
\]
for quartic carriers. The exact statements below retain their own extension, rank and filtration hypotheses.

The audited e=2 result is stronger than the older P-044-slice formulation: the universal fourth-extension obstruction has reduced zero locus
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on this whole resultant-open locus
\[
H^0(I_{C_3}(4))=H^0(I_{C_4}(4))=T\,H^0(O_{\mathbf P^3}(1)).
\]
This is certified by the universal primitive-quadruple verifier and independently reconstructed by the quartic-factor audit. The dx=1 P-044 saturation certificate is now closed, but it is not needed for the global e=2 carrier exclusion.

### A. Intrinsic setup

#### A.1 Successive condition maps

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

#### A.2 Quadric comparison divisor

The conormal sequence for \(C\subset Q\subset\mathbf P^3\) is
\[
0\to O_C(-8)\to N_C^*\to O_C(-6)\to0.
\]
Let \(M=\ker(N_C^*\twoheadrightarrow L)\). Since \(\det N_C^*=O(-14)\),
\[
M\simeq O_C(-e-7).
\]
The composite \(O_C(-8)\to N_C^*\to L=O_C(e-7)\) is a section \(r\in H^0(O_C(e+1))\). Let \(R=Z(r)\). The finite R and 2R formulas in A.2--A.5 assume r is not identically zero. Section K.4 separately treats the actual e=1 comparison-zero boundary.

**PROVED.** The induced map \(M\to O_C(-6)\) is multiplication by the same section up to scalar. Hence
\[
M\simeq O_C(-6)(-R),\qquad \deg R=e+1.
\]

#### A.3 First quartic source

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

The residual restriction sequence is

    0 -> O_Q(-2,2) -> O_Q(1,3) -> O_C(10) -> 0.

Since H^0(O_Q(-2,2))=0 and H^1(O_Q(1,3))=0, we obtain

    0 -> H^0(O_Q(1,3)) -> H^0(O_C(10))
      -> H^1(O_Q(-2,2)) -> 0.

By Kunneth,

    H^1(O_Q(-2,2))
      = H^1(P^1,O(-2)) tensor H^0(P^1,O(2)),

so this cokernel has dimension 3.

**PROVED.** The previously observed codimension-three first-normal condition is intrinsic: the extendable degree-10 sections are the kernel of the connecting map to H^1(O_Q(-2,2)). In the affine coordinate basis this is the old

    V = <1,z,z^3,z^4,z^6,z^7,z^9,z^10>;

the missing z^2,z^5,z^8 are a coordinate manifestation of the 3-dimensional cohomological obstruction.

#### A.4 The second primitive quartic condition localizes on 2R

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

<a id="2026-10-06-quartic-jet-geometry-structural-supplement"></a>

#### A.5 Local first and second jet conditions for e=2

This subsection records the local derivation; signs depend on choices of local generators, but the structural content does not.

Choose local coordinates near p in R:
- u along C,
- v normal to C inside Q,
- w an equation for Q.

Then I_C=(v,w). Normalize the primitive quotient locally so that, to first order,

    v |-> epsilon,    w |-> r epsilon.

Write the canonical triple as

    v = epsilon + alpha epsilon^2,
    w = r epsilon + beta epsilon^2  mod epsilon^3,

and set kappa=beta-r alpha.

A quartic containing C_2 has local expansion

    F = h(w-rv) + 1/2(A v^2 + 2Bvw + Cw^2) + O(I_C^3).

Substitution gives

    rho(F) = h kappa + 1/2(A+2Br+Cr^2),

and modulo r^2,

    bar-rho(F) = [h kappa + A/2 + Br]_{2R}.

Restricting F to Q, write F|_Q=v d_h, where d_h=0 is the residual (1,3)-divisor D_h. Then locally

    d_h = -rh + (A/2)v + ...

At a simple p in R, if u=r is used as local parameter,

    partial_u d_h(p) = -h(p),
    partial_v d_h(p) = A(p)/2.

Thus the value component of bar-rho(F)|_{2p} prescribes a relation between the tangent and transverse derivatives of D_h at p:

    partial_v d_h(p) - kappa(p) partial_u d_h(p) = 0

up to the sign convention for kappa.

**PROVED LOCALLY, subject to the stated generator/sign conventions.** One of the two new conditions at each p in R is a prescribed tangent-direction/contact condition for D_h.

The second coefficient modulo r^2 involves a second jet of d_h, not merely its first jet. Therefore it is premature to identify all six new conditions with containment of three fixed doubled points in Q.

### B. e=2 reconstruction

For e=2 write the quotient by binary quadratics \(A,B\). The comparison section is \(r=A+zB/2\). The exact universal fourth-obstruction locus is
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on it
\[
2r=2A+zB=2a_0+b_2z^3.
\]
Under the standard \(C\subset Q\) identification, the relevant ruling coordinate restricts as \(z^3\).

In the dx=1 coordinate normalization the exact comparison is

    r=x+(a+1/2)z+(1+b/2)z^2+(d/2)z^3.

It is pulled back from a linear equation in that ruling coordinate
if and only if a=-1/2 and b=-2. Then r=x+(d/2)z^3; in the dx=1
normalization d=1/x, this is r=x+z^3/(2x). Thus the P-045 condition
is exactly the ruling-fiber condition in these coordinates. The
statement retains its normalization and generator conventions.

**PROVED.** Every basepoint-free e=2 quotient extending to the canonical primitive quadruple has
\[
R=C\cap F
\]
for a ruling fiber \(F\subset Q\). Thus the fourth-extension condition itself forces the first quartic source to jump from dimension 5 to 6. This is the intrinsic content behind the old P-045 ruling observation, now on the entire universal fourth-obstruction locus. On the relevant fiber,
O_Q(1,3) restricts to O_P1(1). A section vanishing on all three points
of R=C intersect F therefore contains F, including the scheme-theoretic
fiber intersection. Dividing its equation by F identifies
K_R with H0(O_Q(1,2)), of dimension six. This supplies the geometric
source-jump proof, separately from the exact second-map rank below.

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

### C. e=0 analysis

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

**PROVED CONNECTION TO MF6.** MF6 gives \(\deg D_2\ge3\) for e=0 saturated multiplicity-six lci/Gorenstein thickenings and excludes the nonregular (3,6) branch. The (4,5) MF6 incidence lives in a modified target \(L^2(D_2)\), not the primitive target \(L^2\).

**OPEN.** Recast the MF6 type-(4,5) matrix as the quasiprimitive analogue of \(\bar\rho_2\) and identify its exceptional high-gcd locus geometrically.

### D. e=1 analysis

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

**The exact coordinate answer appears in Sections J--K below.** An intrinsic incidence interpretation of the obstruction-zero locus remains a separate question.

The audited BF/MF6 e=1 possibilities \((d_2,d_3)=(0,4),(1,3),(2,2)\) should be separated into: first solve the triple-extension obstruction in \(H^1(O(-4))\); then study the finite \(2R\) evaluation map, modified to \(L^2(D_2)\) when \(D_2>0\).

### E. General principle

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

#### E.1 Multiplicity growth and the limits of a jet budget

For a primitive complete intersection of surfaces of degrees a,b supported on a degree-d curve, the multiplicity is

    m = ab/d.

Thus increasing carrier degrees has competing effects:
1. it increases the number of available hypersurface sections;
2. it also increases the required multiplicity, hence the number of infinitesimal layers that must be survived.

The relevant comparison is therefore not a single Hilbert-function count. It is the cumulative loss from the successive ranks (or a more invariant replacement accounting for the changing domains) against the initial carrier freedom.

A naive sum of h^0(L^k(a)) is not sufficient: targets can vanish, maps need not be surjective, and dependencies can be forced by geometry. The C_0 ruling-fiber phenomenon is precisely an example where the geometry of the conormal data changes the rank.

#### E.2 A conditional geometric research question

**HEURISTIC / RESEARCH PROGRAM.** Define an expected jet budget for candidate carrier data by comparing available hypersurface freedom with the ranks expected from the successive maps rho_k.

Negative expected budget should not be interpreted as an automatic obstruction. Rather:

> When the expected jet budget is negative, existence of a carrier forces the conormal/multiple-structure data into degeneracy loci of the successive jet maps.

The useful theorem would therefore have the form

    negative expected jet budget
      => STCI only on specified geometric degeneracy loci.

The substantive problem is to describe those degeneracy loci geometrically.

This suggests a possible division:
- underdetermined cases: carrier freedom exceeds the independent jet conditions, so survival is dimensionally plausible;
- overdetermined cases: STCI requires special geometric dependencies among the jet conditions.

Known STCI examples should eventually be tested against this distinction.

The actual rank c_k of a map with domain dimension s_k always satisfies
c_k<=s_k; a proposed regime s_k<c_k is impossible. Only an *expected*
independent-condition count can exceed the domain dimension. Such a
count supplies a determinantal research question, not a theorem of
nonexistence. The explicit e=0/e=1 source-target calculations above
are negative controls for a blanket rank-degeneracy obstruction.

### F. Connections

**Local cohomology — PROVED CONCEPTUAL CONNECTION, not an identification theorem.** The local-cohomology quartic problem is also determinantal: an ancestor \(a\) defines a multiplication matrix \(L(a)\), and multiplier existence is \(\operatorname{rank}L(a)=\operatorname{rank}N(a)+2\). Exact local-cohomology work independently finds exceptional degree-two directions aligned with the e=2 fourth-zero family. A canonical identification with \(\bar\rho_2\) is **OPEN**.

**MF6 — PROVED CONCEPTUAL CONNECTION.** MF6 defect divisors record failure of the primitive associated graded algebra to remain pure powers of \(L\). They modify jet targets from \(L^j\) to \(L^j(D_j)\). MF6 pole/incidence calculations are a quasiprimitive refinement of the jet-budget framework, but the pole divisor is not itself the rank defect.

**P-044/P-045 — PROVED.** The old P-045 ruling condition is the dx=1 shadow of the universal e=2 statement that fourth-extension compatibility forces \(R\) to be a ruling-fiber divisor. The exact dx=1 saturation certificate closes that slice, but the universal primitive-fourth certificate is the stronger carrier input.

**Deformation/extension theory — PROVED.** The obstruction groups
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O(3e-7))
\]
explain why e=0,1,2 differ before any quartic rank count: their dimensions are 6,3,0.

### G. Intrinsic geometric questions

The coordinate e=1 obstruction and its complete reduced zero locus are
proved in Sections J--K below. The remaining structural question is an
intrinsic construction of the map from the quotient pencil
N_C^* -> O(-6) to H1(O(-4)), with a geometric interpretation of its
splitting locus and the associated finite 2R contact map. For e=2,
the rank-three matrix theorem is complete; a coordinate-free factorization
through a natural rank-three space attached to the ruling fiber and
extension class remains a distinct explanatory question.

### H. Literature audit and novelty boundary

The following primary antecedents identify the established extension machinery and the limits of a novelty claim.

#### H.1 Bănică--Forster: extension theory is established machinery

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

#### H.2 Drézet: modern intrinsic parametrization

Jean-Marc Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, develops primitive curves of arbitrary multiplicity by gluing \(U_i\times\operatorname{Spec}\mathbf C[t]/(t^n)\) and nonabelian \(H^1\). His later survey and papers develop extension, deformation, and moduli theory further.

**LITERATURE-ESTABLISHED, NOT NEW.** Treating primitive multiple curves intrinsically via their canonical filtration and associated line bundle, rather than by ambient coordinates, is standard. Any eventual general theorem should be phrased compatibly with this literature rather than advertised as a new theory of primitive multiple curves.

Relevant sources:
- J.-M. Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, arXiv:math/0605726.
- J.-M. Drézet, *Primitive multiple schemes*, Eur. J. Math. 7 (2021), 985--1045, arXiv:2004.04921.
- J.-M. Drézet, *Primitive multiple curves: classification, deformations and moduli spaces of sheaves* (survey, 2013).

#### H.3 Rational-quartic STCI literature

The unrestricted characteristic-zero rational-quartic STCI problem remains open. The fixed-C0 all-quartic-carrier theorem has its full proof elsewhere. Relevant primary antecedents include:

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

#### H.4 Ropes/ribbons literature

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

#### H.5 Revised status of the framework

**PROVED + LITERATURE-ALIGNED.** The two-layer organization
\[
\text{existence/splitting of the multiple structure}
\quad+\quad
\text{rank of ambient containment maps}
\]
is the correct framework, but the first layer is Bănică--Forster/Drézet theory.

**PROJECT-SPECIFIC PROVED RESULT.** For the rational quartic and quartic carriers, the quadric comparison converts the ambient first-symbol problem into evaluation of \(O_Q(1,3)\) on \(R\), and the next primitive containment condition into a finite map on \(2R\). The e=2 fourth-extension locus forces \(R\) to be a ruling divisor and has exact ambient rank three.

**OPEN NOVELTY QUESTION.** Determine whether this \(R/2R\) ambient-carrier reduction, or an equivalent construction, already occurs in the older literature on contact of surfaces along curves (notably Gallarati), infinitesimal neighborhoods, or Rees/principal-parts methods. Search should continue before publication-level novelty claims.

### J. Exact e=1 primitive-triple obstruction

This section carries out the first revised target from Section G for the fixed quartic
\[
C_0=[s^4:s^3t:st^3:t^4].
\]

#### J.1 Setup

For \(e=1\),
\[
L=O(-6),\qquad M=O(-8),
\]
and every Ferrand double is specified in the fixed split conormal frame by
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
with projective basepoint-free condition
\[
\Delta=a_0b_1-a_1b_0\ne0.
\]

By Bănică--Forster Proposition 2.4, extension to a primitive triple is equivalent to splitting
\[
0\to L^2=O(-12)\to \nu_{C_2}|_C\to M=O(-8)\to0.
\]
The extension class lies in
\[
\operatorname{Ext}^1(M,L^2)=H^1(O(-4)).
\]

**LITERATURE STATUS.** The splitting criterion and obstruction group are standard Bănică--Forster theory. The explicit specialization below to the fixed embedded rational quartic and its quotient pencil was not found in the targeted literature search; it should presently be treated as a project calculation, not a publication-level novelty claim.

#### J.2 Moving-coordinate cocycle

Use the same exact embedded chart transition as in the audited e=2 computation, but now reverse the binary *linear* forms by
\[
A^\vee(w)=wA(1/w),\qquad B^\vee(w)=wB(1/w).
\]
For \(m=Bu-Av\), which has line type \(M=O(-8)\), the quadratic coefficient of the opposite-chart equation gives the Cech cocycle
\[
h_2=-\frac{2A+zB}{8z^5}
\left(12A^2+3z^2B^2+4z^2(A'B-AB')\right).
\]
The same formal expression appeared in the e=2 calculation; the different line type changes which Laurent coefficients survive in cohomology.

For \(H^1(O(-4))\), the basis classes are \(z^{-1},z^{-2},z^{-3}\). Up to a common nonzero scalar, the three obstruction coordinates are
\[
\boxed{
\begin{aligned}
c_1={}&-b_1(2a_0b_1+12a_1^2+16a_1b_0+9b_0^2),\\
c_2={}&-(2a_1+b_0)(8a_0b_1+12a_1^2+4a_1b_0+3b_0^2),\\
c_3={}&-2a_0(2a_0b_1+36a_1^2+16a_1b_0+3b_0^2).
\end{aligned}}
\]

**PROVED COMPUTATIONALLY/FORMALLY.** These are the exact Cech coordinates obtained from the moving-coordinate transition; no sampling is used.

#### J.3 Exact zero locus on the resultant-open quotient space

Localize at \(\Delta\) by adjoining \(t\Delta-1\). An exact Groebner calculation gives, among the localized consequences,
\[
a_0(2a_1+b_0)=b_1(2a_1+b_0)=0,
\]
\[
a_0(a_0b_1+2b_0^2)=b_1(a_0b_1+2b_0^2)=0,
\]
and
\[
a_0(3b_0^2t+2)=b_1(3b_0^2t+2)=0.
\]

Hence the resultant-open zero locus has the following exhaustive set-theoretic decomposition.

##### Main component

If \((a_0,b_1)\ne(0,0)\), then
\[
\boxed{b_0=-2a_1,\qquad a_0b_1=-8a_1^2.}
\]
Here
\[
\Delta=-6a_1^2\ne0,
\]
so \(a_1,a_0,b_1\) are all nonzero. Projectively this is a one-dimensional rational locus.

The quadric-comparison section is
\[
r=A+\frac z2B
=a_0+\frac{b_1}{2}z^2
=a_0-\frac{4a_1^2}{a_0}z^2.
\]
Thus its degree-two divisor \(R\) is a symmetric pair in the chosen affine coordinate. Whether this admits a coordinate-free incidence interpretation is OPEN.

##### Boundary directions

If \(a_0=b_1=0\), put \(r_0=b_0/a_1\). Basepoint-freeness says \(r_0\ne0\), and the remaining obstruction is
\[
(r_0+2)(3r_0^2+4r_0+12)=0.
\]
Thus there are three additional projective quotient directions over an algebraically closed characteristic-zero field:
\[
\boxed{r_0=-2,\quad 3r_0^2+4r_0+12=0.}
\]

At \(r_0=-2\), the comparison section \(A+\frac z2B\) vanishes identically. This is a genuinely exceptional configuration: the primitive conormal kernel \(M=O(-8)\) coincides with the quadric conormal subline \(O(-8)\subset N_C^*\). The divisor \(R\) formalism must therefore be treated separately there; one must not write a length-two \(R=Z(r)\).

At the two quadratic-root directions, the comparison section is a nonzero scalar multiple of \(z\) as an \(O(2)\)-section, so its homogeneous zero divisor consists of the two coordinate boundary points \(0,\infty\).

**PROVED.** The above main component plus three boundary points is the complete reduced/set-theoretic primitive-triple locus on \(\Delta\ne0\), subject to the exact transition conventions already audited for the fixed curve.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_triple\_obstruction.py}.
\]

#### J.4 Consequence for the jet-budget program

The e=1 extension-existence condition is therefore neither vacuous nor a generic three-independent-equation cut. It has a positive-dimensional exceptional component. This reinforces the revised framework:

\[
\text{BF splitting degeneracy}
\quad\text{first, then}\quad
\text{ambient quartic jet rank}.
\]

On the main component, \(R\) has length two and
\[
K_R=H^0(I_{R/Q}(1,3))
\]
has dimension six. The next concrete problem is to compute
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
along the one-dimensional main component and the two nonzero-comparison boundary directions. The \(r\equiv0\) boundary direction requires a separate formulation because the \(R/2R\) reduction degenerates.

#### J.5 Literature check specific to this calculation

A targeted search was made for explicit primitive-triple formulas for embedded rational quartics, Ferrand doubles extended to triples, and formulas for the Bănică--Forster splitting class. The sources located continue to use BF/Ferrand as the general mechanism; no explicit formula matching the three \(c_i\) above was found.

Ellia's primitive-STCI work uses numerical consequences of primitive multiple structures rather than this quotient-pencil splitting locus. Modern papers using quasi-primitive extensions likewise cite BF as the construction machinery. Therefore the safe current classification is:

- **standard:** Ferrand double construction, BF splitting criterion, obstruction group \(H^1(O(-4))\);
- **project-specific exact calculation:** the three displayed \(c_i\) and their resultant-open zero-locus decomposition;
- **unknown novelty:** whether an equivalent classification occurs in older specialized literature not indexed by the searches used here.

Before any external write-up, search citation chains around Bănică--Forster, Ferrand, and older work on multiple/contact structures rather than claiming the explicit locus is new.


### K. Exact e=1 quartic contact on the primitive-triple locus

The e=1 BF splitting locus from Section J can now be tested against the ambient quartic carrier map.

#### K.1 Full quartic-through-double source

The ambient quartic ideal of \(C_0\) has dimension 18. For a quotient
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
impose that the first normal symbol be \(h(B,-A)\), with \(h\in H^0(O(8))\). Exact linear algebra in the 35 quartic monomials gives, away from the exceptional comparison-zero direction below,
\[
h^0(I_{C_2}(4))=7.
\]
This agrees with the intrinsic decomposition
\[
6=\dim K_R,\qquad 7=6+\dim\langle Q^2\rangle.
\]

For a lift \(F\) with symbol \(h(B,-A)\), its restriction to the canonical primitive triple is the quadratic Taylor coefficient
\[
[F(A\epsilon,B\epsilon)]_{\epsilon^2}-h\gamma,
\]
where \(\gamma\) is the nonnegative-chart correction obtained from the BF quadratic cocycle.

#### K.2 Main one-dimensional triple component: no jet-rank defect

Parameterize the main component projectively by
\[
a_0=1,\qquad a_1=t,\qquad b_0=-2t,\qquad b_1=-8t^2.
\]
The resultant is
\[
\Delta=-6t^2,
\]
so every admissible point has \(t\ne0\).

The full second-order contact matrix has rank exactly five for every \(t\ne0\). A single covering \(5\times5\) minor is
\[
\boxed{-589824\,t^{16}},
\]
so there is no specialization gap on the component.

Therefore
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
at every point of the main e=1 primitive-triple family.

Equivalently, after quotienting the universal \(Q^2\) source direction against \(r^2\), the finite map
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
has maximal rank four. Thus
\[
\boxed{\delta_2^Q=0}
\]
uniformly on the main component.

**PROVED.** The e=2 carrier mechanism does not recur here: BF splitting imposes a special one-dimensional family of quotients, but it does not force a second ambient jet-rank defect.

#### K.3 Two nonzero-comparison isolated directions

At the two isolated directions
\[
a_0=b_1=0,\qquad
3(b_0/a_1)^2+4(b_0/a_1)+12=0,
\]
the quartic-through-double source has dimension seven and the full contact map again has rank five. Hence
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
there as well.

So every e=1 primitive triple with nonzero quadric-comparison section has exactly the expected two-dimensional quartic carrier space.

#### K.4 The comparison-zero point is qualitatively different

At the remaining isolated direction, scale to
\[
A=z,\qquad B=-2.
\]
Then
\[
A+\frac z2B=0.
\]
Hence the primitive conormal kernel \(M=O(-8)\) is exactly the quadric conormal subline
\[
O_C(-8)\subset N_C^*.
\]

The first-symbol source jumps:
\[
\boxed{h^0(I_{C_2}(4))=10}.
\]
The BF quadratic cocycle vanishes identically, so the canonical triple has no quadratic gluing correction in the fixed charts. Moreover the quadric equation has chart expression
\[
Q=u+\frac z2v,
\]
and under the triple parameterization
\[
u=z\epsilon,\qquad v=-2\epsilon
\]
it vanishes identically.

Therefore the canonical primitive triple is contained in the smooth quadric:
\[
\boxed{C_3\subset Q}.
\]

Consequently
\[
Q\cdot H^0(O_{\mathbf P^3}(2))
\subseteq H^0(I_{C_3}(4)).
\]
Both sides have dimension ten, so
\[
\boxed{
H^0(I_{C_3}(4))
=
Q\cdot H^0(O_{\mathbf P^3}(2)).
}
\]

**PROVED.** This exceptional e=1 triple has maximal carrier freedom only because the entire triple lies on the quadric; every quartic carrier factors by \(Q\).

For an STCI presentation with a quartic equation, this is immediately dangerous in exactly the same elementary projective sense as the e=2 cubic-times-linear factorization: a defining quartic \(QH_2\) carries the entire surface component \(Q=0\), and intersection with any positive-degree mate contains a curve on \(Q\), not merely the nonplanar quartic support. Thus this direction cannot supply a genuine quartic equation in an STCI pair supported exactly on \(C_0\).

#### K.5 Structural conclusion for e=1

The primitive e=1 locus exhibits two distinct mechanisms:

1. **nonzero comparison section:** BF splitting is exceptional, but ambient quartic contact is maximal rank and leaves exactly a two-dimensional quartic kernel;
2. **zero comparison section:** the primitive structure aligns with the quadric itself, the source jumps to dimension ten, and every quartic factors through \(Q\).

This strengthens the negative conclusion from the jet-budget framework. Rank defect is not the general source of carrier survival. For e=1, the generic primitive-triple survivor locus has **zero** ambient discrepancy:
\[
\delta_2^Q=0.
\]
The remaining two quartics must therefore be understood geometrically rather than eliminated by dimension count.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_quartic\_contact.py}.
\]

### L. Residual geometry as a separate question

On the nonzero-comparison e=1 triple locus the exact two-dimensional
quartic pencil above need not have a jet-rank defect. Whether its residual
geometry is a fixed factor, a fixed residual curve, a larger base locus,
or a genuine pencil is a question about the actual equations, separate
from the primitive extension and first two contact ranks. The
[complete e=1 rebuild](OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-e1-jet-rebuild)
repairs the invalid fixed-ruling-line shortcut. The all-quartic mate
problem is already closed by the [full carrier proof](../synthesis/quartic_carrier_proof.md);
these structural questions do not reopen that theorem.

---

<a id="2026-10-06-primitive-quadruple-universal"></a>

## Universal degree-two primitive fourth structures

Status: exact universal classification and carrier theorem, verified over
characteristic zero. The result excludes the degree-two direction branches
of hypothetical `(4,7)` and `(4,8)` complete intersections on the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`. It does not settle STCI for `C0`, other rational
quartics, arbitrary curves, or positive characteristic.

The computation corrects the plausible universal exclusion suggested by
the samples in `2026-10-05-uniform-multiplicity.md`: primitive quadruples of
conormal quotient type `O(-5)` **do exist**. Their quotient directions form
a resultant-open subset of a linear projective three-space. The obstruction
to the indicated complete intersections is instead that every ambient
quartic containing their canonical primitive triple factors as a cubic
times a linear form.

### Formal coordinates and complete parameter coverage

Use the first ambient chart

\[
z=x_1/x_0,\quad v=x_2/x_0-z^3,\quad
u=x_3/x_0-z^4-\tfrac32zv.
\]

The opposite moving coordinate is

\[
W=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]

and its split normal coordinates are

\[
u'=\tfrac12\left(\frac z{z^4+u+\tfrac32zv}-W^3\right),\quad
v'=-\frac{3zW}{z^4+u+\tfrac32zv}+W^4+
\frac2{z^4+u+\tfrac32zv}.
\]

To first order both normal coordinates transition by `z^-7`. Specify
the quotient `O(-7)^2 -> L=O(-5)` by

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2,
\quad u\mapsto A\ell,\quad v\mapsto B\ell.
\]

These are homogeneous binary quadratics, even when an affine leading
coefficient vanishes. Their projective resultant is

\[
\Delta=a_0^2b_2^2-a_0a_1b_1b_2-2a_0a_2b_0b_2+
a_0a_2b_1^2+a_1^2b_0b_2-a_1a_2b_0b_1+a_2^2b_0^2.
\]

The sole parameter restriction is `Delta != 0`. The matrix sending
degree-at-most-one Bezout coefficients `(S0,S1,T0,T1)` to the coefficients
of `(S0+S1 z)A+(T0+T1 z)B` is

\[
\begin{pmatrix}
a_0&0&b_0&0\\a_1&a_0&b_1&b_0\\
a_2&a_1&b_2&b_1\\0&a_2&0&b_2
\end{pmatrix}.
\]

Its determinant is `Delta`, including affine degree drops. Thus the
Bezout gauges exist uniquely over the entire resultant-open set; no
additional leading-coefficient charts, generic-pencil normalization, or
unexamined boundary directions enter the computation. Reversing the
coefficient vectors gives the opposite-chart gauges, with the same
determinant. We do not use arbitrary changes of the split frame or base
coordinate to normalize quotient directions: those would require changing
the full nonlinear transition.

Set `m=Bu-Av`, whose line type is `M=O(-9)`. Then

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6).
\]

Because both cohomology groups of `O(-1)` vanish, each direction has a
unique embedded primitive triple. A zero fourth obstruction also produces
a unique primitive quadruple, since `H0(O(-6))=0`.

### Exact fourth obstruction and its entire zero locus

For `d=A'B-AB'`, the quadratic cocycle is

\[
h_2=-\frac{2A+zB}{8z^5}\left(12A^2+3z^2B^2+4z^2d\right).
\]

Write `gammaU` for its nonnegative Laurent part and put
`gammaV=(-z*(h2-gammaU))|_(z=1/w)`. The canonical triple has
`m+gammaU ell^2=0` on the first chart and
`m'+gammaV(W) ell'^2=0` on the second. Polynomial Bezout coefficients
`SA+TB=1` give its first-chart parameterization

\[
u=A\ell-T\gamma_U\ell^2,\qquad
v=B\ell+S\gamma_U\ell^2.
\]

All coefficient functions in the opposite equation are evaluated at the
moving coordinate `W` **before truncating**. The cubic coefficient of that
equation, multiplied by `z^9`, gives a Laurent cocycle `h3`; its
coefficients of `z^-1,...,z^-5` represent `H1(O(-6))`.

The universal exact result is

\[
(c_1,\ldots,c_5)=(G_1,\ldots,G_5)/\Delta,
\]

where each `Gi` is a homogeneous degree-eight polynomial. Their complete
expanded values, not a numerical fit, are preserved in
`research/scratch/primitive47universal/equations.json`. If `I=(G1,...,G5)`
and `K=(2a1+b0,2a2+b1)`, the verified exact certificates are

\[
I\subseteq K,\qquad
\Delta^3(2a_1+b_0)^3\in I,\qquad
\Delta^3(2a_2+b_1)^3\in I.
\]

Consequently, on `Delta != 0`, all five coordinates vanish **if and only if**

\[
\boxed{b_0=-2a_1,\qquad b_1=-2a_2.}
\]

This is a set-theoretic classification; the powers in the membership
certificates are not a claim that the obstruction scheme is reduced.
Its projectivized parameter space is an open subset of a linear `P3`.
The restricted resultant is

\[
\Delta_0=a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, `(a0,b2)` cannot both vanish. Equivalently, the fourth-zero
directions satisfy

\[
2A+zB=q_0=2a_0+b_2z^3.
\]

For example `A=z^2+1, B=-2z` has
`h2=-4/z-8/z^3-3/z^5`, `gammaU=0`,
`gammaV=4+8w^2+3w^4`, and all five fourth coordinates zero. The prior
nonzero sampled direction `A=z^2,B=1` lies outside this locus.

### Every quartic carrier is a cubic multiple, on all charts

Use ambient coordinates `[x:y:Z:W]`, and define

\[
Q=xW-yZ,
\]

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
+a_0^2(x^2Z-y^3)+a_0b_2(xZ^2-y^2W)
-\frac{b_2^2}{4}(yW^2-Z^3).
}
\]

This cubic is in the ideal of `C0`; its first normal symbol is
`-q0(B,-A)/2`. It contains the canonical primitive triple and quadruple.
The universal verifier checks the latter directly through third order in
`ell`, using the unique gluing correction for the quadruple.

The first-symbol image of ambient quartics in `I(C0)` has dimension 17,
with kernel `kQ^2`; its three missing linear combinations are
`Qnormal_2=P_1/2`, `Qnormal_5=P_4/2`, `Qnormal_8=P_7/2`.
For direction `(B,-A)` on the fourth-zero locus, an admissible symbol is
`h(B,-A)`, with

\[
h\in\langle1,z,z^3,z^4,z^6,z^7\rangle.
\]

Thus its quartic lift has seven coefficients, the six coefficients of
`h` and the coefficient `k` of `Q^2`. Restricting these lifts to the
canonical triple gives the following seven-by-seven matrix, with columns
ordered `(h0,h1,h3,h4,h6,h7,k)` and rows ordered by the coefficient of
`z^0,...,z^6` in the quadratic normal jet:

\[
\begin{pmatrix}
a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&0&0&0&a_0^2\\
-a_0b_2^2/4&0&a_0^2b_2/2&0&-a_0^3&0&0\\
0&a_0b_2^2/4&0&-a_0^2b_2/2&0&a_0^3&0\\
a_2b_2^2/2&-a_1b_2^2/2&-a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&2a_0^2a_1&a_0b_2\\
-b_2^3/8&0&a_0b_2^2/4&0&-a_0^2b_2/2&0&0\\
0&b_2^3/8&0&-a_0b_2^2/4&0&a_0^2b_2/2&0\\
0&0&0&-a_1b_2^2/2&-a_0a_2b_2&a_0a_1b_2&b_2^2/4
\end{pmatrix}.
\]

Its minor in zero-based rows `(0,1,2)` and columns `(4,5,6)` is
`-a0^8`; that in rows `(4,5,6)` and columns `(0,1,6)` is
`-b2^8/256`. Because `Delta0 != 0` implies `(a0,b2) != (0,0)`, these
two minors cover every admissible direction and prove rank at least three.
The four independent quartics `xT,yT,ZT,WT` lie in the kernel. The cubic
is never zero: its `y^3` coefficient is `-a0^2`, and its `Z^3`
coefficient is `b2^2/4`. Hence these multiples are linearly independent,
proving rank exactly three on the full resultant-open locus.

For the primitive triple `Y3` and quadruple `Y4`, this proves

\[
\boxed{
H^0(\mathcal I_{Y_3}(4))=
H^0(\mathcal I_{Y_4}(4))=
T\,H^0(O_{\mathbf P^3}(1)).
}
\]

An equivalent compact solution of the matrix is

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4),\qquad
k=2a_1b_2c_1+4a_0a_2c_3.
\]

The coincidence between the fourth-zero locus and the rank-two exceptional
quartic first-symbol direction locus is independently obtained in the
local-cohomology direction investigation. It explains why a generic
first-symbol rank count would miss this family.

### Consequence for hypothetical complete intersections

For a quasiprimitive complete intersection `(4,b)` supported on `C0`,
the checked filtration duality in `2026-10-05-uniform-multiplicity.md`
gives, when `L=O(-5)`, top defect degree `b-7`. At `b=7` the entire
structure is primitive. At `b=8`, superadditivity and complementary
divisor duality force `D2=D3=0`, so its canonical fourth structure is
primitive. Thus either branch requires a direction in the classified
fourth-zero locus and its defining quartic must contain `Y3`.

The carrier theorem forces `F4=T*H` with `H` a nonzero linear form.
For any homogeneous mate `Gb` of positive degree, `V(H,Gb)` is a
projective plane curve or the whole plane. It is contained in
`V(F4,Gb)`, and it cannot be contained in the nonplanar integral curve
`C0`. Therefore `V(F4,Gb)` cannot have support exactly `C0`.

This excludes the **e=2 branches** of `(4,7)` and `(4,8)` on `C0`.
The same argument excludes any `(4,b)` whose e=2 canonical quadruple is
primitive. It does not exclude e=0 or e=1 at these degrees, nor e=2
structures with a defect before the fourth layer, nor carriers of higher
degrees. The cubic `T` can be singular at the zeros of `q0`; its existence
does not furnish a smooth supporting surface or an STCI construction.

### Reproduction and continuation evidence

One repository-local command verifies the full calculation, including
exact ideal membership and all-chart rank minors:

```sh
python research/computations/verify_primitive_quadruple_universal.py
```

It requires SymPy and Macaulay2's `M2`; the recorded verification used Macaulay2 1.26.06. It regenerates its
inspectable scratch equations, derives all jets with sparse polynomial
arithmetic, checks ten directions against the original independent
rational-series implementation, verifies the universal cubic restrictions,
and runs exact Macaulay2 certificates. The ten sample comparisons are
cross-checks; the global conclusions come from the polynomial identities,
resultant-localized membership certificates, and covering minors.

The durable files are `verify_primitive_quadruple_universal.py`,
`scratch/primitive47universal/{generate.py,equations.json,classify.m2}`,
and `scratch/primitive47universal/{quartic_contact.py,quartic_contact.json,
quartic_contact.m2}`. The independent theoretical reconstruction is in
`2026-10-05-primitive-carrier-theory.md`; the frontier-audit lane is
checking the quadratic cocycle and contact matrix by a separate
Bezout-independent computation.

A tempting fifth-order exclusion also fails for the sample
`A=z^2+1,B=-2z`: its fifth obstruction is zero, as recorded with exact
Laurent coefficients in the theory note. The productive next question is
therefore the uniform ambient compatibility of an e=2 primitive triple,
and then the remaining case `deg D2=1`; increasing sampled primitive
orders does not address the ambient quartic factor obstruction.


---

<a id="2026-10-06-primitive-triple-parity"></a>

## A parity slice and its fourth-layer defect obstruction

Status: exact characteristic-zero classification of the entire parity
slice; necessary extension argument checked conceptually by the frontier
audit lane. The statement concerns the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, a hypothetical complete intersection with a
quartic carrier, degree-two first quotient, and **D2=0**. The conclusion is
an all-mate-degree exclusion for this parity slice. It does not exclude
arbitrary degree-two directions or the case `deg D2=1`.

### Exhaustive one-parameter family

Consider the basepoint-free quotient direction

\[
A=a_0+a_2z^2,\qquad B=b_1z.
\]

Projective coprimality forces `a0*a2*b1 != 0`. The actual ambient
automorphism

\[
[x_0:x_1:x_2:x_3]\longmapsto
[x_0:c x_1:c^3x_2:c^4x_3]
\]

preserves `C0` and sends the exact split coordinates `(z,u,v)` to
`(cz,c^4u,c^3v)`. Choose `c^2=a2/a0` and rescale the quotient. This
gives the complete normal form

\[
\boxed{A=1+z^2,\qquad B=\beta z,\qquad \beta\ne0,}
\]

where `beta=b1/a2`. This normalization uses an embedded automorphism and
transports the full jets; it is not an arbitrary normal-frame or pencil
change. Its homogeneous resultant is `beta^2`.

### Exact quartic compatibility of the canonical primitive triple

Because `Hom(M,L^2)=O(-1)`, every degree-two direction has its unique
primitive triple `Y3`. A quartic containing `Y3` must have first symbol
`h(B,-A)`, with `h` a binary form of degree seven, and may have the extra
`Q^2` coefficient, where `Q=x0*x3-x1*x2`. These nine coefficients obey
three ambient first-symbol image constraints and seven actual quadratic
contact equations.

The universal derivation in
`scratch/primitive47universal/general_triple_contact.py` reconstructs the
symbol image from all 35 quartic monomials, chooses a constant rational
right inverse to its 34-dimensional combined restriction/symbol image,
and computes the contact coefficient

\[
f_2-h\gamma_U,
\]

where `f2` is the ordinary quadratic Taylor coefficient and `gammaU`
is the nonnegative Laurent part of the canonical triple cocycle. This
formula does not require a Bezout choice. Three higher polynomial
coefficients are exact multiples of one first-symbol constraint, so the
ten equations are exhaustive.

On the displayed parity family, the resulting matrix is ten by nine.
The exact greatest common divisor of its ten maximal minors, normalized
to be monic, is

\[
\boxed{(\beta-6)(\beta+2)^9(\beta+6)^2.}
\]

Thus the triple has an ambient quartic carrier **if and only if**

\[
\boxed{\beta=-2,\quad -6,\quad\text{or }6.}
\]

At `beta=-2` the matrix rank is five, and the four-dimensional carrier
space is cubic times linear forms, exactly as proved in
`2026-10-06-primitive-quadruple-universal.md`. At `beta=+-6` the rank is
eight and the carrier is unique up to scalar. In ambient coordinates
`[x:y:Z:W]`, convenient forms are

\[
F_+=6xWy^2-x^2yZ-4x^2Z^2+y^4-2y^3Z,
\]

\[
F_-=8xW^3+6xWyZ+12xWZ^2+x^2Z^2-y^3Z
       -6y^2Z^2-12yZ^3-8Z^4.
\]

The normalizations in the exact coefficient certificate are `F+` and
`-F-/6`, respectively. No claim of geometric irreducibility is needed.
A separate Jacobian check found affine singular-ideal dimension two and
degree three for each; these are not covered by an isolated-singularity
normal-quartic argument.

### A necessary condition for introducing the fourth-layer defect

Let `Y3` be the primitive triple associated to a degree-two quotient, and
put `L=O(-5)` and `M=O(-9)`. Its ideal is locally generated by

\[
f=m+\gamma\ell^2,\qquad \ell^3.
\]

Consequently the rank-two bundle

\[
\mathcal V=\mathcal I_{Y_3}/
                 (\mathcal I_C\mathcal I_{Y_3})
\]

fits in an exact sequence

\[
0\longrightarrow L^3\longrightarrow\mathcal V
\longrightarrow M\longrightarrow0.
\]

Its extension class is the ordinary primitive-fourth obstruction
`h3 in H1(Hom(M,L^3))=H1(O(-6))`: the off-diagonal term of the transition
between the two ideal generators is precisely the cubic moving-coordinate
coefficient used in the universal fourth verifier.

Suppose a saturated quasiprimitive fourth layer `Y4` extends `Y3`, with

\[
E_3=\mathcal I_{Y_3}/\mathcal I_{Y_4}=L^3(D_3).
\]

The support ideal `I_C` annihilates `E3`: it does so generically, and
`E3` is torsion free on `C`. Hence the quotient map gives
`V -> E3`. Its restriction to `L^3` is the canonical multiplication
section with zero divisor `D3`. Applying `Hom(-,E3)` to the exact sequence
above shows the necessary condition

\[
\boxed{
h_3\longmapsto0\quad\text{in}\quad
H^1(O(-6+D_3)).
}
\]

This is a necessary condition, not a sufficiency or classification claim
for defective extensions. Equivalently, some nonzero binary form of degree
`deg D3` must annihilate the class under multiplication. Higher terms
`ell*f` and `ell^4` cannot alter this condition, because their images in
`E3` vanish.

For a quartic-carrier complete intersection with degree-two first quotient,
the checked all-degree filtration calculation in
`2026-10-05-uniform-multiplicity.md` gives, with `s=mate_degree-1`,

\[
\deg D_s=s-6.
\]

Write `s=3q+r`, `0<=r<=2`. Superadditivity implies
`q deg D3 <= 3q+r-6 < 3q`, and hence

\[
\boxed{\deg D_3\le2.}
\]

This bound uses the complete-intersection adjunction and divisor duality;
it is not a bound for arbitrary standalone multiple curves.

### The two remaining parity carriers cannot support the bounded defect

The exact fourth-obstruction coordinates, ordered by
`z^-1,...,z^-5`, are

\[
c_+=( -128,0,160,0,-192),\qquad
c_-=(64,0,-8,0,0).
\]

Multiplication by an arbitrary binary quadratic has, in these coordinates,
the matrix

\[
H(c)=\begin{pmatrix}
c_1&c_2&c_3\\c_2&c_3&c_4\\c_3&c_4&c_5
\end{pmatrix}
:H^0(O(2))\longrightarrow H^1(O(-4)).
\]

This follows directly by multiplying a Laurent representative by
`sigma0+sigma1*z+sigma2*z^2` and keeping the three surviving terms
`z^-1,z^-2,z^-3`. The determinants are

\[
\det H(c_+)=-163840,\qquad \det H(c_-)=512.
\]

Thus neither class has a nonzero quadratic annihilator. A degree-zero or
degree-one annihilator would produce a quadratic annihilator by further
multiplication, so these are excluded as well. Neither unique quartic
triple carrier can be part of a hypothetical complete intersection with
`deg D3<=2`. The `beta=-2` carrier has already been excluded by its linear
factor. Every other parameter admits no quartic containing its primitive
triple. Therefore the entire basepoint-free parity family with `D2=0`
is excluded for **every mate degree**.

### Reproduction and remaining open computation

The exact companion is

```sh
python research/computations/verify_primitive_triple_parity.py
```

It regenerates the arbitrary-direction quartic contact matrix, uses
polynomial-domain determinants over `QQ[beta]` for all ten maximal minors,
checks their gcd and the three exceptional ranks, reconstructs the two
unique quartics, checks their classes against the original rational-series
fourth-obstruction implementation, and verifies both Hankel determinants.
Its full certificate is
`scratch/primitive47universal/parity_triple_certificate.json`.

The all-direction primitive-triple contact matrix is saved in
`general_triple_contact.json`. Attempts to compute the whole six-parameter
rank-drop ideal by generic Macaulay2 maximal minors and saturation were
stopped after remaining slow. A normalized nonexceptional chart and a
finite-field version also did not complete. Those attempts establish no
global classification. An exact one-chart Dynamic determinant calculation
completed but produced large expanded minors; it did not settle the
saturated ideal. The files `general_triple_contact.m2`,
`triple_contact_p_chart.m2`, and `triple_contact_p_factors.m2` preserve the
attempts. No unfinished CAS jobs remain from this lane.

The strongest continuation target is the arbitrary-direction rank-drop
locus of the ten-by-nine matrix, followed by the quadratic-annihilator
incidence condition for its fourth obstruction. The separate case
`deg D2=1` needs a defective-triple gluing state; a primitive-triple
calculation cannot silently be applied to it.


---
