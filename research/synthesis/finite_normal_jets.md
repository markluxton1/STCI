# Exact finite normal-jet tests at fixed degrees

These are independently audited local-algebra and degree-exhaustion deductions, retained at their full scope: arbitrary characteristic, integral curves including singular curves, and a weighted reduced-reducible extension. They are not a bound on possible STCI degrees or an implemented all-degree solver.

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


## Scope and evidence

The proof needs no computational certificate. The independently checked Nakayama, gcd, sharpness and global-coefficient arguments establish the criterion. No finite truncation uniform in all degrees is supplied. In particular the k-valued source parameters cannot be relaxed to arbitrary k(C)-valued parameters. The fixed sextic [R-0025](../results/ci_fixed_sextic_jet_rigidity.md) is a separate exact actual-source kernel computation, rather than an execution of a general solver.


## Candidate A: a single nonsaturated first-relation defect in degree (6,12)

**Focused question.** Can an actual homogeneous pair of degrees \((6,12)\), with sole reduced support the fixed characteristic-zero quartic, have full generic ordinary initial CI \((2,9)\), with a first-relation saturation defect of length one and saturated movement one?

This is a deliberately narrow slice of the open nonsaturated-first-relation frontier. It does not claim to be the first possible pair in a global ordering, or to exhaust nonsaturated cases.

**Exact authority boundary.** [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md) is promoted and proves a defect/resultant budget under actual lci, sole smooth support, and a full generic binary-CI initial algebra. It does not exclude nonsaturated first relations. [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) assumes saturation, and [STCI-R-0013](../results/saturated_actual_generator_movement.md) excludes movement one only in that saturated class. Consequently R0013 cannot dispose of the proposed slice. The general non-CI-initial-ideal cases remain separate; this candidate still assumes a full generic CI.

The exact identities used next are in the accepted evidence for R0016, [first-relation defect investigation](../supplements/FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-first-relation-defect-investigation), sections 3–5. Its historical provisional label does not independently promote its contents, but R0016 explicitly links the proof and its independent audits. The new numerical application below is provisional.

Let \(R_{\mathrm{sat}}=\mathcal O(-14-\epsilon)\), let \(D\) have length \(\delta\), and use the evidence notation \(c_j\) for saturated generation defects. The socle line of an actual degree-\((a,b)\) CI has degree \(\ell=14-4(a+b)\). With \((a,b;r,s)=(6,12;2,9)\), its degree identity gives

\[
2(-58)=2(8)(-14)-7(-14-\epsilon)+c_8,
\qquad c_8=10-7\epsilon.
\]

Effectivity and \(\epsilon\ge0\) leave \((\epsilon,c_8)=(0,10)\) or \((1,3)\). In the second case the resultant equation gives

\[
\deg\Delta=c_8-2c_9=3-2c_9,
\qquad c_9=0\text{ or }1.
\]

Thus its resultant degree is three or one. For \(\delta=1\), the general bound \(c_8\le\binom72\delta\) does not contradict either value. These are necessary arithmetic possibilities, not existence evidence.

**Concrete unresolved actual-source incidence.** Use the actual sextic second-symbol image, already computed with rank 22 and kernel \(kq^3\) in the independently reviewed [sextic symbol map](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-symbol-map). Its symbol calculation is reusable independently of the saturated \((2,12)\) application advertised in that note.

Parameterize a full movement-one quadratic root

\[
f=(A_0+A_1z)U^2+(B_0+B_1z)UV+(C_0+C_1z)V^2,
\]

with homogeneous endpoint charts retained, and a point \(p\) supporting \(D\). Impose that the second symbols of actual global \(F_6,G_{12}\) are multiples of \(f\), with common multiplier divisor exactly \(p\), so that their actual first kernel is \(R_{\mathrm{sat}}(-p)\). The raw multiplier degrees are nine and 33; after removing their common linear factor, the degrees are eight and 32 and the remaining two sections must have no common zero.

Next divide the truncated normal expansion of \(G_{12}\) by the actual \(F_6\) over \(k(C)\), retaining all global coefficients as constants in \(k\). Force the remainder through normal degree eight to vanish and test that its degree-nine term is coprime to \(f\). For each supplied sextic this is a finite linear test on the actual degree-twelve source. The unknown sextic/root parameters make the total incidence nonlinear, but finite.

The generic cluster energy would then be \(2\cdot9=18\), spending all degree \(72\) on \(C\). A proper global solution would therefore be highly consequential and needs independent audit; there is no asserted solution. A useful negative result could show that every solution factors through \(F_6\), violates the one-point defect condition, or has a forced extra initial relation. Failure to solve the incidence proves nothing.

The simplest local warning remains the accepted source family \((txy+x^3+y^4,xy^2)\): it is finite-flat with constant length ten while the first relation degenerates. Its generic complete-ideal cluster has energy \(4+3+3\), whereas the special cluster has energy \(9+1\). This elementary new cluster reading illustrates that constant energy permits substantial redistribution. The local \((2,5)\) model is a benchmark, not a surviving global degree row.
