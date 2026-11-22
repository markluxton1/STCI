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

## 2. An explicit finite flattening test from endpoint interpolation

The defect calculations in
[endpoint delta invariants](arrangement_endpoint_delta.md)
give much more than a fiberwise Hilbert polynomial: they describe
the actual flattening stratification for the scheme-union family (1).

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

**Proposition (explicit flat-arrangement strata).**
Take the locally closed determinantal loci
\[
 B_{\mathbf r}=
 \{Z\in B_m:
  \operatorname{rank}\mathbf E_{0,n}=r_{0,n},\
  \operatorname{rank}\mathbf E_{\infty,n}=r_{\infty,n}
  \text{ for all }n<M\}
\tag{6}
\]
with their usual reduced locally closed scheme structures.
On each such locus, every cokernel in (5) is locally free, so
\(\mathcal Q_m\) is flat over \(B_{\mathbf r}\).
Since every \(\mathcal C_i\) is flat, (2) implies
\(\mathcal A_m|_{B_{\mathbf r}}\) is flat, and the
sequence defining the intersection ideal remains exact under
base change. In particular its geometric fiber is **exactly**
the intended reduced union \(A_Z\).

**Proof.** On a fixed rank stratum, a maximal nonzero minor
can be inverted locally, and all larger minors vanish.
Elementary row/column operations identify each evaluation
map with a block containing an identity matrix and zero
elsewhere. Thus its image and cokernel are vector bundles.
Equations (2), (5) give flatness of \(\mathcal A_m\) and
preservation of the map to the sum of the \(\mathcal C_i\).
Taking the kernel after a base change recovers
\(\bigcap I_{C_{z_i}}\) on every fiber. \(\square\)

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

On a stratum where (1) commutes with base change,
a sufficient additional condition for the fiber of (3)
to be the desired blow-up is **normal flatness over the
parameter stratum**:
\[
 \mathcal O/ \mathcal I_m^n\quad\text{flat over the stratum
 for every }n\ge1. \tag{7}
\]
Equivalently, the associated graded normal-cone modules
\(\mathcal I_m^n/\mathcal I_m^{n+1}\) must be flat,
together with the already-established flatness of
\(\mathcal O/\mathcal I_m\).
Indeed (7) implies
\[
 \mathcal I_m^n\otimes k(Z)\simeq I_{A_Z}^{\,n},
\quad
 \left(\bigoplus_n\mathcal I_m^n\right)\otimes k(Z)
 \simeq \bigoplus_n I_{A_Z}^{\,n},
\]
so relative Proj has the correct fiber. This follows from
the exact sequences
\(0\to\mathcal I_m^n\to\mathcal O\to
 \mathcal O/\mathcal I_m^n\to0\).
Condition (7) is **not** proved on the strata (6);
it is a further test involving *all* infinitesimal
neighborhoods, not just the reduced Hilbert polynomial.
One can inspect the graded normal cones or refine by
flattening before making an assertion about actual fibers.

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
Then \(\mathcal K_a=\ker\epsilon_a\)
and \(\mathcal K_b=\ker\epsilon_b\)
are vector bundles commuting with base change.
The projective incidence
\[
 \mathbf P(\mathcal K_a)\times_{B_m}
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

## 7. The moduli quotient and next geometric contractions

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
Rees blow-up; the explicit endpoint-flat
strata (6); the smooth separated family
(9) with fiber (10); the exact global
section dictionary (11); the characteristic-
independent normal modification (12)–(14);
the relative equation-pair incidence (16)
and its reduced CI criterion.

**Concrete unresolved steps:** identify
normal-flat strata where (3) really has
fiber \(\operatorname{Bl}_{A_Z}\mathbf P^3\);
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
are lost. The singular direct blow-ups (3)
are the geometric objects of interest,
and (12)–(14) give the local modification
that must be reconciled when passing
between the two. This is a substantive
realization/contraction program rather than
an analogy between quotient and blow-up.
