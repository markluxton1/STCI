# Independent audit: the lambda-one case without a degree-zero horizontal prime

Date: 2026-10-10. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted, bounded conditional
exclusion**. This does not exclude the full lambda-one stratum.
No canonical frontier file was edited.

Binding source: [the free-chain and line-budget proof](2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md),
sections 1--4, SHA-256
`f6701f0cee494573469d15e6bc18d76b787e8963701a4795c4ba2905f00f2522`.
The source originally marked its two-line argument pending parent
audit; this separate note records that audit without modifying
the frozen source.

Assume the accepted lambda-one plane marking and the smooth
embedded lift. Assume additionally that the possible horizontal
degree-zero exceptional prime B=e0-e_i-e_j is absent. Then no
mate can exist. Consequently a surviving lambda-one mate must
have that B present. The two free-child and single-satellite
patterns with B present remain outside this proof.

## 1. Coverage and the one-line argument pass

The [marked-prime audit](2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md)
shows that the remaining horizontal exceptional primes are one
or two proper plane lines. There must be at least one, since
K.Z=1 is the sum of horizontal coefficients. Absence of B gives
every blowup center at most one direct child, excluding all
satellites. Every cluster is a free chain. A horizontal line
has four on-line centers; once its chain leaves the line it
cannot return, because the later center lies above a different
point of the current exceptional divisor from the strict line.

For a single horizontal line H, a cluster with s on-line and
t off-line centers attaches the entire A_(s+t-1) chain at node
s. Eliminating its intersection matrix contributes st/(s+t),
not just the number of off-line centers. The horizontal
coefficient in Z is one, so these contributions sum to two.
Cauchy, using sum s<=4 and sum t<=4, forces all four on-line
and four off-line centers to participate and t=s in every
cluster. The integral anti-nef uniformizer cycle with Y_H=1
has attachment coefficient at least min(s,t). Thus its
neighboring coefficients sum to at least four, while
Y.H<=0 requires their sum at most three. This excludes the
single horizontal proper-line case. The discrete-slope proof
of that integer chain bound in the source is valid.

## 2. The two-line coverage and equality argument also pass

Two disjoint strict horizontal lines share exactly their
original plane intersection as one simple center. Their
supports therefore use seven simple centers, leaving one
center outside their union. The shared free chain can follow
only one line. If it later leaves that line, its newly null
terminal connects the entire null prefix to both line primes,
contradicting one positive-h-degree prime per exceptional
fiber. Thus that chain stops on the line, contributes an
endpoint A_k arm to the other line, and k<=3.

The sole outside center can add at most one other arm. Its
preceding on-line chain has s<=3 and one off-line center, so
its contribution is s/(s+1), not necessarily 1/2. A shared-
cluster continuation is forbidden by the preceding connectivity
argument. These are all cases; other placements add no arm.

If the two arms are split between the lines, their total
horizontal coefficient is at most 8/9. If both lie on the same
line, it is at most one. The required sum K.Z=1 forces equality
in the second case, with k=s=3. The geometric configuration
then uses all eight centers in two clusters whose proper roots
P,Q both lie on the same horizontal line. The first child
directions at P,Q are the two respective horizontal lines.

A vertical exceptional proper line would pass through p0 and
two simple centers. It cannot contain both P,Q, since their
joining line is horizontal and avoids p0. At either proper
root its direction differs from the first child's horizontal
direction, so it cannot contain any later center in that
cluster. There are no other centers. No vertical proper
exceptional line therefore exists in the equality case. The
only positive-h-degree exceptional primes are the two horizontal
lines, with coefficient sum one. This gives h.Z=1, contrary
to the required integral marked identity h.Z=3. The two-line
case is excluded as well.

## 3. Exact surviving boundary

This proof closes the lambda-one subcase with B absent. It
preserves all infinitely near free-chain patterns and the
stronger integral local uniformizer-cycle test. It does not
cover B present, where a unique satellite can make B attach
to an internal chain vertex. No star-shape assumption for that
remaining graph is justified here. The full lambda-one lane,
the lambda-zero bisection lane, and the genus-two mate problem
remain open at the pause.
