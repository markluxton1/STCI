# Optional polynomial scaling for the degree-15 pencil block

Status: a new exact source-polynomial transformation design, not an invertibility
certificate, rank proof, or full-fiber exclusion. The main recovery subsequently
inverted the simpler common-denominator block in about five seconds; this design
is retained as a reusable option, not a replacement for that successful path.
No inherited rank or tensor verifier was replayed in producing it.

The selected 17 by 17 block is specified by the existing modular index-selection
record. That modular record selects rows and columns only. All calculations below
use the characteristic-zero rational source of attempt03.

Every seed denominator is a rational constant times powers of k-1 and k+1.
The common denominator (k^2-1)^9 therefore clears the seed denominators. Exact
polynomial arithmetic first forms this common numerator matrix, then measures
the valuations of each nonzero entry at k=1 and k=-1. For each of the two places,
integer row and column exponents are chosen to satisfy

    row_exponent[i] + column_exponent[j] >= pole_order(B[i,j]).

The Hungarian assignment dual supplies a minimum total exponent cover of this
inequality system. Negative column exponents are permitted: polynomial
cancellation in the source verifies that the final scaled entries remain
polynomials. Rational numerical denominators are then cleared row by row.
The resulting integer polynomial matrix P has the form

    P = D B E.

The JSON records all diagonal factors and all integer coefficients of P in
increasing degree order. It has 150 nonzero entries, maximum entry degree 21,
and total determinant scaling degree 152 (77 at k=1 and 75 at k=-1).
Clearing (k^2-1)^9 independently in all 17 rows instead uses degree 306.
These figures concern input representation only; they do not bound the cost of
inversion or prove that the selected determinant is nonzero.

If an inverse of P is subsequently certified, then

    B_inverse = E P_inverse D.

This identity must still be checked in the intended field; the design by itself
supplies no inverse. The factors k-1 and k+1 must be verified to be units in that
field before transporting an inverse.

An additional exact simplification is that source row16 has precisely two
nonzero entries, both -1, in source columns6 and0. Hence the column operation
column0 := column0-column6 gives a constant pivot and removes one row and one
column. No further entire constant row appears immediately after that step.
The saved peeling record is a design for this operation; it is not a determinant
calculation.

Artifacts:

- [Reproducible scaling-design script](../computations/general_localcoh_degree15_polynomial_scaling_design_2026_10_14.py).
- [Scaled polynomial matrix and diagonal factors](../validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/selected-block-scaled-polynomials.json).
- [Constant row peeling record](../validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/constant-row-peel.json).
- [Original index-selection diagnostic](../computations/general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json).

The script uses Python standard-library exact rational polynomial arithmetic.
Its divisions assert exactness, and its scaling potentials assert every required
entrywise denominator inequality. It neither starts nor stops a CAS job.
