# Independent coverage review and repairs before the final seal

Reviewer: `checker_coverage_review`, delegated by
`record_continuation_integrity`, 2026-10-10. The reviewer read files but
did not change them, execute mathematical verifiers, or create a seal.
The parent auditor implemented the repairs below in its owned checker.

The earlier checker had correct historical and October 10 source/run
accounting, and there was no observed drift in the files it bound. Its
remaining weaknesses concerned the strength and coverage of the
integrity assertion. These are now addressed as follows:

1. Bound files retain their first-observed hashes. A subsequent binding
   with different bytes fails, and every bound file is rehashed at the
   end. The complete October 10 note inventory and live HEAD must also
   remain unchanged during a run.
2. Independently observed exact trust anchors are pinned for the frozen
   October 9 result, checker and execution manifest, and October 8
   continuation index. The prior October 10 acceptance is now retained
   as a separately pinned historical record as root creates a new
   continuation acceptance. Coordinated changes to sibling files can no
   longer satisfy the historical unchanged assertion merely by updating
   their hashes to agree with one another.
3. All October 10 note files are discovered and bound, including the
   previously omitted bisection quadratic-descent note and the historical
   latest-pause rundown. Their status headers are observations; only the
   root acceptance promotes a mathematical scope.
4. The accepted no-zero-horizontal audit's explicit input digest is
   checked against the actual line-budget source, as was already done
   for the normal ambient conic model's audited inputs.
5. Final result creation uses exclusive `open("x")`. Parallel final
   checker processes cannot overwrite a previously created result.
6. The D5 source exception is narrowed to an exact current digest. The
   proof sections 1--5 are compared byte-for-byte with the frozen source
   snapshot. The permitted changes are the status header and acceptance
   or model-coverage routing in sections 6--7; calling them only a header
   repair would understate their actual extent.
7. Canonical routing requires an actual parsed local Markdown link to
   the precise acceptance path, rather than the filename occurring as
   arbitrary text. Existing linked files inside the repository are also
   bound by bytes, rather than merely checked for existence.
8. Fresh read-only runtime probes are preserved separately, adding zero
   mathematical executions. They do not enlarge the historical index or
   become mathematical evidence by being included in the integrity
   scope.

The selected Markdown parser remains deliberately bounded. It handles
ordinary inline destinations but not reference-style definitions,
balanced destination parentheses or escaped delimiters. No such edge
case was found in the review's then-tracked files. Those limits remain
explicit in the checker result. File existence and exact bytes do not
verify the mathematical proposition or an external literature source.

The final seal remains pending the root's canonical reconciliation.
Preliminary passes do not authorize a claim that the current mathematical
frontier is sealed, nor that the universal STCI problem is resolved.
