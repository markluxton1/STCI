# Independent audit of the Hamiltonian actions and failed extension mechanism

Date: 2026-10-31. Reviewer: independent mathematical audit agent.
Status: **passes independent reconstruction on the stated entirely thick
branch**. No canonical promotion or unrestricted STCI conclusion.

Reviewed source:
[Hamiltonian actions of a supported thick complete intersection](2026-10-31-contact-global-consequence.md),
Sections 1–5, 243 lines, SHA-256
`0fd2a26cf4aedc5b32b07861828ff47afdc3527e176a67108659ea677a2cbf4f`.
The [previous contact-identity audit](2026-10-31-cyclic-cover-duality-audit.md)
and its exact twisted-cubic pair are reused as inherited evidence; their
proof histories and certificates were not rerun.

## 1. Exact hypotheses and filtration

Let \(k\) be algebraically closed of characteristic zero. On
\(U=\mathbf A^4\setminus\{0\}\), let \(L\) be the smooth punctured
cone over the fixed quartic, \(P=\mathcal I_L\),
\(X=V(F_a,G_b)\cap U\), and \(N=P\mathcal O_X\). Assume sole reduced
support, proper complete intersection, the inherited involutivity
identity \(\{F,G\}=AF+BG\), and **ordinary ideal-sheaf** membership
\(F,G\in P^2\) on \(U\). No ordinary-square membership at the vertex
is inferred. This distinction is correctly preserved by the source.

For a Lagrangian smooth support, \(\{P,P\}\subset P\). Expanding
products by the Leibniz rule gives
\[
\{P^i,P^j\}\subset P^{i+j-1}\quad(i,j\ge1),
\qquad \{P^2,\mathcal O_U\}\subset P.
\]
Thus either induced Hamiltonian derivation \(\delta\) satisfies
\[
\delta(\mathcal O_X)\subset N,\qquad
\delta(N^j)\subset N^{j+1}\quad(j\ge1).
\]
The second inclusion uses both square membership and involutivity of
the reduced support; the first uses square membership alone.
Involutivity of the actual ideal makes the derivations descend to
\(X\). These are statements about the actual nilpotent ideal, not its
associated graded algebra.

The quasi-compact Noetherian scheme \(X\) has \(N^r=0\) for one
uniform \(r\). Consequently \(\delta^r=0\) on its sheaf of rings.
The finite exponential is a ring homomorphism
\(\mathcal O_X\to\mathcal O_X[t]\), has inverse obtained from
\(-t\), and satisfies the addition law by the binomial identity.
On affine opens it defines an action; these maps glue since they come
from the same sheaf derivation. Their reduction is the identity, so
the underlying reduced open sets are preserved. This proves the
algebraic \(\mathbf G_a\)-actions claimed on the punctured thick scheme.
They are permitted to be trivial.

There is no deduction of a projective action here. A homogeneous
Hamiltonian derivation has degree \(a-2\) or \(b-2\), generally not
zero, so its exponential need not commute with the scalar action used
to form the projective quotient. No claim about extension across the
vertex is required or established by this audit.

## 2. The entire socle and the cofactor trace

Put \(\Sigma=\operatorname{Ann}_{\mathcal O_X}N\). It is an invertible
module on smooth \(L\), by the same closed-immersion duality used in the
inherited socle calculation. Every derivation preserving \(N\)
preserves \(\Sigma\): differentiating \(sn=0\) gives
\(\delta(s)n=-s\delta(n)=0\). For \(s\in\Sigma\),
\[
\delta(as)=a\delta(s)+\delta(a)s=a\delta(s)
\]
because \(\delta(a)\in N\). Hence the action on \(\Sigma\) is
\(\mathcal O_L\)-linear. An endomorphism of an invertible module is
locally multiplication by a regular function on \(L\); nilpotence and
reducedness force that function to be zero. This proves annihilation
of the **entire** socle, including both endpoint neighborhoods, without
identifying it with an ordinary top power of \(N\).

For the cofactor argument, localize the ambient regular ring at the
generic point of \(L\). Its maximal ideal is \(P\), the residue field
is \(K=k(L)\), and \(I=(F,G)\) is \(P\)-primary. A height-two regular
sequence is a minimal generating pair there, so \(I/PI\) is
two-dimensional over \(K\). The induced Hamiltonian action is
\(K\)-linear because its derivative on every ambient coefficient lies
in \(P\). It is nilpotent: for \(P^r\subset I\), sufficiently many
derivatives send \(I\subset P^2\) into
\(P^{r+1}\subset PI\).

In the ordered basis \((F,G)\), \(\delta_F\) has matrix
\(\left(\begin{smallmatrix}0&A\\0&B\end{smallmatrix}\right)\)
modulo \(P\), whose trace is \(B\); \(\delta_G\) has trace \(-A\).
Nilpotence gives \(A,B\in P\) at the generic point. Since these are
homogeneous polynomials and the support is integral, they vanish on
the whole cone and belong to \(I_C\). The source correctly claims the
stronger branch-specific membership
\(\{F,G\}\in I_C(F,G)\).

