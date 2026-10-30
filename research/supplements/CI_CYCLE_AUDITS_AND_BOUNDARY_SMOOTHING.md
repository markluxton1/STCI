# Complete-intersection cycles: consolidated mathematical investigations

Full source mathematical content retained in subject sections. Statements retain their original provisional or audited scope; this compilation does not promote results.


---

## 2026-10-25-ci-cycle-exploration-audit.md

# Independent audit of the complete-intersection cycle exploration

Date: 2026-10-25. Reviewer: independent audit agent in the notebook team.
Status: mathematical review of exploratory calculations and their stated limits;
no canonical result promotion and no STCI conclusion.

The review starts from [research/INDEX.md](../INDEX.md), then
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md),
[STCI-R-0021](../results/quartic_mu4_degeneration.md), and
[the contribution protocol](../CONTRIBUTING_AGENT.md). The promoted facts about
the prescribed four-component family and the fixed curve's conormal splitting
are used as premises. Their inherited proofs were not rerun.

The contributions reviewed are [deformations](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-deformation-laboratorymd),
[conductor and topology](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-conductor-topologymd),
[specialization and proximity](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-specialization-proximitymd),
and [the root pencil](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-root-pencilmd). The synthesis notebook
is reviewed separately below when assembled.

## 1. Independent reconstruction of the deformation calculation

An ambient degree-four monomial with exponent vector
\((e_0,e_1,e_2,e_3)\) restricts to the binary monomial with parameter weight
\(j=e_1+3e_2+4e_3\). All weights \(0,\ldots,16\) occur among the thirty-five
monomials. Therefore the actual global source has dimension \(35-17=18\),
and its pencil Grassmannian has dimension \(2(18-2)=32\).

For each weight, differences from one chosen monomial give an integral basis
of the restriction kernel. In coordinates
\(x_0=1,x_1=u,x_2=u^3+Y,x_3=u^4+X\), a basis difference of weight \(j\)
has first-normal coefficients
\[
A=(e_3-e'_3)u^{j-4},\qquad B=(e_2-e'_2)u^{j-3}.
\]
Terms with zero coefficients are omitted; no negative powers are introduced.
This independently constructs the global coefficient space, rather than
replacing it by unrestricted rational-function-valued sections.

At the distinguished pair the first symbols are
\(F=(-1,0)\), \(G=(-3u^8,4u^9)\). Hence the derivative of the affine
determinant is
\[
(h,k)\longmapsto4u^9A_h+3u^8B_h-B_k.
\]
An independent rational row reduction on the above basis gives rank nineteen
in the nineteen coefficients of degrees zero through eighteen. The projective
rank is eighteen. Changes of basis of the pencil contribute only a scalar
multiple of the original determinant, so quotienting by them gives the same
rank on the Grassmannian. This confirms the claimed surjective differential
and fourteen-dimensional tangent kernel.

Both source and target are smooth at these characteristic-zero points. The
usual differential criterion therefore says that the boundary map is smooth
locally at the distinguished pencil, and that its local fiber is smooth of
dimension fourteen. This is a local deduction. It neither classifies that fiber
nor realizes every global boundary divisor.

The boundary degree is independently forced by
\(\det N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-14)\) and two quartic
twists of degree sixteen: \(-14+16+16=18\).

## 2. Generic residual curve: hypotheses and geometric bridge

