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

## Mixed-weight sextic: exact quadric restriction and four residual lines

For `c_0=t^3-w`, `c_2=w^3-t(tw+q)^2`, and `f=h q^3+c_2^2-c_0^2`, the restriction to the containing quadric is
\[
f|_{q=0}=(w-t^3)^2(w^4-1).
\]
Consequently the residual ruling lines are `w^4=1`; along each such line `c_2=-w^2 c_0`. The quadratic normal initial form at the marked curve, in `w=t^3+u`, is
\[
4t^{10}q^2-4t^{11}qu+(t^{12}-1)u^2,
\]
whose discriminant is `16t^{10}`. This is a split normal node over the function field, in contrast to the nonsplit control in the global-equations chapter. The derivative of the quadric restriction at `w=1` equals `4(1-t^3)^2`, proving generic smoothness of that residual line away from its contact points. These are exact restrictions and attachment identities, not a classification of all sextic carriers or an STCI construction.


### Archived exact certificate: `research/computations/ci_cycle_line_degeneration_2026_10_25.py`

The following original computational certificate is preserved verbatim, with its original hypotheses, limitations, and external dependencies. No additional mathematical conclusion is asserted by its archival transfer.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Exact global-source, ruling-line, and boundary identities; stdlib only.

The Macaulay2 companion checks projective schemes. This file checks explicit
polynomial identities and squarefreeness, not global genericity or flatness.
"""
from fractions import Fraction
import json
from pathlib import Path

NV=6

def const(n): return {(0,)*NV:n} if n else {}
def var(i):
    e=[0]*NV; e[i]=1; return {tuple(e):1}
def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}
def scale(p,c): return {m:c*v for m,v in p.items() if c*v}
def sub(p,q): return add(p,scale(q,-1))
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            e=tuple(x+y for x,y in zip(m,n)); out[e]=out.get(e,0)+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def diff(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            e=list(m); e[i]-=1; out[tuple(e)]=c*m[i]
    return out
def subst(p,images):
    out={}
    for m,c in p.items():
        term=const(c)
        for image,n in zip(images,m): term=mul(term,power(image,n))
        out=add(out,term)
    return out

checks={}
# Segre restriction and moving ruling line.
a,b,A,B,c,d=[var(i) for i in range(6)]
x0=mul(A,c); x1=mul(A,d); x2=mul(B,c); x3=mul(B,d)
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
curve_factor=sub(mul(A,power(d,3)),mul(B,power(c,3)))
checks['f_segre_factorization']=add(F,mul(mul(a,x0),left))==mul(mul(power(A,3),add(d,mul(a,c))),curve_factor)
checks['g_segre_factorization']=add(G,mul(mul(b,x3),right))==scale(mul(mul(power(B,3),add(c,mul(b,d))),curve_factor),-1)
# Actual homogeneous sources and their independently differentiated symbols on C.
x0,x1,x2,x3,a,b=[var(i) for i in range(6)]
Q=sub(mul(x0,x3),mul(x1,x2))
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
H0=add(*(power(x,2) for x in [x0,x1,x2,x3]),mul(x0,x2),scale(mul(x1,x3),2))
H1=add(scale(power(x0,2),2),scale(power(x1,2),3),scale(power(x2,2),5),scale(power(x3,2),7),mul(x0,x1),mul(x0,x3),mul(x1,x2),scale(mul(x2,x3),3))
f=add(F,mul(Q,H0),mul(mul(a,x0),left))
g=add(G,mul(Q,H1),mul(mul(b,x3),right))
# Directly restrict the actual pair to the moving line in its ruling.
pa,pb,lr,ls=var(0),var(1),var(2),var(3)
line_images=[lr,scale(mul(pa,lr),-1),ls,scale(mul(pa,ls),-1),pa,pb]
checks['moving_ruling_actual_restriction']=not subst(f,line_images) and subst(g,line_images)==mul(mul(power(ls,3),sub(const(1),mul(pa,pb))),add(mul(power(pa,3),lr),ls))
fixed_images=[scale(lr,-1),lr,scale(ls,-1),ls,pa,pb]
checks['fixed_line_actual_restriction']=subst(f,fixed_images)==mul(mul(sub(const(1),pa),power(lr,3)),add(lr,ls)) and subst(g,fixed_images)==mul(mul(sub(const(1),pb),power(ls,3)),add(lr,ls))
a1,b1,u=var(0),var(1),var(2)
images=[const(1),u,power(u,3),power(u,4),a1,b1]
restrict=lambda p: subst(p,images)
checks['all_actual_pairs_vanish_on_C']=not restrict(f) and not restrict(g)
af,bf=restrict(diff(f,3)),restrict(diff(f,2))
ag,bg=restrict(diff(g,3)),restrict(diff(g,2))
det=sub(mul(af,bg),mul(bf,ag))
h0,h1=restrict(H0),restrict(H1)
expected=add(mul(add(u,a1),h1),mul(mul(power(u,9),add(const(1),mul(b1,u))),h0),scale(mul(a1,power(u,8)),-3),scale(mul(add(const(4),scale(mul(a1,b1),2)),power(u,9)),-1),scale(mul(b1,power(u,10)),-3))
checks['two_parameter_actual_boundary_formula']=det==expected
at11=lambda p:subst(p,[const(1),const(1),u,const(1),const(1),const(1)])
Eboundary=add(h1,mul(power(u,9),h0),scale(power(u,8),-3),scale(power(u,9),-3))
checks['boundary_splits_one_plus_seventeen']=at11(det)==mul(add(u,const(1)),Eboundary)
coeffs=[Eboundary.get(tuple([0,0,i,0,0,0]),0) for i in range(18)]
checks['shared_point_not_a_triple']=sum(c*((-1)**i) for i,c in enumerate(coeffs))==14
checks['both_endpoints_free']=coeffs[0]==2 and coeffs[-1]==1

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def remainder(p,q):
    p=trim(p)
    while len(p)>=len(q):
        z=p[-1]/q[-1]; k=len(p)-len(q)
        for j,c in enumerate(q): p[j+k]-=z*c
        p=trim(p)
    return p
def gcd(p,q):
    while q: p,q=q,remainder(p,q)
    return [x/p[-1] for x in p]
def squarefree(coeffs):
    return gcd(list(map(Fraction,coeffs)),[Fraction(i*coeffs[i]) for i in range(1,len(coeffs))])==[Fraction(1)]
checks['boundary_seventeen_squarefree']=squarefree(coeffs)
q5=[2,3,2,9,-2,4]
checks['line_five_points_squarefree']=squarefree(q5)
checks['line_shared_point_excluded']=sum(c*((-1)**i) for i,c in enumerate(q5))==-14
# Normal row identity gives the common smoothing direction at all five nodes.
r,s=var(0),var(1)
qpoly=add(scale(power(r,5),4),scale(mul(power(r,4),s),-2),scale(mul(power(r,3),power(s,2)),9),scale(mul(power(r,2),power(s,3)),2),scale(mul(r,power(s,4)),3),scale(power(s,5),2))
F1=scale(mul(mul(r,add(r,s)),add(r,scale(s,2))),-1)
G1=add(scale(power(r,3),-4),scale(mul(power(r,2),s),2),scale(mul(r,power(s,2)),-9),scale(power(s,3),-1))
checks['five_nodes_same_smoothing_direction']=scale(mul(G1,power(r,3)),-1)==add(mul(r,qpoly),mul(F1,power(s,3)))
checks['genus_budget']=12+5-1==16 and 12+23-3+1==33
if not all(checks.values()): raise AssertionError(checks)
out={'scope':'Finite actual-source identities and squarefree polynomials only; projective schemes checked separately by M2.','passed':sum(checks.values()),'total':len(checks),'checks':checks,'boundary_E_coefficients_ascending_u_degree':coeffs,'line_E_intersection_coefficients_ascending_r_degree_s_equals_1':q5,'moving_line_stratum':'a*b=1','fixed_line_stratum':'a=b=1','local_five_node_smoothing_direction':'da+db','genus_E':12,'genus_smooth_residual':16,'C_E_points':17,'C_L_points':1,'L_E_points':5}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(f'{out["passed"]}/{out["total"]} exact polynomial/budget checks: PASS')
print(path.name)
```
</details>


### Archived certificate: `research/computations/verify_split22_boundary_survivor.py`

Original finite calculation preserved verbatim. Its scope remains as stated in the script; it is not a global sextic existence assertion.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Verify the missed content-free d=1,[2,2] first-normal boundary in P-041.

This is only a first-normal incidence certificate.  It does not construct an
integral sextic, a mate, or an STCI presentation.
"""

import sympy as sp


z, s, t = sp.symbols("z s t")

# Linear factors ell=p*xi+r*eta and m=u*xi+v*eta.
p = sp.Integer(1)
r = sp.Rational(3, 2) * z
u = 1 - 3 * z**4 + z**8
v = z / 2 - z**5 / 2 + z**9 / 2

# Evaluation at the quadric direction q1=xi+z*eta/2 is obtained by
# substituting [xi:eta]=[-z/2:1].
assert sp.expand(-p * z / 2 + r) == z
assert sp.expand(-u * z / 2 + v) == z**5

alpha = sp.expand(p * u)
beta = sp.expand(p * v + r * u)
gamma = sp.expand(r * v)

assert alpha == z**8 - 3 * z**4 + 1
assert beta == 2 * z**9 - 5 * z**5 + 2 * z
assert gamma == sp.Rational(3, 4) * (z**10 - z**6 + z**2)


def coefficient(polynomial, degree):
    return sp.Poly(polynomial, z).coeff_monomial(z**degree)


a = [coefficient(alpha, index) for index in range(11)]
b = [coefficient(beta, index) for index in range(11)]
c = [coefficient(gamma, index) for index in range(11)]

# The eleven exact equations for the image of the sextic quadratic-normal map.
equations = [
    -a[9] + 2 * b[10],
    -b[0] + 2 * c[1],
    a[0] - 2 * b[1] + 4 * c[2],
    -3 * a[1] + 2 * b[2] + 4 * c[3],
    a[2] - 2 * b[3] + 4 * c[4],
    a[3] - 2 * b[4] + 4 * c[5],
    -a[4] + 4 * c[6],
    a[5] - 2 * b[6] + 4 * c[7],
    a[6] - 2 * b[7] + 4 * c[8],
    -a[7] - 2 * b[8] + 12 * c[9],
    a[8] - 2 * b[9] + 4 * c[10],
]
assert all(sp.expand(equation) == 0 for equation in equations)

