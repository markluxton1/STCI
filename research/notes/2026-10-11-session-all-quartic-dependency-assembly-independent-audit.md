# Independent assembly audit: all integral quartic carriers of the fixed C0 are excluded

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit`.
Status: **PROVED HERE / independent dependency and coverage audit PASS**,
under the explicitly recorded classical and independently accepted component
inputs. No canonical frontier file is edited by this note. The conclusion
is an all-quartic carrier theorem, not an unrestricted non-STCI theorem.

Work over an algebraically closed field of characteristic zero, with the
literal smooth rational quartic and its projective equivalents

    C0=[s^4:s^3 t:s t^3:t^4] subset P3.

**Audited assembled theorem.** If `F` is an irreducible homogeneous form of
degree four with `C0 subset V(F)`, no homogeneous form `G` of any positive
degree has `V(F,G)=C0` set-theoretically. The carrier can be normal or
nonnormal, its normalization can be singular, and the mate can have arbitrary
normal order or degree. No generic-smoothness, reduced-conductor, first-normal
ratio, clean-conductor, ordinary-singularity or displayed-family restriction
remains in this assembled statement.

## 1. Actual checkout and scope of this audit

The live checkout inspected here had HEAD
`2ba77d1a1177db9390693066c6b185040766c089`. The source notes and working-tree
canonical records were read rather than treating an older pause summary as
current evidence. The October 10 resumed
[acceptance](2026-10-10-session-continuation-results-acceptance.md) already
accepts the bisection and nonendpoint section exclusions. Its remaining
endpoint label is its preserved earlier frontier. The subsequently saved
[full endpoint reduction](2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md)
and [binding independent audit](2026-10-10-session-genus-two-endpoint-full-independent-audit.md)
supply the missing component checked in this assembly. Root acceptance and
canonical reconciliation remain distinct actions.

This audit verifies logical interfaces, full case coverage and the exact
degree consequence. It does not claim a fresh literature novelty result,
rerun every historical numerical enumeration, count copied verifier sources
as independent programs, or use parallel-agent agreement as proof. It read
the actual component proofs, including their hypotheses and rejected
shortcuts, and checked the decisive local and divisor calculations below.

## 2. The carrier classification has no omitted case

An integral quartic `X=V(F)` is either normal or nonnormal. In the normal
case a general plane section is a smooth genus-three curve and the separate
normal-carrier theorem applies. In the nonnormal case, finite normalization
`nu:S->X` has a general smooth integral pulled-back hyperplane curve of
genus `pi` in exactly `{0,1,2}`. The plane section has arithmetic genus
three, and the nonnormal codimension-one locus gives positive normalization
defect. A hypersurface is Cohen--Macaulay, so a nonnormal integral quartic
cannot hide only an isolated failure of normality outside this argument.

The normalization sectional genus is not the ambient plane quartic's
arithmetic genus and not the conductor degree. The following table is the
complete split used by the proof.

| Carrier or normalization lane | Complete exclusion used |
|---|---|
| Integral normal quartic | [Normal global audit](2026-10-07-session-normal-global-adversarial.md), including [nonreduced exceptional cycles](2026-10-07-session-normal-nonreduced-independent-audit.md) |
| Nonnormal, `pi=0` | [Minimal-degree classification and cone audit](2026-10-09-session-normalization-genus-zero-independent-audit.md), with the accepted entire F0/F2 scroll and Veronese projection proofs |
| Nonnormal, `pi=1` | [All genus-one interfaces](2026-10-10-session-genus-one-interface-independent-audit.md) and [all repeated contact partitions](2026-10-10-session-ribbon-repeated-partitions-independent-audit.md) |
| Nonnormal, `pi=2`, `lambda=0` | [Full second-pencil/Cartier-double/ribbon audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md) |
| Nonnormal, `pi=2`, `lambda=1`, three distinct contacts | [Full nonendpoint trisecant audit](2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md) |
| Nonnormal, `pi=2`, `lambda=1`, one triple contact | [Full endpoint audit](2026-10-10-session-genus-two-endpoint-full-independent-audit.md), including reversal of the endpoint |

There is no separate nonrational-normalization row: the
[ruled intersection audit](2026-10-09-session-nonrational-normalization-independent-audit.md)
proves that every nonnormal integral quartic containing a smooth rational
degree-four curve has rational normalization, without assuming a mate.
Its nef pushdown identity retains every infinitely near blowup:

    4=(2g-2)a^2+(6-2pi)a+sum m_i(a-m_i),   0<=m_i<=a.

For a nonrational ruling this forces `a<=2`, while the rational lifted
degree-four curve is a fiber component and forces `4<=a`. The contradiction
establishes rationality before either del Pezzo or conic-model reduction.

## 3. Generic regularity and full inverse support remove hidden hypotheses

The generic regularity of an integral quartic along C0 is automatic. If all
ambient partial derivatives vanished generically on C0, they would vanish
on it. A general integral plane quartic would then have its four distinct
transverse C0-intersection points singular. Its normalization defect would
be at least four, greater than arithmetic genus three. The
[genus-zero audit's addendum](2026-10-09-session-normalization-genus-zero-independent-audit.md)
proves this without a normality assumption. Consequently there is no extra
integral quartic lane singular at the generic point of C0.

Under a mate, the unique curve component `c` above C0 is a smooth embedded
copy of C0. A proper birational strict-transform map to this normal curve
is quasi-finite, hence finite and an isomorphism. Potential additional
isolated inverse-image points cannot simply be ignored. The actual nonzero
Cartier pullback of G on normal S has a pure one-dimensional zero scheme;
its zero support is the entire inverse image of C0. This rules out isolated
extra points and yields full support exactly c. Intersecting its Weil
divisor with H gives

    div_S(nu*G)=b c ~ bH,   H.c=H^2=4,   b=deg G.

Thus the coefficient is b even when the mate has higher generic normal
order. The smooth curve c need not be Cartier at a singular point of S;
the positive-genus arguments expressly retain that possibility.

The `pi=0` classification includes the singular rational-normal-quartic
cone, in addition to F0, F2 and the Veronese surface. The accepted entire
scroll proofs include nongorenstein and nonreduced conductor schemes. A
smooth-normalization theorem alone is therefore not being used to cover
all quartic normalizations.

## 4. The genus-one theorem is genuinely complete

The actual rational resolution has `K_M=-L`; S is the crepant degree-four
ADE del Pezzo model. The signed D5 saturation proof applies to the actual
exceptional lattice and actual smooth lift and gives genuine `2c~2H`.
The complete anticanonical map identifies this S with a normal integral
two-quadric intersection in P4 before any projection computation is used.
Restriction to c identifies the fifth coordinate with `s^2t^2`, so the
projection deletes precisely the middle coordinate of the complete rational
normal quartic. This establishes the fixed-center hypothesis for every
carrier in this lane; it does not posit that a displayed toric family is
exhaustive.

The actual Cartier double is a global CM ribbon, including all its ADE
points, with nilideal O(-6) and the complete kernel net `M(d) eta=0`.
The entire conductor algebra and singleton test give the necessary support
condition for the nonzero binary quartic L_C. Its five and only five
multiplicity partitions are

    [1,1,1,1], [2,1,1], [2,2], [3,1], [4].

The interface audit covers the first two with every direction and basepoint
chart; the independent repeated-partition audit covers the last three,
including the derivative-invisible quadric coefficient and every determinant
root. Its `[2,2]` final obstruction proves that no positive power of the
actual quadratic section descends, in both split and nonsplit conductor
algebras. No mate-degree bound remains. All reparametrizations used in the
fixed-center classification preserve that center; an arbitrary smooth
rational quartic projection is not substituted for the literal C0.

## 5. Both genus-two mate strata, and all trisecants, are covered

The [adjoint proof](2026-10-09-session-genus-two-adjoint-independent-audit.md)
gives the complete connected basepoint-free conic pencil `f=K_M+L`, with
`K_M^2=0`. The [null-curve and correction proof](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md)
classifies every exceptional prime as vertical (-2) or horizontal (-3),
with at most two disjoint horizontal sections. For the effective rational
actual correction Z it proves

    q=-Z^2>0,   lambda=K_M.Z in Z>=0,
    q+lambda=4,   lambda^2<=q.

Consequently the only mate strata are `(lambda,q)=(0,4)` and `(1,3)`.
The earlier shortcut `q=4` in every case is not used.

The [entire conductor proof](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
establishes rational singularities of S and the actual reduced downstairs
conductor line, with no embedded or isolated components. Its upstairs
quadratic algebra retains split, singular and nonreduced covers. The
[normal ambient-model proof](2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md)
constructs the actual strict transform in the ambient line blowup and proves
its normal ADE property by proper trace, before invoking crepancy. It is T,
not the possibly non-Gorenstein S, which is asserted ADE. The pulled line
ideal is exactly O(-D_M), without a residual zero-dimensional base scheme.

In `lambda=0`, the second rational pencil produces an actual equality
`2Z=sum k_t F_t-2R`, with all entire fiber multiplicities and every one of
the four blowup centers retained. Thus `2Z` is integral exceptional and
`2c~2H` is an actual Cartier equivalence. Its full Cartier double is pure
CM with nilideal O(-8), as follows from `chi(O_S(mH))=2m^2+m+1`.
Normalization gives a nonzero global ambient conormal map to that nilideal.
The verified `N_C0/P3^*=O(-7)^2` forbids such a map. This covers bisecants,
tangents and all local-normalization singularities, without requiring Q to
be an ambient quadratic section.

In `lambda=1`, the actual line intersection has length three, so the line
lies on the unique smooth quadric q and belongs to its degree-three ruling.
The restriction is `t^3-a s^3`. In characteristic zero it has three distinct
roots for finite nonzero a, or one triple root for a=0 or infinity; reversal
exchanges the latter. These are all line positions.

The no-degree-zero-horizontal theorem forces the special prime B with
`c#.B=0`. The complete nonendpoint proof exhausts every (2,2) divisor
containing its Gamma fiber, including double B, reducible residuals, double
fixed fibers, and B with coefficient zero when another horizontal exists.
For integral residual, the two other contacts force its two branch values;
the branches cross B transversely and give actual endpoint A-chains. Their
all-length correction formula is strictly below the required coefficient
one. It never infers disjointness on T merely from disjointness on M.