The new generic-residual explanation in the deformation note is sound with its
stated characteristic-zero, general-pair scope. The checked ideal generators
have degree at most three. They give global generation of \(I_C(3)\), and the
graph construction embeds the blowup into \(\mathbf P^3\times\mathbf P^6\).
The Segre line bundle restricts to \(4H-E\), which is therefore very ample.
Two general members give a smooth irreducible residual curve upstairs by
Bertini. The smoothness and irreducibility inputs can be checked in the primary
references [Stacks, smooth Bertini](https://stacks.math.columbia.edu/tag/0FD4)
and [Stacks, irreducible Bertini](https://stacks.math.columbia.edu/tag/0G4C).

The surjective boundary differential implies that simple determinant zeros
occur for general pencils. At a simple zero the two first symbols have rank
one, so there is exactly one common point on the exceptional fiber. The
residual curve crosses the exceptional divisor transversely there. In local
blowup coordinates \(x=t,y=tv,u=u(t)\), transversality means that \(t\) is
a curve parameter; its image has nonzero \(x\)-derivative. Thus blowdown is
smooth on that branch and its tangent is transverse to the marked curve
\(x=y=0\). This checks the sometimes omitted bridge from the smooth residual
upstairs to a smooth residual downstairs.

On a smooth quartic containing \(C\), adjunction gives \(C^2=-2\) and the
residual class is \(4H-C\). Its degree is twelve, its square is thirty, its
genus is sixteen, and its intersection with \(C\) has length eighteen.
Equivalently, \(0+16+18-1=33\). The residual genus is not seventeen.

This argument concerns a general point of the full proper-pair parameter space.
It does not assert smooth residual curves for the asymmetric fixed-carrier
pencil or for a general member of the fiber over \(9p+9q\).

## 3. Root pencil and the elliptic diagnostic

The global perturbation is correctly signed:
\[
G_a=G+a x_3^2Q,
\qquad Q=x_0x_3-x_1x_2.
\]
On the fixed carrier, its roots satisfy
\[
f_a(z)=z^4-az+a-1=(z-1)(z^3+z^2+z+1-a).
\]
Distinct nonzero roots give four smooth quartics. At the first endpoint their
leading coefficients are the roots \(\lambda\); at the other they are
\(\lambda^{-3}\). The relation
\[
\lambda^{-3}=\frac{\lambda}{a\lambda+1-a}
\]
is a common Möbius transformation for \(a\ne1\). Consequently the endpoint
cross-ratios agree throughout the open four-smooth-component locus. This
strengthens the proposed elliptic diagnostic without making it an invariant
of arbitrary moving-carrier complete intersections.

The discriminant and exceptional values are correct:
\[
\operatorname{disc}(f_a)
=256(a-1)^3-27a^4
=(a-4)^2(-27a^2+40a-16).
\]
At \(a=4\), the fundamental cycle is twice the marked quartic plus two other
quartics, since \(f_4=(z-1)^2(z^2+2z+3)\). The first-normal determinant is
identically zero there. At \(a=1\), the polynomial has distinct roots but the
zero-root parametrization is a singular plane quartic. The note correctly
keeps this embedded boundary separate from the root discriminant.

At infinity the cycle \(C+3L_a+9L_d\) follows from the explicit Segre
factorization of \(F|_Q\) and the doubled plane \(x_3^2\). Degree is
\(4+3+9=16\). Its marked determinant divisor can remain \(9p+9q\), although
the residual schemes and their support differ drastically from the original
three quartics. This is a valid example of lost information in the boundary.

For \(w^2=f_a(z)\), the cubic transformation gives
\[
Y^2=X^3+6X^2+4(4-a)X+(4-a)^2,
\]
and direct Weierstrass invariant calculations yield
\(c_4=192(a-1)\), \(c_6=-864a^2\),
\(\Delta_E=16\operatorname{disc}(f_a)\). Thus the displayed formula for
\(j\) is correct, including \(j(0)=1728\) and \(j(1)=0\). The warning
against reducing this inseparable double-cover description in characteristic
two is essential and present.

## 4. Conductor, topology, and generalized Jacobian

The endpoint plane germ has four smooth branches with pair contact three.
Thus its local delta is \(6\cdot3=18\); total delta is thirty-six. On a
normalized branch the residue differential \(du/(4y^3)\) has pole order nine.
The conductor divisor on each branch is therefore \(9p+9q\), and
\(\omega_{\mathbf P^1}(9p+9q)=\mathcal O(16)\), in agreement with the
restriction of the complete-intersection dualizing sheaf.

Topologically over \(\mathbf C\), identifying four points at each of two
locations in four disjoint spheres lowers Euler characteristic from eight to
two. Connectedness and four fundamental component classes give
\((b_0,b_1,b_2)=(1,3,4)\). The bipartite incidence graph independently gives
\(b_1=8-6+1=3\). For the nodal marked comparison, the normalization contributes
genus sixteen and the graph contributes seventeen loops, giving
\(b_1=32+17=49\), \(b_2=2\), and Euler characteristic minus forty-six.

At each special endpoint the local units quotient has torus dimension three
and unipotent dimension fifteen. Globally, normalized-component rescalings
remove three of the six torus dimensions. In characteristic zero this gives
the noncanonical group decomposition
\[
\operatorname{Pic}^0(Z)\simeq\mathbf G_m^3\times\mathbf G_a^{30}.
\]
This agrees with the primary framework in the corrected version of
[Geisser, Theorems 1–3](https://arxiv.org/html/0704.0479v4). For the nodal
comparison the abelian quotient has dimension sixteen and the torus rank is
seventeen. No unconditional monotonicity of the individual dimensions follows
from these examples.

The full conductor degree seventy-two at \(Z\) and degree thirty-six for the
nodal marked comparison are also correct. Both have marked boundary degree
eighteen on \(C\); the difference comes from internal residual singularities.

## 5. The eight-component competitor

The explicit pair \((QL_1L_2,RL_3)\) has eight displayed reduced components
of degrees \(4,1,1,2,3,3,1,1\). The finite ideal equality and primality checks
were replayed independently and passed. Primality over \(\mathbf Q\) alone
would not suffice for geometric irreducibility; the contribution now supplies
the stronger geometric bridge on the \(\mathbb F_1\) normalization.
For the two plane sections, the coefficient pairs
\((v_0^2+v_1^2,v_0+v_1)\) and
\((v_0^2+5v_1^2,2v_0+3v_1)\) are coprime even over the algebraic closure.
They define actual smooth rational sections mapping birationally to the cubics.
Their displayed nondegenerate quadratic terms give their ordinary nodes.

Thus all eight normalized components are rational, and
\(\delta=33+8-1=40\). This valid competitor rules out unqualified maximality
of total delta in the full reduced proper \((4,4)\) locus containing \(C\).
It does not address a restricted comparison class with integral hypersurfaces
or prescribed component data.

## 6. Ordering and specialization: scope checks

The normalized cycle mass \(4m_C/(ab)\) is unchanged by taking powers of
both equations: regular-sequence local intersection multiplicity scales by
the same factor as the total degree. It is constant at one quarter on the
generically simple \((4,4)\) locus. It can detect the explicit collision at
\(a=4\), but cannot identify the original roots-of-unity arrangement.

The Chow parameter point retains the actual effective cycle; its Chow-group
class in \(\mathbf P^3\) retains only degree. The locus with coefficient at
least \(m\) along a fixed \(C\) is closed by projectivity of the addition map
from lower-degree cycles. These observations support a specialization
diagnostic, not a universal comparison of all complete intersections.

The binary-form GIT interpretation is correctly scoped to the abstract
normalization. A degree-eighteen divisor is semistable precisely when every
multiplicity is at most nine. The equal two-point divisor is the closed
strictly semistable orbit. This is the classical statement recalled in
[Alper–Isaev, section 5.2](https://sites.math.washington.edu/~jarod/papers/binary.pdf).
It does not put that orbit in every stable orbit closure, and the full
\(\mathrm{PGL}_2\) is not the fixed embedded-curve stabilizer.

The integral associated-graded calculation
\(\mathbf Z[u,\eta]/(4u^9\eta)\) is compatible with the principal initial
term over the domain \(\mathbf Z[u]\); its reduction modulo two differs from
the actual special-fiber graded algebra with relation \(\eta^4\). Thus the
base-change caveat is real. The derivative cannot be treated as a nonzero
degree-eighteen section after reduction. Finite-cover discriminants, global
curve conductors, and the primitive part of an integral determinant are
different objects throughout the notes.

## 7. Verification evidence and remaining questions

Independent replay on 2026-10-25 passed:

```sh
python3 research/computations/explore_ci_contact_deformations_2026_10_25.py
python3 research/computations/verify_ci_cycle_root_pencil_2026_10_25.py
/opt/homebrew/bin/M2 --script research/computations/explore_ci_residual_pencil_2026_10_25.m2
/opt/homebrew/bin/M2 --script research/computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2
```

The script outputs support finite identities, ideal calculations, and exact
ranks. The preceding geometric reconstructions supply the bridges separately.
They do not prove completeness of any proposed proximity profile.

Outstanding exploratory questions include topology strata inside a fixed
boundary fiber; a direct, globally verified generic residual example;
functorial retention of horizontal contact and arithmetic content; and which
leading-sheet moduli persist when both hypersurfaces move. These remain
research directions, with no expectation that one ordering must answer all
of them. No accepted mathematics or canonical frontier status changes.

## 8. Synthesis review

The [main notebook](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-geometry-notebookmd) was read after
assembly. Its comparison of mass, boundary, normalization, topology, and
nilpotent structure is consistent with the component calculations above.
The review strengthened the generic-residual paragraph from an expectation
to a new provisional deduction, using the actual very-ampleness/Bertini route.
The corresponding next experiment now asks for a directly computed exact
example, rather than suggesting that existence of the generic picture is
still unproved. The diagram and evidence qualifications were reconciled with
that change.

The synthesis correctly keeps the following limitations visible: the local
fourteen-dimensional fiber has not been classified; there is no calculated
extremum across all complete intersections; the auxiliary elliptic curve is
not an elliptic component or a universal invariant; normalization and
arithmetic normal filtrations need not commute with specialization; and the
degree-sixteen characteristic-two scheme is different from its degree-four
reduction. The lower-degree quadric/cubic comparison is used with its
independently audited provisional source status.

**Review outcome:** the stated elementary calculations, the explicit
deformation mechanisms, and the new general-pair geometric deduction pass
this independent mathematical scope review. The suggested extremality
principles and moduli packages remain exploratory ideas. Review status of
these notes is not canonical promotion or mathematical closure of an STCI
question.



---

## 2026-10-25-ci-cycle-valuative-audit.md

# Independent audit of the adaptive valuative continuation

Date: 2026-10-25. Reviewer: independent audit agent from the cycle-exploration team.
Status: reviewed local deductions and scope checks; exploratory research, with
no canonical promotion and no universal residual-component theorem.

The reviewer followed [the research index](../INDEX.md) and the contribution
protocol. The fixed-curve conormal and prescribed degeneration facts in
[R0020](../results/quartic_conormal_characteristic_jump.md) and
[R0021](../results/quartic_mu4_degeneration.md) remain accepted premises; their
proofs were not rerun. This review concerns the new
[adaptive notebook](CI_CYCLE_ADAPTIVE_FRONTIER.md#2026-10-25-ci-cycle-adaptive-valuative-notebookmd),
[generic multiplicity note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-valuative-multiplicitymd),
[contact-cycle note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-valuative-contact-cyclemd), and
[endpoint valuation note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-endpoint-valuationsmd).

**Outcome.** The parameter-ideal refinement is correct and materially useful:
complete ambient valuative information does recover the generic multiplicity
of an actual proper two-equation intersection along the marked curve. The
counterexample using a parameter ideal and its nonparameter integral closure
does not disprove that restricted assertion. The point-contact criteria,
weighted-cluster formula, endpoint calculations, and distinctions among
valuation centers also pass the checks below. None establishes the strict
global inequality for every homogeneous pair.

## 1. The exact class and the unproved quantifier

Let \(k\) be algebraically closed of characteristic zero, let the embedded
quartic be the specified \(C\), and let \(W=V(A_d,B_e)\) be a proper
hypersurface intersection containing \(C\) in its reduced support. The absence
of a common surface component makes the equations a regular sequence; the
curve is pure and Cohen–Macaulay. Its fundamental cycle has the form

\[
[W]=m_C[C]+R,\qquad de=4m_C+\deg R.
\]

Therefore \(R\ne0\) is equivalent to \(m_C<de/4\). This is a reformulation,
not a proof of strictness. The new notebook correctly permits a different
valuation, cluster, point, or comparison ideal for each pair. Its eventual
research target has the form

\[
\forall W\quad\exists\text{ suitable data certifying }m_C<de/4.
\]

What is established locally is weaker and different: for each given pair,
finite adapted data determine \(m_C\). Exact reconstruction does not show
that every reconstructed number is strictly below its global degree budget.
The notes keep this missing implication explicit. If \(de\) is not divisible
by four, integrality already forces strictness; the equality boundary is the
substantive unresolved case.

## 2. Why parameter ideals retain colength valuatively

Set \(S=\mathcal O_{\mathbf P^3,\eta_C}\), with maximal ideal
\(\mathfrak m\), residue field \(K=k(C)\), and \(J=(A,B)S\).
The ring is regular local of dimension two and \(J\) is
\(\mathfrak m\)-primary. It is a parameter ideal, generated by a regular
sequence. Its generic transverse length is the coefficient \(m_C\).

One direct reconstruction of the length–multiplicity bridge uses the
associated graded ring of a regular-sequence ideal:

\[
\operatorname{gr}_J S\simeq(S/J)[T_1,T_2].
\]

Consequently

\[
\ell(S/J^n)=\ell(S/J)\binom{n+1}{2},
\qquad e(J)=\ell(S/J)=m_C.
\]

Multiplicity is unchanged on passing to the integral closure. These standard
facts and the general multiplicity framework are recorded in
[Huneke–Swanson, Proposition 11.1.10\(2\) and Proposition 11.2.1](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).

Thus equal integral closures of two parameter ideals imply equal colengths.
The familiar ideals \((x^2,y^2)\) and \((x,y)^2\) have colengths four and
three, but both have multiplicity four; only the first is a parameter ideal.
Their comparison warns against arbitrary-ideal colength reconstruction. It
does not obstruct multiplicity reconstruction for the actual CI class.
Neither statement recovers every feature of the finite Artinian algebra.

Completion preserves the finite length. An identification
\(\widehat S\simeq K[[x,y]]\) uses a coefficient field and normal parameters;
it is a computational choice, not a canonical global trivialization.
In particular, \(K\) need not be algebraically closed.

## 3. The finite data must contain the valuations themselves

In this setting a finite full Rees list gives

\[
\overline{J^n}
=\{h\in S:v_i(h)\ge n v_i(J)\text{ for every }i\}.
\]

Here each \(v_i\) is a specified normalized divisorial valuation, together
with its threshold. An unlabeled collection of integers is not equivalent
data. Finiteness and the simultaneous recovery of the integral closures of
all powers are the primary facts described in
[Swanson, *Rees Valuations*, Definition 1.1 and Theorem 2.1](https://www.math.purdue.edu/~iswanso/reesvals.pdf).

Knowing the full ideal closure and then its multiplicity gives \(m_C\).
The finite list depends on \(J\); no uniform predetermined list or depth
bound follows. The existence of a finite description is also different from
having computed and certified it for a given input.

The fixed-coordinate example in the notes checks this distinction sharply.
For \(J_N=(y-x^2,x^N)\), all positive monomial valuations in \(x,y\) give
\(\min\{v(y),2v(x)\}\), independent of \(N\ge2\). In the adapted parameters
\(z=y-x^2,x\), the ideal is the complete ideal \((z,x^N)\), with length
\(N\) and one Rees valuation of weights \((N,1)\) on \((z,x)\). A nonlinear
direction, rather than more weights in the original chart, exposes the
missing contact.

## 4. Full clusters, weak orders, and residue degrees

For \(I=\overline J\), let \(r_P\) be the order of its weak transform at
each infinitely near base point and let \(d_P=[\kappa(P):K]\). The finite
point basis includes the original point. On a principalizing model,

\[
e(I)=\sum_Pd_Pr_P^2=-D^2,
\qquad I\mathcal O_X=\mathcal O_X(-D).
\]

The square-sum formula follows by applying the Hoskin–Deligne length formula
to the complete powers \(I^n\), whose weak orders are \(nr_P\), and comparing
quadratic leading coefficients. The required residue-weighted length formula
is [Huneke–Swanson, Theorem 14.5.4](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).
The displayed square uses the orthogonal total-exceptional-transform basis.
It is not the unweighted sum of squares of coefficients on strict exceptional
curves, nor the sum of squares of raw divisorial values.

The nonsplit example was reconstructed independently. Over \(K=k(t)\), put

\[
J=(y^2-tx^2,x^n),\qquad n\ge3.
\]

The quotient is free of rank two over \(K[[x]]/(x^n)\), so its length is
\(2n\). The first point has order two. In the chart \(y=xv\), the weak ideal
is \((v^2-t,x^{n-2})\). Its remaining chain has \(n-2\) order-one points
over \(K(\sqrt t)\). The energy is therefore
\(4+2(n-2)=2n\). Counting this degree-two chain only once without its field
degree gives the wrong answer.

The proposed closure is also correct:

\[
\overline J=(y^2-tx^2,x^n,x^{n-1}y).
\]

The added generator has square in \(J^2\). The last divisorial valuation has
\(v(x)=v(y)=1\), \(v(y^2-tx^2)=n\), and its threshold-\(n\) ideal is exactly
the displayed ideal: after reduction modulo \(y^2-tx^2\), the leading
coefficients \(1,\sqrt t\) cannot cancel over \(K\). Its colength is \(2n-1\),
while its multiplicity is \(2n\). This example supports, rather than weakens,
the parameter-ideal distinction.

## 5. One-sided bounds have to point the right way

A partial cluster omits nonnegative terms from the energy, so it gives a
lower bound on \(m_C\). Similarly, a subset of the valuation inequalities
defines an ideal \(L\supset\overline J\), yielding \(e(L)\le m_C\), whenever
the compared ideals are maximal-ideal-primary. These estimates alone cannot
prove a positive residual degree.

Conversely, a certified maximal-ideal-primary ideal
\(H\subset\overline J\) gives \(m_C\le e(H)\). If a computable adapted
parameter ideal \(H=(u^r,v^s)\) satisfies that containment and \(4rs<de\), it
does certify a residual component. This is a valid format for a pair-dependent
certificate. Finding such an \(H\), or any other upper bound, for every
global pair is not a consequence of the local criterion.

## 6. Flag valuations: center, residue field, and scalarization

Let \(B=\operatorname{Bl}_C\mathbf P^3\), let \(E\) be its exceptional
surface, and let \(E_p\) be its fiber over \(p\in C\). The partial flag

\[
B\supset E\supset E_p
\]

defines a rank-two composite valuation with final residue field
\(k(E_p)\simeq k(z)\). In a suitable splitting its value group is
\(\mathbf Z^2\) with lexicographic order: first normal order, then the
fiber-divisor order of the leading residue. Refining by a point of \(E_p\)
gives rank three and final residue field \(k\).

The partial flag has center \(p\) on the original threefold. It is not
centered on \(S=\mathcal O_{\mathbf P^3,\eta_C}\): a curve parameter at
\(p\) and its inverse are units in \(S\), whereas the flag gives them
opposite nonzero values. Generic Rees valuations and point-centered flags
cannot be substituted for one another without a bridge.

The warning about real linear combinations is necessary. In local regular
parameters \((u,x,y)\), with \(C=(x,y)\), the partial flag has
\(\nu(u)=(0,1)\), \(\nu(x)=\nu(y)=(1,0)\). For

\[
f=u^Nx+y^2,\qquad g=-u^Nx,
\]

one has \(\nu(f)=\nu(g)=(1,N)\) but \(\nu(f+g)=(2,0)\).
For positive real \(\alpha,\beta\) and \(N>\alpha/\beta\), assigning
\(w(h)=\alpha\nu_1(h)+\beta\nu_2(h)\) violates the valuation inequality:
\(w(f+g)=2\alpha<\alpha+N\beta\). Thus it is not generally a valuation.

Positive monomial weights on the actual regular parameters do define genuine
valuations, by taking a minimum over **all** monomials. This is a different
construction. Moreover, on arbitrary \(K[[x]]\) the coefficients can have
unbounded poles: the series
\(\sum_{n\ge1}u^{-n^2}x^n\) has weighted terms tending to minus infinity
whenever both \(u\)- and \(x\)-weights are positive. A series domain and pole
control must therefore accompany such a construction. The new notebooks
state both restrictions correctly.

## 7. Point excess and contact cycles

Multiplicity associativity gives, at \(p\in C\),

\[
e_p(W)=m_C+\sum_{D\ni p}m_De_p(D).
\]

The smoothness of \(C\) supplies its multiplicity one. A proper projective
complete-intersection curve is connected, including in the nonreduced case;
the displayed Koszul/cohomology argument proves this in the present setup.
Hence residual components, if present, meet \(C\). Therefore

\[
R\ne0\iff\exists p\in C:e_p(W)>m_C.
\]

This equivalence is correct. A sole-support multiple structure has
\(e_p(W)=m_C\) at every point, so nilpotent behavior does not produce a
false positive.

For each normalized residual branch \(r\), the order of the pulled back
ideal \(I_C\) is a well-defined nonnegative integer. Summing its positive
orders with cycle multiplicities gives the contact divisor
\(B_C^{\mathrm{val}}(R)\). The normalization map lifts to the blowup, and
Cartier intersection there gives

\[
B_C^{\mathrm{val}}(R)=\pi_*(E\cdot\widetilde R).
\]

This uses the strict residual cycle, not the full inverse image. It vanishes
exactly when \(R=0\) in this connected setup. If
\(M_C(W)=\sum_p(e_p(W)-m_C)[p]\), each branch contributes at least its
ordinary multiplicity to its ideal contact, so \(M_C(W)\le B_C^{\mathrm{val}}(R)\).
The cubic-generation argument also correctly gives
\(\deg B_C^{\mathrm{val}}(R)\le3\deg R\): a general cubic through \(C\)
avoiding all residual components has a divisor on each normalization
dominating the ideal-contact divisor.

Computing \(R\) and then its contact cycle already detects the residual.
The research challenge remains estimating a positive witness from the
equations and global constraints without presupposing such a component.

## 8. Contact, conductor, and the four-line counterexample

The local CI

\[
k[x,y,z]/(xy-xz,xy-yz)
\]

is the reduced union of the three coordinate axes and the diagonal line.
Its normalization has four polynomial components. At the vertex the image
has dimension one in degree zero and dimension three in degree one; it is
all four components in degrees at least two. The quadrics \(xy\),
\(x^2-xy\), \(y^2-xy\), \(z^2-xy\) exhibit the latter assertion directly.
The conductor order on every normalized line is two and total delta is four.

For the marked \(x\)-axis, the three other branches each have order one on
\((y,z)\), giving valuative contact three. Their union intersects the marked
axis in length two: no linear form vanishes on all three residual directions,
while \(x^2-xy\) restricts to \(x^2\). The first-normal determinant is also
\(x^2\). Thus pairwise branch-contact sums, actual residual-scheme
intersection, and conductor boundary cannot be identified in arbitrary
nonplanar CI germs. Their coincidence at the special quartic bouquet is
properly kept in its smooth-surface scope.

## 9. Endpoint calculations and actual transforms

For the established endpoint equation
\(f=Y\prod_{j=1}^3(Y-c_ju^3)\), distinct nonzero \(c_j\), positive monomial
weights give

\[
v_{\alpha,\beta}(f)=\beta+3\min\{\beta,3\alpha\}.
\]

At the wall \(\beta=3\alpha\), distinct monomials give a nonzero initial
polynomial, so equal weights cause no cancellation. Three successive
point blowups produce the rays \((1,1),(1,2),(1,3)\) and then the four
separated directions. The surface flag \(S\supset C\supset p\) has value
\((1,9)\); it is a different flag from the ambient partial flag above.

The partial-splitting equation has value
\(\beta+\min\{3\beta,\alpha\}\), surface-flag value \((1,1)\), and ordinary
point multiplicity two. Its new wall can record curvature relative to a
chosen axis rather than common branch tangency; the endpoint note correctly
identifies that limitation.

In the ambient \(Y\)-chart, \(Y=t,X=t\xi\), the full flag gives
\(v(X)=(1,0,1)\), \(v(f)=(1,9,0)\). The total transform is

\[
t\bigl(\xi,t^3+4u^3t^2+6u^6t+4u^9\bigr).
\]

Removing the exceptional factor by saturation gives the strict residual
curve. Its intersection with \(E\) has ideal \((\xi,u^9)\) and length nine.
This checks both the contact computation and the warning against counting
exceptional components as residual curves downstairs.

## 10. Review boundary

The adaptive continuation's mathematical statements pass this review under
their stated hypotheses. No new script is needed for the elementary local
counterexamples and inequalities reconstructed here. The earlier cycle
exploration's finite scripts remain evidence for their own explicit pairs;
they do not establish the all-pairs claim discussed in this continuation.

What remains open is the global step: obtain, for every actual homogeneous
pair, a strict upper bound \(m_C<de/4\), or an independently justified
positive point/contact witness. There is no claimed uniform valuation list,
degree bound, finite exhaustive search, or proof that all formal local
examples globalize. Those limitations are the substantive continuation
boundary, not defects in the valid local multiplicity bridge.



---

## 2026-10-25-ci-cycle-fixed-boundary-node-smoothing.md

# Five residual nodes can move independently to first order at fixed boundary

Date: 2026-10-25. Status: exploratory exact tangent calculation with independent reconstruction; no canonical promotion. The [independent review](#2026-10-25-ci-cycle-fixed-boundary-node-smoothing-auditmd) records the finite calculation and its local-deformation interpretation separately. The starting point is the line-plus-degree-eleven degeneration in the [line-degeneration note](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-line-degenerationmd). The main question is whether a fixed attachment divisor on \(C\) can hide changes in the genus and component structure of the residual curve.

**Finite result.** At this actual quartic pencil, the full boundary map has projective differential rank 18, and the map from its 14-dimensional fixed-boundary tangent space to the five residual node parameters is surjective. Its kernel has dimension 9. Thus retaining the exact boundary to first order does not force any linear relation among the five node smoothing parameters. A separate formal interpretation is given below; no explicit polynomial arc with exactly constant boundary has been constructed by this calculation.

## 1. The actual point and the two separate boundaries

Use the homogeneous forms \(F,G,Q,A,D_3,H_0,H_1\) from the [smooth residual benchmark](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-smooth-residual-examplemd), but take coefficients 1,1:

\[
f=F+QH_0+x_0A,\qquad
g=G+QH_1+x_3D_3.                             \tag{1}
\]

The residual cycle is \(L+E\), where

\[
L=V(x_0+x_1,x_2+x_3),\qquad
\deg E=11,\quad g(E)=12.
\]

The companion exact rational computation verifies that \(E\) is smooth and geometrically integral, \(L\cap E\) consists of five reduced points, \(C\cap E\) has seventeen reduced points, and \(C\cap L\) is one further reduced point, with no triple intersection. In particular the five nodes of \(L\cup E\) lie off \(C\). These are different from the eighteen attachment nodes of the full curve along \(C\).

The boundary-divisor map is

\[
\beta:U\subset\operatorname{Gr}(2,V)
\longrightarrow\mathbf P H^0(C,\mathcal O_{\mathbf P^1}(18)),
\qquad V=H^0(\mathbf P^3,I_C(4)),\quad \dim V=18.
\]

It is regular at this pencil because its first-normal determinant is nonzero. The determinant has degree 18 and is squarefree, so the eighteen attachments are simple. In this note, *fixed boundary* means the fiber of this actual map, not merely constant boundary degree. It fixes an effective divisor on the marked \(C\).

The five residual nodes are encoded on the chart \(x_3=1\) of \(L\) by

\[
[x_0:x_1:x_2:x_3]=[-r:r:-1:1],
\]

\[
P(r)=4r^5-2r^4+9r^3+2r^2+3r+2.               \tag{2}
\]

The finite étale algebra

\[
\mathcal A=\mathbf Q[r]/(P)
\]

records all five nodes without choosing their roots. The point \(L\cap C\) is \(r=-1\), and \(P(-1)=-14\), so none of the five nodes is that attachment point.

## 2. A node smoothing functional obtained from the actual gradients

Take normal coordinates \(n_0=x_0+x_1\), \(n_1=x_2+x_3\) along \(L\). On \(x_3=1\), the coefficients of \(n_1\) in the two first-normal parts are

\[
F_1(r)=-r(r+1)(r+2),\qquad
G_1(r)=-4r^3+2r^2-9r-1.
\]

The polynomial \(F_1\) is a unit in \(\mathcal A\): \(P\) is relatively prime to each of \(r,r+1,r+2\). Thus the first equation is a smooth carrier at every one of the five nodes. The actual gradients satisfy

\[
F_1\,\partial_jg-G_1\,\partial_jf=0
\quad\text{in }\mathcal A\quad(j=0,1,2,3).     \tag{3}
\]

For a global perturbation pair \(h,k\in V\), eliminating the first carrier equation shows that the first-order constant term in the node equation is

\[
k|_L-\frac{G_1}{F_1}h|_L.
\]

Equivalently, multiply by the invertible factor \(F_1\) and use the scaled class

\[
S(h,k)=F_1k|_L-G_1h|_L\pmod P\quad\in\mathcal A. \tag{4}
\]

This class is a node smoothing parameter up to multiplication by a nonzero factor at each geometric node. The scale cannot change a surjectivity statement. The script checks equation (3) from the actual homogeneous derivatives and separately verifies that the normal determinant along \(L\) equals \(-(r+1)P(r)\).

## 3. The source really consists of global homogeneous quartics

For a degree-four monomial \(x_0^{m_0}x_1^{m_1}x_2^{m_2}x_3^{m_3}\), restriction to \(C\) has parameter weight

\[
w=m_1+3m_2+4m_3.
\]

Group the thirty-five monomials by this weight. In each nonempty group, subtract one fixed reference monomial from the others. This gives an integral 18-element basis of the actual restriction kernel \(V\).

On \(x_0=1\), put \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\). A monomial's first-normal part is

\[
m_3u^{w-4}X+m_2u^{w-3}Y.
\]

The formula is used on each monomial difference. Write these two coefficients as \(\sigma_h=(A_h,B_h)\). The affine differential of the determinant at (1) is

\[
D(h,k)=\det(\sigma_h,\sigma_g)
       +\det(\sigma_f,\sigma_k)
\in H^0(\mathcal O_{\mathbf P^1}(18)).         \tag{5}
\]

Its target is represented by nineteen coefficients in \(u\). The node functional (4) is represented by five coefficients in the basis \(1,r,r^2,r^3,r^4\) of \(\mathcal A\). The combined matrix therefore has 24 rows and 36 columns over \(\mathbf Q\).

The [standard-library exact verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py) constructs these actual source forms, the carrier functional, and both matrices. It does not replace global sections by arbitrary rational-function-valued symbols.

## 4. The exact ranks and explicit tangent witnesses

Exact Gaussian elimination over \(\mathbf Q\) gives

\[
\boxed{\operatorname{rank}D=19,\qquad
       \operatorname{rank}S=5,\qquad
       \operatorname{rank}(D,S)=24.}          \tag{6}
\]

The final equality implies

\[
\operatorname{rank}\bigl(S|_{\ker D}\bigr)=24-19=5.
\]

The calculation also solves explicitly for five rational source vectors \(v_0,\ldots,v_4\in V^2\) satisfying

\[
D(v_i)=0,\qquad S(v_i)=r^i\pmod P
\quad(i=0,\ldots,4).                         \tag{7}
\]

Their 36 source coefficients are recorded in the [JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json), together with the global monomial basis, polynomial (2), matrix pivot columns, and all checked ranks. The script verifies every equality in (7) exactly. These are actual homogeneous first-order perturbations with zero affine boundary derivative.

The nodes need not be individually rational over \(\mathbf Q\). Equation(7) spans their étale algebra over \(\mathbf Q\). After extending to an algebraically closed field and splitting \(P\), evaluation identifies \(\mathcal A\otimes k\) with \(k^5\), so the five geometric node parameters are independent. Selecting only one geometric node may require coefficients in a splitting field; no assertion that all nodes are rational is made.

## 5. Passing from ordered equations to the Grassmannian

The source \(V^2\) has dimension 36, while the pencil space has dimension 32. Infinitesimal changes of basis of \(f,g\) form the four-dimensional \(\operatorname{GL}_2\) gauge space. At every node both \(f\) and \(g\) vanish, so all four gauge directions have zero node class.

Their boundary derivatives are scalar multiples of the base determinant; the trace directions span that scalar line. A direction whose projective boundary derivative vanishes can therefore be modified by a gauge direction to make its affine boundary derivative exactly zero, without changing its node smoothing class. Consequently (6) gives the intrinsic pencil-space statement

\[
\operatorname{rank}d\beta=18,\qquad
\dim\ker d\beta=32-18=14,
\]

\[
\operatorname{rank}\bigl(S|_{\ker d\beta}\bigr)=5,
\qquad \dim(\ker d\beta\cap\ker S)=9.          \tag{8}
\]

The projective scaling issue does not remove one of the node parameters or manufacture an extra smoothing direction.

## 6. Formal interpretation, kept separate from the finite matrix result

There is a useful standard local consequence after extending scalars to split and mark the five nodes. The parameter space of pencils is smooth, and the surjective boundary differential makes the completed fixed-boundary fiber a smooth formal space of dimension 14.

For a split node in a flat family, [Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX) gives a completed equation \(xy-\tau_i=0\), with \(\tau_i\) a function of the formal base parameters. Its first differential is the node class (4), up to a unit. The étale local counterpart is [Stacks, Lemma 53.21.1](https://stacks.math.columbia.edu/tag/0CBY).

On the completed fixed-boundary fiber, the five linear forms \(d\tau_i\) are independent by (8). Formal coordinates can therefore be chosen so that its complete local ring is

\[
k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].     \tag{9}
\]

In this formal sense the five residual nodes can be smoothed independently while the boundary divisor is held exactly fixed. This conclusion uses the standard node local form and the formal inverse-function argument in addition to the finite rank computation.

The étale node charts also give a local algebraic existence interpretation. After a common étale base change that labels the nodes, the five node parameters are regular functions. The joint map \((\beta,\tau_1,\ldots,\tau_5)\) has surjective differential, so its restriction to the fixed-boundary fiber maps smoothly to \(\mathbf A^5\) near the marked point. A chosen one-parameter pattern \(\tau_i=c_i t\) therefore lifts locally after an étale change of the one-parameter base; a zero \(c_i\) retains that node, and a nonzero \(c_i\) smooths it in the generic fiber. This is an existence statement for local algebraic families, derived from smoothness and the node charts. It does not display their coefficients in the original global quartic chart.

No explicit polynomial or rational one-parameter path in the global coefficient space is supplied here. In particular, the five tangent pairs in (7) preserve the boundary to first order; simply writing \(f+th,g+tk\) need not preserve it at higher orders. Constructing such a path, or displaying the recursively corrected coefficient series, remains a separate experiment. Formal node charts likewise do not give a new uniform statement for arbitrary complete intersections.

## 7. The geometric picture suggested by the calculation

The residual \(L\cup E\) has

\[
p_a(L\cup E)=0+12+5-1=16.
\]

Its dual graph has two vertices joined by five edges, so four units of arithmetic genus lie in graph cycles. Smoothing all five connecting nodes would combine the components and turn those graph cycles into four additional units of normalization genus, giving the genus 16 smooth residual picture.

The rank calculation shows that these five node directions survive the fixed-boundary constraint. The attachment divisor records where the residual meets \(C\); it does not determine how much genus resides in the residual normalization or in gluing away from \(C\). This is a concrete organizing structure for the notebook: the 14-dimensional boundary fiber has five independent residual-node directions and nine further tangent directions invisible to both diagnostics.

For partial smoothing over a splitting field, the usual graph picture predicts that smoothing at least one connecting node joins the two components, while the other unsmoothed bridges become self-nodes. One should distinguish that formal/local picture from an explicitly computed global algebraic subfamily. The strongest directly reproduced statement remains the exact joint rank and its tangent witnesses.

The next focused experiment is to lift one tangent witness through higher orders under the exact equation \(\beta=\beta_0\), then compute the residual normalization in a concrete fiber. The result would make visible what the boundary map presently hides. No fixed scalar proximity measure is required to formulate this experiment.

## Reproducibility and scope

```sh
python3 research/computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py
```

The script uses only Python's standard library and finishes in a fraction of a second. It checks that \(P\) is squarefree, the carrier derivative is invertible, the gradient-dependence identities hold at the node algebra, the base boundary is degree 18 and squarefree, and all five explicit rational tangent pairs satisfy (7). A separate agent independently rebuilt the global basis and both maps in a scratch computation, obtaining the same ranks 19,5,24 and the same Grassmannian interpretation.

The geometry of \(L,E\) and their intersections is supplied by the [companion exact line-degeneration computation](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-line-degenerationmd) and its [independent audit](#2026-10-25-ci-cycle-line-degeneration-auditmd); this script does not repeat that projective smoothness calculation. The formal interpretation has its additional local-deformation input stated explicitly. No accepted result, proof, or canonical frontier record changes.



---

## 2026-10-25-ci-cycle-fixed-boundary-node-smoothing-audit.md

# Independent reconstruction of the fixed-boundary node-smoothing calculation

Date: 2026-10-26. Reviewer: independent reconstruction worker in the cycle-notebook team. Status: reviewed finite calculation and its stated formal-local consequence; unpromoted research evidence. The filename retains the October 25 investigation date. This review completes the current experiment and proposes no additional work.

**Outcome.** The [investigation note](#2026-10-25-ci-cycle-fixed-boundary-node-smoothingmd) correctly gives exact affine ranks 19,5,24 from actual global quartics. On the Grassmannian, the fixed-boundary tangent space has dimension 14 and maps onto all five residual-node smoothing parameters, with kernel dimension 9. After splitting and marking the geometric nodes, the stated completed local coordinate form is justified by the standard node-family theorem and the formal inverse-function argument. This is distinct from an explicitly computed coefficient arc, which the note correctly says has not been supplied.

## 1. The independently reconstructed source and maps

The reviewed point is the actual homogeneous pair

\[
f=F+QH_0+x_0A,\qquad g=G+QH_1+x_3D_3,
\]

with the forms specified in the [smooth-residual benchmark](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-smooth-residual-examplemd). The [line-degeneration calculation](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-line-degenerationmd) and its [independent audit](#2026-10-25-ci-cycle-line-degeneration-auditmd) supply the starting geometry: the residual is \(L\cup E\), with \(E\) smooth of degree 11 and genus 12, and exactly five reduced ordinary nodes \(L\cap E\) away from \(C\). The current rank calculation does not independently recertify projective smoothness of \(E\).

Before reading the durable verifier, the reviewer independently rebuilt its ingredients in a standard-library rational computation:

- all degree-four homogeneous monomials, grouped by weight \(m_1+3m_2+4m_3\);
- the 18-element actual global restriction-kernel basis, obtained by monomial differences within those groups;
- the two first-normal rows along \(C\), by differentiating the actual homogeneous polynomials;
- all 36 columns of the boundary differential;
- all 36 columns of the five-node smoothing map in the finite algebra below.

No arbitrary rational-function coefficients were introduced into the global quartic source.

On \(L\), use \([-r:r:-1:1]\) and

\[
P(r)=4r^5-2r^4+9r^3+2r^2+3r+2,
\qquad \mathcal A=\mathbf Q[r]/(P).
\]

The actual derivative in the \(x_2\) direction is

\[
F_1=-r(r+1)(r+2),\qquad
G_1=-4r^3+2r^2-9r-1.
\]

The reviewer checked that \(F_1\) is a unit modulo \(P\). Thus eliminating the smooth first carrier equation gives the first-order node class

\[
\delta g-(G_1/F_1)\delta f,
\]

and the scaled class

\[
S=F_1\delta g-G_1\delta f\pmod P
\]

has the same rank. The scale is an invertible factor at every geometric node. The actual gradient proportionality modulo \(P\) is checked in the durable verifier, not presumed from a numerical rank deficiency at a sampled root.

The independent exact Gaussian elimination returned

\[
\operatorname{rank}D=19,\qquad
\operatorname{rank}S=5,\qquad
\operatorname{rank}(D,S)=24.
\]

The reviewer also explicitly checked that every one of the 36 untruncated boundary-derivative polynomials has degree at most 18 before extraction of its nineteen coefficient rows. Thus the rank does not omit a higher-degree boundary constraint through coefficient truncation. The durable verifier now also asserts this bound before coefficient extraction and passed its replay.

## 2. Review and replay of the durable evidence

After that independent reconstruction, the reviewer read and replayed the [durable verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py) and read its [JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json). The verifier passed. Its ranks agree with the independent reconstruction.

The durable file additionally checks:

- squarefreeness of \(P\) and invertibility of \(F_1\) in \(\mathcal A\);
- the actual four ambient gradient-proportionality identities;
- the normal determinant along \(L\), equal to \(-(r+1)P(r)\);
- nonzero, degree 18, squarefree boundary determinant along \(C\);
- actual restriction to \(C\) of every source form;
- five explicitly solved rational source vectors whose boundary derivative is zero and whose scaled node images are \(1,r,r^2,r^3,r^4\).

The 36 coefficients of each witness are in the JSON, in its stated global basis order. Their meaning is first-order: writing the corresponding linear coefficient perturbations does not by itself keep the boundary fixed to every higher order.

The node algebra need not split over \(\mathbf Q\). Surjectivity onto its five-dimensional rational vector space becomes independent control of the five geometric nodes after extension to a splitting field. This does not assert that those five nodes are individually rational.

## 3. The Grassmannian and scalar-boundary issue

The ordered source \(V^2\) has dimension 36. Infinitesimal recombination of its two independent equations supplies four gauge directions. All four have node class zero because both original equations vanish at the nodes. Their boundary derivatives are scalar multiples of the base determinant, with the trace directions spanning that scalar line.

It follows that quotienting by these gauge directions and projectivizing the determinant target gives

\[
\operatorname{rank}d\beta=18,
\qquad \dim\ker d\beta=32-18=14.
\]

Any direction with zero projective boundary derivative may be adjusted by a gauge direction to have zero affine boundary derivative, without changing its node image. Therefore the joint rank 24 establishes

\[
\operatorname{rank}(S|_{\ker d\beta})=5,
\qquad \dim(\ker d\beta\cap\ker S)=9.
\]

There is no lost smoothing direction caused by passing from ordered equations to pencils, and no extra direction created by counting a scalar determinant variation as a movement of the effective divisor.

## 4. The formal claim and its precise extra input

Take an algebraically closed characteristic-zero field \(k\) containing the node residue fields. Near the reviewed pencil, the proper-complete-intersection locus in \(\operatorname{Gr}(2,18)\) is smooth of dimension 32, and the boundary map is regular because its determinant is nonzero.

The 18 independent projective boundary-coordinate differentials can be included in a regular formal coordinate system of the source. Equivalently, the formal inverse-function argument identifies the completed local ring of the fixed-boundary fiber with \(k[[z_1,\ldots,z_{14}]]\). This is a statement about the actual fiber of the divisor map, not only the linear kernel.

For each split node, [Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX) applies to the flat universal complete-intersection family and gives a completed equation \(xy-\tau_i\). Its base parameter has differential equal to the node class calculated above, up to a unit. Because the five restricted differentials are independent, they extend to a basis of the cotangent space of that 14-dimensional regular complete local ring. Applying the formal inverse-function argument again gives

\[
\widehat{\mathcal O}_{\beta^{-1}(\beta_0),[f,g]}
\simeq k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].
\]

The isomorphism is noncanonical and is asserted after the stated field extension and marking of the nodes. It legitimately expresses independent formal smoothing at exactly fixed boundary. It uses the flat node-family theorem in addition to the finite matrix calculation; the matrix alone would not state a higher-order lifting theorem.

The [étale local node-family theorem, Stacks Lemma 53.21.1](https://stacks.math.columbia.edu/tag/0CBY), supplies the algebraic local counterparts after an étale neighborhood. Together with the independent differentials, one can choose a smooth local map to the five smoothing parameters and obtain suitable algebraic curves locally in that neighborhood. In particular, a prescribed local curve \(\tau_i=c_i t\) in the five-parameter target lifts after an étale base change of that curve; nonzero \(c_i\) smooth the corresponding node generically, while zero \(c_i\) retain it in its node chart. This is an existence interpretation; it does not turn the displayed rational tangent vectors into a polynomial or rational coefficient arc on the original global parameter space. No such explicit arc has been computed here.

## 5. Scope and conclusion of review

The exact finite result, the scalar quotient, and the completed-local consequence pass independent review for this specified pencil. They explain how a fixed degree 18 attachment divisor can coexist with five independent residual-node smoothing directions. The reviewed calculation has no unrestricted complete-intersection claim and no implication that one uniform proximity invariant controls every pair.

The starting line-plus-degree-eleven geometry remains supported by its separate computation and audit. No canonical result, inherited proof, or accepted frontier record is changed. The current experiment is finished; no continuation experiment is begun by this audit.



---

## 2026-10-25-ci-cycle-line-degeneration-audit.md

# Independent audit of the residual ruling-line degeneration

Date: 2026-10-25. Reviewer: independent cycle-notebook audit agent.
Status: reviewed exact example and local deformation deductions; exploratory
and not canonically promoted.

The reviewer followed [the research index](../INDEX.md). This audit concerns
the new [line-degeneration note](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-line-degenerationmd);
the original prescribed \(\mu_4\) family in
[R0021](../results/quartic_mu4_degeneration.md) is an accepted reference and
its proof was not rerun. The smooth member at parameters \((2,3)\) has its
separate [exact audit](#2026-10-25-ci-cycle-smooth-residual-auditmd).

**Outcome.** The checked member at \((1,1)\) is exactly the union of the marked
quartic \(C\), a ruling line \(L\), and a smooth geometrically integral curve
\(E\) of degree eleven and genus twelve. All twenty-three pairwise attachment
points are ordinary nodes and there are no triple points. The five residual
nodes have the same nonzero smoothing direction in the specified
two-parameter family. Locally their smoothing parameters are unit multiples
of \(ab-1\). Their product has order five, with the discriminant qualification
in section 5 below.

## 1. The exact pair and its geometric data

Use the actual forms \(F,G,Q,A,D_3,H_0,H_1\) displayed in the contribution
note, and
\[
f_a=F+QH_0+a x_0A,\qquad
g_b=G+QH_1+b x_3D_3.
\]
At \((a,b)=(1,1)\), set
\[
J=(f_1,g_1),\quad I_D=\operatorname{sat}(J:I_C),\quad
I_L=(x_0+x_1,x_2+x_3),\quad
I_E=\operatorname{sat}(I_D:I_L).
\]

A separate rational Macaulay2 calculation independently reconstructed:

- \(\operatorname{codim}J=2\), \(\deg D=12\), and \(P_D(n)=12n-15\).
- \(I_D=I_L\cap I_E\) and \(J=I_C\cap I_D\), as exact ideals.
- \(\deg E=11\) and \(P_E(n)=11n-11\), hence arithmetic genus twelve.
- The saturated projective Jacobian singular ideal of \(E\) is the unit ideal.
- \(H^0(E,\mathcal O_E)=\mathbf Q^1\).
- \(L\cap E\) has five reduced geometric points, \(C\cap E\) has seventeen,
  and \(C\cap L\) has one; their triple intersection is empty.

The independent suite returned
\[
(\deg E,P_E,\deg(L\cap E),\deg(C\cap E),H^0(\mathcal O_E))
=(11,11n-11,5,17,\mathbf Q).
\]
The durable
[Macaulay2 verifier](../computations/ci_cycle_line_degeneration_2026_10_25.m2)
was then replayed and passed. The geometric smoothness plus proper
global-section argument used in the preceding smooth-residual audit proves
geometric connectedness and hence geometric integrality of \(E\). This is
stronger than primality over \(\mathbf Q\).

Reduced length-one intersections of two smooth branches give distinct tangent
directions. Thus these are transverse nodes. There are exactly five nodes
of \(D=L\cup E\), and exactly twenty-three nodes of \(C\cup L\cup E\).
The absence of triples is necessary for both counts and was tested separately.

## 2. Reconstructing the moving line

On \(Q\), use Segre coordinates
\[
(x_0,x_1,x_2,x_3)=(\rho c,\rho d,\sigma c,\sigma d),\qquad
K_C=\rho d^3-\sigma c^3.
\]
Direct substitution, independent of the residual ideal computation, gives
\[
f_a|_Q=\rho^3(d+ac)K_C,\qquad
g_b|_Q=-\sigma^3(c+bd)K_C.
\]
The ruling factors coincide precisely when \(ab=1\). Near \((1,1)\), this
gives the actual line
\[
L_a=V(x_1+a x_0,\ x_3+a x_2).
\]
It meets \(C\) at curve parameter \(u=-a\).

The fixed line \(L=L_1\), by contrast, lies on both hypersurfaces only when
\(a=b=1\). These two statements must remain distinct: the fixed-line locus
is a point, while the moving-ruling locus is the hyperbola. The formulas
identify lines in this ruling on \(Q\); no unrelated global classification
of lines in all intersections is being inferred from them.

The standard-library
[identity verifier](../computations/ci_cycle_line_degeneration_2026_10_25.py)
checks the actual global restrictions and the boundary formulas. Its fourteen
checks also passed independent replay.

## 3. The five-point scheme and normal matrix

With \(L=[-r:r:-s:s]\), put
\[
P_5=4r^5-2r^4s+9r^3s^2+2r^2s^3+3rs^4+2s^5.
\]
The actual pullback of \(L\cap E\) is \((P_5)\), which is geometrically
squarefree. The point \(C\cap L\) has \(r/s=-1\), and
\(P_5(-1,1)=-14\ne0\).

Use normal coordinates \(n_0=x_0+x_1\), \(n_1=x_2+x_3\). Differentiating the
actual pair at \((1,1)\) yields the displayed matrix in the contribution,
whose determinant is
\[
-(r+s)P_5.
\]
Its second-column entries are
\[
F_1=-r(r+s)(r+2s),\qquad
G_1=-4r^3+2r^2s-9rs^2-s^3.
\]
The exact coprimality checks show that \(F_1\), \(s\), and \(r+s\) are units
at every point of \(P_5=0\). Thus \(f_1\) is a legitimate local smooth
carrier at each residual node, even though no such choice is assumed for
arbitrary pairs in the wider investigation.

The determinant has six zeros: five residual attachments and one attachment
to \(C\). Its degree six also agrees with the determinant of the quartic
first-normal map on a line, whose two summands each have degree three.

## 4. Independent first-order smoothing calculation

At a point of \(P_5=0\), parameter variations have
\[
\delta f=-r^3(r+s)\delta a,\qquad
\delta g=-s^3(r+s)\delta b.
\]
Eliminate the normal coordinate with nonzero derivative \(F_1\). A convenient
representative of the one-dimensional node-smoothing class is
\[
\delta g-\frac{G_1}{F_1}\delta f
=(r+s)\left(\frac{G_1}{F_1}r^3\delta a-s^3\delta b\right).
\]
The independently checked polynomial identity
\[
-G_1r^3=rP_5+F_1s^3
\]
reduces this class to
\[
-s^3(r+s)(\delta a+\delta b).
\]
The scalar is nonzero at all five nodes. This proves the common smoothing
direction, with no choice of numerical approximations to the roots of \(P_5\).
The sign differs from another possible cokernel representative only by a unit.

The direction is precisely normal to \(ab=1\) at \((1,1)\). A tangent
direction to that hyperbola does not smooth the nodes to first order; a
transverse direction smooths all five to first order.

## 5. From first order to the local discriminant

First-order agreement alone would not prove that the five full discriminant
branches coincide. Here the moving line supplies the additional information.
Along \(ab=1\), a neighborhood of the checked member retains a smooth
remaining component and five simple intersections with \(L_a\). Simplicity
of the intersections ensures that their positions persist after an étale or
analytic localization. Hence each node's smoothing parameter vanishes along
the actual smooth divisor \(h=ab-1=0\).

After labelling the geometric nodes, the standard local form is
\(xy=\tau_i(a,b)\). The completed version and its hypotheses are in
[Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0C58); the
[étale nodal-family description](https://stacks.math.columbia.edu/tag/0H8M)
gives the corresponding local formulation. Since \(h\) divides \(\tau_i\)
and its derivative transverse to \(h=0\) is nonzero, the quotient is a unit:
\[
\tau_i=h\,u_i,\qquad u_i(1,1)\ne0.
\]
Therefore
\[
\prod_{i=1}^5\tau_i=(ab-1)^5u,\qquad u(1,1)\ne0.
\]

The multiplicity five belongs to this product of node-smoothing contributions,
or the corresponding norm/Fitting discriminant. It is not a universal claim
about every scheme structure called a discriminant: the scheme-theoretic
image of the critical locus can have the reduced ideal \((ab-1)\). The
contribution note now states this distinction explicitly.

To exclude additional residual singularities near this parameter, use a
proper flat model. The two strict transforms on
\(\operatorname{Bl}_C\mathbf P^3\) are divisors of class \(4H-\mathcal E\).
Their central proper intersection is the residual curve. A relative regular
sequence gives flatness after shrinking the parameter neighborhood. At the
eighteen reduced marked attachments the residual curve crosses \(\mathcal E\)
transversely, and blowdown is an isomorphism on it. These conditions remain
open nearby. Properness and openness of smoothness then reduce the local
residual singular-fiber support to the five node neighborhoods just analyzed.
This supplies the needed geometric bridge; the finite first-order matrix
calculation alone would not supply it.

The statement is local near \((1,1)\). It does not assert that the entire
affine parameter plane, the whole hyperbola, or every point of a path to
\((2,3)\) has only these singularities.

## 6. Genus and topology cross-checks

The residual curve satisfies
\[
p_a(L\cup E)=0+12+5-1=16.
\]
Its five gluing edges between two components have four graph cycles.
Smoothing all five nodes joins the components and converts these four
cycles into genus, yielding the smooth residual genus sixteen.

For the total curve, the line member has three normalized components of
total genus twelve and twenty-three nodes, hence arithmetic genus
\[
12+23-3+1=33.
\]
Its dual graph has first Betti number twenty-one, so over \(\mathbf C\)
the total curve has \(b_1=24+21=45\), \(b_2=3\), and Euler characteristic
\(-41\). The smooth-residual member has \(b_1=49\), \(b_2=2\), and Euler
characteristic \(-46\). The drop by five agrees with smoothing five ordinary
nodes. The componentwise canonical-degree table in the contribution also
checks: each component satisfies \(2g_i-2+n_i=4d_i\).

This is deformation that absorbs a line into a higher-genus residual
component, not a contraction of that line. The explicit local discriminant
and finite ideal identities support this picture without an STCI inference.

## 7. Review boundary

The exact geometric example, moving ruling, five common first-order smoothing
classes, local product-discriminant statement, and topology calculations pass
independent review with the qualifications above. Evidence is reproducible
using the two durable scripts linked in sections 1 and 2. No new canonical
record, all-pairs theorem, or global discriminant classification is asserted.



---

## 2026-10-25-ci-cycle-smooth-residual-audit.md

# Independent audit of the explicit smooth residual example

Date: 2026-10-25. Reviewer: independent audit agent from the cycle notebook
team. Status: reviewed exact characteristic-zero coordinate example; not a
canonical promotion or a classification of complete intersections.

This audit follows [the repository retrieval protocol](../INDEX.md).
The existing geometry of the marked quartic is used as a premise, with
[R0021](../results/quartic_mu4_degeneration.md) fixing the original reference
pair. This audit concerns new computations, not a replay of that accepted
result. The broad adaptive residual question remains as stated in the
[valuative continuation](CI_CYCLE_ADAPTIVE_FRONTIER.md#2026-10-25-ci-cycle-adaptive-valuative-notebookmd).

**Outcome.** The final explicit pair over \(\mathbf Q\) has exactly the
scheme union of \(C\) and a smooth geometrically integral residual curve
\(D\) of degree twelve and genus sixteen. Their scheme intersection consists
of eighteen distinct geometric points and avoids both distinguished endpoints.
Thus the smooth-residual comparison picture now has one reproducible exact
example; it is no longer only a general-pair deduction or an unexecuted
experiment. The assertions below use exact rational computations and their
geometric interpretation. No finite-field lifting is involved.

## 1. The precise final pair

Use
\[
C=[s^4:s^3t:st^3:t^4],\qquad
Q=x_0x_3-x_1x_2,
\]
\[
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,\quad
A=x_1^3-x_0^2x_2,\quad D_3=x_2^3-x_1x_3^2,
\]
and the actual quadrics
\[
H_0=x_0^2+x_1^2+x_2^2+x_3^2+x_0x_2+2x_1x_3,
\]
\[
H_1=2x_0^2+3x_1^2+5x_2^2+7x_3^2
    +x_0x_1+x_0x_3+x_1x_2+3x_2x_3.
\]
The audited pair is
\[
f=F+QH_0+2x_0A,\qquad
g=G+QH_1+3x_3D_3.
\]
All its coefficients lie in \(\mathbf Q\), both forms have degree four,
and every summand vanishes on the actual fixed curve. This is a pair of
global homogeneous forms, not a prescription of rational-function-valued
normal symbols.

In \(S=\mathbf Q[x_0,x_1,x_2,x_3]\), put
\[
J=(f,g),\qquad K=\operatorname{sat}(J:I_C),\qquad
T=\operatorname{sat}(K+I_C).
\]
The saturation is with respect to the irrelevant ideal. The recorded curve
ideal is
\[
I_C=(Q,A,x_0x_2^2-x_1^2x_3,D_3).
\]
It was already checked in the deformation laboratory; the current computation
uses that actual ideal throughout.

## 2. Independent exact reconstruction

The reviewer constructed a separate rational Macaulay2 computation from the
displayed equations before replaying the durable verifier. It checked:

- \(J\) has codimension two and degree sixteen.
- \(K\) is saturated, defines a projective scheme of dimension one, has degree twelve, and Hilbert
  polynomial \(12n-15\).
- The exact ideal identity \(J=I_C\cap K\) holds.
- The saturated ideal
  \(K+I_2(\operatorname{Jac}K)\) is the unit ideal.
- \(T\) has degree eighteen and
  \(\operatorname{sat}(T+I_3(\operatorname{Jac}T))=(1)\).
- Neither endpoint point ideal meets \(T\) projectively.
- \(H^0(\operatorname{Proj}(S/K),\mathcal O)=\mathbf Q\).

The independent suite returned
\[
\operatorname{codim}J=2,\quad \deg D=12,\quad
P_D=-27P_0+12P_1=12n-15,\quad
\deg T=18,\quad H^0(\mathcal O_D)=\mathbf Q^1.
\]
Here Macaulay2 uses \(P_0(n)=1\), \(P_1(n)=n+1\). Its sheaf cohomology
output is a rank-one module over \(\mathbf Q\); the Krull dimension of that
module is zero and must not be used as its vector-space dimension.

The durable
[Macaulay2 verifier](../computations/verify_ci_smooth_residual_example_2026_10_25.m2)
was then read and replayed. It contains the same final equations and all the
substantive assertions above. Its conclusion matches the independent
reconstruction.

## 3. Why the computations imply geometric smoothness and irreducibility

The residual construction is linkage to the locally Cohen–Macaulay curve
\(C\) inside a proper complete intersection. Its residual is an unmixed curve;
the checked union identity additionally excludes a hidden failure to recover
the total scheme. The Jacobian test uses the minors of size two, corresponding
to codimension two in projective three-space. Saturating to the unit ideal
means that the projective singular locus is empty. It is not merely the
absence of rational singular points.

This is an exact test over \(\mathbf Q\), a perfect field. The Jacobian
identities remain valid after extending scalars, so \(D\) is geometrically
smooth. The origin of the homogeneous affine cone is irrelevant to
projective smoothness and is precisely why saturation is used.

Smoothness alone would not prove geometric irreducibility: disjoint smooth
components could remain. The separate computation of \(H^0(\mathcal O_D)\)
closes that gap. Flat base change of cohomology under field extension gives
\[
H^0(D_{\overline{\mathbf Q}},\mathcal O)
=H^0(D,\mathcal O)\otimes_{\mathbf Q}\overline{\mathbf Q}
=\overline{\mathbf Q}.
\]
Thus \(D\) is geometrically connected. For the standard equivalence between
this global-section condition and geometric connectedness in the proper,
geometrically reduced setting, see
[Stacks, Lemma 33.9.5](https://stacks.math.columbia.edu/tag/0FD2).
A smooth curve over an algebraically closed field is regular, so distinct
irreducible components are disjoint. Connectedness then implies a single
irreducible component. This establishes geometric integrality, rather than
only primality over \(\mathbf Q\).

The Hilbert polynomial now yields genus sixteen because \(D\) is a smooth
connected curve. No inference of smoothness from its numerical polynomial
was made.

## 4. Eighteen reduced attachments really give eighteen nodes

The ideal \(T\) is the actual scheme intersection \(C\cap D\). Its projective
zero-dimensional scheme has degree eighteen. The rank-three Jacobian test,
again with projective saturation, proves geometric reducedness. Hence over
\(\overline{\mathbf Q}\) it consists of eighteen distinct points.

Both curves are smooth. At each attachment, reduced intersection length one
implies distinct tangent directions: if the residual tangent agreed with the
marked tangent, every normal equation of \(C\) would vanish to at least order
two on that residual branch. A length-one pullback would be impossible.
Their union therefore has an ordinary transverse node at each attachment.
The ideal equality \(J=I_C\cap K\) proves that this union is the full original
complete intersection.

The genus accounting independently matches:
\[
p_a(C\cup D)=0+16+18-1=33.
\]
There are no other singularities of this union because both components are
smooth and they are disjoint away from \(T\).

## 5. A separate check from the global first-normal sections

On \(x_0=1\), let \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\). Restricting the
two quadrics to \(C\) gives
\[
h_0=1+u^2+u^3+2u^5+u^6+u^8,
\]
\[
h_1=2+u+3u^2+2u^4+5u^6+3u^7+7u^8.
\]
The first-normal rows of the final pair are
\[
\sigma_f=(h_0-1)X+(-uh_0-2)Y,
\]
\[
\sigma_g=(h_1-3u^8-6u^9)X+
                 (4u^9+9u^{10}-uh_1)Y.
\]
The reviewer expanded their determinant independently, obtaining
\[
\Delta(u)=(u+2)h_1+u^9(1+3u)h_0-6u^8-16u^9-9u^{10}.
\]
Its constant coefficient is four and its leading coefficient in degree
eighteen is three. Thus neither \(p\), represented by \(u=0\), nor \(q\),
represented by \(u=\infty\), is a zero of its degree-eighteen homogenization.
The nonzero determinant also independently gives generic transverse
multiplicity one along \(C\).

The standard-library
[boundary verifier](../computations/verify_ci_smooth_residual_boundary_2026_10_25.py)
constructs the actual homogeneous forms, derives their first symbols, compares
the determinant with this formula, and checks
\(\gcd(\Delta,\Delta')=1\) over \(\mathbf Q\). Its
[JSON evidence](../computations/ci_smooth_residual_boundary_2026_10_25.json)
records the nineteen coefficients. This is independent complementary evidence
for eighteen simple attachments and for endpoint avoidance; the projective
residual smoothness comes from the separate Jacobian and cohomology checks.

## 6. Rejected candidates and exact scope

The preliminary pair \(F+QH_0,G+QH_1\) also passed the smooth residual checks,
but retains simple attachments at both endpoints. It is useful as a comparison
and was independently checked before the final endpoint-free pair.

Adding \(x_0A\) and \(x_3D_3\), both with coefficient one, is an unsuccessful
intermediate candidate for an irreducible residual. It contains the line
\(x_0+x_1=x_2+x_3=0\). On that line \(Q=0\), \(F+x_0A=0\), and
\(G+x_3D_3=0\). The final coefficients two and three avoid this failure.
The rejected case should remain a documented diagnostic rather than an
unmentioned failed search.

The final example provides a single benchmark for the deformation notebook.
It neither classifies all pairs, proves properties for every point of a
parameter space, nor controls arbitrary bidegrees. It does concretely show
that all eighteen residual attachment points can move away from the two
distinguished endpoints while retaining \(C\).

Reproduce the durable checks from the repository root:

~~~sh
/opt/homebrew/bin/M2 --script research/computations/verify_ci_smooth_residual_example_2026_10_25.m2
python3 research/computations/verify_ci_smooth_residual_boundary_2026_10_25.py
~~~

These exact computations and the geometric bridges above pass independent
review. The user’s universal residual-component aim remains open; no canonical
record or inherited proof is changed by this audit.

