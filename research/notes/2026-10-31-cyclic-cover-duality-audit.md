# Independent audit of the full Jacobian and contact identities

Date: 2026-10-31. Reviewer: independent adversarial audit agent.
Status: **revised proposal passes independent mathematical review on its
stated hypotheses**. The removed absolute-normalization assertion remains
outside this audit's accepted coverage.
No canonical promotion or unrestricted STCI conclusion.

The object reviewed is
[the cyclic-cover duality proposal](2026-10-31-cyclic-cover-duality.md).
The hypotheses are an algebraically closed characteristic-zero field,
the fixed smooth quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and **any** proper
homogeneous complete intersection \(Z=V(F_a,G_b)\) with
\(Z_{\mathrm{red}}=C\). Put \(d=a+b\), \(m=ab/4\), and
\(\mathcal S=\operatorname{Ann}_{\mathcal O_Z}(\mathcal I_C\mathcal O_Z)\).
No regularity of a carrier, normal flatness, first-relation saturation,
or global retraction is assumed.

## 1. The original normalization argument and its disposition

The original proposal asserted the additional exact formula
\[
\Omega_Z\longrightarrow i_*\omega_C
\xrightarrow{\ m i_*\ }\omega_Z
\]
for the canonically normalized absolute fundamental class, and compared
relative traces for the projections \(z\), \(z+u\), and \(z+v\).
The identity \(\operatorname{Tr}_{A/k[[z]]}=m\cdot\mathrm{reduction}\)
is correct. The determinant-one coordinate changes also preserve the
displayed **determinant-line** frame. Nevertheless, these facts alone
do not identify the different relative Tate isomorphisms with one fixed
absolute-duality normalization. An unspecified isomorphism taking the
Jacobian to the trace is insufficient for that comparison.