For the endpoint, the full degree-four ideal identity gives the entire
eleven-dimensional carrier family `F=q Q+D L0`. The unique positive
horizontal correction must lie over the sole triple contact and has
coefficient one. The full endpoint proof then retains and excludes:

* a coefficient-zero special B with a second supporting horizontal prime,
  including the second Gamma fiber at infinity;
* two distinct residual crossings, including a crossing at infinity;
* the entire triple residual family, with its endpoint A-chain, exact
  internal A-chain attachment `2/(n+5)`, D4 distinct outer arms and
  incompatible multiplicity-three case;
* the doubled-horizontal divisor `2B+2F`, with all normal-coefficient roots
  on P1, repeated roots and arbitrary ADE blocks away from the contact.

In the last case the degree-three normal coefficient gives the exact
away-contact contribution `2 v^t Q^(-1) v=ord(h)`. The actual contact
equation gives total contribution at most 5/2, below the required three.
This is the calculation closing the potentially dangerous repeated scheme;
an assumed all-A-chain graph or an abstract D7 numerical example is not used
to assert realizability or exclusion. The [full endpoint binding audit](2026-10-10-session-genus-two-endpoint-full-independent-audit.md)
checks these actual family interfaces and local attachments. Reversal closes
the second endpoint. This exhausts `lambda=1` and hence the genus-two lane.

