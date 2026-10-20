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


## Independent merge review — 2026-10-20

This maintenance review independently checked intake commit
`ef1cad0ab8fada44d8b9988c929c2cf6f2f319ca` against target base
`84dacd99c54915b1bbb224bb01565f01716445de`. It did not rely on the
completed-check table above. The review covered the full 44-file diff, with
separate source-fidelity, navigation/scope, and authority reviews. It performed
no new independent mathematical proof audit, including of VI-011.

### Source fidelity and inventory

All six original donor directories were available. Every one of the 31 selected
original files was read and compared byte for byte with its archived destination;
all matched, totaling 203,435 bytes. All manifest source/destination mappings,
SHA-256 digests, byte counts and import flags matched. There were no missing or
unregistered snapshots within the declared selection.

| Donor | Source artifact inventory | Verbatim snapshots |
| --- | ---: | ---: |
| I | 19 | 14 |
| II | 9 | 0 |
| III | 14 | 4 |
| IV | 32 | 5 |
| V | 6 | 0 |
| VI | 18 | 8 |
| Total | 98 | 31 |

The donor artifact directories were independently enumerated: all 98 recorded
artifact paths, titles and source hashes agreed; the only other files in those
directories were six `.gitkeep` placeholders. Donor IDs and per-donor artifact
paths were unique. II and V are screened collections with explicit no-import
decisions, so no corresponding snapshot directory is required.

I and VI still had the recorded branches and HEADs. All 22 selected files from
those two donors were absent from their recorded commits and remained untracked.
The other four donors had no local Git metadata. This verifies fidelity to the
available working-tree originals; it does not reconstruct intake-time file
history or turn the surrounding Git HEADs into immutable source commits.
If those local donors later become unavailable, the repository-only intake
validator establishes internal consistency, not an independent source comparison.

The following read-only check reproduces selected-source comparisons and all
98 inventory hash comparisons while the manifest's original local roots exist:

```sh
python3 - <<'PY_SOURCE_AUDIT'
import hashlib
import json
from pathlib import Path

root = Path.cwd()
packet = root / "research/archive/space-curves-2026-10-19"
manifest = json.loads((packet / "manifest.json").read_text())
inventory = json.loads((packet / "source-artifact-inventory.json").read_text())
sources = {s["id"]: Path(s["local_root"]) for s in manifest["sources"]}
for item in manifest["files"]:
    original = (sources[item["source_id"]] / item["source_path"]).read_bytes()
    archived = (root / item["destination_path"]).read_bytes()
    assert original == archived, item["destination_path"]
    assert len(original) == item["bytes"], item["source_path"]
    assert hashlib.sha256(original).hexdigest() == item["sha256"], item["source_path"]
for donor in inventory:
    for item in donor["artifacts"]:
        original = (sources[donor["source_id"]] / item["path"]).read_bytes()
        assert hashlib.sha256(original).hexdigest() == item["sha256"], item["path"]
print("31 selected source files and 98 source inventory hashes match.")
PY_SOURCE_AUDIT
```

### Alternate historical ZIP revision

The available I donor ZIP
`/Users/markluxton/Projects/space_curves/research-state-terra-medium.zip`
contains an earlier revision of
`research-state/artifacts/ARTIFACT-20260821-013.yaml`:

| Source revision | Bytes | SHA-256 |
| --- | ---: | --- |
| Earlier ZIP entry | 5,298 | `f60d9a134bba57c413287697827d3cf5824ac58e20654fca2a2726e28a91ebe6` |
| Declared working-tree source and archived snapshot | 5,395 | `03a72f692d7fd2d29f4445afc9f5359070ebdc8721e8922670d9d52d859c42ab` |

The working-tree revision replaces the old residual-line display with
`V(3U2-5U0,3U3-5U0-5U1)`, cites I-023 and adds `EVENT-20260821-028` to its
history references. The archive correctly preserves the declared working-tree
revision. This is a documented source-version difference; no donor snapshot was
rewritten during the merge review. I-023 and the incidence companion are absent
from that older ZIP; its other 11 selected entries match.

All four selected files in III's `research-state-sol-high.zip` match. The three
selected entries in IV's `research-state-terra-max.zip` match; its two experiment
scripts are absent from the ZIP and were verified against their working-tree
originals instead. These ZIPs are supplementary historical evidence, not the
source revision declared by the manifest.

### Independently executed repository and replay checks

- Intake validator: six donors, 31 snapshots, zero errors.
- Canonical-record validator: 12 records, zero errors.
- Core Markdown checker: 123 destinations in 12 documents, zero missing.
- Targeted `scripts/check_markdown_links.py` on both packet guides and the two
  edited indexes: four documents, zero local-link issues. Historical donor-relative
  commands and IDs remain source-context references; this selective packet does
  not close their full dependency graph or verify remote literature URLs.
- Full historical Markdown checker: 2,483 destinations in 647 documents, 361
  missing. An independently reconstructed target-base scan had 2,436 destinations
  in 637 documents and exactly the same 361 missing-link issue lines. No new
  failures were introduced. CI treats this historical scan as informational;
  the core-navigation job is gating.
- Syntax-only `compile()` on six imported Python scripts and the intake validator:
  seven files passed without writing bytecode.
- The two bounded companions were rerun from their documented donor roots:
  `/opt/homebrew/bin/M2 --script scripts/finite_normal_jet_certificate.m2` and
  `python3 -B experiments/c4_root_collision.py`. Both exited zero, and stdout
  and stderr matched the recorded files byte for byte. This is reproducibility
  evidence for those examples, not a proof audit of the imported general claims.
- The only whole-diff whitespace findings were the two original hard line breaks
  already documented above. They remain unchanged to preserve donor bytes.

### Authority and scope decision

The full diff contains only this archive packet, its validator and bounded-run
evidence, and the two one-line index additions. Root `README.md`, `AGENTS.md`,
`research/AUTHORITY.md`, canonical result/question records, `STATE.md`, `FRONTIER.md`
and workflows are unchanged. All additions are regular files; there are no mode
or symlink changes. Source status labels remain historical. Corrected coordinates,
superseded quartic priorities, omitted dependencies and reviewer-independence
gaps remain explicitly qualified in the [archive guide](README.md).

VI-011 remains an imported source proof/audit packet pending a separate reviewed
promotion. This maintenance review adds no independent mathematical proof audit,
new theorem, or change to the established mathematical frontier. The material
archival checks pass; merge remains conditional on passing PR checks at the
reviewed head revision.
