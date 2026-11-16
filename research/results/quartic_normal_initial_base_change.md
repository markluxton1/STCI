---
id: STCI-R-0057
type: result
title: Full normal initial ideals and failure of base change for the prescribed quartic pair
scope: "#scope"
statement: "#statement"
proofs:
  - name: filtered elimination and the initial term of a principal ideal
    at: "research/arguments/quartic_specialization_and_symbols.md#2-the-full-initial-ideal-explains-the-multiplicity-change"
    using: [STCI-R-0021]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Full normal initial ideals and failure of base change

## Scope

Use \(F=x_1^4-x_0^3x_3,\ G=x_2^4-x_0x_3^3\) and the marked curve
\(C=C_0=[s^4:s^3t:st^3:t^4]\). On \(x_0=1\) put
\(u=x_1,\ X=x_3-u^4,\ Y=x_2-u^3\) and filter by \(I=(X,Y)\).
Write \(\xi,\eta\) for the normal degree-one classes of \(X,Y\).
The comparison concerns the integral chart and the fibers of
characteristics zero and two.

## Statement

In \(\mathbf Z[u,\xi,\eta]\) the full initial ideal of \((F,G)\) is
\((\xi,4u^9\eta)\). Equivalently, on the quotient chart
\(\mathscr A=\mathbf Z[u,Y]/(P)\), where \(P=(u^3+Y)^4-u^{12}\),
\[
\operatorname{gr}_{(Y)}\mathscr A
 =\mathbf Z[u,\eta]/(4u^9\eta).
\]
In characteristic zero the same formula holds over \(k\), and the
positive pieces are supported at \(u=0\). Generically on \(C\) the initial
ideal is \((\xi,\eta)\), and the local intersection length is one.
In characteristic two the full initial ideal is \((\xi,\eta^4)\) across
the chart, and the generic local intersection length is four. The first
symbols of \(F,G\) generate only \((\xi)\).
In the opposite chart \(x_3=1\), with parameter \(c=x_2/x_3\) and
normal coordinates \(A=x_0/x_3-c^4,\ B=x_1/x_3-c^3\), the same statements
hold with \((u,X,Y)\) replaced by \((c,A,B)\).

In particular the natural comparison
\[
(\operatorname{gr}_{(Y)}\mathscr A)\otimes\mathbf F_2
   \longrightarrow
 \operatorname{gr}_{(Y)}(\mathscr A\otimes\mathbf F_2)
\]
is \(\mathbf F_2[u,\eta]\to\mathbf F_2[u,\eta]/(\eta^4)\).
The source of this comparison before reduction has the nonzero class
\(u^9\eta\) killed by four. In contrast \(\mathscr A\) and every
filtration term \((Y)^n\mathscr A\) are flat over \(\mathbf Z\).

## Limitations

The normal cone here belongs to the intersection filtered by the marked
curve ideal. The ambient curve is regularly embedded and its conormal
symmetric algebra has the usual base change. The vertical part of the
characteristic-zero normal cone lies over the endpoints. The three residual
curves of the intersection itself are the components of R-0021. The
[canonical identification with the filtered equation-module kernel](quartic_char2_fourth_equation_kernel.md)
requires its own comparison argument.

## Review

The Phase 5 independent reviewer accepted the route using the chart
identities of R-0021. The reviewer checked the lowest-term product over a
domain, the opposite chart by coordinate reversal, the cancellation
giving the order-four generator, and the comparison map with kernel
\((\eta^4)\). The review checked the \(\mathbf Z\)-flat filtration terms
and the nonzero \(4\)-torsion in their associated graded algebra.

The October 23 audit checked the principal-order argument, the distinction
from the first symbols of the displayed generators, and the failure of
base change. It distinguished flatness of the filtration terms from torsion
in their successive quotients. [Source review](../arguments/quartic_specialization_and_symbols.md#source-review-and-verification)
