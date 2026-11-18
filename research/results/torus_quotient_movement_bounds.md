---
id: STCI-R-0072
type: result
title: Lower bounds on transverse movement from the actual defining equations
scope: "#scope"
statement: "#statement"
proofs:
  - name: multiplier rank and the splitting of the moving quotient
    at: "#proof"
    using: [STCI-R-0020, STCI-R-0042]
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
For general \(x,y\in\mathbf G_m\), the common quotient \(A/(K_x+K_y)\) has length at most \(m-L_1\). At a general \(x\), a nonzero tangent vector to the base induces a linear map \(K_x\to B_x\) of rank at least \(L_1\). These ranks count transverse directions. The tangent vector belongs to a one-dimensional base.

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

**Powers of an actual weight component.** Let \(H\) be any nonzero weight component of \(F\) for weights \((0,1,3,4)\). For \(1\le j\le q\), \(H^j\notin J\). Indeed, in degree \(ja<b\) membership forces \(F\mid H^j\). Weight widths add in the polynomial domain, so \(F\) would itself be an eigenform. At \(ja=b\) write a purported membership as \(H^j=QF+cG\), \(c\in k\). For \(c=0\) the same divisibility argument applies. For \(c\ne0\), \((F,H^j)\) generates \(J\) and has an eigenform generator. Both contradict the characteristic-zero [one-eigenform theorem](eigenform_trace_obstruction.md). This includes \(a=b\) and works for reducible generators. The homogeneous CI ideal is saturated, so the nonmembers give nonzero sections on \(Z\).

Let \(\mathcal B_{\ge j}\) be the subbundle comprising the summands of degree at least \(j\). It is intrinsic, being the image of the evaluation of \(\mathcal B(-j)\) twisted back by \(j\). Bundle multiplication sends \(\mathcal B_{\ge i}\mathcal B_{\ge j}\) into \(\mathcal B_{\ge i+j}\), since all maps from a higher-degree line bundle to a lower-degree one vanish. In particular the positive subbundle is an ideal. Write each component on the chart as \(H_w=r^w h_w(U,V)\). The \(h_w\) give global sections through the constant source \(A\). The quotient \(\mathcal B/\mathcal B_{\ge1}\) is trivial, and every map from \(A\otimes\mathcal O\) to it is constant. Projecting the actual relation \(\sum_w r^w h_w=0\) to this quotient and separating Laurent powers gives \(h_w\in H^0(\mathcal B_{\ge1})\) for every \(w\).

For the coefficient \(h\) of \(H\), it follows that \(h^j\mathcal B_\eta\subseteq(\mathcal B_{\ge j})_\eta\). Its dimension equals the image length for \(P=H^j\) since \(r\) is a generic unit. Applying (2) with \(d=ja\) proves (1). In fact \(e\ge\sum_{j\ge1}\dim(h^j\mathcal B_\eta)\), so the actual ranks remain usable beyond the powers guaranteed to survive by the degrees. Equivalently a nilpotent Jordan block of size \(s\) contributes \(\binom{s}{2}\) to this last sum.

**General fibers and the derivative.** Put \(F_\lambda(x)=F(x_0,\lambda x_1,\lambda^3 x_2,\lambda^4 x_3)\). For general \(\lambda\in k^*\), \(F_\lambda\notin J_a\). Otherwise the entire orbit would lie in that closed linear subspace and separating its weights would put \(H\) in \(J_a\), already excluded. In the fixed frame the relation \(F(\lambda r,U,V)\) belongs to \(K_{\lambda r}\), viewing \(F\) in chart coordinates. Its image in \(B_r\) generates an ideal of dimension at least \(L_1\) at generic \(r\) by (2). The whole image of \(K_{\lambda r}\) there is an ideal. The rank condition is open on the pair of fibers, giving the asserted general secant bound.

For the derivative, let \(D\) be the diagonal weight derivation, acting as \(r\partial_r\) at fixed \(U,V\). There is a minimal-degree generator \(F\) with \(DF\notin J_a\). Otherwise \(D\) preserves \(J_a\), which is spanned by the degree-\(a\) generators. In characteristic zero its eigenvalues distinguish the integer weights, so this space would contain an eigenform. For \(a<b\) it would generate \(kF\), and for \(a=b\) it would extend to a basis of the generating pencil. Both violate the one-eigenform theorem. On the torus the tangent map takes a local relation to its coefficient derivative modulo the kernel, up to the choice of sign. On every multiple \(pF\) it gives \(pDF\) in the quotient. Its generic image thus has dimension at least \(L_1\) by (2). For equal degrees the choice of pencil member matters in this derivative argument.

## Consequence for opposite full limits

Put \(d_{0\infty}=m-\dim_k A/(K_0+K_\infty)\) in the same global frame. The constant quotient \(\mathcal B/\mathcal B_{\ge1}\) factors through both fibers, so \(d_{0\infty}\le\operatorname{rk}\mathcal B_{\ge1}\). Write \(D_i(B_i)\) for the matched constant-image index and \(t_i\) for the embedded length at \(p_i\) of the full intrinsic limit \(L_i\), with the opposite chart at infinity as in [R-0070](intrinsic_limits_endpoint_fibers.md). Its identities \(t_i=D_i(B_i)-\delta_i\), together with the [CI budget](../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification), give
\[
 D_0(B_0)+D_\infty(B_\infty)-t_0-t_\infty-m(2a+2b-7)
 =e\ \ge\ \max\{d_{0\infty},L_1\}+\sum_{j=2}^q L_j.              \tag{3}
\]
Formula (3) uses the actual common quotient at the two special fibers. The generic rank argument gives no lower bound on their distance because rank can drop under specialization.

## Limitations

An actual proper containing pair whose generic transverse quotient moves in fewer than \(L_1\) first-order directions must have a residual projective curve. A proposed punctual family with too few summands at any level in (1) cannot be the entire modification of a defining pair, regardless of its total degree of movement. The [control with the CI polynomial](../arguments/torus/tropical_thickenings_and_endpoint_duality.md#one-moving-summand-with-the-complete-intersection-polynomial) exhibits this distinction in unbounded degree.

The known upper bound \(e\le m(4m-2a-2b+3)\) is compatible with (1) throughout \(b\ge a\ge5\). Indeed its right side is at least \(ab^2/4\), while \(\sum L_j\le4b^2/(7a)\). Realizing the surviving splittings by two homogeneous equations, or proving a conflicting restriction on all of them, remains open.

## Review

Independent reconstruction checked (2) both by the socle injection and by Serre duality on \(Z\): multiplication gives a nonzero map \(\mathcal O_X(a+b-d-4)\to\omega_Z\), while the conormal layers give \(H^1(\mathcal O_X(a+b-d-4))=0\) if \(7l<4(a+b-d)-14\). Independent checks also covered generator replacement at \(ja=b\), constancy of the quotient used to separate weights, multiplication of the splitting filtration, and the generic secant and differential ranks. The elementary upper bound on Grassmannian secant ranks is the kernel and span estimate. The lower bounds here use the homogeneous equations and their degrees. [Serre duality on a proper Cohen–Macaulay scheme](https://stacks.math.columbia.edu/tag/0FVZ), [Buch, §3, Lemma 1](https://arxiv.org/pdf/math/0106268#page=3), [Hellus–Hübl, Theorem 1.2 and Remark 1.4](https://arxiv.org/pdf/1312.7661).
