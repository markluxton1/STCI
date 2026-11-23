# Relative arrangement blow-ups and a smooth separated model

**Scope.** This develops the original proposal: blow up the **ideal of the entire finite arrangement**, vary the arrangement in families, and look for the complementary divisor contractions. All constructions here concern reduced arrangements of **distinct** transverse translates on the open quotient torus; collisions, nonreduced quotient schemes, and Chow-boundary cycles require separate extensions. The statements involving the explicit universal toric graph use [the existing calculation](chow_quotient_fan_and_blowup_comparison.md).

**General theorems used first:** the Rees-algebra definition, universal property, and flat-base-change theorem for blow-ups ([Stacks 01OF](https://stacks.math.columbia.edu/tag/01OF), [Stacks 0805](https://stacks.math.columbia.edu/tag/0805)); standard cohomology/base-change and determinantal rank stratification; the already-proved one-curve [\(V_5\) link and section dictionary](../residuals/blowup_residual_geometry.md). Ordinary blow-ups **do not** commute with an arbitrary nonflat base change; flatness of the center over the base by itself is not a substitute for checking the Rees algebra (see the explicit cautionary counterexample in the discussion following [Stacks 01OF](https://stacks.math.columbia.edu/tag/01OF)).

## 1. The actual relative arrangement ideal

Set \(T=(\mathbf G_m)^2\), with coordinates \((u,v)\). Work first with **ordered** configurations
\[
 B_m=\operatorname{Conf}_m(T)
 =\{(z_1,\dots,z_m)\in T^m:z_i\ne z_j\text{ for }i\ne j\}.
\]
The symmetric group acts freely, and the constructions below are symmetric; one can descend to the unordered configuration space after establishing the relevant properties.

In \(\mathbf P^3\times B_m\), let \(\mathcal C_i\) be the closed embedded family
\[
 ([s:t],z_1,\dots,z_m)\longmapsto
 ([s^4:s^3t:u_i st^3:v_i t^4],z_1,\dots,z_m).
\]
Each \(\mathcal C_i\cong\mathbf P^1\times B_m\). Define the **scheme union**
\[
 \mathcal A_m=\bigcup_{i=1}^m\mathcal C_i,\qquad
 \mathcal I_m=\bigcap_{i=1}^m\mathcal I_{\mathcal C_i}
 \subset\mathcal O_{\mathbf P^3\times B_m}.
 \tag{1}
\]
The canonical coherent **normalization-discrepancy** sheaf fits in
\[
 0\longrightarrow\mathcal O_{\mathcal A_m}
 \longrightarrow\bigoplus_i\mathcal O_{\mathcal C_i}
 \longrightarrow\mathcal Q_m\longrightarrow0.
 \tag{2}
\]
It is supported on the two constant endpoint sections
\(\{p_0,p_\infty\}\times B_m\).
A critical subtlety: the ideal intersection in (1) need not commute with
specialization on all of \(B_m\). A fiber of \(\mathcal A_m\) is not
automatically the reduced union \(A_Z\) without a base-change check.

The **direct proposed family** is the relative Rees blow-up
\[
 \boxed{
 \mathcal X_m^{\mathrm{Rees}}
 =\operatorname{Proj}_{\mathbf P^3\times B_m}
   \bigoplus_{n\ge0}\mathcal I_m^n
 \longrightarrow B_m .}
 \tag{3}
\]
It always exists as a projective \(B_m\)-scheme, and carries the
relative exceptional Cartier divisor \(\mathcal E\) and the pullback \(H\).
But a closed fiber of (3) is in general only
\[
 \operatorname{Proj}_{\mathbf P^3}
  \bigl(\bigoplus_{n\ge0}\mathcal I_m^n\otimes k(Z)\bigr);
\]
it is **not automatically**
\(\operatorname{Bl}_{I_{A_Z}}\mathbf P^3\). This is precisely the
nonflat-specialization issue the family construction must confront,
rather than suppress.

## 2. Finite endpoint strata and re-formed flat arrangement families

The defect calculations in
[endpoint delta invariants](arrangement_endpoint_delta.md)
give finite rank strata on which the union can be **formed anew** as a
flat family with the intended fibers. This differs from restricting the
scheme union (1), since formation of its kernel need not commute with a
nonflat change of base.

Fix \(M=4(m-1)\). For \(0\le n<M\), let \(\mathbf E_{0,n}\) be the
\(m\times N_n\) evaluation matrix with columns
\[
 \bigl(u_i^av_i^b\bigr)_{1\le i\le m},
 \qquad a,b\ge0,\quad 3a+4b\le n.
\]
Similarly let \(\mathbf E_{\infty,n}\) use
\[
 (\alpha_i,\beta_i)
 =\left(v_i^2/u_i^3,\ v_i^3/u_i^4\right).
\]
For every configuration of \(m\) distinct points, polynomials of
ordinary total degree at most \(m-1\) separate the points by Lagrange
products of suitable affine-linear forms. Their monomials have
\((3,4)\)-weighted degree at most \(4(m-1)\). Hence **uniformly**
\[
 \operatorname{rank}\mathbf E_{0,n}
 =\operatorname{rank}\mathbf E_{\infty,n}=m
 \quad\text{for }n\ge M. \tag{4}
\]

Complete (2) at \(p_0\). Because every branch uses the same
parameter \(r=x_1/x_0\), the map from
\(\mathcal O_{B_m}[[r,x_2,x_3]]\) to
\(\mathcal O_{B_m}[[r]]^{\,m}\) decomposes by the
coefficient of \(r^n\). Therefore its cokernel, regarded as a
\(\mathcal O_{B_m}\)-module, is
\[
 \mathcal Q_{0}\cong
 \bigoplus_{n=0}^{M-1}
 \operatorname{coker}(\mathbf E_{0,n}).\tag{5}
\]
The same holds for \(\mathcal Q_\infty\), with the
opposite-endpoint parameters. These are isomorphisms of
\(\mathcal O_{B_m}\)-modules after the canonical endpoint
identifications (not assertions that their full local algebra
structures split into independent graded pieces).

**Proposition (explicit flat-arrangement families on rank strata).**
Take the locally closed determinantal loci
\[
 B_{\mathbf r}=
 \{Z\in B_m:
  \operatorname{rank}\mathbf E_{0,n}=r_{0,n},\
  \operatorname{rank}\mathbf E_{\infty,n}=r_{\infty,n}
  \text{ for all }n<M\}
\tag{6}
\]
with their usual reduced locally closed scheme structures. For
\(S=B_{\mathbf r}\), define on \(\mathbf P^3\times S\)
\[
 \mathcal I_{m,S}^{\mathrm{union}}
   =\bigcap_i I_{\mathcal C_i\times_{B_m}S},\qquad
 \mathcal A_{m,S}^{\mathrm{union}}
   =V(\mathcal I_{m,S}^{\mathrm{union}}).
 \tag{6a}
\]
This **re-formed union** is flat over \(S\) and commutes with every
further base change from \(S\). Its geometric fiber is exactly the
intended reduced union \(A_Z\). Neither assertion identifies (6a) with
the restriction of \(\mathcal A_m\) or \(\mathcal I_m\) from \(B_m\).

**Proof.** On a fixed rank stratum, a maximal nonzero minor
can be inverted locally, and all larger minors vanish.
Elementary row/column operations identify each evaluation
map with a block containing an identity matrix and zero
elsewhere. Thus its image and cokernel are vector bundles.
Apply the coefficient calculation (5) **over \(S\)** to the
cokernel of the map to the pulled-back branch structure sheaves.
It is locally free over \(S\). The image of the ambient structure
sheaf in the branch sheaves is the structure sheaf of (6a), or
equivalently the kernel of the map from the branch sheaves to this
cokernel. The resulting exact sequence with the flat branch
sheaves and flat cokernel proves both its flatness and compatibility
with further base change. Flatness of this structure sheaf also
preserves the defining ideal sequence. Thus the ideal after any
further base change is the intersection of the corresponding branch
ideals. \(\square\)

**Why restriction of the original union fails.** Work in
characteristic zero, with two branches near \(p_0\), over
\(R=k[\tau]_{(\tau)}\), and choose
\[
 (u_1,v_1)=(1,1),\qquad (u_2,v_2)=(1+\tau,2).
\]
Put \(r=x_1/x_0\), \(\zeta=x_2/x_0-r^3\), and
\(\eta=x_3/x_0-r^4\). In the map to the two normalization
branches these have images
\[
 r\mapsto(r,r),\qquad
 \zeta\mapsto(0,\tau r^3),\qquad
 \eta\mapsto(0,r^4).
\]
The coefficient-of-\(r^3\) image module is the direct sum of
\(R(1,1)\) and \(R(0,\tau)\). Its second generator survives
tensoring with \(R/(\tau)\), but maps to zero on the two actual
specialized branches. In the specialized union algebra it satisfies
\(r\zeta=\zeta^2=0\), since before specialization
\(r\zeta=\tau\eta\) and \(\zeta^2=\tau r^3\zeta\).
Thus the original family has an embedded nilpotent at the endpoint,
whereas the re-formed reduced union has \(\zeta=0\).
The same coefficient module calculation on the open chart
\(v_2-v_1\ne0\) of \(B_2\), replacing \(\tau\) by
\(u_2-u_1\), exhibits the failure for (1) itself.
Local freeness of the *restricted* cokernel does not remove
\(\operatorname{Tor}_1^{\mathcal O_{B_m}}
(\mathcal Q_m,\mathcal O_S)\); this is exactly the lost kernel term.

This is a **finite** stratification: the uniform bound \(M\)
means only finitely many determinantal ranks must be checked.
The formula
\[
 P_{A_Z}(d)=4md+m-\delta_0(Z)-\delta_\infty(Z)
\]
is constant on these strata. Merely requiring its *sum*
\(\delta_0+\delta_\infty\) to be constant is a weaker condition
than requiring all ranks in (6), and is insufficient for
the full endpoint-filtration comparison.

### What more is needed for the direct Rees fiber

For a rank stratum \(S\), form the Rees blow-up using the actual
re-formed ideal \(\mathcal I=\mathcal I_{m,S}^{\mathrm{union}}\).
A sufficient additional condition for this new family to have the
desired blow-up fibers is **normal flatness over \(S\)**:
\[
 \mathcal O/ \mathcal I^n\quad\text{flat over the stratum
 for every }n\ge1. \tag{7}
\]
Equivalently, the associated graded normal-cone modules
\(\mathcal I^n/\mathcal I^{n+1}\) must be flat,
together with the already-established flatness of
\(\mathcal O/\mathcal I\).
Indeed (7) implies
\[
 \mathcal I^n\otimes k(Z)\simeq I_{A_Z}^{\,n},
\quad
 \left(\bigoplus_n\mathcal I^n\right)\otimes k(Z)
 \simeq \bigoplus_n I_{A_Z}^{\,n},
\]
so relative Proj has the correct fiber. This follows from
the exact sequences
\(0\to\mathcal I^n\to\mathcal O\to
 \mathcal O/\mathcal I^n\to0\).
Condition (7) is **not** proved on the strata (6);
it is a further test involving *all* infinitesimal
neighborhoods, not just the reduced Hilbert polynomial.
One can inspect the graded normal cones or refine by
flattening before making an assertion about actual fibers.
This proves nothing about the restriction of (3) to a nonopen
stratum unless its original Rees algebra is separately shown to
base-change to the re-formed Rees algebra. On the open maximum-rank
locus the kernel already commutes with restriction, so the distinction
disappears there.

For \(m=1\), the center is smooth over \(T\) and the
relative blow-up is the trivially transported family
\(\operatorname{Bl}_C\mathbf P^3\times T\); its
complementary \(V_5\) contraction is already known.
For \(m>1\) the two endpoint contacts make the
normal-flatness issue nontrivial.

## 3. A smooth simultaneous blow-up model on the resolved quotient

There is a second family which does have the desired
fiberwise-blow-up property **without** normal-flatness
assumptions on the singular reduced unions.

Take any *smooth projective toric resolution*
\[
 \psi:W'\longrightarrow\mathbf P^3,\qquad
 \rho:W'\longrightarrow S
\]
of the normalized graph of the rational quotient
\(q:\mathbf P^3\dashrightarrow S\), whose fan is given in
[chow_quotient_fan_and_blowup_comparison.md](chow_quotient_fan_and_blowup_comparison.md).
Over the open quotient torus \(T\), the toric map has
the canonical trivialization
\[
 \rho^{-1}(T)\simeq\mathbf P^1\times T,
 \quad
 ([s:t],u,v)\stackrel{\psi}{\longmapsto}
 [s^4:s^3t:u st^3:v t^4].
 \tag{8}
\]
(There are no extra rays in the kernel of the quotient-lattice
map after toric subdivision; the fiber fan remains that of
\(\mathbf P^1\).)

For ordered \(Z\in B_m\), let
\(\widetilde C_i=\rho^{-1}(z_i)\subset W'\).
They are **pairwise disjoint smooth** \(\mathbf P^1\)'s,
contained in the smooth open set (8), and
\(\psi|_{\widetilde C_i}:\widetilde C_i\to C_{z_i}\)
is an isomorphism. Define over \(B_m\) the disjoint
union of the moving fibers
\[
 \widetilde{\mathcal A}_m
 =\coprod_{i=1}^m\widetilde{\mathcal C}_i
 \subset W'\times B_m,\qquad
 \widehat{\mathcal W}_m=
 \operatorname{Bl}_{\widetilde{\mathcal A}_m}
       (W'\times B_m).\tag{9}
\]

**Proposition (smooth separated arrangement family).**
The morphism \(\widehat{\mathcal W}_m\to B_m\)
is smooth and projective, and its fiber is canonically
\[
 \widehat W_Z=\operatorname{Bl}_{\coprod_i\widetilde C_i}W'.
 \tag{10}
\]
There are \(m\) disjoint exceptional divisors
\(\widetilde E_i\), each isomorphic fiberwise to
\(\mathbf P^1\times\mathbf P^1\).

**Proof.** Near any one center, (8) makes (9) the
product of \(\mathbf P^1\) with the ordinary blow-up
of a smooth surface along a moving section. Translation
by \(z_i^{-1}\) makes the local section constant over
\(B_m\). Because the sections are pairwise disjoint,
these product descriptions cover all centers;
off them the total space remains the smooth
product \(W'\times B_m\). Hence the family is smooth
and commutes with every base change. Each normal
bundle \(N_{\widetilde C_i/W'}\) is
\(\mathcal O_{\mathbf P^1}^{\oplus2}\), yielding
\(\widetilde E_i\simeq
 \mathbf P^1\times\mathbf P^1\). \(\square\)

This is a **concrete family of blow-ups**, but its centers
are the *disjoint lifted orbit fibers in \(W'\)* rather
than their singular union inside \(\mathbf P^3\).
The maps \(\widehat W_Z\dashrightarrow
 X_Z=\operatorname{Bl}_{A_Z}\mathbf P^3\)
are initially only birational correspondences.
A morphism to \(X_Z\) would require
\(\mathcal I_{A_Z}\mathcal O_{\widehat W_Z}\)
to be invertible, which is **not** proved;
one must principalize this pullback if needed.

## 4. The separated family retains exactly the original section spaces

Although (9) is not the original blow-up \(X_Z\),
its section spaces are **exactly right** for
classification of containing hypersurfaces.

Put \(H=\psi^*\mathcal O_{\mathbf P^3}(1)\) on
\(W'\), and use the same letter on \(\widehat W_Z\).
Let \(\widetilde E_Z=\sum_i\widetilde E_i\).

**Proposition (global section dictionary, every \(d\)).**
For each reduced configuration \(Z\in B_m\)
and \(d\ge0\),
\[
 \boxed{\begin{aligned}
 K_d(Z)
 &=H^0(\mathbf P^3,I_{A_Z}(d))\\
 &\cong H^0(W',I_{\coprod_i\widetilde C_i}
                  \otimes\psi^*\mathcal O_{\mathbf P^3}(d))\\
 &\cong H^0(\widehat W_Z,
          \mathcal O_{\widehat W_Z}
              (dH-\widetilde E_Z)).
 \end{aligned}}\tag{11}
\]

**Proof.** Proper birationality onto the normal
\(\mathbf P^3\) gives \(\psi_*\mathcal O_{W'}=
\mathcal O_{\mathbf P^3}\).
Push forward
\[
 0\to I_{\coprod_i\widetilde C_i}
   \to\mathcal O_{W'}
   \to\bigoplus_i\mathcal O_{\widetilde C_i}\to0.
\]
Left exactness and the scheme isomorphisms
\(\widetilde C_i\to C_{z_i}\) identify
\[
 \psi_*I_{\coprod_i\widetilde C_i}
 =\ker(\mathcal O_{\mathbf P^3}\to
           \bigoplus_i\mathcal O_{C_{z_i}})
 =I_{A_Z}.
\]
The projection formula proves the first isomorphism.
For the blow-up of the disjoint regular centers,
the direct image of
\(\mathcal O_{\widehat W_Z}(-\widetilde E_Z)\)
is their ideal sheaf, proving the second
isomorphism. \(\square\)

**Relative sheaf-level version.** Let
\(\widehat g:\widehat{\mathcal W}_m
\to\mathbf P^3\times B_m\) be the
composite blow-up/graph morphism, and
let \(\mathcal H\) be the pullback of
\(\mathcal O_{\mathbf P^3}(1)\).
The same proof works *before* taking
individual fibers:
\[
 \boxed{
 \widehat g_*
 \mathcal O_{\widehat{\mathcal W}_m}
        (d\mathcal H-\widetilde{\mathcal E})
 \ \cong\ \mathcal I_m(d)
 }\tag{11b}
\]
as coherent sheaves on
\(\mathbf P^3\times B_m\).
Indeed pushforward of the exceptional
line bundle gives the ideal of the
disjoint lifted moving curves; then the
proper birational graph morphism pushes
that ideal to the kernel of
\(\mathcal O_{\mathbf P^3\times B_m}
 \to\bigoplus_i\mathcal O_{\mathcal C_i}\),
which is precisely \(\mathcal I_m\).
The projection formula handles the
hyperplane twist.

Pushing once more to \(B_m\) identifies
the coherent family of degree-\(d\)
containing-section modules
\[
 p_{B_m*}\mathcal I_m(d)
 \ \cong\
 \widehat p_*
 \mathcal O_{\widehat{\mathcal W}_m}
        (d\mathcal H-\widetilde{\mathcal E}).
 \tag{11c}
\]
These are *relative* identities,
not assertions that pushforward
commutes with **all** nonflat
specializations. On a constant-rank
stratum of the explicit evaluation
map (15), the kernel **of the restricted map** gives the
correct fiber spaces \(K_d(Z)\). This kernel need not be the
restriction of the original kernel sheaf; equivalently one can apply
(11b) afresh over that stratum using its re-formed union ideal.
This identifies the original
containing-equation family with a
direct image from a **single smooth
projective blow-up family**.

Thus the equation problem is now literally a family
of divisor spaces
\[
 |dH-\widetilde E_Z|
 \quad\text{on the smooth projective threefolds }
 \widehat W_Z.
\]
The price is that the morphism to \(\mathbf P^3\)
contracts boundary divisors; an intersection of two
chosen divisors upstairs can have residual
components that require proper pushforward and
scheme-theoretic boundary checks. Formula (11)
does **not** by itself turn two sections into an STCI.

## 5. The endpoint discrepancy is a normal-bundle modification

The map \(\psi\) on each lifted orbit curve is an
isomorphism onto \(C_{u,v}\), but the normal bundles
are not identified. The source normal bundle is
\[
 N_{\widetilde C_{u,v}/W'}
 \simeq\mathcal O_{\mathbf P^1}^{\oplus2}.
\]
The differential of \(\psi\) induces a generically
invertible map
\[
 \mathcal O_{\mathbf P^1}^{\oplus2}
 \longrightarrow N_{C_{u,v}/\mathbf P^3}.
\tag{12}
\]

Near \(p_0\), use the uniformizer \(r=x_1/x_0\).
In source coordinates \((r,u,v)\), the map is
\[
 (r,u,v)\mapsto(r,\ ur^3,\ vr^4).
\]
Its differential on normal directions is,
in regular normal frames,
\(\operatorname{diag}(r^3,r^4)\).
Near \(p_\infty\) take \(w=x_2/x_3\)
and the unimodular opposite coordinates
\[
 (\alpha,\beta)=(v^2/u^3,v^3/u^4).
\]
Then \(\psi\) again has the local form
\((w,\alpha,\beta)\mapsto
 (w,\alpha w^3,\beta w^4)\).
Therefore the normal map (12) has
local elementary divisors **\((3,4)\) at both ends**
and is invertible away from them. In particular
\[
 \boxed{
 \operatorname{coker}(12)\cong
 \bigl(k[[r]]/(r^3)\oplus k[[r]]/(r^4)\bigr)_{p_0}
 \ \oplus\
 \bigl(k[[w]]/(w^3)\oplus k[[w]]/(w^4)\bigr)_{p_\infty},
 }\tag{13}
\]
as a torsion sheaf on \(\mathbf P^1\), and its
determinant has zero divisor
\[
 7p_0+7p_\infty.\tag{14}
\]
The calculation is characteristic-independent
because the change of torus characters
\((u,v)\mapsto(\alpha,\beta)\)
has unimodular exponent matrix. There is no
need to invoke a characteristic-dependent
choice of transverse torus vector fields.
It recovers geometrically the invariant factors
and determinant divisor of the [existing
endpoint-frame result](../../frameworks/torus-supported-boundaries/torus_actions_and_endpoint_frames.md),
but explains them as the **defect of the
separated-fiber normal bundle under contraction**.

This is the precise geometric mechanism by
which two disjoint lifted arrangements acquire
high-order common contact when pushed to
\(\mathbf P^3\). For \(m>1\), the
[arrangement endpoint delta invariant](arrangement_endpoint_delta.md)
measures how *simultaneously* pushing all
the lifted branches together reduces the
normalization's structure sheaf.

## 6. A concrete universal incidence of actual equation pairs

For each \(d\ge0\), let \(S_d=H^0(\mathbf P^3,O(d))\).
The already-established translate evaluation
gives a **finite matrix over \(B_m\)**:
\[
 \epsilon_d:S_d\otimes\mathcal O_{B_m}
  \longrightarrow
  \bigoplus_{w=0}^{4d}\mathcal O_{B_m}^{\,m},
 \quad
 F\longmapsto
  \bigl(f_w(u_i,v_i)\bigr)_{w,i},
 \tag{15}
\]
where
\(F(1,r,Ur^3,Vr^4)=\sum_w r^wf_w(U,V)\).
Its fiber kernel is exactly \(K_d(Z)\)
for **arbitrary** homogeneous equations,
not just eigenforms.

Refine the endpoint strata (6) by imposing
constant ranks of \(\epsilon_a,\epsilon_b\).
On each resulting stratum \(S\), put
\(\mathcal K_a=\ker(\epsilon_a\otimes\mathcal O_S)\)
and \(\mathcal K_b=\ker(\epsilon_b\otimes\mathcal O_S)\).
These are vector bundles commuting with further base change from
\(S\); they are not asserted to be restrictions of the kernels on
\(B_m\).
The projective incidence
\[
 \mathbf P(\mathcal K_a)\times_S
 \mathbf P(\mathcal K_b) \tag{16}
\]
parametrizes chosen equations containing
the actual reduced arrangement; take its
open locus of coprime pairs (and, when
\(a=b\), mod out changes of basis if
classifying ideals rather than ordered equations).

**Degree exhaustion for reduced arrangements.**
If \(ab=4m\), any coprime pair in (16)
is a proper complete intersection of degree
\(4m\) containing \(m\) distinct quartics
of total degree \(4m\). Therefore it has
generic multiplicity one on each quartic
and no other curve component. Since a CI
is Cohen–Macaulay and generically reduced,
it is reduced; its ideal is \(I_{A_Z}\).
Conversely every reduced scheme-theoretic
CI arrangement is represented in (16).
This is an existing degree-exhaustion
principle, now placed into a **family
of smooth blow-up divisor systems** via (11).

For \(ab>4m\), set-theoretic realization
requires local generic intersection lengths
and a separate test for residual support;
neither (11) nor (16) alone gives it.
The endpoint defects are necessary filters
for reduced CIs, but not for arbitrary
thickenings with the same reduced support.

## 7. Direct fiberwise Rees blow-ups: a completed two-curve model

The direct construction using the re-formed union (6a) is tractable
for **two distinct curves**:
its local ideal and every Rees chart can be written explicitly.
This constructs the desired fiberwise direct blow-up families for
\(m=2\) on a finite, concrete stratification. It does not identify
them with the restrictions of (3) across a rank drop.

At \(p_0\), write \(r=x_1/x_0\), \(y=x_2/x_0\),
\(z=x_3/x_0\), and subtract the first branch:
\[
 Y=y-u_1r^3,\quad Z'=z-v_1r^4,\quad
 a=u_2-u_1,\quad b=v_2-v_1.
\]
The two curve ideals are \((Y,Z')\) and
\((Y-ar^3,Z'-br^4)\).

**Proposition (local complete-intersection ideal for two branches).**
If \(a\ne0\), the **scheme-theoretic intersection of
their ideals** is
\[
 \boxed{I_{A_Z,p_0}
   =\left(Z'-\frac ba rY,\quad Y(Y-ar^3)\right).}\tag{18}
\]
If \(a=0\), then \(b\ne0\) (since the points are
distinct), and
\[
 \boxed{I_{A_Z,p_0}
   =\left(Y,\quad Z'(Z'-br^4)\right).}\tag{19}
\]
Thus, after an invertible local coordinate change,
the ideal at either endpoint has the standard form
\[
 \boxed{I=(z',\,y'(y'-a'r^c)),\qquad
        a'\in k^\times,\quad c\in\{3,4\}.}\tag{20}
\]

**Proof.** If \(a\ne0\), the first generator of
(18) vanishes identically on both branches.
Modulo that generator, the two branch ideals
are the principal ideals \((Y)\) and
\((Y-ar^3)\) in \(k[[r,Y]]\).
Those distinct irreducibles are relatively
prime in this UFD, so their intersection
is their product. Relatively over a stratum where \(a\) is a unit,
the quotient by \((Y)\) is the base's formal \(r\)-disk, on which
\(Y-ar^3\) restricts to the nonzerodivisor \(-ar^3\).
The same intersection-equals-product argument therefore works over
the stratum without assuming its local rings are UFDs. With \(a=0\)
and \(b\) a unit it instead applies to \(Z'\) and \(Z'-br^4\),
giving (19). Both displayed pairs are relative regular sequences:
eliminate the smooth first coordinate, then use the monic quadratic
second generator. \(\square\)

At the opposite endpoint use the regular
coordinates
\[
 (w,y',z')=(x_2/x_3,x_1/x_3,x_0/x_3)
\]
and parameters
\((\alpha_i,\beta_i)=(v_i^2/u_i^3,v_i^3/u_i^4)\).
Exactly the same proof applies: \(c=3\)
when \(\alpha_1\ne\alpha_2\), and \(c=4\)
otherwise.

Consequently the two-curve configuration
space has a **finite four-case stratification**
according to whether \(u_1=u_2\) and
whether \(\alpha_1=\alpha_2\). On each
nonempty stratum the union **formed on that stratum** is
a *relative regular immersion of codimension two*:
near both endpoints the generators (18)–(19)
are relative regular sequences, and elsewhere
the curves are disjoint smooth sections
of the orbit-curve family. Its coordinate
ring is flat over the base stratum (locally
free of rank two over the formal \(r\)-disk,
using the monic quadratic second generator).

For a relative regular immersion,
\[
 \operatorname{gr}_{\mathcal I}\mathcal O
  \cong\operatorname{Sym}_{\mathcal O_\mathcal A}
              (\mathcal I/\mathcal I^2),
\]
and each graded term is flat over the
stratum because \(\mathcal O_\mathcal A\)
is flat and the conormal bundle is locally free.
The finite extensions
\(\mathcal O/\mathcal I^n\) are therefore
flat for all \(n\). Thus condition (7)
holds and **the Rees blow-up of that stratum's re-formed union
commutes with every further specialization within the stratum**.
In particular we have
a genuine family with fiber
\(\operatorname{Bl}_{A_Z}\mathbf P^3\),
not merely the separated model (9).

### The endpoint Rees chart and its singularity

For a local ideal of the form (20), write
\(f=z'\) and \(g=y'(y'-a'r^c)\).
As \(f,g\) form a regular sequence,
the Rees algebra is their symmetric algebra
modulo its one Koszul relation.
The blow-up embeds in
\(\operatorname{Spec}k[[r,y',z']]
 \times\mathbf P^1_{[S:T]}\) by
\[
   gS=fT.
\]
On the chart \(S\ne0\), putting
\(\lambda=T/S\) gives the **explicit
threefold hypersurface**
\[
 \boxed{y'(y'-a'r^c)=\lambda z'.}\tag{21}
\]
The other chart \(T\ne0\) is smooth:
\(z'=\mu y'(y'-a'r^c)\).

In any characteristic, (21) has one
isolated singular point at
\(r=y'=z'=\lambda=0\), over the common
endpoint. Its exceptional fiber there
is \(\mathbf P^1\). In characteristic
different from two, completing the square
gives
\[
 \lambda z'
  =\left(y'-\frac{a'}2r^c\right)^2
      -\frac{(a')^2}{4}r^{2c}.
 \tag{22}
\]
This is the standard *isolated compound
\(A_1\)* threefold form \(xy=f(z,t)\)
with quadratic leading part; the planar branch equation
\(y'(y'-a'r^c)=0\) has contact
order \(c\). A **special** hyperplane
section \(z'=\lambda\) becomes
\((y'-a'r^c/2)^2-\lambda^2
 =(a')^2r^{2c}/4\), hence has
surface singularity of type \(A_{2c-1}\)
(over characteristic different from two),
whereas a general transverse section
of the threefold has type \(A_1\). Do **not**
call the **threefold** singularity
\(cA_{2c-1}\): the general hyperplane
section determines the \(cA_1\) type;
\(c\) is additional analytic
information. See [the standard cDV
definition](https://msp.org/gt/2013/17-4/gt-v17-n4-p02-p.pdf).

Thus the first nontrivial direct arrangement
blow-up is a threefold with explicit
isolated cDV points above \(p_0,p_\infty\).
The orders \(3\) versus \(4\) are
precisely the contact stratification
detected by the endpoint delta formula,
and now also control the local
**birational singularities** of the
direct blow-up. This is concrete
input for any proposed complementary
contraction, not a claim of a new
global Sarkisov link.

## 8. A higher-\(m\) planar locus and a rigidity threshold

There is a useful generalization of the
local complete-intersection construction
that connects directly to the dual
affine-line incidence already established
for reduced \((4,4)\) arrangements.

Let \(S\) be a reduced locally closed parameter family on which all
\(u_i-u_j\) are units and
\(v_i=A+B u_i\), with \(A,B\) regular functions on \(S\).
Form the union of the pulled-back branches over \(S\).
At \(p_0\), this **re-formed union** has the relative local CI ideal
\[
 \boxed{
 \left(z-Ar^4-Br y,\quad
       \prod_{i=1}^m(y-u_i r^3)\right),
 \quad r=x_1/x_0,\ y=x_2/x_0,\ z=x_3/x_0.
 }\tag{23}
\]
The first equation is a smooth local
carrier surface; modulo it each branch
is a principal divisor \(y-u_i r^3\).
The factors need not be irreducibles over the parameter ring, so a
relative argument is needed: the quotient by any one monic factor
is \(\mathcal O_S[[r]]\), on which the product of the preceding
factors restricts to a unit times a power of \(r\), a nonzerodivisor.
Induction therefore identifies the intersection of their principal
ideals with their product. The ring defined by
(23) is free of rank \(m\) over
the formal \(r\)-disk, with basis
\(1,y,\ldots,y^{m-1}\).
Thus the family is normally flat at
\(p_0\) on the open locus where the
\(u_i\)'s remain distinct.

If in addition the opposite-endpoint
coordinates \(\alpha_i\) are distinct
and satisfy \(\beta_i=C+D\alpha_i\),
then the identical construction at
\(p_\infty\) gives
\[
 \boxed{
 \left(z'-Cw^4-Dw y',\quad
       \prod_{i=1}^m(y'-\alpha_i w^3)\right),
 \ w=x_2/x_3,\
 y'=x_1/x_3,\
 z'=x_0/x_3.
 }\tag{24}
\]
Thus on this **dual-planar locus**
the union formed over the locus has
a relative local CI ideal at both
endpoints, and the direct arrangement
Rees blow-up genuinely commutes with
further specialization in any such family. This uses its re-formed
ideal, not an unverified pullback of \(\mathcal I_m\) from \(B_m\).

**Proposition (a degree-four rigidity gate).**
Assume \(m\ge5\) distinct \(u_i\)'s,
the first affine-line incidence in
(23), and the second incidence in
(24), with all \(\alpha_i\) distinct.
Then necessarily
\[
 \boxed{A=C=0,\qquad D=B\ne0,\qquad
        v_i=B u_i\quad\forall i.}\tag{25}
\]
Hence **every** such \(m\ge5\)
simultaneously dual-planar
configuration lies on a common
smooth quadric
\(x_0x_3-Bx_1x_2=0\).
For non-quadric dual-planar families
with nonzero line intercepts,
there can be at most four distinct
translated curves.

**Proof.** The opposite incidence is
equivalent to
\[
 (A+Bu)^3-Du(A+Bu)^2-Cu^4=0
\tag{26}
\]
at every chosen \(u_i\), because
\(\beta=v^3/u^4\) and
\(\alpha=v^2/u^3\).
The left side has degree at most four.
With at least five distinct roots
it is identically zero. Its constant
coefficient is \(A^3\), forcing
\(A=0\); its degree-four coefficient
is \(-C\), forcing \(C=0\).
The remaining coefficient is
\(B^2(B-D)u^3\).
Since all \(v_i=Bu_i\) are nonzero,
\(B\ne0\), so \(D=B\). The converse
quadric relation is immediate.
The argument is valid in every
characteristic. \(\square\)

This extends the geometric **pattern**
behind the degree-\((4,4)\) line
criterion, without claiming
that arbitrary degrees or
nonreduced STCI structures obey
line-incidence conditions. It also
shows exactly where such a
proposed universal line-based
framework stops: for \(m\ge5\),
its only configurations lie on
a quadric carrier. The correct
general-degree replacement would
need higher-complexity curves
on the quotient surface,
or more than one weight component
per defining equation.

## 9. The moduli quotient and next geometric contractions

There is a second torus quotient, **distinct**
from the intrinsic \(H\)-quotient:
the residual diagonal torus \(T\) translates
all \(m\) parameters simultaneously. On ordered
configurations,
\[
 B_m/T
 \simeq\{(z_2z_1^{-1},\ldots,z_mz_1^{-1})
       \in T^{m-1}:\ 
       z_i\ne1,\ z_i\ne z_j\}.
 \tag{17}
\]
This removes the two degrees of freedom
corresponding to simultaneous ambient
coordinate scaling; for \(m=1\)
the family is isotrivial. The projective
blow-up and divisor-incidence constructions
are equivariant for this diagonal action.
For unordered configurations the
finite symmetric-group quotient must also
be taken into account.

**Already constructed:** (3) as a relative
Rees blow-up with possibly incorrect arrangement fibers;
genuine fiberwise Rees families formed anew on the two-curve contact
strata and the dual-planar locus;
the explicit rank strata (6) with re-formed flat unions (6a);
the smooth separated family
(9) with fiber (10); the exact global
section dictionary (11); the characteristic-
independent normal modification (12)–(14);
the relative equation-pair incidence (16)
and its reduced CI criterion.

**Concrete unresolved steps:** identify
further strata with normally flat re-formed unions, and determine
where their Rees algebras agree with the restriction of (3),
for general non-planar configurations;
compute local Rees and exceptional fibers
at \(p_0,p_\infty\) for \(m=2,3,4\);
principalize the pulled-back singular
arrangement ideal on (9) and determine
the induced morphism to (3);
study cones of movable divisors and possible
Mori/Sarkisov contractions on these
threefolds; and extend (9) to collision and
Chow-boundary schemes retaining flat
embedded ideals rather than just cycles.
No complementary \(V_5\)-type contraction
is asserted for \(m>1\).

**Interpretation:** (9) gives a single
smooth relative model where all arrangement
curves have been separated, and (11) proves
that no homogeneous **containment** equations
are lost. The singular blow-ups \(\operatorname{Bl}_{A_Z}\mathbf P^3\)
are the fiberwise geometric objects of interest; they are fibers of
the re-formed normal-flat families just proved, and are not automatically
fibers of the unrestricted universal construction (3).
The normal-bundle formulas (12)–(14) give the local modification
that must be reconciled when passing
between the two. This is a substantive
realization/contraction program rather than
an analogy between quotient and blow-up.
