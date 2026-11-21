# Full Chow-polytope rigidity for the fixed quartic

## Scope and statement

Let \(k\) be algebraically closed, of arbitrary characteristic, and fix
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]
Let \(T=(\mathbf G_m)^4/\mathbf G_m\) act diagonally on the fixed coordinates.
For an effective one-cycle \(Z\), write its Chow form in **two hyperplane
coefficient rows** \(a=(a_0,\ldots,a_3)\), \(b=(b_0,\ldots,b_3)\).
It vanishes exactly when the two hyperplanes have a common point on the
cycle support. For a monomial \(a^u b^v\), its column weight is
\(w=u+v\in\mathbf Z^4\). Define \(P_Z\) as the convex hull of the
column weights with nonzero coefficients. In particular
\(\sum_i w_i=2\deg Z\). The scalar ambiguity of a Chow form does not change
this polytope.

This classifies **all effective one-cycles**, with no invariance hypothesis.
Invariance is a conclusion: this is a rigid fiber of the Chow-polytope map.
The canonical statement is [R-0074](../../results/chow_polytope_rigidity.md).

For every integer \(m\ge1\),
\[
 P_Z=mP_C
 \quad\Longleftrightarrow\quad
 Z=\sum_j n_j[\lambda_j C],\qquad
 \lambda_j\in T(k),\quad n_j\in\mathbf Z_{>0},\quad\sum_jn_j=m.
\]
Equality is in the **full column-weight lattice**, with the displayed
normalization: not a projected polygon and not equality up to translation.
This is a statement about effective curve cycles, not schemes, Hilbert
polynomials, embedded points, or two homogeneous defining equations.
In particular it does not solve or obstruct unrestricted STCI for \(C_0\).

## From the cycle fiber to actual complete intersections

For a fixed type \(a\le b\) with \(4\mid ab\), set \(m=ab/4\).
There are three different objects to compare:

1. **Cycle points.** By R-0074 the geometric points of the
   polytope fiber are unordered \(m\)-multisets in the two-dimensional
   torus orbit \(T/\operatorname{Stab}(C)\) of the fixed quartic.
   Multiplicity partitions record collisions of translates, not
   whether the curves meet: the translates already share the marked
   endpoints. The cycle \(m[C]\) is one marked point of the deepest
   diagonal. This is a description of geometric points, not an
   identification of scheme structures or of their compactifications.
2. **Hilbert lifts.** Above a cycle, retain the embedded schemes with
   the complete-intersection polynomial
   \(ab\,n+ab(4-a-b)/2\), and track their cycles under flat limits.
   Specifying a cycle gives neither its scheme structure nor the
   existence of a flat lift from a given component.
3. **Actual CI realization.** For \(a=b\), take two-dimensional
   subspaces of \(S_a\) with coprime generators. For \(a<b\), take
   a line \([F]\) in \(S_a\) and a line
   \([G\bmod F S_{b-a}]\) in the quotient, again with coprime
   representatives. These equation parameters map to embedded ideals,
   then to their fundamental cycles. A flat Hilbert limit need not
   stay in this proper CI locus.

For a reduced union \(Y=\bigcup_i C_{u_i,v_i}\), asking whether \(Y\)
is an STCI means asking for \(\sqrt{(F,G)}=I_Y\); the resulting fundamental
cycle may have any positive multiplicities \(\sum_i n_i[C_{u_i,v_i}]\).
A **reduced fundamental cycle** requires every \(n_i=1\), so CI purity
also makes the intersection scheme reduced. Classifying this latter case
does not classify all STCI supports. Likewise, cycle invariance does not
imply ideal invariance, and support on \(V(A)\) gives \(A\in\sqrt{(F,G)}\),
not necessarily \(A\in(F,G)\) or permission to use \(A\) as a generator.

