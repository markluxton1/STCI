# Characteristic comparison and actual equation realization

**Assessment, October 31, 2026.** This is a synthesis and recommendation from
the committed branch states listed below. It introduces no new theorem and
does not promote branch results. The fixed curve is
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\).
Its unrestricted characteristic-zero STCI question remains open.

The preceding arithmetic investigation is closed at `563fa53`: its proofs,
independent review dispositions and necessary support are committed, with no
unfinished computation represented as a result. Open mathematical questions
below are proposed next work, not an automatically running research queue.

## What the arithmetic lane has established

The original degree question has an exact connection to characteristic zero.
For the minimum larger defining degree \(\delta(p)\), ranging over **all**
geometric supported pairs,
\[
 C\text{ is not an STCI in characteristic zero}
 \quad\Longleftrightarrow\quad \delta(p)\longrightarrow\infty.
\]
An unbounded subsequence along distinct primes would already suffice.
Thus unrestricted growing lower bounds would settle the original problem;
the arithmetic reformulation does not provide a weaker substitute for it.
Conversely, a bounded-degree incidence with a characteristic-zero point
has supported pairs in almost every characteristic. The
[full integral incidence](../supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md)
retains actual scalar coefficients and properness.

Three different kinds of progress must remain separate:

| Result | Scope and consequence |
| --- | --- |
| Sharp minimum \(p\) for \(p\ge7\) | [Weight-restricted pairs](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md): one weight-homogeneous equation with arbitrary mate, or at most two weights in each equation. This is not a lower bound for unrestricted \(\delta(p)\). |
| Unconditional growing quartic-mate bound | [Effective transfer](../supplements/EFFECTIVE_CHARACTERISTIC_TRANSFER.md), combined with promoted R-0001, gives \(\beta_4(p)\gg\sqrt{\log\log p/\log\log\log p}\), over all quartic carriers. The coarse unrestricted growth estimate remains conditional on characteristic-zero nonexistence. |
| Obstructions to characteristic-zero lifting | [Prime-to-p extraction](../supplements/PRIME_TO_P_POWER_EXTRACTION.md) and [Frobenius precision](../supplements/FROBENIUS_POWER_LIFTING_PRECISION.md) allow both equations to deform, but prescribe the special pair and keep the embedded curve fixed. They do not cover every horizontal component of the full incidence. |

For the known \((F_p,H_4^n)\) pairs, \(p\ge7\), the last row is
particularly concrete. Maximum **strong** unramified precision is exactly
\(1+v_p(n)\); a strong lift imposes the curve-ideal nilpotence bound,
not merely topological support on an Artin fiber. In this family the minimum
larger degree at precision \(W_N\), \(N\ge2\), is
\(4p^{N-1}\). Increasing powers produces arbitrarily long finite lifts,
but no compatible fixed-degree characteristic-zero presentation follows.

Any actual supported mixed-characteristic trait through these points requires
\(p\mid n\) and absolute ramification \(E=v_\pi(p)\ge p-1\).
Even then, a sufficiently accurate lower-degree approximation, with the same
first equation and precision \(s>E/(p-1)\), would extract a quartic
mate and give a contradiction. None of these necessary conditions constructs
a trait at the remaining indices.

There is also a geometric necessary condition at every ramification index.
On a hypothetical generic degree-\(p\) carrier, close the pure
multiplicity-\(p\) root \(D_K\) over the DVR. Its special fiber has
\[
 0\longrightarrow T\longrightarrow\mathcal O_{D_0}
 \longrightarrow\mathcal O_{V(F_p,H_4)}\longrightarrow0,
\]
where \(T\ne0\) is supported at one or both parameter endpoints and
\[
 p_a(D_K)=1+2p^2-\operatorname{length}T.
\]
If \(T=0\), flat Cartier extension and the vanishing
\(H^1(\mathcal O_{V(F_0)})=0\) would recover an ambient quartic
equation. This is the most concrete connection from this lane to the
global presentation problem. The positive defect is necessary, not known
to be impossible or realizable in an actual trait.

## What the other branches change

The comparison uses committed snapshots, after refreshing remote refs.
Local investigator commits beyond the remote tips are included. This is
source inspection, not a merge of their proofs or navigation. For a path
absent from this checkout, retrieve the stated version with
`git show <commit>:<path>`; branch names alone do not fix the evidence.
The actual sextic and octic calculations discussed below are in
characteristic zero; their possible comparison across characteristics is
proposed work, not an inherited positive-characteristic theorem.

