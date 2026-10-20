# A finite normal-jet certificate for a fixed pair of surface degrees

Date: 2026-09-06 (America/New_York).
Operation: direct lead proof, independently audited by a bounded worker.
Epistemic status: proved here from standard local algebra and projective degree
formulas; no claim of literature novelty or a solution of the universal STCI problem.

## Question and research delta

Artifact 010 correctly showed that leading tangent forms do not determine later
intersection multiplicities. It left the absence of a justified finite truncation as
a reason not to compute further. This intervention separates two questions:

- At fixed surface degrees, how much normal information suffices?
- Can any finite list of degrees exhaust the STCI question for a given curve?

The first now has an exact answer, including singular integral curves and reduced
reducible curves. The second remains open in general. The certificate uses actual
global forms and exhausts the global degree budget; it does not infer globalization
from arbitrary normal germs.

## 1. Local finite-length lemma

Let (R,m) be Noetherian local, J an ideal, and B a positive integer. If
\[
 t=\operatorname{length}_R R/(J+\mathfrak m^{B+1})\le B,
\]
then R/J has finite length t, and \(\mathfrak m^t\subset J\).

Indeed, put T=R/J and n=mT. The B+1 successive factors
\(n^i/n^{i+1}\), for \(0\le i\le B\), have total length t. At least one
factor vanishes. Nakayama applied to the finite T-module \(n^i\) gives
\(n^i=0\), so the truncation already equals T. The same no-gap argument
shows that a length-t local ring has \(n^t=0\).

