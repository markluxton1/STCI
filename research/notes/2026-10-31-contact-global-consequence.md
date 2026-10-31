# Hamiltonian actions of a supported thick complete intersection

Date: 2026-10-31. Status: **independently reviewed provisional deductions
and a precisely failed extension mechanism**; see the
[bounded audit](2026-10-31-contact-global-consequence-audit.md).
No canonical promotion or unrestricted STCI conclusion.

## 1. Question, sources, and scope

Over an algebraically closed field of characteristic zero, let

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad I=(F_a,G_b),\qquad \sqrt I=I_C,
\]

with a proper complete intersection. The
[reviewed Jacobian/contact theorem](2026-10-31-cyclic-cover-duality.md),
Sections 2–5, supplies the actual homogeneous identity

\[
\{F,G\}=AF+BG,\qquad \deg A=b-2,\quad\deg B=a-2,
\tag{1}
\]

for the symplectic form
\(dx_0\wedge dx_3-2dx_1\wedge dx_2\). Its
[audit](2026-10-31-cyclic-cover-duality-audit.md) is inherited evidence;
the different, Jacobian, and socle proofs are not rerun here.

The attempted new mechanism was to turn (1) into global characteristic
foliations or a Lagrangian deformation argument. Primary literature was
checked before choosing this mechanism:

