# Primary-source verification for the bisection descent audit

Date: 2026-10-10. Auditor: `bisection_full_audit/primary_descent_sources`.
Status: **PRIMARY SOURCES VERIFIED; reduced-surface scope guard supplied**.
No canonical frontier file is changed here.

## Kollár: degree-zero line-bundle descent

Source: [Chapter 2, Canonical Models](https://web.math.princeton.edu/~kollar/book/chap2.pdf),
June 1, 2010 draft. Proposition 76(1) is on printed page 35 (PDF page 35,
zero-based page 34); its proof is on printed page 36.

The hypotheses are a rational surface singularity, a proper log minimal
resolution, and a line bundle having degree zero on **every** exceptional
prime. The conclusion is that its direct image is locally free of rank
one and that the natural pullback map recovers the original line bundle.
No Gorenstein or prior Q-Cartier hypothesis is imposed. The proof uses
vanishing of first cohomology on every exceptional cycle, degrees on its
reduction, and formal functions. Section 3 allows normal excellent
surfaces; the characteristic-zero projective setting is covered.

Application guard: rationality of the target singularities and degree
zero on all exceptional primes must be established separately. For the
accepted resolution with rational exceptional (-2)- and (-3)-curves,
adjunction gives nonnegative canonical intersection, as required for
minimality with zero boundary.

## Craighero--Gattazzo: the literal degree-(4,4) exclusion

Source: [Craighero--Gattazzo, 1986](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf),
Rendiconti del Seminario Matematico della Università di Padova 76,
177--200. Printed pages 177--178 impose an algebraically closed field
of characteristic different from 2 and 3. Proposition 4 is on printed
page 187 (PDF page 12, zero-based page 11). Its displayed equation,
checked visually, is the intersection-cycle equation `F.G=4 C0` for
`C0=[s^4:s^3t:s t^3:t^4]`. The paper's convention makes surfaces reduced.
This is a degree-(4,4) exclusion, not an unrestricted STCI theorem.

**Scope repair for the descended quartic (proved here).** Suppose the
integral quartic `X` and a degree-four form `G` have intersection support
exactly `C0`. Every irreducible factor of `G` cuts a nonempty curve on
`X`, so it contains `C0`. No factor is linear. Any reducible or nonreduced
`G` therefore consists of two degree-two factors, both proportional to
the unique quadric `q`. But `q` cannot be a mate: on `q`, the quartic
carrier cuts class `(4,4)`, whereas `C0` has class `(1,3)`. Consequently
`G` is integral and reduced, and Proposition 4 applies.

## Observation record

Both PDFs were opened and their relevant searchable text inspected
through the browsing tool. Its screenshot output did not expose an
image through this execution wrapper. The CG PDF was therefore fetched
read-only to `/private/tmp/stci-cg1986-source-audit.pdf` and page 12
rendered with `pdftoppm`; the equation and curve coordinates were
visually checked in `/private/tmp/stci-cg1986-p187.png`. These temporary
paths are observations, not durable dependencies of the mathematical
argument. The initial restricted-network fetch failed to resolve the
host; the authorized read-only fetch succeeded. No failure is hidden
and no failed source retrieval is treated as mathematical evidence.