| Branch or baseline | Fixed checkpoint | Contribution to this assessment |
| --- | --- | --- |
| `main` | `9d734e1` | Earlier canonical baseline; no unrestricted STCI conclusion. |
| `codex/intersections-containing-quartic-2026-10-27` remote | `b271fc5` | Actual elliptic double-inverse construction and scoped closeout, retained in the consolidation proof home below. |
| `restructure/mathematical-consolidation` | `fd50fb6` | Broader account of containing intersections, residual cycles, actual ACM sources, projection and conductor descent; selected earlier investigator results only. |
| `codex/stci-char0-four-streams-2026-10-30` | `7530d05` | Supported-closure and specialization analysis; newer Milnor, Chow and exceptional-cover assessments. |
| `codex/spectral-realization-2026-10-31` | `0046bec` | Scheme-theoretic spectral torsion and an actual order-three root/sextic-lifting slice. |
| `codex/stci-complexity-torsion-two-2026-10-31` | `2875622` | Actual octic/root-lift comparison and a certified proper pair with residual degree 32. |
| `codex/positive-characteristic-degree-bounds-2026-10-31` | `563fa53` | The arithmetic, lifting and endpoint-root results summarized above, plus scoped sextic reductions. |

**The broader target includes actual intersections with residual curves.**
The consolidation branch explicitly retains
\([V(F,G)]=m[C]+R\), \(ab=4m+\deg R\), as useful geometry.
An actual source, a supported ACM construction upstairs, or a proper pair
with known residual support can teach more than another necessary numerical
condition. For our lane this means recording how residual support first
appears under lifting, together with the strong-support obstruction, rather
than reporting only that one proposed lift failed.

The elliptic construction makes this concrete: its fixed octic normalization
has an additional inverse scheme of projective length twelve, so that member
cannot gain a mate by increasing the mate degree. The full five-parameter
support and descent loci are still uncomputed. This is a separate candidate
family, with actual homogeneous sections; it has not been reduced to our
powered-quartic points. Evidence: `fd50fb6`,
`research/synthesis/elliptic_double_inverse_construction.md`, §§1–6,
including its retained source at `b271fc5`.

