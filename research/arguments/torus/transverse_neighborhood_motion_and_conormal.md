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

## 6. Endpoint geometry: a common logarithmic space and two ordinary lattices

The [existing endpoint normal-map and lattice calculations](tropical_thickenings_and_endpoint_duality.md) establish the transverse weights 3 and 4 on the reduced normal bundle and the corresponding function lattices. The comparison here uses those same monomial coordinates on the entire smooth ambient product \(Y=\mathbf P^1\times T\), not just the reduced curve. Standard inputs are the logarithmic cotangent trivialization of a smooth toric variety by its character lattice (e.g. the toric differential discussion in Cortiñas--Haesemeyer--Walker--Weibel, *The K-theory of toric varieties*, §3), and the right-exact transitivity and quotient sequences of Kähler differentials ([Stacks 10.131](https://stacks.math.columbia.edu/tag/00RM), [37.63](https://stacks.math.columbia.edu/tag/06BB)). These give the comparisons below; they are not new general deformation theorems.

Near zero the toric contraction \(\rho\) is \((t,u,v)\mapsto[1:t:t^3u:t^4v]\). Its cotangent map on the ambient affine chart has image
\[
 \operatorname{im}(\rho^*\Omega_{\mathbf P^3}\to\Omega_Y)
 = O_Y\,dt\oplus t^3 O_Y\,du\oplus t^4 O_Y\,dv .
\]
Indeed the coordinate differentials are \(dt,3t^2u\,dt+t^3du,4t^3v\,dt+t^4dv\); eliminate the first column terms. The ambient cokernel is the sum of the two torsion modules with exponents 3 and 4, and the determinant has order seven. Restricting the matrix to the separated finite flat family \(W\) preserves injectivity because \(t\) is regular there. This is a statement about the pulled-back **ambient** cotangent bundle, not injectivity of the induced Kähler map of the possibly nonreduced schemes.

The opposite adapted coordinates are
\[
 t^-=y/w=q/t,\quad u^-=v^2/u^3,\quad v^-=v^3/u^4.
\]
They give the reversed projective chart \([ (t^-)^4 v^-:(t^-)^3 u^-:t^-:1]\), with the same two cotangent weights. Since \(q=u/v,\eta=u^2/v\) form a character basis, the coordinate transition is particularly meaningful:
\[
 (t,q,\eta)\mapsto(q/t,q,\eta^{-1}).
\]
In logarithmic coordinates \(\ell=d\log t,\alpha=d\log q,\beta=d\log\eta\), it is
\[
 \ell^-=-\ell+\alpha,\quad\alpha^-=\alpha,\quad\beta^-=-\beta.
\]
A differential written \(h\ell+c\alpha+d\beta\) is therefore
\[
 -h\ell^-+(c+h)\alpha^- -d\beta^- .
\]
The longitudinal evaluation reverses sign, whereas the relative transverse component changes by a shear through the distinguished q-direction. This is a change between the two **endpoint-adapted product splittings**, not a claim that an intrinsic transverse cotangent space depends on its chart. A stationary equation (zero longitudinal evaluation) has no such shear. The original fixed transverse characters are unchanged up to inversion; what changes is the parameter used to describe a transverse slice. On moving thick schemes one must not identify the two relative fiber projections as the same map.

The toric logarithmic cotangent bundles are trivial with fiber \(M\otimes_{\mathbf Z}k\), where \(M\) is the common dense-torus character lattice. The pullback is an isomorphism for this toric contraction (check on monomial \(d\log\) bases, related by a unimodular matrix). Ordinary projective cotangent forms define sublattices in this common logarithmic space. Near zero, using \(u=\eta/q,v=\eta/q^2\), the lattice is generated, up to units, by
\[
 t\ell,\quad t^3(\beta-\alpha),\quad t^4(\beta-2\alpha).
\]
Near infinity it is generated by the same expressions with all symbols replaced by their minus versions. These are canonical images of ordinary ambient cotangent bundles; the listed generators merely record them in adapted torus coordinates. This identifies the differential meaning of both endpoint weights and gives a common ambient space for comparing conormal geometry across endpoints.

If \(W\to Z\) is the actual finite modification, the pullback of the rank-two conormal bundle \(E_Z=I_Z/I_Z^2\) maps to \(I_W/I_W^2\) on the separated model. Differentiation commutes with the two maps to ambient cotangent bundles. It follows that the differential of a pulled-back actual equation factors through the indicated ordinary lattice. This pulled-back bundle is always locally free, but \(I_W/I_W^2\) need not be: the separated closure uses saturation and need not be a regular immersion at the endpoints. Thus do not identify the conormal map of the separated scheme with that of the pulled-back projective presentation.

For example the stationary equation supplied by the spectral cycle satisfies, on the first affine chart,
\[
 \rho^*H(xy,zw)=t^{4m}H(u,v)=t^{4m}v^m h(q),
 \qquad h(Q)=H(Q,1).
\]
Its class in \(I_W/I_W^2\) is the stationary transverse class \([h(q)]\) multiplied by \(t^{4m}v^m\). Its differential on \(W\) is \(t^{4m}v^m h'(q)dq\), since \(h(q)=0\) on \(W\). Likewise \(zw\,d(xy)-xy\,d(zw)\) pulls back to \(t^8uv\,d\log q\). The homogeneous weights simply account for the extension of the transverse relation through the contraction. The analogous statement in the reversed chart uses \(q^-=q\), but the projective trivialization has changed. These formulas hold without assuming reducedness.

## 7. The differential defect of an endpoint

Let \(R=k[[t]]\) and \(A\subset B\) be the endpoint function lattices (at infinity use \(t^-\) and the adapted transverse coordinates). Write \(B=R[u^{\pm1},v^{\pm1}]/J\) and \(A=R[t^3u,t^4v]\subset B\). For a finite flat separated family the completed algebra is finite over \(R\). At infinity the change from \(\tau=1/t\) to \(t^-=q\tau\) preserves the parameter ideals in \(B\); completeness and finiteness modulo that parameter give finiteness over \(k[[t^-]]\), and regularity gives flatness. The two local descriptions need not give the same relative family.

By the standard quotient and transitivity sequences,
\[
 \Omega_{B/A}
 =\frac{B\,du\oplus B\,dv}
 { \langle d_{/R}J,\ t^3du,\ t^4dv\rangle }.
\]
This is the module representing infinitesimal variations upstairs invisible to the downstairs functions: a derivation vanishing on \(A\) is exactly a homomorphism from this module. It is supported at the endpoint, because the lattices agree away from it. It is distinct from the function defect \(B/A\), and from the ambient cokernel of the cotangent map: the latter must be quotiented by the actual relative equations to get this module.

For a local illustration in characteristic zero take \(B=R[\epsilon]/(\epsilon^n)\), \(u=u_0+\epsilon,v=v_0\), with nonzero \(u_0,v_0\). The endpoint algebra is \(A=R[t^3\epsilon]\); hence
\[
 \ell_R(B/A)=3n(n-1)/2,\quad
 \Omega_{B/A}\simeq (R/(t^3))[\epsilon]/(\epsilon^{n-1})\,d\epsilon,
 \quad\ell_R\Omega_{B/A}=3(n-1).
\]
For \(n=1\) interpret the differential module as zero. The full function defect counts all weighted powers; the differential defect also records relations among their variations. They already differ at \(n=3\), where the lengths are 9 and 6. For a varying double direction \(u=u_0+\lambda(t)\epsilon,v=v_0+\epsilon,\epsilon^2=0\), the endpoint algebra is \(R\oplus t^d R\epsilon\) with \(d=\min(3+\operatorname{ord}_t\lambda,4)\) (order infinity for zero). The contraction distinguishes whether the limiting direction has a nonzero weight-three component; it need not distinguish all higher-order motion. Both examples are local controls, not global degree-labelled constructions.

The geometric picture is now: the cycle fixes an envelope, the moving quotient selects neighborhoods inside it, its conormal map describes shape and motion, and the two weighted ordinary cotangent lattices express how that information becomes accessible in projective space. The stationary q-form and the change of splitting through q are particularly natural comparisons. The remaining geometric question is how the full pulled-back projective equation bundle, the actual conormal module of the separated family, and the two function/conductor lattices determine or constrain one another; no sufficiency or global realization theorem is asserted. The present calculations are provisional pending independent review.


The [plane-pencil and equation-bundle comparison](plane_pencil_equation_bundles.md) reconnects this local picture with the realization objective: the moving degree-m neighborhood is part of a full degree-ab plane CI, and the degree-labelled minimal generator bundles of a fixed-type plane-CI family determine whether its equations come from one global homogeneous pair. This is a complementary projective family, not an identification with the separated modification or an existence assertion for its completion.


## 8. Recovering the ordinary reduced conormal from product-model intersections

Use the [three independent product presentations](transverse_coefficient_realization_synthesis.md#three-independent-complementary-pair-product-models) and the logarithmic normal space \(\mathcal V=k\alpha\oplus k\beta\), \(\alpha=d\log U,\beta=d\log V\), with \(U,V\) ambient characters and \(u,v\) fixed on the individual reduced graph. This is the kernel of restriction to the logarithmic differential on the normalized orbit. Standard toric input: Cox--Little--Schenck, *Toric Varieties*, §8.1, especially the discussion following Theorem 8.1.1 (https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf). We use it to recover ordinary conormal data rather than derive a new normal bundle classification.

Differentiating the two graph equations in the three models gives respectively
\[
 I:(ur^3\alpha,(v/u)r(\beta-\alpha)),\quad
 II:(ur^3\alpha,vr^3\beta),\quad
 III:(ur^2\alpha,vr^4\beta).
\]
These are bases of the generic conormal space; their spans over \(R=k[[r]]\) are the ordinary conormal lattices of the corresponding smooth graph at zero. Suppressing unit factors gives
\[
 \Lambda_I=Rr^3\alpha+Rr(\beta-\alpha),\quad
 \Lambda_{II}=r^3(\mathcal V\otimes R),\quad
 \Lambda_{III}=Rr^2\alpha+Rr^4\beta.
\]
The ordinary projective conormal of the reduced curve, using \(y-ux^3,w-vx^4\) in \(z=1\), is exactly
\[
 \Lambda_{\mathbf P^3,0}=\Lambda_{II}\cap\Lambda_{III}
 =Rr^3\alpha+Rr^4\beta .
\]
It also lies in \(\Lambda_I\). This is an actual recovery of a local ordinary conormal from compatibility of the product graphs, not a general assertion of intersection-descent for ideals. At infinity one must reverse the product charts as well as the parameter. In the adapted coordinates of Section 6 the new transverse basis is
\[
 \alpha^-=2\beta-3\alpha,\qquad \beta^-=3\beta-4\alpha .
\]
With \(R^-=k[[r^-]]\), \(r^-=q/r\), the same intersection of the **reversed** II and III lattices yields
\[
 \Lambda_{\mathbf P^3,\infty}
 =R^-(r^-)^3\alpha^-+R^-(r^-)^4\beta^-.
\]
The unreversed III lattice at infinity generally does not give this intersection. The inverse-chart transition and not just the longitudinal inversion matters.

The common model-II lattice is globally \(\mathcal O_{\mathbf P^1}(-3p_0-3p_\infty)\otimes\mathcal V\) (the reversed II gives the same lattice at infinity, because the change of transverse basis is unimodular). The projective conormal is obtained from it by requiring the leading value at zero to lie in \(k\alpha\), and at infinity to lie in \(k\alpha^-\); in other words, one elementary modification at each endpoint. In characteristic different from two these two lines in \(\mathcal V\) are independent. Using them as constant basis vectors splits the conormal as
\[
 \mathcal O(-3p_0-4p_\infty)\alpha
 \ \oplus\ \mathcal O(-4p_0-3p_\infty)\alpha^- .
\]
This recovers the classical \(N_{C/\mathbf P^3}\simeq O(7)^2\) result (Eisenbud--Van de Ven, *On the normal bundles of smooth rational space curves*, https://eisenbud.github.io/papers/pdfs/1981-001.pdf). In characteristic two the lines coincide and the splitting instead is \(O(-6)\oplus O(-8)\) for the conormal. These are classical splitting types, not new exclusions; the product-intersection interpretation is the point.

For actual homogeneous \(F\), set \(f=F(1,r,r^3U,r^4V)\). The full logarithmic differential before restriction is
\[
 df=(rF_x+3r^3UF_y+4r^4VF_w)\ell+r^3UF_y\alpha+r^4VF_w\beta
\]
where partials are evaluated at the substituted homogeneous coordinates. On a reduced orbit contained in \(F=0\), the longitudinal coefficient vanishes and the other two belong to \(\Lambda_{\mathbf P^3,0}\). On a moving thick scheme the longitudinal coefficient can survive, and we must retain it. On changing affine projective frame or multiplying by an exceptional factor, the identity \(d(hf)=h\,df+f\,dh\) gives the differential transition on the common zero scheme (where the second term vanishes). For a pair the wedge acquires the product of the exceptional factors. This does not identify the strict-transform ideal with the pair after individual saturation, nor recover a rank-two conormal for the separated nonreduced closure. A pair of regular forms in the reduced intersection lattice alone does not imply a global polynomial lift or actual CI realization. The precise extension question is to recover the *full equations and their differential maps*, including the longitudinal component and thick structure, by the analogous boundary compatibility, not to demand a new splitting result for the reduced curve. Provisional comparison pending independent review.
