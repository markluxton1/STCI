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

On \(x_0\ne0\) take the regular normal parameters
\[
 a_0=x_2/x_0-r^3=r^3U,\qquad b_0=x_3/x_0-r^4=r^4V.
\]
On \(x_3\ne0\) take \(z=x_2/x_3\),
\(a_\infty=x_1/x_3-z^3\), \(b_\infty=x_0/x_3-z^4\).
On the overlap inside \(\Omega\) the full changes of coordinates are
\[
 z=(u/v)r^{-1},\quad \alpha=v^2/u^3,\quad\beta=v^3/u^4,
 \qquad (a_\infty,b_\infty)=(z^3(\alpha-1),z^4(\beta-1)).
\]
In the conormal sheaf \(E=\mathcal I/\mathcal I^2=N_C^\vee\) this gives
\[
 \binom{a_\infty}{b_\infty}
 =
 \begin{pmatrix}-3r^{-6}&2r^{-7}\\-4r^{-7}&3r^{-8}\end{pmatrix}
 \binom{a_0}{b_0},
 \qquad \det=-r^{-14}.
\]
For the containing quadric \(q=x_0x_3-x_1x_2\), the conormal sequence
has subline \(\mathcal O_{\mathbf P^1}(-8)\) and quotient
\(\mathcal O_{\mathbf P^1}(-6)\). Its class is represented by
\(-2r^{-1}\) in \(H^1(\mathcal O_{\mathbf P^1}(-2))\) in the frames of
the transition proof. For example, the conormal frame
\((b_0-\tfrac32ra_0,a_0)\) on the first chart becomes a frame on the
entire opposite chart after multiplying both entries by \(r^{-7}\).
Thus \(N_C\cong\mathcal O_{\mathbf P^1}(7)^{\oplus2}\). The extension
class is essential to this splitting calculation. [Conormal transition
and characteristic dependence](../../arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0).

For the determinant divisor, let \(\Phi:\mathcal O_C^2\to N_C\) be
the normal components of the global infinitesimal scalings of \(x_2,x_1\)
in that order. Evaluate the two vector fields on the regular normal
parameters above. At zero the column values are \((r^3,0)\) and
\((-3r^3,-4r^4)\). At infinity, scaling \(x_2\) scales \(z\) and acts
on \(\alpha,\beta\) with exponents \(-3,-4\), while scaling \(x_1\)
fixes \(z\) and scales \(\alpha\) alone. The matrices are
\[
 \Phi_0=
 \begin{pmatrix}r^3&0\\0&r^4\end{pmatrix}
 \begin{pmatrix}1&-3\\0&-4\end{pmatrix},
 \qquad
 \Phi_\infty=
 \begin{pmatrix}z^3&0\\0&z^4\end{pmatrix}
 \begin{pmatrix}-3&1\\-4&0\end{pmatrix}.
\]
Their determinants are \(-4r^7\) and \(4z^7\) in the corresponding
normal frames. Each constant matrix is invertible, so the invariant
factors at each endpoint have orders \(3,4\). On the overlap
\((-r^{-14})(-4r^7)=4z^7\), as required by the normal-component
transition. The map is an isomorphism on \(C\cap\Omega\). Consequently
\[
 \operatorname{div}(\det\Phi)=7p_0+7p_\infty
\]
as the zero divisor of a section of \(\det N_C\). Its degree agrees with
\(\deg\det N_C=14\). The compactification using independent \(u,v\)
directions gives the same divisor via its own differential. [Exact
normal map in the chart torus](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map).

The failure of the generic coordinates to extend is visible already in
\(E\otimes k(C)\). At zero they divide \(a_0,b_0\) by \(r^3,r^4\).
At infinity the two regular parameters divide by \(z^3,z^4\) to give
\(\alpha-1,\beta-1\), which are related to \(U,V\) by an invertible
constant matrix to first order. Both \(U,V\) have poles in that regular
conormal frame as well. Thus the generic coordinates give a formal
normal system over the dense orbit, and the endpoint models require the
regular parameters and their full transition. The length-seven frame
cokernel at each endpoint belongs to the ambient normal map \(\Phi\).

