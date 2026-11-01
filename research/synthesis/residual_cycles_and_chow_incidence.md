# Residual cycles, Chow incidence, and actual generators

**Status:** reviewed provisional general geometric deductions; independent
reconstruction and its scope are recorded below.
No canonical result is promoted. The unrestricted characteristic-zero STCI
question for the fixed quartic remains open.

Fix an algebraically closed field k, an integral curve
C in projective three-space of degree delta, and positive integers a<=b.
Write S=k[x_0,x_1,x_2,x_3], I=I_C, and D=ab. Unless explicitly restricted
below, the statements work in every characteristic. The motivating curve is
C_0=[s^4:s^3t:st^3:t^4], for which delta=4. Neither carrier smoothness nor
normality, and no constant transverse quotient, is assumed.

The question first concerns every **proper containing intersection**
Y=V(F_a,G_b), with F,G in I, and fundamental cycle

\[
 [Y]=m_C(Y)[C]+R_Y,\qquad
 D=\delta m_C(Y)+\deg R_Y.
\]

Here R_Y is the effective sum of the other curve components with their
generic lengths. Sole support is a special case. The main deductions are a
closed multiplicity filtration on the actual equation space, and an exact
two-degree generation test on the Hilbert scheme with the **full** prescribed
complete-intersection Hilbert polynomial. These are intrinsic reductions;
the resulting incidences have not been computed or proved empty.

## 1. The proper-pair Chow morphism

Let G=Gr(2,4) be the Grassmannian of lines, and put
E_e=H^0(G,O_G(e)) for e>=0. Fix a nonzero Chow section
Q=Ch_C in E_delta, up to scalar. All products and equalities below are
sections on G. In Pluecker coordinates they are interpreted **modulo the
Pluecker relation**, not as equalities of arbitrarily chosen polynomial
representatives.

On the ordered presentation space

\[
 X=\mathbf P(I_a)\times\mathbf P(I_b)
\]

let U be the open subset of pairs with no common factor. Empty equation
spaces simply give an empty parameter space. The universal-line Sylvester
construction gives

\[
 R_{F,G}\in E_D,
 \qquad
 \chi:U\longrightarrow\mathbf P(E_D),\quad
 (F,G)\longmapsto[R_{F,G}].                         \tag{1}
\]

