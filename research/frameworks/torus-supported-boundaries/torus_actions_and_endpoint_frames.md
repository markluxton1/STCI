# Torus actions, endpoint frames, and transport

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

## I. Torus geometry and normal coordinates

### Intrinsic and transverse actions

The intrinsic torus \(T_C\) acts by \([s:t]\mapsto[s:\lambda t]\), hence
has projective weights \((0,1,3,4)\). Its fixed points on \(C\) are
\(p_0=[1:0:0:0]\) and \(p_\infty=[0:0:0:1]\). Reversal
\([x_0:x_1:x_2:x_3]\mapsto[x_3:x_2:x_1:x_0]\) exchanges them and
inverts \(T_C\). Scaling \(x_2\) and scaling \(x_1\) separately give
the two distinguished transverse tori. They move \(C\) on the opposite
quartic carriers \(x_1^4=x_0^3x_3\) and \(x_2^4=x_0x_3^3\),
respectively, and reversal exchanges the two actions. In characteristic
zero the full projective stabilizer of \(C\) is \(T_C\) extended by
this reversal. [Opposite carriers and the stabilizer](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#2-the-torus-action-and-opposite-carriers).

On the dense coordinate torus \(\Omega\subset\mathbf P^3\), use
\[
 [x]=[1:r:ur^3:vr^4],\qquad
 r=x_1/x_0,\quad u=(x_2/x_0)/r^3,\quad v=(x_3/x_0)/r^4.
\]
Here \(T_C\) scales \(r\) and fixes \(u,v\), and \(U=u-1,V=v-1\)
generate the ideal of \(C\cap\Omega\). Scaling \(x_2\) by \(\lambda\)
scales \(u\) by \(\lambda\). Scaling \(x_1\) by \(\lambda\) takes
\((r,u,v)\) to \((\lambda r,\lambda^{-3}u,\lambda^{-4}v)\).
Their infinitesimal normal directions therefore form a basis along
\(C\cap\Omega\), with matrix
\(\begin{pmatrix}1&-3\\0&-4\end{pmatrix}\) in the \(U,V\) coordinates.
The chart torus with independent coordinates \(u,v\) uses the scalings
of \(x_2,x_3\) instead. [Dense orbit coordinates and finite images](../../arguments/torus_embedded_quotients.md#finite-image-and-purity).

### Endpoint transitions and determinant

On \(x_0\ne0\), regular normal parameters are \(a_0=x_2/x_0-r^3=r^3U\), \(b_0=x_3/x_0-r^4=r^4V\). On \(x_3\ne0\), set \(z=x_2/x_3\), \(a_\infty=x_1/x_3-z^3\), \(b_\infty=x_0/x_3-z^4\). The conormal transition is
\[
\binom{a_\infty}{b_\infty}=
\begin{pmatrix}-3r^{-6}&2r^{-7}\\-4r^{-7}&3r^{-8}\end{pmatrix}
\binom{a_0}{b_0},\qquad\det=-r^{-14}.
\]
The quadric-conormal extension class is \(-2r^{-1}\in H^1(\mathcal O(-2))\); in characteristic zero this yields \(N_C=\mathcal O(7)^2\). Its characteristic-two jump is proved in the [conormal transition argument](../../arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0).

For the two infinitesimal transverse scalings (of \(x_2,x_1\)), the normal-component map \(\Phi:\mathcal O_C^2\to N_C\) has endpoint matrices
\[
\Phi_0=\operatorname{diag}(r^3,r^4)
\begin{pmatrix}1&-3\\0&-4\end{pmatrix},\qquad
\Phi_\infty=\operatorname{diag}(z^3,z^4)
\begin{pmatrix}-3&1\\-4&0\end{pmatrix}.
\]
Thus in characteristic zero its determinants are \(-4r^7\), \(4z^7\); the invariant-factor orders are \((3,4)\) at both endpoints, and
\(\operatorname{div}(\det\Phi)=7p_0+7p_\infty\). This is the ambient normal-map degeneracy, not an intrinsic failure of the generic formal coordinates. The [exact chart-torus normal map](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map) gives the independent coordinate model. The dense-torus variables \(U,V\) divide the regular endpoint parameters by powers of \(r\) or \(z\), so endpoint formal equations must use these regular frames and their transitions.

### Transport along the two moving directions

For the torus action \((r,u,v)\mapsto(\lambda r,\mu u,\nu v)\), center the normal coordinates on the **moving** curve \(gC\):
\[
U_g=u/\mu-1,\qquad V_g=v/\nu-1.
\]
The full transported equation is \(\sum_w(\lambda^{-1}r)^w f_w(1+U_g,1+V_g)\). Thus transport preserves the normal filtration, Rees algebra, graded algebra, and finite transverse scheme. Expansion about the old fixed curve instead can introduce constant terms and falsely lose containment. At the endpoints the regular normal frames acquire the unit multipliers \(\mu,\nu\) and the corresponding transformed \(\alpha,\beta\) centers, preserving invariant-factor orders \((3,4)\) and determinant divisor \(7p_0+7p_\infty\). For pure supported schemes, equivariance preserves the finite-modification invariants \(m,h,\delta_0,\delta_\infty\) along the parameter torus. A separate auxiliary linear action on a fixed punctual plane does **not** automatically lift through endpoint contractions.

For a one-parameter subgroup with nonzero transverse character, the marked limit curve misses the dense coordinate torus. For a sole-supported moving scheme, parameter-saturated containments \(\mathcal I_{\mathcal C}^N\subset\mathcal I_{\mathcal Z}\subset\mathcal I_{\mathcal C}\) preserve support on the limiting marked curve; specialization of cycles gives \(m\) times its limit cycle, while the Hilbert polynomial remains fixed. The original curve's dense-torus normal length becomes zero. Neither the full limit ideal nor minimal generator degrees follow without the full weight calculation. [Cycle specialization](https://stacks.math.columbia.edu/tag/0H4H) · [full-limit proof](../../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits).

The two transverse directions, together with intrinsic reparametrization, form a three-dimensional family of maps \(\mathbf P^1\to\mathbf P^3\) fixing the two endpoints. Two-point bend-and-break therefore produces a connected reducible rational degree-four cycle, and stable-map properness compactifies the family. This concerns **reduced maps**, not the finite image cokernel or equations of a thickening. [Two-point bend-and-break](https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/M2.pdf#page=69) · [stable maps](https://arxiv.org/pdf/alg-geom/9608011) · [explicit transverse example](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two).
