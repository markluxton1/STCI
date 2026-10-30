# A global extension obstruction for an elliptic target incidence

October 30, 2026. Author: elliptic_target_incidence. Status:
**reviewed provisional necessary-condition exclusion**, with an
[independent reconstruction](2026-10-30-projection-elliptic-target-incidence-audit.md).
No canonical result or question is changed. This computes the emptiness of
a specified support stratum, not the complete marked projection locus.

## Exact source and completed stratum

Use the characteristic-zero marked smooth-quadric source of
[the residual-geometry note](2026-10-29-projection-residual-geometry.md).
Thus \(S=\mathbf P^1\times\mathbf P^1\), \(c\) is its diagonal, and four
basepoint-free sections \(U_i\) of \(\mathcal O_S(2,2)\) restrict on \(c\)
to the literal curve \(C_0=[s^4:s^3t:st^3:t^4]\).
Assume
\[
V(q(U))=2c+D,\qquad D\in|\mathcal O_S(2,2)|,
\]
and full reduced inverse support of \(C_0\) equal to \(c\).

The [complete residual-boundary exclusion](2026-10-29-projection-m2-boundary.md)
forces \(D\) to be smooth and irreducible. It is an elliptic curve.
The target ruling functions \(A,B:D\to\mathbf P^1\) have degrees two
and six, and the target curve has equation \(A=B^3\).
The [smooth-residual audit](2026-10-29-projection-m2-doublecover-audit.md)
proves that \(Z=D\cap c\) consists of four distinct points; their target
parameters \(t=B|_c\) are finite and nonzero. The boundary divisors of
\(A,B\) are reduced and pairwise disjoint, and \(f=B^3/A\) is a
degree-twenty cover branched only over zero, one and infinity.

Normalize the polynomial cutting out the four source diagonal parameters
to have leading coefficient one:
\[
R_Z(t)=t^4+a t^3+b t^2+c_1t+d,\qquad d\ne0.
\]
Its roots are distinct. These are actual diagonal parameters, not an
unmarked choice of coordinates on an abstract elliptic cover.

**Completed claim.** Every possible tuple as above satisfies
\[
\boxed{b\ne0.}
\]
In other words, the complete order-two support stratum whose intersection
quartic has zero middle coefficient is empty. This includes every
contact-multiplicity distribution on the four points; no balanced-contact
assumption or birationality hypothesis on \(D\to Q\) is used.
The condition is unchanged by the torus scaling and inversion preserving
the literal marked quartic.

## 1. The precise elliptic line-bundle identity

Put
\[
L=A^*\mathcal O_{\mathbf P^1}(1),\qquad
M=B^*\mathcal O_{\mathbf P^1}(1).
\]
Their degrees are two and six. The ambient hyperplane bundle on \(D\) is
\(L\otimes M\). Since the source hyperplane bundle is
\(\mathcal O_S(2,2)\), and \(c\) has class \((1,1)\),
\[
L\otimes M\simeq\mathcal O_D(2Z).
\tag{1}
\]
Disjoint reduced boundary divisors imply
\[
f^*\mathcal O(1)\simeq L\otimes M^3.
\]
The ramification in the zero and infinity fibers is twice the zero
and pole divisor of \(B\), hence has line-bundle class \(M^4\).
The fiber over one is supported on the reduced divisor \(Z\); if \(T\)
denotes its full fiber divisor, its ramification divisor is \(T-Z\),
of class \(L\otimes M^3\otimes\mathcal O_D(-Z)\).
All ramification is in these three fibers. Riemann--Hurwitz on the
elliptic curve therefore gives the actual Picard-group identity
\[
M^4\otimes L\otimes M^3\otimes\mathcal O_D(-Z)
\simeq (L\otimes M^3)^2.
\]
Consequently \(M\simeq L\otimes\mathcal O_D(Z)\), and (1) yields
\[
\boxed{L^2\simeq\mathcal O_D(Z),\qquad M\simeq L^3.}
\tag{2}
\]
These are line-bundle identities, not just equality of degrees. They do
not identify \(Z\) with the actual ramification divisor of \(A\).

## 2. A degree-two interpolation lemma retains the source embedding

Let \(E\) be an elliptic curve and \(Z=P_1+\cdots+P_4\) four distinct
points. Suppose \(L\) is a degree-two line bundle with
\(L^2\simeq\mathcal O_E(Z)\). Let \(a:E\to\mathbf P^1\) have degree two
and bundle \(L\), and suppose the four finite values \(a(P_i)\) are
distinct.

If another degree-two function \(u:E\to\mathbf P^1\), finite at \(Z\),
has \(u(P_i)=a(P_i)\), its line bundle is also \(L\). Indeed, if
\(u-a\) is identically zero this is immediate. Otherwise its zero
divisor contains \(Z\), of degree four, while its pole divisor has
degree at most four. Equality of zero and pole degrees forces
\[
\operatorname{div}_0(u-a)=Z,\qquad
\operatorname{div}_\infty(u-a)
=\operatorname{div}_\infty u+\operatorname{div}_\infty a.
\]
In particular there is no pole cancellation or overlap. If \(P\) is the
bundle of \(u\), then
\[
P\otimes L\simeq\mathcal O_E(Z)\simeq L^2,
\]
so \(P\simeq L\).

Every degree-two function with this bundle is a ratio of a basis of
the complete two-dimensional space \(H^0(E,L)\). Two such functions
are related by a Möbius transformation. Since \(u\) and \(a\) agree at
four distinct values, this transformation is the identity. Thus in
fact \(u=a\).

Consequently an embedded curve of type \((2,2)\) on
\(\mathbf P^1_u\times\mathbf P^1_v\) cannot have
\[
u(P_i)=v(P_i)=a(P_i)
\]
at all four points: the two source ruling functions would both equal
\(a\), and the image would lie in the diagonal rather than being an
embedded elliptic curve.

