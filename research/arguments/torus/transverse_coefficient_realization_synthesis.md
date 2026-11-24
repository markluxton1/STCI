# Constructing CI equations from transverse Chow coefficients

**Status:** research synthesis and elementary comparisons, characteristic zero unless stated otherwise. The organizing principle is a research objective, not a new universal exclusion theorem. Existing proof owners are linked below. The additional product/Grassmannian and centered-section formulas are recorded with their derivations for subsequent independent review.

## 1. The organizing principle: build the equations from the cycle

Start with the unordered configuration
\[
 \sigma=\sum_i n_i[(u_i,v_i)]\in\operatorname{Sym}^m T,\quad
 T=(\mathbf G_m)^2,\quad m=\sum_i n_i,\quad
 C_{u,v}=[s^4:s^3t:u st^3:v t^4].
\]
Write \(z,x,y,w=x_0,x_1,x_2,x_3\), \(A=xy,\ B=zw\),
\(q_i=u_i/v_i\), and \(\eta_i=u_i^2/v_i\).
For fixed degrees \(d,e\) with \(de=4m\), the objective is to describe
the realization locus \(\mathcal R_{d,e}\) of configurations that are
the **entire fundamental cycle** of an actual proper pair \(F_d,G_e\).

Reverse the usual order of investigation. Rather than select a carrier
and seek a mate or compute an invariant after finding \(F,G\), construct
the canonical objects of \(\sigma\) first. Each then specifies
requirements on the unknown equations: ideal memberships and their
Koszul cofactors, prescribed section spaces and line bundles,
determinantal presentations, compatibility of gradients, and gluing
through the coordinate boundary.

The polynomials
\[
 \mathcal C_\sigma(X,Y,W)=\prod_i(X+u_iY+v_iW)^{n_i},\qquad
 H_\sigma(A,B)=\prod_i(A-q_iB)^{n_i}
\]
are the natural coefficient coordinates of this realization problem.
The latter is a specialization of the former:
\[
 H_\sigma(A,B)=\mathcal C_\sigma(0,-B,A)/\mathcal C_\sigma(0,0,1).
\]
The full transverse Chow polynomial determines the cycle but not a
nonreduced scheme realizing it. The realization locus is constructible
(by the proper-pair locus and the Chow-form/resultant morphism);
equations alone need not describe it. The exact reduced-cycle criterion,
including a coprime-pair condition, is already proved in
[transverse Chow coefficients](transverse_chow_moment_realization.md).
The moving nonreduced case is the genuine gap.

**Research objective:** extract useful, preferably degree-uniform
relations on the coefficients from the joint existence of \(F,G\).
The complete set of spectral conditions may be much richer than a first
moment, but we do not need to classify the realization locus to settle
STCI. A single necessary coefficient relation excluding its small
diagonal would suffice. Do not make full classification a prerequisite
to using a successful small part of this framework.

### What the spectrum can and cannot encode

Write \(H=A^m-M_1A^{m-1}B+M_2A^{m-2}B^2-\cdots\).
The character \(q=xy/(zw)\) is distinguished by the relation
\(1+3=0+4\) of longitudinal weights. Under transverse torus translation
all \(q_i\) scale by the same unit, so \(M_j\) scales by its \(j\)-th
power. Vanishing is intrinsic under that symmetry, not under arbitrary
changes of character. The first condition is eigenvalue balance,
\(M_1=\sum n_iq_i=0\). On the small diagonal \(M_1=mq\ne0\) in
characteristic zero; in characteristic dividing \(m\) this separator
does not work. Equivalently,
\([YW^{m-1}]\mathcal C_\sigma=M_1[W^m]\mathcal C_\sigma\).

The full spectral polynomial alone cannot distinguish all configurations.
For example \(F=x^4-z^3w,\ G=y^4-zw^3\) realizes the four reduced
curves \(C_{\zeta,1}\) for \(\zeta^4=1\). The four curves
\(C_{1,\zeta^{-1}}\) have the same \(H=A^4-B^4\) but are all on
the irreducible cubic \(z^2y-x^3=0\). Any quartic containing them
must contain the cubic by degree exhaustion (16 > 12), so there is
no proper (4,4) pair for this second cycle. In fact the existing
[degree-four spectral surjectivity](chow_realization_moment_separation.md)
shows every depressed quartic with nonzero constant term occurs.
No further universal independent equation in just those quartic
spectral coefficients should be sought. The paired information in
\(\mathcal C_\sigma\) is indispensable for full realization.
The reciprocal first moment is not universally zero either.

