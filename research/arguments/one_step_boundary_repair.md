---
id: STCI-A-0011
type: argument
title: One-step boundary repair in the actual equation module
status: complete
scope: "#scope"
conclusion: "#conclusion"
---

# One-step boundary repair in the actual equation module

## Scope

Let \(C\) be a smooth connected projective curve regularly embedded in a
smooth threefold over an algebraically closed field. Fix a pure
Cohen–Macaulay thickening \(Y\) supported on \(C\) with generic transverse
algebra \(k(C)[y]/(y^n)\), \(n\ge 2\). The extension problem keeps this
actual lower embedding fixed and prescribes the next saturated normal
layer and its multiplication map. The argument works in arbitrary
characteristic. The bound on the determinant target for the fixed
rational quartic uses its characteristic-zero conormal description.

The homogeneous source tests take place in \(\mathbf P^3\), where the
prescribed degrees satisfy \(ab=(n+1)\deg C\). The separate divisor budget
assumes an actual proper solely supported complete intersection in the
generically curvilinear setting. The [independent audit](#2026-10-27-one-step-boundary-obstruction-audit)
records the scope of the reconstruction and its inherited inputs.
The companion [global repair and weighted initials argument](normal-geometry/normal_boundary_weighted_initials.md#boundary-repair-global-lifting)
gives the principal-parts test for the actual homogeneous source.

## Conclusion

For the prescribed layer \(L^n(D)\), the power relation consumes \(A_Y\)
of the divisor \(D\). The pushout by the remaining divisor \(D-A_Y\) must
kill the equation-module extension class \(e_Y\), and a surjective lift
gives the specified embedded extension. For a final Gorenstein step the
power relation already consumes the entire top divisor. The exact
criterion is \(e_Y=0\) and equality in every top-pairing divisor.

On the proper homogeneous source of the specified bidegree, the
equation-module determinant detects sole support by degree exhaustion.
With the full Gorenstein criterion, top adjunction, and the stated
cohomology vanishings, realization reduces to the two source spaces
being nonzero and having no common fixed surface. This applies to
\(C_0=[s^4:s^3t:st^3:t^4]\) for \(a,b\ge4\) under the stated hypotheses.
The family of admissible lower embeddings and its actual global sources
remain to be determined. The actual two-equation filtration has a
separate divisor budget, with a punctual comparison term required for
raw initial generators.

<a id="2026-10-27-one-step-boundary-obstruction"></a>

## One-step boundary repair and the final Gorenstein obstruction

The argument treats whole classes of embedded multiple curves, not a sampled pair. It makes no unrestricted STCI exclusion or literature novelty claim; the [independent audit](#2026-10-27-one-step-boundary-obstruction-audit) records its review scope.

### 1. Scope and the actual equation module

Let C be a smooth connected projective curve over an algebraically closed
field, regularly embedded in a smooth threefold X. Let I=I_C and E=I/I^2.
Let Y be an embedded pure Cohen--Macaulay thickening with sole support C
and generic transverse algebra k(C)[y]/(y^n), n>=2. Put J=I_Y and

    L=((I O_Y)/(I O_Y)^2)/torsion, R=ker(E -> L),
    M_Y=(J/IJ)/torsion.

All torsion is over O_C. The module M_Y is a rank-two vector bundle:
generically Y has ideal (x,y^n), and a torsion-free coherent sheaf on C
is locally free. Its first-symbol map has image R(-B_Y), with B_Y effective.

Purity implies I^n O_Y=0 and hence I^n subset J and I^(n+1) subset IJ.
Therefore there is a canonical map

    Sym^n E=I^n/I^(n+1) -> J/IJ -> M_Y.

It kills R Sym^(n-1)E: this holds generically and its target is torsion
free. Thus it factors as an injection u_Y:L^n -> M_Y. Let U_Y be its
image and let Ubar_Y be its saturation. Both have generic rank one,
and Ubar_Y is the kernel of the first-symbol map. There is a canonical
effective divisor A_Y with

    U_Y=L^n, Ubar_Y=L^n(A_Y),
    0 -> Ubar_Y -> M_Y -> V_Y=R(-B_Y) -> 0.              (1)

Write

    e_Y in Ext^1_C(V_Y,Ubar_Y)=H^1(C,Ubar_Y tensor V_Y^vee)

for the extension class of (1). This class depends on the actual embedded
lower thickening, rather than only the degrees of its normal layers.
The triple version of this equation-module construction is inherited
reviewed evidence in the
[intrinsic cubic-contact note](normal-geometry/quartic_pair_obstruction.md).
The argument here uses the power-relation line for arbitrary n.

### 2. Exact one-step repair theorem

Fix an effective divisor D and the proposed next saturated layer

    T=L^n(D),

with its prescribed multiplication inclusion i_D:L^n -> T. Consider
embedded extensions Z of Y for which J/I_Z=T is killed by I and the
normal multiplication is i_D.

**Theorem.** Such an extension necessarily has A_Y<=D. Once that
inequality holds, extending i_D to a map M_Y -> T is equivalent to

    image(e_Y)=0 in
    H^1(C,Ubar_Y tensor V_Y^vee(D-A_Y)).                 (2)

The maps extending i_D, if any, form a torsor under H^0(V_Y^vee tensor T).
Among them, the surjective maps correspond to actual embedded pure CM
extensions with the specified layer and generic length n+1. Surjectivity
is an additional condition, automatic when D=A_Y.

Proof. An actual extension gives a surjection

    J/IJ -> J/I_Z=T,

since IJ subset I_Z. It factors through M_Y because T is torsion free.
On U_Y its restriction is the prescribed i_D. To extend this map to the
saturation Ubar_Y=L^n(A_Y), the necessary and sufficient regularity
condition is A_Y<=D; then the extension there is uniquely the inclusion

    gamma: Ubar_Y -> T=Ubar_Y(D-A_Y).

Apply Hom_C(-,T) to (1). The obstruction to extending gamma to M_Y is
the pushout of the extension class e_Y along gamma. Functoriality of
Ext identifies it with (2). The kernel of the restriction map is
Hom_C(V_Y,T), giving the stated torsor of global solutions.

Conversely, compose a surjective solution q:M_Y -> T with J -> M_Y
and let I_Z be its kernel. It is an ideal, contains IJ, and gives

    0 -> T -> O_Z -> O_Y -> 0.

Both the left and right terms are CM of dimension one, so O_Z is pure
CM as well. The extension is square-zero since J^2 subset IJ. At the
generic point, q is nonzero on the relation y^n, and the kernel has
ideal (x-c y^n,y^(n+1)) after a change of parameters; the generic length
is n+1. The quotient O_Z/T=O_Y is pure, so T is saturated, and it is
the last saturated normal layer. Normal multiplication is i_D by
construction. When D=A_Y, gamma is an isomorphism, so every extending
q is surjective. Otherwise surjectivity needs testing only at the
finite zero divisor D-A_Y of gamma. This proves the theorem. No global
retraction of Y or Z to C has been used. Square-zero here refers to the
extension ideal T; it does not assert that the whole nilradical squares
to zero.

This proves a controlled-modification comparison for a FIXED lower
embedding. The exact available repair divisor is D-A_Y, rather than D.
The lower embedding, its A_Y and its e_Y must be varied together in a
family; one cannot vary the boundary while freezing unrelated obstruction
data from a different lower scheme.

### 3. Applying the socle budget

Suppose Y occurs as a saturated truncation of a solely supported,
generically curvilinear Gorenstein multiple curve Z_full of length m.
Write its saturated layers as W_i=L^i(D_i), and D_soc=D_(m-1).
Use the inherited perfect pairings and effectivity in their stated
quasiprimitive scope:

    W_i tensor W_(m-1-i) -> W_(m-1) is perfect,
    D_i+D_(m-1-i)=D_soc, D_0=D_1=0.

In particular 0<=D_i<=D_soc. If the next layer after Y is W_n, theorem
(2) requires e_Y to die after the exact twist D_n-A_Y, and hence after
the possibly larger twist D_soc-A_Y. This is now a proven necessary
repair bound, with coefficient one, for this particular lifting class.
It does not assert that all ambient obstruction problems share this
target or the same twist.

The [principal-parts and multiplication-kernel criterion](normal-geometry/normal_boundary_weighted_initials.md#boundary-repair-global-lifting)
can be applied to the actual bundle Ubar_Y tensor V_Y^vee. On P1 this
is a line bundle, and all possible effective repair divisors can be
tested by one multiplication matrix. The actual divisor must also
satisfy its prescribed linear system and all paired-layer constraints.
Passing a relaxed pole test is not sufficient for a Gorenstein or CI
extension.

### 4. The final Gorenstein step has no extra repair allowance

**Corollary (necessary splitting).** Let Z_full be as in section 3 with
m>=3, and let P_i be its saturated normal ideals. Take

    Y=Z_full/P_(m-1), n=m-1, T=P_(m-1)=W_(m-1).

Then

    Ubar_Y=T, A_Y=D_soc, e_Y=0,                         (3)
    M_Y=Ubar_Y direct_sum V_Y.

The splitting is a necessary condition for a Gorenstein completion of
this fixed penultimate embedded thickening. A nonzero e_Y excludes
EVERY such completion, regardless of the total socle-divisor degree.

Proof. The actual extension gives q:M_Y -> T. Its restriction to
Ubar_Y is nonzero generically and hence injective between line bundles.
There is an intrinsic product map

    j:W_1 tensor W_(m-2) -> M_Y.

Lift the two factors to ambient functions in I and multiply. Their
product belongs to J=I_Y and has zero first normal symbol, so its class
lands in Ubar_Y. Changing a lift of W_(m-2) by P_(m-1) changes this
class by IJ. Changing a lift of W_1 by P_2 gives a class with zero
image under q, because P_2 P_(m-2) subset P_m=0, and also zero first
symbol, because the ambient product lies in I^2. It is therefore zero
in the torsion-free M_Y, since q is injective on Ubar_Y. Changes of
ambient representatives vanish modulo IJ; the same argument verifies
O_C-bilinearity without a global coefficient-field splitting.

The composite q j is the perfect Gorenstein pairing

    W_1 tensor W_(m-2) -> W_(m-1)=T.

It is an isomorphism. Since j lands in Ubar_Y, q|Ubar_Y is consequently
an isomorphism. Thus q supplies a retraction of the inclusion Ubar_Y
in M_Y, and (1) splits. Comparison of the canonical multiplication
L^(m-1) -> T with u_Y identifies their actual zero divisors, giving
A_Y=D_soc. This proves (3).

The restriction m>=3 is essential: when m=2 the lower scheme is C
itself, and E -> L need not split. Under the actual Gorenstein
hypothesis, the first-symbol divisors of Y and Z_full do agree: the
perfect pairing gives P_1 P_(m-2)=P_(m-1) subset K^2, so quotienting by
P_(m-1) adds no new first-order relation. This equality is a consequence
of the pairing, not an identification made for arbitrary lower schemes.

This is a class-wide obstruction on embedded lower thickenings. It
does not state the converse: splitting M_Y need not yield a Gorenstein
completion, and gives no two global carrier equations on its own.

#### Full one-step Gorenstein criterion for a fixed lower Y

The missing converse has an exact additional condition. Let W_i be the
saturated normal layers of Y, 0<=i<n, with W_i=L^i(D_i). Ambient
multiplication gives canonical maps

    j_i:W_i tensor W_(n-i) -> Ubar_Y, 1<=i<n.

Indeed products lie in J. Changes of representatives vanish generically
in IJ, hence vanish in the torsion-free M_Y; this also proves O_C-linearity.
Their images lie in the kernel of the first-symbol map. Compatibility
with ordinary powers gives the actual divisor

    div(j_i)=A_Y-D_i-D_(n-i)>=0.

**Theorem.** Y admits an embedded Gorenstein curvilinear completion of
generic length n+1, preserving this lower embedding, iff

    e_Y=0 and A_Y=D_i+D_(n-i) for every 1<=i<n.          (3a)

Necessity is the preceding corollary and the perfect top pairings.
For sufficiency choose a retraction q:M_Y -> Ubar_Y and construct Z by
section 2 with T=Ubar_Y. It is pure CM, with the old saturated lower
layers and new top Ubar_Y. Its top multiplication pairings are q j_i,
which are perfect by (3a). Complete at a point and choose a local curve
parameter D=k[[t]]. The CM algebra is finite free over D. A basis
adapted to its saturated flag has a Frobenius Gram matrix with zero
entries beyond the antidiagonal and unit antidiagonal, by these perfect
pairings. A functional taking the coefficient of the top basis element
therefore gives a perfect D-pairing. Hence Z is Gorenstein.

The completions, when they exist, form a torsor under
H^0(V_Y^vee tensor Ubar_Y). This is an embedded Gorenstein extension
criterion. It does not produce two global homogeneous equations of
specified degrees. The numerical divisor equalities alone are insufficient:
the extension class e_Y is part of the actual embedded data.

### 5. An exact universal contact test for the actual global source

Keep the fixed embedded lower thickening Y of length n>=2. Let C have
degree d, choose a,b with ab=(n+1)d, and take actual forms

    F in H^0(P3,J(a)), G in H^0(P3,J(b)).

Their classes induce

    rho_(F,G): O_C(-a) direct_sum O_C(-b) -> M_Y,
    theta_Y(F,G)=wedge^2 rho_(F,G)
        in H^0(C,det M_Y tensor O_C(a+b)).

**Theorem (exact fixed-lower-source test).** On the open locus where F,G
are a proper pair, their intersection W has sole reduced support C iff
theta_Y(F,G)=0. If theta_Y(F,G) is nonzero, the generic multiplicity
along C is exactly n and the residual degree is d.

Proof. At eta_C the ideal J_eta has two minimal generators, because
Y_eta is curvilinear. Removing O_C-torsion does not change that generic
fiber, so (M_Y)_eta=J_eta/m J_eta. The determinant is nonzero iff the
classes of F,G span that two-dimensional space. Nakayama then gives
(F,G)_eta=J_eta, and the generic length is n.

If the determinant is zero, the containment (F,G)_eta subset J_eta is
strict, so the generic transverse length of W is at least n+1. It is
finite by properness. Bezout bounds it by ab/d=n+1. Equality therefore
holds and exhausts the total degree; purity of a proper complete
intersection leaves neither a residual curve nor an embedded component.
Conversely sole support gives length n+1 by degree, hence strict
containment and zero determinant. A section of the determinant line
is zero iff its generic value is zero, which makes this a global test.

Thus this stage involves the entire source map

    Theta_(Y;a,b): H^0(J(a)) tensor H^0(J(b))
        -> H^0(C,det M_Y tensor O_C(a+b)).                (4)

For a=b, it is alternating and factors through wedge^2 H^0(J(a)). The
zero pencils are the Plucker linear section

    Gr(2,H^0(J(a))) intersect P(ker Theta),

with the common-surface-factor locus removed. For a!=b use the Segre
product P H^0(J(a)) times P H^0(J(b)) intersect P(ker Theta), again on
the proper-pair open set. All coefficients are actual global constants.
This is not a sampled example or a symbolic-section surrogate.

For an arbitrary admissible family of lower thickenings, these maps
vary on cohomology/rank strata. A theorem that every decomposable
kernel point is improper excludes the whole family. A proper kernel
point gives actual existence at the specified degrees. Showing only
that the generic source has nonzero determinant leaves the special
kernel locus unresolved. Classifying all admissible lower embeddings
and computing their actual source maps remain substantive work.

The triple case is the intrinsic cubic-contact construction cited above.
This argument gives its determinant/degree-exhaustion meaning for every
curvilinear lower length n; it does not replay the accepted quartic
classification or prove its nonvanishing by formal target degree.

#### Uniformly small target for the fixed rational quartic

Before testing a prospective degree-(a,b) completion, its penultimate Y
must satisfy the top-line adjunction requirement

    Ubar_Y=omega_C tensor O_C(4-a-b).

Using V_Y=R(-B_Y) and det E=R tensor L=omega_C^(-1) tensor O_C(-4),
the determinant target simplifies to

    det M_Y tensor O_C(a+b)=L^(-1)(-B_Y).               (4a)

This is a line-bundle identification on the admissible locus; it is
not assumed for an arbitrary lower Y unrelated to those carrier degrees.
For the fixed characteristic-zero rational quartic, L=O(-q) with
1<=q<=7 in the sole-support curvilinear CI setting. Thus the target
in (4) has dimension max(q-deg B_Y+1,0)<=8. For every admissible fixed
penultimate Y, the whole actual-source contact test requires at most
eight bilinear equations, or eight Plucker-linear equations when a=b.
This does not classify those Y or prove that their proper kernel loci
are empty. The following simplification is essential: on the fully
Gorenstein-admissible locus these equations are automatic in the main
rational-quartic degree range, so their small number must not be sold
as an additional nontrivial obstruction there.

There is also a conditional class-wide dimension test. Let P be the
Segre source product (or the Grassmannian for equal degrees), and let
r be the rank of Theta as a linear map on the ambient tensor/wedge
space. Its zero locus on P is a projective linear section of codimension
at most r. If dim P>=r and the improper-pair locus has codimension >r
inside P, projective dimension theory forces a proper zero point.
By the exact source theorem this proves fixed-degree existence. Thus
an exclusion on such a source family must account for a sufficiently
large improper locus, a failure of the lower admissibility conditions,
or a genuinely small source. No generic codimension estimate for that
improper locus is asserted here.

#### Exact fixed-surface criterion when the top layer has no source sections

Assume Y satisfies the full Gorenstein-completion criterion (3a), and
the top line Ubar_Y is identified with T=omega_C tensor O_C(4-a-b).
Choose a retraction q:M_Y -> T and let Z be its completion. For an
actual degree-a section F through Y, the image q(F) is a global section
of T(a); similarly q(G) belongs to H^0(T(b)). Therefore, if

    H^0(C,omega_C tensor O_C(4-b))=0,
    H^0(C,omega_C tensor O_C(4-a))=0,                    (4b)

ALL degree-a and degree-b forms through Y also vanish on Z. Equivalently
the exact ideal sequence 0 -> I_Z -> I_Y -> i_*T -> 0 has identical
global section spaces in those degrees. Consequently Theta is
identically zero for these sources, not just zero on selected pairs.

For C0, omega_C=O_P1(-2) and O_C(1)=O_P1(4). The two bundles in (4b)
are O(14-4b) and O(14-4a), so (4b) always holds when a,b>=4.

The automatic source vanishing itself is more general than the rank-two
curvilinear construction. For any Gorenstein multiple structure Z with
smooth sole support C, its socle T=Ann_(O_Z)(I_C O_Z) is the line
omega_C tensor (omega_Z|C)^(-1), and the quotient Y=Z/T is pure.
If omega_Z|C=O_C(s) and C is rational, then H^0(T(d))=0 for d<=s.
Hence H^0(I_Y(d))=H^0(I_Z(d)) throughout that degree range. For a
degree-(a,b) CI, s=a+b-4, so both carrier degrees lie in this range
when a,b>=4. This explains the source collapse without requiring a
particular generic transverse Hilbert function. Constructing the
admissible Y and its Gorenstein completions by the rank-two method
above still requires generic curvilinearity.

There is a simple exact properness criterion for the whole source.
Let H_a=H^0(P3,I_Y(a)) and H_b=H^0(P3,I_Y(b)), both nonzero. Over the
infinite field k, a coprime pair F in H_a, G in H_b exists iff no
irreducible surface divides EVERY section of BOTH spaces. To prove
the nontrivial direction, first choose F avoiding the finitely many
irreducible factors of the fixed gcd of H_b. Each avoidance excludes
a proper linear subspace of H_a. Then choose G avoiding the finitely
many factors of F, again outside a finite union of proper subspaces.
The converse is immediate.

**Exact realization criterion in this range.** Fix a,b with
ab=(n+1)deg C and (4b). A fixed lower Y is the penultimate level of a
sole-support degree-(a,b) CI iff:

1. It satisfies (3a), so an embedded Gorenstein completion exists.
2. Its saturated power line is Ubar_Y=omega_C tensor O_C(4-a-b).
3. Both actual source spaces H_a,H_b are nonzero and they have no
   common fixed surface component.

For sufficiency, construct one completion Z using (1)--(2), choose
the coprime global source pair from condition 3, and use (4b) to see
that both equations vanish on Z. Its degree is ab, so a proper CI
containing it has the same cycle and is equal to Z: the kernel of
O_CI -> O_Z would be a punctual subsheaf of the pure O_CI. Necessity
follows from sections 4--5 and CI adjunction. In that direction generic
curvilinearity is automatic: the Artin Gorenstein generic CI algebra
has a length-one ideal as the kernel of its map to Y, hence that ideal
is its socle. In length at least three the socle lies in the square of
the maximal ideal, so its quotient has the same embedding dimension.
The quotient Y is curvilinear. Purity identifies Y with the saturated
penultimate truncation. This is a criterion for a FIXED actual lower
embedding. Classifying all such Y is still open.

Thus, for C0 and a,b>=4, there is no further source-determinant
nonvanishing problem on the fully admissible splitting locus. The
global obstruction there is exactly a missing source space or a common
fixed surface in the two actual linear systems. For other curves or
degrees where (4b) fails, the universal bilinear/Plucker test remains
necessary to examine.

There is an additional necessary rigidity condition in this range:

    H^0(C,V_Y^vee tensor Ubar_Y)=0                     (4c)

for any Y that actually occurs as the penultimate level of that global
CI. Otherwise (3a) supplies more than one distinct embedded Gorenstein
completion. By (4b), every degree-a and degree-b form through Y vanishes
on every completion. A single proper degree-(a,b) pair would contain
all of them, and degree exhaustion would make all completions equal,
contradicting their distinct normalized retractions. Thus a positive-
dimensional completion torsor forces failure of the global source test.
On P1, (4c) is simply deg Ubar_Y<deg V_Y. It is a useful preliminary
filter; it is not sufficient for a CI realization.

### 6. A separate budget on the actual two-equation module

Now assume Z_full=V(F_a,G_b) is a proper CI with sole support C and
generic transverse length m>=2. For its ideal J_full put

    D_eq=J_full/IJ_full=O_C(-a) direct_sum O_C(-b),
    F^r D_eq=((J_full intersect I^r)+IJ_full)/IJ_full.

Let B_full be the first-symbol divisor, so the image in E is R(-B_full).
There are canonical endpoints

    F^2 D_eq=ker(D_eq -> E)=K_eq,
    F^m D_eq=L^m, F^(m+1) D_eq=0.

The top inclusion has ACTUAL divisor

    div(F^m D_eq -> K_eq)=D_soc+B_full.                 (5)

One must not infer (5) merely by equating determinant line bundles.
A local multiplicative Tor comparison proves its coefficientwise form.
Choose integral normal parameters x,y with X spanning R and Y mapping
to L. The top equation y^m gives the normal Koszul cycle (0,y^(m-1)).
An equation f=A x+B y gives (A,B). Their Tor product is

    +/- (A|C) y^(m-1) e_X wedge e_Y.

The carrier Koszul resolution identifies the product with the exterior
product in D_eq, while normal Tor_2 is Ann_(O_Z)(I O_Z) tensor det E.
Thus the wedge map L^m tensor R(-B_full) -> det D_eq factors as the
top-power inclusion of divisor D_soc and the first-symbol inclusion
of divisor B_full. Their divisors add, proving (5).

Every intermediate F^r is a rank-one subsheaf between these endpoints.
Writing G_r=F^r/F^(r+1), telescoping gives

    sum_(r=2)^(m-1) div(G_r)=D_soc+B_full<=2 D_soc.      (6)

The inequality uses the first-normal bound in [R0019](../results/quasiprimitive_residual_cycles.md), in its specified
finite-flat/saturated scope. This is an equation-module cost, distinct
from the structure-sheaf torsion (m/2)D_soc.

For the reviewed spectral comparison, write

    Q=in_I(J_full)/S_+ in_I(J_full),
    0 -> Delta_r -> Q_r -> G_r -> 0.

Generic curvilinearity gives Delta_eta=0. The torsion comparison yields

    sum_r div(tors Q_r)
      =D_soc+B_full+sum_r div Delta_r.                  (7)

Hence (6) is NOT a bound on all raw initial-equation torsion unless
Delta=0. Higher spectral cancellations must be retained. See the
[normal Koszul comparison](../results/normal_koszul_comparison_defect.md)
for the spectral argument and the
[open sole-support question](../frameworks/formal-normal-geometry/open_normal_geometry.md#punctual-relative-defect-under-sole-support)
for the remaining existence problem.

### 7. What has been gained and what remains

The proposed boundary-repair comparison is now proved for the specific
one-step obstruction e_Y in (1). The final Gorenstein step sharpens it
to exact vanishing: its top divisor is already fully used in saturating
the power relation and cannot be counted again as new repair allowance.
The actual-source determinant test (4) is exact after properness and
degree exhaustion; the CI equation module has the separate cost (5)--(7).

These results make the next family-level questions definite:

- Determine the zero locus of e_Y for admissible embedded lower
  thickenings; a nonzero class excludes all final Gorenstein completions.
- On its zero locus, impose local Gorenstein/pairing conditions and the
  top adjunction line. For C0 with a,b>=4, then test the two actual
  source spaces and their common fixed surfaces; the source determinant
  is automatic there. In degree ranges where (4b) fails, retain the
  full source determinant test.
- In earlier stages, use the exact remaining divisor D_n-A_Y and the
  common-divisor principal-parts test; total degrees alone discard this
  information.

The source-sensitive jet images and finite fixed-degree endpoint remain
those in the preceding repair note. No whole admissible family has
been proved to have e_Y nonzero here, so no new STCI exclusion follows.

### 8. Literature and provenance boundary

The perfect-pairing characterization of Gorenstein multiple structures and canonical-filtration duality are classical; see Manolache, [*Gorenstein Multiple Structures on Smooth Algebraic Varieties*](https://arxiv.org/pdf/0706.2204), §2 and Remark 2, including quasiprimitive specialization. The fixed-lower equation-module extension and actual-source determinant arguments are proved here. No novelty or exhaustive literature claim is made; inherited filtration inputs retain their own scope.

---

<a id="2026-10-27-one-step-boundary-obstruction-audit"></a>

## Independent audit: one-step boundary and final Gorenstein obstruction

Date: 2026-10-27. Reviewer: independent `equation_budget_audit` agent.
Status: mathematical reconstruction of the [source note](#2026-10-27-one-step-boundary-obstruction),
No new unrestricted STCI exclusion or realization
of an unclassified family is certified.

### Scope and method

The argument concerns a smooth connected projective curve \(C\) in a smooth threefold \(X\) over an algebraically closed field and a pure Cohen–Macaulay lower thickening \(Y\) with sole support \(C\), generically curvilinear of length \(n\ge2\). It is characteristic-independent except for the characteristic-zero conormal description of \(C_0\). Accepted saturated pairings and first-normal bound R-0019 are premises. Independent review checked equation modules, extension/converse, the actual-source determinant (automatic after full Gorenstein admissibility and the stated cohomology vanishings), and coefficientwise divisor comparison; no finite example was used to infer a family result.

### 1. The equation module and its power line

For J=I_Y, M=(J/IJ)/torsion is a rank-two vector bundle on C: the
generic ideal is a curvilinear two-generator complete intersection,
and torsion-free coherent sheaves on a smooth curve are locally free.
The first-symbol map has rank-one image R(-B_Y).

Purity proves I^n O_Y=0 from generic nilpotence. Therefore I^n subset J
and I^(n+1) subset IJ, giving Sym^n E -> M. Its generic kernel is
R Sym^(n-1)E, and this entire subbundle maps to zero because M is
torsion free. The quotient L^n maps injectively. Its saturation Ubar
is exactly the kernel of the first-symbol map, yielding the source's
sequence (1) and actual inclusion divisor A_Y.

This construction retains the embedded ideal. It is not determined
solely by the ranks and degrees of the ordinary normal layers.

### 2. One-step extensions and their exact obstruction

An extension by the O_C-line T=L^n(D), killed by I, induces a map
J/IJ -> T. Its torsion-free target makes it factor through M. Extending
the prescribed map L^n -> T first to Ubar=L^n(A_Y) is possible exactly
when A_Y<=D, and then that map is uniquely the natural inclusion.

Applying Hom(-,T) to 0 -> Ubar -> M -> V_Y -> 0 shows that extending
this inclusion to all of M is equivalent to vanishing of the pushout
of e_Y. Naturality of Ext identifies the pushout with the map

    H^1(Ubar tensor V_Y^vee)
      -> H^1(Ubar tensor V_Y^vee(D-A_Y)).

Thus the source's available repair divisor D-A_Y and its torsor
H^0(V_Y^vee tensor T) are correct. It would be incorrect to use all of D
as new repair allowance after A_Y has already been used in saturation.

For the converse, a surjective q:M -> T gives the ideal kernel of
J -> M -> T; it contains IJ. The resulting sequence
0 -> T -> O_Z -> O_Y -> 0 is CM of dimension one by the depth lemma.
The ideal T is square zero because J^2 subset IJ. Generic nonvanishing
on y^n makes the generic quotient the curvilinear extension of length
n+1. Since O_Y is pure, T is saturated in O_Z and is the final
saturated layer. The prescribed ordinary multiplication is the map
L^n -> T. This verifies the exact converse stated in section 2.
Surjectivity is automatic when D=A_Y; otherwise it is an additional
condition at the finite vanishing divisor of Ubar -> T.

### 3. The final Gorenstein step and the full converse

For a genuine final Gorenstein completion, the map q:M -> T is
generically injective on Ubar. Multiplying ambient representatives of
W_1 and W_(m-2) defines the source's map j into Ubar. Changes of lifts
give zero generically in J/IJ and hence zero in the torsion-free M;
the source's argument using q and the saturated product also verifies
the same fact without assuming a global coefficient retraction.
The composite qj is the inherited perfect top pairing. It follows that
q|Ubar is an isomorphism, and normalizing by it gives a retraction of
Ubar in M. Hence e_Y=0. Compatibility with the ordinary power maps
identifies A_Y with D_soc as an actual divisor, not merely by degree.

For arbitrary fixed lower Y, the maps

    j_i:W_i tensor W_(n-i) -> Ubar, 1<=i<n,

are indeed canonical. Products vanish generically in O_Y, so purity
puts them in J. Changes of representatives lie generically in IJ;
their classes therefore vanish in M. This also proves O_C-linearity.
The products have zero first symbol and thus land in Ubar. Composing
with the ordinary maps from L^i and L^(n-i) yields the degree-n power
map, proving the ACTUAL divisor formula

    div(j_i)=A_Y-D_i-D_(n-i).

Necessity of e_Y=0 and zero divisors of every j_i follows from a
Gorenstein completion. Conversely, a retraction q constructs a pure CM
completion with top Ubar, and the old saturated lower layers are
preserved. If every j_i is an isomorphism, its top pairings are perfect.
Locally over a lifted parameter DVR, a basis adapted to the saturated
flag gives a Frobenius Gram matrix: entries beyond the antidiagonal
are zero and antidiagonal entries are units. A top-coefficient
functional is therefore perfect, proving the completion Gorenstein.
This independently verifies the source's iff criterion (3a).

The m>=3 restriction is correct. When the lower scheme is C itself,
its conormal E need not split; that case is outside the rank-one
first-symbol setup used here. Under the final Gorenstein pairing,
the top ideal is contained in K^2, so passing to the penultimate level
does not add first-order relations. The equality of the two first-symbol
divisors is therefore justified in this scope.

### 4. Exact actual-source determinant and its limits

At eta_C, J has two minimal generators and M_eta=J_eta/m J_eta.
The determinant of two actual carrier sections is nonzero exactly when
their classes span this space, which by Nakayama is equivalent to
generating J_eta. Their generic length is then n. If the determinant
vanishes, their ideal is strictly smaller, so a proper pair has generic
length at least n+1. Under ab=(n+1)deg C, Bezout makes this equality
and exhausts degree; purity leaves no residual curve or embedded point.
This proves the exact source criterion, including the residual degree d
when the determinant is nonzero.

The Segre/Grassmannian description uses actual global section spaces,
so its unknowns are constants in k. No generic formal-symbol surrogate
has been substituted. A generic nonzero determinant does not exclude
its exceptional zero locus, as the source explicitly records.

The conditional dimension assertion is valid for the nonempty Segre or
Grassmannian source: a section by r ambient linear equations is
nonempty when dim P>=r, and has dimension at least dim P-r. A closed
improper locus of larger codimension cannot contain it. The source
makes no unjustified general estimate of that improper locus.

### 5. Small target and the essential automatic-vanishing refinement

On the top-adjunction-admissible locus, det M=Ubar tensor R(-B_Y)
and Ubar=omega_C O_C(4-a-b) give exactly

    det M tensor O_C(a+b)=L^(-1)(-B_Y).

For C0 in characteristic zero, 1<=q<=7 gives the claimed target
dimension at most eight. This is an upper bound on the source contact
equations, not automatically a set of eight nontrivial conditions.

The source's later refinement is necessary and correct. Once a global
retraction q:M -> T exists, the quotient of any actual degree-a
section through Y is a section of T(a)=omega_C O_C(4-b), and similarly
for degree b. If both cohomology spaces vanish, every such section
already vanishes on the completion. Therefore Theta is identically
zero on this source, with no further determinant obstruction.
For C0 and a,b>=4 the bundles have degrees 14-4b and 14-4a, so the
vanishings hold. This statement is also valid for any smooth curve
satisfying the source's two displayed cohomology vanishings.

For two nonzero section spaces over an infinite field, existence of
a coprime pair is equivalent to absence of a common fixed irreducible
surface. The finite-union-of-proper-linear-subspaces argument in the
source proves the nontrivial direction exactly: choose F avoiding all
fixed factors of H_b, then G avoiding every irreducible factor of F.

Consequently the exact fixed-lower realization criterion is valid in
the stated range. For sufficiency the constructed completion has degree
ab, and all source sections vanish on it. A proper CI containing it
has the same cycle; its kernel over the completion is a punctual
submodule of a pure CI structure sheaf and is zero. Thus the schemes
are equal. This does not classify all admissible Y or supply a proper
pair in an unclassified family.

#### Final source refinements: socle quotients, curvilinearity, and rigidity

The final saved source contains three further consequences, which the
reviewer independently checked. They do not require a sampled example.

First, for any Gorenstein multiple structure Z with smooth sole support,
its socle Ann_(O_Z)K is the O_C-line omega_C tensor (omega_Z|C)^(-1)
by finite duality. It is saturated: locally a lifted curve parameter t
is a nonzerodivisor, and tb in Ann K implies t(bK)=0 and hence bK=0.
The quotient by this socle is therefore pure CM. For rational C and
omega_Z|C=O_C(s), the line T(d)=omega_C O_C(d-s) has negative degree
whenever d<=s. Its H^0 vanishes, so the ideal exact sequence proves
H^0(I_Y(d))=H^0(I_Z(d)). This source collapse does not use generic
curvilinearity. The rank-two classification of its possible completions
does still use that separate hypothesis.

Second, in the necessity direction of the exact realization criterion,
a generic Artin Gorenstein CI algebra mapping onto the curvilinear
length-one-shorter algebra has a length-one kernel. Such an ideal is
the socle. In length at least three that socle lies in the square of
the maximal ideal: if m^2=0 and the length were at least three, the
socle would have dimension at least two; otherwise the last nonzero
power m^s, s>=2, is already the unique socle. Quotienting by it
preserves embedding dimension. Since the quotient is curvilinear,
the original algebra is curvilinear too. Purity then identifies the
lower Y with the saturated penultimate truncation.

Finally, the completion torsor has distinct embedded ideals for
distinct normalized retractions. Indeed two surjections with the same
kernel differ by an automorphism of the target line, and their
restrictions equal the identity on Ubar, forcing that automorphism
to be the identity. Under (4b), all actual degree-a and degree-b
sections through Y vanish on every such completion. A single proper
pair would contain every completion; equal degree and purity would
make all of them the same scheme. Thus an actual CI in this range
requires H^0(V_Y^vee tensor Ubar_Y)=0. On P1 this is equivalently
deg Ubar_Y<deg V_Y, exactly as in (4c). It is only a necessary
rigidity condition, and the source does not assert sufficiency.

All three final refinements pass audit with their stated hypotheses.

### 6. Actual equation-module and spectral divisor accounts

For an actual CI of generic curvilinear length m, purity gives
I^m subset J_full and I^(m+1) subset IJ_full. The same power-line
argument yields F^m D_eq=L^m and F^(m+1)=0. Also F^2 is the line
kernel of the first-symbol map D_eq -> R(-B_full).

The coefficientwise inclusion divisor needs the source's multiplicative
Tor argument; determinant line-bundle isomorphisms alone give only a
class or linear equivalence. The reviewer independently reconstructed
that argument. A normal Koszul cycle for y^m is (0,y^(m-1)), while
f=Ax+By gives (A,B). Their product is, up to sign,
(A|C)y^(m-1) times the normal determinant frame, because the top power
annihilates the nilradical. Carrier Tor identifies this with the wedge
in D_eq, and normal Tor_2 is the socle times det E. Thus the actual
zero divisor is D_soc+B_full.

Intermediate equation quotients are torsion, and telescoping gives
sum div G_r=D_soc+B_full. The R0019 first-normal divisor is the image
of the TOTAL ideal of the multiple structure, hence equals B_full;
its bound applies here without the auxiliary-surface hypotheses of
its separate residual-cycle assertion. This verifies the bound by
2 D_soc in the specified finite-flat/saturated setting.

Generic curvilinearity makes Delta generically zero, so the reviewed
torsion comparison gives the source's equality

    sum div tors Q_r=D_soc+B_full+sum div Delta_r.

The 2 D_soc bound does not apply to raw initial-equation torsion
without subtracting Delta. The source preserves the unresolved
punctual-Delta question and does not claim to settle it.

### Scope of the obstruction

The contact criterion and fixed-surface reduction apply to an entire fixed lower embedding. They do not establish that the admissible lower-embedding family contains a proper source point or that the fixed-surface condition always fails. The global classification remains open.
