# higher initial ideals and embedded thickenings

## Integration guide: cancellations and higher embedded data

The [higher-initial investigation](#2026-10-21-higher-initial-ideals-valuations) records how cancellations between leading normal forms create higher initial generators; the explicit examples must be retained because they rule out replacing the full initial ideal with just the first symbols. The [embedded ribbon/triple obstruction](#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction) concerns a different global extension and gluing problem, with its own Čech and coordinate-invariance hypotheses.

Compare the [full ideal-filtration diagram](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd), the [valuation length counterexample](../synthesis/coefficient_valuations.md), and the [boundary equation-module test](BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md#2026-10-27-one-step-boundary-obstruction). The common obstruction to an overly simple approach is loss of higher-order or gluing information, **not** a theorem that any given local thickening fails globally.

The original coprime theorem, examples, and unreviewed status remain intact below.

---


Complete mathematical arguments and exploratory boundaries preserved. Conditional conclusions remain conditional; computational and geometric obstructions are not asserted beyond their original hypotheses.

---

## 2026-10-21-higher-initial-ideals-valuations

# Higher initial ideals and transverse valuations — research note (2026-10-21)

Status: PROPOSAL; no independent review. Branch only.

## Setup
Let I be the homogeneous ideal of C0 in S and J=(F,G). The global gr_I(S)=⊕ I^n/I^{n+1} has two gradings: homogeneous polynomial degree and filtration degree. Its sheafification along C0 is Sym(I_C/I_C²), but global sections of the latter need not be obtained from individual global graded pieces without saturation. At η_C, completion gives K[[x,y]] with K=k(C0), and gr_m=K[X,Y]. The full initial ideal in_m(JR) includes leading forms of every combination AF+BG; it is generally larger than (in F,in G). Generic localization can lose special-point torsion/degeneration.

## Coprime theorem
If in(F)=F_r and in(G)=G_s are relatively prime, they are a homogeneous regular sequence; the filtered Koszul argument gives gr(R/J)=K[X,Y]/(F_r,G_s), and length(R/J)=rs. In an STCI with no residual components, Bézout gives de=4 length(R/J), hence de=4rs in this case.

## Explicit cancellation examples
(1,1): F=x, G=x+y^n, n>=2. The full initial ideal is (X,Y^n), length n, whereas the individual initials generate only (X).
(2,2): F=x², G=x²+y³. Cancellation gives J=(x²,y³), initial ideal (X²,Y³), length 6, rather than 4.
(2,3): F=x², G=x³+y^5. Cancellation by xF gives J=(x²,y^5), initial ideal (X²,Y^5), length 10 rather than 6.
These are local transverse models, not global STCI constructions.

## Quartic benchmark, local chart x0=1
Put t=x1, u=x2-t³, v=x3-t⁴. Then C is u=v=0. For F=x1⁴-x0³x3, G=x2⁴-x0 x3³:
F=-v.
G=(t³+u)^4-(t⁴+v)^3.
Modulo F, G reduces to (t³+u)^4-t¹².
At generic t ≠0, characteristic 0: initial G modulo F is 4t^9 u, so J=(v,u) and length 1. Characteristic 2: (t³+u)^4-t¹²=u⁴, so J=(v,u⁴), full initial ideal (V,U⁴), length 4. The individual initial forms in characteristic 2 are F_1=-V and G_1=-t^8 V (since (t⁴+v)^3 has linear term t⁸v), so cancellation is essential. In characteristic zero, G_1=4t⁹U-3t⁸V, and initial forms are coprime. Over algebraic closure of K in characteristic zero the transverse scheme is generically reduced of length one at C; other components of the (4,4) intersection must occur elsewhere, so the pair is not STCI in characteristic zero. In characteristic two it is a length-four curvilinear thickening along C at the generic point. Global radical equality requires separate projective chart/boundary verification.

## Valuations
The m-adic order is total transverse degree and is not a valuation on K itself. For each closed p in C, ord_p on K gives a discrete base valuation. Weight vectors (w_x,w_y)>0 give monomial valuations on K(x,y) with trivial base valuation; after choosing p, Gauss-type extensions v(Σ a_ij x^i y^j)=min(ord_p(a_ij)+i w_x+j w_y) give base-sensitive information, subject to coordinate choice and suitable completion. Composite lexicographic valuations retain transverse order and then coefficient order. Newton polygons/infinitely near points resolve common tangent factors and distinguish transverse branches; a single m-adic initial ideal generally does not encode their Puiseux exponents. Weighted initial ideals of the full ideal, not just two generators, are required. Rees valuations of J describe normalized blowup data but need not recover all infinitely near branches.

## Globalization and limitations
The degree-d normal symbol of F of I-order r is a section of Sym^r(N_C^∨)⊗O_C(d), which for the characteristic-zero balanced splitting is O_{P¹}(4d-7r)^{⊕(r+1)} (O_C(1)=O_{P¹}(4)). Thus a nonzero symbol requires 4d-7r>=0; similarly 4e-7s>=0. This is a necessary degree constraint, not a new STCI exclusion. The local (x,y) coordinates are only rational frames of the conormal bundle: rational cancellation coefficients generally have poles at closed points and do not produce ambient global polynomial combinations. Clear denominators only after tracking the induced twists and possible extra zero divisors. In characteristic two do not use the characteristic-zero normal-bundle splitting.

Related notes: [residual-cycle and wedge distinctions](../synthesis/residual_contact_cycles.md#wedge-degeneracy-distinguishes-neither-thickness-nor-residual-contact); [special-fiber length and standard bases](../synthesis/valuations_and_residual_contact.md#valuative-standard-bases-and-special-length-jumps); [orders, Hilbert filtration, and duality](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-equality-orders-filtration-dualitymd).

## Conormal splitting and quartic family references

- [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md): audited characteristic-dependent conormal splitting; the balanced formula above applies when the characteristic is not two.
- [STCI-R-0021](../results/quartic_mu4_degeneration.md): audited global behavior of the prescribed quartic pair, including its four characteristic-zero components and characteristic-two support.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md): conditional normal-flatness and first-relation-defect results; neither applies to arbitrary full initial ideals without its hypotheses.

## Priorities
1. Compute a standard basis of the actual generic ideal for arbitrary candidate F,G and retain each cancellation certificate.
2. Track denominators of certificates at closed points and formulate sheaf-valued graded relations with saturation.
3. Compare base-sensitive weighted valuations at each exceptional point with global degree constraints.
4. Seek a numerical exclusion for nonsaturated relations and both orders >=2; no such exclusion is proved here.

This note does not claim the generic local data determine global radical equality or that the example proves a characteristic-zero impossibility theorem.


---

## 2026-10-21-intrinsic-embedded-ribbon-triple-obstruction

# The embedded ribbon-to-triple obstruction

The characteristic-free ideal-sheaf construction fixes the embedded
ribbon and its conormal quotient. The [October 21 audit](#independent-audit-and-arithmetic-provenance)
independently reconstructed this correction of the difference-of-lifts
argument. The quartic Laurent coefficients come from the separate
[arithmetic calculation](#quartic-consistency).

## The canonical embedded extension

Let `i:C -> X` be a regular immersion of codimension two of schemes, with ideal `I`, and `E=I/I²`. Fix a surjective homomorphism of locally free sheaves `q:E -> L` with `L` invertible and kernel `M` invertible. Put `J₂=ker(I -> E -> L)`, and define the **canonical ideal** `K=I J₂+I³` (indeed `I³ ⊂ I J₂`).

There is a canonical exact sequence of **O_C-modules**
```
0 -> L^⊗2 -> J₂/K -> M -> 0.                    (*)
```
The sheaf of embedded ideals `J₃` satisfying `I³ ⊂ J₃ ⊂ J₂`, with local primitive-triple normal form `(x-a y²,I³)` for generators adapted to `q`, is canonically identified with the sheaf of O_C-linear splittings of (*). It is a locally nonempty torsor under `H=Hom_O_C(M,L²)`. Its class is exactly the Yoneda extension class
```
o_X(q) = [J₂/K] ∈ Ext¹_O_C(M,L²) = H¹(C,H).
```
It vanishes exactly when a global embedded primitive triple exists. If one exists, the set of global embedded triples is a torsor under `H⁰(C,H)`.

This holds in arbitrary characteristic, including mixed-characteristic DVRs; smoothness over a DVR is sufficient but not required beyond the stated regular immersion and locally free quotient. The claim is about embedded ideals in the fixed X and the fixed quotient q, not about abstract multiple curves.

## Independent proof

1. Regular immersion gives `I²/I³ ≅ Sym²(E)`. Since `J₂` is the inverse image of `M`, `I² ⊂ J₂`, and the image of `I J₂` in `I²/I³` is precisely the image `ME` of `M ⊗ E -> Sym²(E)`. Consequently
```
(I²+K)/K = I²/(I J₂+I³) ≅ Sym²(E)/(ME) ≅ Sym²(L)=L².
```
The last isomorphism is canonical for a line quotient, with no need to invert 2. The quotient `J₂/I²=M`. These identify the kernel and cokernel of (*).

2. Since `I J₂ ⊂ K`, multiplication by `I` kills `J₂/K`. Thus (*) is genuinely an exact sequence of O_C-modules, not a spurious O_C-module structure on `I/I³`. This repairs the central gap in the earlier proof.

3. For any admissible `J₃`, `I J₃ ⊂ J₃`, `I³ ⊂ J₃`, and the local normal form implies that the image of `J₃` in `E` is `M` and its intersection with `I²` modulo `I³` is `ME`. Therefore `K ⊂ J₃` and `J₃/K -> M` is an isomorphism: its inverse is a splitting of (*).

4. Conversely, a splitting `s:M -> J₂/K` has image an O_C-submodule. Its inverse image `J₃` in `J₂` is an O_X-ideal because the action modulo `K` factors through `O_C`. It contains `K` and hence `I³`, and maps onto `M` with quadratic intersection `ME`. Locally choose adapted generators `x,y` of `I`, with `x` mapping to a frame of `M` in `E` and `y` to a frame of `L`. The splitting is generated modulo `K` by `w=x-a y²` for some local coefficient `a`. Since `J₂=(x,y²)=(w,y²)`, the product `I J₂` lies in `(w,I³)`. Thus `J₃=(w,K)=(w,I³)=(w,y³)`, using `I=(w,y)` in the last equality. The quotient has graded pieces `O_C,L,L²` by the linear image `M` and quadratic intersection `ME`. This construction uses no division.

5. Splittings of an exact sequence with locally free quotient M exist locally. The difference of two splittings is a unique O_C-linear map M -> L². This action is free, transitive, additive and restriction-compatible. The construction uses only intrinsic ideals and module operations.

6. On a trivializing cover choose splittings s_i and set h_ij=s_j-s_i. Then h_ij+h_jk=h_ik. Replacing s_i by s_i+t_i adds the Čech coboundary t_j-t_i. Vanishing means the splittings can be adjusted to agree and glue, and inverse images in J₂ give a global *embedded ideal*. Conversely a global ideal yields a global splitting. Standard sheaf Ext gives Ext¹(M,L²)=H¹(Hom(M,L²)) because M is locally free. There is no nonabelian obstruction at this fixed embedded stage.

## Arbitrary adapted coordinate transformations

Locally choose generators x,y of I with q(x)=0 and q(y) a frame of L. Any other adapted generators, modulo I³, have the form
```
x' = α x + A x² + B xy + C y²,
y' = β x + δ y + D x² + E xy + F y²,
```
where α and δ restrict to units on C; coefficients may be ambient functions, including dependence on moving base coordinates. Terms from nilpotent variations of these coefficients are already included in their quadratic jets. In the quotient by `(x-a y²,I³)`, x=a y², y'=δ y + O(y²), and x'=(α a+C)y². Hence
```
a' = (α a+C)/δ²
```
with all coefficients restricted to C (and the appropriate local frames). For two choices a,b in the *same original frame*,
```
a' - b' = (α/δ²)(a-b).
```
This is exactly the transition for Hom(M,L²): x' has M-frame αx, y' has L-frame δy. The affine translation C/δ² may depend on the full quadratic neighborhood and base-coordinate movement; it cancels in differences. Arbitrary linear mixing β, all x²/xy terms, and quadratic corrections to y' do not change this result. No chosen retraction of the quadratic neighborhood is used. Equality is equality of ideals, not of preferred generators.

## Functoriality, base change and dependence

Isomorphisms of the data `(X,C,q)` carry `I,J₂,K` and (*) to their counterparts. Under flat ambient base change, the defining ideals, conormal quotient and (*) pull back to the corresponding geometric construction, and so does the Yoneda class. For nonflat ambient base change, the pullback of (*) as a module sequence on the new curve remains exact because `M` is locally free. Identifying that sequence with the new geometric extension still requires a compatible regular immersion and conormal quotient, with the relevant ideal, product and graded identifications commuting with pullback. When these identifications hold, the Yoneda class pulls back naturally. An isomorphism on cohomology under base change is a separate question.

The class is determined by the embedded quadratic neighborhood `O_X/I³` and `q`, since that truncation determines `J₂/K`. The associated graded algebra `Sym(E)` and the abstract ribbon can lose this information.

## Quartic consistency

For the specified relative rational quartic and distinguished quotient `L=O(-6), M=O(-8)`,
```
H = M^∨ ⊗ L² = O(-4).
```
On the two standard affine charts, H¹(O(-4)) has Laurent representatives u^-1,u^-2,u^-3. The earlier independently audited raw ambient calculation yields the transition defect `K(u)` and for the distinguished quotient `[-6u^-2]`. Each local kernel equation defines a splitting of (*), and their normalized differences give its Čech cocycle. The general theorem identifies this inherited cocycle with the Yoneda extension class. For the specified admissible quotients over Z_(2) and Z_2, the middle coefficient is 2 mod 4. [Full Čech reduction](Z4_LIFTING_AND_DEFORMATION.md#full-cech-reduction), [coefficient verifiers and arithmetic scope](Z4_LIFTING_AND_DEFORMATION.md#exact-computational-support-and-scope).

## Why the common comparison object matters

The statement that one can subtract arbitrary lifts of M *inside I/I³* as O_C-linear maps is not justified: I/I³ has no canonical O_C-module structure. Also the expression I²/(I³+IJ) is circular unless J is fixed and it does not by itself define a common comparison object for varying J. The common object is instead **J₂/(I J₂+I³)**. It is annihilated by I, so the difference construction and its additive law are literal O_C-module statements. The original numerical calculation survives; the original general proof contains the gap described above.

## Independent audit and arithmetic provenance

The October 21 independent reviewer gave **verdict B** after replacing
the difference-of-lifts argument by (*). The audit read the original
proposal, the literature report and the five October 20 lifting
reports. It reconstructed the general fixed-ambient, fixed-quotient
torsor, descent and coordinate invariance by ideal and module operations.
It inherited the Laurent coefficient, sign conventions and mod-four
reduction from the earlier quartic audits. Those calculations have the
arithmetic scope stated above. The audit’s handoff permits using the
corrected class with the fixed-quotient and base-change hypotheses.
Identification with a divided-Frobenius operation remains open.
[Original independent audit](https://github.com/markluxton1/STCI/blob/a5ed68f7f11d3b51e5e972a9a4b90e0a3bd7ce5b/research/notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md).

## A coordinate change as an explicit control

The complete quadratic transition, including movement of the base coordinate, yields for the distinguished relative-quartic quotient the contributions K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, and total K=-6u^-2. Under A'=A+B, B'=B the first contributions become K_A'=18u^-2+9u^-1 and K_B'=-12u^-2-9u^-1; the base term stays unchanged. Only the total represents the intrinsic class. These are the inherited exact chart calculations from [the arithmetic lifting proof](Z4_LIFTING_AND_DEFORMATION.md), with the failure of individual-summand invariance isolated in [the coordinate control](Z4_INTRINSIC_ARITHMETIC_MECHANISM.md#a-coordinate-summand-really-changes). The corrected extension proof explains the invariance; it does not independently recompute these Laurent coefficients.

## Relation to arithmetic operations

No identification of this Yoneda class with a divided-Frobenius or cotangent-complex operation has been established. Such a comparison requires a morphism of the relevant embedded deformation complexes and proof that it takes the actual extension class to the proposed operation. The existence of a formal arithmetic operation alone does not establish a nonzero geometric obstruction.

## Primitive triples on smooth rational quartics

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
\((m,\ell^2)\).  The embedded extension theorem proved above (also the Bănică--Forster criterion in this setting) says it extends to a primitive
triple exactly when

\[
0\longrightarrow L^2\longrightarrow
J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0
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
rational quartic.  By the [smooth-quadric graph description](../synthesis/01-problem-and-curve.md), the curve is the graph, on
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
[the exact marked-transition verifier](../computations/verify_all_quartic_primitive_obstruction.py).


## Characteristic reach of the two mechanisms

The filtered-Koszul coprime theorem and the corrected embedded extension 0→L²→J₂/(IJ₂+I³)→M→0 require no division by an integer, so their stated regular-immersion/line-quotient constructions apply in every characteristic, including relative mixed characteristic. Their obstruction classes need not remain nonzero after specialization. In the fixed-quartic P010 calculation the balanced frames use 1/2 and the final obstruction has a factor 3: the fixed-C0 displayed nonvanishing proof also applies for every p>3 (only powers of2 are inverted and3 stays nonzero), disappears at3, and cannot simply be read in characteristic2, where the conormal splits differently. The explicit characteristic3 primitive presentation in [positive-characteristic constructions](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) is the control. The higher-initial example itself works in characteristic2 and shows why cancellation, rather than two selected symbols, is essential. These local/embedded mechanisms are compatible with [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) for the fixed C0.

### The fixed-quartic primitive-triple boundary in characteristic2

The invalidity of the balanced coordinate formulas at2 does not leave this particular type undecided. R0020 gives N_C0^*=O(-8)⊕O(-6). There is no surjection to O(-7): a homomorphism from O(-6) vanishes because H0(O(-1))=0, while every homomorphism O(-8)→O(-7) is a section of O(1) and vanishes somewhere. Thus no embedded primitive triple of typeO(-7) exists on fixedC0 in characteristic2 already at the conormal quotient stage. The length-three lci/adjunction argument above works in every characteristic and would force this type for a supported(3,4) pair, so that pair is excluded in characteristic2. Together with the displayed nonzero P010 class for p>3 and the characteristic-zero calculation, the fixed-C0(3,4) obstruction has exactly characteristic3 as its positive-characteristic escape; there the explicit primitive presentation exists. This is an independently reconstructed source-level extension. No assertion about every smooth rational quartic in characteristic2 follows from the fixedC0 splitting alone.