The cofactors with the indicated homogeneous degrees are unique:
their difference would be a Koszul syzygy \((HG,-HF)\) with
\(\deg H=-2\). This use of uniqueness concerns the fixed homogeneous
pair and its prescribed cofactor degrees.

## 3. The deformation complex and the exact literature boundary

The conormal Lie-algebroid operations descend for any involutive ideal:
\(\{I^2,I\}\subset I^2\) and \(\{I^2,\mathcal O_U\}\subset I\)
make both operations independent of representatives. Thus the displayed
initial differential is defined even for this nonreduced scheme.
Its kernel is the common Hamiltonian kernel, and the preceding proof
indeed gives
\[
\Sigma\subset\mathcal H^0(\mathcal C_X^\bullet).
\]
Analytically over \(\mathbf C\), each stalk of this socle line is a
free rank-one module over the local ring of a positive-dimensional
smooth support. It is infinite-dimensional as a complex vector space.
The zeroth cohomology therefore cannot have finite-dimensional
constructible stalks. No assertion about first cohomology or existence
of deformations follows from this inclusion.

The sources were checked directly. The Introduction of
[Sevenheck–van Straten, *Deformation of singular Lagrangian subvarieties*](https://arxiv.org/pdf/math/0002083)
explicitly starts with reduced analytic support. In their subsequent
[rigidity paper](https://arxiv.org/pdf/math/0311503), Theorem 2 gives
the constant zeroth kernel, Theorem 3 imposes Condition P for
constructibility, and Theorem 6 imposes further rigidity hypotheses.
Theorem 14's Lagrangian-variety setting does not authorize substituting
an everywhere thick scheme into that package of conclusions.

There is also a direct check of the missing Condition P here. At every
closed point of the entirely thick branch, both equations have zero
linear part in the smooth four-dimensional ambient space. Thus the
embedding dimension of \(X\) is four everywhere, and the stratum
called \(S_0\) in that paper has dimension two, violating its required
dimension bound. This is consistent with the independently proved
failure of finite constructible stalks; it is not a counterexample to
the cited theorems under their hypotheses.

The cotangent-chart control \((p_1^2,p_2^2)\) checks the meaning of
the failure: Hamiltonian actions shift the base by nilpotents, while
every \(h(q_1,q_2)p_1p_2\) lies in their common kernel. That kernel
contains functions varying along the reduced support, rather than
only locally constant functions of its characteristic foliation.

## 4. Level sets and the noncommuting homogeneous control

With \(\lambda,\mu\) central, the quotient by
\((F-\lambda,G-\mu)\) in \(R[\lambda,\mu]\) is \(R\), through
\(\lambda\mapsto F\), \(\mu\mapsto G\). The generator bracket
maps to the actual polynomial \(\{F,G\}\). Leibniz therefore proves
the claimed equivalence between involutivity of this universal
level-set ideal and \(\{F,G\}=0\). Involutivity of the zero-level
ideal alone is weaker. This matches the distinction in
[Garay, Sections 1–2](https://www.journalofsing.org/volume8/garay.pdf);
his stability theorem is not used as an existence theorem here.

For the inherited twisted-cubic pair \(f,g\), its already checked
bracket is \(\{f,g\}=\tfrac43x_3f\). Independently applying the
Leibniz rule gives
\[
\{f^3,g^2\}=6f^2g\{f,g\}=8x_3f^3g\ne0.
\]
The proper complete intersection \(J=(f^3,g^2)\) has degrees
\((6,6)\), reduced support the twisted cubic, and both generators
in its reduced ideal square. Its degree-six component is exactly the
two-dimensional span of \(f^3,g^2\), and it has no lower-degree
elements. Any homogeneous two-generator presentation must therefore
have both degrees six and differ by an invertible constant matrix.
Its bracket is multiplied by the nonzero determinant and cannot
vanish. This proves the stated failure for **all homogeneous generating
pairs of this same ideal**, without making a claim about nonhomogeneous
presentations, local changes of generators, or different supported
ideals on the twisted cubic.

## 5. Disposition and geometric effect

All new mathematical deductions in the reviewed source pass. No
material correction is required. The action is on the punctured thick
cone; square membership is on that punctured ambient scheme; the
cofactor and noncommuting-control claims retain their exact global
homogeneous meaning. Verification was by hand reconstruction and
primary-source inspection; no numerical calculation, inherited
verifier rerun, or canonical-record change was performed.

The geometry is a uniform description of the entirely thick branch:
Hamiltonian motions only move nilpotent transverse structure, kill
its actual socle line, and force nilpotent cofactor values. The large
socle kernel obstructs direct transfer of the reduced deformation
complex's constant-kernel/constructibility mechanism. The twisted-cubic
control separately shows that homogeneous involutivity need not be
replaceable by commuting homogeneous equations of the same ideal.

Neither finding conflicts with existence of an actual supported pair.
The missing bridge is still a quartic-specific incompatibility or a
construction involving the actual global homogeneous equations. The
order-one branch is outside these new deductions. This audit supports
reviewed provisional status only.
