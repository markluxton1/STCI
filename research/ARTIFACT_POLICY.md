# Mathematical artifacts

Keep proofs, explicit constructions and counterexamples, concrete open questions,
and exact computations needed to establish surviving claims. Retain the smallest
adequate support, with inputs, mathematical interpretation, and a usable checking
command when computation is essential. A second implementation is useful only
when it supplies distinct verification or an argument the first does not.

Do not retain execution logs, environment diagnostics, repeated PASS output,
regenerable bulk dumps, chronological handoffs, or migration manifests merely as
history. Inspect their content before removal: some contain unique corrections or
essential proof steps. Replace necessary support with a reviewed argument or
compact exact certificate first. Git history preserves earlier versions.

Do not add large generated artifacts to ordinary Git. An essential external
artifact needs an accessible location, integrity identifier, and a precise
explanation of the claim depending on it. A checksum or regeneration recipe is
not evidence that the computation was completed. Do not rewrite shared history
or delete source branches as part of working-tree consolidation.

Keep claim scope and independent review status with the mathematical statement;
follow [authority and retention rules](AUTHORITY.md).
