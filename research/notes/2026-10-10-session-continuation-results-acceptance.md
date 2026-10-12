# October 10 resumed continuation: accepted results and exact frontier

The universal projective-curve STCI question and the unrestricted
characteristic-zero question for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This acceptance extends the
[earlier October 10 acceptance](2026-10-10-session-results-acceptance.md),
whose proof and evidence bytes are preserved. No novelty claim is made
without the separate literature assessment.

All new mate exclusions here concern the fixed monomial curve and its
projective equivalents over every algebraically closed field of
characteristic zero. An arbitrary smooth rational quartic embedding is
not silently substituted. The field, carrier degree, entire conductor,
and unresolved higher-degree scope are essential.

## 1. The complete genus-two bisection lane is excluded

**PROVED HERE / independently accepted.** An integral quartic carrier
of fixed C0 whose finite normalization has sectional genus two admits
no mate in the `lambda=0` stratum, in any positive mate degree.
The bisection, ordinary bisecant and tangent boundaries are all covered.

Root accepts the full
[bisection independent audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md)
after reading its proof and independently reconstructing both its
Cartier compression and its global ribbon contradiction. The argument
uses the following complete chain, rather than a bounded root-of-unity
or exceptional-graph search.

1. The accepted mate identity gives a smooth lift `c` on the rational
   resolution M with `c^2=0`, `K_M.c=-2`, and `f.c=2` for the connected
   adjoint pencil `f=K_M+L`. Its actual correction Z is effective,
   rational and exceptional, supported on vertical `(-2)` curves.
2. The complete `|c|` is a second connected rational pencil. Its product
   with `|f|` has degree two onto `P1 x P1`. The normal Stein cover W
   is finite flat, with branch class `(2,2)`, and is a degree-four ADE
   del Pezzo. The resolution M is obtained from its crepant resolution
   V by exactly four point blowups, allowing all infinitely near and
   intersection centers.
3. With R the actual integral relative canonical divisor, the
   [second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md)
   proves an equality of actual rational divisors

       Z+R=(1/2) sum_t k_t F_t,   sum_t k_t=4.

   Here F_t is the entire fiber with all multiplicities and k_t counts
   centers. Thus `2Z` is integral and exceptional. The accepted
   numerical-to-linear lemma on M upgrades this to the actual Weil
   equivalence `2c_S~2H` on the finite normalization S. Consequently
   `2c_S` is an effective Cartier divisor, cut by a genuine quadratic
   section Q on S. This section is not assumed ambient.
4. Normality makes S Cohen--Macaulay. Its Cartier double curve is
   therefore pure CM, with smooth reduction `c_S~=C0` and generic
   length two. Its nilradical J has square zero: J squared is
   generically zero, hence would be a finite-support subsheaf of the
   pure CM curve. The same purity makes J torsion-free of rank one
   on the smooth reduction, so J is a line bundle.
5. The accepted normalization/conductor sequence, equivalently
   rational-resolution Riemann--Roch, gives

       chi(O_S(mH))=2m^2+m+1  for every integer m.

   The exact Cartier sequence gives `chi(O_(2c_S))=1-7=-6`.
   Since `chi(O_c)=1`, it follows that `J=O_P1(-8)`. This step does
   not require a Cartier canonical divisor on S.
6. The actual morphism `2c_S -> S -> X -> P3` induces a global map
   `I_C0/I_C0^2 -> J`: the ambient ideal pulls into J and its square
   maps to zero. Off the conductor line, normalization is an
   isomorphism, so the actual double curve is locally a closed
   subscheme of P3. The map is generically surjective and nonzero.
7. The already known repository P-009 gives
   `N_C0/P3^*=O_P1(-7) direct-sum O_P1(-7)`. Root independently
   reconstructed the derivative coefficient calculation; the
   [new Jacobian audit](2026-10-10-session-quartic-normal-bundle-independent-audit.md)
   supplies two cubic kernel columns independent at every point,
   including both endpoints. But

       Hom(O(-7) direct-sum O(-7), O(-8))=H0(O(-1))^2=0,

   contradicting the required nonzero global map.

The global double-curve lemma in steps 4--7 applies whenever a
genus-two normalization with these exact Euler characteristics has an
actual Cartier `2c_S~2H` supported on the unique embedded lift. It is
not confined to smooth normalization points. It also excludes a
section-stratum candidate if an independently established integral
`2Z` supplies that same Cartier equivalence. There is no assertion
that every section correction has this property.

The proof uses a full globally existing ribbon. It does not infer
global pole or higher-multiplicity behavior from tangent data.

## 2. Every nonendpoint trisecant section case is excluded

**PROVED HERE / independently accepted.** Root accepts the
[nonendpoint continuation audit](2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md)
and its separately written
[relative Morse/branch audit](2026-10-10-session-relative-morse-conductor-branches-independent-audit.md)
after reading their complete arguments. They exclude every genus-two
`lambda=1` mate whose actual conductor line meets C0 at three distinct
points. There is no bound on mate degree or exceptional chain length.