- [Sevenheck–van Straten, *Deformation of singular Lagrangian
  subvarieties*](https://arxiv.org/pdf/math/0002083), Introduction and
  Section 2, begins with a **reduced** Lagrangian subspace and constructs
  the conormal Lie algebroid and its complex. The complex itself makes
  sense for an involutive ideal.
- [Sevenheck–van Straten, *Rigid and Complete Intersection Lagrangian
  Singularities*](https://arxiv.org/pdf/math/0311503), Theorems 2, 6 and
  14, gives the constant-kernel, rigidity and perversity statements in
  that geometric setting. An everywhere thick scheme is not covered
  merely because its defining ideal is a complete intersection.
- [Garay, *Degenerations of invariant Lagrangian
  manifolds*](https://www.journalofsing.org/volume8/garay.pdf), Section 1,
  distinguishes involutive ideals from the ideals of all level sets of
  a commuting integrable system. Its stability theorem has specific
  singularity and arithmetic hypotheses, not an arbitrary supported-CI
  existence theorem.

The new deduction below shows the failure of the reduced-kernel
mechanism **throughout the entirely thick branch**, rather than just
noting the source's scope. It requires no bound on the orders or degrees,
no choice of carrier, and no normal-flatness assumption. It does not
exclude this branch or assert that every hypothetical pair belongs to it.

## 2. The entirely thick branch has unipotent Hamiltonian actions

Work on \(U=\mathbf A^4\setminus\{0\}\). Let \(L\subset U\) be the
smooth punctured cone over \(C\), let \(X=V(I)\cap U\), and write
\(P=\mathcal I_L\) and \(N=P\mathcal O_X\). Here \(L\) is Lagrangian,
so \(\{P,P\}\subset P\). Assume in this section that

\[
F,G\in P^2\quad\text{as ideal-sheaf sections on }U.
\tag{2}
\]

This is the branch where both carriers are singular along the entire
reduced curve. Ordinary ideal-square membership at the cone vertex is
not assumed or inferred.

**Proposition.** Under (1)–(2):

1. The two induced Hamiltonian derivations
   \(\delta_F=\{F,-\}\) and \(\delta_G=\{G,-\}\) on \(\mathcal O_X\)
   are locally nilpotent. Their exponentials give algebraic additive-group
   actions on \(X\) that fix \(L\) pointwise.
2. Both derivations annihilate the entire socle line
   \(\Sigma=\operatorname{Ann}_{\mathcal O_X}N\).
3. The unique homogeneous cofactors in (1) satisfy
   \(A,B\in I_C\).

**Proof.** Involutivity makes both derivations descend to \(X\). The
Leibniz rule and \(\{P,P\}\subset P\) give

\[
\{P^i,P^j\}\subset P^{i+j-1}\quad(i,j\ge1).
\]

For either \(\delta\), (2) therefore implies

\[
\delta(\mathcal O_X)\subset N,
\qquad \delta(N^j)\subset N^{j+1}\quad(j\ge1).
\tag{3}
\]

The nilradical \(N\) is nilpotent, so a sufficiently high power of
\(\delta\) is zero. The finite sum \(\exp(t\delta)\) defines an
automorphism over \(k[t]\), and its inverse is \(\exp(-t\delta)\).
These maps glue; their reduction is the identity. This proves the
additive-group assertion on the punctured cone. No projective
additive-group action or action across the cone vertex is asserted.

The socle is preserved by any derivation preserving \(N\): differentiate
\(sn=0\), use \(s\delta(n)=0\), and obtain \(\delta(s)n=0\).
Moreover (3) makes the action on \(\Sigma\) \(\mathcal O_L\)-linear.
Duality identifies \(\Sigma\) with an invertible \(\mathcal O_L\)-module.
Locally its endomorphism \(\delta\) is multiplication by one function on
the reduced scheme \(L\). Nilpotence forces that function to vanish.
This proves assertion 2, including at both projective endpoints.

For assertion 3, localize the ambient ring at the generic point of
\(L\). Its maximal ideal is \(P\), its residue field is \(K=k(L)\),
and \(I\) is \(P\)-primary. The two minimal generators give a basis of
the two-dimensional vector space \(I/PI\). The action of \(\delta_F\)
on this space is \(K\)-linear: differentiating a coefficient gives an
element of \(P\), which disappears modulo \(PI\). It is nilpotent.
Indeed, \(P^r\subset I\) for some \(r\), so repeated differentiation
eventually sends \(I\subset P^2\) into
\(P^{r+1}\subset PI\). In the basis \((F,G)\), its matrix is

\[
\begin{pmatrix}0&A\cr0&B\end{pmatrix}\pmod P.
\]

Its trace is zero, hence \(B|_L=0\). The corresponding matrix for
\(\delta_G\) has trace \(-A\), proving \(A|_L=0\). The homogeneous
polynomials \(A,B\) consequently vanish on \(C\). Finally, their
uniqueness follows from the only syzygies of the regular sequence:
two representations would differ by \((HG,-HF)\), but the required
degree of \(H\) would be \(-2\). \(\square\)

Geometrically, these flows move only nilpotent transverse structure;
they supply no nonzero characteristic foliation of the reduced cone.
The sharper cofactor condition \(\{F,G\}\in I_C(F,G)\) is a necessary
consequence in this branch. Its proof is a filtration/nilpotence
argument, not a new incompatibility with global homogeneous equations.

## 3. The actual deformation-complex obstruction

The involutive-ideal complex begins

\[
\mathcal O_X\xrightarrow{d_0}
\mathcal Hom_{\mathcal O_X}(I/I^2,\mathcal O_X),
\qquad d_0(h)(F)=\{F,h\},\quad d_0(h)(G)=\{G,h\}.
\]

The proposition proves the sheaf inclusion

\[
\Sigma\subset\mathcal H^0(\mathcal C_X^\bullet).
\tag{4}
\]

Over \(\mathbf C\), every stalk of \(\Sigma\) is an infinite-dimensional
complex vector space: it is locally the analytic local ring of the
positive-dimensional smooth support, multiplied by a socle generator.
Thus this zeroth cohomology is not a sheaf with finite-dimensional
constructible stalks. In particular, one cannot extend the reduced
constant-kernel/constructible-deformation argument to the thick branch
by citing complete-intersection hypotheses alone. Statement (4) does
not calculate \(\mathcal H^1\), prove that all deformations exist, or
assert that no useful modified complex can be constructed.

The basic local model makes the geometry visible. In a cotangent chart
with symplectic coordinates \((q_1,q_2,p_1,p_2)\), use
\(I=(p_1^2,p_2^2)\). The actions shift the base coordinates by nilpotents.
Every function \(h(q_1,q_2)p_1p_2\) lies in the common Hamiltonian kernel.
These are infinitesimal functions on the support, not locally constant
functions describing a reduced characteristic foliation.

## 4. Commuting homogeneous generators are an additional requirement

Involutivity of \((F,G)\) does not imply that the level-set family is
involutive. In \(R[\lambda,\mu]\), consider
\(J=(F-\lambda,G-\mu)\). Its quotient is \(R\), with
\(\lambda\mapsto F\), \(\mu\mapsto G\). Consequently

\[
\{J,J\}\subset J\quad\Longleftrightarrow\quad\{F,G\}=0.
\tag{5}
\]

There is an actual everywhere-thick homogeneous Legendrian CI for
which no homogeneous generating pair of the same ideal can commute.
This is a stronger control than merely observing a nonzero bracket in
one presentation. For the twisted cubic, put

\[
f=x_0x_2-x_1^2,\qquad
g=x_2^3-2x_1x_2x_3+x_0x_3^2.
\]

The inherited contact note verifies
\(\sqrt{(f,g)}=I_T\) for \(T=[s^3:s^2t:st^2:t^3]\), and, for
\(dx_0\wedge dx_3-3dx_1\wedge dx_2\),

\[
\{f,g\}=\tfrac43x_3f.
\]

Now take the proper degree-\((6,6)\) complete intersection

\[
J=(f^3,g^2),\qquad \sqrt J=I_T,
\qquad \{f^3,g^2\}=8x_3 f^3g\ne0.
\tag{6}
\]

Both generators lie in \(I_T^2\). Every homogeneous two-generator
presentation of this same graded ideal has degrees \((6,6)\), and its
generators are an invertible constant linear combination of
\((f^3,g^2)\): the degree-six piece is exactly their two-dimensional
span. Its Poisson bracket is the nonzero bracket in (6), multiplied by
the nonzero determinant. Hence no such presentation yields a commuting
pair or the level-set family in (5). This statement concerns this ideal;
it does not rule out a different supported ideal on \(T\).

## 5. Disposition and missing bridge

This attempt establishes a uniform geometric description of the
Hamiltonian actions in the entirely thick branch, sharpens its cofactor
membership, and identifies two concrete failures of a proposed route:
the socle prevents a direct use of the reduced constant-kernel theory,
and even actual homogeneous supported Legendrian CIs need not admit
commuting homogeneous generators of their defining ideal.

The missing step remains quartic-specific: a global obstruction to the
actual homogeneous cofactor identity, or a construction satisfying it,
must use more than the nilpotent Hamiltonian actions and reduced
Lagrangian deformation results. No residual component, retraction,
torus invariance, quantization, or unrestricted degree exclusion follows
from the arguments here. The order-one branch has not been excluded.
No further case enumeration is proposed by this note.

No numerical calculation, inherited verifier rerun, or canonical-record
change was performed. Independent review reconstructed the punctured-cone
boundary, finite exponential and gluing, generic conormal trace argument,
socle linearity, and the scope of the noncommuting homogeneous-presentation
control. No material correction was required. The audit also verifies the
reduced deformation literature's hypotheses; it does not infer an STCI
obstruction from their failure here.

## 6. Quantization of the smooth cone and a supported-cohomology limit

October 31 continuation. The deductions below are independently reviewed
and provisional; they do not assume an STCI pair exists.
Sections 1–5 and their audit remain inherited evidence.

### 6.1 Every line bundle on the smooth punctured cone quantizes

Put \(Y=\widehat C_0\setminus\{0\}\subset
U=\mathbf A^4\setminus\{0\}\), with the symplectic form of §1.
For the constant Moyal quantization \(\mathcal O_\hbar\) on U,
every line bundle L on Y has a complete flat module quantization
whose reduction is \(i_*L\).

Indeed \(Y=\mathcal O_{\mathbf P^1}(-4)^\times\). Removing the
zero section from this line bundle gives
\(\operatorname{Pic}(Y)=\mathbf Z/4\). Thus the additive
Atiyah–Chern classes of L and \(K_Y\) vanish even in the
**truncated** de Rham group
\(\mathbb H^2(Y,\Omega_Y^{\ge1})\), a characteristic-zero vector space.

The constant Moyal product has a global module splitting, symmetric
second coefficient and zero transition derivations. The cocycle in
[Baranovsky–Ginzburg–Kaledin–Pecharich, Remark 5.3.4](https://arxiv.org/pdf/1403.3493)
therefore gives \(\operatorname{At}(\mathcal O_\hbar,Y)=0\) in
that same truncated group. All higher period classes vanish:
the quantization restricts from affine four-space, whose
\(H^2_{\rm dR}\) is zero. Consequently the two conditions of
their Theorem 1.1.4 hold:
\[
c_1(L)-\tfrac12c_1(K_Y)=\operatorname{At}(\mathcal O_\hbar,Y)=0,
\qquad i^*\omega_j=0\quad(j\ge2).
\]
This proves the stated existence. Ordinary de Rham vanishing
alone would not justify the truncated-class equality.

The argument extends to the punctured cone of any smooth rational
Legendrian curve in this constant symplectic four-space: positive
hyperplane degree d gives Picard group \(\mathbf Z/d\). It does not
quantize a thick quotient \(\mathcal O_U/(F,G)\), whose reduced
ideal acts nontrivially. No equivariant structure, filtered Weyl
module, or extension across the cone vertex is supplied.
Geometrically, smooth half-canonical/period compatibility is
available; it cannot obstruct the desired thick equations.

### 6.2 Rational supported Chern classes have only one possible degree

Over \(\mathbf C\), let \(V=\widehat C_0\subset\mathbf A^4\),
including its vertex. Its link is the circle bundle of Euler
number \(-4\) over \(S^2\), hence a rational homology three-sphere.
The one-point compactification of V is the suspension of its
link. Borel–Moore homology and ambient duality therefore give
\[
H_j^{BM}(V,\mathbf Q)=
\begin{cases}\mathbf Q&j=4,\\0&j\ne4,\end{cases}
\qquad
H^r_V(\mathbf A^4,\mathbf Q)=
\begin{cases}\mathbf Q&r=4,\\0&r\ne4.\end{cases}
\tag{7}
\]
For clarity, this is **rational** concentration. Integrally the
link has \(H_1=\mathbf Z/4\), so
\(H^{BM}_2(V,\mathbf Z)=\mathbf Z/4\) and
\(H^6_V(\mathbf A^4,\mathbf Z)=\mathbf Z/4\) also survive.

Every coherent sheaf supported on V consequently has its supported
de Rham Chern character concentrated in degree four, without any
quantization hypothesis. For a supported CI, the surviving class
is \(m[V]\), with \(m=ab/4\). This calculation includes the vertex;
it does not identify vertex phenomena with a projective residual.
It generalizes to the cone over every smooth rational projective
curve of positive degree d in P3, with integral torsion \(\mathbf Z/d\).
The Lagrangian hypothesis is unnecessary for (7).

[Baranovsky–Ginzburg, ZAG Handbook, Theorem 11.1, pp. 41–44](https://api.pageplace.de/preview/DT0400.9781040378878_A50830332/preview-9781040378878_A50830332.pdf)
announces supported trace-density vanishing for general coherent
modules **assuming flat quantizability**. In this dimension and
support dimension its conclusion is exactly concentration in
degree four. The chapter sends the full proof to a work listed as
in preparation. The conclusion is already automatic by (7), even
if that theorem and the missing quantizability premise are granted.
The elementary topological deduction here does not depend on the
announced theorem.

### 6.3 The missing full-module and filtered bridges

The checked additional sources do not provide quantization of an
arbitrary supported CI quotient. [Baranovsky–Ginzburg–Pecharich,
Theorem 7 and Corollary 13](https://arxiv.org/pdf/0909.5520)
concern bundles on smooth coisotropic supports.
[Garay–van Straten, Theorem 1](https://arxiv.org/pdf/0802.1647)
requires a commuting integrable system and torsion-free obstruction
module; §4 already shows why involutivity does not supply commuting
homogeneous generators.
[Baranovsky–Huey, §§1.1–2 and 7](https://arxiv.org/pdf/2607.12910)
extends existing finite-order quantizations of bundles locally free
on the symplectic ambient variety. Its morphism-lifting discussion
does not produce a quantized Koszul complex with flat cokernel.

Even a formal quantization would need an equivariant/algebraization
argument before becoming a Bernstein-filtered Weyl module; setting
the formal parameter to one is not defined in general. Stafford's
two-generator theorem, as implemented by
[Leykin, Theorems 3 and 6 and §§4–5](https://arxiv.org/pdf/math/0204303),
does not guarantee a two-symbol presentation of the characteristic
ideal. For example, the left ideal
\[
A_2\partial_1+A_2\partial_2
=A_2P+A_2Q,\qquad
P=\partial_1,\quad Q=x_1\partial_1+\partial_2,
\]
has associated graded ideal \((\xi_1,\xi_2)\) under the Bernstein
filtration, whereas its displayed symbols generate only
\((\xi_1,x_1\xi_1)=(\xi_1)\). The missing symbol is recovered by
the cancellation \(Q-x_1P=\partial_2\). This explains the
filtered-presentation gap, not a failure of the two-generator theorem.

No operator, local-algebra or quantization classification is selected.
Reopening requires an actual full-module construction together with
control of its principal-symbol support, or a finer invariant linked
by a proved implication to arbitrary homogeneous pairs. The rational
test is exhausted here; unstable, integral and equivariant refinements
are not claimed exhausted. STCI existence remains live.