The primary sources actually checked distinguish these responsibilities:
[Stacks 49.12.4](https://stacks.math.columbia.edu/tag/0BWB) gives the
Jacobian–trace isomorphism, whereas
[49.13.1–2](https://stacks.math.columbia.edu/tag/0FKB) describes the
canonical relative Tate map and its base-change compatibility.
Changing \(z\) to \(z+u\) is not the base change in that proposition.
Thus the proposal's citations did not, by themselves, discharge this
extra absolute-normalization assertion. This is a precise coverage gap,
not a counterexample to the asserted classical identity.

The author agreed to remove that stronger assertion and replace the
mixed-minor argument by the elementary algebraic-neighborhood proof
below. The downstream conclusions require no exact coefficient \(m\)
in the absolute class map. This audit does not claim to have established
that discarded extra normalization statement.

## 2. Independent reconstruction of the local argument

The reused local input is
[the October 14 pointwise conductor audit, Section 3](2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md).
Only its relative-Jacobian/socle argument is used; the normalization,
conductor and curvilinear hypotheses elsewhere in that note are not
imported. Its proof works for every actual lci thickening of smooth
support: the completed algebra
\[
A=k[[z,u,v]]/(h_1,h_2),\qquad \sqrt{(h_1,h_2)}=(u,v),
\]
is finite free of rank \(m\) over \(R=k[[z]]\). Its socle
\(\Sigma=\operatorname{Ann}_A(u,v)\) is a saturated free rank-one
\(R\)-submodule. The relative Jacobian \(j=J_{uv}\) belongs to
\(\Sigma\) generically, hence everywhere by torsion freeness.
Saturation injects \(\Sigma/z\Sigma\) into \(A/zA\). The latter is
an Artin complete intersection of length \(m\), whose Jacobian is a
nonzero socle generator in characteristic zero; the precise primary
input is [Eisenbud–Ulrich, Theorem 8.5](https://arxiv.org/pdf/1309.2050),
which includes formal nonhomogeneous Artin complete intersections.
Nakayama therefore
gives \(\Sigma=Rj\). This does not assume that socles commute with
base change or that the normal Hilbert function is constant.

For the new comparison, work first on an **algebraic étale coordinate
neighborhood** of the smooth support, with coordinates \((z,u,v)\)
and \(D=(u,v)\). The preceding completed argument proves the generator
assertion at every point of that neighborhood. For each \(\lambda\in k\),
\(z'=z+\lambda u\) restricts to the same parameter on \(D\), and its
relative Jacobian is exactly
\[
j_\lambda=j-\lambda J_{zv}.
\]
Taking \(\lambda=1\) first shows \(J_{zv}\in\Sigma\); write
\(J_{zv}=g j\), where \(g\) is regular on the reduced curve.
If \(g(p)\ne0\) at any closed point, choose
\(\lambda=g(p)^{-1}\). Then \(j_\lambda=(1-\lambda g)j\) fails to
generate the free socle at \(p\), contradicting the same pointwise
Jacobian theorem for \(z'\). Thus \(g\) vanishes at every closed point,
and reducedness and finite type imply \(g=0\). Replacing the projection
by \(z+\lambda v\) similarly gives \(J_{zu}=0\).

The order matters: this is not an argument using only the single closed
point of \(k[[z]]\), where a nonzero coefficient such as \(g=z\)
could vanish. The result is proved on the algebraic neighborhood and
then completed. An arbitrary formal coordinate change preserves its
geometric statement: the Jacobian two-form is the socle-valued conormal
volume form to the smooth support.

A direct special-point control is
\[
A=k[[z,u,v]]/(u^2-zv,v^2).
\]
It is free over \(k[[z]]\) on \(1,u,v,uv\), with generic curvilinear
fiber and special fiber \(k[u,v]/(u^2,v^2)\). Here
\(J_{uv}=4uv\), \(J_{zu}=0\), and \(J_{zv}=-2v^2=0\).
The normal Hilbert function changes, while the actual socle generator
and mixed-minor identities survive. This is a local test of the claimed
scope, not a projective existence construction.

## 3. All six minors, signs, twists and exact ideal membership

The local statement puts every ambient minor
\(M_{ij}=F_{x_i}G_{x_j}-F_{x_j}G_{x_i}\) in the actual socle,
with a local combination generating it. Complementary minors identify
their projective tuple with the tangent two-plane of the affine cone;
Euler's identities give the radial tangent direction modulo the actual
ideal. Independent differentiation of the parametrization gives
\[
\tfrac14(\partial_s\phi\wedge\partial_t\phi)
=(s^6,3s^4t^2,4s^3t^3,2s^3t^3,3s^2t^4,t^6).
\]
Complementation with the ambient volume orientation consequently gives
\[
(M_{01},M_{02},M_{03},M_{12},M_{13},M_{23})
\leftrightarrow
(t^6,-3s^2t^4,2s^3t^3,4s^3t^3,-3s^4t^2,s^6).
\]
The scalar is one common nonzero constant: the two nowhere-vanishing
tuples give the same line at each point, and their line bundles have
the same degree on the complete curve \(\mathbf P^1\).

The inherited duality identity is
\(\mathcal S=\omega_C\otimes\omega_Z^{-1}|_C\), as in
[R-0032](../results/full_conormal_socle_budget.md). Hence
\[
\deg\mathcal S=-2-4(d-4)=14-4d,\qquad
\mathcal S(d-2)\simeq\mathcal O_{\mathbf P^1}(6).
\]
The first and last sextics have no common zero, including both
endpoints. This verifies generation of the socle everywhere and
\(M_{12}-2M_{03}=0\) in the quotient sheaf. A homogeneous proper
complete-intersection ideal in four variables is saturated, so this is
the exact polynomial membership
\[
M_{12}-2M_{03}\in(F,G),
\]
with coefficient degrees \(b-2\) and \(a-2\), respectively.
Passing only to the radical would lose the substance of this conclusion.

## 4. The different and the colon

The plane pencil has no base point on \(Z\), since its base line
\(x_0=x_3=0\) misses \(C\). Its map to \(B=\mathbf P^1\) is finite,
and Cohen–Macaulay purity makes it flat. On either base chart, the
relative two-variable Jacobian is the corresponding trivialization of
\(M_{12}\). For finite flat lci maps, the different equals the Kähler
different and is locally generated by that Jacobian;
[Stacks 49.12.2–3](https://stacks.math.columbia.edu/tag/0BWB) covers this
input, including nonreduced fibers.

The sextic \(M_{12}\leftrightarrow4s^3t^3\) has exactly the zero divisor
\(R_f=3p_0+3p_\infty\). Therefore its ideal, with twists removed as
an ideal inside \(\mathcal O_Z\), is
\[
\mathfrak D_\pi=\mathcal S(-R_f).
\]
This is a nilpotent ideal when \(Z\) is nonreduced, not a Cartier
ramification divisor on \(Z\). It does not make \(Z\to B\) étale off
the endpoints. The divisor statement is on the smooth reduced support.

Although \(M_{12}\) vanishes at the endpoints as a socle section,
multiplication by its nonzero local coefficient is injective on
\(\mathcal O_C\). Since \(\mathcal S\) is faithful over
\(\mathcal O_C\), its annihilator is exactly the nilradical. Thus
\(\operatorname{Ann}_{\mathcal O_Z}(M_{12})=\mathcal I_C\mathcal O_Z\).
The homogeneous colon of a saturated ideal is saturated, giving
\[
(F,G):M_{12}=I_C
\]
in the polynomial ring. Endpoint zeros do not enlarge this annihilator.

## 5. Geometry, a genuine STCI control, and the frontier

For \(\omega=dx_0\wedge dx_3-2dx_1\wedge dx_2\), the cone over
the quartic is Lagrangian. The checked minor identity says that every
hypothetical two-equation thickening is involutive for its Poisson
bracket, since \(\{F,G\}=M_{03}-\tfrac12M_{12}\in(F,G)\).
The Leibniz rule extends this to brackets of arbitrary elements of the
ideal. The actual conormal Jacobian is supported in the socle and
retains the reduced tangent geometry through every transverse
degeneration. This is an all-pairs compatibility theorem, not a proof
of incompatibility.

[Buczyński, Theorem 4.9](https://arxiv.org/pdf/math/0503528) is about
irreducible normal complete-intersection varieties. It does not apply
to an everywhere-nonreduced thickening. The reduced-ideal Poisson
criterion in the same paper also does not establish the stronger
membership in an arbitrary nilpotent defining ideal.

An explicit control prevents that mistaken extrapolation. The twisted
cubic \(T=[s^3:s^2t:st^2:t^3]\) is Legendrian for
\(dx_0\wedge dx_3-3dx_1\wedge dx_2\) and is the sole reduced support
of the proper pair
\[
F=x_0x_2-x_1^2,\qquad
G=x_2^3-2x_1x_2x_3+x_0x_3^2.
\]
On \(x_0\ne0\), eliminating \(x_2\) gives
\(x_0^3G=(x_0^2x_3-x_1^3)^2\); on \(x_0=0\), the equations force
\(x_1=x_2=0\), its remaining endpoint. Thus the pair is an actual
characteristic-zero STCI of multiplicity two, and direct differentiation
gives
\[
M_{12}-3M_{03}=-4x_3F.
\]
Legendrian support and an involutive nonreduced CI therefore coexist.
This does not settle existence for the quartic's different embedding.

Neither the socle-valued tangent identity nor the precise different
forces a global retraction, torus invariance, or extension of the étale
reduced-algebra splitting over the two ramification points. The
remaining missing implication is a quartic-specific incompatibility of
these necessary identities with actual homogeneous two-generator
equations, uniformly in degree. None is established here.

Characteristic zero is used materially in the transverse Artin
Jacobian theorem. Its same generator conclusion holds when the
characteristic does not divide \(m\); when it divides \(m\), the trace
vanishes and the relative Jacobian vanishes instead. Extending the full
quartic formula to positive characteristic additionally requires
checking its characteristic-dependent cone and projection geometry.

## 6. Verification boundary and final disposition

The audit reconstructed the local special-point proof, the varying
projection argument, all six sextics, exact ideal and colon passages,
different twists, contact signs, and the explicit twisted-cubic control
by hand. No inherited proof, certificate, or numerical computation was
rerun. The discarded absolute-normalization assertion is not accepted
by this audit.

The revised source was read in full after the author's correction. Its
SHA-256 at final review was
`6e4ac8fe78ab99361ae2f813c59390e257dee5bfb15eac9539fa54152bc10288`.
The final mathematical disposition is **pass for Sections 1–6 as revised**:
the local comparison and every stated full-minor, exact ideal, different,
colon and contact conclusion follow. No material mathematical finding
remains unresolved in those conclusions. This establishes reviewed
provisional evidence, not canonical promotion, projective existence,
or an unrestricted quartic STCI exclusion.

## 7. Added no-retraction corollary: separate scoped review

The later source §5.1 adds a geometric extraction from the existing
missing fifth section. The independent reviewer
/root/arithmetic_cover_strategy_challenge, using a fresh
gpt-6.1-sol/high context for the bounded cover assessment, reconstructed
the argument before checking its written form. The assignment is
complete; it involved no edits, nested delegation or computation.

For any supported complete intersection as stated, its four-dimensional
space of hyperplane sections cannot surject onto the five-dimensional
space on the reduced quartic. A retraction over the pencil would
preserve its polarization and split this restriction, proving the
claimed impossibility. The generalization requires compatible
preservation of the polarization. The section argument is
characteristic free; the unique punctured retraction additionally
uses characteristic different from two and formal étaleness.

The reviewer checked the geometric interpretation and the boundaries:
no exclusion of an arbitrary unpolarized retraction, no endpoint
identification, no new independent budget, and no STCI nonexistence
claim. Its final disposition is **scoped PASS for §5.1** at source
SHA-256

    bdf7331c3163d2189b41671261777cf481353315fb351610f7dc32a2f655fb4e

The preceding Sections 1–6 retain their earlier review above; the
new review does not repeat that full audit. The companion
[strategy assessment §30](2026-10-31-unrestricted-strategy-assessment.md#30-marked-covers-clarify-a-missing-section-arithmetic-and-residual-constructions-need-embedded-input)
records the literature checks and independently challenged stopping
decision. This addition remains provisional, with no canonical
promotion.
