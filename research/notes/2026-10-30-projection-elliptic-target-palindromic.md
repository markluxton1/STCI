# A primitive balanced elliptic target curve that fails global extension

October 30, 2026. Investigator: elliptic_target_incidence/balanced_palindromic.
Status: **exact constructed target incidence with a reviewed global
extension obstruction**. The explicit target calculation has not received
a separate independent computational replay. The global obstruction is
the [support theorem](2026-10-30-projection-elliptic-target-incidence.md),
whose [independent audit](2026-10-30-projection-elliptic-target-incidence-audit.md)
reconstructs the marked-source argument. No canonical record is changed.

This example is a useful positive intermediate construction with a precise
negative global conclusion. It shows that the correct genus, four
normalized inverse points, and the required degree-twenty contact passport
do not ensure extension to four actual global sections on the source.

## 1. An explicit primitive curve of class \((6,2)\)

Let \(k\) be algebraically closed of characteristic zero, choose
\(\eta^2=-4/5\), and put
\[
R(t)=t^4+\eta t^3+\eta t+1,\qquad P(t)=R(t)^5.
\]
The four roots of \(R\) are distinct, finite and nonzero.
Define the three polynomials \(e_i(A)\) uniquely by regrouping exponents
modulo three:
\[
P(t)=e_0(t^3)+t e_1(t^3)+t^2e_2(t^3),
\qquad \deg e_i\le6.
\]
On \(Q=\mathbf P^1_A\times\mathbf P^1_B\), take the bihomogenized curve
\[
C':e_0(A)+B e_1(A)+B^2e_2(A)=0.
\]
The coefficient triple has gcd one and both \(e_0,e_2\) have degree six,
so this is the literal complete bidegree \((6,2)\), without a fixed ruling.

Its quadratic discriminant has the exact factorization
\[
\begin{aligned}
\Delta(A)&=e_1(A)^2-4e_0(A)e_2(A)=-3S(A)^2D(A),\\
S(A)&=(\eta A+1)(A+\eta)(A^2-7\eta A+1),\\
D(A)&=5A^4+\frac{28}{5}\eta A^3+\frac{102}{25}A^2+
      \frac{28}{5}\eta A+5.
\end{aligned}
\]
The quartic \(D\) is separable. Thus \(\Delta\) is not a square in \(k(A)\),
the target curve is geometrically integral, and its normalization is the
smooth elliptic curve
\[
E:Y^2=-3D(A),\qquad
B=\frac{-e_1(A)+S(A)Y}{2e_2(A)}.
\]
This gives an actual primitive target incidence, rather than a
postulated low-genus model.

## 2. The exact four-point contact and ruling boundaries

The fixed target quartic has equation \(A=B^3\). Restriction of the
equation of \(C'\) to it is \(R(t)^5\). Moreover
\[
\gcd\bigl(R(t),\Delta(t^3)\bigr)=1.
\]
Therefore each of its four target intersection points is smooth on
\(C'\), has exactly one preimage on \(E\), and has intersection
multiplicity five with the fixed quartic. There are exactly four
normalized inverse points, not six or eight as in the earlier special
root configuration.

The two ruling functions on \(E\) have degrees two and six. Their zero
and pole divisors are reduced and pairwise disjoint. The exact verifier
checks this also at the two visible nodal target points over \(B=0,\infty\):
\[
\begin{aligned}
e_0(A)&=(\eta A+1)^2Q_0(A),\\
Q_0(A)&=10A^4+(\eta^3+30\eta)A^3+33\eta^2A^2
 +(10\eta^3+3\eta)A+1,\\
e_2(A)&=(A+\eta)^2Q_\infty(A),\\
Q_\infty(A)&=A^4+(10\eta^3+3\eta)A^3+33\eta^2A^2
 +(\eta^3+30\eta)A+10.
\end{aligned}
\]
Both residual quartics are squarefree and coprime to \(e_1\).
At the double roots \(A=-1/\eta,-\eta\), the discriminant has order
exactly two, and both local branches have simple zero, respectively
simple pole, of \(B\). The normalized \(B\) divisors are therefore
reduced despite the squares visible in the target coefficients.
No first-ruling endpoint is a second-ruling endpoint.

It follows either directly or by equality in Riemann--Hurwitz that
\[
B^3/A:E\longrightarrow\mathbf P^1
\]
is a degree-twenty cover with zero and infinity partitions
\((3^6,1^2)\), and partition \((5^4)\) over one. These three fibers already
account for all forty ramification units. The target incidence passes
the complete elliptic boundary and ramification tests.

## 3. Its precise global failure

At a root of \(R\), the target and marked parameters satisfy
\[
t=-\frac{\eta A+1}{A+\eta}.
\]
This is a nondegenerate Möbius transform of \(A\), since
\(\eta^2\ne1\). If the four points extended to a full-singleton marked
projection from \(S=\mathbf P^1_u\times\mathbf P^1_v\), its actual source
ruling functions would have degree two and satisfy \(u=v=t\) at those
points. The support theorem gives
\(\mathcal O_E(Z)=L^2\), \(L=A^*\mathcal O(1)\).
The degree-two interpolation argument then forces both source ruling
functions to equal that same Möbius transform globally. Their image would
be the diagonal, contradicting the required \((2,2)\) elliptic embedding.

Thus this exact primitive target curve cannot extend to the required
marked global projection. The obstruction is global source interpolation,
not failure of the target genus or inverse-point count.

## 4. Reproduction and limits

The [Macaulay2 script](../computations/stci_projection_elliptic_target_palindromic_2026_10_30.m2)
and [saved output](../computations/stci_projection_elliptic_target_palindromic_2026_10_30.txt)
work over rational polynomial rings, imposing \(5\eta^2+4=0\) by exact
ideal reduction and unit-ideal tests. They check the discriminant
factorization, separability, primitive bidegree, four smooth normalized
intersection points, and all boundary simplicity assertions.
The final marker is
PRIMITIVE_BALANCED_ELLIPTIC_TARGET_CANDIDATE_VERIFIED.
The construction is exact over \(\mathbf Q(\eta)\), not inferred from
samples over finite fields.

The initial symbolic portion retains the two-parameter palindromic
support \(t^4+a t^3+b t^2+a t+1\) and its reciprocal discriminant.
It is preprocessing only: its full two-parameter genus-one locus has not
been classified. The completed global zero-middle-coefficient support
exclusion is broader than this example and is proved separately.
