# Independent prelaunch review: one guarded global QQ saturation prospect

Date: 2026-10-16.

Status: **PASS for the reviewed driver and corrected runner sources,
conditional on the runner's fresh in-process preflight passing before
Macaulay2 launch.** This is a source/runtime-control review, not a
mathematical result from the prospect. The reviewer started no CAS,
coefficient assembly, saturation or benchmark.

Reviewed files:

- [global QQ driver](../computations/generalization_quintic_h2_global_QQ_saturation_2026_10_16.m2),
  SHA256 c6d6fceaeb16182a226373dfc19efe3d8816d0cc4797e7186f26bd038051735b;
- [guarded runner](../computations/run_quintic_h2_global_QQ_saturation_guarded_2026_10_16.py),
  SHA256 e47317ab64eeb5968aba839880955a54ba55396ae7358dcb0b5f8718a2f6be04.

## 1. Exact mathematical input and computation scope

The driver loads the already audited load-only input over QQ, checks
seventeen equations and nine ring variables, and calls exactly one
saturation of h2GlobalIdeal by ideal(h2GlobalDomainUnit). That saved
domain polynomial is delta*E*Delta1. The driver introduces no cover
discriminant, K, q coefficient or j inverse. It does not reconstruct
the actual octic or replay any accepted verifier or model assembly.

The driver saves a stage before the load, after the load and before
the saturation; on completion it saves the resulting generators and
the unit-ideal comparison. Its own output explicitly treats a unit
comparison as provisional until an exact certificate in the original
generators is extracted and checked. No mathematical outcome of that
computation is asserted by this review.

Read-only checks confirmed that the current loader still matches
the accepted attempt-05 source digest and both completed model-data
files still match its input digests. The runner now obtains the
expected loader hash from that accepted execution record, rather
than merely recording its current hash and comparing it to itself.

## 2. Fresh preflight is mandatory and fails before M2

The runner checks all bound input hashes before its preflight. It
then loads libproc, checks the declared rusage-info structure size,
and samples its own process. A small private-session child reports
its PID, process group and inherited CPU limits, allocates a small
buffer, and is sampled for resident/footprint data. The same
private-group termination/reap helper is tested on that child.

Any exception in input checking, monitor setup, child probing or
preflight-record writing returns a blocked-before-M2-launch record.
The actual M2 Popen is strictly after that try/except. An older
standalone preflight record does not bypass the fresh preflight in
this runner. If a capability is denied there, no M2 is started.

## 3. Resource controls and process evidence

The reviewed settings are 120 seconds wall time, RLIMIT_CPU soft and
hard both 120 seconds, and a 1536 MiB stop threshold on the maximum
of the M2 PID's sampled resident memory and physical footprint,
polled every 0.25 seconds. The memory control is accurately described
as a polled threshold, not a hard virtual-address or aggregate
process-group memory limit. The wall threshold initiates group
cleanup; a short termination/reap grace period is separate from the
computation's threshold.

M2 is launched with start_new_session=True, so its private process
group is the returned PID. PID/group provenance is written
immediately after Popen. Every subsequent operation, including that
initial record and console output, is within the try/finally that
stops and reaps the owned group. The final source catches exceptions
for recording rather than rethrowing before terminal evidence is
saved. Signal races where a group exits before SIGKILL are handled.

Monitor failure during the actual job triggers cleanup. Normal
completion also checks for remaining members of the private group.
Unexpected group-cleanup exceptions are recorded, with a direct-child
reap fallback; this is not silently reported as confirmed group
absence. Terminal evidence includes the actual process exit code,
reason, elapsed time, child CPU accounting, sampled memory peaks,
cleanup events and stream hashes. Nonzero process exits are
distinguished from successful completion.

The runner refuses a restart if this single attempt already has an
execution record. It freezes its own source and the M2 driver and
records their hashes. This review applies to the specific hashes
above; changes require an updated source review and new bindings.

## 4. Review boundary

The first source draft had a post-Popen gap before its cleanup try
and rethrew exceptions before saving terminal evidence. Those issues
were reported and corrected before this PASS review. The current
runner also binds the expected loader hash and handles the noted
termination races. Read-only Python syntax and current loader/model
binding checks passed; no subprocess or CAS was started by those
checks.

The reviewed sources are suitable for the one authorized bounded
prospect after their fresh preflight passes. The execution record,
stage, exit code and cleanup events must still be inspected after
the attempt. A timeout, memory stop or process failure supplies no
emptiness conclusion. A successful unit-ideal output would still
require its original-generator certificate before mathematical
promotion. This review neither reports a global h2 exclusion nor
closes the quintic or STCI problem.

## 5. Read-only terminal evidence review

The one attempt is now terminal. I read its
[execution record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json),
fresh preflight record, stage, streams, last metrics and prelaunch
source-review metadata. I started no runtime probe, CAS, subprocess
job or rerun of the prospect during this review; checks were file
reads, JSON comparisons and hashes.

The fresh preflight passed before M2 launch, with its probe child
reporting CPU limits 120/120 and its cleanup recording the private
group absent. The separate fresh-preflight file exactly matches the
preflight object embedded in the execution record. The actual M2
PID and private process group were both 39519.

The actual terminal status is **interrupted**, with stop reason
polled-memory-stop-threshold and M2 exit code -15 (SIGTERM). The
recorded wall time is 58.564014667 seconds and child CPU accounting
is 118.528412 seconds. Peak sampled resident memory is 1,611,595,776
bytes, or 1536.9375 MiB, slightly above the declared 1536 MiB polled
threshold; peak physical footprint is 1,597,376,144 bytes, or about
1523.377 MiB. The final metrics file records the same peaks. These
are measured values from the polled process; they do not constitute
a hard memory cap.

Cleanup records SIGTERM-private-group followed by private-group-absent.
Both caught_exception and cleanup_exception are null. Thus the
audited runner's terminal evidence reports the private group gone
after termination and reaping. The supervisor's successful return
must not be confused with mathematical completion of the M2 job.

The last stage is
before-global-QQ-saturation-by-delta-E-Delta1-only. Neither
saturated-ideal.txt nor is-unit.txt exists, and there is no
saturation-complete stage or completion line. Stdout contains only
the loader's successful seventeen-equation/nine-variable message;
its sentence saying no GB/saturation was executed describes that
load-only subscript, not the later driver attempt. Stderr is empty.
No saturation result or unit-ideal claim was produced.

Read-only verification passed for both current and frozen driver
hashes, both current and frozen runner hashes, all three bound
inputs, and both stream hashes against the terminal record. The
reviewed source hashes are unchanged from section 1. The expected
loader and completed-data bindings therefore remained intact for
this attempt.

This attempt supplies a bounded computation/resource record and
**no emptiness conclusion**. The global seventeen-equation problem
after delta*E*Delta1 remains the handoff target. No accepted proof,
model assembly or completed verification was rerun by this audit.
