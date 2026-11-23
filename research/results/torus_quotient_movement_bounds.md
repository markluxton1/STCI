---
id: STCI-R-0072
type: result
title: Lower bounds on transverse movement from the actual defining equations
scope: "#scope"
statement: "#statement"
proofs:
  - name: multiplier rank and the splitting of the moving quotient
    at: "#proof"
    using: [STCI-R-0020, STCI-R-0042, STCI-R-0084]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Lower bounds on transverse movement from the actual defining equations

## Scope

Fix \(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an algebraically closed field of characteristic zero. Start with a proper homogeneous pair of degrees \(a\le b\) through \(C\). Its cycle is \(m[C]+R\), with \(4m+\deg R=ab\). The bounds below are necessary if \(R=0\). They apply in every bidegree, with arbitrary singularities and arbitrary generic transverse algebra. The [degree exclusion](quartic_carrier_exclusion.md) gives \(a\ge5\) for such a pair.

Write \(Z=V(F,G)\), \(J=(F,G)\). Under sole support the [entire finite modification](../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification) gives a finite flat family over \(\mathbf P^1_r\) of rank \(m=ab/4\). Its algebra \(\mathcal B\) is a quotient of \(A\otimes\mathcal O\), where \(A=k[U,V]/(U,V)^m\). These are *fixed* coordinates on the torus chart \([1:r:r^3(1+U):r^4(1+V)]\). Write \(K_x=\ker(A\to B_x)\) for its fiber kernels. Split the globally generated bundle as \(\mathcal B=\bigoplus_i\mathcal O(\beta_i)\), \(\beta_i\ge0\), and write \(e=\sum_i\beta_i\) for its Plücker degree.

## Statement

Set \(q=\lfloor b/a\rfloor\) and \(L_j=\lceil(4(a+b-ja)-7)/7\rceil\) for \(1\le j\le q\). Every such sole-support pair satisfies
\[
 \#\{i:\beta_i\ge j\}\ \ge\ L_j,\qquad
 e\ \ge\ \sum_{j=1}^{q} L_j.                                      \tag{1}
\]
For general \(x,y\in\mathbf G_m\), the common quotient \(A/(K_x+K_y)\) has length at most \(m-L_1\). At a general \(x\), a nonzero tangent vector to the base induces a linear map \(K_x\to B_x\) of rank at least \(L_1\). Explicitly, for the classifying map \(f:\mathbf P^1\to\operatorname{Gr}(A,m)\) to the Grassmannian of rank-\(m\) quotients, \(df_x(v)\) is an element of \(\operatorname{Hom}(K_x,B_x)\). The bound counts the dimension of its image in \(B_x\). The classifying map itself has image of dimension at most one.

The secant bound also holds along the fixed involution, rather than only
for independently general fibers:
\[
 \dim_k A/(K_r+K_{-r})\le m-L_1
 \qquad\text{for general }r\in\mathbf G_m.             \tag{1a}
\]
In particular the embedded quotient family cannot factor through
\(r\mapsto r^2\). For \((6,6)\), the common quotient of the fibers at
\(r,-r\) has length at most six. This does not increase the Plücker
bound in (1); it restricts a specified pair of fibers of the same family.

For example, \((6,6)\) requires at least three positive summands and general fibers of length nine share a quotient of length at most six. For \((6,16)\) there must be at least nine summands of degree at least one and at least five of degree at least two, giving \(e\ge14\). The latter assertion covers every actual sole-support pair in that bidegree, including all normal orders. At fixed \(a\) the lower bound in (1) grows as \(2b^2/(7a)+O_a(b)\), by summing the arithmetic progression and bounding each rounding error by one.

## Proof

**The generic image of a homogeneous multiplier.** Let \(P\) have ordinary degree \(d\) and nonzero restriction to \(Z\). Write \(X=V(J:P)\) and \(\ell=\dim_{k(C)}(P\mathcal O_{Z,\eta_C})\), using the torus parameter for the coefficient field. Multiplication embeds \(\mathcal O_X\hookrightarrow\mathcal O_Z(d)\). Thus \(X\) is a pure curve on \(C\) of generic length \(\ell\). Let \(l\) be its last nonzero generic power of \(\mathcal I_C\). Purity makes \(\mathcal I_C^{l+1}\mathcal O_X=0\) everywhere, and \(l\le\ell-1\) by the strictly decreasing nonzero powers in the generic local algebra.

Multiplication sends the last layer \(\mathcal I_C^l\mathcal O_X\) into \(\operatorname{Hom}_Z(\mathcal O_C,\mathcal O_Z)(d)\). Finite duality for \(C\subset Z\) and CI adjunction \(\omega_Z=\mathcal O_Z(a+b-4)\) identify this target with \(\omega_C(d+4-a-b)=\mathcal O_{\mathbf P^1}(14-4(a+b-d))\), where the first twist is ambient. There is therefore a nonzero composite
\[
 \operatorname{Sym}^l(\mathcal I_C/\mathcal I_C^2)\longrightarrow
 \mathcal I_C^l\mathcal O_X\lhook\joinrel\longrightarrow
 \mathcal O_{\mathbf P^1}(14-4(a+b-d)).
\]
The source splits as \(\mathcal O(-7l)^{l+1}\). Comparing degrees gives
\[
 7l\ge4(a+b-d)-14,\qquad
 \ell\ge\left\lceil\frac{4(a+b-d)-7}{7}\right\rceil.                \tag{2}
\]
This applies the socle of the **original CI** to the image of a specific multiplier. The colon curve only needs purity. For \(P=1\) the Loewy bound is the existing whole-curve bound. [Conormal splitting](quartic_conormal_characteristic_jump.md), [actual socle and conormal filtration](full_conormal_socle_budget.md).

**Lemma (intrinsic multiplicative filtration).** For \(j\ge0\) define
\[
 \mathcal B_{\ge j}=\operatorname{im}\!\left(
 H^0(\mathbf P^1,\mathcal B(-j))\otimes\mathcal O(j)\longrightarrow\mathcal B\right).
\]
Then \(\mathcal B_{\ge i}\mathcal B_{\ge j}\subseteq\mathcal B_{\ge i+j}\). In particular \(\mathcal B_{\ge1}\) is an ideal. If an actual equation through \(Z\) restricts on the torus to \(\sum_w r^w h_w(U,V)\), every coefficient maps to a global section of \(\mathcal B_{\ge1}\).

*Proof of the lemma.* On a summand \(\mathcal O(\beta)\), evaluation has image the whole summand for \(\beta\ge j\) and zero otherwise. Hence the evaluation image is a subbundle intrinsic to \(\mathcal B\), and any splitting can be used to compute its rank. Multiplying summands of degrees at least \(i,j\) gives zero projection to every summand of degree below \(i+j\), by vanishing of the corresponding Hom groups. Taking \(i=0\) gives the ideal assertion since \(\mathcal B\) is globally generated. The quotient \(\mathcal B/\mathcal B_{\ge1}\) is trivial. In the fixed transverse frame the images of the \(h_w\) from the constant source \(A\) in this quotient are constant vectors. The equation vanishes on the torus, so linear independence of the distinct Laurent powers of \(r\) forces each projected vector to vanish. This proves the lemma.

**Powers of an actual weight component.** Let \(H\) be any nonzero weight component of \(F\) for weights \((0,1,3,4)\). For \(1\le j\le q\), \(H^j\notin J\). Indeed, in degree \(ja<b\) membership forces \(F\mid H^j\). Weight widths add in the polynomial domain, so \(F\) would itself be an eigenform. At \(ja=b\) write a purported membership as \(H^j=QF+cG\), \(c\in k\). For \(c=0\) the same divisibility argument applies. For \(c\ne0\), \((F,H^j)\) generates \(J\) and has an eigenform generator. Both contradict the characteristic-zero [one-eigenform theorem](eigenform_trace_obstruction.md). This includes \(a=b\) and works for reducible generators. The homogeneous CI ideal is saturated, so the nonmembers give nonzero sections on \(Z\).

For the coefficient \(h\) of the weight component \(H\) of \(F\), it follows that \(h^j\mathcal B_\eta\subseteq(\mathcal B_{\ge j})_\eta\). Its dimension equals the image length for \(P=H^j\) since \(r\) is a generic unit. Applying (2) with \(d=ja\) proves (1). In fact \(e\ge\sum_{j\ge1}\dim(h^j\mathcal B_\eta)\), so the actual ranks remain usable beyond the powers guaranteed to survive by the degrees. Equivalently a nilpotent Jordan block of size \(s\) contributes \(\binom{s}{2}\) to this last sum.

**General fibers and the derivative.** Put \(F_\lambda(x)=F(x_0,\lambda x_1,\lambda^3 x_2,\lambda^4 x_3)\). For general \(\lambda\in k^*\), \(F_\lambda\notin J_a\). Otherwise the entire orbit would lie in that closed linear subspace and separating its weights would put \(H\) in \(J_a\), already excluded. In the fixed frame the relation \(F(\lambda r,U,V)\) belongs to \(K_{\lambda r}\), viewing \(F\) in chart coordinates. Its image in \(B_r\) generates an ideal of dimension at least \(L_1\) at generic \(r\) by (2). The whole image of \(K_{\lambda r}\) there is an ideal. The rank condition is open on the pair of fibers, giving the asserted general secant bound.

**The fixed involution.** Let
\(\tau(x_0,x_1,x_2,x_3)=(x_0,-x_1,-x_2,x_3)\). The
[one-sign-eigen-equation theorem](../arguments/torus/sign_symmetry_and_actual_sources.md#1-one-sign-eigen-equation-is-sufficient)
excludes a \(\tau\)-eigenvector in \(J_a\): such a vector is a
minimal-degree generator and can be mated with the other generator of
the same CI. Consequently \(\tau F\notin J_a\) for every nonzero
\(F\in J_a\). If \(a<b\), membership would make the line \(kF=J_a\)
invariant. If \(a=b\), the invariant space spanned by \(F,\tau F\)
would contain a sign eigenvector in the generating pencil. On the torus
\(\tau F\) restricts to \(F(-r,U,V)\), a relation in \(K_{-r}\).
Apply (2) to this nonzero degree-\(a\) multiplier on the original CI.
Its image ideal in \(B_r\) has generic dimension at least \(L_1\),
and is contained in the image of \(K_{-r}\). This proves (1a).

For the derivative, let \(D\) be the diagonal weight derivation, acting as \(r\partial_r\) at fixed \(U,V\). There is a minimal-degree generator \(F\) with \(DF\notin J_a\). Otherwise \(D\) preserves \(J_a\), which is spanned by the degree-\(a\) generators. In characteristic zero its eigenvalues distinguish the integer weights, so this space would contain an eigenform. For \(a<b\) it would generate \(kF\), and for \(a=b\) it would extend to a basis of the generating pencil. Both violate the one-eigenform theorem. On the torus the tangent map takes a local relation to its coefficient derivative modulo the kernel, up to the choice of sign. On every multiple \(pF\) it gives \(pDF\) in the quotient. Its generic image thus has dimension at least \(L_1\) by (2). For equal degrees the choice of pencil member matters in this derivative argument.

## Consequence for opposite full limits

Put \(d_{0\infty}=m-\dim_k A/(K_0+K_\infty)\) in the same global frame. The constant quotient \(\mathcal B/\mathcal B_{\ge1}\) factors through both fibers, so \(d_{0\infty}\le\operatorname{rk}\mathcal B_{\ge1}\). Write \(D_i(B_i)\) for the matched constant-image index and \(t_i\) for the embedded length at \(p_i\) of the full intrinsic limit \(L_i\), with the opposite chart at infinity as in [R-0070](intrinsic_limits_endpoint_fibers.md). Its identities \(t_i=D_i(B_i)-\delta_i\), together with the [CI budget](../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification), give
\[
 D_0(B_0)+D_\infty(B_\infty)-t_0-t_\infty-m(2a+2b-7)
 =e\ \ge\ \max\{d_{0\infty},L_1\}+\sum_{j=2}^q L_j.              \tag{3}
\]
Formula (3) uses the actual common quotient at the two special fibers. The secant rank can drop at this special pair. Equation (3) is a necessary condition for two proposed limits to arise from one defining pair. An endpoint exclusion requires showing that the proposed data violate it or another necessary condition.

## Limitations

An actual proper containing pair whose generic transverse quotient moves in fewer than \(L_1\) first-order directions must have a residual projective curve. A proposed punctual family with too few summands at any level in (1) cannot be the entire modification of a defining pair, regardless of its total degree of movement. The [control with the CI polynomial](../arguments/torus/tropical_thickenings_and_endpoint_duality.md#one-moving-summand-with-the-complete-intersection-polynomial) exhibits this distinction in unbounded degree.

The known upper bound \(e\le m(4m-2a-2b+3)\) is compatible with (1) throughout \(b\ge a\ge5\). Indeed its right side is at least \(ab^2/4\), while \(\sum L_j\le4b^2/(7a)\). Realizing the surviving splittings by two homogeneous equations, or proving a conflicting restriction on all of them, remains open.

## Review

Independent reconstruction checked (2) both by the socle injection and by Serre duality on \(Z\): multiplication gives a nonzero map \(\mathcal O_X(a+b-d-4)\to\omega_Z\), while the conormal layers give \(H^1(\mathcal O_X(a+b-d-4))=0\) if \(7l<4(a+b-d)-14\). Independent checks also covered generator replacement at \(ja=b\), constancy of the quotient used to separate weights, multiplication of the splitting filtration, and the generic secant and differential ranks. The elementary upper bound on Grassmannian secant ranks is the kernel and span estimate. The lower bounds here use the homogeneous equations and their degrees. [Serre duality on a proper Cohen–Macaulay scheme](https://stacks.math.columbia.edu/tag/0FVZ), [Buch, §3, Lemma 1](https://arxiv.org/pdf/math/0106268#page=3), [Hellus–Hübl, Theorem 1.2 and Remark 1.4](https://arxiv.org/pdf/1312.7661).

The fixed-involution extension was independently reconstructed during the
November 23, 2026 geometry synthesis, using the sign-eigen-carrier exclusion
and the same actual-CI multiplier bound (2). It needs no classification of
the endpoint algebras and does not identify a special endpoint secant rank
with its generic value.
