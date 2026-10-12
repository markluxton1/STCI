# Post-seal quintic continuation integrity record

This directory began as an interrupted October 11 extension. The saved
`check_record.py` is that unfinished draft and was not finally executed.
Its prepared antecedent, the independent coverage review and inventory,
and the separately completed endpoint inventory are retained unchanged.
Root completed the record on October 12 using the separate
[check_quintic_record.py](check_quintic_record.py), without representing
the interrupted draft as a successful seal.

The new checker executes no mathematical source. It checks the frozen
prior seal and all its noncanonical bindings; current accepted proof
versions; the independently inventoried 91 files and endpoint inventory;
the five captured nonendpoint attempts; link routing; current HEAD and
canonical stability. It preserves original-metadata, reconstructed-source,
unbound-original-stream and direct-tool-observation limitations. A PASS
does not prove a theorem, certify novelty or resolve unrestricted STCI.

The mathematical frontier comes from the
[root acceptance](../../notes/2026-10-11-session-quintic-continuation-results-acceptance.md).
The entire intrinsic endpoint quintic family is excluded. The nonendpoint
modulus, other quintic normalizations and higher carriers remain open.
The new nonendpoint direct proof has a separate mathematical audit pending.

The [independent coverage review](independent-coverage-review.md) covers five
histories: 35 disclosed M2 script executions, 12 exit zero and 23 nonzero,
with 14 original metadata-only rows and 21 captured raw-stream rows. Its
77 declared comparisons and 91 observed files are not new mathematical
executions. Some exit-zero scripts are exploratory or incomplete versions.

The [endpoint inventory](endpoint-execution-coverage.json) separately covers
28 captured executions, including 15 exit zero, eight setup/export failures
and five actual assertion failures. Five additional local-excess direct
tool observations have weaker local provenance and are not merged into
those captured executions. Source copies and duplicate aggregate record
views do not supply independent verifier implementations. Original raw
stream hashes absent from a record are newly observed as such, rather
than invented retroactively.

The nonendpoint folder has five captured attempts: four nonzero and one
passing repair. The final source has seven supporting conditions plus
one PASS ALL output label. These conditions constrain a residual section
and a specified ramified-line stratum; they do not exhaust nonendpoint
projection parameters.

The final command is

```sh
python3 research/validation/2026-10-11-quintic-continuation-seal/run_final_seal.py
```

It exclusively creates `result.json`, raw checker stdout/stderr, and
`execution-manifest.json`, refusing to overwrite any. The checker requires
the separately recorded root readiness and preserved accepted-input
digests. Preflight writes only a replaceable observation. Read the actual
result and manifest for the completed status, counts and hashes. Both
old and new seals concern their observed snapshots; neither freezes the
future checkout or substitutes byte counts for mathematical scope.
