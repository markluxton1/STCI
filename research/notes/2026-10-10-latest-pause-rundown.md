# Latest-pause rundown and live audit supplement

Snapshot: 2026-10-10, approximately 13:35 UTC. This is a status record,
not a replacement for the canonical audited state or a new integrity seal.
It distinguishes the saved October 9 frontier from the October 10 audit
results that have just arrived. No novelty claim is made.

## Global scope

The universal integral projective-curve STCI problem remains **OPEN in
this repository**. The unrestricted characteristic-zero problem for
`C0=[s^4:s^3t:st^3:t^4]` also remains **OPEN**. The recent work concerns
integral quartic carriers and does not force an arbitrary presentation to
have a quartic member. Higher minimum carrier degrees and entirely-thick
presentations remain outside the quartic exclusions.

## Established quartic frontier

The [canonical audited state](../AUDITED_STATE_2026-10-07.md) and
[October 9 acceptance](2026-10-09-session-results-acceptance.md) retain
the independently accepted results:

- Every normal integral quartic carrier for fixed `C0` is excluded in
  characteristic zero, in every mate degree.
- Every sectional-genus-zero normalization, and every smooth
  normalization, is excluded in every mate degree. The complete
  degree-four minimal-degree classification includes both smooth scrolls,
  the Veronese surface, and the rational-normal-quartic cone.
- Every nonnormal integral quartic containing any smooth rational
  degree-four curve has rational normalization, without a mate hypothesis.
- A genus-one normalization is an ADE degree-four del Pezzo surface.
  Under a mate, the complete exceptional type is `4A1` or `A3+2A1`,
  the mate degree is even, and the actual linear equivalence is `2c~2H`.

## Genus one: complete argument, final acceptance integration pending

The [remaining-partitions proof](2026-10-09-session-ribbon-repeated-partitions-complete.md)
covers `[4]`, `[3,1]`, and `[2,2]`, including coefficient and direction
boundaries. The earlier squarefree and `[2,1,1]` arguments complete the
five partitions of the four conductor-contact zeros. The proof retains
the literal omitted-middle projection center and the entire conductor.
It excludes mates in every degree, rather than merely a bounded range.

The [October 10 interface audit](2026-10-10-session-genus-one-interface-independent-audit.md)
has finished and accepts the whole implication chain through squarefree
and `[2,1,1]`: full inverse support, actual Cartier double, singular ADE
points, complete ribbon net, ambient lift, and fixed projection coordinates.
It states that acceptance of the remaining-partition proofs closes every
genus-one quartic carrier, with no further interface hypothesis.

The separate remaining-partition auditor has reported a successful new
Macaulay2 countercheck: **29 exact conditions**, terminal exit zero. Its
[saved result](../validation/2026-10-10-repeated-partitions-independent-audit/result.json)
records universal net/support ideal equality for `[3,1]` and `[2,2]`, an
exhaustive direction chart, and an independent conductor section proving
the all-powers obstruction. At this snapshot its written audit and final
provenance record are being saved. Thus the complete exclusion has passed
the reported independent mathematical checks; canonical reconciliation
and root acceptance of the final saved audit are still outstanding.

A real evidence-attribution error was found in the old `[2,1,1]` note:
its cited current Python checker lacked some claimed checks. The written
proof passed the separate audit. A new M2 companion supplied **42 exact
identities over QQ**, with terminal PASS, and
[both execution attempts](../validation/2026-10-10-genus-one-interfaces/execution-record.json)
are retained. Historical checker passes must not be attributed to the
previously missing identities.

## Genus two: structural progress, no mate exclusion

The [adjoint model](2026-10-09-session-genus-two-adjoint-conic-model.md)
has independently accepted core inputs: on the rational minimal resolution,
`L^2=4`, `K.L=-2`, and `f=K+L` is a basepoint-free rational pencil with
`f^2=0` and `L.f=2`. Its exceptional primes are vertical `(-2)` curves
and at most two disjoint horizontal `(-3)` sections. The separate
[mate-strata audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md)
retains BOTH possibilities

    (lambda,q)=(0,4):  c#^2=0, f.c#=2;
    (lambda,q)=(1,3):  c#^2=1, f.c#=1.

The claim that only `q=4` survives was corrected and must not be reused.
The newly saved [marking and section pause audit](2026-10-10-session-genus-two-marking-and-section-pause-audit.md)
accepts the owner's remaining ruled/plane marking sections, while retaining
the exceptional-graph obligations. In particular, internal chain
attachments and satellite blowups invalidate proposed simple arm-budget
or star assumptions. Conditional small-graph bounds do not constitute a
geometric exclusion until their hypotheses are proved. Both mate strata
remain open.

The new [entire-conductor independent audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
accepts a substantial additional reduction without a mate: all singularities
of the normalization are rational, the actual downstairs conductor scheme
is a reduced line with no embedded or isolated points, and the entire
upstairs conductor is a finite flat double cover with algebra

    O_P1 direct-sum O_P1(-2),  w^2=delta,  delta in H0(O_P1(4)).

This retains singular and nonreduced covers, including `delta=0`.
It does not make the upstairs conductor Cartier. The quartic has generic
order exactly two along the line. Turning the conductor/adjoint model into
a uniform mate obstruction is still required. An ambient line-blowup lift
has a new proposed argument but is not certified by this snapshot.

## Other open routes and continuation record

The principal MF6 finite candidate locus is necessary, not an actual
classified carrier list. Its at-most-630 bound does not exclude those
parameters. The 22 second endpoint-family points of degrees `3,4,15`
retain every lower lift line. Remaining common-quartic-ancestor strata,
early `e=2` defects, higher carrier degrees, entirely-thick presentations,
and the totally ramified split-sextic boundary remain open.

The historical [October 9 seal](../validation/2026-10-09-late-continuation-seal/README.md)
records **97 distinct sources with latest PASS evidence / 110 explicitly
indexed executions**, plus **2006 integrity checks / 313 scoped local
links**. These counts apply to that frozen record; the October 10 results
have not been silently added, and the seal does not certify later edits.

Live Git HEAD was inspected as `406d63db72000a3951497a0ba2a8fbfbc13e8ead`,
commit title `2026-10-09 afternoon limit reached`. The morning HEAD in the
older acceptance is historical. New research files are present as
untracked files; this status pass performed no Git mutation.

The old temporary CAS Python currently lacks SymPy. The new independent
checks use the verified Macaulay2 1.26.06 runtime. This current runtime
failure does not invalidate preserved historical execution evidence.

Immediate continuation: finish and reconcile the full genus-one audit;
then pursue the genus-two conductor/adjoint model while preserving both
mate strata and all nonreduced conductor cases. Even full exclusion of
every quartic carrier would leave the unrestricted problem open.
