# Terminal record: one whole-h2 global QQ saturation prospect

The one authorized global prospect ended without a mathematical result.
It loaded the accepted seventeen-equation, nine-variable input over
`QQ`, reached the single saturation by `delta*E*Delta1`, and was stopped
when the M2 process exceeded the sampled memory threshold. This is
bounded computation evidence; it does not prove that the incidence is
empty or nonempty. There is no unit-ideal output or certificate.

The authoritative data are the
[execution record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json),
[fresh preflight record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/preflight-record.json),
[last sampled metrics](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/live-metrics.json),
and [last stage](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stage.txt).

## Actual execution and cleanup

| Field | Recorded value |
| --- | --- |
| M2 PID and private process group | `39519` |
| Supervising tool session | `82234`, subsequently closed |
| M2 start UTC | `2026-10-16T11:35:33.981234+00:00` |
| M2 terminal UTC | `2026-10-16T11:36:32.545921+00:00` |
| Wall time | `58.564014667` seconds |
| CPU time | `118.528412` seconds |
| Actual M2 exit | `-15` (SIGTERM) |
| Stop reason | `polled-memory-stop-threshold` |
| Peak resident bytes | `1611595776` |
| Peak physical-footprint bytes | `1597376144` |
| Memory stop threshold | `1610612736` bytes (1536 MiB) |
| Last stage | `before-global-QQ-saturation-by-delta-E-Delta1-only` |
| Cleanup | `SIGTERM-private-group`, then `private-group-absent` |
| Caught or cleanup exception | Both `null` |

The private process group was terminated and the M2 child reaped. The
owner subsequently resumed tool session `82234`; the supervisor returned
exit zero and the terminal text
`TERMINAL interrupted polled-memory-stop-threshold exit -15`.
The supervisor exit zero records successful handling of the bounded
interruption. It is not an M2 success code. There is no live execution
handle from this prospect and no restart was made.

The configured wall threshold was 120 seconds, with cleanup grace; the
OS CPU soft and hard limits were both 120 seconds. The memory guard
sampled `max(resident,physical-footprint)` for the M2 PID every 0.25
seconds. It is a polled stop threshold, not a hard aggregate or virtual
memory bound. A fresh own-child preflight passed before the M2 process
was launched, including inherited CPU-limit verification, memory
monitoring, and private-group termination/reaping.

## Exact source, input and output binding

The
[frozen M2 driver](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/source.m2)
has SHA256
`c6d6fceaeb16182a226373dfc19efe3d8816d0cc4797e7186f26bd038051735b`.
The
[frozen runner](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/runner.py)
has SHA256
`e47317ab64eeb5968aba839880955a54ba55396ae7358dcb0b5f8718a2f6be04`.
These are the independently reviewed hashes in the
[prelaunch source record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/prelaunch-source-review.json).

The loader hash was checked against the accepted load-only execution
record. The exact seventeen-generator data have SHA256
`c29dff74c9b120df41b7c59852d81d88d9d7004fa6e8586cda961eafd82e5008`;
the exact domain polynomial has SHA256
`4bd9af1e22bcf421017a2b0213cdc74e5dfbd9451860c1c644c24104977e778b`.
The loader itself has SHA256
`f5db87f6ea8dbd7d32411621bec3c68221ceaa9dc48a54e5dd3e82312535d1b4`.
All are bound in the execution record. No accepted coefficient
assembly, theorem verifier, or prior prospect was rerun.

The sole new algebra operation was

```macaulay2
saturate(h2GlobalIdeal, ideal h2GlobalDomainUnit)
```

over `QQ`. Its domain is exactly `delta*E*Delta1`. There is no inverse of
the rational-cover determinant, quadratic discriminant, a q coefficient,
or `Jbar`; repeated and cover-boundary points remain in this model.
The precise geometric scope is the accepted
[global monic ODE incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md)
and its
[independent audit](2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit.md).

The 193-byte
[stdout](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stdout.txt)
contains only the loader's confirmation of the exact saved input. Its
line `No GB/saturation executed` describes the load-only library stage;
the driver's later stage marker records entry into the new saturation.
The
[stderr](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stderr.txt)
is empty. Neither `saturated-ideal.txt` nor `is-unit.txt` exists, and no
`saturation-complete` marker was reached.

The generic earlier bounded driver was not used for this prospect. Its
exact checkpoint bytes are retained as
[generic-runner-at-checkpoint.py](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/generic-runner-at-checkpoint.py),
recovered from checkpoint
`bf124f8ab962ef0ed4085397034c50ee8d0d7162`, with SHA256
`55d370623116a153645974d755e3e0805a3eb054f087734d5206ddb7128b7018`.
Thus this new runner does not change the source binding of earlier
execution records.

The global h2 incidence remains an accepted necessary target whose
emptiness has not been decided. No additional CAS run is part of this
record.