# Homogenize each coefficient pair to its common degree and check that neither
# factor has vertical content on P1.
low_left = s
low_right = sp.Rational(3, 2) * t
high_left = s**9 - 3 * s**5 * t**4 + s * t**8
high_right = (s**8 * t - s**4 * t**5 + t**9) / 2

assert sp.gcd(sp.Poly(low_left, s, t), sp.Poly(low_right, s, t)).total_degree() == 0
assert sp.gcd(sp.Poly(high_left, s, t), sp.Poly(high_right, s, t)).total_degree() == 0

print("PASS: content-free d=1,[2,2] first-normal boundary survivor is exact")
```
</details>


### Archived certificate: `research/computations/verify_split22_finite_reduction.py`

Original finite calculation preserved verbatim. Its scope remains as stated in the script; it is not a global sextic existence assertion.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Exact higher-jet finite reduction for the two-ramified [2,2] family.

Characteristic zero, C0, and the reduced/content-free/no-vertical assumptions
of P-020. Mathematical normal-sheaf arguments are in the companion note.
This certificate does not claim a global STCI exclusion of the surviving
h=-1/2 line, and never cancels mate scale in a local class group.
"""
import sympy as s

x0,x1,x2,x3,z,e,W,a,lam = s.symbols('x0 x1 x2 x3 z e W a lam')
u0,u2,u3,u5,u6,u8,beta = s.symbols('u0 u2 u3 u5 u6 u8 beta')
h=a+s.Rational(1,2)
c=3*a*a+2*a+1
q=x0*x3-x1*x2
A=x0*x0*x2-x1**3
B=x0*x2*x2-x1*x1*x3
D=x2**3-x1*x3*x3
S=(u0*x0*x0+u3*x0*x2-(2*h+1)**2/(2*(2*h-1))*x0*x3
   +u2*x1*x1+(2*h+1)/2*(u5*x1*x3+u6*x2*x2)+2*h*u8*x3*x3)
K=u0*x1*A+u2*x2*A+u3*x3*A+u5*x2*B+u6*x3*B+u8*x2*D
F=a*B*B+q*q*S+a*q*K+lam*q**3
f=s.cancel(F.subs({x0:1,x1:z,x2:z**3+e,x3:z**4+e*((1-a)*z+W)})/e**2).expand()
fp=s.Poly(f,e,W)
coef=lambda i,j:s.factor(fp.coeff_monomial(e**i*W**j))
R=a*(u0+u2*z*z+u3*z**3+u5*z**5+u6*z**6+u8*z**8)-2*(a+1)*z**4
betaval=a*lam-(a+1)*(a*a+1)/a
G=u2-a*u3*z+beta*z*z+(a*a+a+1)*u5*z**3-a*(a+2)*u6*z**4+c*u8*z**6
assert s.cancel(coef(0,1)+z*R)==0
assert s.cancel(coef(1,0)+a*a*z*G.subs(beta,betaval))==0
assert s.cancel(coef(0,2)-(R+z**4)/a)==0
L=(a*u2-a*(2*a+1)*u3*z+(-a*a+3*a*beta+2*a+5)*z*z
   +3*a*a*(a+1)*u5*z**3-a*(3*a*a+4*a+2)*u6*z**4
   +a*(9*a*a+6*a-1)*u8*z**6)
H=a-a*a*u5*z+2*a**3*u6*z*z+2*a*a*(a**3-a*a-a-1)*u8*z**4
assert s.cancel(coef(1,1)-L.subs(beta,betaval))==0
assert s.cancel(coef(2,0)-H)==0
assert s.cancel(coef(3,0)+a*a*u8*z)==0

# Quadratic endpoint germs and order-one Jacobian components, without lambda.
quad=lambda form:s.expand(sum(co*z**i*e**j*W**k for (i,j,k),co in s.Poly(form,z,e,W).terms() if i+j+k<=2))
assert s.factor(s.det(s.hessian(quad(f),(z,e,W))))==-2*a**3*u0*u0
assert s.expand(coef(0,1)).coeff(z,1)==-a*u0
cinf=(3*h-s.Rational(1,2))/(2*h)
fi=s.cancel(F.subs({x3:1,x2:z,x1:z**3+e,x0:z**4+e*(cinf*z+W)})/e**2).expand()
assert s.factor(s.det(s.hessian(quad(fi),(z,e,W))))==-2*a**3*u8*u8
assert s.factor(s.diff(fi,W).subs({e:0,W:0}).coeff(z,1))==a*u8
print('PASS: exact Jacobian components and both forced A1 endpoint germs')

# Nonzero G: coefficient comparison forces G|R and the even parameter stratum.
N,T,y=s.symbols('N T y')
P=c*c*(-2*(a+1)+T*(a+2)*c*c/(2*a+1)**2)/(a**3*(3*a+2))
be=a*a*(3*a+2)*P/c
V6=T*c*c/(a*(2*a+1)**2)
ss={u0:N*N*P/a,u2:N*P,u3:0,u5:0,u6:V6/N,u8:T/(N*N),beta:be}
Q=N+a*z*z/c
assert s.cancel(R.subs(ss)-Q*G.subs(ss))==0
Gy=P+be*y-a*(a+2)*V6*y*y+c*T*y**3
Qy=1+a*y/c
Ly=a*P+(-a*a+3*a*be+2*a+5)*y-a*(3*a*a+4*a+2)*V6*y*y+a*(9*a*a+6*a-1)*T*y**3
Hy=a+2*a**3*V6*y+2*a*a*(a**3-a*a-a-1)*T*y*y
By=a**3*y*y-a*a*Qy*Ly+Qy*Qy*Hy
Dy=4*y*y/a*Hy-Ly*Ly
Br=s.factor(s.rem(By,Gy,y))
nums=lambda poly:[s.factor(s.together(s.Poly(poly,y).coeff_monomial(y**i)).as_numer_denom()[0]) for i in range(3)]
gb=s.groebner(nums(Br),T,a)
assert gb.reduce(a*T)[1]==0 and gb.reduce(2*a*a+a)[1]==0
print('PASS: every squarefree G stratum has an interior A1 and is excluded')

# No interior A1 is permitted by the remaining defect budget 2/5.
# For cubic Gy, Gy | Br*(Gy')^2 is necessary also at multiple roots.
Gn=s.together(Gy).as_numer_denom()[0]
Bn=s.together(Br).as_numer_denom()[0]
rr=s.rem(Bn*s.diff(Gn,y)**2,Gn,y)
unitfactors=[a,2*a+1,3*a+2,c,T]
def remove_units(poly,extras=()):
    return s.prod(p**m for p,m in s.factor_list(poly)[1] if p not in unitfactors+list(extras))
ns=[remove_units(n) for n in nums(rr)]
gn=s.groebner(ns,T,a)
S1=3*a**4+8*a**3+40*a*a+36*a+9
S2=8*a**4-6*a**3+33*a*a+36*a+9
S3=2*a**7+15*a**6+48*a**5+39*a**4+2*a**3-3*a*a+4*a+1
elim=a*a*(a+1)**4*(2*a+1)**11*(3*a+2)**2*S1*S2*S3
assert s.Poly(gn.polys[-1].as_expr(),a).monic()==s.Poly(elim,a).monic()
linear=next(p.as_expr() for p in gn.polys if s.Poly(p,T).degree()==1)
assert s.factor(s.diff(linear,T)).as_poly(a).monic()==s.Poly((a+1)**2*(2*a+1)**7*(3*a+2),a).monic()
print('PASS: no-node eliminant leaves a=-1 and three finite algebraic strata')

def field(poly,modulus):
    n,d=s.together(poly).as_numer_denom()
    n=s.rem(n,modulus,a);d=s.rem(d,modulus,a)
    return s.rem(n*s.invert(d,modulus,a),modulus,a)
def field_value(poly,ts,Y,modulus):
    result=0
    for coefficient in s.Poly(poly,y).all_coeffs():
        result=field(result*Y+field(coefficient.subs(T,ts),modulus),modulus)
    return result

# S1 is the triple-root cubic stratum. Its two interior points are A5.
ts1=6*(16*a**5+48*a**4+56*a**3+32*a*a+9*a+1)/(99*a**7+420*a**6+701*a**5+694*a**4+441*a**3+184*a*a+47*a+6)
y1=field((a+2)*c/(3*(2*a+1)**2),S1)
assert field(linear.subs(T,ts1),S1)==0
for polynomial in ns:
    assert field(polynomial.subs(T,ts1),S1)==0
for derivative in range(3):
    assert field_value(s.diff(Gy,y,derivative),ts1,y1,S1)==0
for poly in [Qy,By,Dy,y]:
    assert s.gcd(field_value(poly,ts1,y1,S1),S1)==1
assert field_value(s.diff(Gy,y,3),ts1,y1,S1)!=0
# The transverse Hessian is invertible; nonzero B gives Morse order6,
# hence A5. The low curve has class3 and defect 3^2/6=3/2.
assert s.Rational(3*3,6)>s.Rational(2,5)
print('PASS: S1 triple collisions are A5 with excessive normal defect')

# S2 is double-root; S3 violates u0 !=0. Assert exact specialized ideals too.
ts2=-(48944*a**3-40956*a*a+375576*a+181341)/2593080
ts3=(992*a**6-16558*a**5-160219*a**4-582979*a**3-530441*a*a+26491*a+216662)/354294
for modulus,ts in [(S2,ts2),(S3,ts3)]:
    for n in ns: assert field(n.subs(T,ts),modulus)==0
    assert field(linear.subs(T,ts),modulus)==0
cs=[field(s.Poly(Gy,y).nth(i).subs(T,ts2),S2) for i in range(4)]
y2=field((9*cs[3]*cs[0]-cs[2]*cs[1])/(2*(cs[2]**2-3*cs[3]*cs[1])),S2)
assert field_value(Gy,ts2,y2,S2)==0
assert field_value(s.diff(Gy,y),ts2,y2,S2)==0
for poly in [Qy,By,Dy,y,s.diff(Gy,y,2)]:
    assert s.gcd(field_value(poly,ts2,y2,S2),S2)==1
assert field(P.subs(T,ts3),S3)==0
assert s.Rational(2*2,4)>s.Rational(2,5)
print('PASS: S2 double collisions are A3; S3 has forbidden endpoint content')

# The chart a=-2/3 has not been divided away.
U=s.symbols('U');aa=-s.Rational(2,3)
ge=U-s.Rational(2,3)*y*y+s.Rational(1,18)*y**3
qe=1-s.Rational(2,3)*y
le=(a*u2+(-a*a+3*a*beta+2*a+5)*z*z-a*(3*a*a+4*a+2)*u6*z**4+a*(9*a*a+6*a-1)*u8*z**6).subs({a:aa,u2:U,beta:0,u6:-s.Rational(3,4),u8:s.Rational(1,18),z:s.sqrt(y)}).expand()
he=H.subs({a:aa,u5:0,u6:-s.Rational(3,4),u8:s.Rational(1,18),z:s.sqrt(y)}).expand()
bre=s.rem(aa**3*y*y-aa*aa*qe*le+qe*qe*he,ge,y)
ne=nums(s.rem(bre*s.diff(ge,y)**2,ge,y))
assert s.gcd(s.gcd(ne[0],ne[1]),ne[2])==1
print('PASS: the exceptional a=-2/3 stratum has no node-free member')

# G=0 is a genuinely separate stratum, with delta10 rather than delta8.
# c=0 forces u2=u3=u5=u6=beta=0; H depends linearly on z4.
fld=lambda expr:field(expr,c)
V=s.symbols('V')
rz=a*u0-2*(a+1)*z**4+a*V*z**8
lz=(-a*a+2*a+5)*z*z+a*V*(9*a*a+6*a-1)*z**6
hz=a+2*a*a*V*(a**3-a*a-a-1)*z**4
jz=-a*a*V*z
vv=fld(-1/(2*a*(a**3-a*a-a-1)))
uv=fld((2*(a+1)-a*vv)/a)
k=fld(s.diff(rz,z).subs({z:1,V:vv,u0:uv}))
psi3=fld(jz.subs({z:1,V:vv})+lz.subs({z:1,V:vv})*s.diff(hz,z).subs({z:1,V:vv})/k)
assert fld(vv-(-3*a-s.Rational(11,4)))==0
assert fld(uv-(s.Rational(3,4)-3*a))==0
assert fld(psi3-(10*a+11)/84)==0 and s.gcd(psi3,c)==1
vd=(a+1)/a
hv=fld(hz.subs({z:1,V:vd}))
dv=fld(4/a*hv-lz.subs({z:1,V:vd})**2)
assert s.gcd(hv,c)==1 and s.gcd(dv,c)==1
# Simple collisions: 8 A1 or 4 A1+4 A2. Double collisions: 4 A3 class2.
for defect in [s.Integer(4),4*s.Rational(1,2)+4*s.Rational(1,3),s.Integer(4)]:
    assert defect!=s.Rational(12,5)
print('PASS: the omitted G=0 stratum is excluded by A1/A2/A3 defects')

# The remaining conductor-sensitive line, without a global STCI assertion.
sm={a:-1,u0:-16*T,u2:16*T,u3:0,u5:0,u6:-4*T,u8:T,beta:-8*T,lam:8*T}
assert s.expand(G.subs(sm)-2*T*(z*z-2)**2*(z*z+2))==0
assert s.expand(R.subs(sm)+T*(z*z-2)**3*(z*z+2))==0
assert s.expand((F.subs(sm)).coeff(T,0)+B*B)==0
print('PASS: every surviving both-ramified carrier is on the h=-1/2 line')
print('BOUNDARY: extra conductor and higher jets on that line remain unresolved')
```
</details>