This is a direct consequence of [Nakayama's lemma, Stacks 00DV](https://stacks.math.columbia.edu/tag/00DV)
and additivity of length, [Stacks 00IU](https://stacks.math.columbia.edu/tag/00IU).
No regularity, dimension, or number-of-generators hypothesis is needed in this lemma.

## 2. Integral-curve certificate

Let C be an integral curve of degree d in \(\mathbf P^3_k\), k algebraically
closed. Let F,G be nonzero homogeneous forms in \(I_C\), of positive degrees
a,b. Put \(R=\mathcal O_{\mathbf P^3,\eta_C}\) and
\(\mathfrak m=I_CR\). Trivialize the two line bundles at the generic point
when forming the ideal \(J=(F,G)R\).

If d does not divide ab, this pair cannot define C set-theoretically.
Otherwise put \(M=ab/d\). Then
\[
 \boxed{\quad
 V_+(F,G)_{\mathrm{red}}=C
 \quad\Longleftrightarrow\quad
 \operatorname{length}_R R/(J+\mathfrak m^{M+1})=M .
 \quad}                                                     \tag{1}
\]

No separate coprimality, smoothness of C, transverse-leading-form, or
non-thick hypothesis is required.

### Proof

If the support equals C, F,G have no common surface factor. They form a
regular sequence and define a degree-ab complete intersection whose only
curve component is C. Thus its generic length is M. A length-M local
algebra is annihilated by \(\mathfrak m^M\), proving the forward implication.

Conversely the local lemma makes the actual generic length M. Write
\(F=HF'\), \(G=HG'\), with H their homogeneous gcd, of degree e.
If H vanishes along C, J is contained in a proper principal ideal of the
two-dimensional regular local ring R, contradicting finite colength.
Thus H is a unit in R, and primality of \(I_C\) gives \(F',G'\in I_C\).
They are coprime, of positive degrees a-e,b-e, and retain local length M.
Their complete intersection therefore has
\[
 ab=dM\le(a-e)(b-e).
\]
This forces e=0. The degree-ab intersection of F,G is now exhausted by
the multiplicity-M contribution of C. Any further curve would add
positive degree. No surface component exists, and every minimal prime
over a coprime two-generated ideal in the polynomial ring has height
exactly two, so there are no isolated support components. This proves (1).

For completeness, the degree formula follows from
\[
 H_{S/(F,G)}(t)=\frac{(1-t^a)(1-t^b)}{(1-t)^4}.
\]
The degree of a pure curve scheme is the sum of its generic lengths times
the degrees of its reduced components. The generic-length convention is
the [associated cycle of a coherent sheaf, Stacks 02QV](https://stacks.math.columbia.edu/tag/02QV).
This explains exactly where global projective geometry enters the proof.

### The extra order is necessary

For the line \(C=V(x,y)\), take \(F=xz^{M-1}\), \(G=x\).
Then \(d=1\), \(ab=M\), and at its generic point J=(x). Modulo
\(\mathfrak m^M\) the quotient has length M, although the common zero
set is the plane x=0. Modulo \(\mathfrak m^{M+1}\) its length is M+1,
correctly rejecting the pair. Thus the exponent M+1 is uniformly sharp
without an additional proper-intersection hypothesis.

If coprimality has already been established, Bézout gives actual length
at most M, so exponent M suffices. The pair (x,\(y^M\)) shows why smaller
exponents do not uniformly recover the full multiplicity of valid pairs.

## 3. A finite matrix, with its global parameters retained

R is regular local of dimension two with residue field \(K=k(C)\).
Choose a coefficient field in its completion and normal parameters u,v.
The [equal-characteristic regular Cohen structure theorem](https://stacks.math.columbia.edu/tag/0C0S)
gives \(\widehat R\simeq K[[u,v]]\). These choices are not canonical.
A section compatible with k can be chosen using a separating transcendence
basis and a separable lift; arbitrary lifts of residues are insufficient.

Set \(N=M+1\),
\[
 A_N=K[u,v]/(u,v)^N,\qquad D=\dim_K A_N=N(N+1)/2.
\]
The images f,g of the actual global forms determine
\[
 T_{F,G}:A_N\oplus A_N\longrightarrow A_N,\qquad
 (h_1,h_2)\longmapsto h_1f+h_2g.
\]
In the basis \(u^iv^j\), \(i+j<N\), this is a finite multiplication
matrix, and (1) is precisely
\[
 \operatorname{rank}_K T_{F,G}=D-M.                           \tag{2}
\]
All monomial multiples must be included. The span of just the two jet
coefficient vectors is not the ideal they generate.

For a fixed C,a,b, choose bases of the finite-dimensional k-vector spaces
\(H^0(\mathcal I_C(a))\) and \(H^0(\mathcal I_C(b))\).
Writing F,G with scalar parameters in k makes matrix entries linear in
those parameters with coefficients in K. Exact rank is a finite locally
closed condition: larger minors vanish identically in K and some required
minor is nonzero in K. Each minor uses a finite-dimensional k-span of
coefficient functions, so these identities and nonidentities become
finitely many polynomial conditions over k.

This gives an exhaustive finite description of the witness locus at
fixed degrees. It is an in-principle description, not a complexity bound
or an implemented general solver. Over a nonrational curve, K must retain
its actual algebraic relations. Replacing scalar parameters in k by
arbitrary parameters in K changes the problem: Artifact 012 gives an
explicit family of false positives from that relaxation.

## 4. Reduced reducible curves

For \(C=\bigcup_i C_i\), retain each degree \(d_i\), generic local ring
\((R_i,\mathfrak m_i)\), and \(J_i=(F,G)R_i\). Define
\[
 B_i=\lfloor ab/d_i\rfloor,\qquad
 t_i=\operatorname{length}_{R_i}
       R_i/(J_i+\mathfrak m_i^{B_i+1}).
\]
Then the corresponding exact test is
\[
 \boxed{\quad V_+(F,G)_{\mathrm{red}}=C
 \quad\Longleftrightarrow\quad \sum_i d_i t_i=ab.\quad}       \tag{3}
\]
The equality implies \(t_i\le B_i\), so the local lemma recovers all
actual lengths. A gcd cannot contain any component; removing a nonconstant
one would preserve the weighted length sum while strictly lowering the
available degree. The support-exhaustion proof then applies as before.
If any \(B_i=0\), equality is impossible since \(t_i\ge1\).

Component multiplicities need not coincide. For example (z,\(x^2y\))
supports two intersecting lines with multiplicities two and one. Dividing
ab by the total reduced degree and assigning that average to every
component would incorrectly reject such examples.

## 5. Validation and strategic interpretation

The independent audit is preserved as
WORKER-20260906-finite-jet-audit.md in the provisional directory.
The lead checked its Nakayama step, gcd argument, sharpness examples,
coefficient-field qualifications, and weighted reducible extension.
The reproducible script scripts/finite_normal_jet_certificate.m2 checks:

- the twisted-cubic positive control, both by ideal containments and jets;
- the exact generic lengths in the binomial characteristic comparison;
- a shared-surface false positive at an insufficient cutoff;
- the global-coefficient trap of Artifact 012.

The former blanket statement that no justified finite truncation is
available is superseded at fixed degrees. Its uniform meaning survives:
N grows with ab, and there is no supplied bound on witness degrees.
Degree-by-degree emptiness, finite-field samples, and unrestricted
function-field jet solutions still cannot decide global nonexistence.

The next informative use is a structured family of actual homogeneous
forms with a justified geometric degree range, or an obstruction to the
global image of its jet maps. Merely increasing degree searches is not a
new research strategy.
