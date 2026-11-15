# Global equations, pencils, and constructive mechanisms

Fix C0=[s^4:s^3t:st^3:t^4] in projective three-space over an algebraically closed field. Characteristic zero is the unrestricted research question; characteristic-free assertions are identified below. This chapter consolidates mathematical proofs rather than chronological priorities. The replacement proofs and their characteristic boundaries received independent preservation and mathematical review on 2026-10-31; claims retain the review scopes stated here. The elementary P-labels identify inherited proofs; each claim is used with its stated hypotheses and linked proof.

The common global requirement is an **actual supported pair**. Local regular embeddings, normalized sections, first normal symbols, affine equations, a bundle section, a cycle identity, or a numerical class can each retain only part of that requirement. The useful comparison is the precise implication each supports, including mechanisms that could construct equations.

The [fixed-surface and endpoint algebra](fixed_surface_and_endpoint_algebras.md) preserves the full simultaneous-surface counterexamples, trace tests, two-chart descent and one-endpoint detector. The [finite-pullback and matrix account](finite_pullback_and_matrix_obstructions.md) proves a polarization-lifting obstruction for a specific constructive source and the failure of a universal simple-quadric factorization. The [foliation and affine-degree account](foliation_and_affine_degree_mechanisms.md) retains the normalized foliation alternatives and the two distinct losses at infinity. Imported October 30–31 deductions received independent hand review in their source states; they remain reviewed mathematics. Their review limitations are preserved with each mechanism.

## Geometric orientation: the locus of globally presented multiple curves

The central question is whether a multiple structure supported on C
admits a presentation by two actual projective hypersurfaces. This
can be viewed from several geometric directions, each retaining
different information:

* On the complement U of C, a supported pair is a base-point-free
  pencil of a positive line bundle. Its graph compactifies as the
  blowup of the complete-intersection ideal.
* On a containing surface, the question becomes whether an effective
  multiple of C is a hyperplane-section divisor. Cartier and
  conductor descent determine when that divisor is globally defined.
* In the Hilbert scheme, supported complete intersections form an
  incidence locus inside the space of multiple structures on C.
  The full torus limit remains supported but need not retain two
  minimal generators.
* On the Grassmannian of lines, the Chow form detects the resulting
  fundamental cycle. It does not detect embedded endpoint algebra
  or supply the two equations.

These viewpoints are complementary, not equivalent substitutes for
the missing equations. The results below distinguish exact global
criteria, necessary numerical shadows, and sufficient construction
mechanisms. Their coordinate formulas are certificates for these
geometric statements.

## Characteristic boundaries

The fixed curve is smooth in every characteristic: on x0≠0 its parameter is x1/x0, and on x3≠0 it is x2/x3. The unrestricted characteristic-zero problem differs sharply from positive characteristic, where the fixed embedding has a quartic-carrier STCI in **every** prime characteristic; the complete construction and its exact carrier-degree conclusions belong to the [positive-characteristic construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-a-quartic-carrier).

| Mechanism in this chapter | Actual characteristic scope |
|---|---|
| Unique smooth quadric, type (1,3), three equations, smooth-carrier and quadric-as-equation exclusions | Every characteristic; the cone proof explicitly covers characteristic two. The smooth-carrier discriminant computation is an integer numerical contradiction, not reduction of its coefficients in k. |
| Ordinary affine leading-form boundary, actual complement pencil, Picard/section extension, regular-sequence graph | Every characteristic over algebraically closed k. They are global equation criteria, so positive-characteristic solutions satisfy them too. |
| Chow/resultant sole-support criterion, ordinary K0 quotient, AG-primary thickening criterion | Every characteristic, with properness/purity and arithmetic Gorenstein hypotheses unchanged. The displayed Chow polynomial specializes modulo p; its nonzero unit-coefficient terms prevent it becoming identically zero. |
| Homogeneous coregularity criterion | Every characteristic with the theorem's regular-sequence and higher-vanishing hypotheses; it does not equate ordinary vanishing with existence. |
| Affine lci and projective bundle-section constructions | The cited algebraic constructions apply to the stated lci curve setting over algebraically closed k. Splitting one guaranteed double remains insufficient to cover arbitrary higher thickness in any characteristic. |
| Elementary transform, hull and fixed-Chern-class control | The explicit kernel, cohomology and integer Chern-number argument work in every characteristic. The stated instanton/monad literature application is over C; the smooth-family power-cohomology theorem assumes a characteristic-zero field in its base. |
| Cremona generic transverse multiplicity | Preserved wherever the two ambient maps are inverse near generic points, in any characteristic. The orbifold/topological refinement and the cited bundle-amplification splitting theorem below are characteristic-zero statements. |

