# Exact evidence for the (4,4) characteristic/conormal proposal

Date: 2026-10-23. Base checkout: `main` at
`3753bf715d855dc38c38d03ad4ed0d87e67369a8`. Research branch:
`codex/quartic-characteristic-conormal-2026-10-23`.

This is evidence for the new
[explanatory note](../../notes/2026-10-23-quartic-characteristic-conormal.md)
and [filtered proof proposal](../../notes/2026-10-23-quartic-44-filtered-proof-proposal.md).
No canonical theorem was created or modified. The existing all-degree
quartic-carrier exclusion was not rerun. The new proof's inherited BF and
primitive-direction classification premises are stated in its source note;
they are not established by PASS output.

All four commands were run from the repository root with exit status zero:

```sh
python3 research/computations/verify_44_quartic_symbol_comparison_2026_10_23.py
/opt/homebrew/bin/M2 --script research/computations/verify_44_mu4_family_2026_10_23.m2
/tmp/stci-z4-env/bin/python research/computations/verify_44_filtered_contact_2026_10_23.py
/tmp/stci-z4-env/bin/python research/computations/audit_44_filtered_contact_2026_10_23.py
```

The symbol script uses the standard library. The contact runtime was Python
3.15.0 with SymPy 1.14.0; any compatible Python/SymPy runtime can replace
this temporary path. Macaulay2 was installed at the displayed path, through
Homebrew version `1.26.06_1`.

- [quartic-symbols.log](quartic-symbols.log): complete integral 18-column
  kernel of the 35-monomial restriction source, both first-symbol images,
  `q^2` kernel, and target dimensions. Exact rational and mod-two arithmetic.
- [mu4-family.log](mu4-family.log): integer expansion, characteristic-two
  ideal, characteristic-zero initial ideal, roots-of-unity substitution,
  homogeneous four-component scheme equality over `QQ(i)`, and contact three.
- [filtered-contact.log](filtered-contact.log): new degree-three-defect
  cocycle/annihilator/contact calculation, complete quartic contact sources,
  and nonzero cubic-contact determinants. Its primitive-type contact formulas
  and orbit exhaustion are explicitly inherited from accepted evidence.
- [independent-contact-audit.log](independent-contact-audit.log): separate
  direct Taylor construction, exact rational identities, a rigorous modular
  rank lower bound of 33, and independent cubic-contact determinants.

Independent mathematical assessments are recorded in the
[geometry/symbol audit](../../notes/2026-10-23-quartic-geometry-symbol-independent-audit.md)
and [filtered-proof audit](../../notes/2026-10-23-quartic-44-filtered-proof-independent-audit.md).
The latter checks the passage from the complete pencils and their contact
determinants to the proposed nonexistence proof, including finite defect
points and the precise inherited scopes.

Development-only failures were discarded before these runs. The substantive
sign correction in the degree-three-defect exploratory calculation and the
rejected legacy ruling-line assertion are preserved in the proposal/audit.
Exact identities and independent reviews support this proposal; they do not
constitute canonical promotion or an unrestricted STCI result.