**Endpoint specialization is shared territory, with different objects.**
The characteristic-zero branch already removes endpoint embedded points in
a torus/Hilbert degeneration and uses dualizing-complex base change. It also
shows that an already embedded supported thickening on its open pencil can
have a supported locally Cohen–Macaulay flat closure; the remaining global
CI presentation is not automatic. Our theorem concerns the lower root on a
mixed-characteristic carrier. Its additional implication is that a pure
special root would force a Cartier divisor and an ambient lower-degree
equation. The exact sequences have a similar shape, but no map identifies
their defect modules. Evidence: `7530d05`,
`research/notes/2026-10-31-unrestricted-strategy-assessment.md`, §§6 and 33;
compare the [root-specialization proof](../supplements/FROBENIUS_POWER_LIFTING_PRECISION.md#root-specialization-and-the-remaining-endpoint-defects).

**Spectral torsion is more precise than a rank experiment, but has a different
input.** The spectral branch identifies the determinant condition with the
relative Picard torsion scheme, including nilpotent parameter structure, and
constructs universal graded data on its normal model. Its roots are saturated
smooth quadratic genus-one \((2,2)\) curves. Our powered-quartic extraction starts
with a generically smooth first carrier and a linear first normal relation.
The spectral torsion exponent is not the powering exponent in
\((F_p,H_4^n)\). There is no proved transfer from spectral \(p\)-torsion
to a strong ambient Witt lift, or an identification of its kernel with \(T\).
Evidence: `0046bec`, `research/synthesis/spectral_determinant_schemes.md`
and `research/synthesis/order_three_roots_and_sextic_lifts.md`.

**Actual equation spaces now give useful controls.** The complexity branch
compares octic forms with lifted roots and supplies a proper octic pair with
generic transverse length eight and residual degree 32. Passing the first
root/equation comparison is therefore not a sole-support certificate.
The spectral branch similarly distinguishes its reviewed sextic slice from
the larger unreviewed diagnostic continuation. These computations favor
testing the full actual source and the next compatibility condition over
collecting more abstract torsion points. Evidence: `2875622`,
`research/supplements/ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md`; `0046bec`,
`research/synthesis/order_three_roots_and_sextic_lifts.md`.

The degree distinction matters. At degree six, the quadratic-symbol image
misses eleven dimensions through a genuine higher differential, after lower
corrections. At degree eight that symbol map is surjective, and the sextic
source instead supplies part of the correction space. A degree-six source
obstruction cannot simply be extrapolated to higher degrees. The accepted
octic seed has a nonzero second root obstruction yet admits the proper
length-eight pair: that obstruction is required only at the next root-tower
depth. Evidence: `2875622`,
`research/supplements/IDEAL_SHEAF_SPECTRAL_SEQUENCES_AND_GLOBAL_JETS.md`, §4,
and `ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md`, §§3–5.

**Some broad obstructions have already lost their proposed extra force.**
The newest characteristic-zero assessment finds its quartic Milnor budget
implied by local geometry. The Chow bundle comparison and exceptional-cover
selection do not yet supply the missing embedded realization or an
independent contradiction. Its last Hom-bundle lemma is explicitly a
proposal without separate independent audit; it is not used here as a
theorem. Evidence: `7530d05`, the same strategy assessment, §§35–38.

## Recommended next work

### 1. Test the endpoint defect required by an actual supported trait

This is the first recommendation for the arithmetic lane. Start from the
root-closure sequence above, retain the full supported complete intersection,
and derive what its annihilators, linkage or duality impose on \(T\).
The question is whether a **positive** endpoint defect is compatible with
those actual data, not whether embedded points can occur in arbitrary flat
families. Reuse the characteristic-zero specialization analysis as a method;
first construct any proposed comparison map between its module and ours.

A bounded local test, after identifying a condition beyond the genus
identity, may use \(p=7,n=7,E=6\), the first powered-quartic
case at the present ramification threshold, with degrees \((7,28)\).
This is a diagnostic choice, not a known lift or an exhaustive reduction.
Keep the fixed curve, quotient flatness and full nilpotence condition.
Do not restart the excluded \((7,8)\) prime-to-seven power case.

Stop with one of: a proved incompatibility in a precisely covered class;
an exact local model realizing the required defect with its remaining global
obligations stated; or a precise additional condition needed for the
comparison. A local model alone must not be called a projective STCI lift.
If the test only reproduces the genus identity, do not escalate powers or
precision automatically.

### 2. Attach actual sextic equations to the order-three parameterization

The complementary direction should retain a possible construction. The
spectral branch parameterizes the smooth order-three roots in the fixed
ruling frames by an open subset of \(\mathbf P^7\). Its reviewed parity
plane contains six first-compatible roots: four fail the actual sextic symbol
test, and two fail the next cubic comparison after every actual correction.
This closes that slice, not the full parameter space. Under the full stated
saturation, movement-two, joint-generation and generic-CI hypotheses, the
remaining numerical row is \((r,s;a,b)=(2,12;6,16)\).

I recommend using this parameterization with the complete actual-sextic
symbol and cubic maps. The first bounded step can audit the existing
four-parameter continuation, including denominator boundaries and its
unresolved \(A=0,D\ne0\) case; the suggested eighteen points in that
diagnostic are not established results. Stop after a complete answer for that
source unless it yields an invariant extending to the full parameter space.
Distinguish this problem from the degree-\((6,6)\) ADE three-orbit reduction
in this lane. Keep the octic residual pair as a control against claiming that
an actual first lift already exhausts the intersection cycle.

Characteristic comparison is useful here if it tracks a demonstrated change
in the actual source or higher obstruction, retaining all good-reduction
and rank-stratum conditions. The output should be an exact point satisfying
all declared conditions, or a family-wide obstruction. A count of
\(\mathbf F_p\)-rational points is not geometric emptiness, and a
finite-prime pattern is not a bound for almost every prime. A survivor still
needs an actual mate and complete projective support verification.

### 3. Keep degree transfer as a consequence of geometric coverage

Apply the effective incidence theorem whenever a new characteristic-zero
carrier class or degree range is actually excluded. Optimize its constants
only if that improves a concrete computation. Extending a restricted weight
bound needs a theorem covering the missing presentations; more Frobenius
examples or stronger bounds inside the same class do not provide it.

The immediate recommendation is therefore endpoint compatibility first,
with the order-three actual-source test as the alternative. It is not a
recommendation to launch all remaining branches or a new unbounded prime
search. A supported mixed-characteristic trait would prove existence in
characteristic zero; an obstruction through our chosen special fibers would
still need a coverage argument to prove nonexistence for every presentation.

## Evidence and closeout

The prior proofs retain their own promoted or reviewed-provisional status.
This comparison reuses their recorded evidence and distinguishes the last
unreviewed diagnostic/proposal passages. No inherited CAS calculation was
rerun, no other branch was merged, and no new mathematical result is claimed.
Independent branch retrieval and a separate bounded review accepted source
fidelity, object distinctions, provisional status and the proposed stopping
conditions. The review checked that the order-three continuation differs
from the closed parity slice and that no conductor, spectral or arithmetic
defect modules were silently identified. Its smooth-root wording refinement
is incorporated. Repository metadata, changed local links, pinned evidence
paths and whitespace are checked at commit closeout; these checks do not
constitute new proof audits or reruns of the inherited calculations.