### Transport along the two moving directions

Write the action on points as \((r,u,v)\mapsto(\lambda r,\mu u,\nu v)\)
with \(\lambda,\mu,\nu\in k^*\). The image curve \(gC\) has centered
normal coordinates \(U_g=u/\mu-1,\ V_g=v/\nu-1\). If a form is written
on \(x_0=1\) as \(\sum_w r^w f_w(u,v)\), its transported equation
\(F\circ g^{-1}\) has full expansion
\[
\sum_w(\lambda^{-1}r)^w f_w(1+U_g,1+V_g).
\]
Thus \(g\) transports the entire normal filtration, including its Rees
and graded algebras and the finite transverse scheme. In these frames
the two transverse scalings are translations of the marked section in
the quotient torus. Expanding in \(u-1,v-1\) instead introduces constant
terms and can lose containment of the fixed \(C\). At \(p_0\) the regular
normal parameters for \(gC\) are \(\mu r^3 U_g,\nu r^4 V_g\).
At \(p_\infty\), center \(\alpha,\beta\) at \(\nu^2/\mu^3,\nu^3/\mu^4\)
respectively. The corresponding unit multipliers preserve the two
orders \(3,4\) and their determinant divisor. Equivariance of the
finite modification carries its algebra and both image inclusions
along with \(gC\), preserving \(m,h,\delta_0,\delta_\infty\) on the
parameter torus for a pure supported scheme.
The auxiliary linear action \((U,V)\mapsto(\mu U,\nu V)\) on a fixed
punctual plane has its own Hilbert-scheme action. An application to
projective equations must specify how that action lifts through the
two endpoint contractions.

For a one-parameter subgroup with nonzero transverse character, the
limit of the marked curve is disjoint from \(\Omega\). Indeed on
\(\Omega\) one of \(u,v\) equals a nonzero power of the parameter
and is required to stay a unit. Its contracted equation has unit
specialization on this chart. For a sole-supported moving scheme,
contract the ideals of both the scheme and its marked support from the
punctured parameter trait. The power containments
\(\mathcal I_{\mathcal C}^N\subset\mathcal I_{\mathcal Z}
\subset\mathcal I_{\mathcal C}\) persist by parameter saturation. Hence
the transverse special scheme is supported on the reduced support of
the flat limit of the marked curve. Its fundamental cycle is \(m\)
times the marked limiting cycle by specialization of cycles of flat
families. Its generic normal length **along the original \(C\)** is
then zero. The projective Hilbert polynomial stays fixed. The ideal
and the degrees of its generators still require the full weight limit.
[Cycle specialization over a DVR](https://stacks.math.columbia.edu/tag/0H4H).

For the reduced parametrization the two moving directions give a
two-dimensional family of distinct curves through the same endpoints.
Together with the one-dimensional reparametrization \(r\mapsto\lambda r\)
they give a three-dimensional family in
\(\operatorname{Mor}(\mathbf P^1,\mathbf P^3;0\mapsto p_0,\infty\mapsto p_\infty)\).
Indeed the four coefficients in \([s^4:\lambda s^3t:
\mu\lambda^3st^3:\nu\lambda^4t^4]\), modulo their common scalar, recover
the three parameters. This meets the dimension-two hypothesis of the
two-point bend-and-break theorem for a projective target. It gives a
connected nonintegral rational cycle of degree four through the two
points. Stable-map properness compactifies the marked maps with nodal
domains. These results concern maps from reduced curves, and the
degree-four break is explicit in the
[transverse sextic control](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two).
The map and its cycle contain no data of the finite image cokernel or
the graded equations of the thickening.
[Mori's two-point theorem, as stated in Debarre, Proposition 7.3](https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/M2.pdf#page=69) ·
[Fulton–Pandharipande, §§1, 5–6](https://arxiv.org/pdf/alg-geom/9608011).

