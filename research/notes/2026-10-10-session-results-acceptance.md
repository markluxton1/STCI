# October 10 root acceptance and continuation frontier

The universal integral projective-curve STCI problem and the unrestricted
characteristic-zero problem for fixed
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record accepts the proof
and audit chains below, superseding the corresponding open genus-one
language in the October 9 acceptance and the latest-pause rundown.
No novelty claim is made without a separate literature assessment.

Unless explicitly broadened, statements concern fixed `C0` over every
algebraically closed field of characteristic zero and an integral quartic
carrier `X` in `P3`. They do not impose a bound on the minimum carrier
degree in an arbitrary presentation. The October 9 and earlier acceptance
records retain their historical proofs, exact runs and scopes.

## 1. The entire genus-one quartic-carrier lane is excluded

**PROVED HERE / independently accepted.** If the finite normalization of
an integral quartic `X` containing fixed `C0` has sectional genus one,
there is no homogeneous form `G` of any positive degree with
`V(X,G)=C0` set-theoretically. There is no additional first-normal-order,
bounded mate degree, reduced conductor or displayed-family hypothesis.

Root accepts the completed
[interface audit](2026-10-10-session-genus-one-interface-independent-audit.md)
and [remaining-partitions audit](2026-10-10-session-ribbon-repeated-partitions-independent-audit.md)
after reading their arguments, the owner partition proof and the actual
exact companions. The proof is the following complete chain:

1. A mate forces the whole inverse image to have support the unique
   embedded smooth lift `c`; normal-surface Cohen--Macaulay purity removes
   extra isolated points. Its actual pulled-back divisor is `b c`, with
   coefficient fixed by degree, not merely set-theoretic support.
2. The accepted rationality, canonical adjoint and `D5` saturation proofs
   make the normalization an ADE del Pezzo of degree four. The entire
   exceptional type is `4A1` or `A3+2A1`, the mate degree is even, and
   `2c~2H` is an actual Cartier equivalence.
3. The complete anticanonical embedding is a normal two-quadric surface
   in `P4`. Restriction to `c` is an isomorphism on its five linear
   sections. Thus its coordinates are exactly the five quartic monomials,
   while the original projection deletes `Y2=U^2V^2`. The center is outside
   the surface. The primary anticanonical theorem includes singular ADE
   models; no smooth del Pezzo hypothesis is being transferred.
4. The actual Cartier double `2c` is a ribbon even at singular points.
   Its nilideal is `O_P1(-6)`, and its conormal quotient gives the entire
   quadratic net `M(d) eta=0`, `eta1^2-eta0 eta2 != 0`. No actual ribbon
   or surface pencil is omitted by this parameterization.
5. The entire conductor is the actual plane conic `(L,R)`, including
   singular and nonreduced schemes. Full inverse support requires
   `rad(L_C)` to divide the other projection derivative. The nonzero
   binary quartic `L_C` has zero middle coefficient. Its five root
   partitions are squarefree, `[2,1,1]`, `[3,1]`, `[2,2]`, and `[4]`.
6. Squarefree and all `[2,1,1]` cases are excluded by the separately
   checked derivative map, including its only common-basepoint locus.
   The [complete repeated-partition proof](2026-10-09-session-ribbon-repeated-partitions-complete.md)
   and separate audit exclude every remaining partition. Endpoints,
   zero direction coordinates and the derivative-invisible coefficient
   are retained; only center-preserving diagonal changes and reversal
   are used to normalize the actual projection.
7. For `[3,1]` and `[2,2]`, independent equality of the complete bilinear
   net/support ideals with explicit linear ideals excludes every hidden
   determinant branch. Actual singular lines eliminate `[4]` and the
   surviving `[3,1]` pencil. The sole `[2,2]` pencil has a smooth conic
   conductor and nonconstant trace-square/norm ratio. Any positive
   power descending would force that ratio to be constant, so every
   exponent is excluded, including the split quadratic-cover case.

