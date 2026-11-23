# Universal first moment: exact proof boundary across the active branches

**Status:** mathematical synthesis of existing main-branch and PR #171--#173
arguments, not a new vanishing theorem or an independent proof audit.
Characteristic zero throughout. The objective is the **necessary** relation,
not a classification of all realizable arrangements.

## Target and proved coverage

For a proper homogeneous pair \(F_a,G_b\) with entire fundamental cycle
\[
 [V(F,G)]=\sum_i n_i[C_{u_i,v_i}],\qquad
 C_{u,v}=[s^4:s^3t:ust^3:vt^4],\qquad
 4\sum_i n_i=ab,
\]
write \(\sigma=\sum_i n_i[(u_i,v_i)]\in\operatorname{Sym}^{ab/4}T\)
and \(M_1(\sigma)=\sum_i n_i u_i/v_i\). The desired assertion is
\[
       R_{a,b}\subseteq V(M_1)\quad\text{for every }a,b.
       \tag{UM1}
\]
If true, it excludes sole support: \(M_1(m[C_{u,v}])=m u/v\ne0\).

The [reviewed first-moment theorem](chow_arrangement_moments.md)
proves UM1 when the ideal is torus-invariant, when an actual generator
is an eigenform, or when the specified pair of coordinate congruences
holds. The whole reduced CI arrangement is invariant, hence covered.
The [PR #173 cycle-first argument](chow_realization_moment_separation.md)
offers further \((3,4)\) and \((4,4)\) coverage; its new proofs await
independent review. The \((4,4)\) diagonal is separately excluded by R-0022.
No unrestricted all-degree theorem is known. These are statements about
the **actual CI cycle**, not arbitrary reduced support, a containing
surface, or a flat Hilbert limit.

The equation \(M_1=0\) is a regular hypersurface equation on the interior
\(\operatorname{Sym}^m T\). More strongly, the linear Chow coefficient
\(A_{yz}=-4A_0M_1\), with \(A_0\ne0\) there, vanishes on the projective
Chow closure of each covered locus. No closure argument can recover
points outside those closures.

### Stronger first-jet refinement from the intrinsic geometry (November 22)

The [spectral–Jacobian/Serre-duality argument](spectral_jacobian_first_jet_bridge.md)
makes the earlier six-layer trace formula **strictly sharper under full
translated-cycle support**. Set \(A=x_1x_2,B=x_0x_3\),
\(M_{ij}=F_iG_j-F_jG_i\). Every such CI satisfies
\[
 A M_{12}-2B M_{03}\in(F,G).
\]
This follows from the **actual** Artinian Jacobian socle and the
tangent Plücker coordinates of each translated component, not
invariance. If \(f_0,g_0\) are the restrictions of \(F,G\) to
\(L=V(x_0,x_3)\), and \(p,q,r,s\) their four first normal
coefficients, then
\[
 \boxed{2M_1=\operatorname{Res}_{f_0,g_0}(ps-qr)
 =\operatorname{Tr}_L\partial_{f_0,g_0}(ps-qr).}
\]
The last equality identifies the residue with the connecting class
for the **Koszul sequence on** \(L\simeq\mathbf P^1\),
whose target is \(H^1(L,\omega_L)\simeq k\).
The moment is half a nondegenerate alternating pairing of two
first normal equation jets. Its critical symplectic space has
dimension \(2\min(a,b)\). The six-layer formula still applies to
**arbitrary** finite-free CI pairs, while this refinement requires
the *entire translated cycle*.

The same argument proves an equation-level **support recognition
criterion**: among proper pairs avoiding \(L\), all reduced
components are translated quartics exactly when the ideal contains
some product of nonzero-parameter quadric-pencil members
and the displayed Jacobian relation. The second quotient
character \(\eta=x_0x_2^2/(x_1^2x_3)\) is encoded by the cubic
pencil \(R_\eta\), with
\(Q_\xi\cap R_\eta=C_{\eta/\xi,\eta/\xi^2}+L_{01}+L_{23}\).
Thus the actual remaining obstacle is to prove **first-jet
isotropy** on this full source-incidence locus, not merely to
calculate the residue. Independent proof review remains due.

### Full spectral-power compatibility: the same Serre line at a later order

The [sole-support first-jet gate](sole_support_first_jet_gate.md)
now compares *both* necessary actual-equation
identities. Sole support imposes
\(\Omega(v_0,v_3)=ab/2\ne0\) in
\(H^1(L,\omega_L)\), but also the
spectral membership \(Q^m\in(F,G)\),
\(m=ab/4\). The latter is automatically
satisfied to normal order
\(r_*=(a-2)(b-2)/2\) near the disjoint
line; its first possible obstruction is the
canonical **degree-\(r_*\) binary form**
\[
 [Q^m]_{r_*}\in H^1(L,\omega_L)\otimes
 \operatorname{Sym}^{r_*}\langle x_0,x_3\rangle .
\]
Thus the low and first high compatibility
conditions land in the **same Serre line**
but at distinct normal degrees, providing
a precise global-jet bridge target.
For any translated-cycle CI, a canonical
linear map from the **full homogeneous
quadric-spectrum space** to this first
obstruction space annihilates the realized
spectral form. The relevant map is not
claimed to be injective or to force
its first coefficient zero.

The two requirements conflict for a
concrete restricted \((4,4)\) family
(\(\lambda\mu=8\) versus \(4\));
the calculation does not cover unrestricted
quartic coefficients or higher degrees.
No general transgression/compatibility
theorem between the Serre pairing and the
higher spectral class is established.

### Exact low-order control of the common-residue bridge

The [global \((4,4)\) example](sole_support_first_jet_gate.md#a-stronger-negative-control-both-leading-stci-conditions-can-hold)
chooses first normal jets
\(p=x_1^3,q=x_2^3,r=-2x_1^3,s=6x_2^3\)
and lifts them to two **actual homogeneous
equations containing** \(C\).
It satisfies the hypothetical-STCI
first-jet residue \(8\) **and** vanishing
first spectral-power residue
\(\mathcal R_{F,G}(Q^4)=0\),
yet has a degree-twelve residual curve.
The full Poisson identity fails at
normal order one; full \(Q^4\)-membership
fails at order three. Thus the same
Serre-line and first spectral leading-class
comparison cannot be a complete exclusion.
The earlier restricted \((4,4)\) mismatch
is a special first-jet pattern, not
an all-quartic argument. The genuine
unknown remains compatibility of the
**entire** ideal identities across the
global equation-source filtration
and all degrees.

## Upward synthesis: the smallest exact common algebraic target

**All-degree finite-cover trace.** Every such proper pair avoids the line
\(L=V(x_0,x_3)\). The graded CI algebra
\(E=k[x_0,x_1,x_2,x_3]/(F,G)\) is finite free of rank \(ab\)
over \(A=k[x_0,x_3]\); its associated cover of \(\mathbf P^1\)
has the fixed graded module splitting, independently of normal form.
By trace additivity over the reduced generic components,
\[
 \operatorname{Tr}_{E/A}(x_1x_2)
  =4x_0x_3\sum_i n_i\,u_i/v_i.
  \tag{T}
\]
This identity requires no torus-invariance assumption on \(E\).
Consequently UM1 is **exactly** the assertion that this trace vanishes
on the Chow-matched proper-pair incidence.

**Only three source layers enter the trace.** Write
\(F=\sum f_j,\ G=\sum g_j\), where \(f_j,g_j\) have degree \(j\)
in \(x_0,x_3\). The [existing degree-two trace/residue theorem
in PR #171](https://github.com/markluxton1/STCI/blob/f6fc360da20168c91071ed3044adf4f289f0fd8a/research/arguments/torus/fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers)
determines (T) **entirely** from
\((f_0,f_1,f_2,g_0,g_1,g_2)\), by a universal finite-free
trace calculation or a Grothendieck-residue formula. This is an
established all-degree reduction of the *value* of \(M_1\), not a proof
that it is zero. Classical residue/trace formulas supply the underlying
algebraic mechanism (Cattani--Dickenstein--Sturmfels,
*Computing Multidimensional Residues*; D'Andrea--Jeronimo,
*Rational Formulas for Traces in Zero-Dimensional Algebras*).
The extra hypothesis that the **whole** cycle is translated remains
global and cannot be replaced by the first two source jets.

**Equivalent resultant coefficient.** The
[homogeneous transverse Chow norm in PR #172](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/torus/chow_arrangement_moments.md#the-homogeneous-transverse-chow-form-as-a-section-norm)
identifies the plane-section resultant of \(F,G\) with a norm
\(\mathcal N_\sigma\), and its first mixed coefficient with \(4M_1\).
Thus the trace formulation and the coefficient vanishing in the
actual resultant image are the **same test**, not independent
obstructions. The full norm is needed to specify the translated
cycle; its perfect-power specialization for sole support is a
restatement of the original realization problem, not a vanishing proof.

## An all-mate non-invariant positive control

The [PR #172 fixed exceptional-quartic carrier theorem](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/torus/quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier)
has an immediate first-moment consequence beyond the \((4,4)\)
classification. On any fixed nonzero member \(T\) of the exceptional
quartic pencil, every proper mate whose entire fundamental cycle is a
sum of translated quartics has degree \(4j\) and cycle
\(2j[C_{1,1}]+2j[C_{1,-1}]\), after the stated normalization.
Hence \(M_1=2j(1-1)=0\) for **every \(j\ge1\)**, even though
the carrier need not be an eigenform. The proof uses the actual
fixed-carrier multiplicity lattice, \(S_2\) extension and the
all-mate singleton quartic exclusion; for the distinguished nodal
member the Hodge matrix and Cartier parity independently recover
that lattice. It does not extend to arbitrary moving carriers.
This is a concrete all-mate mechanism additional to direct
finite-free trace or proper invariant degeneration.

## Downward controls: why apparent shortcuts fail

1. **No universal invariant-CI degeneration.** The
   [exceptional quartic pencils in PR #171](https://github.com/markluxton1/STCI/blob/f6fc360da20168c91071ed3044adf4f289f0fd8a/research/arguments/torus/quartic_hilbert_chow_limits.md#chow-closure-and-full-opposite-limits)
   satisfy \(M_1=0\) yet their cycles are outside the Chow closure
   of invariant quartic CI realizations. Their flat limits can have
   extra generators. A Chow-fixed cycle or invariant radical does not
   guarantee a proper invariant initial pair. The
   [rank-two descent counterexample on main](equivariant_set_theoretic_descent.md#a-rank-two-counterexample-with-a-complete-intersection-origin)
   independently prevents a general equivariant two-generation claim.
2. **The trace is not constrained by endpoint concentration alone.**
   The [explicit quartic control](https://github.com/markluxton1/STCI/blob/f6fc360da20168c91071ed3044adf4f289f0fd8a/research/arguments/torus/fixed_surface_and_endpoint_algebras.md#8-all-three-boundary-supports-are-compatible-with-zero-first-trace)
   has the prescribed endpoint and quadric restrictions but residual
   sheets; a specialization has zero first trace without sole support.
   No inference from the endpoint polynomial, fixed-quadric
   restriction, or a scalar trace can discard those sheets.
3. **Fixed-depth jets of a single containing equation are too free.**
   The [PR #172 center-jet surjectivity theorem](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/torus/chow_matched_equation_layers.md#a-fixed-depth-center-jet-limitation)
   gives \(H^0(I_C(d))\twoheadrightarrow(S/I(L)^N)_d\)
   for \(d\ge N+2\). The all-degree one-sided cone-jet trace
   tests from PR #171 therefore do not imply that an arbitrary
   high-degree containing equation has the requisite special jet.
   The missing constraint must involve **both equations and their
   actual complete intersection cycle**.
4. **Extreme coefficients and determinants lose equation relations.**
   The [PR #172 canonical end-adaptation and counterexamples](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/torus/chow_matched_equation_layers.md)
   distinguish the two opposite adapted presentations, higher
   cancellation layers, and the full flat limits. Even two coprime
   end pairs need not recover actual generic contact. A proof using
   toric quotient endpoint sections must retain the same actual
   degree-labelled equation spaces and their relation maps.
5. **Chow and numerical carrier tests do not themselves see the
   first additive moment.** The exact reduced-union endpoint Hilbert
   strata in PR #173, and the
   [normal-carrier Hodge/Cartier monoid in PR #172](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/torus/fixed_surface_restriction_lifts.md#normal-carriers-a-complete-geometric-description-of-the-arrangement-monoid),
   are strong actual-realization filters. Neither supplies an
   all-degree coefficient identity \(M_1=0\); numerical intersection
   data cannot be silently identified with the additive \(u_i/v_i\)
   coordinates.

**Three different filtrations.** The jet filtration at the **disjoint
projection line** \(L=V(x_0,x_3)\), the two **opposite intrinsic
weight** filtrations of an actual generator system, and the local
normalization filtrations at the **contracted curve endpoints**
\(p_0,p_\infty\) are not interchangeable. The six-layer trace
functional belongs to the first, whereas the global endpoint sections
in PR #173 describe the second, and the delta/Hilbert strata describe
the third. An all-degree implication between them must be proved using
the same actual source equations; numerical coincidences are insufficient.

## A weaker target sufficient for STCI and its two regimes

The [all-degree normal-replacement theorem in PR #172](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier)
uses classical Bertini and \(R_1+S_2\): if each component has
generic transverse embedding dimension at most one, an actual
generator replacement produces a normal integral larger carrier
without changing the CI ideal. The converse fails for the
**entirely-thick** generic transverse algebras. This partitions the
possible source approach but proves neither regime's moment
vanishing. The normal-replacement mechanism and its stated generic-embedding-dimension boundary were independently reconstructed on November 23, 2026 at the linked carrier proof owner; neither regime's unrestricted moment vanishing is proved.

If a sole-support STCI exists, choose one of **minimal degree
product**. The [factor-descent argument in the same source](https://github.com/markluxton1/STCI/blob/e5f97d3b23c7023e6940b752d7fa4112e5706f78/research/arguments/carriers/normal_carrier_divisor_geometry.md#equal-degree-pencils-below-degree-ten-the-sextic-proof-extends-to-octics)
makes every nonzero member of its actual generator systems integral:
a positive-degree factor together with the other generator gives a
smaller sole-support pair. Therefore proving the trace vanishing for
minimal degree-product sole-support pairs would already settle STCI;
UM1 for all Chow-matched arrangements is a stronger, potentially
more geometrically accessible, statement. Do not transfer
normal replacement to the entirely-thick alternative.

## Research decision and stopping condition

Priority is **one source-sensitive implication**:
\[
 \begin{gathered}
 (F_a,G_b)\text{ proper},\quad
 [V(F,G)]\text{ Chow-matched to translates}
 \\ \Longrightarrow\
 \operatorname{Tr}_{E/k[x_0,x_3]}(x_1x_2)=0.
 \end{gathered}
\]
The first useful probe is to compare the established invariant-pair,
exceptional non-invariant quartic, and one-sided cone-jet
arguments **at the common six-layer trace functional**, asking
what additional *joint equation/cycle* identity makes each vanish.
A candidate identity must survive the exceptional quartic control
and the known higher-source cancellation examples. This is narrower
than determining all Chow coefficients or classifying all CI
arrangements.

The current cross-framework iteration has not produced that
joint identity, an independent proof of UM1, or an all-degree
exclusion. Additional repetitions of the known numerical,
endpoint or degeneration filters without a new equation relation
would not advance the objective. Independent correctness,
literature, editorial and generality review of any proposed
new implication remains required before promotion.
