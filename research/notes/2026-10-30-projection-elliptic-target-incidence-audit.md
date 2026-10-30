# Independent audit of the elliptic support and extension obstruction

October 30, 2026. Reviewer: elliptic_target_incidence/balanced_palindromic.
Verdict: **PASS for the zero-middle-coefficient support stratum stated
in the [proposal](2026-10-30-projection-elliptic-target-incidence.md)**.
This is reviewed provisional evidence, not canonical promotion and not
a computation of the whole marked projection locus.

I reconstructed the argument independently of the author's coefficient
calculations. The inputs are the reviewed full residual-boundary exclusion
and the reviewed smooth elliptic Riemann--Hurwitz equality in
[the boundary proof](2026-10-29-projection-m2-boundary.md) and
[the smooth-residual audit](2026-10-29-projection-m2-doublecover-audit.md).
They supply a smooth elliptic residual \(E\), target ruling functions
\(A,B\) of degrees two and six, and four distinct points
\(Z=P_1+\cdots+P_4=E\cap c\). The function \(f=B^3/A\) is a degree-twenty
cover ramified only over zero, one and infinity; its zero and infinity
partitions are \((3^6,1^2)\), while its fiber over one has reduced support
exactly \(Z\). Its boundary divisors are reduced and pairwise disjoint.
The source diagonal parameters \(t_i\) at \(P_i\) are finite, nonzero and
distinct.

## The exact Picard identity

Put \(L=A^*\mathcal O(1)\) and \(M=B^*\mathcal O(1)\).
Disjoint boundary supports give \(f^*\mathcal O(1)=L\otimes M^3\).
The ramification in the zero and infinity fibers has class \(M^4\):
each zero or pole of \(B\) contributes order two, and every zero or pole
of \(A\) contributes zero.

The ramification divisor over one is \(T-Z\), where \(T=f^{-1}(1)\)
with multiplicities. It therefore has class
\(L\otimes M^3\otimes\mathcal O_E(-Z)\). There is no ramification
elsewhere, so Riemann--Hurwitz, using \(\omega_E=\mathcal O_E\), gives
\[
L^2M^6=M^4LM^3\mathcal O_E(-Z).
\]
Consequently \(M=L\mathcal O_E(Z)\). The actual source polarization gives
\(LM=\mathcal O_E(2,2)=\mathcal O_E(2Z)\), hence
\[
L^2=\mathcal O_E(Z),\qquad M=L^3.
\]
These are equalities in the Picard group. No cancellation of a factor two
in a degree-zero group, and therefore no hidden two-torsion assumption,
occurs. They do not assert that \(Z\) is the ramification divisor of \(A\).

## The degree-two interpolation step

Let \(a'\) be a Möbius transform of \(A\) with
\(a'(P_i)=t_i\). Its line bundle is still \(L\).
Each source ruling function \(u\) or \(v\) has degree two and is finite at
these four points. If \(u-a'\) is nonzero, its zero divisor contains \(Z\)
of degree four, while its pole divisor has degree at most four.
The zero and pole degrees must be equal, so both degrees are exactly
four. In particular there is no cancellation in the pole divisor:
\[
\operatorname{div}_0(u-a')=Z,\qquad
\operatorname{div}_\infty(u-a')
=\operatorname{div}_\infty u+\operatorname{div}_\infty a'.
\]
If \(P\) is the line bundle of \(u\), this gives
\(PL=\mathcal O_E(Z)=L^2\), so \(P=L\).
If \(u=a'\) identically the same conclusion is immediate.

A degree-two bundle on an elliptic curve has exactly two global
sections. Thus all its degree-two functions are related by Möbius
transformations. Agreement at the four distinct values \(t_i\) forces
that transformation to be the identity, so \(u=a'\). The same proof gives
\(v=a'\). This contradicts the actual embedding of the residual into
\(\mathbf P^1_u\times\mathbf P^1_v\): its image would lie in the diagonal.

## Both determinant strata of the support polynomial

Assume the marked support quartic is
\[
R_Z(t)=t^4+a t^3+c_1t+d,\qquad d\ne0,
\]
with four distinct roots. At its roots, \(A=t^3\) and
\[
t(A+c_1)=-(aA+d).
\]
If \(d-ac_1\ne0\), the ratio
\[
a'=-\frac{aA+d}{A+c_1}
\]
is a degree-two function with bundle \(L\), finite at each \(P_i\).
Indeed a zero denominator at a support point would also make the
numerator zero, forcing \(d-ac_1=0\). The preceding interpolation
contradiction applies.

If \(d=ac_1\), then \(a,c_1\ne0\) and
\[
R_Z(t)=(t+a)(t^3+c_1).
\]
Separable four-root support gives three distinct points \(P_i\) with
the same value \(A(P_i)=-c_1\). A degree-two map has no fiber with
three distinct points. This excludes the degenerate determinant case as
well; it is not removed by localizing at a convenient minor.

The argument is independent of the contact multiplicities at the four
points and independent of birationality of the residual map to its target
image. It applies to the entire stated support stratum on the actual
marked source. It does not exclude nonzero middle coefficient or the
order-one determinant source.
