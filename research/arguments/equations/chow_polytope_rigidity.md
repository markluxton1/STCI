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
power, and leaves the separate H16 formulation/stabilizer review outside
this note. It does not upgrade the
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

The bounded remaining question is whether this classical criterion admits
a useful structural characterization directly in arbitrary proper
\(F,G\), or their prescribed maps, without constructing the whole
resultant and without assuming eigenforms. Even such a characterization
would leave the marked-support and actual equation-realization gates.
No degree-specific search or new general theorem is proposed here.

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
