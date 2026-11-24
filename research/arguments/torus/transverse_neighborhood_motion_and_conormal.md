# Transverse neighborhoods: shape, motion, and conormal geometry

**Status:** provisional geometric synthesis and elementary illustrations, characteristic zero. The subject is realization geometry, not a new obstruction. The existing [coefficient synthesis](transverse_coefficient_realization_synthesis.md) and [normal graph account](grassmannian_sum_and_conormal_compatibility.md) give the surrounding constructions.

## 1. Two components of the conormal map

Write the dense ambient torus as \(U=B\times T\), with \(B=\mathbf G_m\) the longitudinal parameter \(t=x/z\) and \(T=(\mathbf G_m)^2\) the orbit space. Let \(Z^\circ\subset U\) be the torus restriction of a proper homogeneous CI whose entire cycle is a translated arrangement \(\sigma=\sum_i n_i[p_i]\), \(m=\sum_i n_i\). Its projection \(p:Z^\circ\to B\) is finite flat of rank \(m\). The ideal \(I\) is a regular immersion of codimension two. Forget the projective Euler twist on this open and put \(E=I/I^2\). The product splitting gives
\[
 d=(d_T,d_B):E\longrightarrow \Omega_T|_{Z^\circ}\oplus p^*\Omega_B .
\]
Here \(d_T\) is the relative conormal map: restricting to a fiber gives its conormal differential in \(T\). Flatness over \(B\) ensures the conormal module and regular sequence restrict correctly to the fibers. The map \(d_B\) is the change in the embedded equations along \(B\). Evaluation on the normalized longitudinal vector field \(t\partial_t\) is intrinsic to the action; the product splitting used to describe the transverse component is a choice of longitudinal coordinate. The usual conormal exact sequence is right exact; do not assume its first map injective for thick schemes. See [Stacks 37.63](https://stacks.math.columbia.edu/tag/06BB), [31.22](https://stacks.math.columbia.edu/tag/0638), and [92.14](https://stacks.math.columbia.edu/tag/08SH).

The normal graph in the relative \(\operatorname{Gr}(2,6)\) retains both maps, after the projective Euler inclusion. Its exterior square can discard the motion. The prescribed orbit conormal plane is instead the pullback of \(\Omega_T\) under the orbit quotient, independent of \(I\).

## 2. The derivative of the moving quotient is the same motion

The [canonical fat-point envelope](full_transverse_chow_pullback_envelope.md) is \(T_\sigma=\operatorname{Spec} A_\sigma\), where
\[
 A_\sigma=k[T]/J_\sigma,\qquad J_\sigma=\bigcap_i\mathfrak m_{p_i}^{n_i}.
\]
The ideal \(J=J_\sigma O_U\) lies in \(I\). Write \(\mathcal B=p_*O_{Z^\circ}\), and let \(\mathcal K\) be the kernel of the constant envelope quotient:
\[
 0\to\mathcal K\to A_\sigma\otimes O_B\to\mathcal B\to0.
\]
The kernel is an ideal as well as a vector subbundle. This quotient defines a map \(g:B\to\operatorname{Gr}_m(A_\sigma)\) (rank-\(m\) quotients). The standard tangent formula \(T_{\operatorname{Gr}}=\operatorname{Hom}(\mathcal K,\mathcal B)\) identifies its derivative, using the kernel convention, with the second fundamental form
\[
 \nabla_{\mathcal K}:\mathcal K\longrightarrow
 \mathcal B\otimes\Omega_B,\qquad k\mapsto dk\bmod\mathcal K .
\]
This is \(O_B\)-linear because the extra Leibniz term is a multiple of \(k\), hence zero in \(\mathcal B\). References: Izzet Coskun, [Grassmannians: the first example of a moduli](https://homepages.math.uic.edu/~coskun/MITweek1.pdf), tangent bundle discussion; Jarod Alper, [Deformation theory notes](https://sites.math.washington.edu/~jarod/courses/math581J-fall21/def-theory-notes.pdf), §1.1 (first-order embedded deformations). The sign of the tangent identification depends on using variation of equations versus displacement of subschemes; here we use the displayed derivative of equations consistently.

There is a direct conormal explanation, requiring no moduli theory. In local rings, the conormal module for \(Z^\circ\subset B\times T_\sigma\) is \(I/(I^2+J)\). The composition of closed immersions gives the right-exact sequence
\[
 J/J^2\otimes O_{Z^\circ}\longrightarrow E
 \longrightarrow I/(I^2+J)\to0.
\]
Since \(J\) comes from a fixed scheme in \(T\), \(d_B\) vanishes on its conormal image. It therefore factors through the last module. After pushforward to \(B\), that module is \(\mathcal K/\mathcal K^2\) and the induced map is precisely \(\nabla_{\mathcal K}\) factored through \(\mathcal K/\mathcal K^2\). Indeed differentiating any lift of \(k\in\mathcal K\) in the ambient product and passing to the quotient gives the same class, since differentiation in \(B\) preserves \(J\). The product rule kills \(\mathcal K^2\). Thus the two Grassmannian constructions are connected by differentiation: the quotient Grassmannian describes the embedded family, the conormal graph describes its differential equations.

In characteristic zero \(d_B=0\) identically iff \(g\) is constant: on a dense Grassmannian chart all rational coordinate functions then have zero derivative in \(k(t)\), hence are constant. The kernel is then a fixed embedded ideal and the family is constant. This recovers the invariant-ideal interpretation without a density or smoothing argument. Pointwise zero velocity does not imply a constant family. In positive characteristic purely inseparable maps invalidate the converse.

## 3. Embedded motion versus intrinsic change

For a vector field \(v\) along \(B\), write \(\nu(v)\in E^\vee\) for evaluation of \(d_B\) on \(v\). The relative tangent map dual to \(d_T\) is
\[
 T_T|_{Z^\circ}\longrightarrow E^\vee.
\]
A transverse vector \(w\) can compensate the longitudinal velocity precisely when \(d_T^\vee(w)+\nu(v)=0\), i.e. when \(v+w\) annihilates the ideal modulo \(I\). Equivalently a longitudinal vector lifts to a derivation on the actual scheme if the corresponding class of \(\nu(v)\) in the cokernel vanishes. This cokernel is the relative first cotangent cohomology module \(T^1_{Z^\circ/B}\) (the degree-one cohomology of the dual of the two-term lci cotangent complex). On a fiber the same formula gives its abstract first-order deformation class, up to the convention sign. This does not assert that infinitesimal triviality integrates to a global trivialization.

Two concrete examples, in local transverse coordinates \(r=q-q_0,s=\eta-\eta_0\) with nonzero \(q_0,\eta_0\):

* Double point rotating inside the transverse surface: \(I=(r^2,s-\lambda(t)r)\). The quotient algebra is always \(O_B[r]/(r^2)\), but the tangent line is \([1:\lambda]\). The equations have differentials \(2r\,dr,\ ds-\lambda\,dr-r\,d\lambda\); their wedge is \(2r\,dr\wedge ds\), losing the velocity because \(r^2=0\). Evaluation of the second form on \(v\) gives \(-r v(\lambda)\); the transverse vector \(r v(\lambda)\partial_s\) compensates. The envelope has ideal \((r,s)^2\). Its image in \(E\) is generated by \([r^2]\) and \(r[s-\lambda r]\), as seen by writing \(s=\lambda r+(s-\lambda r)\); hence the quotient conormal is generated by \([s-\lambda r]\) modulo \(r\). Its velocity maps to the socle line spanned by \(r\). The fixed envelope accounts for the infinitesimal length, while the quotient line accounts for the moving direction.

* Length-four family changing abstract shape: \(I=(r^2,s^2-(t-1)r)\) over \(B=\mathbf G_m\). The algebra is free on \(1,r,s,rs\), by reduction by the two monic equations (equivalently first quotient by \(r^2\), then by the monic quadratic in \(s\)). For \(t\ne1\) a fiber is \(k[s]/(s^4)\); at \(t=1\) it is \(k[r,s]/(r^2,s^2)\). It remains a flat relative CI with the same cycle \(4[p]\). Its differentials are \(2r\,dr,\ 2s\,ds-(t-1)dr-r\,dt\); their wedge is \(4rs\,dr\wedge ds\). At \(t=1\), the velocity for \(\partial_t\) has value \(-r\) on the second equation. No transverse vector compensates it because the second relative differential there is \(2s\,ds\), and \(r\notin(s)\) in the fiber algebra. The conormal graph distinguishes this from the rotating double point, even though the exterior square again loses the longitudinal term.

Both examples are torus-local embedded families, not claims of projective degree-labelled realization. In particular all characteristic-zero assertions about the abstract deformation class are first-order statements at the specified fibers.

## 4. Geometric meaning of compatibility with projected forms

A transverse covector \(\omega\) admits a full conormal lift precisely when
\[
 \omega\in d_T(\ker d_B).
\]
Indeed a lift \(e\in E\) must satisfy \(d_T(e)=\omega\) and \(d_B(e)=0\). Relative compatibility alone means \(\omega\in\operatorname{im}d_T\) and does not ensure absolute compatibility. The fixed-envelope conormal classes automatically lie in \(\ker d_B\). In particular the cycle polynomial \(H(q)\) defines such a class, explaining the compatible weighted form \(H'(q)dq\) by factorization through the fixed envelope (or projected cycle divisor). The same argument applies to any relation pulled back from the orbit space. This tells us which equations of the infinitesimal neighborhoods are constant along the family, not just which covectors have zero wedge with the socle-valued minors.

## 5. Return to the projective geometry

The separated model \(\mathbf P^1\times T_\sigma\) gives the finite flat closure of the moving quotient: extend the generic quotient by taking its torsion-free scheme closure in the fixed envelope, equivalently extend the ideal-valued quotient map into the projective quotient Grassmannian. The closure is finite flat over the smooth base curve; ideal preservation holds by closure. The same second fundamental form then has the global target \(\mathcal B\otimes\Omega_{\mathbf P^1}\) on that separated model. The conormal module at the endpoints need not be locally free of rank two; no such extension of the original relative rank-two graph is asserted. The contraction to \(\mathbf P^3\) is the existing endpoint modification (see [embedded quotient framework](../../frameworks/embedded-torus-quotients/index.md) and [endpoint duality](tropical_thickenings_and_endpoint_duality.md) for the sole-supported case). A global homogeneous CI presentation has further information beyond the quotient and its first derivative.

The natural next comparison is how the fixed-envelope conormal classes, the relative fiber equations, and the velocity transform under the two endpoint contractions. This brings the Grassmannian geometry back into contact with our normal bundles and endpoint lattices. The examples show why neither the cycle nor the determinant of the conormal map alone captures this geometry. The formulas here are applications of standard deformation theory; their project-specific interpretation and subsequent global comparison are the research task. No new general realization theorem or first-moment vanishing is asserted.