## Consolidated historical supplement: `research/supplements/ENDPOINT_FOUR_ACTUAL_SEXTICS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Endpoint-four sextic constructions

Full historical mathematical content retained with original scope and limitations.

---

# Actual sextics on the retained endpoint-four chart

Started 2026-10-25; completed 2026-10-26. Status: exact new linear realization, independently reproduced fixed-carrier jet certificate, and independently audited local scope bridge.

## Scope and accepted inputs

The curve is the fixed characteristic-zero quartic
\(C=[s^4:s^3t:st^3:t^4]\). The family construction starts in the conditional degree-\((6,16)\) lane with full generic ordinary initial CI \((2,12)\), saturated actual first relation, and movement two. [STCI-R-0014](../results/movement_two_six_rows.md) makes it a necessary numerical row under those hypotheses; it does not assert existence. The final fixed-carrier corollary is stated separately and does not require those initial-ideal or saturation hypotheses.

The [October 21 conductor/chart independent review](CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-conductor-and-chart-independent-review), section 6, retains the endpoint-four root chart with

\[
\begin{aligned}
a(z)&=a_0+2b_2z+z^2,\\
b(z)&=b_1z+b_2z^2,\\
c(z)&=(b_1/2-a_0/4)z^2,\\
f&=a(z)u^2+b(z)uv+c(z)v^2,\qquad a_0\ne0.
\end{aligned}
\]

Its normalization is \(4f(-z/2,1)=z^4\). On the retained integral-nodal open its actual Picard modulus is

\[
\rho=2b_1/a_0-1,\qquad \rho^{12}=1,\quad\rho\ne1.
\]

The root and torsion reductions are reviewed evidence. They are not an emptiness result. The [saved sextic symbol computation](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2-the-exact-global-k-linear-symbol-map) supplies the actual source \(H^0(I_C^2(6))\), its rank-22 second-symbol image, and the one-dimensional kernel \(kq^3\). Those accepted computations are used as premises, not rerun here.

The exact balanced normal frame is

\[
(x_0,x_1,x_2,x_3)
=(1,z,z^3+v,z^4+u+\tfrac32zv).
\]

All coefficients below are global constants. No free \(k(C)\)-coefficients are introduced into the homogeneous source.

## Every prescribed second symbol has an actual sextic lift

Put

\[
q=x_0x_3-x_1x_2,\qquad D=x_2^3-x_1x_3^2.
\]

The multiplier forced by this endpoint chart is proportional to \(z^8\); fix its nonzero scalar by requiring the target second symbol to be \(z^8f\). The complete affine family of actual sextics with this target is

\[
\boxed{
F_6=(2b_1-a_0)q^2x_3^2+(b_1-a_0)qDx_2
       -b_2qDx_3+\tfrac14D^2+\kappa q^3.
}
\]

Here \(a_0,b_1,b_2,\kappa\) are parameters over \(\mathbf Q\); the nodal/torsion open is imposed afterward. The affine freedom in \(\kappa\) is precisely the accepted kernel. This is a complete description of the second-symbol lifting problem on the stated target, rather than a selection of examples.

To reconstruct the formula, solve four new right-hand sides in the saved image matrix. In the target order \(P_0,\ldots,P_{10},Q_0,\ldots,Q_{10},R_0,\ldots,R_{10}\), the nonzero entries are

\[
P_8=a_0,\quad P_9=2b_2,\quad P_{10}=1,
\quad Q_9=b_1,\quad Q_{10}=b_2,
\quad R_{10}=b_1/2-a_0/4.
\]

The resulting ambient source combinations are

| Parameter block | Actual sextic |
| --- | --- |
| \(a_0\) | \(-q^2x_3^2-qDx_2\) |
| \(b_1\) | \(2q^2x_3^2+qDx_2\) |
| \(b_2\) | \(-qDx_3\) |
| constant | \(D^2/4\) |
| \(\kappa\) | \(q^3\) |

A direct polynomial substitution independently checks the answer. In the balanced frame,

\[
q_1=u+zv/2,\qquad D_1=-2z^5u.
\]

Using these first symbols in the displayed sextic gives exactly \(z^8f\). The verifier additionally checks that the zeroth and first normal symbols vanish and that every ambient block has homogeneous degree six. It saves the full normal expansion, including all higher terms, for subsequent mate calculations.

This establishes actual sextic realizability of the prescribed **second symbol**. It does not establish compatibility with a prescribed higher formal root correction, membership in every earlier ambient-obstruction incidence, integrality of every member, or existence of \(G_{16}\).

## The normalization \(a_0=1\) uses the actual torus

Projective root scaling alone cannot set \(a_0=1\), because the coefficient of \(z^2\) has already been fixed. There is, however, a valid ambient normalization. The actual \(C\)-preserving torus is

\[
T_\lambda=\operatorname{diag}(1,\lambda,\lambda^3,\lambda^4).
\]

It gives \(q\mapsto\lambda^4q\), \(D\mapsto\lambda^9D\), and

\[
\lambda^{-18}F_6(T_\lambda x)
=F_6(\lambda^{-2}a_0,\lambda^{-2}b_1,
       \lambda^{-1}b_2,\lambda^{-6}\kappa).
\]

After the finite étale square-root cover \(\lambda^2=a_0\), one obtains \(a_0=1\) without changing the \(D^2/4\) coefficient or the endpoint normalization. The invariant modulus is \(\rho\). The remaining \(\mu_2\) changes the sign of the normalized \(b_2\) and fixes \(\kappa\). Equivalently, the squared normalized parameter is \(b_2^2/a_0\), and the normalized kernel parameter is \(\kappa/a_0^3\).

Thus subsequent exact computations may work over cyclotomic fields with
\(b_1=(\rho+1)/2\), but must record this cover. The universal formula above retains \(a_0\) free and needs no extension field.

## An additional geometric flag: a triple line on the carrier

Let \(L_0=V(x_2,x_3)\). Since \(q\in I_{L_0}\) and \(D\in I_{L_0}^2\), every sextic in the family vanishes to order at least three on \(L_0\). The generic order is exactly three when \(\kappa\ne0\), because the other four parameter blocks have order four. When \(\kappa=0\), the retained torsion chart has generic order exactly four: the quartic normal coefficient of \(x_1^2x_2^2x_3^2\) is

\[
3b_1-2a_0=a_0(3\rho-1)/2,
\]

which cannot vanish for a root of unity \(\rho\) with \(a_0\ne0\).

This is a singular line on the sextic carrier. It is not automatically a component of the intersection with a proposed mate. The line meets \(C\) only at \([1:0:0:0]\), with pullback ideal \((z^3,z^4)\). If a mate has sole support \(C\), its restriction to \(L_0\) must consequently be a nonzero scalar times \(x_1^{16}\); an identically zero restriction would make \(L_0\) a residual component. This provides a separate necessary global condition, not a completed family exclusion.

For another useful algebraic form, put \(L=(b_1-a_0)x_2-b_2x_3\). Then

\[
F_6=(D/2+qL)^2
 +q^2\bigl((2b_1-a_0)x_3^2-L^2+\kappa q\bigr).
\]

This identity may help future normalization or conductor calculations. No normality claim is inferred from it.

## One selected carrier: a completed necessary jet exclusion

The current investigation tests only

\[
\rho=-1,\quad a_0=1,\quad b_1=b_2=0,\quad\kappa=1,
\]

so

\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3.
\]

Any actual \(G_{16}\) in the scoped full generic initial-\((2,12)\) problem must satisfy

