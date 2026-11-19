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

The table also has a direct check: when column 1 is present, at \(z=0\)
the dehomogenized quartics are \(xF(x),xG(x)\). The simple root at zero
of the first lifts formally, giving coefficient
\(\pm\Delta_{01}\operatorname{Res}(F,G)\). This argument lifts only
that simple root, so it does not assume the other roots are separable.
For full support the residual cubics have powers \(0,2,3\), giving
\(\operatorname{Res}(F,G)=\pm(\Delta_{13}^3+\Delta_{12}^2\Delta_{23})\).
For support \(\{0,1,3\}\) it reduces to \(\pm\Delta_{13}^3\).
For \(\{0,2,3\}\), the full quartic resultant is
\(\pm(\Delta_{03}^4-\Delta_{02}^3\Delta_{23})\), which gives its row.
The checker verifies these polynomial expressions independently of this
root interpretation.

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
