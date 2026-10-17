# A simple conductor-root coefficient at target infinity

Date: 2026-10-12. Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **EXACT COEFFICIENT IDENTITY, WITH A CAPTURED STANDARD-LIBRARY CHECK**.
The auxiliary [diagonal norm note](2026-10-12-session-nonendpoint-diagonal-norm-identity.md)
and its fifteen-check source remain frozen. No previously sealed file or
canonical summary is edited here.

Let `F(p)` be the exact polynomial bound in that note and put `a=B=0`.
Direct coefficient extraction gives, for every `delta,G,J`,

    coefficient_(p^8) F=0,
    coefficient_(p^7) F=delta^7.                    (1)

Since `delta!=0`, homogenization of `F` to degree eight has exactly a
simple zero at `p=infinity`. This uses the literal section, not an
upper bound inferred from its first-normal zero locus.

The [new coefficient checker](../computations/verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py)
reads the frozen 344-monomial primitive polynomial, validates its exact
SHA-256, and reconstructs it through elementary integer polynomial
arithmetic using Python's standard library. It performs no `eval`, uses
no CAS dependency, and does not replay the fifteen-check M2 source.
The [captured run](../validation/2026-10-12-nonendpoint-conductor-infinity-coefficient/20261012T213137628207Z/execution-record.json)
records the source, input and raw-output hashes and passed with exit
code zero and empty stderr.

The following geometric consequence depends on the separate
[restricted-conductor determinant argument](2026-10-12-session-nonendpoint-restricted-conductor-determinant.md).
Its independent mathematical audit is ongoing at this note's freeze.
Once that argument identifies `F` with a unit multiple of the actual
degree-eight conductor restriction, its zero at target infinity has
exactly length one on every admissible projection with `a=B=0`.
The conormal cubics already have a common root at that endpoint, because
their constants vanish there (`a=b=0`). Under full inverse support all
other conductor zeros must be supported at another common conormal
root, or at the A4 point if `J=0`.

In particular, with `J!=0`, a parameter value for which the sole common
conormal root is target infinity cannot have full inverse support:
that point has length one while the total conductor restriction has
degree eight. This is conditional on the actual-conductor geometric
bridge, rather than inferred solely from a polynomial degree match.
It is not a full common-root incidence exclusion or a universal STCI
statement.
