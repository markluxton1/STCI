# Local filtration audit and promotion boundary — 2026-10-26

Status: mathematical review of local statements, not an independent executable replay, not a global sheafification certification, and not a new canonical theorem. Sources: RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md and the October 23–24 investigation and independent review notes.

## 1. Exact comparison from ideals

Let R be a noetherian local ring, I an ideal, J subset I, S=gr_I(R), H=in_I(J), B=in_I(IJ), and S_+ its positive part. The inclusion S_+H subset B is immediate by multiplying representatives and taking leading terms, even when cancellations make B larger. The filtration F^n on D=J/IJ is the image of J intersect I^n. Its nth graded quotient is (J intersect I^n)/(J intersect I^(n+1) + IJ intersect I^n). The initial-symbol identification therefore gives gr_F^n D=H_n/B_n. Consequently

0 -> B_n/(S_+H)_n -> H_n/(S_+H)_n -> H_n/B_n -> 0

is exact. In particular the comparison map is a surjection from Q to gr_F D, not the reverse. This argument is local and requires no global splitting.

## 2. Generic generator excess

At the generic point of a smooth curve, suppose R is a regular transverse two-dimensional local ring and J is a two-generator parameter ideal. Then D=J/IJ is a two-dimensional vector space over the residue field. The induced finite filtration is exhaustive and separated; hence dim gr_F D=2. The initial ideal H is a finite-colength homogeneous ideal in a polynomial ring in two variables, and Q=H/S_+H has dimension mu(H). Summing the exact comparison gives dim Delta=mu(H)-2. This does not imply Delta vanishes whenever J is a complete intersection: the initial ideal can need extra generators.

## 3. Punctual torsion criterion

On a smooth curve, suppose the graded comparison is an isomorphism generically. Each Delta_n is torsion. Over a local DVR, Q_n -> G_n is surjective with equal generic rank. The induced map of torsion-free quotients is an isomorphism (the target is free and the source quotient has equal rank), so there is an exact torsion sequence 0 -> Delta_n -> tors(Q_n) -> tors(G_n) -> 0. Length Delta_n equals length tors(Q_n) minus length tors(G_n). Thus torsion in Q is necessary but not sufficient for a punctual defect. If Q is torsion-free, the defect vanishes.

## 4. Smooth-carrier support and its precise logical role

The independent October 23 review reconstructs the completed-local straightening of a smooth carrier and concludes Delta_p=0 wherever at least one carrier has nonzero first normal symbol. Therefore Supp Delta is contained in C intersect Sing(F) intersect Sing(G), under the regular ambient and two-generator CI hypotheses. Containment is not an existence assertion. The argument is local, and no global line-bundle twist is needed for this support inclusion.

## 5. What the examples do and do not show

The October 24 punctual family has Delta concentrated in one degree with arbitrary torsion length, but its actual complete intersection has residual support, so it does not address radical(J)=I. The supported quadruple J=(x^2,y^2+tx) has radical I and torsion in Q, but Delta=0. These are opposite controls, not a solution to the supported punctual-defect question.

## 6. Still unverified

The characteristic-two quartic claim ker(D -> I/I^2) is isomorphic to O(-24) and to Q_4 relies on global chart frames and transitions; it is supported by the prior independent audit, but has not been rechecked in this turn. The normal-Koszul spectral sequence requires its filtered-complex indexing, convergence and incoming-differential identifications to be retained exactly as in the source; no simplified global spectral-sequence theorem is promoted here. The case radical(J)=I with generic Delta=0 and nonzero isolated Delta remains open.

## Decision

The local exact comparison, generic excess, torsion criterion and support containment have independently reviewed proofs and are suitable for a *separately scoped local-algebra* result after schema/path validation. Do not promote CR-13's global O(-24) assertion or infer a general supported-defect vanishing theorem from this note. This review does not perform a fresh executable replay.