## 3. A zero middle coefficient supplies the forbidden interpolant

Suppose \(b=0\). At each root \(t_i\) of \(R_Z\), the marking gives
\[
A(P_i)=t_i^3,\qquad B(P_i)=t_i,\qquad
t_i(A(P_i)+c_1)=-(aA(P_i)+d).
\tag{3}
\]
If \(d-ac_1\ne0\), the function
\[
a'(P)=-\frac{aA(P)+d}{A(P)+c_1}
\]
is a nondegenerate Möbius transform of \(A\), with the same degree-two
bundle \(L\). Its denominator does not vanish at a root in (3):
otherwise the numerator would vanish there too, contrary to the
nonzero determinant \(d-ac_1\).
It has the four distinct finite values \(a'(P_i)=t_i\).

The two source ruling functions \(u,v\) also have degree two and have
these values at \(Z\), because \(P_i\) lie on the source diagonal.
Identity (2) and the interpolation lemma force \(u=v=a'\) globally,
contradicting the source embedding.

The degenerate determinant case is also excluded. If \(d=ac_1\), then
\[
R_Z(t)=(t+a)(t^3+c_1).
\]
Since \(d\ne0\) and the four roots are distinct, three distinct points
of \(Z\) have the same first ruling value \(A=-c_1\). A degree-two map
cannot have three distinct points in one fiber. This exhausts the
entire zero-middle-coefficient stratum.

## 4. A genuine target incidence that fails this extension test

The independent
[palindromic target calculation](2026-10-30-projection-elliptic-target-palindromic.md)
exhibits a useful negative control. Take
\[
R(t)=t^4+\alpha t^3+\alpha t+1,\qquad \alpha^2=-4/5,
\qquad P(t)=R(t)^5.
\]
Regrouping exponents modulo three gives a primitive target curve
\(e_0(A)+Be_1(A)+B^2e_2(A)=0\) of class \((6,2)\).
Its normalization is elliptic and the four target intersections with
\(C_0\) have exactly four smooth normalized preimages, each with contact
five. Thus the abstract target-curve incidence genuinely survives.

It still cannot extend to the marked source projection: its support
quartic has \(b=0\), so Section 3 applies. A low-genus target image and
the correct number of inverse points are insufficient without the two
actual source ruling maps. This preserves a constructive intermediate
example and identifies its exact global failure.

## 5. Computational continuation on balanced contact

For balanced contact \((5,5,5,5)\), an arbitrary four-point support can
be written
\[
P(t)=(t^4+a t^3+b t^2+c t+1)^5
\]
after torus scaling and a nonzero scalar. The target equation is uniquely
recovered by grouping the coefficients modulo three.
The exact coefficient source is built in
[stci_projection_elliptic_target_2026_10_30.m2](../computations/stci_projection_elliptic_target_2026_10_30.m2).
The discriminant of its quadratic in \(B\) is a binary degree-twelve form.
Under the elliptic full-inverse hypotheses it is a square of a binary
quartic times a separable binary quartic, whose branch divisor avoids
the first-ruling endpoints.

Completed rational computations exclude the lower square-factor charts
of affine degrees zero, one and two, after saturation by the
discriminant of the support quartic. Their affine discriminant degrees
are at most four, six and eight, respectively. Each saturated ideal is
the unit ideal; see
[the boundary script](../computations/stci_projection_elliptic_target_boundary_2026_10_30.m2)
and [its saved output](../computations/stci_projection_elliptic_target_boundary_2026_10_30.txt).

The affine square-factor degree-three chart has now been completed by
a separate exact resultant and number-field calculation, rather than
by the unfinished multivariate saturation. This computational conclusion
still awaits independent review. The degree-twelve and degree-eleven
leading coefficients first force
\[
b=-3a^2/4,\qquad c=(7a^4+40)/(20a),\qquad a\ne0,
\]
on the nonzero-middle locus. Scaling the support parameter by \(t=ay\)
and writing \(\lambda=a^4\) gives the one-parameter support
\[
20\lambda y^4+20\lambda y^3-15\lambda y^2+(7\lambda+40)y+20.
\]
The resultant of its target discriminant and that discriminant's
derivative has six nonconstant irreducible factors in \(\lambda\), of
degrees \(1,2,2,3,12,14\). The degree-one and one degree-two factors
give degenerate support or a lower discriminant degree, already excluded.
For every root of each remaining factor, exact arithmetic in its
number field gives odd squarefree discriminant degree eight, hence
normalization genus three, instead of one. Away from the resultant
roots the degree-ten discriminant is squarefree and also has the
wrong genus. This excludes the entire stated degree-ten chart.
The [classification script](../computations/stci_projection_elliptic_target_degree_ten_resultant_2026_10_30.m2)
and [complete output](../computations/stci_projection_elliptic_target_degree_ten_resultant_2026_10_30.txt)
end with the marker DEGREE_TEN_PARAMETER_CLASSIFICATION_COMPLETE.

The affine square-factor degree-four chart, corresponding to target
discriminant degree twelve, is **not completed**. Its nonzero-middle
saturation was stopped with script and partial output retained. The
balanced-contact case and arbitrary four-point contact distributions
are therefore not exhausted. The independent audit linked at the top
reviews the uniform geometric support theorem, not these subsequent
large coefficient calculations. No unfinished Gröbner computation is
reported as a completed locus calculation.

The small
[support-identity verifier](../computations/stci_projection_elliptic_target_support_2026_10_30.m2)
checks the factorization and Möbius identity used in Section 3; its
[output](../computations/stci_projection_elliptic_target_support_2026_10_30.txt)
does not replace the line-bundle and source-embedding proof.
