# Global equations, pencils, and constructive mechanisms

Fix C0=[s^4:s^3t:st^3:t^4] in projective three-space over an algebraically closed field. Characteristic zero is the unrestricted research question; characteristic-free assertions are identified below. This chapter consolidates mathematical proofs rather than chronological priorities. The replacement proofs and their characteristic boundaries received independent preservation and mathematical review on 2026-10-31; provisional claims remain provisional. It does not promote a canonical result or settle existence. The elementary P-labels identify inherited proofs; canonical result records remain the authority for promoted claims.

The common global requirement is an **actual supported pair**. Local regular embeddings, normalized sections, first normal symbols, affine equations, a bundle section, a cycle identity, or a numerical class can each retain only part of that requirement. The useful comparison is the precise implication each supports, including mechanisms that could construct equations.

The [fixed-surface and endpoint algebra](fixed_surface_and_endpoint_algebras.md) preserves the full simultaneous-surface counterexamples, trace tests, two-chart descent and one-endpoint detector. The [finite-pullback and matrix account](finite_pullback_and_matrix_obstructions.md) proves a polarization-lifting obstruction for a specific constructive source and the failure of a universal simple-quadric factorization. The [foliation and affine-degree account](foliation_and_affine_degree_mechanisms.md) retains the normalized foliation alternatives and the two distinct losses at infinity. Imported October 30–31 deductions received independent hand review in their source states; they remain reviewed provisional mathematics. Their review limitations are preserved with each mechanism.

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

## Rational quartic geometry and elementary carrier obstructions

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

## Affine equations and the projective boundary

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


## Complement pencils and positive line bundles

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

## Chow determinant and the sole-support certificate

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
substituting the six minors.  The exact verifier is [verify_chow_form.py](../computations/verify_chow_form.py).  Thus a \((4,5)\) pair must satisfy

\[
 R_{F,G}=\lambda\operatorname{Ch}_{C_0}^{5}.
\]

This is a genuinely global computational representation, independent of the
chosen first-normal frame.  Mathematically it is the classical Chow form of a
complete-intersection cycle, hence a reformulation and certificate rather
than a new existence theorem.

## Ordinary K-theory and its precise limitation

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

The [affine/projective scope and exact counterchecks](../supplements/AFFINE_PROJECTIVE_AND_LITERATURE_LIMITS.md) retain the lci-cone criterion and the distinct tensor, real-sphere, Picard and failed unique-prime controls. These prevent incorrect source transfers; they provide no projective STCI counterexample.

Forster, [Theorems 5.1–5.2](https://www.mathematik.uni-muenchen.de/~forster/eprints/Compl_inter.pdf), proves respectively that an lci subscheme of affine space with trivial normal bundle is STCI and that every lci affine curve is STCI. The second proof chooses a conormal quotient onto the inverse determinant, adds a Ferrand nilpotent structure, trivializes its conormal bundle on the affine curve, and applies the first theorem. In affine three-space the resulting bundle is free. These are statements about the affine embedding and do not supply the coprime leading forms required above.

Szpiro, [Chapter IV §3, Theorems 1–3, printed pp.71–73](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr62.pdf), proves that an lci codimension-two subscheme of a smooth quasi-projective threefold over an infinite field supports a multiplicity-two zero scheme of a rank-two bundle section. For projective three-space the bundle need not split. Its existence applies to smooth C0; the split target and actual equation compatibility are additional conditions. The double obstruction above concerns that guaranteed multiplicity-two construction, not every possible higher structure.

For conductor descent, the full square and compatible sections are developed in the [carrier/conductor account](carrier_conductor_socle_interfaces.md). Ferrand, [Theorem 2.2](https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf), patches flat/projective modules over A=(A/c)×_(A'/c)A' for finite normalization A⊂A' and conductor c. The exact sequence 0→A→A'⊕A/c→A'/c→0, tensorized by a line bundle, identifies the actual compatibility test. Reduced conductor support or a divisor class upstairs does not replace it.

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

## Flat limits, generator conditions and affine source scope

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
[degeneration boundary](../supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#why-degeneration-does-not-cover-every-pair)
therefore concerns loss of two generators, not a necessary loss of support
by the full Hilbert limit. Neither Cohen--Macaulayness nor AG structure is
assumed at the fixed boundary.

The provisional [sextic residual examples](toric_sextic_residuals_and_limits.md)
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
[orbit-family criterion](toric_quotients_and_endpoint_descent.md) instead
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
CI, ideal. The [primary/Gorenstein criterion](../supplements/FOUNDATIONAL_FRONTIER_AND_INCIDENCE.md#2-p-035-the-homogeneous-primarygorenstein-criterion-survives-audit)
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
[exact Mandal–Zinna audit](../supplements/AFFINE_PROJECTIVE_AND_LITERATURE_LIMITS.md#exact-audit-of-arxiv251107589v1-step-3)
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
not a new theorem or a completed boundary calculation; no canonical result
is promoted.
Independent scope review on October 31, 2026 accepted this expanded exposition
and its linked strategy/navigation changes against the existing proof owners.
It checked support versus ideal invariance, full limits versus extreme forms,
retained embedded data, fixed-family coverage and the unresolved deformation
and generator conditions. No material finding remained; no new mathematical
computation or deformation-existence claim was part of that review.

## Primary complement obstructions and actual sections

The [complete section-obstruction account](complement_section_obstructions.md) proves the continuous rank-two criterion on the complement of any smooth connected complex space curve and the twisted Chow-Witt comparison over an algebraically closed field of characteristic different from two. For the positive split bundles relevant to equations, the checked primary classes impose only degree divisibility. Hartogs identifies actual algebraic or holomorphic sections with homogeneous pairs, while the nonplanar low-degree control shows that the primary conditions do not realize them. The complement is nonaffine, so affine splitting and representability results do not close that gap.