\[
G_{16}\in(F_*)+(u,v)^{12}
\quad\text{over }\mathbf Q(z)[[u,v]].
\]

This is only a necessary condition. Its coefficient space is nevertheless finite: all 969 coefficients of a homogeneous degree-sixteen form remain constants. The 286 forms \(F_*H_{10}\) satisfy it and cannot be proper mates.

The [fixed-carrier M2 certificate](../computations/endpoint4_fixed_m2_2026_10_25.m2) evaluates the actual normal substitution at \(z=1,\ldots,30\) modulo the prime 65521. At each point it uses

\[
\mathbf F_{65521}[u,v]/(F_*|_z,(u,v)^{12}),
\]

a 23-dimensional quotient. It stacks the resulting \(23\times969\) constant-coefficient matrices. The final \(690\times969\) matrix has rank 683. It also independently constructs the coefficient matrix of all 286 degree-ten multiples of \(F_*\), verifies their rank 286, and verifies that the stacked matrix annihilates them.

The modular rank gives a characteristic-zero lower bound, not merely a numerical heuristic. Every sample has \(z\ne0\) and \(1+z^2\ne0\) modulo the prime. The \(u^2\) leading coefficient of the carrier's quadratic normal part is \(z^8(1+z^2)\). Formal normal division through degree eleven can therefore be performed with denominators that are units at the chosen prime; a universal rational remainder matrix specializes to the tested finite-field matrix. Equivalently, in the 78-dimensional truncated polynomial module, multiplication by the nonzero order-two carrier on polynomials of degree at most nine has constant rank 55, leaving a free rank-23 quotient over the local coefficient DVR. The modular target thus has the required good reduction.

It follows that the characteristic-zero necessary jet kernel has dimension at most \(969-683=286\). The known multiples already have dimension 286, so

\[
\boxed{
\{G_{16}:G_{16}\in(F_*)+(u,v)^{12}\}
=F_*H^0(\mathbf P^3,\mathcal O(10)).
}
\]

The equality persists under characteristic-zero coefficient-field extension. This first excludes a proper degree-sixteen mate in the scoped full generic initial-\((2,12)\) problem. The following independently audited local argument gives a stronger fixed-carrier conclusion without that initial-ideal assumption.

## Every proper degree-sixteen pair on this carrier has residual degree at least eight

The [nonsplit-node scope audit](BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md#2026-10-26-endpoint4-nonsplit-node-scope-audit) independently reconstructs the needed local lemma. The generic quadratic normal term of \(F_*\) is

\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\]

Its discriminant square class \(1+z^2\) remains nonsquare in \(k(z)\) after any characteristic-zero extension of the constant field: its geometric zeros are simple. Over \(k(z)(\sqrt{1+z^2})\), the completed curve has two transverse smooth branches exchanged by the quadratic Galois action. A function defined over \(k(z)\) has the same finite vanishing order \(n\) on each branch. The generic intersection length is therefore \(2n\), and division by the prepared quadratic gives

\[
G\in(F_*)+(u,v)^n.
\]

For clarity, the membership follows by writing the prepared remainder as \(a(v)u+b(v)\). Subtracting its restrictions to the two branches, whose difference has order one in \(v\), gives \(\operatorname{ord}a\ge n-1\); then \(\operatorname{ord}b\ge n\). This uses actual conjugate branches and finite intersection length, not just the two initial normal symbols.

If a proper homogeneous degree-sixteen pair \((F_*,G)\) containing \(C\) had \(n\ge12\), the completed jet-kernel certificate would force the global form \(G\) to be a multiple of \(F_*\), contradicting properness. Thus every such pair has

\[
\boxed{m_C=2n\le22,\qquad
\deg\bigl([V(F_*,G)]-m_C[C]\bigr)=96-8n\ge8.}
\]

This fixed-carrier conclusion does not require a prescribed full generic initial CI, a saturated first relation, or the movement-two hypothesis. Those assumptions explain where the carrier came from. The conclusion requires the actual displayed \(F_*\), mate degree sixteen, properness, and characteristic zero. It makes no assertion that the bound is attained. It does not exclude the endpoint-four chart for other \(b_2,\kappa,\rho\), the endpoint-three chart, the orbit-collision chart, other movement rows, or unrestricted STCI presentations.

## Reproduction and review record

Run

```text
python3 research/computations/endpoint4_actual_2026_10_25.py
python3 research/computations/endpoint4_fixed_m2_2026_10_25.py
python3 research/computations/endpoint4_fixed_jet_independent_2026_10_26.py
```

The first script records the inherited matrix hash, solves only the new right-hand sides, and performs a direct ambient substitution. The generated [JSON](../computations/endpoint4_actual_2026_10_25.json) includes full ambient and normal expansions, parameter conventions, and the torus action. The exporter also produces an M2 family presentation; its successful load adds no further mathematical test.

Independent `endpoint4_formula_audit` reconstructed the second symbol, torus normalization, and exact singular-line orders without rerunning the inherited rank proof. It corrected the initial overly cautious normalization warning: the actual torus does supply the square-root gauge.

The fixed-carrier wrapper saves a [PASS metadata record](../computations/endpoint4_fixed_m2_2026_10_25.json) and [complete M2 output](../computations/endpoint4_fixed_m2_2026_10_25.txt), including source hashes, all sample ranks, the actual degree-six carrier vector, the 969 exponent-column order, and all 286 known-multiple checks. A preliminary M2 implementation failed those checks because an unparenthesized multiline assignment omitted the last two carrier terms. That failure was diagnosed and corrected before the final PASS. Ambient reconstruction and explicit annihilation checks now prevent that mistake from being hidden by the reported rank.

The [independent normal-division script](../computations/endpoint4_fixed_jet_independent_2026_10_26.py) uses recursive normal-degree division in a fixed 23-element basis, followed by separate modular elimination, rather than the M2 quotient Gröbner basis. Its [JSON record](../computations/endpoint4_fixed_jet_independent_2026_10_26.json) independently reports rank 683 and annihilation of all 286 actual multiples at every sample. The nonsplit-node implication is reviewed in the linked scope audit. No result is changed here.

The independent replay uses Python's standard library and a C++17 compiler, selecting clang++ or g++ from the environment. Its temporary rank executable is built outside the repository and removed after the run. Macaulay2 provides the other implementation.



## Consolidated historical supplement: `research/supplements/SPLIT_SEXTIC_AND_MULTIPLICITY_SIX_RESTRICTIONS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Split sextic geometry and multiplicity-six restrictions

This chapter retains exact structural restrictions for two different questions concerning the fixed characteristic-zero embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\): an integral sextic whose quadratic normal cone splits into two reduced content-free sections, with an arbitrary-degree hypothetical mate; and a degree-\((4,6)\) supported pair with generic curvilinear length six. They share saturated multiplicity and actual normal-source mechanisms, but their necessary data are not identified without proof.

The all-quartic-carrier theorem already excludes a characteristic-zero \((4,6)\) STCI. The seven-type calculation remains useful multiple-curve algebra; it is not a surviving actual degree-pair case. The split-sextic statements concern their exact carrier hypotheses and possible other mate degrees, not all sextic carriers. No unrestricted STCI conclusion follows.

Except for the explicitly characteristic-free singleton-normalization lemma and final local control, the split-carrier numerical and projection arguments below retain their characteristic-zero scope. The conormal splitting, divisions by two, actual source ranks and characteristic-zero geometric arguments are not silently transferred to characteristic two or three. The fixed curve does have a [quartic-carrier STCI in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier), which is a separate construction.