The independent computation is over `QQ` and extends to every
characteristic-zero field. Factorization and root-of-unity arguments use
the algebraically closed constant field. The upstream complex ADE input
retains its separately stated finite-coefficient descent. This result
must not be enlarged to arbitrary smooth rational quartics: their
projection centers need not be equivalent to the fixed deleted-middle
center.

Consequently the only remaining integral quartic-carrier normalization
lane for fixed `C0` is sectional genus **two**, using the already accepted
normal, genus-zero, smooth-normalization and nonrational exclusions.
This consequence is still not an unrestricted all-degree theorem.

## 2. New genus-one exact evidence and corrected attribution

The new independent [M2 interface companion](../computations/verify_session_genus_one_211_interfaces_2026_10_10.m2)
verifies **42 exact identities** for the entire `[2,1,1]` calculation.
The separate [M2 repeated-partition companion](../validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2)
verifies **29 exact conditions**, including full ideal equality and a
different conductor section from the owner's calculation.

Root copied their exact source bytes into a separate snapshot cwd and
observed both terminal passes; actual subprocess streams, commands,
elapsed times, hashes and copied sources are retained in the
[root replay manifest](../validation/2026-10-10-genus-one-root-replay/execution-manifest.json).
These are two additional executions of two source paths, not four new
mathematical verifiers. The proof's geometric quantifiers are supplied
by the written audits, not by the number of identities.

The older `[2,1,1]` note incorrectly attributed some checks to its
current Python companion. The new interface audit explicitly corrects
that attribution and supplies the missing exact certificate. Historical
passes must not be represented as checking identities absent from their
source. Protected-name and parser scaffold failures, and the failed
SymPy import, remain in the separate execution records. No dependency
installation or historical failure deletion was performed.

## 3. Genus-two actual conductor-line theorem

**PROVED HERE / independently accepted without a mate hypothesis.**
Root accepts the [entire-conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md).
In the accepted genus-two situation the resolution is rational,
`L^2=4`, and `K_M.L=-2`. Every singularity of the normal surface `S`
is rational, without assuming `K_S` Cartier or Q-Cartier. Negative
canonical degree gives `H2(O_S)=0`; Leray and rationality of `M`
give `R1 sigma_*O_M=0`. Proper duality then gives
`R sigma_*omega_M=omega_S`.

Quartic hypersurface adjunction and finite duality identify the actual
conductor ideal `I` with `nu_*omega_S`. Its maximal Cohen--Macaulay
property makes the downstairs conductor pure CM. The exact polynomial
`chi(O_X(m))-chi(I(m))=m+1` forces that entire scheme to be a reduced
line `Gamma`, with no embedded or isolated points.

Natural MCM biduality and closed-immersion duality give
`nu_*O_S/O_X=omega_Gamma=O_P1(-2)`. The entire upstairs conductor `D`
is therefore a finite flat double cover with algebra

    p_*O_D=O_P1 direct-sum O_P1(-2),
    w^2=delta,       delta in H0(O_P1(4)).

The trace splitting is global. Singular, split and nonreduced covers,
including `delta=0`, are retained. `D` is connected Gorenstein of genus
one and hyperplane degree two, but is not asserted Cartier on `S`.
General transverse-plane genus proves generic quartic order exactly two
along `Gamma`. This is a structural reduction, not a mate exclusion.

## 4. Accepted markings and a bounded section-case exclusion

The [marking audit](2026-10-10-session-genus-two-marking-and-section-pause-audit.md)
accepts the remaining ruled/plane marking steps of the
[adjoint model](2026-10-09-session-genus-two-adjoint-conic-model.md),
including the exact vertical `D8` lattice. The complete pencil
`f=K_M+L` is rational and basepoint-free, `f^2=0`, `L.f=2`.
Both mate strata must remain:

    (lambda,q)=(0,4): c#^2=0, f.c#=2;
    (lambda,q)=(1,3): c#^2=1, f.c#=1.

