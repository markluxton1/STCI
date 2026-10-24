# Validation record: quartic automorphisms and bitangent geometry

Date: 2026-10-24. Scope: the new exploratory package linked by the
[synthesis](../../notes/2026-10-24-quartic-automorphisms-bitangents-synthesis.md).
This record documents mathematical review and executable checks. It is
not canonical promotion, a novelty claim, or an STCI conclusion.

## Mathematical reconstruction

- [Projection/group audit](../../notes/2026-10-24-quartic-projection-independent-audit.md):
  independent derivations of the center, complete automorphism group,
  osculating and ruling interpretations, moduli, and the brief
  characteristic-two comparison. The final positive-dimensional-group
  characterization was separately rechecked.
- [Symmetric-square audit](../../notes/2026-10-24-quartic-symmetric-independent-audit.md):
  independent derivations of the secant map, exceptional fibers, conic
  intersections, trace-free construction, and compositions. The reviewer
  independently ran symbolic checks rather than relying on the author's
  verifier alone.

The reviewers found no remaining mathematical discrepancy within those
scopes. Drafting improvements and corrections are preserved in their
audits: the explicit endpoint reconstruction, the reduced diagonal versus
double discriminant in characteristic two, ordered-relation notation in
composition, and the distinction between a reduced scheme image and
cycle/resultant multiplicities. The secant image's precise analytic
singularity type at the two endpoint tangent trisecants is not determined
or needed for the proved fiber, normalization, and differential statements.

## Executable checks

From the repository root, the final exact run was:

```sh
/tmp/stci-z4-env/bin/python \
  research/computations/verify_quartic_automorphisms_bitangents_2026_10_24.py
```

Result: **PASS: 49 exact checks**. The durable
[JSON report](../../computations/quartic_automorphisms_bitangents_2026_10_24.json)
records each check and the actual Python/SymPy versions. The package
requires SymPy 1.14.0, pinned in the
[requirements file](../../computations/requirements-quartic-geometry-2026-10-24.txt).
The local temporary environment is convenient rather than part of the
mathematical evidence. With another Python environment that has the pinned
dependency, the same script regenerates the report without network use.

```sh
python3 research/computations/validate_records.py
git diff --check
```

Results: **Checked 23 canonical records; 0 error(s)** and no whitespace
errors. No canonical result/question record was edited. These metadata
checks do not reprove inherited mathematics.

## Figures and file checks

The [figure README](../../figures/quartic-geometry-2026-10-24/README.md)
documents regeneration. Both final PNGs were visually inspected, and the
SVG versions are retained for export and editing. The conic picture is an
actual real affine slice; the projection picture is explicitly schematic.
SVG generation uses the standard library; PNG generation additionally
uses Pillow, available in the checked bundled desktop runtime.

The final package's relative Markdown links and image destinations were
checked locally for existence: **94 destinations in nine package/navigation
files; zero missing**. Both new Python scripts were compiled for
syntax. The committed file inventory is limited to the four author notes,
two independent audits, computation and figure evidence, this validation
record, and short additions to the research/computation navigation.

The base is the special-lines investigation commit
`51dc4772e6a2b028a1d9559a4bcfbd69be9bd0d6`; inherited proof and audit paths
are preserved. The dedicated branch is
`codex/quartic-automorphisms-bitangents-2026-10-24`.
