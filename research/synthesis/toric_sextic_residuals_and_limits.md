# Weight, normal, and torus-limit geometry of the Macaulay quartic

<a id="invariant-sextic-geometry-orbit-closures-residual-boundaries-and-hilbert-limits"></a>

Let \(k\) be algebraically closed of characteristic zero and fix
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). Write
\(S=k[x_0,x_1,x_2,x_3]\), \(P=I_C\subset S\), and
\(\mathcal I=\mathcal I_C\) for the ideal sheaf. The starting data are an
actual proper pair \(F\in P_a,\ G\in P_b\) of positive degrees, with
\(J=(F,G)\) of height two and \(Y=V_+(J)\). Sole reduced support on \(C\)
is an additional hypothesis wherever stated. The unrestricted
characteristic-zero set-theoretic complete intersection (STCI) question
remains open. The [source map](#source-map-and-scope) identifies the proof
homes for the constructions below.

[I. Torus geometry](#i-torus-geometry-and-normal-coordinates) ·
[II. Equations and filtrations](#ii-equations-and-filtrations) ·
[III. Full torus limits](#iii-extreme-weights-and-full-limits) ·
[IV. Endpoint extension](#iv-generic-algebra-and-endpoint-extension) ·
[V. Global constraints](#v-global-constraints) ·
[VI. Sextic example](#vi-the-filtrations-together-in-the-sextic-example)

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
this reversal. [Opposite carriers and the stabilizer](toric_torsion_and_endpoint_contacts.md#2-the-torus-action-and-opposite-carriers).

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
of \(x_2,x_3\) instead. [Dense orbit coordinates and finite images](../arguments/torus_embedded_quotients.md#finite-image-and-purity).

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
and characteristic dependence](../arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0).

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
normal map in the chart torus](tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map).

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
[transverse sextic control](../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two).
The map and its cycle contain no data of the finite image cokernel or
the graded equations of the thickening.
[Mori's two-point theorem, as stated in Debarre, Proposition 7.3](https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/M2.pdf#page=69) ·
[Fulton–Pandharipande, §§1, 5–6](https://arxiv.org/pdf/alg-geom/9608011).

## II. Equations and filtrations

### Weight components and actual symbols

Use weights on polynomial monomials given by substitution
\(x_i\mapsto\lambda^{w_i}x_i\), with \(w=(0,1,3,4)\). Write
\(F=\sum_\alpha F_\alpha\), \(G=\sum_\beta G_\beta\).
A degree-\(d\), weight-\(\ell\) monomial \(x^e\) restricts on the
\(x_0=1\) torus chart to \(r^\ell u^{e_2}v^{e_3}\) and on \(C\) to
\(s^{4d-\ell}t^\ell\) in homogeneous parameters. This identifies the
weight grading with one coordinate of the parametrization bigrading.
Every weight component of a form through \(C\) lies in \(P\).
[Actual weight-wise equation spaces](../arguments/torus_embedded_quotients.md#actual-equations-and-the-ci-criterion).

Let \(D^jS_d=H^0(\mathbf P^3,\mathcal I^j(d))\) be the space of
actual degree-\(d\) equations of normal order at least \(j\).
These are sheaf powers, read as saturated homogeneous source spaces.
Regular embedding identifies
\(\mathcal I^j/\mathcal I^{j+1}=\operatorname{Sym}^j E\).
Since these sheaves are locally free on the integral curve,
vanishing of the lower classes at \(\eta_C\) implies their global
vanishing. Write \(\mathcal O_C(a)=\mathcal O_{\mathbf P^1}(4a)\) for
the ambient twist. For \(F\) of exact generic normal order \(r_F\)
its first symbol is a nonzero section
\[
 f\in H^0(C,\operatorname{Sym}^{r_F} E\otimes\mathcal O_C(a)),
 \qquad \operatorname{Sym}^{r_F} E\otimes\mathcal O_C(a)
 \cong \mathcal O_{\mathbf P^1}(4a-7r_F)^{\oplus(r_F+1)}.
\]
The same holds for \(g\) of order \(r_G\) and ambient degree \(b\).
The order-\(j\) symbol map embeds the actual homogeneous source
\(D^j S_d/D^{j+1} S_d\) into the sections of the corresponding bundle.
Its image can be proper even for a balanced bundle. In the torus chart,
the symbol of a weight component is the first nonzero Taylor part in
\(U,V\) of its transverse coefficient polynomial, multiplied by the
corresponding power of \(r\). The symbol of the sum comes from the
components of minimum normal order. [Normal symbols and actual source images](../arguments/quartic_specialization_and_symbols.md#4-which-symmetric-algebra-sections-come-from-quartics).

### Excess vanishing and common directions

The full expansion in a chosen formal frame retains every higher
Taylor coefficient. Nonlinear changes between the two endpoint charts
mix those coefficients with the lower terms. An intrinsic order-\(j\)
symbol belongs to \(\operatorname{Sym}^jE\otimes\mathcal O_C(d)\) after
the preceding classes vanish, or after a specified compatible subtraction
of their actual lifts. The degree \(4d-7j\) bounds that symbol. Arbitrary
higher local Taylor coefficients require their chosen frame and lower
terms.

The coefficient vanishing divisor \(D_f\) of \(f\) has multiplicity at
\(p\) given by the minimum of the valuations of its coefficients in
a regular frame over \(\mathcal O_{C,p}\). It measures the common
scalar factor of the symbol. A positive coefficient means the degree
\(r_F\) symbol vanishes on the transverse fiber there. The section can
still be nonzero as a germ, so a jump of slice order is different from
membership in a higher sheaf power. Define \(D_g\) in the same way.

The resultant of the two binary symbols is a section of
\[
 (\det E)^{r_F r_G}\otimes
 \mathcal O_C(a)^{r_G}\otimes\mathcal O_C(b)^{r_F},
 \qquad \deg=4(ar_G+br_F)-14r_Fr_G.
\]
Indeed a binary change of variables acts by the determinant to the power
\(r_Fr_G\), and the scalar degrees of the resultant in the two symbols
are \(r_G,r_F\). If the symbols are generically coprime, its divisor
counts special common directions with the scalar contributions
\(r_GD_f+r_FD_g\) and the resultant divisor of the primitive symbols
after dividing out their contents. A generic common direction makes
the resultant identically zero. The corresponding common locus on
\(\mathbf P(N_C)\) then has a component dominating \(C\). Special
fibers can carry vertical excess, for example a whole exceptional fiber
when both symbols vanish there. [Global resultant
calculation](formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant) ·
[Strict transforms and vertical cycles](02-two-surfaces.md#22-the-common-graph-and-its-two-contractions).

Further excess divisors can arise from saturation of the **full** normal
relation modules. For example, in the sole-supported lci setting with
full generic initial ideal a coprime binary CI of degrees \(2\le r<s\), a first
relation with image \(L(-D)\) in its saturated line \(L\) has a
quotient-relation resultant with divisor supported on \(D\).
This comparison uses the actual relations and their generation
lengths. [Statement and hypotheses](../results/nonsaturated_first_relation_resultant.md#statement-and-hypotheses) ·
[Effective resultant proof](../supplements/FIRST_RELATION_AND_SPECTRAL_ROOTS.md#5-the-effective-resultant-divisor).

### Two filtrations and the full normal cone

The decreasing minimum-weight filtration is
\(W^\ell S=\bigoplus_{j\ge\ell}S^{(w)}_j\), where \(S^{(w)}_j\)
denotes weight \(j\) in all ordinary degrees. Use \(-w\) for the
opposite direction. The normal filtration is \(\mathcal I\)-adic
on the ambient sheaf and uses \(D^j\) on actual homogeneous source
spaces. Each \(D^j S_d\) is \(T_C\)-stable, so its ambient weight
decomposition is direct and the order of a nonzero sum of weight
components is the minimum of their normal orders. A single extreme
weight need not realize that minimum. The ambient intersection
filtration \(W^\ell S\cap D^j S\) is multiplicative, so
\[
 \bigoplus_{\ell,j\in\mathbf Z}
 (W^\ell S\cap D^j S)\,h^{-\ell}\varepsilon^{-j}
 \ \subset\ S[h^{\pm1},\varepsilon^{\pm1}]
\]
is an extended two-parameter Rees algebra, with \(D^j S=S\) for
\(j\le0\). In normal degree \(j\), a weight-\(i\) element \(f\in D^j S\)
contributes \(f h^{-i}\varepsilon^{-j}\) and its nonnegative
\(h\)-multiples. Shifting each weight by \(h^{-i}\) identifies the
ambient algebra with the extended normal Rees algebra with \(h\)
adjoined. Specialization of a mixed ideal or a quotient requires
its own comparison.

For the sheaf \(\mathcal J\) of \(J\), the full normal initial ideal
\(H=\operatorname{in}_{\mathcal I}(\mathcal J)\) has degree-\(j\)
piece \(((\mathcal J\cap\mathcal I^j)+\mathcal I^{j+1})/\mathcal I^{j+1}\).
Thus the normal cone algebra of \(Y\) along \(C\) is
\[
 \operatorname{gr}_{\mathcal I\mathcal O_Y}\mathcal O_Y
 =\operatorname{Sym}^\bullet E/H.
\]
It includes initials of all local combinations of the two equations.
The canonical surjection from \(H/(\operatorname{Sym}^{>0} E)H\)
onto the associated graded of \(\mathcal J/\mathcal I\mathcal J\)
uses the images of \(\mathcal J\cap\mathcal I^j\) as filtration steps.
Its kernel is
\(\operatorname{in}_{\mathcal I}(\mathcal I\mathcal J)/(\operatorname{Sym}^{>0} E)H\).
[Filtered equation comparison](../results/local_filtration_comparison_defect.md) ·
[Normal Koszul cancellation](../arguments/normal_koszul_cancellation.md).

## III. Extreme weights and full limits

### Restrictions on sole-support pairs

Suppose \(\sqrt J=P\). For each end of the weight range let
\(F_-,G_-\) denote the lowest nonzero components and \(F_+,G_+\) the
highest, with gcds \(h_-,h_+\). Hellus–Hübl's Theorem 1.2(a,b), for
this embedding over an algebraically closed field of characteristic
zero, gives
\[
 h_-,h_+\in P,\qquad
 \sqrt{(F_-,G_-)}=\sqrt{(h_-)},\qquad
 \sqrt{(F_+,G_+)}=\sqrt{(h_+)}.
\]
Both gcds are nonunits and each extreme pair has only height-one
minimal primes. This is a theorem about displayed components of a
hypothetical defining pair. [Hellus–Hübl, Theorem 1.2](https://arxiv.org/pdf/1312.7661).

Thoma's characteristic-zero bihomogeneous-carrier theorem concerns
smooth monomial space curves of degree greater than three. For \(C\)
the carrier condition is having one weight, and the trace argument
below verifies the exclusion with an arbitrary homogeneous mate over
the algebraically closed field \(k\). The earlier binomial-carrier
theorem likewise allows an arbitrary homogeneous mate and applies to
smooth nondegenerate monomial space curves other than the twisted cubic
in characteristic zero. [Thoma 1991](https://link.springer.com/article/10.1007/BF02568376) ·
[Thoma 1989, Theorem 3.1](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections).

Both equations of a hypothetical pair have at least two weights, and
at least one has at least three. The latter is Thoma's weight-count
restriction as recovered in Hellus–Hübl's Remark 1.4. Indeed, if each
equation had just its two extreme components, \(h_-,h_+\) would be a
weight-homogeneous pair with reduced support \(C\), since both contain
\(C\) and their common zeros lie in \(V(F,G)\). [Hellus–Hübl,
Remark 1.4](https://arxiv.org/pdf/1312.7661).

The repository trace restriction for this embedding gives \(ab=0\)
in \(k\) for a sole-support pair with at least one eigenform. It
therefore excludes this case in characteristic zero and forces
\(p\mid ab\) in characteristic \(p>0\). The trace proof also applies
under the two congruences \(F\equiv x_1^a\bmod x_0^2\) and
\(G\equiv x_2^b\bmod x_3^2\) after exchanging and rescaling the equations
as needed. An eigenform factor alone suffices for the characteristic-zero
exclusion by factor reduction. In positive characteristic that reduction
gives \(\max(a,b)\ge p\). A stable height-two homogeneous CI ideal with
radical \(P\) satisfies the trace restriction, since a character basis of
\(J/S_+J\) lifts to generators of the given ordinary degrees. The
extreme-component conclusion also holds in characteristic \(p>0\) under
\(p\nmid ab\). [Trace hypotheses and factor reduction](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#the-bound-and-its-exact-large-prime-minimum) ·
[Equivariant generator
lifting and trace consequence](../arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections) ·
[Prime-to-\(p\) extreme components](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#extreme-components-of-arbitrary-presentations).

A separate bound for **proper sextic eigenpairs**, with or without
containment of \(C\), is that their transverse quotient on \(\Omega/T_C\)
has total length at most eight, sharply, over an algebraically closed
field of any characteristic. It leaves at least four degrees on the
coordinate boundary.
[Sharp sextic quotient bound](../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound).

### First cancellation and the full homogeneous initial ideal

For either weight direction the full homogeneous initial ideal is
generated by the corresponding initial forms of **all** elements of
\(J\). For the minimum convention, write \(F_-=h_-A\),
\(G_-=h_-B\) with coprime homogeneous weight eigenforms \(A,B\). The
following computation uses only the gcd and the weight decomposition.
It applies to any such homogeneous pair, with a unit gcd allowed.
\[
 H_1=BF-AG=B(F-F_-)-A(G-G_-)\in J.
\]
The two initial products have equal weight and cancel. If \(H_1\ne0\),
its least-weight nonzero component lies in \(\operatorname{in}_w J\),
at weight strictly greater than the cancelled weight. It lies in \(P\)
whenever \(F,G\in P\), since \(P\) is weight graded. More explicitly,
at a positive gap \(j\) from the cancelled weight its component is
\(B F_{w(F_-)+j}-A G_{w(G_-)+j}\), using zero for absent terms. Use the
first **nonzero** such component. For a proper pair with nonunit gcd
the entire combination is nonzero, since \(BF=AG\) would give
\(F=AH',\ G=BH'\) with \(\deg H'=\deg h_->0\).

Membership in the smaller ideal \((F_-,G_-)=h_-(A,B)\) is a separate
test. Every component of this combination is in \((A,B)\), and its
initial belongs to the smaller ideal precisely if it is divisible by
\(h_-\) **and** the quotient belongs to \((A,B)\). If the initial
belongs to the smaller ideal, write it as \(LF_-+MG_-\) with
multipliers of the matching ordinary degrees and weights. Subtract
\(LF+MG\) and inspect the next surviving weight. A term outside the
smaller ideal gives an additional equation for the full initial
ideal. Further cancellations may still be needed. The maximal-weight
rule uses \(-w\). For the normal filtration the analogous
cancellation uses lifts of a homogeneous syzygy of the two normal
symbols, with the coefficient and equation orders aligned. Over
\(k(C)\) these can be lifts in the transverse local ring. Global
homogeneous lifts require actual source-space membership. [Normal
cancellation and filtered equation modules](../arguments/normal_koszul_cancellation.md) ·
[Exact sextic weight cancellation](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit).

For a fixed homogeneous ideal in \(S\), all diagonal weights are
organized by its Gröbner fan modulo the ordinary degree direction.
This applies to the unsaturated full initial ideals. The normal
filtration is a second Rees construction along the marked immersion.
Regularity identifies the ambient normal cone with the normal bundle,
and flat base change preserves the construction. Specialization to a
closed parameter fiber instead needs the power-quotient test below.
The Hilbert scheme of points represents finite locally free embedded
families such as \(W\) in Part IV. The tropical compactification
theorem, with proper closure and flat multiplication map, applies to
the reduced torus model there. Formation of the projective image under
parameter specialization uses the relative lattice in Part IV.
[Fukuda–Jensen–Thomas, §2](https://arxiv.org/pdf/math/0509544) ·
[Normal cone and deformation](https://stacks.math.columbia.edu/tag/0FBG) ·
[Hilbert scheme of points](https://stacks.math.columbia.edu/tag/0B94) ·
[Tevelev, Definition 1.1](https://arxiv.org/pdf/math/0412329).

### Opposite saturated Hilbert limits

Let \(h\) be the orbit-family parameter. The normalized substitutions
of the chosen \(F,G\) give equations on \(h\ne0\). Contract their
translated ideal from \(S[h,h^{-1}]\) to \(S[h]\), equivalently saturate
the normalized two-equation ideal by \(h\). Dividing lifted syzygies
by their common power of \(h\) is one way to obtain elements of this
contraction. Each graded piece of the quotient embeds in its
localization over \(k[h,h^{-1}]\), where the translated quotient is
free over the base. The pieces are therefore finite free over \(k[h]\).
The full weight initial ideal defines the special fiber with the
original graded Hilbert function. Irrelevant saturation gives the
ideal of the projective Hilbert limit and can change small-degree
pieces. Projective flatness preserves the Hilbert polynomial. Applying
the same construction with the opposite weights gives the other fixed
limit of the **same** orbit. [Full-limit construction and saturation](global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit).

When the two displayed initials are coprime, the special two-equation
ideal has height two. The two normalized equations form a regular
sequence, and adjoining \(h\) raises its height to three. Thus \(h\)
is regular on their quotient, the contraction adds no equations,
and the special fiber is itself a saturated complete intersection.
[Coprime presentation in a sextic residual family](../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit).

For sole support, a chosen power bound
\(\mathcal I^N\subset\mathcal J\subset\mathcal I\) and fixed Hilbert
polynomial define a closed projective \(T_C\)-stable incidence. Both
limits retain these inclusions, sole reduced support and the generic
length forced by the polynomial. Generation is tested on the moving
saturated height-two ideal \(J'\) via
\(J'_d/S_1J'_{d-1}\). The ideal defines a CI of type \((a,b)\) exactly
when these spaces have two basis classes with degrees \(a,b\), counted
with multiplicity. It is enough to test through an independently
established regularity bound on \(J'\). The incidence
allows embedded points, and fixed limits can require extra generators.
Occurrence of proposed pairs of opposite limits requires a separate
realization argument. [Supported
incidence and both limits](../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits) ·
[Moving-ideal generator test](../arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test).

## IV. Generic algebra and endpoint extension

### Generic transverse algebra

On \(\Omega\), complete the original intersection at the generic point
of \(C\) using the chart coefficient field \(K=k(C)=k(r)\).
The actual local ideal gives the Artinian complete intersection
\[
 A_\eta=K[[U,V]]/(F|_{x_0=1},G|_{x_0=1}),\qquad
 m_C=\dim_K A_\eta.
\]
Properness ensures that this local ideal is primary to \((U,V)\).
The plane intersection multiplicity inequality gives
\(m_C\ge r_Fr_G\), with equality exactly when the first binary
symbols are coprime over \(\overline K\). The colength of the **full**
normal initial ideal computes \(m_C\) even with a common direction.
For example \((U,U+V^n)\) with \(n\ge2\) has length \(n\) and both
displayed symbols equal to \(U\). The first-order symbols therefore
measure only the first contact. [Generic length and common normal
directions](02-two-surfaces.md#21-generic-length-and-common-normal-directions).

### Endpoint lattices and contact

For the constant case, let \(B\) be a finite positive-length quotient
of \(k[u^{\pm1},v^{\pm1}]\) with its named units, and let
\(n=\dim_k B\). Close the embedded product
\(\mathbf G_{m,r}\times\operatorname{Spec}B\) in \(\mathbf P^3\).
Its saturated ideal is the kernel of the degree-four parametrization
into \(B[s,t]\). In degree \(d\) the weight-\(w\) kernel tests
\(\sum_e c_e u^{e_2}v^{e_3}=0\) in \(B\) on the monomials of
that weight. The finite map \(\nu:\mathbf P^1_B\to Z_B\) to
that image is an isomorphism on \(\Omega\) and the two endpoint
completions are the image algebras
\[
 A_0=k[[r]][r^3u,r^4v]\subset B[[r]],\qquad
 A_\infty=k[[z]][z^3\alpha,z^4\beta]\subset B[[z]].
\]
They are finite free lattices of rank \(n\) over their indicated
parameter rings. At zero the filtration on the coefficient space \(B\)
in order \(j\) is the span of \(u^i v^l\) with \(i,l\ge0\) and
\(3i+4l\le j\), since each such monomial enters the image multiplied by
\(r^{3i+4l}\). At infinity the same recipe uses \(\alpha,\beta\) and
\(z\). Both filtrations eventually reach \(B\), since inverses of units
in a finite algebra are polynomials in those units. In an adapted
basis, each coefficient basis element entering at order \(j\) gives
a lattice generator multiplied by the \(j\)-th parameter power.
The index is the sum of these orders. [Finite image and purity](../arguments/torus_embedded_quotients.md#finite-image-and-purity) ·
[Endpoint defects](../arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial).

In a reduced orbit arrangement, pairwise contact at zero is the order
of the first differing graph coefficient, at order three for different
\(u\) values and at order four for equal \(u\) and distinct \(v\).
At infinity compare \(\alpha,\beta\) in the same way. For the
\(x_1\)-scaling root-of-unity arrangement this gives length four at
zero precisely when distinct labels have the same cube, length three
otherwise, and length three at infinity. These lengths describe the
embedded jets of **pairs** of branches. For a union of several
branches the full lattice records how each new branch meets the
preceding union. In the full \(\mu_8\) arrangement the pairwise contacts
over both endpoints sum to \(168\). Its total normalization defect is
\(136\).
[Pairwise contact and jet stabilizers](toric_torsion_and_endpoint_contacts.md#4-pairwise-endpoint-contact) ·
[Genus of the full arrangement](toric_torsion_and_endpoint_contacts.md#6-arithmetic-genus-and-normalization-defects).

### Conductor, torsion and descent

At an endpoint write \(A\subset \widetilde A\) for the image lattice
and its upstairs algebra. The finite torsion module
\(\widetilde A/A\) has length \(\delta\) over the parameter DVR.
The conductor \(\mathfrak c=\{b\in\widetilde A:b\widetilde A\subset A\}\)
is an ideal in both rings. The condition for a local function upstairs
to descend is that its class in \(\widetilde A/\mathfrak c\) belongs
to \(A/\mathfrak c\), or equivalently
\(A=\widetilde A\times_{\widetilde A/\mathfrak c}A/\mathfrak c\).
This uses the full finite algebras, including nilpotents. When \(A\)
is Gorenstein, as it is for a sole-supported complete intersection,
DVR lattice duality gives \(\ell(A/\mathfrak c)=\delta\) and
\(\ell(\widetilde A/\mathfrak c)=2\delta\), allowing a non-Gorenstein
upstairs algebra. For a reduced constant quotient \(B\), the finite
map \(\nu\) is the normalization.
[Full conductor boundary](tropical_thickenings_and_endpoint_duality.md#actual-endpoint-lattices-and-the-full-conductor-boundary) ·
[Fourth-root image and conductor](../arguments/torus_embedded_quotients.md#the-fourth-root-image-and-its-conductor).

The torsion of \(\widetilde A/A\) depends on the **embedded** quotient
and its multiplication. For \(B=k\) at \((u,v)=(1,1)\) both indices
are zero even though the ambient normal-frame cokernel has length seven
at each endpoint. The same abstract \(B\) can give different indices
in different embeddings. Torsion in the ordinary graded normal layers
of an intersection is a third object, measured by saturation of those
layers. [Distinct embeddings of the same finite algebra](../arguments/torus_embedded_quotients.md#embedded-quotients-and-characteristic-dependent-endpoints) ·
[Normal saturation defects](normal_filtration_boundary_obstructions.md).

For a proper pair with sole support on \(C\), let \(W\) be the
scheme-theoretic closure of the **entire** torus restriction in
\(\mathbf P^1_r\times\mathbf G_m^2\). Its ideal is contracted from
the punctured charts. In the generic algebra of length \(m_C\),
the nilpotent ideal \((U,V)\) has \(m_C\)-th power zero. By purity
this power vanishes on the torus restriction and then on \(W\) by
contraction. The projection \(\pi:W\to\mathbf P^1_r\) is finite, and
\(\mathcal B=\pi_*\mathcal O_W\) is a quotient of the constant bundle
with fiber \(k[U,V]/(U,V)^{m_C}\). Purity gives torsion-freeness on
the torus and contraction gives it at both endpoints, so \(\mathcal B\)
is locally free of rank \(m_C\). The projective parametrization extends
to \(\rho:W\to Y\), whose reduction is an isomorphism onto \(C\).
Properness and quasi-finiteness make \(\rho\) finite. It is an
isomorphism off the endpoints, and purity makes
\(\mathcal O_Y\to\rho_*\mathcal O_W\) injective.

At zero the image lattice is \(k[[r]][r^3U,r^4V]\). At infinity the
base parameter is \(\tau=r^{-1}\) and the projective parameter is
\(z=(u/v)\tau\). They define the same adic topology upstairs. A basis
of the common closed fiber lifts to a basis over \(k[[z]]\) by
completeness and \(z\)-torsion-freeness. The image lattice there is
\(k[[z]][z^3(\alpha-1),z^4(\beta-1)]\). These two inclusions give the
cokernel lengths \(\delta_0,\delta_\infty\) for \(\rho\).

If \(\deg\mathcal B=0\), global generation trivializes \(\mathcal B\).
Its multiplication and the coordinate sections \(U,V\) would be
constant. The resulting embedded family would have a \(T_C\)-invariant
scheme image, contradicting the characteristic-zero invariant CI
exclusion in Part III. Thus \(\deg\mathcal B>0\). The abstract
transverse algebra can stay isomorphic as its embedding varies.
The lattice parameter here runs along \(C\). The intrinsic limit
pulling that parameter toward an endpoint has pure quotient given by
the constant image of the corresponding embedded fiber. The two
embedded lengths in the full limit come from the relative image and
the Hilbert polynomial. For a hypothetical \((6,6)\) pair each
endpoint fiber must have total constant-image defect at least \(153\)
and pass the degree-six source test.
[Endpoint comparison](../results/intrinsic_limits_endpoint_fibers.md) ·
[Sextic endpoint conditions](../arguments/torus_hilbert_boundary.md#necessary-endpoint-conditions-for-a-sextic-pair) ·
[Entire finite modification](tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification) ·
[Moving endpoint lattices](tropical_thickenings_and_endpoint_duality.md#actual-endpoint-lattices-and-the-full-conductor-boundary) ·
[Strict movement](tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier) ·
[Remaining full-ideal comparison](../investigations/quotient-hilbert-comparison/index.md#question).

### The characteristic-seven control in both endpoint frames

For \(F=x_1^4-x_0^3x_3,\ G=x_2^7-x_0x_1x_3^5\), the quotient on
\(\Omega/T_C\) is \((v-1,u^7-1)\). The original equations form a
proper CI in either characteristic and have no coordinate-boundary
curve, as follows directly on \(x_0=0\) and \(x_3=0\).
At zero the quotient basis \(1,u,\ldots,u^6\) enters with weights
\(0,3,\ldots,18\), giving \(D_0=63\).
At infinity \(\alpha=u^{-3},\beta=u^{-4}\). The smallest values in
the semigroup generated by \(3,4\) in the seven residue classes modulo
seven are \(0,8,9,3,4,12,6\), giving \(D_\infty=42\).
The corresponding monomials in \(u\) form a basis of
\(k[u]/(u^7-1)\) in every characteristic. The total \(105\) gives
\(28n+7-105=28n-98\),
the degree-\((4,7)\) CI polynomial.

In characteristic seven this algebra is \(k[U]/(U^7)\), the family is
constant, and \(h=0\). The two displayed equations have common linear
normal symbol \(V\), while their full local ideal contains \(U^7\).
Thus the normal orders have product one and the normal length is seven.
In characteristic zero the first symbols are independent, and the
marked length at each of the seven roots is one. The projective
intersection has seven distinct quartic components. The Frobenius
collision changes the embedded algebras and support while preserving
the same endpoint-index sum and projective CI polynomial. In
characteristic seven, \(h=0\) is compatible with the trace theorem
because seven divides the degree product. The trace proof concerns
the generic multiplicity of the full
nonreduced algebra and allows the reduced fourfold projection to be
separable. The actual two global equations hold in both fields.
[Entire finite modification and characteristic scope](tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier) ·
[All reduced binomial components](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#12d-necessity-of-the-frobenius-exponent-and-all-reduced-components).

#### Higher jets of the seven branches in characteristic zero

Write \(Z=V(F,G)\) for this pair over the algebraically closed field
of characteristic zero. Its branches come from the curves
\[
C_\zeta=[s^4:s^3t:\zeta st^3:t^4],\qquad \zeta\in\mu_7.
\]
At \(p_0\) put \((r,y,w)=(x_1,x_2,x_3)/x_0\). At \(p_\infty\) put
\((z,b,a)=(x_2,x_1,x_0)/x_3\). The exact graph equations are
\[
\begin{array}{c|cc}
 & \text{order three} & \text{order four}\\ \hline
p_0 & y=\zeta r^3 & w=r^4\\
p_\infty & b=\zeta^{-3}z^3 & a=\zeta^{-4}z^4.
\end{array}
\]
The embedded jets of the individual branches agree through order two,
and every pair separates at order three at both points. In fact
\(\zeta\mapsto\zeta^{-3}\) permutes \(\mu_7\), so the difference of
the cubic graph functions generates the pairwise intersection ideal
\((r^3)\) or \((z^3)\) in the parameter ring. At order four the
coefficient at \(p_0\) is common to all branches. At \(p_\infty\) the
quartic coefficient is the inverse of the cubic coefficient and
supplies a third independent character, alongside \(1\) and the cubic
coefficient. [Embedded jet convention](toric_torsion_and_endpoint_contacts.md#5-intrinsic-interpretation-by-jet-stabilizers).

The completed rings of the whole intersection are
\[
A_0=k[[r,y]]/(y^7-r^{21}),\qquad
A_\infty=k[[z,a,b]]/(ab-z^7,\ a^3-b^4).
\]
At zero this follows by eliminating \(w=r^4\). At infinity the two
equations give the reductions
\[
ab\longmapsto z^7,\qquad a^3\longmapsto b^4,\qquad
b^5\longmapsto a^2z^7 .
\]
The third reduction follows from \(b^5=a^3b=a^2z^7\). Each step
decreases \(3\deg_a+2\deg_b\) on a monomial and increases its ordinary
total degree. Thus they give convergent reductions of formal series
to the span of \(1,b,a,b^2,a^2,b^3,b^4\) over \(k[[z]]\).
The seven images in the product of the branch rings have distinct
characters of \(\mu_7\), so the reduced monomials form a free basis.
At zero the corresponding basis over \(k[[r]]\) is \(1,y,\ldots,y^6\).

Identify the coefficient algebra of the normalization with
\(B=k[u]/(u^7-1)=k^{\mu_7}\), where \(u(\zeta)=\zeta\). The least
order \(d_{e,i}\) at which \(u^i\) occurs in the image at endpoint
\(p_e\) follows from these two bases.

| Endpoint | \(1\) | \(u\) | \(u^2\) | \(u^3\) | \(u^4\) | \(u^5\) | \(u^6\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(p_0\) | 0 | 3 | 6 | 9 | 12 | 15 | 18 |
| \(p_\infty\) | 0 | 6 | 12 | 4 | 3 | 9 | 8 |

At each order \(d\) the allowed coefficients are precisely the span
of the characters with \(d_{e,i}\le d\). This describes the image in
the product of the normalized branch jets at every order. The
coefficient of the parameter to power \(d\) can be prescribed
independently on every branch for \(d\ge18\) at \(p_0\) and \(d\ge12\)
at \(p_\infty\). The conductors are \(r^{18}B[[r]]\) and
\(z^{12}B[[z]]\). Indeed, multiplication by a branch idempotent isolates its
coefficient, and the character expansion
\(\frac17\sum_{i=0}^6\zeta^{-i}u^i\) of that idempotent uses all
seven characters. A proper span in the table cannot contain it.
The sums of the entry orders recover the two normalization defects
\(63\) and \(42\).

For the ordinary jets of the intersection, use \(A_e/\mathfrak m_e^{n+1}\).
With bars denoting degree-one classes, the two tangent
cones are
\[
\operatorname{gr}_{\mathfrak m_0} A_0=k[\bar r,\bar y]/(\bar y^7),
\qquad
\operatorname{gr}_{\mathfrak m_\infty} A_\infty
  =k[\bar z,\bar a,\bar b]/(\bar a\bar b,\bar a^3,\bar b^5).
\]
The degree-increasing reductions at infinity preserve the lower
bound on the total degree of any monomial in \(\mathfrak m_\infty^n\).
The reduced monomials are independent and each lies in the maximal
ideal power given by its total degree, which proves the second
tangent-cone presentation. The successive graded dimensions at
zero are \(1,2,3,4,5,6,7,\ldots\), and at infinity they are
\(1,3,5,6,7,\ldots\). Both sequences stay at \(7\) once they reach it.

## V. Global constraints

### Postulation and support

For a proper homogeneous pair \((F,G)\), the Koszul resolution gives
\[
 \operatorname{Hilb}_{S/J}(z)=\frac{(1-z^a)(1-z^b)}{(1-z)^4},
 \qquad
 H_{S/J}(d)=b_3(d)-b_3(d-a)-b_3(d-b)+b_3(d-a-b),
\]
where \(b_3(j)=\binom{j+3}{3}\) for \(j\ge0\), and \(0\) otherwise.
For large \(d\) this is
\[
 P_Y(d)=ab\,d+\frac{ab(4-a-b)}2,\qquad
 p_a(Y)=1+\frac{ab(a+b-4)}2.
\]
The regular sequence makes \(S/J\) Cohen–Macaulay of dimension two,
so \(J\) is saturated and \(Y\) is pure with no embedded points.
Its fundamental cycle is
\[
 [Y]=m_C[C]+R,\qquad ab=4m_C+\deg R,
\]
where \(R\) is effective and has no \(C\)-component. For this proper
pair, sole reduced support is equivalent to \(\deg R=0\), or
\(m_C=ab/4\). In particular \(4\mid ab\) is necessary for sole
support. If a proposed subscheme is already contained in \(Y\),
equality of degrees also forces scheme equality by purity. This is
the degree-exhaustion step in the exact CI criterion for a constant
embedded quotient, after finding two coprime forms in its actual
homogeneous kernel. [Koszul polynomial](../arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test) ·
[Pure-curve degree exhaustion and equation criterion](../arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion).

The constant image of Part IV has polynomial
\(4nd+n-\delta_0-\delta_\infty\) and genus
\(1-n+\delta_0+\delta_\infty\). Indeed its finite modification has
Euler characteristic \(n(4d+1)\) in twist \(d\), and the endpoint
cokernels subtract a constant. For the moving finite modification
of an actual sole-support CI, put \(e=\deg\mathcal B\). Subtracting
\(\chi(\mathcal O_Y)\) from \(\chi(\mathcal B)=m_C+e\) gives
\[
 \delta_0+\delta_\infty=e+m_C(2a+2b-7).
\]
These lengths contribute to the constant term, whereas generic lengths
and residual curve degrees contribute to the linear coefficient.
For \((6,6)\), the CI polynomial is \(36d-144\), the genus is \(145\),
and sole support would give \(m_C=9\) and total endpoint index \(e+153\).
[Constant image polynomial](../arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial) ·
[Moving endpoint budget](tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification).

### Normal contact and residual cycles

For an actual sole-support pair, suppose the first symbols were
generically coprime, so \(m_C=r_Fr_G\). At each point of \(C\),
complete and choose a parameter lift for a transverse slice. Sole
support makes the completed algebra finite over the parameter DVR,
and the CM property makes the parameter a nonzerodivisor. The slice
has length \(m_C\), the rank of that free module. Its two orders are
at least \(r_F,r_G\) by the global sheaf-power condition. Equality in
the plane intersection inequality forces both orders to stay
\(r_F,r_G\) and their symbols to stay coprime. The resultant would be
nowhere zero. Its degree from Part II and the sole-support degree
formula would give
\[
 \frac{a}{r_F}+\frac{b}{r_G}=\frac{7}{2}, \qquad
 \frac{ab}{r_Fr_G}=4.
\]
The sum is at least four by the arithmetic–geometric mean inequality.
Thus sole support forces common generic normal directions and
\(m_C>r_Fr_G\). This restriction concerns the first normal symbols.
[Global resultant obstruction](formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant).

Common factors have different roles in the two filtrations. A common
normal factor is a generic direction of continued contact on the
blowup. Residual curves are the strict intersection components off
the exceptional divisor, pushed down to \(\mathbf P^3\). A vertical
exceptional component pushes down to a point. In the raw extreme
fiber \(V(h_\pm A,h_\pm B)=V(h_\pm)\cup V(A,B)\), so a common
weight factor gives a surface.
Cancellation equations in the full limit can cut that surface down
to curves. For the sextic example below, the colon by \(q\) and the
restriction modulo \(q\) compute the residual divisor cycle on \(Q\),
while the full ideal retains its endpoint scheme. [Blowup and residual
cycle](02-two-surfaces.md#22-the-common-graph-and-its-two-contractions) ·
[Colon and divisor-cycle proof](../arguments/torus_sextic_residuals.md#a-colon-formula-for-divisor-cycles).

The dense-torus quotient controls only the part of the cycle seen
there. For a proper eigenpair the quotient on \(\Omega/T_C\) is
finite. Each of its points closes to a quartic orbit with multiplicity
equal to its local quotient length. For total quotient length \(n\)
the remaining cycle on the coordinate boundary has degree \(ab-4n\).
Identifying the marked orbit also requires its point \((1,1)\) and
its own local length. For mixed-weight pairs the generic normal
algebra is taken over \(k(C)\) and the product description by a
constant quotient requires an extra hypothesis. [Orbit curves and
quotient multiplicities](../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree).

### What the Hilbert function controls

The Hilbert function counts dimensions of graded pieces. ACM requires
depth two for the saturated coordinate ring, equivalently vanishing of
the Rao module \(\bigoplus_d H^1(\mathcal I_Y(d))\) for a pure curve.
For an ACM curve, multiplying its Hilbert series by \((1-z)^2\)
gives the Hilbert series after quotienting by a regular sequence of
two general linear forms. Thus a negative coefficient excludes ACM.
For the reduced quartic \(C\) the Hilbert function starts \(1,4,9,13\)
and equals \(4d+1\) for \(d\ge2\). The degree-two weight sums fill
\(0,\ldots,8\), and adding weights \(0\) and \(4\) inductively fills
\(0,\ldots,4d\) in every higher degree. The resulting numerator is
\(1+2z+2z^2-z^3\).
The CI Hilbert series follows from the Koszul resolution, whose
regular-sequence hypothesis proves ACM. The same series can arise
with different Betti numbers and depth. For a numerical check even
with a saturated ideal, in \(k[x,y,v,w]\) the quotient by
\((x^2,xy,xv^2,y^4)\) has Hilbert series
\[
 \frac{1-z^4}{(1-z)^3}+\frac{z+z^2}{1-z}
 =\frac{(1-z^2)^2}{(1-z)^4}.
\]
The first summand counts terms without \(x\), and the second counts
\(x,xv\) times powers of \(w\). The variable \(w\) is regular, proving
saturation, but modulo \(w\) the class of \(xv\) lies in the socle,
so the ring has depth one. This illustrates the distinction between
numerical and actual ACM. In Part VI the special fiber is ACM by
Hilbert–Burch and shares the CI series with its general fiber while
requiring three generators. [Migliore–Nagel, numerical ACM and the
Hilbert function](https://arxiv.org/abs/1202.2275) ·
[Sextic special-fiber resolution](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit).

## VI. The filtrations together in the sextic example

### Comparison diagram

Let \(\mathcal Y\) be the flat projective orbit closure over a
parameter chart of one direction, with special fiber \(Y_\pm\).
Read the sheaves on \(Y_\pm\) by pushforward along the closed fiber
inclusion. The inclusion of \(C\) gives the relative normal ideal
\(\mathcal K=\mathcal I\mathcal O_{\mathcal Y}\) (with \(\mathcal I\)
pulled back from \(\mathbf P^3\)), and let \(\mathcal K_\pm\) be its
image on the special fiber. The two routes are
\[
\begin{array}{ccc}
 \mathcal O_{\mathcal Y}
   &\xrightarrow{\text{full weight limit}}&\mathcal O_{Y_\pm}\\
 \downarrow\scriptstyle{\operatorname{gr}_{\mathcal K}}
   &&\downarrow\scriptstyle{\operatorname{gr}_{\mathcal K_\pm}}\\
 \operatorname{gr}_{\mathcal K}\mathcal O_{\mathcal Y}
   &\xrightarrow{\text{base change, then quotient}}&
      \operatorname{gr}_{\mathcal K_\pm}\mathcal O_{Y_\pm}.
\end{array}
\]
At the bottom, reduction induces a surjection after tensoring with
the special residue field, because the images of the powers of
\(\mathcal K\) are the powers of \(\mathcal K_\pm\).
Flatness of the power quotients over the parameter DVR suffices for
the bottom map after tensoring to be an isomorphism, by the
degreewise Tor sequence. The flat projective family gives the
specialization in the top row and preserves the Hilbert polynomial.
The endpoint construction in Part IV takes a finite image over a
parameter on the curve itself.
[Normal-cone base-change criterion](../results/normal_cone_slice_specialization.md#statement) ·
[Finite-flat slice with different normal algebras](../results/supported_length_five_defect_specialization.md) ·
[Geometric endpoints versus opposite Hilbert limits](../investigations/quotient-hilbert-comparison/index.md#method).

### A verified full sextic limit

<a id="4-the-hilbert-scheme-limit-remembers-relations-between-equations"></a>

Use \(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\),
\(B_3=x_0x_2^2-x_1^2x_3\), and put
\(a_6=x_0^2x_3A\), \(b_4=x_0^3x_2\). The proper sextic pair of
R-0046 is
\[
 F=q^3+a_6,\qquad G=q^3+x_0^2x_1B_3,\qquad G-F=-b_4q.
\]
The weights of \(q,A,B_3,a_6,b_4\) are \(4,3,6,7,3\),
respectively. Both displayed highest components are \(q^3\), of
weight twelve. Their first cancellation already gives \(b_4q\), of
weight seven. In the presentation \(J=(q^3+a_6,b_4q)\), lifting the
next syzygy gives the maximal-weight orbit family identity
\[
 b_4(q^3+h^5a_6)-q^2(b_4q)=h^5 a_6b_4.
\]
The right-hand side divided by \(h^5\) gives the indispensable
degree-ten equation. The Hilbert–Burch proof identifies the entire
contracted family as
\((q^3+h^5a_6,b_4q,a_6b_4)\). In particular the special ideal
\[
 J_+=(q^3,b_4q,a_6b_4)
\]
is the full initial ideal and is irrelevant-saturated. It is ACM,
with minimal generator degrees \(6,6,10\) and syzygy degrees
\(10,12\). The two degree-ten contributions cancel in its Hilbert
numerator, leaving \(1-2z^6+z^{12}\). [Full family, flatness,
saturation and resolution](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit).

<a id="41-how-the-boundary-cycle-changes-in-the-full-limit"></a>

The full ideal matters even though \(b_4\) and \(x_0^2x_3\) are units
on \(\Omega\). There both ideals are \((q,A)\), so the marked
generic algebra is \(k(C)\) and the transverse quotient is \(k\)
on each fiber. Globally, write \(L_{ij}\) for the line spanned by the
two coordinate points with indices \(i,j\) and
\(T=V(x_2,x_0x_3^2-x_1^3)\) for the irreducible plane cubic.
The original and limiting cycles are
\[
\begin{aligned}
 [Y]&=[C]+13[L_{23}]+13[L_{13}]+2[L_{01}]+[L_{02}]+[T],\\
 [Y_+]&=[C]+13[L_{23}]+14[L_{13}]+4[L_{01}]+[L_{02}].
\end{aligned}
\]
For the special fiber \(J_+:q=(q^2,b_4)\) and
\(J_++(q)=(q,a_6b_4)\), giving the cycle
\(\operatorname{div}_Q(a_6|_Q)+3\operatorname{div}_Q(b_4|_Q)\).
In the original fiber, splitting the divisor of \(b_4q\) on \(F=0\)
gives the original cycle. Equivalently the cubic specializes as a
plane divisor to \([L_{13}]+2[L_{01}]\), accounting for the change.
Both have total degree \(36\), residual degree \(32\), genus \(145\)
and no embedded associated components. [Cycles and local
multiplicities](../arguments/torus_sextic_residuals.md#cycles-and-endpoint-schemes-of-the-three-generator-limit).

The endpoint schemes retain the localized ideals themselves. In the
table \((q_i,a_i,b_i)\) are the indicated affine restrictions of
\((q,a_6,b_4)\), localized at the origin. The ideals are
\((q_i^3+a_i,b_iq_i)\) before and \((q_i^3,b_iq_i,a_ib_i)\) after
specialization.

| Chart and coordinates | \(q_i\) | \(a_i\) | \(b_i\) |
| --- | --- | --- | --- |
| \(x_0=1\), \((r,y,z)=(x_1,x_2,x_3)\) | \(z-ry\) | \(z(y-r^3)\) | \(y\) |
| \(x_3=1\), \((\xi,\eta,\zeta)=(x_0,x_1,x_2)\) | \(\xi-\eta\zeta\) | \(\xi^2(\xi^2\zeta-\eta^3)\) | \(\xi^3\zeta\) |

The dense open thus has identical normal length while the special
boundary has changed as a scheme and as a cycle. This example
belongs to the residual locus. The sole-support incidence of Part III
has its own preservation proof and its own moving generator test.
[Exact endpoint chart ideals and scope of R-0046](../results/sextic_three_generator_full_limit.md#statement).

### Supplementary sextic source spaces and pencils

<a id="sextic-source-spaces-and-pencils"></a>

<a id="6-from-invariant-examples-to-the-supported-ci-hilbert-locus"></a>
<a id="7-parameter-spaces-pencils-fixed-loci-and-deformation-strata"></a>

The normal-order and moving-generator tests use different source
spaces. For a degree-six form, write its 84 ambient monomials in the
torus chart as \(r^w u^i v^j\) with coefficients \(c_{w,i,j}\).
Membership in \(H^0(\mathcal I^2(6))\) is equivalent, separately
at each weight, to
\[
 \sum_{i,j}c_{w,i,j}=0,\qquad
 \sum_{i,j}i c_{w,i,j}=0,\qquad
 \sum_{i,j}j c_{w,i,j}=0.
\]
These are the value and two first normal coefficients at \((1,1)\).
The local-freeness argument of Part II gives the global sheaf-power
condition. The weight dimensions in weights six through eighteen
are \((1,1,2,2,2,2,3,2,2,2,2,1,1)\), summing to \(23\).
[Characteristic-free actual sextic sources](../supplements/ACTUAL_EQUATION_SPACES.md) ·
[Exact coefficient verifier](../investigations/torus-residual-controls/verify.py).

With \(D_3=x_2^3-x_1x_3^2\), the dense-torus expressions for
\((q,A,B_3,D_3)\) from the quartic ideal are
\[
(r^4(v-u),\ r^3(u-1),\ r^6(u^2-v),\ r^9(u^3-v^2)).
\]
On \(Q\) one has \(u=v\), and every degree-six double section
restricts to \(r^6(u-1)^2R(r^3u)\) with \(\deg R\le4\). In Segre
coordinates \(x=(ac,ad,bc,bd)\) this is \((bc^3-ad^3)^2\) times
a section of \(\mathcal O_Q(4,0)\). Cubic matching for higher lifts
uses the actual equation source. A separate reviewed reduction,
in characteristic zero or \(p\ge7\), proves that every proper
sole-support \((6,6)\) pair would have generic curvilinear length
nine and would satisfy the necessary divisor profiles in that proof.
The reduction uses the quadric restriction, the balanced normal
bundle and actual saturated duality. [Actual cubic
matching](rank_strata_and_sextic_lifts.md) ·
[Sole-support sextic reduction](../supplements/SEXTIC_PAIR_REDUCTION.md).

For equal degrees the equation pencils live in
\(\operatorname{Gr}(2,H^0(\mathcal I(d)))\). The reduced quartic has
Hilbert function \(4d+1\) for \(d\ge2\), giving source dimensions
\(18\) for \(d=4\) and \(59\) for \(d=6\). The corresponding
pencil dimensions are \(32\) and \(114\). Pencils consisting entirely
of double sextics form \(\operatorname{Gr}(2,23)\), of dimension \(42\)
and codimension \(72\) in the sextic pencil space. Dependence of two
normal symbols over \(k(C)\) can occur without a constant combination
in the double-sextic source, so the codimension measures this pencil
condition. Generation on the Hilbert locus still uses the full ideal.
[Normal source spaces](../supplements/ACTUAL_EQUATION_SPACES.md) ·
[Moving generator criterion](../results/moving_ideal_generator_criterion.md#statement).

The quartic root pencil illustrates another difference between parameter
spaces. For \(z^4-\eta z+\eta-1\) the discriminant in characteristic
zero is \((\eta-4)^2(-27\eta^2+40\eta-16)\). It detects collisions of
roots. At \(\eta=1\) a separable root reaches zero and leaves the quotient
torus. This and the boundary at \(\eta=\infty\) are separate events from
the marked and residual collisions. These calculations describe the
specified parameter line. [Quartic root pencil](root_pencil_geometry.md#3-three-ways-the-pencil-leaves-the-open-arrangement).

### Source map and scope

<a id="proofs-of-orbit-multiplicities-and-full-limits"></a>
<a id="1-orbit-families-and-the-residual-boundary"></a>
<a id="5-the-geometry-of-invariant-curve-strata"></a>
<a id="11-eight-quotient-points-and-a-quadruple-residual-line"></a>
<a id="12-six-quotient-points-and-a-twelvefold-residual-line"></a>
<a id="13-a-noncurvilinear-quotient-of-the-same-length"></a>
<a id="2-fixed-point-incidence-forces-residual-boundary-for-eigenpairs"></a>
<a id="3-residual-curves-move-before-they-acquire-boundary-support"></a>
<a id="31-specializing-divisors-not-attracting-individual-points"></a>
<a id="32-absorption-changes-the-decomposition-into-marked-and-residual-cycles"></a>

| Part | Established on the stated inputs | Conditional statement or open comparison | Proof homes |
| --- | --- | --- | --- |
| I | Balanced conormal, transverse transport and frame divisor | A transverse boundary moves the marked support off the coordinate torus | [Conormal transition](../arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0), [normal map](tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map), [transverse control](../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two) |
| II | Actual normal symbols, binary resultant, full normal cone | The quotient-relation resultant bound uses a full generic binary CI and an actual sole-supported lci thickening | [Global resultant](formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant), [equation comparison](../arguments/filtered_equation_comparison.md), [quotient-relation bound](../results/nonsaturated_first_relation_resultant.md) |
| III | Full opposite limits and moving-ideal generation | Extreme gcds require a hypothetical sole-support pair. The trace and length-eight restrictions have their stated equivariance hypotheses | [Hellus–Hübl](https://arxiv.org/pdf/1312.7661), [weight restrictions](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md), [full supported limits](../arguments/torus_hilbert_boundary.md), [sextic bound](../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound) |
| IV | Endpoint lattices, conductor, pure intrinsic limits and embedded lengths | Strict movement is conditional on an actual sole-support CI. Full opposite-endpoint algebras and moving equation incidence remain open | [Constant quotient descent](../arguments/torus_embedded_quotients.md), [moving modification](tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification), [intrinsic comparison](../arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits) |
| V | CI postulation and degree exhaustion for a pure containing curve | Sole support is tested by the full degree budget, with residual boundary degrees included | [Two surfaces](02-two-surfaces.md), [degree exhaustion](../arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion), [orbit degrees](../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree) |
| VI | R-0046 gives a saturated ACM limit with three generators and residual degree \(32\) | Base change for the relative normal cone of a proposed family needs its own hypotheses. Recovery of arbitrary supported CI presentations from opposite limits is open | [R-0046 proof](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit), [normal-cone criterion](../results/normal_cone_slice_specialization.md), [supported-boundary framework](../frameworks/torus_supported_boundaries.md#directional-loci) |

Other reviewed sextic controls retain their separate proof sections
for [length-eight and length-six quotient schemes](../arguments/torus_sextic_residuals.md#eigenpair-residual-controls),
[moving residual divisor limits](../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit),
and [residual absorption](../arguments/torus_sextic_residuals.md#residual-absorption-in-a-proper-flat-family).
The [historical source review](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md#L625-L631)
records the scope of the original residual and full-limit checks.
