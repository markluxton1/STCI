# Independent integration audit of the STCI equation search

Date: 2026-10-29. Reviewer: `search_logic_audit`.

**Verdict: PASS for the scoped synthesis and navigation change.** The
[search record](../STCI_SEARCH.md) is an independently reviewed provisional
research program and report of specified tests. It does not promote any
canonical result, classify all defining pairs, or change the unrestricted
characteristic-zero open status.

The review read the final synthesis, the relevant arithmetic, freedom,
projection and sextic source/audit notes, and the current framing in
[FRONTIER](../FRONTIER.md), [STATE](../STATE.md), and the
[decision guide](../RESEARCH_DECISION_GUIDE.md). It did not replay accepted
proofs or the final computation package. The independent reconstruction
and new projection computation earlier in this run are recorded in the
[logic and positive-criterion audit](2026-10-28-stci-search-logic-audit.md).

## Mathematical scope checks

- **Arithmetic.** The all-pairs minimum \(\delta(p)\) is distinguished
  from fixed-quartic mate minima and from the one-binomial minimum.
  Fixed-degree constructibility is applied to geometric solutions over
  algebraic closures; absence of \(\mathbb F_p\)-rational points is not
  treated as geometric emptiness. The restricted minima \(4,4,20,p\)
  for \(p=2,3,5,\ge7\), respectively, agree with the separate
  [arithmetic audit](2026-10-28-stci-search-arithmetic-audit.md).
  The inequality \(\delta(p)\le\delta_{\rm bin}(p)\) cannot give the
  unrestricted lower bound, and no such conclusion is asserted.
- **Freedom.** The spaces are sheaf powers, equivalently saturated
  homogeneous powers, with actual global scalar coefficients. The
  dimension formula, forced quadric factor, and symbol-image dimensions
  agree with the independently reconstructed
  [freedom audit](2026-10-28-stci-search-freedom-independent-audit.md).
  The requirement of common leading roots is limited to integral
  degree-at-least-five representatives. Shared roots may produce the
  necessary excess contact; no bound for arbitrary higher contact is
  inferred from the product of the raw equation orders.
- **Projection source.** The sixteen-parameter description is complete
  for the fixed diagonal restrictions, not for arbitrary normalization
  geometries. Pure-power membership supplies actual homogeneous mates
  for maps meeting the stated hypotheses. Necessity retains full
  singleton inverse support. The corrected map's off-diagonal inverse
  has scheme length sixteen, without a distinctness claim. Its isolated
  inverse points prohibit a mate without assuming birationality. Both
  failed projection sources remain literal sources, not exclusions of
  the whole degree-eight model.
- **Sextic tests.** The seven specified rational carriers and all their
  proper degree-sixteen mates are the scope. Three \(\kappa=0\) inputs
  have only \(\ell_C\le18\), without an attainment assertion. Four
  nonzero-\(\kappa\) inputs have sharp maximum sixteen and the fixed
  full ideal \((F,q^8)\) at maximal contact, with cycle
  \(16[C]+32[L_0]\). The source and
  [independent audit](2026-10-28-stci-search-experiments-audit.md)
  justify the modular-rank bridge and distinguish representative
  independent Macaulay2 checks from the seven-input primary computation.
  A smaller modular rank is not treated as a characteristic-zero
  construction.

## Clarifications identified during integration

The final synthesis explicitly distinguishes raw normal orders of the two global
equations from the later relation orders that arise in a standard basis
after cancellations or division by the first relation. In particular,
the \(s=12\) in the conditional \((2,12;6,16)\) row does not require
an integral degree-sixteen global equation of raw normal order twelve.
The raw-order inequality \(s\le16/3\) and the conditional relation row
therefore concern different data. The reviewer verified the clarification
in Section 4 of the final search record.

The current headers and summaries in all three navigation documents
consistently adopt the user-directed candidate/test/failure/update cycle.
Earlier construction and residual work is retained as available input,
with mathematical status unchanged. One remaining older sentence in
STATE described its earlier guiding question in current tense; it now
says "At that stage ... was". The reviewer verified this correction.
It is a navigation clarification, not a mathematical conflict.

## What the review does not certify

It supplies no exhaustive search-degree bound, no effective
characteristic cutoff, no proof that a selected family contains every
possible witness, and no identification of the auxiliary quadric's rank
change with the larger jet kernel. The synthesis retains these limits
and specifies the next equation or parameter locus to test. That is the
appropriate scope of the delivered search record.