The characteristic-zero binomial constructions below show that actual
members can realize several translates. It is not asserted that every
Chow multiset admits an actual CI lift. For each type, the question is
to determine the image of actual proper pairs in the cycle fiber:
what the general cycle and multiplicity partition of each component
are, which collision strata the image meets, and how the Hilbert
boundaries compare with cycle limits. This is a
moduli question independently of whether the marked cycle \(m[C]\)
has a proper CI lift. The
[fixed-family elliptic meeting divisor](../carriers/elliptic_double_inverse_construction.md#the-meeting-norm-divisor-and-its-normalization)
illustrates how to separate an incidence divisor, its generic fiber,
and exceptional strata in a concrete family; it is not this Chow
or Hilbert moduli space.

For boundary limits, let \(\overline O\) be the reduced projective Chow
closure of the single-translate orbit \(O=\{[C_{u,v}]\}\).
Multiplication of Chow forms gives a proper morphism
\(\operatorname{Sym}^m(\overline O)\to
\operatorname{Chow}_{1,4m}(\mathbf P^3)\), whose image is exactly the
closure of all translated arrangements: the source is projective and
\(O^m\) is dense in \(\overline O^m\). Thus every geometric limit is a
sum of \(m\) degree-four single-orbit limit cycles, allowing collisions
and boundary breakup. This gives neither unique boundary decomposition,
a scheme isomorphism, nor a flat CI lift. Boundary cycles can leave the
fixed-polytope fiber.

The [fixed toric carrier classification](../torus/fixed_carrier_chow_arrangements.md)
gives an explicit actual-pair locus retaining the quartic equation as one
generator: precisely the root polynomials with \(c_1=c_2=c_5=0\) descend.
It covers repeated roots
and every CI with reduced fundamental cycle supported on that carrier.
Characteristic zero forbids one- and two-support arrangements with that fixed
generator, while partial collisions occur. This separates the fixed-equation
problem from the moving-carrier
and non-invariant Hilbert-lift questions below.

For general arrangements, the [trace-moment theorem](../torus/chow_arrangement_moments.md)
gives \(\sum_i n_i u_i/v_i=0\) in characteristic different from two for
proper pairs with an eigenform generator or the stated actual polynomial
congruences. This includes invariant CI ideals and every reduced CI arrangement.
It is detected by a linear equation in Chow-form coefficients. In
characteristic zero, the full Chow closure of this realization locus avoids
every deepest collision \(m[C_{u,v}]\). The
[quartic classification](../../results/quartic_chow_pencil_classification.md)
gives actual non-invariant lifts of the cycles
\(2[C_{u,v}]+2[C_{u,-v}]\) outside the invariant \((4,4)\) Chow closure.
Every quartic pencil in the fiber satisfies the same moment. In higher
degrees, [one-carrier trace tests](../torus/chow_trace_cone_jets.md)
reach some non-invariant presentations.
For arbitrary forms, the [translate-coordinate evaluation map](../torus/fixed_surface_restriction_lifts.md#translate-coordinates-constrain-actual-coefficients)
gives all linear containment constraints; transverse local intersection
algebras then determine multiplicities, without assuming invariant generators.

### Realization of a reduced Chow-matched cycle

Work over an algebraically closed field. Write S=k[x0,x1,x2,x3] with weights (0,1,3,4), Ω the dense projective torus, and (t,u,v)=(x1/x0,x2*x0²/x1³,x3*x0³/x1⁴) on Ω. The stabilizing one-parameter torus scales t, and the closures of its cosets are the translates C_(u,v) appearing in R-0074. Fix positive ordinary degrees a,b with ab=4m, and distinct quotient points P_i=(u_i,v_i), i=1,…,m. Let Y be the reduced union of the C_(u_i,v_i).

For the two assignments (w_F,w_G)=(a,3b),(3a,b), set U=(S_a)_(w_F)∩I_Y and V=(S_b)_(w_G)∩I_Y. Each is the kernel of a linear evaluation matrix: a monomial x0^d0 x1^d1 x2^d2 x3^d3 of the designated weight restricts on Ω to t^w u^(d2) v^(d3) on x0=1; evaluating the coefficient at all P_i is exactly vanishing on Y.

**Criterion.** The cycle Σ[C_(u_i,v_i)] is realized by a proper degree-(a,b) pair iff one assignment has nonzero U,V and no irreducible common factor of all polynomials in both spaces (equivalently gcd of their combined bases is 1).

A proper CI that realizes the cycle is pure and generically reduced on each component, hence reduced (no nonzero subsheaf of its structure sheaf is supported away from the associated generic points). It is therefore Y, with stable saturated ideal. The equivariant minimal-generator lifting lemma ([R-0038](../../results/torus_eigenvector_generator_lifting.md)) gives actual eigenform generators of the same ordinary degrees, not leading forms. The middle coordinate vertices are outside Y. Only an eigenform of weight a (resp. b) can be nonzero at the x1 vertex in degree a (resp. b), since only a pure power survives there, and analogously weight 3a (resp. 3b) is required at the x2 vertex. One generator cannot cover both; the assignments follow. Conversely let there be no common fixed factor. Choose a nonzero F∈U avoiding the finitely many factors of gcd(V) (none divides U); then choose G∈V avoiding every factor of F (none divides V). These choices avoid finite unions of proper linear subspaces. Their pair is proper. The prescribed m degree-four curves exhaust Bézout degree ab, leaving no boundary residual and forcing all generic lengths to be one. Necessarily 4|a or 4|b, because otherwise both assigned weights are nonzero mod4 and both forms vanish on x1=x2=0.

### Which degree pairs realize some reduced cycle (characteristic zero)

Up to swapping the degrees precisely a=4r with r≥1 and b∉{1,2,5} occur. The divisibility condition follows from x1=x2=0 as above. After reversing the coordinates if necessary the generator assignments are weight a for F_a, weight 3b for G_b (reversal changes w to 4·ordinary_degree−w). For b=1,2,5 any such G is divisible by x2: to avoid x2 a monomial x0^(b−i−j)x1^i x3^j requires i=3b−4j and ceil(2b/3)≤j≤floor(3b/4), an empty interval precisely in those three positive degrees. A whole coordinate plane in one generator forces a curve of intersection on the boundary, impossible. For b=3,4,6,…,11 the interval contains an integer by inspection and for b≥12 its unrounded width is b/12≥1. Choose such j and put i=3b−4j. Then
 F=x1^(4r)−x0^(3r)x3^r,
 G=x2^b−x0^(b−i−j)x1^i x3^j.
The Laurent quotient is v^r=1, u^b=v^j; in characteristic zero it gives exactly rb distinct translates (also works when char(k) does not divide rb). Boundary check: x0=0 forces x1=0 and then x2=0 since the second monomial cannot be pure x3 (j<b); x3=0 forces x1=x2=0 since j>0; x1=0 forces x0 or x3 zero; and when x2=0 with the other coordinates nonzero the second monomial cannot vanish. This realizes every permitted degree pair without assigning any repeated cycle. In positive characteristic the necessity still holds; no classification asserted when char(k) divides rb.

### Quartics, including invariant collision lifts

For (4,4), the eigenbasis must have weights 4 and 12. The only possible forms are:
 F=a₀x1⁴+b₀x0²x1x2+c₀x0³x3,
 G=d₀x2⁴+f₀x1x2x3²+e₀x0x3³.
Here a₀,d₀ ≠0 exclude the middle vertices; c₀,e₀ ≠0 exclude a boundary curve on x1=0 or x2=0 (otherwise the corresponding equation contains the whole plane; its intersection with the positive-degree second equation is never finite). Conversely these four nonzero coefficients leave only the two allowed endpoints on the union of coordinate hyperplanes: x0=0 first forces x1=0 and then G forces x2=0; x3=0 first forces x2=0 and then F forces x1=0; x1=0 and x2=0 each force x0=0 or x3=0, which were just checked. On Ω, elimination gives v=α+βu with α≠0 and monic polynomial
 P(u)=u⁴+B u(α+βu)²+C(α+βu)³, with C≠0.
None of its roots has u=0 (constant Cα³≠0) or v=0 (would imply u⁴=0). Thus the torus intersection is finite over the quotient and the equations give a proper projective pair. Its cycle multiplicities are the polynomial root multiplicities because the torus scheme is G_m × Spec k[u]/(P) after eliminating v. Conversely these are all invariant CI lifts with cycle of translates, and in particular all lifts on the distinct four-translate stratum.

For four prescribed distinct points, the line v=α+βu is determined by any two; it must contain all four, and their monic root polynomial minus u⁴ must belong to the displayed two-dimensional span. That is an explicit realization criterion. The span basis is independent (constant term of its second element is nonzero, and its first element has nonzero u coefficient). The lifts are unique there, and unique among invariant lifts even at any realized collision with at least two distinct points. The locus on the distinct stratum has dimension four (α,C nonzero, β,B arbitrary, squarefreeness open and nonempty) inside the eight-dimensional multiset space. Its dimension follows also from unique recovery of parameters from the cycle, so this does not assert the parametrization is a scheme isomorphism. For nonemptiness in any characteristic set β=0 and choose B,C avoiding repeated roots of u⁴+Bα²u+Cα³ (in characteristic two, B≠0 suffices).

In characteristic zero all multiplicity partitions other than (4) occur among invariant lifts. For β≠0 rescale quotient coordinates to α=β=1. Requiring a double root r fixes B=−r³(r+4)/(r+1)², C=r⁴(r+3)/(r+1)³, with r≠0,−1,−3. The residual monic quadratic's discriminant is −4r²(r²+4r+2)/(r+1)^6 and its value at r is r²(r²+4r+6)/(r+1)^2. Hence r=1 gives (2,1,1), r=−2±√2 gives (2,2), and r=−2±√(−2) gives (3,1). At a triple root P'''(r)=24r/(r+1)^3≠0 (substitute r²+4r+6=0). If β=0, P''=12u² forbids a triple root. Thus only (4) fails invariantly, and the older characteristic-zero quartic-carrier exclusion rules out all (4) lifts. The [classification of actual quartic pencils](../torus/quartic_chow_pencils.md#classification) supplies the non-invariant lifts, all on the exceptional two-support cycles with multiplicity two on each.

## Chow forms, products, and the one-parameter subgroup

The elementary Chow facts used here are that the form determines its
effective cycle and that cycle addition multiplies forms. Consequently
\(P_{Z+Z'}=P_Z+P_{Z'}\) (Minkowski sum), also in positive characteristic.
For example, the product of the initial forms for any weight is nonzero
in the polynomial ring, so cancellation cannot remove an exposed face of
the Minkowski sum. A diagonal translate rescales every coefficient-row
monomial by a nonzero scalar; it preserves the column-weight support.
These are cycle-level facts, distinct from the
[global equation-resultant criterion](global_equations_and_constructions.md#p-033-the-global-chow-resultant-certificate).

Put \(e=(0,1,3,4)\). For \(C\), the two hyperplanes pull back to binary
quartics
\[
 f=a_0s^4+a_1s^3t+a_2st^3+a_3t^4,\qquad
 g=b_0s^4+b_1s^3t+b_2st^3+b_3t^4.
\]
Their homogeneous resultant is the Chow form, up to a nonzero scalar:
the parametrization is base-point-free and birational onto its image.
The change \(t\mapsto zt\) multiplies the resultant by \(z^{16}\), so
\(e\cdot w=16\) throughout \(P_C\). If \(P_Z=mP_C\), its Chow form is
therefore an eigenvector for the subgroup
\(H=\{[1:z:z^3:z^4]\}\subset T\). Its projective class, and hence its
cycle, is \(H\)-invariant. Using the inverse action on coefficient rows
only changes the eigencharacter sign and not this conclusion.

Each irreducible component \(D\) is invariant: the irreducible image of
\(H\times D\) lies in the finite union \(\operatorname{Supp}Z\) and contains
\(D\), so its closure is \(D\). The fixed locus in \(\mathbf P^3\) consists
of the four coordinate points, since the integer characters \(0,1,3,4\)
are distinct in every characteristic. Thus \(D\) contains a nonfixed point;
its one-dimensional orbit is dense in \(D\). This classifies components as
reduced orbit closures, with their cycle multiplicities kept separately.
See also the [primitive orbit-degree formula](../../results/torus_orbit_curve_degree.md).

## The endpoint-support test

All column weights are nonnegative. The minimum of \(w_1+w_2\) on \(P_C\)
is zero: setting columns 1 and 2 to zero gives
\((a_0b_3-a_3b_0)^4\), up to sign, which is nonzero in every characteristic.
Minkowski additivity and nonnegativity imply that the minimum is zero for
every irreducible component of \(Z\). Equivalently its Chow form remains
nonzero after \(a_1=a_2=b_1=b_2=0\).

Independent pairs of hyperplanes in \(\langle x_0,x_3\rangle\) form a
dense open set and all intersect in
\(L_{12}=V(x_0,x_3)\). The nonzero restriction is therefore equivalent to
\(D\cap L_{12}=\varnothing\). If \(J\) is the nonzero coordinate support
of an orbit, its limits at zero and infinity are the coordinate points
with least and greatest exponent in \(J\). Avoiding \(L_{12}\) forces both
of these endpoints to lie among \(p_0,p_3\). Since \(D\) is a curve,
\(\{0,3\}\subset J\).

There are exactly four support types:
\[
 \{0,3\},\qquad\{0,1,3\},\qquad\{0,2,3\},\qquad\{0,1,2,3\}.
\]
The first is the reduced line \(L_{03}\), of degree one. The other three
have degree four: their exponent differences have gcd one, giving a
birational parametrization in every characteristic. They are diagonal
translates of the corresponding monomial curves. In particular the last
type is a translate of \(C\). Do not use the degree-four parametrization
resultant for the reduced line: that would produce its Chow form to the
fourth power and give the wrong cycle.

## The separating face

For a polytope \(P\), let \(F_0(P)\) be its face minimizing \(w_0\), and
let \(W(P)=\max_{F_0(P)}w_2-\min_{F_0(P)}w_2\). Faces under a fixed
functional add under Minkowski sum, as do their widths. In the following
table, convex hulls are in \(\mathbf R^4\):

| Support | Minimum of \(w_0\) | \(F_0(P)\) | \(W(P)\) |
| --- | --- | --- | --- |
| \(\{0,3\}\) | 1 | \(\{(1,0,0,1)\}\) | 0 |
| \(\{0,1,3\}\) | 1 | \(\{(1,4,0,3)\}\) | 0 |
| \(\{0,2,3\}\) | 3 | \(\{(3,0,4,1)\}\) | 0 |
| \(\{0,1,2,3\}\) | 1 | \(\operatorname{conv}\{(1,4,0,3),(1,3,3,1)\}\) | 3 |

Here is exact algebraic support for the table. Write
\(\Delta_{ij}=a_i b_j-a_j b_i\), and scale \((a_0,b_0)\) by \(z\).
For the three quartic supports the first nonzero coefficients in \(z\)
of the Sylvester determinant are respectively, up to a common sign within
each row,
\[
\begin{array}{c|c}
\{0,1,3\} & z\Delta_{01}\Delta_{13}^3\\
\{0,2,3\} & z^3\Delta_{02}^3\Delta_{23}\\
\{0,1,2,3\} & z\Delta_{01}
  (\Delta_{13}^3+\Delta_{12}^2\Delta_{23}).
\end{array}
\]
The line has Chow form \(\Delta_{03}\). These identities are integral
polynomial identities, without division by a characteristic-dependent
integer. The two summands in the full-support initial coefficient have
distinct column weights, precisely the displayed endpoints. Each endpoint
has an expanded monomial coefficient \(1\) or \(-1\), so none disappears
in any characteristic; all other weights of the initial coefficient lie
on their segment.

The [reproducible checker](chow_polytope_rigidity.support/verify.py)
constructs the three \(8\times8\) Sylvester matrices over \(\mathbf Z\),
expands their determinants by a sparse permutation algorithm, checks the
initial coefficients above, all face weights, total degree, the
\(e\)-weight 16, and the coefficient-unit witnesses. It uses only Python's
standard library. Replay from the repository root:

```sh
python3 research/arguments/equations/chow_polytope_rigidity.support/verify.py
```

For a direct proof of the identities, expand the Sylvester determinant first
in its constant-coefficient column and then in the remaining adjacent
column. Its linear coefficient in \(z\) is
\(\pm\Delta_{01}\operatorname{Res}(F,G)\), where
\(F=a_1+a_2x^2+a_3x^3\), \(G=b_1+b_2x^2+b_3x^3\).
On the open set \(\Delta_{23}\ne0\), their common root satisfies
\(x^2=-\Delta_{13}/\Delta_{23}\),
\(x^3=\Delta_{12}/\Delta_{23}\); compatibility gives
\(\Delta_{13}^3+\Delta_{12}^2\Delta_{23}=0\).
The parametrization \([s^3:st^2:t^3]\) is birational in every
characteristic. Its irreducible Chow resultant and this equation have the
same bidegree \((3,3)\), so they agree up to scalar; specialization to
pure endpoint monomials fixes that scalar up to sign. Setting column 2
to zero gives the \(\{0,1,3\}\) row. For \(\{0,2,3\}\), the same
elimination uses \(x^3=-\Delta_{03}/\Delta_{23}\),
\(x^4=\Delta_{02}/\Delta_{23}\) and gives the full resultant
\(\pm(\Delta_{03}^4-\Delta_{02}^3\Delta_{23})\).
Its lowest \(z\)-term gives the remaining row. These polynomial identities
extend from the indicated dense open sets: the incidence hypersurface
meets \(\Delta_{23}\ne0\) densely (take a common root \(x=1\)),
and that condition excludes a root at infinity. Equal bidegrees then
identify the eliminants with the irreducible Chow resultants. This algebraic derivation is
the proof; the determinant checker is reproducible supporting evidence.

## Width and degree exhaustion

Let \(N\) be the number of full-support components of \(Z\), counted with
multiplicity. The table and Minkowski additivity give
\[
 3N=W(P_Z)=W(mP_C)=3m,
\]
so \(N=m\). On the other hand, the sum of the column coordinates is
\(2\deg Z\); equality of the polytopes gives \(\deg Z=4m\).
The full-support quartics already contribute \(4m\), and every other
component of an effective one-cycle has positive degree. No other
components can occur. This proves the forward implication. Conversely,
diagonal translates have polytope \(P_C\), and multiplication of their
Chow forms gives \(P_Z=(\sum_j n_j)P_C\).

## Review and limitations

The support test, orbit classification (including the degree-one line),
face widths, characteristic scope, and degree exhaustion were independently
reconstructed for this proof. The integer determinant identities were
also replayed independently using symbolic resultants. The retained
standard-library checker supplies a separate direct determinant replay;
its output checks algebraic identities, not equation realization.

The statement resolves the cycle-level H15 proof gate. It makes no claim
of a scheme-theoretic identification of a Chow locus with a symmetric
power. The set-level H16 formulation and stabilizer are proved below; its
scheme-locus interpretation remains outside the claim. It does not upgrade the
[full Hilbert-boundary results](../../frameworks/torus-supported-boundaries/index.md)
to a two-generator realization theorem.

Even translation of polytopes cannot be discarded: adding \([L_{03}]\)
to \(m[C]\) adds the singleton \((1,0,0,1)\) to its polytope. Thus equality
up to translation would admit an extra line. The full, unshifted equality
in the statement is essential.


## Proper surface pairs and the remaining equation question

Let \(F,G\) be homogeneous of positive degrees \(a,b\), with no common
surface component, and \(ab=4m\). Their proper complete intersection has
fundamental cycle \(Z=[V(F,G)]_{\mathrm{cyc}}\) of degree \(ab\). Hence
\[
 P_Z=mP_C\quad\Longleftrightarrow\quad
 Z=\sum_j n_j[\lambda_j C],\qquad \sum_jn_j=m.
\]
This is necessary for \(Z=m[C]\), but does not distinguish the marked
quartic from other translates or force all translates to coincide.
It does not imply that the equations themselves are eigenforms.

There is already a classical coefficient criterion on the open parameter
space of proper pairs. Form the incidence resultant
\[
 R(F,G;\alpha,\beta)=\operatorname{Res}_x(F,G,L_\alpha,L_\beta),
\]
which is their cycle's Chow form, of bidegree \((ab,ab)\) in the two
hyperplane rows. Expand it as \(\sum c_{uv}(F,G)\alpha^u\beta^v\).
Then \(P_Z=mP_C\) holds exactly when all coefficients with
\(u+v\notin mP_C\) vanish and, at each vertex of \(mP_C\), at least one
coefficient of that weight is nonzero. This gives a finite constructible
condition in fixed degrees, not a new structural theorem. It incorporates
coefficient cancellations; the Newton polytopes of \(F,G\) alone are not
asserted to determine the answer. The existing
[prescribed Sylvester bundle map](chow_bundle_maps.md) gives the same
criterion through its determinant; arbitrary unrelated bundle determinants
do not constitute homogeneous equation realization.

The [quartic classification](../torus/quartic_chow_pencils.md#classification)
gives a structural characterization in degree \((4,4)\) from the
actual equations. An [endpoint different test](../torus/chow_endpoint_different.md#statement)
recognizes single support after Chow matching in arbitrary degree.
An equation-side criterion for matching outside the quartic pencils,
and an obstruction to single support for unrestricted pairs, remain open.

## Eigenpairs and transverse finite quotients

For eigenpairs under \(H=T_C\), [R-0050](../../results/torus_orbit_curve_degree.md)
uses \(x=(1,t,t^3u,t^4v)\) to write the restrictions as
\(t^rf(u,v),t^sg(u,v)\). The finite Laurent quotient
\(B=k[u^{\pm1},v^{\pm1}]/(f,g)\), possibly zero, gives
\(V(F,G)\cap T_{\mathrm{dense}}=\operatorname{Spec}B\times\mathbf G_m\).
Its points \((\epsilon,\zeta)\) give translated quartics
\([s^4:s^3t:\epsilon st^3:\zeta t^4]\); local lengths give generic
cycle multiplicities. This sees no components supported on the coordinate
boundary. Excluding those components is essential before inferring the
whole projective cycle. With boundary excluded, marked sole support is
precisely \(\operatorname{Supp}B=\{(1,1)\}\), not reducedness of \(B\).

For two Laurent binomials with independent exponent-difference rows and
nonzero constants, the quotient is a torsor under the finite diagonalizable
kernel of the associated torus isogeny. Smith normal form identifies that
kernel as \(\mu_{d_1}\times\mu_{d_2}\). In characteristic zero its roots
are distinct and reduced; in characteristic \(p\), the prime-to-\(p\)
part remains reduced while the \(p\)-primary part can concentrate length
nonreducedly. This explains a contrast in binomial instances, not in all
Laurent systems. H15 neither forces subgroup-scheme structure nor ensures
that a chosen finite quotient is realized by a proper projective pair
without boundary residuals.

## Foundational references and literature boundary

- Dalbec and Sturmfels, [*Chow Forms*](https://math.berkeley.edu/~bernd/chowforms.pdf),
  in *Invariant Methods in Discrete and Computational Geometry* (1995),
  explains cycle encoding and gives the complete-intersection resultant
  example (printed p. 4). The incidence construction above is classical.
- Fink, [*Tropical cycles and Chow polytopes*](https://arxiv.org/abs/1001.4784),
  Definition 4.4 and the preceding weight discussion (arXiv p. 9), defines
  the Chow weight polytope. Bracket substitution in two hyperplane rows
  preserves the column weights used here. The foundational source is
  Kapranov, Sturmfels and Zelevinsky, *Chow polytopes and general resultants*,
  [Duke Math. J. 67 (1992), 189–218](https://doi.org/10.1215/S0012-7094-92-06707-X).
- Eisenbud and Schreyer, with an appendix by Weyman,
  [*Resultants and Chow forms via Exterior Syzygies*](https://arxiv.org/abs/math/0111040),
  supplies a general Chow-complex determinant construction. It does not
  remove the prescribed-equations condition in this application.
- Edidin and Graham, [*Equivariant intersection theory*](https://arxiv.org/abs/alg-geom/9609018),
  provides the equivariant cycle framework, not an inference that a pair
  defining an invariant cycle must consist of eigenforms.
- Eisenbud and Sturmfels, [*Binomial Ideals*](https://arxiv.org/abs/alg-geom/9401001),
  Section 2, treats Laurent binomial ideals via partial characters; this
  is the relevant established framework for the special finite quotients.

This focused audit identifies classical tools already covering the
coefficient and determinant reformulations. It is not an exhaustive
literature search or a claim that the remaining structural question is new.


## Set-level symmetric-power fiber (H16)

Retain an algebraically closed field k of arbitrary characteristic and an
integer m >= 1. Define F_m(k) to be the set of effective one-cycles Z with
P_Z = m P_C in the full, unshifted column-weight normalization above.

This is a corollary of R-0074 together with the split-torus stabilizer
calculation below, not a new rigidity theorem. It classifies cycles in the
exact polytope fiber, not surface pairs or equation realizations.
There is a natural bijection of sets

    Sym^m(T/T_C)(k)  -->  F_m(k),
    {(u_i,v_i)}     |->  sum_i [C_{u_i,v_i}],

where T_C is the stabilizer of the embedded curve C in the diagonal torus, T/T_C is canonically isomorphic to G_m^2 after choosing the fixed coordinate normalization, and

    C_{u,v} = [s^4:s^3t:u st^3:v t^4],  u,v in k^*.

Repeated parameters mean repeated cycle components, not a choice of a nonreduced subscheme structure. Equivalently the source is the set of unordered multisets of m points of (k^*)^2.

### Stabilizer, including scheme-level check for the curve

Identify the dense coordinate torus of P^3 with T using [1:1:1:1] as identity. Scheme-theoretically

    C intersect T = H = {[1:z:z^3:z^4]}.

Indeed on x_0 = 1 the Laurent equations are x_2 = x_1^3 and x_3 = x_1^4, so this is a closed subgroup isomorphic to G_m, not merely a parametrized image of nontrivial degree.

If a diagonal element lambda stabilizes C, it stabilizes C intersect T = H. Evaluating lambda H = H on the identity gives lambda in H. Conversely H stabilizes C by the change t -> zt. This argument works over every k-algebra, using the identity section, so the scheme-theoretic stabilizer of the embedded curve is precisely the smooth subgroup H. There is no additional finite or infinitesimal factor in T_C. The exponent 1 is important: no root extraction or division by 3 or 4 occurs, even in characteristics 2 or 3.

Explicitly the split quotient is

    q([lambda_0:lambda_1:lambda_2:lambda_3])
      = (lambda_0^2 lambda_2/lambda_1^3,
         lambda_0^3 lambda_3/lambda_1^4).

Its section is (u,v) -> [1:1:u:v]. Its kernel is H. In coordinates a=lambda_1/lambda_0, b=lambda_2/lambda_0, c=lambda_3/lambda_0, the isomorphism T = G_m x G_m^2 is (a,b,c) -> (a,b/a^3,c/a^4). Thus this is a split quotient over any base field and does not hide an inseparable isogeny.

### Proof of the cycle bijection

1. Each coset of H produces precisely one translated embedded quartic. Distinct (u,v) produce distinct curves: on their dense torus portions the two regular functions x_0^2 x_2/x_1^3 and x_0^3 x_3/x_1^4 have the constant values u and v. These distinguish the cosets and curves.
2. H15/R-0074 says every Z in F_m(k) is a sum of m such translates, counting multiplicity. This proves surjectivity.
3. Effective cycles have unique decompositions into distinct integral curves with positive integral multiplicities. Since (u,v) uniquely identifies a curve, that decomposition uniquely identifies the parameter multiset. This proves injectivity.
4. Conversely the Chow form of a cycle sum is the product of the component forms, and all translates have P_C, giving m P_C.

For completeness, Sym^m(G_m^2) is the affine finite-group quotient Spec(k[u_i^{+/-1},v_i^{+/-1}]^{S_m}). Over algebraically closed k, its k-points are exactly the S_m-orbits of the tuples. This statement holds when char(k) divides m!: finite-group geometric quotient theory does not require averaging or division by m!. An elementary point-separation proof uses a function taking values 0 and 1 on two disjoint finite orbits and takes its product over the group. Integrality of the invariant-ring inclusion supplies surjectivity. See Jarod Alper, Stacks and Moduli, May 21, 2024 draft, Theorem 4.2.6 (printed p. 167; PDF p. 172).

### Necessary qualifications

- This proves the displayed bijection of sets, not an isomorphism between a scheme-theoretic Chow locus and the symmetric power. Geometric points alone do not determine nilpotents, tangent directions, or inseparability. A scheme assertion requires specifying the intended locus and its structure and checking the induced morphism, not just invoking H15.
- The stabilizer just proved is that of the curve C. Do not silently substitute the stabilizer of a multiple cycle's Chow point. In characteristic p, infinitesimal translations can fix the Chow point of p[C] without fixing C: over k[epsilon]/(epsilon^2), a translated Chow polynomial has form F + epsilon G, and (F + epsilon G)^p = F^p. For example [1:1:1+epsilon:1] is outside H but fixes that multiple-cycle Chow point. This is a concrete reason not to infer scheme-level orbit or tangent conclusions from the set bijection.
- The symmetric-power statement is for algebraically closed k (or for geometric points over an algebraic closure). Over a nonclosed field, Sym^m(X)(k) need not equal Sym^m(X(k)). For example over R a conjugate pair of nonreal points in G_m^2 defines a real point of Sym^2 although neither point is real. Use a separately formulated descent/closed-point cycle statement rather than asserting all k-cycles are sums of k-rational translates. Imperfect fields add inseparability issues and are outside the present claim.
- Use full unshifted Chow-polytope equality. Projected equality or equality up to translation has not been shown to select F_m.
- This does not prescribe scheme structure on the cycle, endpoint or embedded-point data, a Hilbert polynomial, generators, or realization by two homogeneous equations. It is not an STCI existence or obstruction theorem.
- R-0050 already contains the normalized family C_{u,v} and its connection to finite Laurent quotients for eigenpairs. H16 adds the exact set-level parameterization of the H15 fiber, using unique decomposition; it is a short corollary, not a new equation-realization framework.

