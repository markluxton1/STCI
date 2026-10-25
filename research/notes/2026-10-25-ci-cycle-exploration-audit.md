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

The contributions reviewed are [deformations](2026-10-25-ci-cycle-deformation-laboratory.md),
[conductor and topology](2026-10-25-ci-cycle-conductor-topology.md),
[specialization and proximity](2026-10-25-ci-cycle-specialization-proximity.md),
and [the root pencil](2026-10-25-ci-cycle-root-pencil.md). The synthesis notebook
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

The [main notebook](2026-10-25-ci-cycle-geometry-notebook.md) was read after
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