## 2. The endomorphisms arise from the configuration itself

The projected effective divisor \(D=\sum_i n_i[q_i]\) on
\(\mathbf G_m\) has coordinate ring
\[
 E_D=k[T,T^{-1}]/(P(T)),\qquad P(T)=H(T,1).
\]
Multiplication by \(T\), denoted \(\Phi\), has characteristic polynomial
\(P\), trace \(M_1\), exterior-power traces \(M_j\), and determinant
\(M_m\). Its traces of powers are the spectral power sums (Newton
identities in characteristic zero). Basis change conjugates \(\Phi\);
transverse translation scales it. This gives a direct reason to think
of balance as tracelessness. The projected-divisor algebra is **not**
the actual CI algebra, and repeated eigenvalues need not correspond
to the same Jordan structure there.

On the dense projective torus use
\[
 r=x/z,\quad U=z^2y/x^3,\quad V=z^3w/x^4,\quad
 [z:x:y:w]=[1:r:Ur^3:Vr^4].
\]
Each orbit is \(\mathbf G_m\times\{(u_i,v_i)\}\). The actual CI
restricts to a finite flat rank-\(m\) algebra over \(k[r^{\pm1}]\)
(the support is finite over the base, the nilpotent thickening is
finite, and CM implies torsion-freeness). Its commuting multiplication
operators have
\[
 \det(TI-\mu_{U/V})=P(T),\qquad
 \det(XI+Y\mu_U+W\mu_V)=\mathcal C_\sigma(X,Y,W).
\]
These identities follow by filtering each local generic algebra by
its maximal ideal; they retain multiplicity without requiring an
invariant CI ideal. See the [constant fat-point envelope](full_transverse_chow_pullback_envelope.md)
and the [embedded quotient framework](../../frameworks/embedded-torus-quotients/index.md).
Cayley--Hamilton is available but not the starting point.

Projection from \(L=V(z,w)\) instead has rank \(4m\).
For the finite flat projection onto \([z:w]\), the characteristic
polynomial of multiplication by \(q\) on the generic fiber is \(P^4\).
The polynomial \(P\) itself annihilates the generic algebra, since
each local generic length is \(n_i\). Homogenizing and using
unmixedness gives \(H(xy,zw)\in(F,G)\).

