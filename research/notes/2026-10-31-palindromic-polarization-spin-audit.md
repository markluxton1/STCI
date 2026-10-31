# Independent audit: palindromic polarization and induced spin

October 31, 2026. Reviewer: `palindromic_spin_review`, fresh independent
review; no nested delegation. **Verdict: PASS for the exact target replay,
the failed first Picard gate, the conditional spin extraction, and the
decision to stop this target. No material finding remains.** This reviews
a provisional contribution; it does not promote a canonical result or
settle the unrestricted characteristic-zero STCI question.

## Reviewed state and dependencies

I followed INDEX then MAP, read the [proposal](2026-10-31-palindromic-polarization-spin.md),
the actual predicates in its [verifier](../computations/verify_palindromic_picard_gate_2026_10_31.py),
and the [saved JSON](../computations/palindromic_picard_gate_2026_10_31.json).
I checked the relevant Picard input against the
[incidence audit](2026-10-30-projection-elliptic-target-incidence-audit.md)
and the first-gate meaning against the
[canonical-extension criterion](2026-10-31-elliptic-canonical-extension.md)
and [its audit](2026-10-31-elliptic-canonical-extension-audit.md).
The latter conditional theorem is inherited reviewed provisional evidence;
its entire proof was not re-audited here.

The literal input is the fixed quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), characteristic zero, and the single target
over \(K=\mathbf Q(\eta)\), \(\eta^2=-4/5\), with
\(R=t^4+\eta t^3+\eta t+1\). Statements about points and line bundles
are geometric, after algebraic closure. The verifier fixes one embedding
of K; conjugation preserves all its identities and nonvanishing claims.

## Full support and normalization boundary

The code reconstructs \(e_0,e_1,e_2\) from \(R^5\), rather than importing
their values. Primitivity, full bidegree, and
\(\Delta=-3S^2D\) with D a separable quartic prove integrality and the
smooth genus-one normalization \(E:y^2=-3D(A)\). The normalized map uses
\(B=(-e_1+Sy)/(2e_2)\). The equation restricted to \(A=t^3,B=t\) is
exactly \(R^5\), of degree twenty with nonzero constant and leading
coefficients. Its bihomogenization therefore has no missing endpoint
intersection. Coprimality with \(\Delta(t^3)\) makes every marked target
point smooth with a unique normalized inverse point, of contact five.
There are no further inverse points over the fixed quartic.

I checked the boundary arguments behind the assertion labels. A simple
root of either residual boundary quartic is coprime to \(e_1\), so gives
a smooth point and a simple zero or pole of B. At the doubled B-zero
root, write \(x=A-A_0\). The checked factors give
\(e_0=x^2u\), u a unit, while \(e_2\) is a unit and \(\Delta\) has
exact order two. Thus \(e_1\) is divisible by x, and the two normalized
expansions are \(B=c_\pm x+O(x^2)\), with distinct nonzero slopes:
their discriminant is nonzero and their product is nonzero. Both are
simple B-zeros. Applying the same argument to \(1/B\) treats the
doubled B-pole root. The code's evaluations of D and the other factors
of S justify the asserted exact discriminant order.

At A=0, D and S are nonzero and the constant boundary coefficients are
nonzero, so the two normalized points have finite nonzero B. At infinity,
\(x=1/A,v=y/A^2\) gives \(v(0)^2=-15\); there are two distinct points,
each with A of pole order one. The homogenized quadratic in B there has
nonzero constant and leading coefficients and nonzero discriminant, so
B is again finite nonzero at both points. These checks give reduced,
disjoint A- and B-boundaries on the normalization, not merely on its
singular image.

Consequently \(f=B^3/A\) has degree twenty and zero/pole partitions
\((3^6,1^2)\). Its fiber over one is exactly \(5Z\). The three fibers
already contribute \(12+16+12=40=2\deg f\), exhausting genus-one
Riemann--Hurwitz in characteristic zero. No untested extra branch value
is being discarded.

## Picard failure and its geometric extraction