The [saturated Gorenstein pairing proof](MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-pairing-audit) supplies the rank-six duality input; [the full primitive-triple obstruction](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#primitive-triples-on-smooth-rational-quartics) is the stated exclusion input used in the last section. The exact first-normal source space is preserved below with its chosen balanced frame.

## A normalization obstruction for an integral thick sextic

<a id="p-019"></a>

There is a complementary obstruction for one integral thick carrier.  Let an
integral degree-\(a\) surface \(X\ne Q\) have generic normal order \(\mu\) along
\(C\).  Restricting to \(Q\) gives an effective residual class

\[
 (a,a)-\mu(1,3)=(a-\mu,a-3\mu),
\]

so \(a\ge3\mu\).  A thick sextic therefore has \(\mu=2\). This normalization obstruction works in every algebraically closed characteristic: the effective quadric restriction, normalization multiplicity formula (including residue-field degrees), projection formula and Cartier intersection integrality require neither separability nor balanced normal splitting.

Let \(\nu:S=X^\nu\to X\) be the normalization, write the components of
\((\nu^{-1}C)_{\mathrm{red}}\) as \(\Gamma_i\), and put
\(\delta_i=[k(\Gamma_i):k(C)]\).  At the generic point of \(C\), the
one-dimensional hypersurface local ring has multiplicity \(\mu\).  The
normalization multiplicity formula gives

\[
 \mu=\sum_i s_i\delta_i,
\]

with positive integers \(s_i\).  Hence for a sextic
\(\sum_i\delta_i\le2\).

Suppose the reduced inverse image is one irreducible Cartier curve \(\Gamma\)
of degree \(\delta\) over \(C\), and suppose a degree-\(b\) mate exists.
Pulling its Cartier divisor to the normalization gives

\[
 q\Gamma\sim b\widetilde H
\]

for some \(q>0\), where \(\widetilde H=\nu^*O_X(1)\).  Projection formula
gives

\[
 \widetilde H^2=a,\qquad \widetilde H\Gamma=4\delta.
\]

Intersecting the displayed equivalence first with \(\widetilde H\) and then
with \(\Gamma\) yields

\[
 \boxed{\Gamma^2=\frac{16\delta^2}{a}.}
\]

For \(a=6\), the multiplicity formula permits only \(\delta=1,2\), giving
\(8/3\) or \(32/3\).  This contradicts integrality of the self-intersection of
a Cartier curve.  Thus a thick sextic in a defining pair can survive this
argument only if the normalized preimage splits into two degree-one branches,
or its irreducible preimage is non-Cartier.  Those are genuine gaps: the
split-branch intersection equations have consistent integral numerical
solutions, so one cannot silently assume equal branch multiplicities or
iterate the same fractionality argument.

### P-020: the split-sextic branch has only two extreme numerical types

Let

\[
 \pi:B=\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3,
 \qquad E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

and use the bidegree convention in which

\[
 H|_E=\mathcal O_E(4,0),\qquad
 \mathcal O_E(E)=\mathcal O_E(7,-1).
\]

An integral sextic of exact normal order two has strict transform
\(D\sim6H-2E\), and hence

\[
 D|_E\sim(10,2).
\]

Assume this divisor is the reduced sum of two distinct integral, content-free
sections, with no vertical component:

\[
 Z_1\sim(d,1),\qquad Z_2\sim(10-d,1).
\]

After exchanging them, take \(0\le d\le5\).  The no-vertical hypothesis makes
the blowdown of the normalized strict transform quasi-finite over the sextic;
the two curves \(\Gamma_i\) above \(Z_i\) are therefore exactly the two
divisorial branches over \(C\).  If a degree-\(b\) mate exists, its pullback to
the normalization has divisor

\[
 bH\sim m_1\Gamma_1+m_2\Gamma_2,
 \qquad m_1,m_2>0.
\]

This equality is an equality of Weil divisors with Cartier left side.  It may
be intersected with the Cartier divisors \(H\) and \(E\), even when the
individual branches are not Cartier.  The ambient blowup intersections are

\[
 H^2D=6,\qquad HED=8,
\]

and

\[
 H\Gamma_i=4,\qquad
 E\Gamma_1=7-d,\qquad E\Gamma_2=d-3.
\]

Consequently

\[
 m_1+m_2=\frac{3b}{2},
\]

\[
 (7-d)m_1+(d-3)m_2=8b.
\]

Put \(\Delta=m_1-m_2\).  Eliminating \(m_2\) gives

\[
 \Delta(5-d)=5b,
 \qquad
 \frac{m_2}{b}=\frac{5-3d}{4(5-d)}.
\]

The case \(d=5\) is impossible, and positivity of \(m_2\) leaves only

\[
 \boxed{d=0,\quad(m_1,m_2,b)=k(5,1,4)}
\]

or

\[
 \boxed{d=1,\quad(m_1,m_2,b)=k(11,1,8)}.
\]

This is a finite reduction, not yet an unconditional exclusion.  It becomes
an exclusion if the two branches are Cartier on the normalization.  Writing
\(z=\Gamma_1\Gamma_2\), one then has

\[
 \Gamma_1^2=7-d-z,\qquad
 \Gamma_2^2=d-3-z.
\]

Intersecting the mate divisor with each branch forces respectively

\[
 d=0:\quad z=\frac{19}{4},
 \qquad
 d=1:\quad z=\frac{17}{5},
\]

both impossible for Cartier-curve intersection numbers, which are integers also on the normal surface.  In particular, if
the first strict transform is smooth at the ten collision points, its branch
intersection is the ordinary value

\[
 Z_1Z_2=10,
\]

and the contradiction is immediate.

The qualification is essential.  On the normal local surface

\[
 xy=e^n,
\]

the two components of \((e=0)\) meet with Mumford intersection \(1/n\), not
one.  Thus normality alone does **not** imply \(z=10\); isolated local
class-group corrections are exactly the remaining split-sextic escape route.
The two forced values above quantify those corrections.  In transverse
\(A_{r-1}\) models they require total differents \(21/4\) and \(33/5\),
respectively.



### P-022: the actual thick-sextic first-normal image

For any characteristic-zero smooth rational quartic, the quadratic
first-normal map is

\[
 H^0(I_C^{(2)}(6))\longrightarrow
 H^0\bigl(C,\operatorname{Sym}^2N_C^*\otimes O_C(6)\bigr).
\]

P-017 gives a 23-dimensional source.  Its kernel is exactly
\(H^0(I_C^{(3)}(6))=kq^3\): restriction to the unique quadric would otherwise
give a section of \(O_Q(3,-3)\).  Thus its image \(W\) has dimension 22.
If \(U\) is the seven-dimensional first-normal image of cubics through \(C\),
then

\[
 W=\langle U\cdot U\rangle.
\]

For \(C_0\), in the balanced frame

\[
 z=x_1/x_0,\qquad a=x_2-z^3,\qquad b=x_3-z^4,
 \qquad \xi=b-\tfrac32za,\quad\eta=a,
\]

an exact row reduction gives eleven independent linear equations cutting out
\(W\subset H^0(O(10))^3\).  Writing a normal quadratic as

\[
 \alpha(z)\xi^2+\beta(z)\xi\eta+\gamma(z)\eta^2,
\]

the equations are

\[
\begin{aligned}
-\alpha_9+2\beta_{10}&=0,&-\beta_0+2\gamma_1&=0,\\
\alpha_0-2\beta_1+4\gamma_2&=0,
&-3\alpha_1+2\beta_2+4\gamma_3&=0,\\
\alpha_2-2\beta_3+4\gamma_4&=0,
&\alpha_3-2\beta_4+4\gamma_5&=0,\\
-\alpha_4+4\gamma_6&=0,
&\alpha_5-2\beta_6+4\gamma_7&=0,\\
\alpha_6-2\beta_7+4\gamma_8&=0,
&-\alpha_7-2\beta_8+12\gamma_9&=0,\\
\alpha_8-2\beta_9+4\gamma_{10}&=0.
\end{aligned}
\]

Solving them produces primitive split
quadratics

\[
 (p\xi+r\eta)(u\xi+v\eta)
\]

of every type \((d,1)+(10-d,1)\), \(0\le d\le5\).  Therefore the actual
ambient image, and not merely the complete space of normal quadratics, permits
all split types.

Exact affine representatives \((p,r),(u,v)\) for the two factors are:

\[
\begin{array}{c|c|c}
d&(p,r)&(u,v)\\\hline
0&(1,0)&(-z^{10}-2,-z)\\
1&(1,z)&(2+6z+2z^8,z+z^2+z^9)\\
2&(1,z^2)&(2+4z+24z^7,z+2z^2+z^5+2z^6+4z^7+12z^8)\\
3&(1,z^3)&(8-2z+8z^3+24z^5+8z^6,4z-3z^2+4z^6+4z^7)\\
4&(1,z^4)&(4+2z+12z^4+4z^5,2z+3z^2+2z^5+2z^6)\\
5&(z^5,1)&(-z^5,1).
\end{array}
\]

This also falsifies a tempting inference.  A square discriminant on the
exceptional divisor forces the *normal divisor* to split, but not the ambient
sextic.  Exact integral examples are

\[
 (A+x_3q)(A-x_3q)+q^3
\]

and

\[
 (A+x_3q)(2A+D)+q^3.
\]

The second has smooth first strict transform at all collisions of its two
normal sections.  Thus any later argument must use the mate, higher normal
coefficients, or normalization intersection theory; first-normal
factorization alone is insufficient.



### P-023: Hodge exclusion for squarefree split-sextic residuals

Retain the split/no-vertical hypotheses of P-020 and let \(S\) be the
normalization of the strict transform of the sextic.  Work on a resolution
\(\widetilde S\), using Mumford numerical pullbacks for the two branch curves.
Write

\[
 K_0=2H-E.
\]

This is the pullback of the adjunction class cut by the unique quadric; it
must not be silently identified with the canonical divisor of a singular
normalization or of its resolution.  The ambient intersections are

\[
 H^2=6,\quad HE=8,\quad E^2=4,
 \quad HK_0=4,\quad K_0^2=-4.
\]

For the low-degree branch \(\Gamma\) of type \((d,1)\), P-020 gives

\[
 K_0\Gamma=d+1,\qquad
 \Gamma^2=\begin{cases}9/4&d=0,\\13/5&d=1.\end{cases}
\]

Put

\[
 L=H+K_0,\qquad
 T=\Gamma^\#+\frac{d+1}{4}K_0,
\]

where \(\Gamma^\#\) is the numerical pullback.  Then \(L^2=10\),
\(LK_0=TK_0=0\), and equality holds in Hodge index:

\[
 (LT)^2=L^2T^2.
\]

Consequently

\[
 T\equiv\tfrac12L\quad(d=0),\qquad
 T\equiv\tfrac35L\quad(d=1).
\]

If the residual binary quartic is squarefree, the quadric section of \(K_0\)
is a sum of four pairwise-disjoint reduced ruling lines \(R_j\).  Each \(R_j\)
is Cartier on the normal surface, even if it passes through a singular point:
locally it is the only component of the reduced Cartier divisor through that
point.  Moreover

\[
 HR_j=1,\qquad K_0R_j=-1,\qquad LR_j=0.
\]

Intersecting the numerical proportionality with \(R_j\) yields

\[
 \Gamma R_j=\frac{d+1}{4},
\]

equal to \(1/4\) or \(1/2\), contrary to integrality of intersection with the
Cartier curve \(R_j\).  Hence neither surviving split type can have a
squarefree residual quartic.  This proof was independently audited for signs
and for the use of Hodge index on a resolution.  What remains is precisely the
highly non-squarefree residual locus; squarefreeness does not follow merely
from a reduced, content-free split first-normal divisor.

For \(C_0\), exact next-jet calculations are consistent with this boundary.
For every \(d=0\) factor, imposing both first-normal divisibility and vanishing
of the next normal coefficient makes the collision polynomial have affine
degree at most five and forces a square factor in the residual binary quartic.
A large \(d=1\) chart has the same behavior.  The full projective space of
\((1,1)\)-factors has not been eliminated.



### P-030: residual-root multiplicities in the split sextic cases

Assume the split/no-vertical hypotheses of P-020 and P-023.  Let
\(K_i\) be the full Cartier cluster lying over a distinct root of the residual
binary quartic, including its root multiplicity and every exceptional
component required by resolution, and let that multiplicity be \(\mu_i\).
The four total units satisfy \(\sum_i\mu_i=4\).

With \(K_0=2H-E\), the intersection identities on the resolved normalization
are

\[
 H\cdot K_i=\mu_i,\qquad E\cdot K_i=3\mu_i,\qquad
 K_0\cdot K_i=-\mu_i,\qquad L\cdot K_i=0.
\]

The same Hodge-index equality used in P-023, now applied to the full cluster
rather than to a reduced branch, forces the low-degree normalization branch
to meet \(K_i\) in

\[
 \Gamma_{\mathrm{low}}\cdot K_i=
 \begin{cases}
   \mu_i/4,&d=0,\\
   \mu_i/2,&d=1.
 \end{cases}
\]

The cluster \(K_i\) is the full Cartier divisor pulled back from the normalization, so it is orthogonal to every exceptional curve. Thus \(\Gamma_{\mathrm{low}}^\#\cdot K_i\) equals the intersection of the integral strict transform with that integral Cartier pullback, and is an integer. This does not assert that the rational numerical pullback \(\Gamma_{\mathrm{low}}^\#\) is integral or Cartier downstairs.  In the
\(d=0\) case every \(\mu_i\) is divisible by four, so the only partition is
\([4]\).  In the \(d=1\) case every \(\mu_i\) is even, leaving only
\([4]\) and \([2,2]\).  The conclusion concerns full Cartier clusters; it
must not be applied to only the reduced visible branch over a multiple root.

This removes the squarefree residual case already excluded in P-023 and all
partitions except the three displayed possibilities.  It does not yet exclude
the surviving multiple-root configurations.



## Clean split conductor: a branch exclusion and its stronger global model

<a id="p-027"></a>

This argument has two distinct scopes. Let \(X\subset\mathbf P^3_{\mathbf C}\)
be an integral sextic, generically nodal along the smooth rational quartic
\(C\), with smooth normalization \(\nu:S\to X\). Suppose the inverse image
of \(C\) consists of two branches \(\Gamma_1,\Gamma_2\), each mapping
isomorphically to \(C\), and
\[
 I_CO_S=O_S(-\Gamma_1-\Gamma_2).
\]
Assume the source conductor divisor is
\(\Delta=\Gamma_1+\Gamma_2+\Delta'\), with \(\Delta'\) disjoint from
both branches. Retain the reduced/content-free split first-normal divisor
\((d,1)+(10-d,1)\), with no vertical component, from the preceding
split-carrier calculation. These are sufficient for the branch exclusion.
Global invariants stated below additionally require \(\Delta'=0\).

The [source double-point/finite-duality formula of Kleiman–Lipman–Ulrich](https://www.math.purdue.edu/~jlipman/papers/2-point.pdf), applied to the finite normalization map into the smooth threefold, gives
\[
 K_S+\Delta=2H.
\]
Because \(\Delta'\) is disjoint from each branch, intersecting with
\(\Gamma_i\) and comparing smooth adjunction
\((K_S+\Gamma_i)\Gamma_i=-2\), with \(H\Gamma_i=4\), gives
\[
 \Gamma_1\Gamma_2=10.
\]
The clean ideal makes the lifted blowup divisor exactly
\(E=\Gamma_1+\Gamma_2\) on \(S\); the split first-normal degrees give
\(E\Gamma_1=7-d\) and \(E\Gamma_2=d-3\). Hence
\[
 \Gamma_1^2=-d-3,\qquad \Gamma_2^2=d-13.
\]
If a degree-\(b\) mate exists, then
\(bH\sim m_1\Gamma_1+m_2\Gamma_2\), with positive integral \(m_i\).
Intersecting with \(H\) gives \(m_1+m_2=3b/2\). Intersecting with the two
branches gives
\[
 4b=-(d+3)m_1+10m_2,
 \qquad4b=10m_1+(d-13)m_2.
\]
Eliminating \(m_i\) forces
\[
 d^2-10d-35=0,
\]
which has no integral solution \(0\le d\le5\). Equivalently, the forced
ratio is \(m_1/b=(9\pm\sqrt{15})/12\), not rational. Thus even additional
conductor components disjoint from the two branches do not rescue this
branch-intersection model.

For the stronger global numerical model, assume the **entire** source
conductor divisor is \(\Gamma_1+\Gamma_2\). Then
\(K_S+\Gamma_1+\Gamma_2=2H\) globally. The target conductor is exactly
\(I_C\): the pullback ideal is the source conductor, so \(I_C\) is
contained in the target conductor; conversely a conductor function vanishes
at the generic point of the integral reduced curve \(C\), and therefore
belongs to its prime ideal. The conductor square consequently gives
\[
 0\longrightarrow O_X\longrightarrow\nu_*O_S
 \longrightarrow O_C(-Z)\longrightarrow0,
 \qquad\operatorname{length}Z=10.
\]
Indeed, the two rational branches meet in the length-ten subscheme \(Z\).
Their union has structure sheaf consisting of pairs of branch functions
agreeing on \(Z\); modulo the diagonal \(O_C\), this is \(O_C(-Z)\).
Since \(\chi(O_X)=11\) for a sextic hypersurface,
\(\chi(O_C(-Z))=-9\), so \(\chi(O_S)=2\). Finite duality identifies
\(\nu_*\omega_S=I_C\otimes\omega_X=I_C(2)\). The quartic has its unique
containing quadric, so \(p_g(S)=h^0(I_C(2))=1\), and then \(q(S)=0\).
Finally
\[
 K_S^2=4H^2-4H(\Gamma_1+\Gamma_2)+(\Gamma_1+\Gamma_2)^2=-4,
 \qquad c_2(S)=12\chi(O_S)-K_S^2=28.
\]
These are the classical ordinary-sextic numbers. In the ordinary model the
degree-twenty discriminant has twenty pinch points, so its double conductor
cover is connected of genus nine and cannot be the two split rational
branches. That comparison uses the ordinary-model hypotheses.

The global numbers do not follow merely from absence of additional conductor
*meeting* the branches: disjoint extra conductor can change them. The branch
exclusion has the weaker disjointness scope proved above; the numerical
identities have the entire-conductor scope. Singular normalization, extra
conductor meeting a branch, or a finite-length factor in \(I_CO_S\) are genuine
escapes from this clean calculation. Nothing here excludes every integral
sextic carrier or constructs an STCI mate.

### P-041: torsion-corrected sharpening of the surviving split sextics

Retain the split, reduced, content-free, no-vertical hypotheses of P-020,
P-023, and P-030.  The only residual binary-quartic root partitions are
\([4]\) for \(d=0\), and \([4]\) or \([2,2]\) for \(d=1\).  Over an
algebraically closed characteristic-zero field every such quartic is a square.
Writing \(h\) for the equation of \(C\) on its unique quadric \(Q=(q=0)\),

\[
 F|_Q=h^2P_2^2=(hP_2)^2.
\]

The bidegree-\((3,3)\) form \(hP_2\) lifts to a cubic
\(T\in I_C(3)\).  Hence \(F-T^2=qK\) for a quartic \(K\), and locally
\((I_C^2:q)=I_C\) gives

\[
 \boxed{F=T^2+qK,\qquad T\in I_C(3),\quad K\in I_C(4).}
\]

Every residual root selected by the low first-normal branch is also met by
the high branch.  On the exceptional divisor the first strict transform has
equation \(\ell m=0\), so its differential vanishes along the exceptional
tangent directions at such a point.  On the strict transform of \(Q\), the
residual root has multiplicity at least two, so the differential vanishes
along those tangent directions as well.  These two divisors are transverse in
the smooth blowup; consequently the first strict transform is singular at
every selected residual-root point.

The mate relations must retain their common scale \(k>0\).  They imply

\[
\begin{array}{c|c|c}
d&(m_{\mathrm{low}},m_{\mathrm{high}},b)&
\text{Cartier multiple forced by the mate}\\\hline
0&k(5,1,4)&4k\Gamma_{\mathrm{low}},\\
1&k(11,1,8)&10k\Gamma_{\mathrm{low}}.
\end{array}
\]

One cannot cancel \(k\): local class groups may have torsion.  In an
independently established ordinary \(A_{\mu-1}\) model
\(xy=t^\mu\), a low branch of contact \(\alpha\) represents
\(\alpha\in\mathbb Z/\mu\), has local Mumford intersection
\(\alpha^2/\mu\), and contributes correction
\(\alpha(\mu-\alpha)/\mu\).  Thus a two-simple \(d=1,[4]\) allocation with
ordinary \(A_3\) germs forces only \(k\) even; it is not unconditionally
excluded.  This corrects the invalid stronger inference from
\(10k[\Gamma]=0\) to \(10[\Gamma]=0\).

There is one further exact exclusion for \(C_0\).  At a totally ramified
ruling, normalize \(d=1,[4]\) so the low factor restricts to \(z^2\).
In the balanced frame its global form is

\[
 (p_0-2z)\xi+\frac{p_0z}{2}\eta.
\]

Content freedom of this low section requires \(p_0\ne0\). Write the high factor as

\[
 u(z)\xi+\left(z^{10}+\frac z2u(z)\right)\eta.
\]

The eleven exact first-normal image equations force \(u_9=-2\) and
\(u_0=u_3=u_6=0\).  In particular both high coefficients are divisible by
\(z\), creating forbidden vertical content.  Coordinate reversal gives the
same conclusion at the other totally ramified ruling.  The general
\(d=0,[4]\), non-totally-ramified \(d=1,[4]\), and \(d=1,[2,2]\) loci remain
open.  The last locus genuinely contains a missed projective boundary at
first-normal order.  In the balanced frame with quadric direction
\(q_1=\xi+z\eta/2\), the content-free factors

\[
 \ell=\xi+\frac32z\eta,
 \qquad
 m=(1-3z^4+z^8)\xi+
   \left(\frac z2-\frac{z^5}{2}+\frac{z^9}{2}\right)\eta
\]

have evaluations \(z\) and \(z^5\) on \(q_1\).  Their product therefore has
the required boundary evaluation \(z^6\), homogeneously \(s^6t^6\), and its
quadratic coefficients

\[
 \alpha=z^8-3z^4+1,\qquad
 \beta=2z^9-5z^5+2z,\qquad
 \gamma=\frac34(z^{10}-z^6+z^2)
\]

satisfy all eleven P-022 image equations.  This is an exact, content-free
first-normal survivor, not an ambient integral sextic or an STCI pair.  It
shows why the \([2,2]\) boundary must remain in the search.  Unsaved
higher-jet samples supply only computational evidence.



### P-042: the necessary multiplicity-six types for a mixed \((4,6)\) pair

Let \(k\) be algebraically closed of characteristic zero and suppose
\(X=V(F_4,G_6)\) is supported set-theoretically on \(C_0\).  The forms have no
common surface factor, so \(X\) is a degree-24 lci curve of generic length six
over \(C_0\).  By P-011 the quartic has normal order one at the generic point.
In the completed transverse regular local ring it can therefore be taken as
one parameter; modulo it the other equation is a unit times the sixth power of
the remaining parameter.  Thus \(X\) is quasiprimitive.

Write the Bănică--Forster pieces as \(E_i=L^i(D_i)\), with \(D_1=0\).  For a
quasiprimitive multiplicity-six lci, the Gorenstein multiplication pairings

\[
 E_i\otimes E_{5-i}\longrightarrow E_5
\]

are isomorphisms.  The natural multiplication maps encode the inequalities
\(D_i+D_j\le D_{i+j}\).  The pairings give
\(D_4=D_5=D_2+D_3\), while \(2D_2\le D_4\) gives
\(0\le D_2\le D_3\).  The pieces therefore have the necessary form

\[
 O_C,\quad L,\quad L^2(D_2),\quad L^3(D_3),\quad
 L^4(D_2+D_3),\quad L^5(D_2+D_3).
\]

Put \(l=\deg L\) and \(d_i=\deg D_i\).  Since \(C_0\simeq\mathbf P^1\),
additivity of Euler characteristic gives

\[
 \chi(O_X)=6+15l+3(d_2+d_3).
\]

A \((4,6)\) complete intersection has

\[
 p_a(X)=1+\frac{24(4+6-4)}2=73,
 \qquad \chi(O_X)=-72,
\]

and hence

\[
 \boxed{5l+d_2+d_3=-26.}
\]

The first piece is a line-bundle quotient
\(O_{\mathbf P^1}(-7)^2\twoheadrightarrow L\), so \(l\ge-7\); effectivity
and the displayed equation give \(l\le-6\).  The eight raw numerical types are

\[
\begin{array}{c|c}
l&(d_2,d_3)\\\hline
-7&(0,9),(1,8),(2,7),(3,6),(4,5),\\
-6&(0,4),(1,3),(2,2).
\end{array}
\]

When \((l,d_2)=(-7,0)\), the canonical multiplicity-three member of the
filtration has pieces \(O,L,L^2\) and is a global primitive triple of type
\(O(-7)\), contrary to P-010.  Exactly seven necessary numerical types remain.
No existence or compatibility among these numerical candidates is asserted.

Finally, the quotient \(O(-7)^2\twoheadrightarrow O(l)\) is represented by a
basepoint-free pair of sections of degree

\[
 e=l+7\in\{0,1\}.
\]

This is precisely the horizontal degree in P-031.  In the nonregular branch,
P-031 gives \(1\le p\le8-e\), \(c=9-e-p\), and \(\deg Z=p+8\).  Therefore
only \(8+7=15\) of the former 36 coarse pole-divisor strata remain.  The seven
Bănică--Forster numerical types and the fifteen pole strata record different
necessary data; no unproved correspondence between them is being assumed.


## Further actual lifts and surviving limits

The [fixed ramified boundary and its larger chart](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split-sextic) construct actual sextic lifts and prove the all-mate exclusion for the specified fixed normal form; this does not exclude every first-normal survivor. The [nonramified quadruple-root and additional two-double-root charts](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split4-nonramified) retain the actual local models and their restrictions. In particular the first-normal boundary example above is a control of source compatibility, not an actual integral carrier or mate.

The numerical seven types in the final section are a coarse stage. The [corrected first-normal Fitting divisor and pole comparison](MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mixed46-poles) gives the stronger exact divisor relation \(A=D_3+\min(D_2,D_3-D_2)\) under its hypotheses. The distinction between that refined evidence, the earlier fifteen coarse pole strata, and actual realization must be retained. No uniform correspondence or realized configuration is inferred from the tables.


## A local control for the regular-ratio hypothesis

For any field and integer \(m\ge2\), in \(k[[t,u,v]]\) take
\(F=tu+v^m\), \(G=u\). Their ideal is exactly \((u,v^m)\), a
complete intersection with radical \((u,v)\), and the quotient is free of
rank \(m\) over \(k[[t]]\). Thus transverse length is constant even at
\(t=0\). The first-normal forms are \(tu\) and \(u\), with rational
quotient \(1/t\). Proper local complete intersection and constant length
therefore do not imply a regular quotient, and do not justify subtracting a
global multiple of one equation from the other. This formal local control
asserts no projective realization with prescribed degrees.


## Further higher-jet reduction

The [full two totally ramified-root reduction](SPLIT_SEXTIC_TWO_RAMIFIED_ROOTS.md) treats the entire stated two-root family, including the zero-polynomial stratum, and leaves an explicit one-parameter carrier line. It is distinct from the preceding first-normal and numerical restrictions.

## Consolidation review

Independent review reconstructed all preserved P019/P020/P022/P023/P027/P030/P041/P042 arguments, source coverage and characteristic boundaries, including the entire-conductor qualification for global invariants. The separate full two-ramified-root reduction was also independently reconstructed and accepted. The bounded proof clarifications in this account
were checked against the original arguments; no material preservation finding
remains. The claims retain their stated hypotheses.



## Consolidated historical supplement: `research/supplements/SPLIT_SEXTIC_TWO_RAMIFIED_ROOTS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Two totally ramified residual roots: a full higher-jet reduction

## Result and scope

Work over an algebraically closed field of characteristic zero on

\[
 C_0=[s^4:s^3t:st^3:t^4].
\]

Retain P-020's **integral carrier, reduced/content-free split first-normal
exceptional divisor, and no vertical component** hypotheses. Consider
only the `d=1,[2,2]` family whose two residual ruling roots are the totally
ramified rulings. The two low evaluation zeros are at their preimages.
This is the complete family parameterized in
[the full split-sextic family](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split-sextic), not merely its fixed specimen.

**Proved necessary reduction.** If a carrier in this entire family has an
STCI mate of any degree, its low-factor parameter must be

\[
 \boxed{h=-\tfrac12.}
\]

Up to the diagonal automorphisms of `C0`, and up to multiplying the carrier
by a nonzero scalar, the remaining carriers have the one-parameter form

\[
\begin{aligned}
 F_\tau={}&-B^2+\tau q\mathcal K,\qquad \tau\ne0,\\
 \mathcal K={}&q(-16x_0^2+16x_1^2-x_3^2)
 +16x_1A-16x_2A+4x_3B-x_2D+8q^2,
\end{aligned}
\]

where
\[
q=x_0x_3-x_1x_2,\quad A=x_0^2x_2-x_1^3,\quad
B=x_0x_2^2-x_1^2x_3,\quad D=x_2^3-x_1x_3^2.
\] No STCI mate is constructed,
and this line is not excluded. Its possible extra conductor and further
normalization data must remain in the frontier. The other `[2,2]` root
configurations and the surviving `[4]` families are outside this theorem.

**Exact certificate:**
`research/computations/verify_split22_finite_reduction.py`.
Run with `python3` in this checkout. The full
certificate passed on 2026-10-06. The new normal-sheaf argument is in
[numerical pullback and the normal line](../synthesis/numerical_surface_pullback.md); root independently audited that proof.
The complete proof, exact source coverage and retained computational dependencies were independently reconstructed and accepted in this consolidation.

## Exact local state and the global Jacobian zero divisor

Put

\[
 a=h-\tfrac12,\quad c=3a^2+2a+1,
 \quad a\ne0,\quad 2a+1\ne0,\quad u_0u_8\ne0.
\]

The last conditions are the existing content-free endpoint conditions;
`2a+1=2h`. In the finite blowup chart set

\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+e,\quad
 x_3=z^4+e((1-a)z+W).
\]

The low section is `e=W=0`. Let `f=F/e^2` be the strict-transform equation.
The ambient carrier `F`, including all its `lambda q^3` lifts, is the exact
one in the [complete larger-family parameterization](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#exact-parameterization-of-the-larger-two-ramified-root-boundary). Define

\[
\begin{aligned}
 R={}&a(u_0+u_2z^2+u_3z^3+u_5z^5+u_6z^6+u_8z^8)
             -2(a+1)z^4,\\
 G={}&u_2-au_3z+\beta z^2+(a^2+a+1)u_5z^3
             -a(a+2)u_6z^4+cu_8z^6,\\
 \beta={}&a\lambda-\frac{(a+1)(a^2+1)}a.
\end{aligned}
\]

Exact expansion gives the two Jacobian components along the low section:

\[
 f_W=-zR,\qquad f_e=-a^2zG.
\]

Also `f(z,0,W)=u(z)W^2-zRW`, with
`u(z)=(R+z^4)/a`. Thus the section is regular generically on the integral
strict surface, independently of whether another nonnormal curve meets it
at finitely many points. The local normal-sheaf theorem therefore applies.

The finite endpoint Hessian determinant is `-2a^3u0^2`; the reversed
endpoint determinant is `-2a^3u8^2`. Both are nonzero. At the finite
endpoint `fW=-a u0 z+...`; at the reversed endpoint the corresponding
component is `a u8 z+...`. Each endpoint is an `A1` germ with Jacobian
common order exactly one. All other base points are covered by the finite
chart with `z!=0`, so the exact global zero-divisor length is

\[
 \boxed{\delta=2+\deg\gcd(R,G).}                         \tag{1}
\]

This formula includes `G=0`, when `gcd(R,0)=R` and `delta=10`. Treating a
zero polynomial as though it had a degree-six bound would be incorrect.
That separate case is closed below.

The ambient normal extension has determinant degree eight and its
Jacobian target degree twelve. Consequently

\[
 \deg N_{\Gamma/D}=\delta-4.
\]

P-020/P-023 force `Gamma#^2=13/5` for an STCI mate. The exact normal-sheaf
defect formula therefore gives

\[
 \operatorname{Def}(\Gamma)=\delta-4-13/5.
\]

Both endpoints contribute `1/2` to this defect, so `delta>=8`.
This uses numerical intersections, where cancelling the positive integer
mate scale is legitimate. No scale is cancelled in a local class group,
and no Cartier index bound is inferred by cancelling it.

## Nonzero G: exact division and the very small remaining defect budget

Suppose first that `G!=0`. Equation (1) gives `delta<=8`; hence

\[
 \delta=8,\qquad \deg G=6,\qquad G\mid R.
\]

In particular `c!=0`. Write

\[
 R=(N+az^2/c)G.
\]

The quotient's linear coefficient is zero by the coefficient of `z^7`.
Its constant coefficient is nonzero because `R(0)=a u0!=0`. Then `u2!=0`.
The coefficient of `z` forces `u3=0`. The coefficients of `z^3,z^5`
together force `u5=0`, without deleting any exceptional root of
`a^2+a+1`. The remaining equations are

\[
\begin{aligned}
 u_0&=Nu_2/a,\\
 u_6&=\frac{Nc^2u_8}{a(2a+1)^2},\\
 \beta&=\frac{a^2(3a+2)u_2}{Nc},\\
 \frac{a^3(3a+2)u_2}{Nc^2}
 -\frac{N^2(a+2)c^2u_8}{(2a+1)^2}&=-2(a+1).
\end{aligned}                                                   \tag{2}
\]

All divisions in (2) are by previously established nonzero quantities.
The factor `3a+2` is **not** divided out here.

The diagonal automorphism `z -> t z` acts, after normalizing the residual
evaluation, by `Rnew=t^-4 R(tz)` and `Gnew=t^-2 G(tz)`. It sends
`N -> N/t^2`. Since the base field is algebraically closed and `N!=0`,
we may take `N=1`. Put `tau=N^2u8`; equivalently one may use the invariant
coordinate `y=z^2/N` before the normalization.

The total defect is `7/5`. The two endpoints consume one, leaving

\[
 \boxed{\operatorname{Def}_{\rm interior}=2/5.}             \tag{3}
\]

A single interior `A1` on the smooth low curve would contribute `1/2`,
contradicting (3). This excludes every carrier with even one such node;
no assumption about the other singular points is required.

## The cubic and its Hessian remainder

For `3a+2!=0`, solve (2) by

\[
\begin{aligned}
 P&=\frac{c^2[-2(a+1)+\tau(a+2)c^2/(2a+1)^2]}{a^3(3a+2)},\\
 b&=\frac{a^2(3a+2)P}{c},\qquad
 V_6=\frac{\tau c^2}{a(2a+1)^2}.
\end{aligned}
\]

Here `u2=P`, `u0=P/a`, `u6=V6`, `u8=tau`, and `beta=b` after taking `N=1`.
In particular `P!=0`, `tau!=0`. Define the cubic

\[
 H_3(y)=P+by-a(a+2)V_6y^2+c\tau y^3,
 \qquad Q(y)=1+ay/c.
\]

The next two exact coefficients of `f` are

\[
\begin{aligned}
 L(y)={}&aP+(-a^2+3ab+2a+5)y
       -a(3a^2+4a+2)V_6y^2+a(9a^2+6a-1)\tau y^3,\\
 H_2(y)={}&a+2a^3V_6y+2a^2(a^3-a^2-a-1)\tau y^2.
\end{aligned}
\]

Set

\[
 B_2=a^3y^2-a^2QL+Q^2H_2,
 \qquad D_2=4y^2H_2/a-L^2.
\]

At a simple root of `G(z)=H3(z^2)`, differentiation **before** imposing
the collision equation gives

\[
 \det\operatorname{Hess}_{z,e,W}(f)
       =-2z^2(G'(z))^2 B_2(z^2).
\]

Thus every simple root with `B2!=0` is `A1`. Let `Brem` be the remainder
of `B2` modulo `H3`. When `H3` is squarefree, absence of nodes would force
all three remainder coefficients to vanish. Their exact Groebner basis
contains `a tau` and `2a^2+a`, impossible on the content-free domain.
So every mate-compatible cubic must have a repeated root.

For arbitrary cubic `H3`, a necessary condition for no simple-root node is

\[
 \boxed{H_3\mid B_{\rm rem}(H_3')^2.}                    \tag{4}
\]

At a double root the squared derivative already supplies multiplicity two;
at a triple root it supplies at least three. At a simple root it is a
unit, so (4) is exactly the needed vanishing there. Therefore (4) does
not impose an unjustified condition at a repeated root.

Clear denominators in (4) and remove only known invertible factors.
Exact elimination gives, up to those invertible factors,

\[
 (a+1)^4 S_1(a)S_2(a)S_3(a)=0,
\]

where

\[
\begin{aligned}
 S_1&=3a^4+8a^3+40a^2+36a+9,\\
 S_2&=8a^4-6a^3+33a^2+36a+9,\\
 S_3&=2a^7+15a^6+48a^5+39a^4+2a^3-3a^2+4a+1.
\end{aligned}
\]

The exact univariate Groebner element is proportional to
`a^2(a+1)^4(2a+1)^11(3a+2)^2 S1 S2 S3`.
A linear-in-`tau` Groebner element has leading coefficient proportional to
`(a+1)^2(2a+1)^7(3a+2)`. Consequently, away from `a=-1` and forbidden
values, these are finite parameter strata. The certificate preserves these
polynomials and checks every exceptional stratum, rather than interpreting
a generic sample as a complete elimination.

## Closing all three finite strata and the divided parameter value

On `S1=0`, the cubic has a triple root

\[
 y_0=(a+2)c/[3(2a+1)^2],
\]

and `tau` is the rational expression checked in the certificate. The
values `y0,Q(y0),D2(y0),B2(y0)` are all units in `Q[a]/(S1)`.
There are therefore two interior collisions, each with collision order
and Jacobian order three. The nonzero transverse determinant allows a
formal Morse elimination of `(e,W)`; its residual leading coefficient is
a nonzero multiple of `B2`, and its order is six. The germ is `A5`.

The curve index is also controlled, not inferred solely from the
singularity's name. The Morse critical section has `(e,W)=O(t^3)`, where
`t=z-z0`. Along the original smooth low curve, both Morse coordinates have
order at least three and their product has order six with nonzero leading
coefficient. Their orders are thus exactly three. The local `A5` class is
three, and the normal-sheaf defect is `3^2/6=3/2`, already exceeding (3).

On `S2=0`, exact elimination gives

\[
 \tau=-\frac{48944a^3-40956a^2+375576a+181341}{2593080}.
\]

The cubic has one double root and one simple root. The double-root value
`y0` and `Q,D2,B2,H3''` there are units modulo `S2`. The same argument
with order two gives an `A3` germ of low-curve class two and normal defect
`2^2/4=1`, again impossible. The certificate verifies these unit statements
by exact reduction and gcd, including all algebraic roots of `S2`.

On `S3=0`, the exact corresponding `tau` value makes `P=0` identically in
`Q[a]/(S3)`. It gives `u0=0`, violating endpoint content-freeness.

The exceptional chart `a=-2/3` in (2) has

\[
 \tau=1/18,\quad u_6=-3/4,\quad \beta=0,\quad u_2=U\ne0,
 \qquad H_3=U-2y^2/3+y^3/18.
\]

For its version of (4), the three remainder numerators have polynomial
gcd one in `Q[U]`. This chart has no node-free member and is excluded.

## Closing the identically-zero G stratum

If `G=0`, content-freeness forces `c=0`, and the other coefficients force

\[
 u_2=u_3=u_5=u_6=\beta=0.
\]

Indeed `c=0` has no common root with any of the other coefficient factors
`a,a^2+a+1,a+2`; no exceptional coefficient vanishing has been suppressed.
Now `delta=10`, and the allowed interior defect is `12/5`.
Put `r=z^4`. Then

\[
 R=a u_0-2(a+1)r+a u_8r^2,
\]

while the coefficient of `e^2` along the low curve is

\[
 H_2(z)=a+2a^2u_8(a^3-a^2-a-1)z^4.
\]

There are only the following possibilities.

- If the quadratic in `r` has distinct roots and `H2` is nonzero at both,
  all eight interior points are `A1`. Their defect is four.
- `H2`, being linear in `r` with nonzero constant, can vanish at only one
  of the two distinct roots. Scale that four-point cluster to `z=1`.
  Reduction modulo `c=0` then gives
  `u8=-3a-11/4`, `u0=3/4-3a`. The transverse `(z,W)` Hessian is invertible;
  the residual cubic coefficient is `(10a+11)/84`, a unit modulo `c`.
  These four germs are `A2`. The low curve has class one: the Morse
  parameter is `e`, which vanishes identically on the curve, so it is one
  of the coordinate branches. The other four germs are `A1`.
  Total interior normal defect is `4/3+2=10/3`.
- If the quadratic has a double root, scale it to `z=1`, obtaining
  `u0=u8=(a+1)/a`. Both `H2` and the transverse Hessian determinant are
  units modulo `c`. The residual Morse order is four, giving four `A3`
  germs of low-curve class two. Their total defect is four.

None equals `12/5`. This closes the case that a degree-six bound on a
nonzero polynomial would have missed.

The defects used here are the **normal-sheaf defects** `i^2/n` for the
smooth low curve of class `i<=n/2` in `A_(n-1)`. They are not the
numerical-pullback self-intersection corrections `i(n-i)/n`. In this scope
one can obtain the former by subtracting the latter from the local
Jacobian/conormal length `i`; the exact defect formula in the companion
normal-sheaf note provides the global bookkeeping.

## Surviving line and continuation requirements

The sole remaining value is `a=-1`, equivalently `h=-1/2`. In the normalized
chart,

\[
\begin{aligned}
 u_0&=-16\tau,&u_2&=16\tau,&u_6&=-4\tau,&u_8&=\tau,\\
 \beta&=-8\tau,&\lambda&=8\tau,
\end{aligned}
\]

and

\[
 G=2\tau(z^2-2)^2(z^2+2),\qquad
 R=-\tau(z^2-2)^3(z^2+2).
\]

This is the displayed carrier `Ftau=-B^2+tau q K`. At the two simple
collisions `z^2=-2`, finite exact scratch Morse calculations made the
residual vanish through degree six for all `tau`; this suggested an extra
conductor locus and was a reason to stop short of a global exclusion.
That finite-jet observation is **not** a proof of an identically vanishing
Morse residual or a completed normalization calculation, and is not used
in the theorem above.

The next mathematical move is to compute the normalization/conductor and
actual numerical branch intersections of this line, with all exceptional
`tau` values preserved. The other two collision points have `z^2=2`,
collision order three and Jacobian order two, so the clean ordinary-node
argument does not apply. Integral-carrier existence, global mate descent,
and radical support still require their own checks. The global conductor
loophole must not be replaced by a tangent-form or class-group shortcut.

## Provenance and failed reductions preserved

The fixed specimen was already excluded in the 2026-10-05 note by actual
higher jets. The present work used that family's **entire exact ambient
lift fiber**, the newly proved normal-sheaf defect inequality, and polynomial
elimination. It did not extrapolate from the fixed specimen.

The first attempted universal `degree G<=6` inference overlooked `G=0`.
That oversight was caught during the resumed 2026-10-06 audit; the companion
normal-sheaf note was amended with the explicit `G!=0` qualification, and
this certificate closes the omitted stratum independently. A further
false shortcut would identify normal-sheaf defects with inverse-Cartan
self-intersection corrections; the different values are recorded above.

The nonramified `[4]` certificate also required two resultant-sign repairs:
`Res(P-2z,1+(P/2-2)z)=-(P-2)^2/2`, and the finite-root `[2,2]` analogue
is `-(P-2)(P-2t)/2`. The repaired verifier now passes all its image, content,
selected `A3`, and symbolic ambient-lift checks. Its mathematical content
conditions were unchanged.

The [preceding split-carrier account](SPLIT_SEXTIC_AND_MULTIPLICITY_SIX_RESTRICTIONS.md) supplies the complete numerical prerequisites. This reduction concerns only the stated totally ramified two-root family.

## Consolidation review

Independent review checked the complete source proof and its computation support, including the zero-polynomial stratum, exceptional parameter values and the exact surviving carrier line. No material mathematical preservation finding remains. The carrier line is not a constructed STCI pair, and the other split-root configurations retain their own scope.