These scopes do not extend the characteristic-zero quartic-carrier exclusion to positive characteristic. In characteristic p, Frobenius changes the construction and descent problem: (1+j)^(p^e)=1 once j^(p^e)=0, so a nilpotent-unit obstruction to taking a required power can disappear. Conversely prime-to-p root rigidity survives under its exact hypotheses in the [finite-pullback proof](finite_pullback_and_matrix_obstructions.md#polarization-and-section-lifting).

## The quartic on its unique quadric: divisor classes and carrier geometry

The unique containing quadric is the simplest carrier on which C
becomes a Cartier divisor. Its two rulings expose the asymmetry
between the class of C and the class of a hypersurface section.
This geometry simultaneously explains the three-equation
presentation and why the quadric cannot serve as one of two
set-theoretic defining equations. The smooth-carrier obstruction
extends the same divisor-class viewpoint beyond the quadric.



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
generates the residual line bundle. For homogeneous ideal generation in every degree n≥3, multiply these sections by H0(O_Q(n−3,n−3)): multiplication surjects onto H0(O_Q(n−1,n−3)) by the separate binary-form multiplication maps. Restriction from ambient degree n−3 is surjective. Together with the quadric kernel, this generates all homogeneous equations; degrees below three contribute only the quadric.

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

## Compactifying affine pencils: the boundary at infinity

An affine complete-intersection description need not compactify
to a supported projective complete intersection. The missing
geometric datum is the divisor cut out at infinity: common
leading factors create additional boundary curves. The
coprimality test below is an exact boundary criterion, not
merely a convenient homogenization calculation.



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


## The complement morphism and its graph blowup

Removing C turns a supported pair into a base-point-free
pencil and hence a morphism to the projective line. Conversely,
the positivity and extension properties of the complement
recover global homogeneous equations. The graph blowup is
the natural geometric compactification of this morphism.
This equivalence captures existence exactly but does not
itself construct the required pencil.



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

## The Chow form as a global cycle detector

The Grassmannian of lines supplies a coordinate-free
description of the fundamental cycle of a complete
intersection. Restricting the two hypersurfaces to its
universal line produces a resultant section; its divisor
records the components with multiplicity. This detects
sole support globally while forgetting the special-point
scheme structure, so it is a certificate rather than a
construction of supported equations.



### P-033: the global Chow-resultant certificate

The [exact Grassmannian Hom theorem](chow_bundle_maps.md) proves that
every map between the prescribed bundles below already comes from two
ambient equations. Arbitrary Chow-power determinants use different bundles;
there is no separate multiplication-block lifting condition after the exact
bundle types have been imposed.

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

Consequently, for an integral curve \(C\) of degree \(\delta\), sole support first forces \(\delta\mid ab\). If that divisibility fails, no such supported pair exists. Otherwise assume \(\delta\mid ab\) and \(\lambda\in k^*\); then

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
substituting the six minors.  The exact verifier is [verify_chow_form.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_chow_form.py).  Thus a \((4,5)\) pair must satisfy

\[
 R_{F,G}=\lambda\operatorname{Ch}_{C_0}^{5}.
\]

This is a genuinely global computational representation, independent of the
chosen first-normal frame.  Mathematically it is the classical Chow form of a
complete-intersection cycle, hence a reformulation and certificate rather
than a new existence theorem.

## Why ordinary K-theory sees only degree divisibility

The complement also carries a K-theoretic shadow of a
base-point-free pencil. In this case that shadow reduces
to the Bezout divisibility condition. The calculation
below is useful for identifying the precise limit of
coarse invariants: it cannot distinguish the multiple
structures or endpoint gluing needed for an STCI.



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

## Arithmetically Gorenstein supported thickenings

### P-035: arithmetically Gorenstein thickening criterion

Let \(S=k[x_0,x_1,x_2,x_3]\) and \(P=I_C\).  Then

\[
 C\text{ is an STCI}
\]

if and only if there is a homogeneous \(P\)-primary ideal \(J\) of height two
such that \(S/J\) is a graded Gorenstein ring.

A defining pair gives \(J=(F,G)\), a height-two graded complete intersection. Its Cohen–Macaulay quotient has no embedded associated primes, and its only minimal prime is P; thus J is P-primary, as required.
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

## Homogeneous local cohomology and the second equation

For the homogeneous prime I of a connected projective curve, set M=H_I^2(S), S=k[x0,x1,x2,x3]. Hartshorne–Polini, [Theorem 3.1](https://arxiv.org/html/1907.05472), says that a homogeneous S-regular pair f,g in I has radical I exactly when f,g is coregular on M and H_I^i(S)=0 for i>2. Coregularity means fM=M and g(0:_M f)=0:_M f. Higher vanishing alone is insufficient. Their Corollary 4.6 makes graded quasi-cyclicity necessary; failure of that property would obstruct STCI.

Their Proposition 5.2 identifies a first coregular equation h with affineness of V(h) minus C. Example 5.3(c) treats C0 explicitly: q=x0x3−x1x2 and g=x1^3−x0²x2 are separately coregular, but (g,q) retains a double line and is not a coregular pair. Thus first-element success does not supply the second equation. No computation here establishes codepth two or failure of graded quasi-cyclicity for C0. The full local-cohomology methods and their narrower computations retain their separate owning statements.

## Primary constructions and the projective bundle gap

The [affine/projective scope and exact counterchecks](#affineprojective-scope-and-explicit-literature-counterchecks) retain the lci-cone criterion and the distinct tensor, real-sphere, Picard and failed unique-prime controls. These prevent incorrect source transfers; they provide no projective STCI counterexample.

Forster, [Theorems 5.1–5.2](https://www.mathematik.uni-muenchen.de/~forster/eprints/Compl_inter.pdf), proves respectively that an lci subscheme of affine space with trivial normal bundle is STCI and that every lci affine curve is STCI. The second proof chooses a conormal quotient onto the inverse determinant, adds a Ferrand nilpotent structure, trivializes its conormal bundle on the affine curve, and applies the first theorem. In affine three-space the resulting bundle is free. These are statements about the affine embedding and do not supply the coprime leading forms required above.

Szpiro, [Chapter IV §3, Theorems 1–3, printed pp.71–73](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr62.pdf), proves that an lci codimension-two subscheme of a smooth quasi-projective threefold over an infinite field supports a multiplicity-two zero scheme of a rank-two bundle section. For projective three-space the bundle need not split. Its existence applies to smooth C0; the split target and actual equation compatibility are additional conditions. The double obstruction above concerns that guaranteed multiplicity-two construction, not every possible higher structure.

For conductor descent, the full square and compatible sections are developed in the [fixed-carrier descent proof](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md). Ferrand, [Theorem 2.2](https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf), patches flat/projective modules over A=(A/c)×_(A'/c)A' for finite normalization A⊂A' and conductor c. The exact sequence 0→A→A'⊕A/c→A'/c→0, tensorized by a line bundle, identifies the actual compatibility test. Reduced conductor support or a divisor class upstairs does not replace it.

Eisenbud–Schreyer, [Theorem 1.4](https://arxiv.org/pdf/math/0111040), identifies the determinant divisor of a Chow complex with the Chow divisor of its associated cycle. The universal-line Sylvester construction above is its specialization to a proper pair. Hilbert–Burch gives the codimension-two Gorenstein implication above. These classical inputs construct exact recognition interfaces; they do not supply the missing pair.

## Finite ambient maps and reduced inverse images

There is a characteristic-free dictionary between projective STCIs and
finite maps. For a supported pair of degrees \(a,b\), put \(D=ab\). Then
\[
\Phi=[F^b:G^a:x_0^D:x_3^D]:\mathbf P^3\longrightarrow\mathbf P^3
\tag{FM}
\]
is a finite surjective morphism. Indeed, a basepoint would lie on
\(V(F,G)_{\mathrm{red}}=C_0\), where \(x_0,x_3\) have no common zero.
The pullback of \(O(1)\) is the ample line bundle \(O(D)\); a curve in a
fiber would have degree zero against this bundle, a contradiction.
Properness and zero-dimensional fibers give finiteness, and its image
has dimension three, hence is the whole target. For the target line
\(\ell=V(y_0,y_1)\),
\[
\Phi^{-1}(\ell)=V(F^b,G^a),\qquad
\Phi^{-1}(\ell)_{\mathrm{red}}=C_0.
\]
Conversely the two pullback equations of a line under a finite
endomorphism form a proper intersection with that reduced inverse
image. One may instead use \(D=\operatorname{lcm}(a,b)\) and powers
\(D/a,D/b\). Equalization preserves sole support, although its powers
change the thick scheme and its multiplicity.

More generally, a nonempty pure codimension-\(r\) closed subset
\(X\subsetneq\mathbf P^n\) is an STCI if and only if it is the reduced
inverse image of a codimension-\(r\) linear space under a finite
endomorphism. To prove the forward direction, equalize the degrees of
its \(r\) equations to \(D\), choose \(n+1-r\) linear forms whose common
\(\mathbf P^{r-1}\) misses \(X\), and append their \(D\)-th powers.
A generic such linear space misses \(X\) by the dimension inequality.
The preceding basepoint and ampleness argument proves finiteness.
Conversely, pullback gives \(r\) forms with common zero set of codimension
\(r\), since the finite map preserves the dimension of this inverse
image. In the Cohen–Macaulay polynomial ring these forms are a regular
sequence. This proves the dictionary without a characteristic assumption.

For (FM), the restricted map is
\([s:t]\mapsto[s^{4D}:t^{4D}]\), of degree \(4D\), with target a line.
It does not assert total invariance \(\Phi^{-1}(C_0)=C_0\), or provide
iteration on the same embedded curve. The two added coordinates complete
an existing supported pair to a finite map; they do not remove residual
support from an arbitrary containing pair.

### Ramification of the completed map

In characteristic zero, factoring the four power derivatives by rows
and expanding along the \(x_0,x_3\) rows gives
\[
\det(d\Phi)=\pm abD^2F^{b-1}G^{a-1}x_0^{D-1}x_3^{D-1}
\bigl(F_{x_1}G_{x_2}-F_{x_2}G_{x_1}\bigr).
\tag{FJ}
\]
Its total degree is \(4D-4\). Removing the added power ramification
leaves the factor of degree \(a+b-2\). On \(x_0\ne0\), the base parameter
of the original pencil is \(x_3/x_0\), so this factor is precisely its
relative Jacobian, up to the invertible chart factor. It generates the
[different of the full finite CI pencil](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity),
including its transverse nilpotents. Thus the completed ambient
ramification recovers existing geometric data, rather than an independent
capacity bound. The characteristic-zero ramification comparison is
separate from the characteristic-free finite-map dictionary.

The checked finite-map sources have corresponding realization boundaries.
[Chinburg–Moret-Bailly–Pappas–Taylor, Definition 1.1 and Theorem 1.2](https://arxiv.org/pdf/1201.0678)
complete already supplied ample sections while preserving their zero
supports, so the pair remains input here.
[Poonen, Theorem 2.2](https://math.mit.edu/~poonen/papers/selfmap.pdf)
extends suitably polarized maps to projective space, but extending a
map from \(C_0\) to a line gives containment in its inverse image, without
sole inverse support. [Jamet, Proposition 1.1 and §1.3](https://arxiv.org/pdf/math/0103202)
concerns the full inverse scheme; its section-lifting assertions do not
pass automatically to that scheme's reduction. The iteration used under
[Luo–Meng's total-invariance hypothesis](https://arxiv.org/pdf/2610.10103)
requires \(f^{-1}(V)=V\), absent from (FM). That hypothesis and its use
were checked, rather than the full preprint. These limits leave other
finite-map constructions available. In particular the
[twisted-cubic finite-pullback exclusion](finite_pullback_and_matrix_obstructions.md)
has different polarization and correction-space assumptions and is not
an exclusion of this line-target dictionary.

## Constructive transport and its limits

### Birational transport must transport transverse thickness

[Mella–Polastri, Theorem 1 and Corollary 1](https://arxiv.org/pdf/0906.4858)
give Cremona equivalence of birational embeddings in codimension at least
two. [Ciliberto–Cueto–Mella–Ranestad–Zwiernik, §2.2 and Remark 2.4](https://people.math.osu.edu/cueto.5/CremonaLinearizations.pdf)
give a constructive treatment and a correction to the earlier proof.
These supply a birational transformation of this reduced rational curve
to a line, with both ambient maps defined at the respective general
points. They do not assert transport of complete-intersection equations.

Such an ordinary equivalence is an ambient isomorphism near those general
points. Consequently strict transforms of two divisors cutting out a
reduced CI retain generic intersection multiplicity one. If their proper
intersection in P3 had sole support C, Bézout would force `ab=4`.
Nonplanarity excludes a degree-one factor and the unique containing
quadric excludes two independent quadrics. Taking powers of the same
equations leaves their strict transformed supports unchanged. Thus
linearizing the reduced embedding does not create the required thickening.
This diagnostic does not apply when C is an indeterminacy center, or
exclude transport of a genuinely nonreduced CI.

The alternative blowup link with a conic on V5 is already developed in the
[equation dictionary and support criterion](blowup_residual_geometry.md).
On that common model the actual strict-transform intersection must be
supported on the exceptional divisor E over C. Support on the image
surface in V5 is insufficient: its inverse image also contains the other
exceptional divisor, whose rulings can be genuine residual trisecants
downstairs. Another Cremona model or section-ring presentation does not
solve this existing condition. A viable new construction needs a specified
thickened CI and a reason its pair-dependent exceptional corrections work,
or a construction on a model centered on C supplying those corrections.

## 2. The exact complement equivalence and its topological scope

Put \(U=\mathbf P^3\setminus C\). A supported pair F,G of degrees a,b gives the everywhere defined map
\([F^{b/g}:G^{a/g}]\), \(g=\gcd(a,b)\).
Conversely, a morphism \(U\to\mathbf P^1\) is given by two generating sections of its pulled-back \(\mathcal O(1)\). Regularity and removal of codimension two identify \(\operatorname{Pic}(U)\) with \(\operatorname{Pic}(\mathbf P^3)\), and extend both sections to A,B of \(\mathcal O(n)\). Negative n has no sections; n=0 gives a constant map. For n>0 the common zero set has no divisor component, is nonempty by projective intersection, and lies in C. Its dimension is at least one; irreducibility of C makes its support exactly C.

Each standard affine chart has inverse image \(D_+(A)\) or \(D_+(B)\); these are affine because A,B are positive-degree homogeneous forms and C lies in both zero sets. Consequently this morphism is affine and its surface fibers are affine. This is automatic once the embedded morphism exists, not a further numerical restriction.

For the topological conclusion, first choose irreducible factors F,G that still form a supported pair. This is legitimate: an irreducible factor and the other equation have a nonempty one-dimensional projective intersection contained in C; then choose a factor of the other equation. Write u=b/g, v=a/g, so \(\gcd(u,v)=1\).

Resolve the rational pencil and take its proper Stein factorization. If the finite degree is d>1, the intermediate smooth curve is rational because it is dominated rationally by \(\mathbf P^3\). Thus the rational function \(F^u/G^v\) is a composition R(h) with \(\deg R=d\). Write h as a quotient of coprime homogeneous forms of the same positive degree. Every fiber value of h has a nonempty hypersurface support. Since the zero divisor of R(h) has just the irreducible support F=0, R has a unique zero, totally ramified of order d. The same holds for its pole. Divisorial orders then give \(d\mid u\) and \(d\mid v\), a contradiction. Hence the resolved pencil, and its nonempty open generic fiber in U, are geometrically connected in characteristic zero.

Over \(\mathbf C\), general position makes U simply connected: a real two-dimensional disk filling a loop can avoid the real two-dimensional smooth curve in the real six-dimensional ambient manifold. [Artal Bartolo–Cogolludo, Definition 1.4 and Proposition 1.5](https://arxiv.org/pdf/1002.2097) applies to this smooth quasiprojective source and the connected generic fiber. Its orbifold multiplicity at a point is the gcd of multiplicities of the components of the actual fiber divisor on U. The resulting orbifold sphere must have trivial fundamental group. The standard presentation allows zero or one multiple fiber, or two with coprime multiplicities, and excludes three or more. The two displayed irreducible fibers have multiplicities u,v, consistent with this condition.

The topological proof is stated over C. For fixed algebraic data over another algebraically closed characteristic-zero field, descend to a finitely generated field, embed it in C, and compare geometric fiber multiplicities and connectivity after algebraically closed base extension. No topological assertion about the other field is needed.

The logarithmic differential has its carrier poles inside U. Its pole divisor is not supported only over C on a resolution. The equalized pencil ideal is \((F^u,G^v)\); one must not silently replace its blowup by that of \((F,G)\). The existing exceptional-cover control remains relevant and does not provide a quartic-specific obstruction.

The subsequent distinction from the [two-hyperplane projection, §4](fixed_surface_and_endpoint_algebras.md) also checks out. If Z is the full proper supported CI, its support avoids \(M=V(x_0,x_3)\), and projection \([x_0:x_3]\) is finite flat of degree ab: fibers are proper hyperplane sections of the Cohen–Macaulay curve Z. The reduction is \([s:t]\mapsto[s^4:t^4]\), of degree four, separable in characteristic zero and odd characteristic and purely inseparable in characteristic two. Thus ab is the rank of the full, generally nonreduced fiber algebra, not the degree of a reduced cover. The two marked fibers on C have scheme length four; no separable Riemann–Hurwitz argument applies in characteristic two.

Geometrically, the equivalence describes a pencil whose whole base locus has been absorbed into C. It is a useful dictionary, but constructing this exact complement fibration is already the global existence problem. Multiple-fiber restrictions obtained from its fundamental group add no contradiction to the coprime equalization.

## 3. Homogeneous bundle amplification

Let E have rank two, and let P,Q be globally defined homogeneous polynomial maps to L1,L2 of fiber degrees r,s>0, with no common nonzero zero in any fiber. Use projectivization by **lines**: a line \(kv\subset E_x\) is sent to
\([P(v)^s:Q(v)^r]\) in the lines of \((L1^s\oplus L2^r)_x\).
Both entries scale by \(\lambda^{rs}\), making this well-defined and regular. Fiberwise they are degree-rs binary forms without common roots, so the induced map has degree rs. With the quotient convention the same map is written using E's dual and the target's dual; splitting of E is equivalent to splitting of its dual. There is no convention-dependent change to the conclusion.

[Amerik–Kuznetsova, Theorem 2](https://arxiv.org/pdf/1609.00910) concerns a morphism between **two** projective bundles over the same base; it does not require a self-map. Its base conditions hold on complex projective three-space. Therefore rs>1 forces E to split. If r=s=1, the map E to L1 direct-sum L2 is fiberwise an isomorphism directly.

The characteristic-zero transfer can be made without assuming that an arbitrary field embeds in C. Descend E and the maps to a finitely generated subfield k0 and embed k0 in C. If the resulting E over C is \(\mathcal O(a)\oplus\mathcal O(b)\), its first Chern class determines the same determinant over k0. Hom spaces commute with field extension. The determinant of a proposed homomorphism from this split bundle to E is therefore a scalar polynomial on a finite-dimensional k0-vector space. It is nonzero at the complex isomorphism, hence not identically zero. An infinite field k0 supplies a point where it is nonzero, giving an isomorphism already over k0 and after base change to k. This also verifies the transfer claimed through a splitting criterion in the assessment.

The characteristic-p comparison is correct: for rank-two E on B, relative Frobenius gives a B-morphism \(\mathbf P(E)\to\mathbf P(E)^{(p)}\simeq\mathbf P(F_B^*E)\), with purely inseparable fiber degree p, even if E is nonsplit; see [Stacks, §33.36](https://stacks.math.columbia.edu/tag/0CC6) for relative Frobenius and its degree on geometric fibers. This shows why the characteristic-zero splitting conclusion cannot simply be imported to characteristic p. It does not assert that the target splits or construct two line-bundle-valued equations from a section.

Geometrically, the two polynomial operations would eliminate every unwanted projective direction of E, not merely directions encountered by the particular section. The literature theorem rules out that uniform operation for a nonsplit bundle. It leaves operations with base directions or degeneration away from the section outside its scope. It also does not prove that an arbitrary STCI would arise by this operation from an arbitrary Ferrand bundle.
### Controlled degeneration is a distinct constructive possibility

Forster–Wolffhardt, [Theorem 1.5 and Proposition 1.6](https://www.math.lmu.de/~forster/eprints/zeroschemes.pdf), concern an **affine** scheme X, a rank-two bundle E and section s, with det(E) trivial on Z=Sch(s). They construct ψ,λ,h with ψ(s)+λh=1 and a map Φ=ψ⊗ψ+i(λ):E→E* whose determinant is λ². The transformed section has exactly the same zero scheme: where λ is invertible Φ is invertible, and where λ vanishes the displayed identity makes ψ(s) invertible. This is an actual identity controlling degeneration, not an assumption that all fiber directions can be eliminated.

Its target is E*. On projective three-space, imposing det(E)|Z trivial with Z_red=C0 forces det(E)=O(c) with 4c=0, hence c=0 and E*≅E by the rank-two wedge pairing. That does not split E. A projective transplant also needs the global sections and identity used in the affine proof. An operation into two line bundles with degeneration controlled relative to the particular section remains a possible constructive mechanism; neither the affine theorem nor the homogeneous amplification restriction supplies it.

### An elementary transform along the embedded quartic

There is an explicit sheaf construction that retains the chosen embedding.
Work over \(\mathbf C\) for the instanton and monad applications below, and
write \(i:C_0\hookrightarrow\mathbf P^3\). The sections \(s^7,t^7\) have no
common zero, so they give a surjection and an actual kernel
\[
0\longrightarrow\mathcal F\longrightarrow O_{\mathbf P^3}^{\,2}
\xrightarrow{(s^7,t^7)}i_*O_{\mathbf P^1}(7)\longrightarrow0.
\tag{ET}
\]
Here \(O_{\mathbf P^3}(1)|_{C_0}=O_{\mathbf P^1}(4)\).
At a point of \(C_0\), one of the two coefficients is a unit on the curve.
After a local change of basis the quotient map is reduction of one
coordinate modulo \(I_{C_0}\). Thus
\(\mathcal F\simeq O\oplus I_{C_0}\) locally there. In particular,
\(\mathcal F\) is rank-two torsion-free, is singular along exactly the
embedded curve, and has reflexive hull \(\mathcal F^{**}=O^2\).

For completeness, put \(h=c_1(O_{\mathbf P^3}(1))\). The Hilbert polynomial
of the quotient is
\(\chi(O_{\mathbf P^1}(7+4n))=4n+8\).
A sheaf with Chern character \(d h^2+e h^3\) on \(\mathbf P^3\) has this
polynomial equal to \(dn+2d+e\); hence
\[
\operatorname{ch}(i_*O_{\mathbf P^1}(7))=4h^2,
\quad\operatorname{ch}(\mathcal F)=2-4h^2,
\quad(c_1,c_2,c_3)(\mathcal F)=(0,4,0).
\]
Twisting (ET) by \(-1\), the vanishing of \(H^0(O(-1))\) and
\(H^1(O(-1))\) gives
\[
H^1(\mathcal F(-1))\simeq H^0(\mathbf P^1,O(3)),\qquad h^1=4.
\]
[Jardim–Markushevich–Tikhomirov, Proposition 3.1](https://arxiv.org/pdf/1501.00736)
identifies this as a torsion-free instanton sheaf of charge four: its input
line bundle is \(O_{\mathbf P^1}(-1)\), whose ambient twist by two is
\(O_{\mathbf P^1}(7)\). The construction therefore gives concrete sheaf
geometry on this embedding. It supplies no ideal of a new multiple curve
or its ACM homogeneous coordinate ring.

Two controls specify what changing this construction would require.
A kernel \(\ker(E\to T)\), with \(E\) locally free and \(T\) supported in
codimension at least two, agrees with \(E\) off that support and has
reflexive hull \(E\). Likewise an isomorphism between two locally free
extensions off \(C_0\) extends uniquely across it; the isomorphism and its
inverse extend as sections of reflexive Hom sheaves. This is the
[codimension-two extension property, Hartshorne, Remark 1.8](https://escholarship.org/content/qt4j1747kh/qt4j1747kh.pdf).
It concerns a fixed identification on the complement. It places no
restriction on deformations that change that complement restriction.

Even allowing that change, a flat deformation of this particular sheaf
with its fixed Chern classes cannot be a split rank-two bundle. A split
bundle \(O(r)\oplus O(-r)\) has \(c_2=-r^2\), incompatible with \(c_2=4\).
After a common twist by \(t\), putative split degrees would satisfy
\[
a+b=2t,\qquad ab=t^2+4,
\qquad(a-b)^2=-16.
\]
This is an equality of integer Chern numbers; reducing its coefficients
in the ground field does not remove it. It excludes splitting within this
flat class, while operations changing the Chern classes and other
multiple structures remain possible. The elementary kernel, cohomology
and numerical calculations themselves use no characteristic-zero step;
the stated instanton literature application is over \(\mathbf C\).

### Monad presentations and cohomology in families

A monad retains a useful presentation without making its cohomology a
split target. In the Horrocks construction described by
[Malaspina–Rao, §1, pp.2–3](https://arxiv.org/pdf/2202.00304), a rank-two
bundle \(E\) on \(\mathbf P^3\) is the cohomology of
\[
A\longrightarrow P\longrightarrow B,
\qquad E=\ker(P\to B)/\operatorname{im}A,
\]
where \(P\) splits and
\(\operatorname{rk}P=2+\operatorname{rk}A+\operatorname{rk}B\).
Thus the split middle bundle has extra directions. Obtaining a section
of two line bundles with the desired zero scheme still requires a
construction eliminating those terms and controlling that section.
Neither the monad nor the reflexive-hull calculation performs this step.

A distinct family theorem controls variation of cohomology rather than
constructing such a section. Precisely,
[Ballico–Cid-Ruiz–Singh, Theorem A](https://arxiv.org/html/2602.09201v2)
assumes a Noetherian domain \(A\) containing a characteristic-zero field
and a closed subscheme \(X\subset\mathbf P^n_A\) smooth over \(A\).
For a fixed integer \(j\), a single nonzero element of \(A\) can be inverted
so that every \(H^i(X_t,O_{X_t}(j))\) is flat over that localization,
for every ordinary power thickening \(X_t=V(I_X^t)\) and every \(i\ge0\).
Flatness does not assert that these modules vanish. The theorem does not
cover arbitrary supported ideals or mixed-characteristic specialization.
These distinctions leave meaningful geometric targets: an actual new
multiple-curve ideal, its multiplication and cohomology, and a section
whose zero scheme is controlled. The checked sheaf and monad operations
produce the objects proved above, without deciding realization of those
further targets. Their source applications received scoped independent
review. Independent integration review reconstructed the elementary transform,
Chern and cohomology calculations, checked the monad and generic-flatness
hypotheses, and accepted the preserved realization limits.

### Precise remaining implications

The complement formulation needs an actual morphism on the embedded complement; the affine formulation needs equations with the prescribed ordinary-degree boundary; the bundle formulation needs a split target and support control. Birational transport needs a genuinely thickened source and actual exceptional corrections. Finite pullback can create thickness, but the twisted-cubic source is excluded by the full-scheme polarization theorem in the companion account; it is not exhaustive even in characteristic two. A successful construction may evade one of that theorem's hypotheses. For nonexistence, a necessary condition must be shown to fail for every hypothetical supported pair, not merely for one bundle or selected source.

The [paired-cover construction and its failed node gluing](projection_and_elliptic_gluing.md#8-a-paired-elliptic-construction-clears-the-component-gate-and-fails-node-gluing) and the [contact program](contact_jacobians_and_hamiltonian_actions.md) have their own actual equation/descent obligations. No foliation residue identity, ordinary K0 class, first trace, fixed-surface restriction, or reduced-cover calculation here is a universal obstruction. A next constructive test should specify its source structure and global lifting or correction mechanism; its success need not be known in advance. These proofs retain informative failed shortcuts while leaving both existence and obstruction live.

## Limits of coarse invariants

Ordinary local cohomological dimension does not distinguish this problem: Hartshorne's second vanishing theorem gives \(\operatorname{cd}_S(I_C)=2\) for the homogeneous prime of an integral projective curve over the algebraically closed characteristic-zero field. The sharper homogeneous coregularity and quasi-cyclicity questions above retain more information than this vanishing alone. No failure of quasi-cyclicity for \(C_0\) is established by the bounded ancestor tests.

Constant-coefficient complement topology is likewise compatible with a two-equation presentation. The purity/Gysin calculation for the smooth rational quartic places the checked singular and constant-coefficient étale classes within the degree bound permitted by two principal affine opens. Over \(\mathbf C\), two smooth affine threefold opens and their affine intersection can have union cohomology in degree four by Mayer–Vietoris; a class in that degree is therefore not an obstruction. This limitation concerns those coefficient systems, not every possible invariant of the complement.

The Picard and ordinary \(K_0\) calculations above retain stable classes and Bézout divisibility; they do not decide unstable generation by two sections. Similarly, the required ACM and subcanonical conditions concern a supported multiple structure, rather than forcing the reduced curve to be ACM. The fixed quartic has a nonzero Rao module and nevertheless has actual positive-characteristic STCI presentations. Its Rao module alone therefore cannot be a general STCI obstruction; the characteristic-zero question still needs the actual thickening and homogeneous equations. Binomial exclusions and failure of naive homogenization retain their own exact source/embedding scopes and do not exclude arbitrary homogeneous pairs.


Several questions lie beyond these fixed-curve criteria. Iterating the
successive singularity/blowup analysis in the presence of common singularities
still needs a termination or monotonicity statement with exact hypotheses;
positive-characteristic constructions prevent a characteristic-free
nontermination principle. Extending unibranch plane-projection/Frobenius
descent beyond the fixed rational quartic requires treating several plane
singularities or positive-genus normalization, rather than assuming one
weighted equation suffices. For singular integral curves, smooth-conormal and
regular-center blowup arguments require replacement by normalization and full
conductor data. Over a nonclosed field, descent of geometric STCI to two
ground-field equations is a separate arithmetic question. These are scope
boundaries and questions, with no assertion that the corresponding extensions
have been established.

## The supported Hilbert locus and its full torus boundary

The Hilbert scheme retains the whole ideal of an
intersection under degeneration, including syzygies and
additional initial generators. A torus-fixed limit of a
supported complete intersection is therefore a necessary
boundary object, but it need not remain a complete
intersection. The correct geometric test is whether such
a fixed supported point lies in the closure of the
supported complete-intersection locus, not whether two
eigenforms alone cut it out.



### Invariant support and the full torus limit

Fix \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an
algebraically closed field of characteristic zero, and put \(P=I_{C_0}\).
The torus \(T=\mathbf G_m\) acts by
\((x_0,x_1,x_2,x_3)\mapsto(x_0,tx_1,t^3x_2,t^4x_3)\); its dense orbit
on \(C_0\) is the curve's subtorus in the projective dense torus.
Every hypothetical sole-support pair therefore has a \(T\)-invariant
radical. This does not make its thickening ideal \(J=(F,G)\) invariant.
If that homogeneous CI ideal were invariant, its minimal generators could
be chosen as weight eigenforms, as proved in the
[constant-family argument](tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier).
The [weight theorem](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#the-bound-and-its-exact-large-prime-minimum)
excludes even one weight-homogeneous carrier with an arbitrary mate in
characteristic zero. Thus invariant reduced support is automatic, whereas
an invariant supported CI ideal is excluded. This distinction leaves a
useful degeneration question rather than a reduction to invariant pairs.

For a supported scheme \(Y\), choose \(N\) with
\(P^N\subset I_Y\subset P\). Both containments hold for every torus
translate. Properness of the projective Hilbert scheme gives its full flat
limits, which are \(T\)-fixed; the closed incidence conditions
\(C_0\subset Y_t\subset V(P^N)\) persist there. Thus the full limits
retain support and Hilbert polynomial. They can acquire embedded structure
on \(C_0\); do not replace them by their pure hulls or reduced schemes
when asking about deformation back to the original CI.

The full limit ideal is different from the ideal of the two extreme forms
of \(F,G\). The
[extreme-component theorem](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#extreme-components-of-arbitrary-presentations)
forces those displayed pairs to have common surface factors in this
characteristic-zero setting. Additional initial generators from all
relations retain the full ideal's support and Hilbert data. The
[degeneration boundary](arithmetic_root_collision.md#why-degeneration-does-not-cover-every-pair)
therefore concerns loss of two generators, not a necessary loss of support
by the full Hilbert limit. Neither Cohen--Macaulayness nor AG structure is
assumed at the fixed boundary.

The [sextic residual examples](../arguments/torus_sextic_residuals.md)
make this generator distinction explicit: a proper (6,6) CI has full toric
limit with minimal generator degrees 6,6,10 and the same Hilbert series.
That limit is saturated and ACM. Both it and the original CI retain residual
curves, so this example supplies a full-ideal control without producing a
boundary in the sole-support incidence used here.

The
[full torus-modification account](tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
retains additional endpoint algebras, their finite defects and presentation
data. Its positive-movement and global-presentation barriers remain useful
controls: local equations or an abstract transverse algebra do not supply
the required homogeneous equations after contraction. They do not exclude
all support-preserving deformations of a fixed boundary ideal.

For a specified constant embedded quotient, the
[orbit-family criterion](../arguments/torus_embedded_quotients.md) instead
recovers its saturated image and its actual degree spaces directly. Properness
and degree exhaustion give an exact CI test for that image. This does not
replace the moving finite family of a hypothetical characteristic-zero
sole-support pair.

### Proposed test: supported deformations of an invariant boundary ideal

**Proposed research direction; not a solved deformation problem.** Fix
degrees \((a,b)\), the CI Hilbert polynomial they determine, and an integer
\(N\). Work in the closed Hilbert incidence
\(C_0\subset Y\subset V(P^N)\) with that polynomial. Starting from an
actual \(T\)-fixed ideal in this incidence, ask whether a flat deformation
inside the incidence reaches a homogeneous AG, equivalently codimension-two
CI, ideal. The [primary/Gorenstein criterion](#2-p-035-the-homogeneous-primarygorenstein-criterion-survives-audit)
states the precise homogeneous condition; if the prescribed degrees matter,
the actual minimal generators must also have degrees \((a,b)\).

This is a bounded interface with two different possible aims. Realizing the
boundary ideal as the full initial ideal, or torus-orbit limit, of a supported
CI is stronger than finding an arbitrary supported flat deformation to a
CI. The latter is already constructively useful: its general fiber would
give actual equations without a prescribed orbit history. Neither aim is
settled by the existence of invariant supported schemes. No finiteness of
the fixed locus, classification of its ideals, or smoothing theorem is
assumed. A fixed \(N\) covers only the declared incidence; a claim about
all pairs needs a justified power bound or an explicit coverage argument.

A useful first task needs an actual boundary ideal with its complete
generators and embedded structure, then actual deformation maps preserving
the containments and Hilbert polynomial. Tangent weights can suggest
directions but do not integrate them, preserve support to all orders, or
prove entry into the CI locus. Stop at an exact supported CI deformation,
a covered exclusion of a specified boundary family, or an identified
missing deformation or generator condition. A calculation at one fixed
ideal does not exclude other fixed ideals or components.

[Bertone–Cioffi–Orth–Seiler, Corollaries 5.5 and 6.18](https://www.mathematik.uni-kassel.de/~seiler/Papers/PDF/Loci.pdf)
give open AG and strict-CI loci and constructive recognition algorithms.
Openness does not preserve these conditions at a flat boundary. Applying
the algorithms constructively here still requires an actual boundary
ideal and a support-constrained deformation with the needed generators.
[Hattori–Zanardini, Theorem A.1](https://ems.press/content/serial-article-files/50397)
passes from Chow stability of an already proper equal-degree CI to
stability of its generating system. It supplies no converse preservation;
their Corollary 4.5 gives stable systems with a common hypersurface factor.
Thus stability alone does not even ensure proper intersection. A fixed
Chow cycle also omits the embedded nilpotent algebra. These checked
applications retain their source's characteristic-zero setting and do
not exclude a support-preserving construction with controlled equations.

A separate affine proof correction is already covered by the
[exact Mandal–Zinna audit](#exact-audit-of-arxiv251107589v1-step-3)
and its stronger, independently proved real-sphere counterexample.
In arXiv:2511.07589v1, Theorem 4.2 Step 3, tensoring the Serre sequence
ends in \(J/cJ\), rather than the image ideal \(J/(c)\). For \(c\in J\)
there is a further exact sequence
\[
0\longrightarrow(c)/cJ\longrightarrow J/cJ
\longrightarrow J/(c)\longrightarrow0.
\]
If \(c\) is a nonzerodivisor, its omitted term is \(A/J\), by multiplication
by \(c\). The linked audit gives the full explicit witness
\(J=(x,y),c=x\), including the failed middle exactness, in every
characteristic. There is also a distinct global-generation control:
\(x(1-x),y\) give a basis of \(J/J^2\), but their zero set has the extra
line \(x=1,y=0\). A conormal basis only gives the required local
information at primes containing \(J\). This latter example does not
refute invertibility of the image ideal; the tensor/kernel identification
is the proof failure. The stronger preprint claims are not imported as
patching theorems. Its narrower published conditional results, the
classical affine-space theorem and the actual affine quartic equations
retain their separate scopes. No new counterexample to projective STCI
over an algebraically closed field follows.

The pre-existing finite-map, flat-boundary and affine-source statements
retain their recorded scoped source reviews and consolidation review.
The supported-deformation formulation above is a proposed investigation,
not a new theorem or a completed boundary calculation.
Independent scope review on October 31, 2026 accepted this expanded exposition
and its linked strategy/navigation changes against the existing proof owners.
It checked support versus ideal invariance, full limits versus extreme forms,
retained embedded data, fixed-family coverage and the unresolved deformation
and generator conditions. No material finding remained; no new mathematical
computation or deformation-existence claim was part of that review.

## Primary complement obstructions and actual sections

The [complete section-obstruction account](complement_section_obstructions.md) proves the continuous rank-two criterion on the complement of any smooth connected complex space curve and the twisted Chow-Witt comparison over an algebraically closed field of characteristic different from two. For the positive split bundles relevant to equations, the checked primary classes impose only degree divisibility. Hartogs identifies actual algebraic or holomorphic sections with homogeneous pairs, while the nonplanar low-degree control shows that the primary conditions do not realize them. The complement is nonaffine, so affine splitting and representability results do not close that gap.

## Historical mixed-weight sextic negative control (exact identities)

This is a finite geometric control, not an unrestricted STCI obstruction. In the affine normal coordinates `c_0=-u`, `c_2=(t^3+u)^3-t(t^4+tu+q)^2`, set `f=c_0^2+c_2^2+q c_0`. Its quadratic normal form is
\[
4t^{10}q^2-(4t^{11}+1)qu+(1+t^{12})u^2.
\]
The discriminant is `1+8t^11-16t^10`, of degree eleven, and `gcd(4t^11+1,t^12+1)=1`. Thus the generic quadratic normal cover is nonsplit in this example. On the quadric `q=0`, after writing `w=t^3+u`, the restriction factors as `(w-t^3)^2(w^4+1)`; the residual ruling lines `w^4=-1` are generically smooth because the `w`-derivative there is `4w^3(w-t^3)^2`. The elementary numerical identity `2*3^2-7*3+8=5` is only a degree-gap check. None of these identities produces a supported pair.


### Archived exact certificate: `research/computations/stci_game_existence_2026_10_30.m2`

Original source preserved verbatim, including its limitations and external dependencies. This is an archival transfer, not a new proof audit.

<details><summary>Historical source</summary>

```macaulay2
-- Existence advocate: explicit elliptic degree-two inverse source.
-- Exact coefficient field Q(i), not a characteristic-zero STCI claim.
K0=QQ[symbol iv]; K=toField(K0/ideal(iv^2+1));
R=K[symbol yy,symbol xx,MonomialOrder=>Lex];
relE=ideal(yy^2-xx^3+xx);
phi=xx^2+2*iv*xx-1+2*(1+iv)*yy;
AA_num=yy+1-iv; AA_den=xx-iv;
funBasis={1_R,xx,yy,xx^2,xx*yy,xx^3,xx^2*yy,xx^4};
monBasis=join(apply(toList(0..8),rr->xx^rr),apply(toList(0..6),rr->xx^rr*yy));
vec=ff->apply(monBasis,mm->sub(coefficient(mm,ff%relE),K));
sections={}; coefficientsSections={};
scan({0,1,3,4},jj->(
 cols=apply(funBasis,ff->vec(ff*AA_den^jj));
 mat=transpose matrix cols;
 rhs=transpose matrix {vec(phi*AA_num^jj)};
 sol=solve(mat,rhs);
 assert(mat*sol==rhs);
 ffun=sum(toList(0..7),kk->sub(sol_(kk,0),R)*(funBasis#kk));
 assert((ffun*AA_den^jj-phi*AA_num^jj)%relE==0);
 sections=append(sections,ffun);
 coefficientsSections=append(coefficientsSections,apply(toList(0..7),kk->sol_(kk,0)));
 print("SECTION_J="|toString jj|" FUNCTION="|toString ffun);
));
Z=K[symbol Z0,symbol Z1,symbol Z2,symbol Z3];
quadBasis={Z0^2,Z0*Z1,Z0*Z2,Z0*Z3,Z1*Z2,Z1*Z3,Z2*Z3,Z3^2};
VV=apply(coefficientsSections,cc->sum(toList(0..7),kk->sub(cc#kk,Z)*(quadBasis#kk)));
qE0=Z0*Z3-Z1^2;
qE1=Z2^2-Z1*Z3+Z0*Z1;
print("GLOBAL_QUADRICS="|toString VV);
print("ELLIPTIC_MARKED_CURVE_IDEAL="|toString ideal(qE0,qE1));
print "EXACT_QUADRATIC_LIFTS_OF_ELLIPTIC_DEGREE_TWO_SOURCE_PASS";
-- First actual fixed input, checking basepoints before any contact search.
muValue=2_K;
UU=VV;
Smu=qE1+sub(muValue,Z)*qE0;
BP=saturate(ideal(Smu)+ideal UU,ideal gens Z);
print("FIXED_INPUT_MU="|toString muValue|" RHO={0,0,0,0}");
print("PROJECTIVE_BASEPOINT_IDEAL="|toString gens BP);
print("BASEPOINT_FREE="|toString(BP==ideal 1_Z));
assert(BP==ideal 1_Z);
smoothS=saturate(ideal(Smu)+ideal apply(gens Z,zz->diff(zz,Smu)),ideal gens Z);
assert(smoothS==ideal 1_Z);
print "FIXED_SOURCE_SMOOTH_QUADRIC_PASS";
-- Q0=1 covers every projective point off Gamma, with two scalar choices.
pullC={UU#0*UU#3-UU#1*UU#2,(UU#1)^3-(UU#0)^2*UU#2,
 (UU#1)^2*UU#3-UU#0*(UU#2)^2,(UU#2)^3-UU#1*(UU#3)^2};
extra=ideal(Smu,qE0-1)+ideal pullC;
print "OFF_GAMMA_TEST_START"; flush stdio;
extraGB=gb extra;
print("OFF_GAMMA_DIMENSION="|toString dim(Z/extra));
print("OFF_GAMMA_DEGREE="|toString degree(Z/extra));
assert(dim(Z/extra)==0 and degree(Z/extra)==24);
print "OFF_GAMMA_AFFINE_LENGTH_24_PROJECTIVE_LENGTH_12_PASS";
print "FIXED_INPUT_FULL_INVERSE_TEST_COMPLETED";

-- The normalization-degree condition is separate from full inverse support.
Target=K[symbol W0,symbol W1,symbol W2,symbol W3];
Source=Z/ideal(Smu);
imageMap=map(Source,Target,apply(UU,ff->sub(ff,Source)));
print "IMAGE_DEGREE_TEST_START"; flush stdio;
imageIdeal=ker imageMap;
print("IMAGE_IDEAL_GENERATOR_DEGREES="|toString degrees gens imageIdeal);
print("IMAGE_DEGREE="|toString degree(Target/imageIdeal));
print("FINITE_MAP_GENERIC_DEGREE="|toString(8//degree(Target/imageIdeal)));
print "FIXED_INPUT_IMAGE_DEGREE_TEST_COMPLETED";
assert(numgens imageIdeal==1 and degree(Target/imageIdeal)==8);
imageF=first flatten entries gens imageIdeal;
KT=K[symbol tt]; N=KT[symbol nn,symbol mm];
normalF=(map(N,Target,{1_N,sub(tt,N),(sub(tt,N))^3+nn,(sub(tt,N))^4+mm})) imageF;
normalExps=apply(terms normalF,ff->first exponents ff);
normalOrder=min apply(normalExps,ee->sum ee);
print("FIXED_CARRIER_GENERIC_NORMAL_ORDER="|toString normalOrder);
assert(normalOrder==2);
firstCoeffs=apply({{2,0},{1,1},{0,2}},ee->sub(coefficient(nn^(ee#0)*mm^(ee#1),normalF),KT));
polyRem=(ff,gg)->(rr:=ff;dg:=first degree gg;ggLead:=sub(leadCoefficient gg,K);vv:=first gens ring ff;while rr!=0 and first degree rr>=dg do (dr:=first degree rr;cc:=sub(leadCoefficient rr,K)/ggLead;rr=rr-sub(cc,ring ff)*vv^(dr-dg)*gg);rr);
polyMonic=ff->if ff==0 then ff else ff*sub(1_K/sub(leadCoefficient ff,K),ring ff);
polyGCD=(ff,gg)->(aa:=ff;bb:=gg;while bb!=0 do (rr:=polyRem(aa,bb);aa=bb;bb=rr);polyMonic aa);
finiteBase=polyGCD(firstCoeffs#0,polyGCD(firstCoeffs#1,firstCoeffs#2));
finiteBase=polyMonic finiteBase;
print("FIRST_SYMBOL_FINITE_COMMON_FACTOR_DEGREE="|toString first degree finiteBase);
print("FIRST_SYMBOL_FINITE_COMMON_FACTOR="|toString finiteBase);
KS=K[symbol ss]; NI=KS[symbol ni,symbol mi];
infinityF=(map(NI,Target,{(sub(ss,NI))^4+mi,(sub(ss,NI))^3+ni,sub(ss,NI),1_NI})) imageF;
infinityCoeffs=apply({{2,0},{1,1},{0,2}},ee->sub(coefficient(ni^(ee#0)*mi^(ee#1),infinityF),KS));
infinityCommon=polyGCD(infinityCoeffs#0,polyGCD(infinityCoeffs#1,infinityCoeffs#2));
infinityOrder=0;
while sub(infinityCommon,{ss=>0})==0 and infinityCommon!=0 do (infinityCommon=infinityCommon//ss; infinityOrder=infinityOrder+1);
print("FIRST_SYMBOL_INFINITY_COMMON_FACTOR_ORDER="|toString infinityOrder);
verticalDegree=first degree finiteBase+infinityOrder;
print("FIRST_SYMBOL_TOTAL_VERTICAL_FACTOR_DEGREE="|toString verticalDegree);
print("HORIZONTAL_EXCEPTIONAL_ROOT_BIDEGREE="|toString(18-verticalDegree,2));
print "FIXED_CARRIER_FIRST_NORMAL_GEOMETRY_COMPLETED";
polyQuot=(ff,gg)->(rr:=ff;qq:=0_(ring ff);dg:=first degree gg;gl:=sub(leadCoefficient gg,K);vv:=first gens ring ff;while rr!=0 and first degree rr>=dg do (dr:=first degree rr;cc:=sub(leadCoefficient rr,K)/gl;term:=sub(cc,ring ff)*vv^(dr-dg);qq=qq+term;rr=rr-term*gg);assert(rr==0);qq);
horizontalCoeffs=apply(firstCoeffs,ff->polyQuot(ff,finiteBase));
rootDisc=(horizontalCoeffs#1)^2-4*(horizontalCoeffs#0)*(horizontalCoeffs#2);
rootDisc=polyMonic rootDisc;
sqC=polyGCD(rootDisc,diff(tt,rootDisc));sqW=polyQuot(rootDisc,sqC);oddPart=1_KT;sqIndex=1;
while sqW!=1 do (sqY=polyGCD(sqW,sqC);sqZ=polyQuot(sqW,sqY);if sqIndex%2==1 then oddPart=oddPart*sqZ;sqW=sqY;sqC=polyQuot(sqC,sqY);sqIndex=sqIndex+1;);
print("HORIZONTAL_ROOT_DISCRIMINANT_ODD_PART_DEGREE="|toString first degree oddPart);
print("HORIZONTAL_ROOT_NORMALIZATION_GENUS="|toString((first degree oddPart-1)//2));
assert(first degree oddPart==3 or first degree oddPart==4);
print "HORIZONTAL_ROOT_IRREDUCIBLE_ELLIPTIC_DOUBLE_COVER_PASS";
extraU0Nonzero=(extra+ideal(UU#0)==ideal 1_Z);
print("EXTRA_INVERSE_HAS_NO_TARGET_INFINITY="|toString extraU0Nonzero);
ExtraRing=Z/extra;
u0Extra=sub(UU#0,ExtraRing);u1Extra=sub(UU#1,ExtraRing);
hPull=sum(toList(0..12),jj->sub(sub(coefficient(tt^jj,finiteBase),K),ExtraRing)*u1Extra^jj*u0Extra^(12-jj));
assert(hPull==0);
print "VERTICAL_FACTOR_VANISHES_ON_FULL_EXTRA_INVERSE_SCHEME_PASS";
print "EXISTENCE_SOURCE_FIXED_INPUT_AND_NORMAL_GEOMETRY_EXACT_CHECKS_PASS";
```
</details>


## Consolidated historical supplement: `research/supplements/AFFINE_PROJECTIVE_AND_LITERATURE_LIMITS.md`

# Affine/projective scope and explicit literature counterchecks

These proofs separate homogeneous projective equations from affine equations, a line-bundle condition on the curve from a divisor-class condition on a carrier, and an embedded lifting problem from a splitting claim. They preserve useful mathematical counterexamples from a bounded literature assessment. The precise preprint audit concerns **arXiv:2511.07589v1**, Theorem 4.2 Step 3 and the unrestricted Theorem 4.4 as formulated in that version; it is not a claim about an uninspected later revision. No counterexample below is asserted to settle projective STCI over an algebraically closed field.

The established affine lci and projective bundle-section constructions, with theorem-level primary sources, are integrated in [the global-equations account](../synthesis/global_equations_and_constructions.md). The fixed quartic has an [explicit quartic-carrier construction in every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier); that fact needs no unverified transfer from a broad affine theorem.

## What the positive-characteristic literature actually supplies

Moh's [official abstract](https://doi.org/10.1090/S0002-9939-1985-0784166-1) states affirmative results for projective monomial curves in positive characteristic and, separately, for a curve admitting a birational linear plane projection with center **disjoint from the curve** and only cusps in its image. The bounded source assessment verified the publisher's indexed abstract, not the full proof, a theorem number or a generalized meaning of cusp. In particular it supplied no theorem asserting that every projective curve admits such a projection. The internal cuspidal projection in [the rational-quartic construction](../supplements/RATIONAL_QUARTICS_IN_POSITIVE_CHARACTERISTIC.md) is instead justified by its own full proof.

The earlier Barile–Morales–Thoma [2000 publisher abstract](https://doi.org/10.1006/jabr.1999.8195) states a constructive positive-characteristic STCI theorem for simplicial affine or projective toric varieties **with full parametrization**. Neither hypothesis may be discarded; the abstract-level assessment did not verify the detailed definition needed for a new application. The direct fixed-quartic application in [the construction chapter](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) uses the independently verified 2002 article instead.
 The same 2000 abstract separately reports weaker almost-STCI results in arbitrary characteristic; those statements are not converted here into STCI assertions or results for arbitrary projective curves.

Published Mandal–Zinna papers and the audited preprint have distinct scopes. The [J. Algebra 690 (2026), 101–113 abstract](https://doi.org/10.1016/j.jalgebra.2025.10.042) concerns affine threefolds over characteristic-zero C1 fields, with trivial conormal and a torsion Grothendieck-class hypothesis. The separate [J. Algebra 693 (2026), 36–53 abstract](https://doi.org/10.1016/j.jalgebra.2025.12.026) concerns a conditional smooth-affine-surface result over the algebraic closure of a finite field, again with trivial conormal and a torsion Grothendieck-class hypothesis. These abstract-level scope assessments do not establish any projective transfer. The counterchecks below address specific displayed claims and proof steps of arXiv:2511.07589v1; they do not conflate those claims with either published conditional theorem.

Cowsik–Nori, *Affine curves in characteristic p are set theoretic complete intersections*, Invent. Math. 45 (1978), 111–114, is the classical affine statement: a pure affine curve in affine n-space in positive characteristic is set-theoretically cut out by n−1 equations. The inherited assessment verified the [publisher record](https://doi.org/10.1007/BF01390268); it did not inspect the full proof. This recorded affine scope is not a projective or homogeneous-cone theorem. Applying an affine-surface lci theorem to the two-dimensional cone over a projective curve requires lci at the cone vertex, which is exactly the failure isolated by the next proof. A same-support affine pair also need not be homogeneous or have the required support at infinity. A search that fails to locate a universal projective theorem is not itself proof of its absence.

## The lci affine-surface theorem and its missing cone hypothesis

Das, *On a conjecture of Murthy*, Adv. Math. 331 (2018), 326–338, [Theorem 4.2 in the author manuscript](https://oldweb.isical.ac.in/~mrinal/Murthy_CI_v2.pdf), proves that a height-\(d-2\) locally complete-intersection ideal in \(\overline{\mathbf F}_p[X_1,\ldots,X_d]\), \(d\ge4\), is an STCI. Theorem 4.1 first constructs a same-support lci thickening with free conormal; at \(d=4\) the proof produces a rank-two projective module and uses Quillen–Suslin to make it free. The primary statement and this proof structure were checked in the inherited source assessment. This is an affine-space theorem with an lci hypothesis, not an assertion for arbitrary projective curves or arbitrary singular cones. [Publisher record](https://doi.org/10.1016/j.aim.2018.04.012).

## Exact obstruction to applying affine surface theorems to the cone

This is proved here and needs no literature extension.

Let `S=k[x0,x1,x2,x3]`, let `m=(x0,x1,x2,x3)`, and let `I` be the homogeneous prime ideal of an integral projective curve. If `I_m` is lci, it has two minimal generators because its height is two in the regular local ring `S_m`. The minimal number of generators equals

`dim_k(I/mI)`.

This is also the number of minimal homogeneous generators of `I`. Hence `I` has two homogeneous generators, so the projective curve is already a scheme-theoretic complete intersection. Thus the affine cone of every projective curve that is not a scheme-theoretic CI fails the lci hypothesis at the vertex. Smoothness of the projective curve does not fix this failure. For example, the twisted cubic is smooth, but its cone ideal has three quadratic minimal generators.

Even an affine same-support pair need not be homogeneous. A further argument is required to supply two homogeneous equations or to control the hyperplane at infinity.

## Exact audit of arXiv:2511.07589v1, Step 3

The source location is Theorem 4.2, Step 3, displayed sequence following equation (1); in the browser HTML it is lines 343--350. The problem is the substitution of `J/(c)` for the actual tensor quotient `J/cJ`.

Test the claimed operation on a complete intersection, over any field:

```
A = k[x,y,z],       J = (x,y),       c = x,
P = A^2,
f(1) = (-y,x),      g(a,b) = ax+by.
```

The sequence `0 -> A -> P -> J -> 0` is exact. Put `B=A/(x)=k[y,z]`. The preprint's proposed sequence with last term `J/(x)` becomes

```
B -> B^2 -> (y) -> 0,
t |-> (-yt,0),       (a,b) |-> by.
```

Its middle kernel is `B(1,0)`, while the preceding image is `yB(1,0)`. The middle homology is `B/(y)`, which is nonzero. Therefore that displayed sequence is not exact, even for this simplest CI ideal.

The actual tensor quotient has an extra torsion summand:

`J/xJ = (x,y)/(x^2,xy)`,

and the class of `x` is nonzero but annihilated by `y`. The natural quotient from `J/xJ` to `J/(x)` kills this summand. If the paper's notation `J/(c)` were instead interpreted as `J/cJ`, its assertion that this module is locally free of rank one would fail in the same example. Neither interpretation repairs the splitting step.

This is an exact algebraic countercheck of the proof, not an argument from parallel agreement or from the theorem's surprising breadth.

## Independent refutation of the unrestricted CI claim

This elementary example is proved here; it is outside the user's algebraically closed-field setting and is used solely to test the preprint's explicit *arbitrary Noetherian ring* claim.

Let

`A = R[x,y,z]/(x^2+y^2+z^2-1)` and `I=(x,y,z-1)`.

The algebra is a smooth two-dimensional real affine algebra, and `I` is the maximal ideal at the north pole. It is lci of height two. In `I/I^2`, the sphere equation gives `2(z-1)=0`, so `I/I^2` has basis the classes of `x,y` and is free of rank two over `A/I=R`.

Suppose `I=(f,g)`. On the real sphere `S^2`, the smooth map `F=(f,g):S^2 -> R^2` then has exactly one zero, the north pole. Since the two generators give a basis of `I/I^2`, its derivative at this zero is invertible, so the local winding number is `+1` or `-1`.

Here is a direct contradiction without invoking an Euler-class computation. On `R^2 \ {0}`, the form

`alpha = (u dv-v du)/(u^2+v^2)`

is closed. Remove a small disk around the north pole from `S^2`; `F^*alpha` is a smooth closed form on the remaining compact surface. Stokes's theorem forces its integral on the boundary to be zero. The invertible derivative forces that same integral to be `+2*pi` or `-2*pi`. Thus `I` cannot have two generators. It is lci with free conormal but is not a CI.

This disproves the preprint's unrestricted Theorem 4.4. It does not give a counterexample to projective STCI over an algebraically closed field.

## Why finite-field torsion does not settle the projective problem

Hartshorne--Polini, *Divisor class groups of singular surfaces*, [primary arXiv full text](https://arxiv.org/html/1301.3222), Proposition 7.1: if a curve meets the singular locus of its carrier surface only finitely, it is STCI on that surface precisely when `r[C]=m[H]` in `APic(X)` for positive integers `r,m`.

An elementary fixed-carrier counterexample to an overbroad torsion inference is a ruling line `L` on a smooth quadric `Q=P^1 x P^1`, over `Fpbar` or any algebraically closed field. Here `Pic^0(Q)=0`, `Pic(Q)=Z^2`, `[H]=(1,1)`, and `[L]=(1,0)`. There are no positive `r,m` with `r(1,0)=m(1,1)`. Thus `L` is not STCI on this chosen quadric, despite complete torsion of `Pic^0(Q)`. Of course the line is STCI in the ambient `P^3` using two planes. The example isolates the gap: finding a suitable carrier with the required full divisor-class relation remains additional work.

Kollar--Lieblich--Olsson--Sawin, *The Zariski topology, linear systems, and algebraic varieties*, [authors' book PDF](https://williamsawin.com/ReconstructionBook.pdf), Definition 7.1.1 and Theorem 7.1.10, prove that over a locally finite perfect field every irreducible curve has SCIP. In that terminology SCIP means that every finite closed subset of the curve can be obtained by intersecting the curve with an ambient effective divisor. It does not mean that the curve is the intersection of two ambient surfaces. The finite-field torsion used there concerns line bundles on the curve and cutting finite subsets. This theorem therefore supplies no hidden affirmative answer to the user's projective space-curve problem.


The tensor-quotient countercheck is an exact algebraic calculation in every characteristic. The real-sphere counterexample uses real topology and tests only the arbitrary-Noetherian-ring CI assertion. The fixed-quadric Picard obstruction holds over every algebraically closed field. These scopes remain distinct from each other and from the open fixed-quartic characteristic-zero question.


## The failed unique-prime inference in arXiv:2209.04489v1

Vahap Erdoğdu, *Radically finite rings and space curves*,
<https://arxiv.org/abs/2209.04489>, v1 submitted 2022-09-09, has no later version
in the inspected arXiv history. Its abstract and Corollary 4.4 assert that space
curves are not always STCI. The full proof is directly accessible at
<https://arxiv.org/html/2209.04489>, section 4, Theorem 4.3 and Corollary 4.4.
The corollary concerns the affine polynomial ring in three variables; it is not
an explicit integral projective-curve construction.

The theorem's argument first establishes a unique maximal ideal above an ideal
generated by two elements, then tries to establish that it is the unique
**prime** ideal above that ideal. The decisive inference is that a contraction
which is a G-ideal makes the prime above it maximal. The G-ideal condition gives
the existence of a maximal ideal with that contraction; it does not identify
every prime above the contraction with that maximal ideal.

### An elementary counterexample to that exact inference — PROVED HERE

Let k be any field and

\[
R=k[x,y]_{(x,y)},\qquad A=R[T].
\]

Then R is a finite-character UFD of dimension two: it is local, with unique
maximal ideal M=(x,y). In the displayed construction in the proof choose

\[
\Pi_1=x,\quad \Pi_2=y,\quad z=1-y,\quad f=T,
\quad g=y+(1-y)T.
\]

These choices satisfy every relation used there, including \(\Pi_2+z=1\).
The element 1-y is a unit of R. Consequently

\[
P^*=(x,g)\subset A
\]

is prime, because elimination of T gives

\[
A/P^*\simeq R/(x)\simeq k[y]_{(y)},\qquad
T\longmapsto-\frac{y}{1-y}.
\]

It has height two. It is properly contained in the height-three maximal ideal

\[
M^*=(x,y,T).
\]

For example y is nonzero in the displayed quotient, so y is not in P*. Since
P* is already prime,

\[
\sqrt{(\Pi_1,g)}=P^*\ne M^*.
\]

At the same time the quotient is local, so M* **is** its unique maximal ideal;
the paper's intermediate statement about the intersection of maximal ideals
holds in this example. This isolates the exact failure: a unique maximal ideal
does not make the smaller defining prime maximal. No appeal to computation is
needed.

The contraction \(P^*\cap R=(x)\) also satisfies the existential property of a
G-ideal used in the paper: the distinct maximal ideal
\((x,yT-1)\) of A contracts to (x), with quotient k(y). That existence does not
change the nonmaximal prime P* above the same contraction.

**Scope.** This disproves a particular implication in the proof, so the
negative-resolution corollary is unsupported by that proof. It does not prove
that every affine space curve is STCI, or that the theorem's whole statement is
false under every possible interpretation of “radically finite.” Searches did
not find a correction or a refereed replacement proof.



## Consolidated historical supplement: `research/supplements/FOUNDATIONAL_FRONTIER_AND_INCIDENCE.md`

# Quadric powers, normal directions and incidence controls

Consolidated research material, including open questions and source assessments.

---

<a id="2026-10-05-foundational-frontier-audit"></a>

## Independent foundational audit and strategic boundaries

Date: 2026-10-05. Scope: P-029, P-035, the uniform smooth-quadric power
algebra, and the positive-characteristic constructions P-012/P-014/P-028.
This is an independent proof audit; it does not resolve the unrestricted STCI
problem. The dedicated positive-characteristic audit and fixed-carrier
refinement are recorded separately in
`2026-10-05-positive-quartic-carrier-optimality.md`.

### Audit outcomes

| Claim | Outcome | Essential boundary |
| --- | --- | --- |
| P-029, complement morphism | Verified | The complement has codimension two, and the curve is integral; a nonconstant map really has positive pullback degree. |
| P-035, graded Gorenstein thickening | Verified | Graded Gorenstein includes Cohen--Macaulayness; local Gorensteinness alone is insufficient. |
| Smooth-quadric power equality | Verified | The explicit multiplication/lifting argument is necessary; sheaf exactness alone would not establish saturation. |
| P-012/P-014, positive characteristic | No mathematical gap found in dedicated independent audit | Covers smooth rational quartics and the specified cuspidal carriers, rather than arbitrary projective curves. |
| P-028, explicit quartic cone | Verified and sharpened | A new exact mate-degree minimum is available on this fixed carrier; it is a carrier-specific result. |
| Broad ACM literature assertion | Source scope unresolved | The original source inspected proves the monomial ACM class. A broad modern survey statement does not reconstruct that broader original proof. |

### 1. P-029: the complement morphism equivalence survives audit

Let C be an integral projective curve, U=P3 minus C, and let
f:U -> P1 be nonconstant. Since P3 and U are regular and the omitted subset
has codimension two, divisor localization identifies Pic(U) with Z,
generated by O_U(1). Hence f*O(1)=O_U(d). The two coordinate sections cannot
exist if d<0 and are constants if d=0: Hartogs extension gives
H0(U,O_U(d))=H0(P3,O(d)) for every d. Thus d>0.

The two coordinate sections extend to homogeneous forms F,G of degree d.
Their common zero set is contained in C. A common irreducible factor would
give a hypersurface inside C, so none exists. Consequently (F,G) has height
two and is a regular sequence. Its projective zero scheme is nonempty and
purely one-dimensional. An integral curve has no proper closed
one-dimensional subset, so the support is C.

In the converse direction one first gives an STCI pair equal degrees by
powers. A constant [F:G] would force proportional forms and a hypersurface
support, impossible. The resulting base ideal is a complete-intersection
ideal and is of linear type. Its Rees graph therefore has exactly the
bihomogeneous equation uG-vF=0, without an extra component.

No missing assumption was found. The integrality of C is used in the final
support argument; an extension to reducible curves would have to ensure
that no component of C is omitted. The criterion is exact but does not make
the existence of a map automatic: regular functions on U are only constants,
and a nonconstant map to P1 has precisely the original homogeneous base-locus
problem.

### 2. P-035: the homogeneous primary/Gorenstein criterion survives audit

Suppose F,G cut out C set-theoretically in projective space. Their common
factor is impossible, so J=(F,G) is a homogeneous height-two complete
intersection. There is no extra cone component supported only at the vertex:
the radical of J is the affine-cone prime P=I_C, since the vertex is already
in that cone. A complete intersection is unmixed. With its sole minimal
prime P it is therefore P-primary, and S/J is graded Gorenstein.

Conversely, if a homogeneous P-primary height-two ideal J has graded
Gorenstein quotient, it is perfect of grade two. A minimal Hilbert--Burch
resolution has ranks (mu(J)-1, mu(J), 1). The Cohen--Macaulay type is
mu(J)-1, because the last differential is minimal and dualizing the
resolution produces that number of minimal canonical-module generators.
Type one forces mu(J)=2. The two homogeneous generators form a regular
sequence and have radical P.

This proof does not conflate a locally Gorenstein multiple curve with an
arithmetically Gorenstein curve. For an lci projective thickening X, the
useful equivalent formulation is to demand both an isomorphism
omega_X=O_X(t) and vanishing of its full Rao module
H1(P3,I_X(n)) for every n. That conjunction gives the graded Gorenstein
property. Merely producing a transverse Gorenstein algebra or a
subcanonical multiple structure leaves the global cohomology condition
unresolved.

### 3. The smooth-quadric ordinary/symbolic power theorem survives audit

Let Q be a smooth quadric and C an integral Cartier divisor of type (a,b),
1<=a<=b. Write I for the saturated homogeneous prime ideal. Smoothness of C
is not needed, because (q,t) is still a local regular sequence in P3 whenever
t cuts out C on the smooth Q. For sheaf powers one has

    0 -> I_sheaf^(m-1)(d-2) --q--> I_sheaf^m(d)
      -> O_Q(d-am,d-bm) -> 0.

The local colon identity and reduction modulo q justify both sides of this
sequence. In degree b the quotient sections lift to b-a+1 ambient forms
T_i because H1(P3,O(b-2))=0. Their m-fold products span
H0(Q,O(m(b-a),0)) in every characteristic: use a monomial basis, with no
binomial-coefficient division. For d>=bm, multiply them by ambient
degree-(d-bm) forms, which surject to O_Q(d-bm,d-bm). For d<bm the
quotient has no sections. Thus every quotient section lifts in the ORDINARY
power I^m. Induction after subtracting such a lift proves

    (I^m)_d = H0(P3,I_sheaf^m(d))

for every integer d, hence saturation of every power.

Off the cone vertex the prime is a complete-intersection prime in a regular
ring. Its associated graded algebra is polynomial over its domain quotient,
so these local powers have no embedded primes. The only remaining possible
embedded prime is the irrelevant maximal ideal, excluded by saturation.
Consequently each I^m is I-primary and equals I^(m).

The verifier `computations/verify_quadric_powers.m2` passed freshly under
`/opt/homebrew/bin/M2 --script`, checking C0 through m=6 and two other
quadric divisor examples through m=4. These computations corroborate the
uniform proof; they are not its induction.

This removes hidden symbolic generators from arbitrary-order calculations
for C0, but does not turn a primary ideal into a two-generated ideal.
Indeed the checked C0 power quotients remain non-Cohen--Macaulay. Nor does
finite generation of the symbolic Rees algebra invoke the dimension-three
local Cowsik result in the dimension-four homogeneous coordinate ring.

### 4. P-012/P-014: positive-characteristic hinge audit

The dedicated worker audited P-012 and P-014 without changing their proofs;
the parent then reread both complete arguments. No gap was found.

For P-012, separable degree-three ruling maps have different of degree four
by Riemann--Hurwitz, including wild characteristic two. A ramified fiber
therefore has shape 2R+P or 3R. Inseparable degree three can occur only in
characteristic three and supplies 3R directly. The projection center removes
exactly one base point: smooth immersion supplies a hyperplane vanishing to
order one there, and hyperplanes separate every other point from the center.
The residual linear system is consequently basepoint-free of degree three.
Its image is not a line, so its map to a plane cubic is birational.

The singleton nonimmersive fiber over R was checked separately in both
ramification cases. For triple contact, the local coefficient v2 is in the
span of v1, which makes the projected derivative vanish in every
characteristic. The plane cubic's total delta-invariant is one, so this
unibranch singularity uses the whole singularity budget. The characteristic
three alpha term in the cusp normal form is essential; for 3 nonzero the
coordinate substitution removes it, including in characteristic two.

The weighted cubic-cone normalization is finite and birational with singleton
geometric fibers, hence a universal homeomorphism. Since h(P) is nonzero,
the graph equation lz-h is irreducible. Its weighted closure includes exactly
the vertex over the projection center. All binary coefficients of its
3p-th power descend in the standard cusp case, because the only missing
binary exponent is one and every exponent is divisible by p. In the
nonclassical characteristic-three case, the explicit s9,t9 identities give
the needed descent. These checks yield the homogeneous degree-(3,4p) pair.

P-014's repaired three-case necessity argument was also checked: when l is a
multiple of t, smooth immersion forces the st3 coefficient of h to be
nonzero. It is the z^(N-1) coefficient that exposes the missing semigroup
monomial in that case. In the nonclassical cusp, the single top-coefficient
relation cuts the binary section space by codimension one; the degree-piece
dimension verifies sufficiency, and it excludes exponents three and six
while allowing nine. The minima are carrier-specific.

The positive-quartic descent verifier uses SymPy. None of the arguments imports a degree bound uniform in characteristic, and no characteristic-zero specialization is implied.

### 5. Source audit: the broad ACM assertion should remain qualified

The author's uploaded original Robbiano--Valla article
*On set-theoretic complete intersections in the projective space* (1983),
DOI [10.1007/BF02924906](https://doi.org/10.1007/BF02924906), was inspected at
[the author full text](https://www.researchgate.net/publication/225984491_On_set-theoretic_complete_intersections_in_the_projective_space).
Its introduction distinguishes positive-characteristic monomial curves
from characteristic-zero monomial projectively Cohen--Macaulay curves.
Section 4 fixes a monomial parametrization before Proposition 2 asserts the
ACM-to-STCI implication. Thus that proposition cannot be quoted for an
arbitrary ACM space curve.

[D'Cruz's Theorem 2.7](https://arxiv.org/html/2003.09101v1) does literally
state the broader implication and cites Robbiano--Valla and
Stueckrad--Vogel. The full original LNM 997 chapter and the cited
Stueckrad--Vogel proof were not recovered. This audit therefore does not
claim the broad assertion false. It does establish that the main report's
unqualified attribution is stronger than the original proof inspected here.
Until the missing original proof scope is checked, use the modern statement
with an explicit source qualification, or restrict the proved positive class
to ACM monomial space curves. No result in this audit depends on the broader
assertion.

The current-open-status source
[Hartshorne--Polini](https://arxiv.org/html/1907.05472v1) was checked freshly
and retains the general question. A retrieval attempt for the 2026 Murayama
notes returned an internal browsing error, so this audit does not claim a
fresh full-text verification of those notes. The repository's previous
dated verification remains separate evidence.

### 6. Exact fixed-carrier improvement and continuation recommendation

For P-028's quartic cone, the dedicated audit derives the full allowable
mate-degree set in characteristic p, with the resulting minimum:

    p=2: 4 divides N, minimum 4;
    p=3: 3 divides N, minimum 3;
    p=5: 25 divides N, minimum 25;
    p>=7: p divides N, minimum p;
    characteristic zero: no mate.

The proof uses the finite birational weighted normalization

    P(1,1,4) -> V(x0*x3^3-x2^4),
    [s:t:z] -> [s^4:z:s*t^3:t^4].

C0 pulls back to the single Cartier curve z-s^3*t=0. A degree-N mate must
pull back to a scalar multiple of (z-s^3*t)^N. Lucas's theorem singles out
the coefficient indexed by p^(v_p(N)); its membership in the normalization
subring is equivalent to p^(v_p(N)) belonging to the semigroup <3,4>.
The separate note supplies the complete proof and exact small-prime controls.
This is an internal proof, with no novelty claim; the characteristic-zero
carrier exclusion also overlaps Thoma's broader one-binomial-carrier
theorem.

An adversarial second proof audit checked the weighted normalization in
all characteristics, the implication from projective support to the single
affine polynomial factor, the nonzero coefficient of z^(N-r), and both
directions of the semigroup criterion. It found no gap. In particular,
arbitrary non-binomial mates are covered by the pullback argument.

The most useful broad organizing condition remains P-035: every proposed
local structure must eventually supply global ACMness and homogeneous
Gorensteinness. For the rational quartic, use the verified arbitrary-order
quadric power algebra to parameterize equations, while retaining all higher
jets and vertical defects. Leading forms, a finite pole-stratum list, or a
local Gorenstein fiber cannot supply that final global test. The new fixed
cone result is a rigorous positive-characteristic control for any proposed
uniform obstruction.


---

<a id="2026-10-05-literature-new-routes"></a>

## Literature refresh and a uniform quadric-curve power algebra

Date: 2026-10-05. This note is independent of the shared ledgers. It records
source scopes, a newly reconstructed uniform lemma, reproducible checks, and
the limits of the resulting route. No unrestricted STCI conclusion is claimed.

### 1. Literature status and genuinely stronger existing exclusions

#### General problem and the Macaulay quartic

The checked primary sources still retain the general connected/integral
projective-space-curve problem and the characteristic-zero Macaulay quartic
as open. In particular, Takumi Murayama's 2026 MA665 notes explicitly retain
the Macaulay curve as an open example:
<https://www.math.purdue.edu/~murayama/ma665.pdf>.
The intended parametrization is the usual quartic; the repeated final `s^4`
in the displayed four-dimensional linear system is a typographical error.
The 2019 Hartshorne--Polini primary paper remains useful for its actual
coregularity criteria:
<https://arxiv.org/html/1907.05472v1>.
A search on 2026-10-05 found no subsequent unrestricted resolution. This is
a dated search conclusion, not a proof of absence of unindexed work.

#### Mandal--Zinna: version and affine scope checked again

<https://arxiv.org/abs/2511.07589> still lists only v1, submitted 2025-11-10,
and no journal reference. Its abstract asserts a broad theorem for lci
height-two ideals in rings of dimension three. It is distinct from the
published conditional theorem in Journal of Algebra 690 (2026), 101--113,
DOI <https://doi.org/10.1016/j.jalgebra.2025.10.042>.
The published result requires an affine algebra over a characteristic-zero
C1 field, free conormal module, and torsion Grothendieck-group class; its
ring-level variant assumes freeness of stably free rank-three modules.
Neither theorem controls projective infinity, and the homogeneous coordinate
ring has dimension four. No projective transfer is inferred.

#### Thoma's ONE-binomial-carrier theorem

A stronger classical exclusion than the ledger's two-binomial-equation
warning is available. Apostolos Thoma, *Monomial Space Curves in P3_k as
Binomial Set Theoretic Complete Intersections*, Proceedings AMS 107 (1989),
55--61, DOI <https://doi.org/10.1090/S0002-9939-1989-0976361-7>, Theorem 3.1,
proves in characteristic zero that a smooth monomial space curve other than
the twisted cubic cannot be an STCI on any binomial carrier. Here the mate
is allowed to be an arbitrary homogeneous polynomial. Thus BOTH carriers of
any characteristic-zero pair for C0 must be nonbinomial.

The original article, uploaded by its author, was checked at
<https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections>;
its institutional record is
<https://olympias.lib.uoi.gr/jspui/handle/123456789/13047>.
The official AMS PDF returned HTTP 403 through the browsing tool, so the
original author-uploaded theorem is the checked full-text evidence.

A useful limitation: torus degeneration does not extend this theorem to
arbitrary carriers. A flat limit of a complete-intersection thickening need
not remain a two-generated complete intersection; extra initial generators
and/or common factors of the two initial forms can appear. Properness of a
Hilbert scheme does not make its complete-intersection locus proper.

#### The broad ACM assertion deserves source-level qualification

Clare D'Cruz, arXiv:2003.09101v1, Theorem 2.7 literally states the broad ACM
space-curve assertion used by the repository:
<https://arxiv.org/html/2003.09101v1>.
Thoma's 1993 primary preprint also lists the assertion, but in a discussion
restricted to monomial curves:
<https://archive.mpim-bonn.mpg.de/948/1/preprint_1993_86.pdf>.
The original Robbiano--Valla chapter was not accessible in full through the
publisher. Thoma's 1989 original introduction explicitly attributes to them
ACM **monomial** space curves. These facts do not disprove the broader
statement, but the original-proof scope has not been reconstructed in this
lane. The safe record is that a modern survey states it, while the original
monomial source chain is narrower. None of the mathematics below uses the
broad assertion.

#### A recent discrepancy invariant does not solve this support problem

Bengus-Lasnier--Rangachev, *The Complete Intersection Discrepancy of a Curve I:
Numerical Invariants*, arXiv:2504.09362v1:
<https://arxiv.org/html/2504.09362v1>.
Its residual-intersection formulas assume a containing complete intersection
Z that agrees with X at the generic points of X. That hypothesis is exactly
what fails for a nontrivial STCI thickening. For smooth C the local intrinsic
discrepancy vanishes already, while a nonreduced CI supported on C may still
have arbitrary generic multiplicity. Therefore the new invariant should not
be imported as an obstruction to STCI support without a new nonreduced
extension. The existing formulas are useful for residual curves, not an
unconditional way around the thick-carrier frontier.

### 2. Uniform theorem for integral curves on a smooth quadric

**PROVED HERE; independent adversarial proof audit completed.** No novelty
claim is made. The monomial special case is classical in Morales--Simis
(1992), and the uniform geometric argument below is particularly convenient
for nonmonomial and singular integral curves.

Let k be algebraically closed, of arbitrary characteristic. Let
Q = V_+(q) be a smooth quadric in P3, identified with P1 x P1, and let C be an
integral divisor of class (a,b), with 1 <= a <= b. Let I be its saturated
homogeneous prime ideal. Then, for every m >= 1,

    I^m = (I^m)^sat = I^(m).

In particular the symbolic Rees algebra is the ordinary, finitely generated
Rees algebra. Smoothness of C is unnecessary: an integral divisor on the
smooth surface Q is Cartier, and its embedding in P3 is locally a complete
intersection away from the affine-cone vertex.

#### Proof with the lifting step made explicit

Write script-I for the ideal sheaf of C. For every m and d there is a sheaf
exact sequence

    0 -> script-I^(m-1)(d-2) --q--> script-I^m(d)
      -> O_Q(d-am,d-bm) -> 0.                         (1)

At a point of C choose local equations (q,t), where t defines C in Q.
The identities `(q,t)^m:q=(q,t)^(m-1)` and
`(q,t)^m mod q=(t^m)` prove (1), including its kernel. Away from C the same
sequence is immediate.

At m=1,d=b, the quotient is O_Q(b-a,0). Since H1(P3,O(b-2))=0,
degree-b forms in I lift its full section space. Choose lifts
T_0,...,T_(b-a) of a monomial basis of H0(O_Q(b-a,0)).
Their m-fold products span H0(O_Q(m(b-a),0)) in every characteristic.
There is no division by a characteristic-dependent binomial coefficient.

For d<bm the right-hand term of (1) has no global sections. For d>=bm put
n=d-bm. Ambient degree-n forms surject onto H0(O_Q(n,n)), and monomial
multiplication gives the surjection

    H0(O_Q(m(b-a),0)) tensor H0(O_Q(n,n))
        -> H0(O_Q(d-am,d-bm)).                         (2)

Consequently every section of the quotient in (1) has an explicit lift in
the ORDINARY power I^m. This matters: sheaf exactness alone would not prove
surjectivity on global sections.

Inductively suppose all sections of script-I^(m-1)(d-2) lie in the ordinary
power. Subtract the lift just constructed from a section of script-I^m(d).
The difference is q times a section of the preceding sheaf power, hence
belongs to I^m. Starting with m=0 proves
H0(script-I^m(d))=(I^m)_d in every degree, which is precisely saturation.

Off the cone vertex, I is a prime lci ideal. Its associated graded ring is
locally a polynomial algebra over the domain S/I, so its powers are locally
I-primary. All possible embedded associated primes are therefore supported
at the vertex. Saturation excludes that associated prime. Thus I^m is
I-primary, and localization at I gives the symbolic-power equality.

The ruling-line case (a=0 or b=0) is separately a two-linear-form complete
intersection and also has the equality. The proof above is for a,b>0.

#### Literature connection

Morales--Simis, *Symbolic powers of monomial curves in P3 lying on a quadric
surface*, Communications in Algebra 20 (1992), 1109--1121,
DOI <https://doi.org/10.1080/00927879208824394>, treats the monomial quadric
case. A later original article explicitly recalls its Proposition 2.3 as
normal torsion-freeness for a monomial curve on xy-wz:
<https://citeseerx.ist.psu.edu/document?doi=7e63dd655dbc886de78bc22d6d0b3229da3ec6f0&repid=rep1&type=pdf>.
The author publication list verifies the earlier paper:
<https://www-fourier.univ-grenoble-alpes.fr/~morales/publications-web-Marcel-Morales2014.pdf>.
The exact uniform scope of the 1992 proof was not read in full, so this note
labels its general statement as proved by the displayed argument, with
classical overlap explicitly acknowledged.

### 3. Consequences usable at arbitrary normal order

#### Exact carrier lower bound and recursive spanning

If F vanishes to normal order at least m along C and is not divisible by q,
then deg F >= bm. At equality, F restricted to Q is a linear combination of
m-fold products of the chosen T_i, modulo q I^(m-1).
Every form of arbitrary normal order is described recursively by these
products and q times the preceding power. For the rational quartic a=1,b=3,
this extends the repository's degree-six symbolic-square picture uniformly
to every normal order; there are no additional hidden symbolic generators.

The theorem says nothing about termination of the infinitely-near common
zero set of a pair. In particular, it does not repair a tangent-only blowup
recurrence. Positive-characteristic pairs remain mandatory controls.

#### Exact Hilbert function

Surjectivity in (1) gives, with binomial and product terms interpreted as zero
when their required degrees are negative,

    dim (I^m)_d = binom(d-2m+3,3)
       + sum(j=1..m) h0(O_Q(d-2m+(2-a)j,
                           d-2m+(2-b)j)).             (3)

For C0 this becomes

    dim (I^m)_d = binom(d-2m+3,3)
       + sum(1<=j<=m, 2m+j<=d)
           (d-2m+j+1)(d-2m-j+1).                    (4)

The first non-q-divisible degree is 3m, and the corresponding quotient has
dimension 2m+1. In particular m=2 gives the known 23-dimensional sextic
space, with 18-dimensional q-divisible kernel and five-dimensional quotient.

### 4. Exact computation and reproducibility

The companion M2 script `research/computations/verify_quadric_powers.m2` checks C0 powers
m=1,...,6 over QQ and the formula (4) over a range of degrees. It also checks
the analogous (1,4) monomial quintic and a nonmonomial (2,4) quadric divisor.
The finite computations are consistency checks; the theorem is the argument
above, rather than an extrapolation from those checks.

For C0 the observed Betti totals of S/I^m are

    (1, (m+1)^2, 2m(m+1), m^2).

Thus ordinary and symbolic powers coincide while the quotients remain
non-Cohen--Macaulay. Finite generation alone cannot invoke a height-two
projective STCI theorem: the local Cowsik dimension-three result changes its
equation count in dimension four, and stronger CM-symbolic-power criteria
need additional hypotheses that these powers fail.

### 5. Research reassessment

The new structural information removes one source of uncertainty from
arbitrary-order normal calculations and can reduce high-order carrier spaces
to concrete q/product data. It is a useful uniform algebra, not a global
obstruction. The strongest additional literature restriction is that both
carriers for C0 must be nonbinomial in characteristic zero. A new investigation
should use these facts to formulate pair-dependent higher-jet or valuation
conditions, rather than expect finite generation, a torus limit, or a
reduced-discrepancy invariant to settle the problem.


---

<a id="2026-10-06-localcoh-incidence"></a>

## Exact finite quartic incidence specification and recovered direction certificate

Date: 2026-10-06. Status: **EXACT COMPUTATION / FIXED-DIRECTION EXCLUSION**.
The full quartic incidence remains unresolved here. A later same-day certificate
extends the fixed-direction result below to the entire normalized parity
family; see `2026-10-06-localcoh-parity-dual.md`. This note concerns the
characteristic-zero monomial quartic C0 and the targets u,v in the existing
local-cohomology frontier. No universal STCI assertion follows.

### 1. Reproduced coordinates

For S=QQ[x,y,z,w], put q=xw-yz, A=x²z-y³, B=xz²-y²w,
C=yw²-z³ and I=(q,A,B,C). The existing finite-principal-part argument reduces
quartic ancestors to E4[-7], where E4=Ext²(S/I⁴,S), of dimension30. The exact
injection into Ext²(S/(q⁴,B⁴),S) represents these sections by 30 homogeneous
degree13 numerators, modulo (q⁴,B⁴).

The script `../computations/localcoh-incidence-tensor.m2` was rerun on Oct6.
Both previously saved outputs regenerated byte-identically:

- `localcoh-incidence-tensor.txt`: SHA256
  `05702619ef67a6fed4420e24a5530eccb18e4700d8e1f1ba5cae89b7899cc60b`.
- `localcoh-incidence-bases.txt`: SHA256
  `ee3e320f240b77c370ad21704c97aeec12b619f55c6ad8aff829aef9235d8dcc`.

The quartic basis has18 elements. Its products with the30 ancestors span the
entire74-dimensional E3[-3] piece. Appending the two target numerators
xz(qB)³ and yw(qB)³ does not enlarge that span. These are exact rational rank
computations, not samples.

A degree17 remainder in the fixed quotient initially gives277 occurring
ambient monomials. Exact row-space compression gives74 equations and a
74×542 rational matrix R. Its first540 columns are products. Column18i+j
is the product of ancestor i with quartic j, for i=0,...,29 and j=0,...,17.
The last two columns are precisely the standard vectors e72,e73, using
zero-based row indices. These coordinate conventions are checked by the
Oct6 Python verifier.

### 2. The complete finite incidence, including its open rank conditions

For a=(a0,...,a29), define the74×18 linear matrix

    L(a)[r,j] = sum_i R[r,18i+j] ai.

The complete finite quartic problem is exactly the affine incidence

    L(a) f = e72,     L(a) g = e73,

in30 ancestor coordinates and two18-coordinate multiplier vectors. This is
148 bilinear equations in66 variables, including two nonzero constant
right sides. Consequently a=0 is automatically excluded; no extra
saturation is needed merely to remove the zero ancestor. The basis of E4
already imposes the I⁴-annihilator/support condition, unlike searching all
of the diagonal Cech quotient.

Write N(a) for the first72 rows of L(a), and P(a) for its final two rows.
Existence of f,g is equivalent to

    P(a): ker N(a) -> QQ² being surjective,

or, equivalently,

    rank L(a) = rank N(a) + 2.

Thus rank N(a)≤16 is necessary. The exact projective constructible locus in
P29 is the union of the strata r=0,...,16 with

    rank N(a)=r,     rank L(a)=r+2.

Each stratum requires all (r+1)-minors of N to vanish, some r-minor of N
nonzero, and some (r+2)-minor of L nonzero. For r=0 the nonzero0-minor
condition is vacuous. Discarding these open conditions produces a larger
closed locus and cannot by itself settle incidence. In particular, a
vanishing-minor computation on N alone is not a full incidence exclusion.

Scaling a by a nonzero scalar is absorbed by reciprocal scaling of f,g,
so this specification is naturally projective in the ancestor. Every
solution is ambient-coprime by the separately established low-degree
ancestor exclusion; coprimality is not assumed in the matrix encoding.

### 3. Recovered polynomial dual for a surviving pure-top direction

Use the balanced normal frame and divided-power top-symbol coordinates
c_i[t^j] with i=0,...,3 and j=0,...,7. The checked top map M has shape32×30,
rank29 and a one-dimensional kernel, represented by

    k4=1/4,   k13=-3/4,   k18=1,

with all other k_i zero. These are zero-based coordinates.

Consider the primitive degree2 normal-dual direction

    nu=(1+t²,-2t),

whose homogeneous pair (s²+t²,-2st) is coprime. Its pure cubic symbol with
coefficient h=1 is in the top image. Its coefficient h=t is outside the
image: the augmented top matrix has rank30. Hence this direction admits
exactly a one-dimensional nonzero top-coefficient space. Normalize that
coefficient to1. Every ancestor with this top symbol is then

    a(c)=a*+c k,

where the nonzero entries of a* are

    a0=8/3, a3=-4/3, a8=12, a9=-8, a14=8/3,
    a17=8/3, a27=12, a28=2, a29=1.

Let L0=L(a*) and L1=L(k). The recovered rational vectors n0,n1 of length74
are stored in `localcoh-incidence-2026-10-06-certificate.json`. They satisfy

    n0^T L0 = 0,
    n0^T L1 + n1^T L0 = 0,
    n1^T L1 = 0,

and

    n0^T e72=1, n1^T e72=0,
    n0^T e73=8/11, n1^T e73=0.

Thus n(c)=n0+c n1 satisfies, identically over QQ[c],

    n(c)^T L(a(c))=0,
    n(c)^T e72=1,    n(c)^T e73=8/11.

Neither target lies in the quartic multiplication image for any value of c,
even over an algebraic closure. This excludes every quartic multiplier for
this entire ancestor line. A nonzero scalar multiple of the top symbol
reduces to the same line by scaling the ancestor and multipliers, so the
exclusion holds for all nonzero top coefficients for this fixed direction.

The verifier `../computations/localcoh-incidence-2026-10-06.py` checks these
identities using Python's standard library and exact rational arithmetic;
it needs no Groebner computation. It also checks hashes, basis-coordinate
agreement with the top map, the unique top line, and the two target columns.
The original discovery used two small one-target Groebner computations,
which returned the unit ideal. The saved dual is a directly checkable
certificate of that result.

### 4. Audit boundary and unfinished attempts

A tempting incorrect multiplication test uses `basis(4,I)` and multiplies its first row alone by ancestor numerators. Macaulay2 represents this basis in the
four ideal-generator coordinates: the first row contains coefficient
polynomials, not the actual quartic forms. Correct forms require summing
all four generator products. The incorrect products have degrees14 or15,
so their degree17 target coefficient functionals vanish vacuously. Such coefficient tests do not establish full-family multiplication exclusions. The tensor exporter audited here uses the correct
sum over all four generators. A corrected full-family test belongs to a
separate computation and is not inferred from the fixed-direction result.

An exploratory full148-equation/66-variable Groebner attempt had produced
no certificate or usable ideal result. It was interrupted during the Oct6
bounded recovery. No mathematical conclusion is drawn from that attempt.

Continuation should work from the exact tensor and the rank-stratum
specification, together with verified top-direction classifications. The
present certificate settles one non-ruling degree2 direction; it does not
settle all degree0,1,2 directions or the full quartic locus.

Validation: Macaulay2 1.26.06 reran the tensor exporter successfully;
standard-library Python reran the Oct6 certificate verifier successfully.