The elementary motivation for trace is summing over a fiber:
on \(z=1\), \(t^4=w/v_i\), \(xy=q_iw\).
Thus \(\operatorname{Tr}(xy)=4zwM_1\). The residue identity is
the corresponding coefficient-extraction operation. For monic
\(f\) with distinct roots \(r_j\), Lagrange interpolation gives
\([t^{\deg f-1}](h\bmod f)=\sum_j h(r_j)/f'(r_j)\);
replacing \(h\) by \(hf'\) recovers the trace. The multivariable
finite-CI version is the standard Scheja--Storch/Grothendieck residue
pairing; see [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md).

The explicit degree-(2m,...,3m) quadric/cubic polar coefficients also
belong to the actual ideal. They constrain construction of the pair.
Use the [polarization proof](weighted_chow_quadric_cubic_polarizations.md)
with its [saturation correction](spectral_interpolation_and_polar_saturation.md):
the two opposite chains give the same dense-torus envelope, and their
syzygy containing \(M_1\) is not an independent obstruction.

## 3. Product geometry: a fixed quadric and the q-translation

Use the product coordinates
\[
 a=x/z,\quad b=y/z,\quad q=xy/(zw),\qquad
 [z:x:y:w]=[1:a:b:ab/q].
\]
Over nonzero \(q\), the graph of the quadric pencil is
\(\mathbf P^1_a\times\mathbf P^1_b\times\mathbf G_m\);
its slice is the Segre quadric \(Q_q\).
The orbit closure in the slice is \(b=ua^3\), of multidegree
\((1,3,0)\) as a map from its normalization.
Distinct \(q\)'s are separated by this graph; at a fixed \(q\),
distinct \(u\)'s meet with length three at each of the two corners.
Three successive point blowups at either corner turn the local
cubic graphs into separated fibers with parameter \(u\) or its
reciprocal; self-intersection drops from six to zero.

The six elementary coordinate projections have ratios
\[
 (r_{01},r_{02},r_{03},r_{12},r_{13},r_{23})
  =(a,b,ab/q,b/a,b/q,a/q)
\]
and degrees \((1,3,4,2,3,1)\) on the normalization.
Triangle identities are \(r_{ij}r_{jk}=r_{ik}\).
Opposite edges recover \(q=r_{01}/r_{23}=r_{02}/r_{13}\),
and \(r_{12}^2/r_{03}=\eta\).
Any spanning tree of the four coordinate vertices gives a birational
three-ratio product model (six elementary ratios, sixteen labeled
spanning trees, not six trees). For example the successive-ratio
model has multidegree (1,2,1). The blowup of four coordinate points
followed by the six strict coordinate lines, the standard
permutohedral toric threefold, resolves all six elementary ratios.
The pullback of \(O(1)\) under \(r_{ij}\) has class
\(H-E_k-E_l-E_{kl}\) for complementary indices \(k,l\), with total
pullback convention for the point classes. A further fan refinement
may be needed for the \(q\)-character itself. This resolution is
distinct from the normalized Chow quotient: see
[quotient fan and blowup comparison](chow_quotient_fan_and_blowup_comparison.md).

For a homogeneous degree-\(d\) form, the product dictionary is
\[
 F(1,a,b,ab/q)=\sum_{r,s=0}^{d} a^rb^sf_{rs}(q),\qquad
 f_{rs}(q)=\sum_{\ell=\max(0,r+s-d)}^{\min(r,s)}
 c_{d-r-s+\ell,r-\ell,s-\ell,\ell}q^{-\ell}.
\]
It follows term by term from the monomial substitution.
The boundary coefficients of the bidegree square have only one
allowed Laurent power of \(q\). Homogenization uses a subsystem of
\(O(d,d,d)\), with base loci at boundary \(q\)-values.
For a generic nonzero quadric parameter not among the \(q_i\), the
restricted pair of bidegrees (d,d),(e,e) intersects at the two
corners with length \(4m\) each: intersect the CM curve with the
quadric, using additivity of Cartier intersection multiplicities
and order four on each normalized component at each endpoint.
At \(q_i\) the restrictions have common curves.
The strict transform of an actual pair need not remain a CI;
exceptional components and thickening data must be accounted for.

This explains why arbitrary spectra are easy on the open torus:
\(U=u_0,\ P(q)=0\). Homogenize by \(F=z^2y-u_0x^3\) and
\(G=H(xy,zw)\). On the quadric with Segre coordinates
\(z=a_0b_0,\ x=a_1b_0,\ y=a_0b_1,\ w=a_1b_1/q_i\),
\(F=b_0^2(a_0^3b_1-u_0a_1^3b_0)\).
Thus the intersection has the desired cycle plus \(2m\) times the
line \(z=x=0\). The obstruction must use projective extension,
not just the existence of a torus algebra with prescribed norm.

## 4. Three Segre surfaces in Gr(2,4)

Use primal Plücker coordinates \(p_{ij}\). The lines joining points
on two complementary coordinate lines form a Segre surface
\(\Sigma_{ij|kl}=V(p_{ij},p_{kl})\cap\operatorname{Gr}(2,4)\).
For each pairing use coordinates \([A_0:A_1]=[x_i:x_j]\) and
\([B_0:B_1]=[x_k:x_l]\) on the two factors. Let \(R_\sigma\) be
the full projective Chow form, and
\(K_\sigma(U,V)=\prod_i(U-\eta_i V)^{n_i}\).
Up to nonzero scalar the restrictions are
\[
\begin{aligned}
 R_\sigma|_{\Sigma_{01|23}}&=A_1^{3m}B_0^{3m}H(A_1B_0,A_0B_1),\\
 R_\sigma|_{\Sigma_{02|13}}&=A_1^mB_0^mH(A_1B_0,A_0B_1)^3,\\
 R_\sigma|_{\Sigma_{03|12}}&=(A_0A_1)^m
 K_\sigma(A_0B_1^2,A_1B_0^2)^2 .
\end{aligned}
\]
Derivation: substitute the parametrization into
\(A_0x_j-A_1x_i\) and \(B_0x_l-B_1x_k\) and take their binary
resultant. For the first pairing the two factors are
\(s^3(A_0t-A_1s),\,t^3(vB_0t-uB_1s)\);
for the second they are
\(s(A_0ut^3-A_1s^3),\,t(B_0vt^3-B_1s^3)\);
for the third they are
\(vA_0t^4-A_1s^4,\,st(uB_0t^2-B_1s^2)\).
Multiplicativity gives the displayed endpoint monomials and
spectral factors. All have bidegree (4m,4m).
The exponents 1,3,2 are the degrees onto the respective
projected images. These are Chow-cycle identities, also valid
with multiplicities, not assertions about exceptional schemes.

For an actual CI the same Chow form is the determinant of the
Sylvester map on every line \(\ell\):
\[
 H^0(O_\ell(e-1))\oplus H^0(O_\ell(d-1))
 \longrightarrow H^0(O_\ell(d+e-1)),\quad
 (P,Q)\longmapsto PF|_\ell+QG|_\ell .
\]
Thus the same unknown pair must produce all three factorizations,
not three independently chosen resultants. The exact general
criterion is existence of such a resultant presentation by a
proper pair; our task is to extract simpler coefficient conditions.
Compatibility of the three restrictions as sections of the Chow
line bundle alone is automatic for every cycle and cannot obstruct CI.
A useful further condition must use the common equation presentation.

At the disjoint line \(L=V(z,w)\), put
\(z=\alpha x+\beta y,\ w=\gamma x+\delta y\).
The two opposite families give the exact restrictions
\(R(\alpha,0,0,\delta)=H(1,\alpha\delta)\) and
\(R(0,\beta,\gamma,0)=H(1,\beta\gamma)^3\)
after normalizing \(R(L)=1\). Weight symmetry eliminates all
other terms of degree at most two. Hence
\(R=1-M_1(\alpha\delta+3\beta\gamma)+O(3)\).
The ruling degrees explain the two Hessian coefficients.
The [existing Chow/first-jet comparison](transverse_chow_moment_realization.md)
identifies the equation-side coefficient; no Hessian vanishing
for arbitrary proper pairs is proved.

## 5. Global sections as requirements on F,G

For a proper CI \(Z\) of the stated cycle, adjunction gives
\(\omega_Z=O_Z(d+e-4)\); its fundamental class map sends the
six homogeneous differential expressions
\(x_i\,dx_j-x_j\,dx_i\) to sections of \(\omega_Z(2)\).
In an adjunction trivialization they are the complementary signed
minors \(D_{kl}\) of the matrix of gradients of \(F,G\).
A realization must give these sections homogeneous polynomial
lifts of degree \(d+e-2\), and realize them by actual gradients,
not merely by a matrix satisfying Plücker relations.
The sections depend on the realizing scheme and adjunction
identification; the cycle alone determines their weighted
normalization-side fundamental-class expressions, not a canonical
ambient polynomial lift or the nonreduced dualizing sheaf.

The tangent Plücker coordinates of the orbit are
\[
 (zx,3zy,4zw,2xy,3xw,yw),
 \qquad q=2p_{12}/p_{03}.
\]
The hyperplane sections \(2p_{12}-qp_{03}=0\) are Lagrangian
Grassmannians for \(dx\wedge dy-(q/2)dz\wedge dw\).
Their common base is \(\Sigma_{03|12}\).
The established [contact geometry](contact_jacobians_and_hamiltonian_actions.md)
and [intrinsic quadric spectrum](quadric_pencil_spectral_intrinsic_geometry.md)
connect the sole-support Poisson identity to the longitudinal
torus via the Hamiltonian of \(xy-qzw\). Involutivity does not
imply this Hamiltonian preserves the actual CI ideal.
Plücker products may be zero on generic thickened components
because the minors lie in the generic socles.

### Centered differential and scalar part of the spectrum

Put \(J=D_{12}\), \(q=xy/(zw)\) in the total quotient ring.
The established spectral--Jacobian identity is \(qJ=2D_{03}\).
Under finite-flat duality for \(\pi:Z\to\mathbf P^1_{[z:w]}\),
\(\pi_*\omega_Z(2)=(\pi_*O_Z)^\vee\); the section \(J\) corresponds
to trace. The homogeneous coordinate ring is graded free over
\(k[z,w]\) with a basis lifting the monomials of
\(k[x,y]/(F|_L,G|_L)\); its degree distribution is the binary CI
Hilbert series. On a monomial lift \(x^r y^s\), generic fiber
summation gives
\[
 \operatorname{Tr}(q^\ell x^r y^s)=
 4z^{r+s-j}w^j\sum_i n_i q_i^\ell u_i^s/v_i^j,
 \quad j=(r+3s)/4\in\mathbf Z,
\]
and zero if \(j\) is not integral. For positive \(r+s\) every
nonzero entry is divisible by \(zw\); the degree-zero basis entry
is the sole exception. Therefore, in characteristic zero,
\[
 qJ=(M_1/m)J+zw\,S,\quad S\in H^0(Z,\omega_Z)
\]
in the adjunction identification. More generally, for any polynomial
\(p\) replace \(q\) by \(p(q)\) and \(M_1/m\) by
\(\operatorname{Tr}(p(\Phi))/m\). Regularity of the resulting
numerators follows directly from the trace coordinates and
duality, without assuming \(q\) regular at the endpoints.

The centered differential
\[
 \frac{x\,dy-y\,dx}{zw}
 -\frac{M_1}{2m}\frac{z\,dw-w\,dz}{zw}
\]
is consequently regular in \(\omega_Z\). On each normalized branch
the first term is \(2q_i\,dt/t\), and the second removes the
mean eigenvalue. This is the geometric version of separating an
endomorphism into its scalar and traceless parts. A coordinate
of the regular section \(S\), evaluated on \(xy\) via the duality
pairing, is \(4(\sum n_iq_i^2-M_1^2/m)\), a centered second moment.
For sole support \(S=0\), since trace kills the generic nilpotent
part and the mean equals the sole eigenvalue.

The **uncentered** differential is regular iff \(M_1=0\) for
such a CI. Its endpoint residues are \(2M_1,-2M_1\).
The global residue theorem gives no obstruction, since they
already sum to zero. At \(p_0\), write
\(F(1,x,y,w)=f+w f_1+\cdots,\ G=g+w g_1+\cdots\).
Euler gives the endpoint numerator
\(D_{03}=f_1(xg_x+yg_y)-g_1(xf_x+yf_y)\) modulo \((f,g)\).
It lies in the one-dimensional socle and equals
\((M_1/(2m))(f_xg_y-f_yg_x)\) there, by the same trace pairing.
Thus regularity at either endpoint, the Hessian vanishing, and
the first normal jet residue on the disjoint line are equivalent
to spectral balance, not proofs of it. The exact first-jet
Macaulay pairing is in [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md).
A single local smooth branch \(y=ux^3,w=vx^4\) has all the local
spectral identities yet a pole \(2q\,dx/x\); the missing input is global.

## 6. Grassmannian sum pencil and return to equations

The [Grassmannian sum and conormal compatibility account](grassmannian_sum_and_conormal_compatibility.md) records the enlarged relative Grassmannian, the direct sum-pencil blowup (without resolving individual spectral pencils), the integral ambient finite fibers, collision relations, the intrinsic conormal graph and the compatible weighted q-form. It distinguishes graph incidence from a canonical lift of nilpotent Plücker data and records the scalar supplied by the actual cycle.

The useful next step is to work backwards: eliminate the auxiliary Grassmannian coordinates and identify which compatibility equations impose genuine constraints on the common homogeneous source. The immediate target is the existing binary first-normal-jet pairing on the disjoint projection line. The weighted q-form follows from spectral ideal membership and Euler, so it does not independently prove balance. No new UM1 coverage or priority change is asserted.

## 7. What to carry forward

* Use the existing reduced-cycle evaluation/moment-matrix criterion
  as the constructive model, and the canonical fat-point envelope
  for repeated components. Do not infer scheme structure from trace.
* Extract simultaneous equation constraints from intrinsic coefficient
  constructions. Check that a proposed additional constraint is not
  already automatic by saturation, duality, or Chow compatibility.
* Compare the common homogeneous equation presentation across the
  product models and the three Grassmannian restrictions. Boundary
  compactification is essential; arbitrary spectra occur on the torus.
* Treat the line-bundle/section viewpoint as a source of constructive
  requirements on the unknown pair, not an assertion that every
  compatible list of sections integrates to homogeneous gradients.
  Hartshorne--Serre gives the established subcanonical lci-to-rank-two
  bundle construction; a CI corresponds to a split bundle, and
  prescribing the cycle is weaker than prescribing an lci scheme.
* Keep the first-moment problem as one possible small, consequential
  part of the coefficient-realization program. Neither centered
  regularity nor the spectral polynomial recurrences remove the
  scalar term. No universal first-moment vanishing is proved here.

The current proof boundary is maintained in
[universal first moment proof boundary](universal_first_moment_proof_boundary.md)
and the [corpus synthesis](universal_first_moment_corpus_review.md).
This synthesis records the geometric motivation and interfaces, not a
parallel proof of the established results or a replacement for the
existing open-problem priorities.