The normal ambient model has actual exceptional-section divisor
`D_T` of class `(2,2)` on `P1_Gamma x P1_f`. The accepted no-B theorem
forces a degree-zero horizontal prime B, with `c.B=0`. The proof first
exhausts every decomposition of `D_T` containing its Gamma fiber:
double B, a graph plus a fixed f-fiber, two horizontal fibers with
distinct f-fibers, and two horizontal fibers with a double f-fiber.
Each is excluded by the full inverse-support condition at contacts
away from horizontal contractions, or by actual smoothness of T at
the specified B contact. This includes B having correction coefficient
zero when a second horizontal prime is present.

An integral residual of class `(1,2)` makes B the sole horizontal
prime and forces its correction coefficient to be one. Its two other
curve contacts supply the two branch values of a degree-two map of
P1, so it crosses B at two distinct transverse points. The relative
formal proof preserves the actual conductor branch ideals and gives
only endpoint A-chains, with all lengths allowed. At the single
curve contact the exact correction coefficient is

    a = ((n+1-k)/(n+1)) / (1+1/(n+1)+1/(m+1)) < 1,

for `n>=1`, `m>=0`, `1<=k<=n`. This contradicts the required `a=1`.
Twelve exact symbolic identities independently countercheck the
all-length formulas; the global support and branch arguments supply
their hypotheses. Two protected-name scaffold failures are preserved
with their exact sources and raw streams in the
[execution record](../validation/2026-10-10-genus-two-nonendpoint-trisecant-continuation-audit/execution-record.json).

This result does not use `c.B=0` to conclude that the images on T are
disjoint: vertical ADE chains can separate them on M. It retains all
reducible and nonreduced conductor configurations before excluding them.

## 3. Preserved weaker bisection reductions and superseded survivors

The independently checked four-blowup and
[even-fiber arguments](2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md)
first left only odd partitions `[3,1]` and `[1,1,1,1]`. The older
second-pencil note's retained `[2,1,1]` was superseded by the local
integral-correction argument. The
[quadratic-descent note](2026-10-10-session-genus-two-bisection-quadratic-descent.md)
then forced a reduced split conductor and a root-of-unity ratio of
unbounded order. Its formula has orientation `m^2=rho*delta`.
Those were necessary conditions, not realized surviving carriers.
The accepted ribbon proof now excludes all of them, including every
root-of-unity order, without changing the preserved weaker sources.

## 4. Exact normal-bundle verification and current repository state

The new independent
[Macaulay2 source](../computations/verify_session_quartic_normal_bundle_2026_10_10.m2)
checks eight exact Jacobian, projective rank and coefficient-matrix
conditions over QQ. Root copied its exact source to an isolated cwd
and observed a successful replay with exit code zero. Its source SHA-256
is `e939b142ee32a89c43e08131f8668a7c5c0e73eebdbcfa81c004de951ff5d62a`.
The [root replay manifest](../validation/2026-10-10-normal-bundle-root-replay/execution-manifest.json)
binds command, source copy, raw streams and elapsed time. This is an
additional execution of one original source, not an additional verifier
for its copied bytes. The normal-bundle splitting itself is inherited
P-009, not claimed as a new theorem.

Live inspection after the pause found HEAD
`2ba77d1a1177db9390693066c6b185040766c089`, title
`2026-10-10 afternoon limit reached`, on
`research/ultra-resume-2026-10-06`. The earlier October 10 acceptance's
`406d63...` live label is a historical observation. Root performed no
Git mutation. The new work and canonical routing are working-tree
evidence beyond that snapshot.

The historical **97 distinct latest-PASS sources / 110 indexed
executions** and October 9 integrity seal remain frozen historical
records. New execution histories and integrity checks are recorded
separately. A record seal certifies bytes and links; its check count
does not certify the mathematical quantifiers.

## 5. Remaining frontier at this acceptance

Genus zero, genus one, normal carriers, smooth normalization and
nonrational normalization have their previously accepted full quartic
exclusions. The genus-two bisection lane is now also excluded.

The remaining integral-quartic lane is the genus-two `lambda=1`
section stratum with an endpoint triple-contact trisecant. The
three-distinct-contact case is now excluded. The two endpoint lines
are exchanged by coordinate reversal; their remaining full local
families are under independent audit. Zero coefficients of a present
horizontal prime, vertical ADE chains linking it to the curve, and
doubled-horizontal residual conductor schemes must remain covered
before a complete endpoint exclusion.

Higher minimum carrier degrees, entirely thick presentations, the
22 retained ancestor-family points with all lower lift lines, the
principal at-most-630-point necessary locus, early-defect strata and
the totally ramified split-sextic boundary remain outside this result.
No theorem forcing a quartic carrier has been established.