## 6. No circular small-degree or numerical input is hidden

The inherited normal-quartic proof uses the classical normal-quartic source
classification, Jaffe's rational-singularity and ADE-pair inputs, the audited
normal-bundle and normal-sheaf bounds, exact reduced/nonreduced necessary
graph enumerations, and prior mate exclusions through degree five. Those
prior exclusions were established before the present assembly: the plane
and quadric obstructions, classical cubic and (4,4) theorems, and repository
P-040 for (4,5). P-040 is independently proved from the multiplicity-five
Banică--Forster/Boratyński classification and P-025's complete chart cover;
it does not use this all-quartic conclusion. Thus the assembly has no
dependency loop through its own new theorem.

The two graph enumerations eliminate a necessary superset; they do not
claim every retained graph is geometrically realized. Their counts and
agreement are evidence for their explicitly proved enumeration scope.
The final Type-D step is the actual pulled maximal-ideal identity, forcing
passage coefficient one, contrary to the remaining coefficient-two rows.

For complex primary classification statements, the recorded finitely
generated coefficient-field transfer includes radical-equality witnesses,
geometric integrality and normality, so it applies to every algebraically
closed characteristic-zero field. No uncountability assumption is imported.

## 7. Degree consequence and remaining scope

For any homogeneous pair F,G with projective `V(F,G)=C0`, the forms are
coprime. Otherwise their common irreducible factor supplies a surface in
the intersection. If f is any nonconstant irreducible factor of F, then
`V(f,G)` is a nonempty pure one-dimensional complete intersection, since
f and G are coprime. It lies in the integral curve C0, so its support is
all of C0. Thus f is itself a carrier of a defining pair. The same applies
to every factor of G, or to any pair of factors f,g. Repetition changes
scheme multiplicity, not this support argument.

No degree-one factor can contain this nonplanar C0. Its only quadric is
`q=x0*x3-x1*x2`, and restrictions of ambient degree-b forms to q have class
(b,b), which cannot have full support a positive multiple of its curve
class (1,3). The verified Craighero--Gattazzo 1989 all-cubic theorem removes
every integral degree-three factor. The assembled theorem above removes
every integral degree-four factor. Therefore:

    Every irreducible factor of either defining form has degree at least 5.
    In particular, every STCI presentation of fixed C0 has min(deg F,deg G)>=5.