The inherited [Chow-resultant criterion](global_equations_and_constructions.md#p-033-the-global-chow-resultant-certificate)
proves that R_{F,G} is nonzero precisely on U and, there,

\[
 R_{F,G}=c\prod_B\operatorname{Ch}_B^{m_B(Y)},\qquad c\in k^*.       \tag{2}
\]

Its coefficients are polynomial in the equation coefficients, homogeneous
of degree b in F and a in G. Thus they define a morphism on U, without
choosing a normalization of R. The construction also descends to the
equal-degree pencil space and to the unequal-degree presentation space
quotienting G by every ambient multiple of F: it depends on the complete
intersection, up to the scalar already discarded in (1).

Equation (2) is a cycle assertion, with generic scheme lengths included.
We use the characteristic-free universal-line Sylvester formulation
already proved in the inherited criterion, including its precise
pushed-forward Koszul construction.

## 2. Closed multiplicity and residual-degree filtrations

**Theorem.** For each integer r>=0 with r delta<=D, the locus

\[
 U_{\ge r}=\{(F,G)\in U:m_C(V(F,G))\ge r\}                          \tag{3}
\]

is closed in U. It is precisely the inverse image under chi of the fixed
projective linear subspace

\[
 \Lambda_r=
 \mathbf P\bigl(Q^r E_{D-r\delta}\bigr)
 \subset\mathbf P(E_D).                                           \tag{4}
\]

Consequently m_C is upper semicontinuous on U and deg R_Y is lower
semicontinuous there. The exact multiplicity loci
U_{>=r} minus U_{>=r+1} form a finite locally closed partition of all
proper containing pairs.

**Proof.** Multiplication by Q^r is an injective k-linear map
E_{D-r delta}->E_D because G is integral. Its projectivized image is
therefore a closed linear subspace. If m_C>=r, factorization (2) puts
R_{F,G} in its image.

Conversely, membership says that R_{F,G}=Q^r H as a section. The Chow
divisor of an integral curve is an irreducible divisor on G, and distinct
integral curves have distinct Chow divisors. Taking the order of vanishing
along that divisor in (2) gives m_C>=r. This divisor argument also avoids
any assumption that chosen Pluecker polynomial representatives factor
uniquely. The semicontinuity and residual-degree statement follow from
D=delta m_C+deg R. No claim that generic local length is automatically
semicontinuous after an arbitrary localization is required. QED.

For U consisting of containing pairs, U_{>=1}=U. Set M=floor(D/delta).
If delta divides D, then

\[
 U_{\mathrm{STCI}}=U_{\ge D/\delta}
 =\chi^{-1}\bigl([Q^{D/\delta}]\bigr).                            \tag{5}
\]

Indeed the residual effective cycle then has degree zero. A proper
complete intersection is unmixed and has no isolated or embedded
components, so its reduced scheme support is exactly C. Conversely sole
support gives the displayed Chow power. If delta does not divide D,
the STCI locus is empty; the top multiplicity locus can still describe
proper intersections with a positive residual degree.

For C_0, equation (5) covers every pair in every fixed degree (a,b) with
4 dividing ab, including reducible or singular carriers and moving
noncurvilinear transverse algebras. It supplies no degree-independent
bound or nonemptiness decision.

### Finite equations and the improper boundary

Choose bases for E_D and its quotient E_D/(Q^r E_{D-r delta}). The
coordinates of the composite of R_{F,G} with that quotient are finitely
many polynomial equations defining (3) on U, set-theoretically. This is
a complete incidence description, rather than an approximation by a
chosen finite normal form. Its natural scheme structure is a pullback of
the linear subspace; no claim that it is reduced is made.

Properness is essential. At every common-factor pair all coefficients
of R vanish, so the polynomial equations also vanish there. In
particular, allowing the scalar in R=cQ^M to become zero admits the
entire improper boundary. Equations on X must be restricted to U, or
their closure must remove components confined to this boundary. In
homogeneous coordinates, if B is the ideal of all resultant
coefficients and L_r the ideal of the quotient coordinates, the
scheme-theoretic closure of the incidence on X minus V(B) is obtained
by saturation L_r:B^infinity, with the usual sheaf/homogeneous
interpretation. Taking the reduced structure gives the set-theoretic
closure. This closure need not equal V(L_r).

The theorem says precisely that multiplicity cannot drop in a
specialization **whose limiting pair remains proper**. It places no
generic length on an improper limiting pencil. Its full flat ideal limit
is the appropriate replacement there.

### A single affine chart for the whole supported-pair locus

There is a stronger fixed-degree conclusion, for any integral C and in
every characteristic. If delta divides D, put M=D/delta and choose any
linear functional \(L:E_D\to k\) with \(L(Q^M)\ne0\). The coefficient
\[
 s=L(R)\in H^0\bigl(X,O_X(b,a)\bigr)
\]
is a section of an ample line bundle. If s is identically zero, the
supported incidence is empty. Otherwise its nonvanishing locus X_s is
affine: a sufficiently high power of the line bundle is very ample,
and X_s is the intersection of its projective embedding with the affine
complement of the hyperplane defined by that power of s. Also X_s is
contained in U, since a common-factor pair has R=0.

Every supported proper pair lies in this **same** chart, because its
resultant is cQ^M. Its entire fixed-degree incidence is therefore
\[
 U_{\mathrm{STCI}}=\chi|_{X_s}^{-1}([Q^M]),
\]
a closed subscheme of an affine scheme, and hence affine. Normalize
L(R)=1 on the Chow target chart; the remaining coefficient equations
define the exact supported incidence there without improper-boundary
saturation. This does not claim that the equations have a solution.

For equal degrees d, the identity
\(R_{A(F,G)}=\det(A)^dR_{F,G}\) makes the resultant a global section
of \(E_{d^2}\otimes O_{\operatorname{Gr}(2,I_d)}(d)\).
The same argument proves affineness of the whole supported proper-pencil
locus. No torus action is required for these conclusions. For C_0 the
functional may be chosen invariant, as proved in the
[centered Chow-linearization argument](vgit_surface_pairs_and_full_limits.md#the-chow-linearization-covers-supported-pairs-in-every-degree),
so the affine chart is T-invariant. Affineness here concerns the ordered
pair space, or the equal-degree pencil space; it is not asserted for an
unequal-degree quotient bundle without its own ampleness proof, the
projective closure, or the entire supported Hilbert locus. Nor does an
affine torus variety have to contain a fixed point: G_m acting on itself
is the elementary counterexample.

## 3. Exact generator incidence at the complete-intersection polynomial

Let

\[
 P_{a,b}(n)=Dn-\frac{D(a+b-4)}2
\]

be the Hilbert polynomial of a proper degree-(a,b) complete intersection.
Let J be any saturated homogeneous ideal with this polynomial; it need
not be primary, Cohen--Macaulay, supported on C, or known to be a limit
of complete intersections.

**Theorem.** The following conditions are equivalent:

1. J is generated by a regular sequence of degrees a,b.
2. There exist F in J_a and G in J_b with R_{F,G} nonzero.
3. J_a is nonzero, and the linear system J_b has no fixed hypersurface
   component: the greatest common divisor of its nonzero forms is 1.

The third condition has a coordinate-free interpretation: the base locus
of the degree-b equation system has codimension at least two, and a
degree-a equation exists.

**Proof of 2=>1.** Nonzero resultant makes K=(F,G) a saturated proper
complete-intersection ideal with Hilbert polynomial P_{a,b}. Since
K is contained in J, the coherent sheaf associated to J/K has Hilbert
polynomial zero. A nonzero coherent sheaf on projective space has a
nonzero Hilbert polynomial, so that sheaf vanishes. Saturation of K and
J then gives K=J as homogeneous ideals. This uses the entire Hilbert
polynomial, not only its degree. The reverse implication is immediate.

**Proof of 3=>2.** Choose any nonzero F in J_a. No irreducible factor
of F divides every member of J_b, because that system has gcd 1.
Over the infinite field k, choose G in J_b outside the finitely many
proper linear subspaces consisting of forms divisible by one of those
factors. Then F and G have no common factor. This proves 2.

**Proof of 1=>3.** If J=(F,G), its degree-b piece contains G and all
ambient multiples F S_{b-a}. For b>a the gcd of those multiples is F;
for b=a it already contains F itself. Coprimality of F,G proves that
J_b has no common factor. QED.

This eliminates a separate higher-degree generator check **on this exact
Hilbert-polynomial locus**. Two independent sections alone are still
insufficient: they can have a common surface factor. Conversely, once
one has a proper prescribed-degree pair inside J, all higher ideal
generation follows from inclusion and the full Hilbert polynomial.

The polynomial hypothesis cannot be omitted. For instance the line ideal
J=(x_0,x_1) has J_2 nonzero and gcd(J_2)=1; it contains the proper pair
(x_0^2,x_1^2), but is not equal to its complete-intersection thickening.
Their Hilbert polynomials differ. This example also explains why a
criterion for containing intersections does not itself identify the
embedded scheme being investigated.

### Openness

The type-(a,b) complete-intersection locus CI_{a,b} is open in
Hilb^{P_{a,b}}(P^3). Here is a proof adapted to the incidence test.
At a point J=(F,G), the Koszul resolution gives
H^1(P^3,I_J(d))=0 for all d. Cohomology and base change for the universal
ideal therefore extend the chosen sections F in degree a and G in
degree b over a neighborhood of J. Their resultant remains nonzero
after restricting that neighborhood. Every fiber still has polynomial
P_{a,b}, so the preceding theorem makes every such fiber a complete
intersection of those degrees.

Consequently this exact open incidence can be tested on a supported
Hilbert locus or on a direction-specific attracting locus. Where J_a
and J_b are vector bundles, it is the existence of a nonzero resultant
on their product; equivalently the restricted resultant polynomial is
not identically zero. The base-component criterion gives the same test
intrinsically. A calculation of it is still required on the family in
question.

## 4. Full graph limits and the top cycle fiber

Let f:U->Hilb^{P_{a,b}} send a proper containing pair to its full
intersection, and take the reduced closure of its graph. The
[surface-pair graph](vgit_surface_pairs_and_full_limits.md#4-retain-the-intersection-the-graph-and-its-two-polarizations)
retains equations and the entire saturated ideal. The ordered
presentation above may be replaced by the less redundant pencil or
unequal-degree presentation space.

To keep the Chow coordinate without making an unnecessary assertion
about the scheme structure of a Hilbert--Chow morphism, use the reduced
projective **triple graph**

\[
 \widehat\Gamma=
 \overline{\{(x,f(x),\chi(x)):x\in U\}}
 \subset X\times\operatorname{Hilb}^{P_{a,b}}\times\mathbf P(E_D).
                                                                    \tag{6}
\]

It is a graph compactification, not a claimed smooth resolution. On U
it is the original graph, and its three coordinates retain the limiting
pair, full embedded scheme, and nonzero projective limit of the Chow
forms. In characteristic zero, flat specialization of fundamental cycles
identifies the third coordinate at geometric boundary points with the
Chow form of the Hilbert coordinate. One can verify this on a trait
through the boundary point: the flat Hilbert family specializes its
fundamental cycle, and the proper separated Chow variety records its
unique limiting Chow form. This is only a geometric-point statement;
no equality of nonreduced Hilbert and Chow functors is used. The standard
cycle-family qualifications are discussed in
[Kollar, section 3.1, especially 3.14](https://web.math.princeton.edu/~kollar/FromMyHomePage/modbook-final.pdf).
The earlier incidence theorems do not depend on this characteristic-zero
boundary interpretation.

Assume now delta divides D, and put M=D/delta. Define the closed top
Chow fiber

\[
 T_M=\widehat\Gamma\cap
 \bigl(X\times\operatorname{Hilb}^{P_{a,b}}\times\{[Q^M]\}\bigr).
                                                                    \tag{7}
\]

There are two different closed spaces to retain:

* The closure of the graph of U_STCI consists of limits of **supported
  approximants**. The primary-power lemma puts its Hilbert coordinates
  in I^M contained in J contained in I. For general integral C its same
  proof uses delta instead of four: a sole-supported proper CI is
  I-primary, has generic length M, and contains I^{(M)}, hence I^M.
* The top fiber T_M of the graph of **all** containing intersections can
  contain limits reached from residual pairs whose C-multiplicity jumps
  at the boundary. It is potentially larger than the first closure.
  No equality or strictness of these two spaces is asserted.

There is a useful strengthening specifically for full CI graph limits.
Every geometric Hilbert coordinate of the graph of all proper complete
intersections is connected, in every characteristic. To see this, pass
through that graph point by a trait with generic point in U, and write
A for its DVR and K for its fraction field. The proper flat universal
Hilbert family f:Y->Spec(A) has H^0(Y_K,O)=K by the complete-intersection
Koszul resolution. Properness makes B=H^0(Y,O) finite over A; flatness
makes restriction B->K injective. Thus A is contained in B and B is
contained in K. Since A is integrally closed, B=A. Stein factorization
gives geometrically connected fibers; see
[Stacks, Theorem 37.53.4](https://stacks.math.columbia.edu/tag/03H0).
The same argument is recorded in the
[residual-limit geometry](torus_residual_arrangements_and_absorption.md).

Consequently **every Hilbert coordinate of T_M has reduced support C**
in characteristic zero, where its Chow coordinate has the cycle
interpretation established above. Its only one-dimensional support is
C, and any point off C would be an isolated component disjoint from C,
contradicting connectedness. This conclusion does not assert primarity,
absence of embedded points on C, or the exponent bound I^M contained
in J. Those stronger properties remain distinct: in particular the
displayed uniform exponent bound on the supported-approximant closure
uses the primary-power argument before specialization.

An arbitrary Hilbert point with cycle M[C], outside this full CI graph,
can still have isolated points off C invisible to that cycle; the graph
connectedness hypothesis is essential. Every point of T_M over U is an
actual STCI pair by (5).

There is a useful stronger boundary test. Suppose (x,J,[Q^M]) lies in
T_M in characteristic zero. If J belongs to CI_{a,b}, then its
fundamental cycle and unmixedness force sole support C, even if the
displayed equation coordinate x is improper. Thus **any actual CI point
of the top fiber is a genuine supported complete intersection**; the
equation coordinate need not provide its generators. Those generators
can instead be recovered by the theorem of section 3.

More precisely, the Hilbert projection of
\[
 T_M\cap p_H^{-1}(CI_{a,b})                                        \tag{8}
\]
is exactly the set of supported type-(a,b) complete-intersection schemes.
One direction follows from the preceding argument. Conversely, every such
scheme has a proper containing presentation and hence occurs already in
the open graph. Thus nonemptiness of (8) is equivalent to existence of an
actual supported pair of these degrees. The graph incidence itself is not
the original proper-pair locus: it can include improper equation coordinates.

This makes the geometric question on a boundary family precise:
does its top-cycle fiber meet the open locus CI_{a,b}, or is it confined
to its closed complement? A deformation inside that fiber reaching the
open locus would provide a supported pair. A theorem confining the
entire relevant fiber to the complement would exclude that covered
family. Nonzero tangent directions, unobstructedness at a selected
point, or proper-pair deformations leaving the top cycle fiber do not
decide this incidence.

If C is preserved by the torus, chi is equivariant and all of these
filtrations and top fibers are torus invariant. A torus limit of a
supported actual pair stays in the supported-approximant closure,
while its equation coordinate can leave U. The full Hilbert coordinate
retains the prescribed polynomial and endpoint or embedded structure.
No claim that its limiting equations still generate it is made.

## 5. Reach, dependencies, and remaining work

The closed Chow filtration replaces an unproved assertion about
localizing a parameter family at the generic point of C. It organizes
**all** proper degree-(a,b) containing intersections by the exact
residual degree. The Hilbert-polynomial theorem replaces a potentially
unbounded generator search by a degree-a section and the absence of a
fixed surface component in degree b. Neither is a numerical eigenform
restriction or a constant-quotient hypothesis.

The written proofs use the inherited Chow-resultant criterion, ordinary
complete-intersection purity and saturation, the nonvanishing of the
Hilbert polynomial of a nonzero coherent sheaf, and cohomology and base
change. Connectedness of the full graph limits additionally uses the
normal DVR argument and Stein factorization stated above. These proofs
need no new finite computation. The characteristic-zero
interpretation of the triple-graph boundary additionally uses ordinary
flat specialization of cycles; no all-characteristic Hilbert--Chow
functor assertion is made.

What remains is a geometric description or an actual emptiness/nonemptiness
calculation for the top-cycle incidence and its CI open locus, with coverage
of all relevant fixed-degree limits. Exhaustion over unbounded (a,b) is
a separate issue. In particular, closedness of the residual filtration
does not imply that the maximum multiplicity is attained with no residual,
that every supported boundary point is deformable through supported
complete intersections, or that a local deformation globalizes.

**Independent audit, 2026-11-01:** an independent reviewer reconstructed
the Chow filtration, improper-boundary saturation, exact generator criterion,
openness, trait connectedness and top-fiber support arguments. The review
accepted the proper-pair and generator statements in every characteristic,
and the triple-graph cycle interpretation at characteristic-zero geometric
points. It separately checked that (8) has the stated Hilbert projection,
even with improper equation coordinates, and does not claim primarity or
the exponent M for arbitrary top-fiber limits. No finite computation is
needed for these proofs. This remains an exact reduction with no canonical
promotion; it supplies neither a characteristic-zero defining pair for C_0
nor a theorem excluding all such pairs.

A separate bounded reconstruction accepted the single affine-chart argument
for the entire fixed-degree supported ordered-pair and equal-degree pencil
loci, for any integral C in every characteristic. It explicitly preserved
the distinction from the projective closure and from unequal-degree quotient
bundles whose ampleness has not been established.
