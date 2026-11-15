# Weight components and normal filtrations

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

**Standing hypotheses.** Throughout this focused development, let \(k\) be an algebraically closed field of **characteristic zero**, and fix the smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). Write \(\mathcal I=\mathcal I_C\) and \(E=\mathcal I/\mathcal I^2\). In particular, the transverse infinitesimal normal-direction matrix has determinant \(-4\ne0\), and the balanced conormal splitting \(E\cong\mathcal O_{\mathbf P^1}(-7)^{\oplus2}\) used below is characteristic-zero; neither assertion is made in characteristic two. Statements about other characteristics require their separately stated hypotheses.\n\n## II. Equations and filtrations

### Weight components and actual symbols

Use weights on polynomial monomials given by substitution
\(x_i\mapsto\lambda^{w_i}x_i\), with \(w=(0,1,3,4)\). Write
\(F=\sum_\alpha F_\alpha\), \(G=\sum_\beta G_\beta\).
A degree-\(d\), weight-\(\ell\) monomial \(x^e\) restricts on the
\(x_0=1\) torus chart to \(r^\ell u^{e_2}v^{e_3}\) and on \(C\) to
\(s^{4d-\ell}t^\ell\) in homogeneous parameters. This identifies the
weight grading with one coordinate of the parametrization bigrading.
Every weight component of a form through \(C\) lies in \(P\).
[Actual weight-wise equation spaces](../../arguments/torus_embedded_quotients.md#actual-equations-and-the-ci-criterion).

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
components of minimum normal order. [Normal symbols and actual source images](../../arguments/quartic_specialization_and_symbols.md#4-which-symmetric-algebra-sections-come-from-quartics).

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
calculation](../../arguments/normal-geometry/formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant) ·
[Strict transforms and vertical cycles](../residual-construction/two_surfaces.md#22-the-common-graph-and-its-two-contractions).

Further excess divisors can arise from saturation of the **full** normal
relation modules. For example, in the sole-supported lci setting with
full generic initial ideal a coprime binary CI of degrees \(2\le r<s\), a first
relation with image \(L(-D)\) in its saturated line \(L\) has a
quotient-relation resultant with divisor supported on \(D\).
This comparison uses the actual relations and their generation
lengths. [Statement and hypotheses](../../results/nonsaturated_first_relation_resultant.md#statement-and-hypotheses) ·
[Effective resultant proof](../../arguments/spectral/spectral_torsion_and_syzygy_splitting.md#5-the-effective-resultant-divisor).

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
[Filtered equation comparison](../../results/local_filtration_comparison_defect.md) ·
[Normal Koszul cancellation](../../arguments/normal_koszul_cancellation.md).