This conclusion includes reducible and repeated presentations. It does not
assert that degree five is attained or that a higher-degree pair exists.
The delegated [degree-factor microaudit](2026-10-11-session-degree-factor-and-mf6-scope-audit.md)
separately inspected the actual [CG1989 primary PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf),
printed pages 171--173: its base field is already algebraically closed of
characteristic zero, its mate has arbitrary degree, and its cubic carriers
are reduced irreducible. The factor lemma handles reducible or repeated
cubic forms. No extra complex-field descent is needed for this particular
cubic input.

Every actual quartic-plus-mate lane is now excluded, including all (4,6)
MF6 mate types and all early-defect quartic mate strata, whatever the extra
defect divisors, principal parameter roots or mate degree. Earlier finite
candidate loci cease to be open *mate existence* problems with an actual
quartic carrier. The theorem does not calculate their parameter sets.

In particular, all seven necessary MF6 numerical types close as actual
mate presentations:

| e | `(d2,d3)` |
|---:|---|
| 0 | `(1,8), (2,7), (3,6), (4,5)` |
| 1 | `(0,4), (1,3), (2,2)` |

All fifteen retained coarse nonregular pole strata likewise close as
actual (4,6) pairs; no unproved bijection between BF types and pole strata
is needed for that conclusion. The regular-ratio `(0,3,6)` subcase and
principal positive-D2 `(1,1,3)` and `(1,2,2)` cases are included.

Common-quartic-ancestor and local-cohomology incidences ask for containment
or simultaneous annihilation, not a two-form STCI radical equality. Their
22 retained endpoint-family roots, entire lift lines, principal necessary
at-most-630-point locus and other uncomputed incidences are not declared
empty by a no-mate theorem. They remain distinct algebraic questions or
possible information for higher-degree research. Entirely thick higher-degree
presentations and an integral split sextic with arbitrary higher-degree mate
also remain outside the all-quartic theorem. If such a sextic has an actual
quartic mate, that pair is excluded; a quartic ancestor alone does not imply
that hypothesis.

The retained split family `F_tau=-B^2+tau*q*K` has degree six, and its
necessary P-020 mate scale is `8k` with k positive. Thus it does not require
a quartic mate; its remaining totally ramified normalization and conductor
work retains its previous scope.

The unrestricted fixed-C0 STCI question, every general integral projective
curve and the universal question over arbitrary algebraically closed fields
remain **OPEN** in this record. No theorem forcing a quartic carrier in an
arbitrary presentation has been established. This audit finds no blocking
coverage gap in the stated all-quartic assembly, while preserving precisely
that larger unresolved scope.

## 8. Source bindings and verification attribution

At this audit the principal component source SHA-256 values were:

| Source | SHA-256 |
|---|---|
| Normal global audit | `cecccf902bfc8a63b70ebf28c1510c49b590c323c4c95be94fa86759425e2bff` |
| Normal nonreduced audit | `3fefd232c29931319eab3894ddb0f82659624a6b623449f163d5242ce8d80a50` |
| Genus-zero independent audit | `b4cc4bdb803e2bab5a66e4366cce5bb0a48521866ff6860a193d117e92c2ef7d` |
| Nonrational independent audit | `e2e24ac3524ef473f86d71d8465ed18987abc83ac6c20ac2630f85196a3908bb` |
| Genus-one interface audit | `96fa5d1f3d5f3de5ca51866d554039a8a19d8e759198e4fce8453c9358261561` |
| Repeated-partition audit | `a7ee3496fe5b3aaedae9b0a34abdfcbc63e6dfbda1d7993cc301d7cb23fc1cf1` |
| Full bisection audit | `5aa6eeedb31ff2fe316b706c3c0e86ff78d9beca01c9f92dfa5d7fafcc283133` |
| Full nonendpoint audit | `970e41c503d71402df22275308cf024b45191dc3fe1e371319285b9adac70395` |
| Full endpoint owner | `366c8396333118dabcaed6106fbc68fdaf0851d1005bf5c5d3511d46c77cc5c9` |
| Full endpoint independent audit | `d4253e444643c2201e49de9dd20545bb6aff993123d303a75c286f8758d4c37c` |

This audit also inspected the existing isolated root manifests for the
[genus-one 42/29-identity replays](../validation/2026-10-10-genus-one-root-replay/execution-manifest.json),
[8-condition normal-bundle replay](../validation/2026-10-10-normal-bundle-root-replay/execution-manifest.json),
and [16-identity endpoint replay](../validation/2026-10-10-endpoint-root-replay/execution-manifest.json).
All record terminal exit zero, and a fresh standard-library SHA-256 check
confirmed their recorded source hashes match the current original sources.
This is source-binding verification of existing executions, not a new
Macaulay2 execution or a mathematical proof inferred from a green manifest.
The local geometry and exhaustive interfaces remain the written proofs.

Historical 97-source/110-execution counts and frozen integrity seals are
unchanged. No repository memory, Git state or canonical record was mutated
by this audit; only this separate continuation-ready note was added.