**PROVED HERE / bounded exclusion.** In the second stratum, the
[marked-prime audit](2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md)
and [independent no-zero-horizontal audit](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md)
exclude both one- and two-proper-horizontal-line cases when the
degree-zero horizontal prime `B=e0-e_i-e_j` is absent. A survivor
therefore requires `B` present. The anti-nef cycle pulled back from a
uniformizer of the smooth embedded curve is integral and has contact
coefficient one; the proofs retain full predecessor and descendant
chains, not a count of unused centers alone.

The `B`-present free-child and satellite cases remain open in these
proofs. Internal chain attachments invalidate the proposed star shortcut.
The bisection stratum remains open as well. The separate frozen
[source line-budget note](2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md)
retains its old pending two-line label; the independent audit supplies
the bounded acceptance without rewriting that historical source.

## 5. The actual normal ambient conic model is accepted

**PROVED HERE / independently accepted without a mate.** Root accepts
the [blowup-lift independent audit](2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md)
after reading its complete proof and checking the cited primary proper
duality and blowup inputs. It accepts the
[owner proposal](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md)
at its recorded hash; the frozen proposal label is superseded by this
separate audit and acceptance, not silently rewritten.

The actual ambient equations of the conductor line correspond through
natural rank-one canonical-duality identifications to a basis of the
complete basepoint-free adjoint pencil. They have a globally regular
common factor `g` in `H0(-K_M)`. The pulled-back ambient line ideal is
exactly `O_M(-div(g))`, including absence of a residual base scheme.
Consequently the morphism lifts to `B=Bl_Gamma(P3)` and has as its image
the actual integral strict transform `T` of `X`.

Exact generic order two gives

    T~4H_B-2E_B,        omega_T=O_T(-E_B),
    rho*omega_T=omega_M.

The proper-duality trace `rho_*omega_M -> omega_T`, untwisted using the
last equality, gives a generically nonzero `O_T`-linear map
`rho_*O_M -> O_T`. Its restriction to `O_T` is a nonzero global constant
because `T` is proper integral. Rescaling forces equality of the two
algebras in the common fraction field, proving normality. This does not
assume normality or higher-direct-image vanishing in advance. Properness
of the target is essential; the audit preserves the affine cusp
counterexample to a version omitting it. Compatible canonical forms
then give an actual crepant equality, hence `T` has ADE singularities.
The original finite normalization `S` need not be Gorenstein.

The ruling of the blowup is the actual family of planes through `Gamma`,
and `T` cuts an actual conic in every fiber. Only vertical `(-2)` curves
are contracted in `M->T`; horizontal `(-3)` sections can be contracted
in `T->S` instead. On the smooth lift the common-factor equality gives

    tau=length(Gamma intersect C0)=4-f.c#.

Thus the bisection stratum is an actual length-two secant/tangent line
case and the section stratum is an actual length-three trisecant case,
including repeated contacts. Length three forces the line onto the
unique smooth quadric containing `C0` and into its degree-three ruling.
This accepted normal conic model excludes neither mate stratum by
itself. Further residual-conductor and double-pencil arguments are
separate ongoing proof obligations.

## 6. Retained unrestricted scope and evidence

The principal MF6 at-most-630-point necessary locus is not a classified
carrier list. The 22 second endpoint-family points of degrees `3,4,15`
retain every lower lift line. Other ancestor strata, early `e=2` defects,
higher minimum carrier degrees, entirely-thick presentations, and the
totally ramified split-sextic boundary remain open. Neither the entire
genus-one theorem nor a future all-quartic theorem would settle those
unrestricted cases.

The October 9 seal's **97 distinct latest-PASS sources / 110 indexed
executions** and **2006 integrity / 313 local-link checks** remain
historical frozen counts. New records are separately indexed and are
not silently added. Live HEAD is `406d63db72000a3951497a0ba2a8fbfbc13e8ead`,
title `2026-10-09 afternoon limit reached`; older morning HEAD references
are historical. Root performed no Git mutation.
