# Intake validation and reproduction

Date: 2026-10-19. These checks concern faithful import and two bounded executable
companions. They are not a new independent proof audit or canonical promotion.
No accepted current-repository proof suite was replayed.

## Completed checks

| Check | Outcome | Scope |
| --- | --- | --- |
| `python3 research/computations/validate_space_curves_intake.py` | 6 donors, 31 verbatim snapshots, 0 errors | Per-file hashes, sizes, source/destination mappings, inventory flags and file counts. |
| `python3 research/computations/validate_records.py` | 12 canonical records, 0 errors | Existing canonical metadata remains valid; no result/question record was added or changed. |
| Python `compile()` on the 6 imported Python scripts and new intake validator | 7 files passed | Syntax only, without executing the donor programs or writing bytecode caches. |
| Imported `scripts/finite_normal_jet_certificate.m2` | Exit 0; all exact checks passed | Twisted cubic, 16 characteristic/binomial cases, insufficient-cutoff counterexamples and coefficient-field trap examples. |
| Imported `experiments/c4_root_collision.py` | Exit 0 | Exact quartic restriction, gradient, Taylor and blowup coefficients; formal Morse/type interpretation remains a separate argument. |

The Macaulay2 run used `/opt/homebrew/bin/M2` and the imported VI project root.
The collision run used `python3` and the imported IV project root, with
`PYTHONDONTWRITEBYTECODE=1`. Commands, relative working directories, elapsed
times and exit codes are recorded next to their exact stdout/stderr:

- [Finite-jet run metadata](../../validation/2026-10-19-space-curves-intake/finite-normal-jet.run.json)
  and [stdout](../../validation/2026-10-19-space-curves-intake/finite-normal-jet.stdout.txt).
- [Conormal-collision run metadata](../../validation/2026-10-19-space-curves-intake/conormal-collision.run.json)
  and [stdout](../../validation/2026-10-19-space-curves-intake/conormal-collision.stdout.txt).

The general statements are supported by their imported arguments and recorded
audits, not inferred from these finite examples. In particular, the coefficient
script tests selected constant pairs; the universal constant-coefficient assertion
uses the transcendental-residue argument in VI-012 and its audit.

The staged whitespace check reports two original Markdown hard line breaks
(trailing double spaces) in III's verbatim worked note, lines 3 and 4. They are
retained to preserve the donor bytes and hashes. Authored files have no whitespace
errors.

## Run from the STCI repository root

Import integrity and canonical metadata:

```sh
python3 research/computations/validate_space_curves_intake.py
python3 research/computations/validate_records.py
```

For each example, start a separate shell at the STCI repository root. Changing to
the imported donor root preserves original relative run paths.

```sh
cd research/archive/space-curves-2026-10-19/space-curves-vi
/opt/homebrew/bin/M2 --script scripts/finite_normal_jet_certificate.m2
```

Expected final output: `All exact checks passed. General constant-coefficient
exclusion is proved in Artifact 012.`

```sh
cd research/archive/space-curves-2026-10-19/space-curves-iv
PYTHONDONTWRITEBYTECODE=1 python3 experiments/c4_root_collision.py
```

Expected key output: `strict_transform_r_coefficient=2, so p2_local=0`.
The script's local-type labels use the formal interpretation described in its
docstring; the polynomial assertions do not mechanize analytic equivalence.

## Retained but not replayed

- The [one-node E6 enumeration](space-curves-i/research-state/scripts/nodal_cubic_quintic_lattice.py)
  is standard-library Python and expects 15 simple lines, 120 admissible quintic
  classes and disjoint-line count `[3]`. The finite enumeration is not by itself
  a proof of geometric effectiveness or completeness; the supplied source
  arguments supply those steps. Its exhaustive Cartesian enumeration can be slow.
- The [quintic coordinate script](space-curves-i/research-state/scripts/vahlen_quintic_exact.py)
  uses the standard library. Its [corrected incidence companion](space-curves-i/research-state/scripts/vahlen_base_locus_discriminant.py)
  additionally requires SymPy and loads the coordinate script by its original
  relative path. Run it from the imported I root if a future investigation needs
  it; use I-023 for the corrected residual-line coordinates.
- The [III symbolic companion](space-curves-iii/research-state/experiments/explicit_examples.py)
  requires SymPy. Its existing output is preserved in the accompanying worked
  note; the script alone does not validate the divisor-class or conductor facts.
- The full IV conormal helper's main program was not run; it was imported by the
  collision script as a dependency. Its broad finite samples do not classify all
  conormal divisors.
- No donor source tree was modified, no donor Git history was merged, no remote
  literature source was freshly verified, and no full parameter-locus elimination
  was performed.

## Local navigation check

All relative file links in this packet's two authored Markdown guides, and the
two new intake links in the research/archive indexes, were resolved locally.
Links and historical IDs inside the verbatim donor files retain their source
meaning. The [intake review](README.md) explicitly records the relevant omitted
dependencies, status conflicts and absent VI “Artifact 013”.