With H the sum of the two infinities, \(L=\mathcal O_E(H)\).
Pole orders give the independent sections \(1,A,A^2,y\) of \(L^2\),
and degree-four elliptic Riemann--Roch proves that they form its full
space. The normalization denominator S is invertible modulo R. The code
checks both the modular y formula and the elliptic equation for the marks.
I independently reconstructed the evaluation matrix using
\[
A=t^3,\qquad A^2\equiv\tfrac45+\tfrac{9\eta}5t-\tfrac95t^2
-\tfrac\eta5t^3,\qquad
y\equiv\tfrac{27}5(1+\eta t+t^2+\eta t^3)\pmod R.
\]
Its remaining two-by-two minor is
\((9\eta/5)(27/5)-(-9/5)(27\eta/5)=486\eta/25\ne0\).
Separability of R identifies quotient-ring vanishing with vanishing at
all four geometric marks. Hence \(H^0(L^2(-Z))=0\) and
\(L^2\not\simeq\mathcal O_E(Z)\). This is an obstruction to the
component polarization required on both smooth and cone sources.
Geometrically, the four marks are not a hyperplane section of the
elliptic normal quartic embedded by \(|2L|\). Its cone is not the
abstract nodal canonical quadric of the inherited criterion. The stated
general interpolation criterion holds when the four finite A-values
are distinct: a vanishing section must have nonzero y coefficient, since
a quadratic polynomial in A cannot vanish at four distinct A-values.
No assertion identifying Z with the A-branch divisor is needed.

I independently recomputed the general Picard identities under the
proposal's complete passport and reduced disjoint boundary hypotheses.
Writing \(\mathcal Z=\mathcal O_E(Z)\),
\(F=f^*\mathcal O(1)=LM^3=\mathcal Z^5\), the ramification class is
\(M^4F\mathcal Z^{-1}\). Riemann--Hurwitz gives
\(F^2=M^4F\mathcal Z^{-1}\), hence \(M=L\mathcal Z\).
It follows that \(\mathcal Z^2=L^4\), so
\(\delta=L^2\mathcal Z^{-1}\) is two-torsion. Its nontriviality here
comes from the evaluation calculation; no multiplication-by-two
cancellation in Picard groups occurs.

All local indices are odd and
\(R_f/2=B_0+B_\infty+2Z\). Therefore
\[
\theta_f=F^{-1}M^2\mathcal Z^2
=\mathcal ZL^{-2}=\delta^{-1}=\delta.
\]
I checked [Eskin--Okounkov--Pandharipande, Sections 1.1.1--1.1.2](https://arxiv.org/pdf/math/0312186)
directly: their opening pullback construction allows a rational target
and defines this theta characteristic by halving the pulled-back
differential divisor; parity is the dimension of sections modulo two.
Their later torus enumeration is not used. On an elliptic curve only the
trivial degree-zero bundle has a section, so the component equality is
equivalent to odd induced spin within the stated hypotheses. This target
has even spin. The equivalent nonsquare statement for \(df/\omega_E\)
follows from its half-divisor class \(\theta_f\).

## Verification, allocation, and limits

I reran the verifier with
`/private/tmp/stci-cas-20261031/bin/python research/computations/verify_palindromic_picard_gate_2026_10_31.py`.
It exited zero under Python 3.15.2 / SymPy 1.14.0 and reproduced the saved
matrix, determinant and dispositions. This rerun is reproducibility
evidence; the argument and boundary reconstruction above supply the
independent review of what those computations establish. The original
Macaulay2 execution and preliminary parameter exploration were not rerun.

**Target replay: PASS. First component Picard gate: FAIL. Residue gluing,
section extension, first-normal contact, carrier construction and mate
descent: NOT RUN.** Target contact five is a verified input, distinct from
the unperformed source first-normal contact test.

Stopping this target is justified by the approved first-failure rule.
The result supplies a reusable geometric explanation: complete contact
can fix a squared polarization while its remaining two-torsion defect is
the induced spin. It neither proves that all covers of this passport have
even spin nor reduces arbitrary STCI pairs to this elliptic construction.
Odd-spin targets remain a constructive possibility, subject to actual
functions A,B and the separate gluing, contact and mate gates. This
failure supplies no mechanism for choosing another target, and does not
justify a cover enumeration or serial narrowing. A future continuation
would need an independently motivated mechanism controlling both spin
and those functions. Unrestricted existence and nonexistence remain open.
