# Independent review: effective rational phase images

Date: 2026-10-15. Reviewer: `mann_bound_audit`.
Verdict: **PASS for the new effective theorem, with the descent and
degenerate-case clarifications recorded below incorporated in the note.**

Reviewed:
[Effective rational phase images: Mann partitions and finite mate bounds](2026-10-15-generalization-effective-rational-phase-bound.md).
The [full-conductor phase-space theorem](2026-10-15-generalization-projection-torsion-coset-reduction.md)
and its existing independent review are accepted premises. This audit
does not replay their proofs or their computations. It checks the new
rational descent, finite arithmetic construction, order estimates,
constructible boundary certificate, and resulting mate-degree bound.
No actual phase image, Mann partition list, or boundary-containment
list was enumerated, and no CAS computation or old proof check was
performed. The finite algorithm is established as a mathematical
procedure, with no claim that it has been run on these families.

## 1. Rational descent and the meaning of the image

The fixed normalized models, fixed coordinate sections of `C0`, section
spaces, restriction maps, and lift kernels are defined over `Q`.
Rational bases and lifts therefore give the full prescribed projection
families over `Q`. This concerns the whole family, not a subfamily
obtained by fixing transcendental coefficients.

The accepted phase construction can retain that field of definition.
On a `Q`-defined integral parameter stratum with coordinate ring `A`,
use `K=Frac(A)` and perform the generic matrix and normalization choices
over `K(x)`. Such a stratum need not be rational or geometrically
integral; no identification `K=Q(T)` is needed. Coefficients of the
finitely many rational functions can be represented in localizations
of `A`. Denominators involving `x` retain their zero-locus treatment
from the accepted construction; merely localizing `A` would not make
those polynomials invertible at every point. Exceptional coefficient
and rank strata must also remain in the finite construction.

Primitive-element choices apply to the relevant finite separable
reduced residual algebras. They do not imply that the full nonreduced
conductor algebra is monogenic. Keeping its bases, multiplication
matrices, and nilpotent equations avoids that unsupported inference.
All algebraic root orderings or splitting choices must remain as
variables and incidence equations, with all allowed choices present.
Selecting one geometric branch over `Qbar` and discarding conjugate
choices would not justify the stated descent. The corrected note makes
these distinctions explicit.

Chevalley's theorem then gives a constructible geometric image over
`Q`. An explicit constructible presentation can use `Q`-defined closed
sets and their closed boundaries without passing to geometrically
irreducible components. This is the image on geometric points, not an
assertion that images of `Q`-rational points exhaust `W(Q)`.

The field-extension assertion is correct. A torsion tuple `zeta` is
defined over `Qbar`. Its phase fibre is finite type over `Qbar`.
Nonemptiness after an algebraically closed extension implies
nonemptiness before extension by faithful flatness, and a nonempty
finite-type scheme over `Qbar` has a `Qbar`-point. Conversely, a
`Qbar`-point persists after extension. Thus the realized torsion tuples
and their orders are unchanged. This does not descend each particular
transcendental carrier that originally realized a tuple.

## 2. Imported arithmetic statement and partition coverage

I independently opened Evertse's
[author's version, Section 2, p. 3](https://pub.math.leidenuniv.nl/~evertsejh/98-roots.pdf).
It states the homogeneous rational form of Mann's theorem needed here:
a nondegenerate relation of length `s` has all root ratios annihilated
by the product of primes at most `s`. The cited published article is
J.-H. Evertse, *Acta Arithmetica* 89(1) (1999), 45--51,
[DOI 10.4064/aa-89-1-45-51](https://doi.org/10.4064/aa-89-1-45-51).
The page reference is to the author's version. Mann's original
bibliographic reference is supplied in the note; this audit did not
read his original full text.

At a torsion zero of each rational Laurent polynomial, the support
can be partitioned into minimal vanishing blocks. The normalized root
ratios for a block of size `s` belong to `mu_P(s)`, hence to `mu_q`
for `q=P(S)`, where `S` is the largest displayed support size.
Enumerating all support partitions and all assignments in that finite
cyclotomic group therefore covers every torsion zero.

The converse needed by the construction also holds: a retained
assignment makes every block sum vanish identically on its associated
binomial solution set. Thus that entire set, including its nontorsion
points, lies in `Y`. Minimality need not be checked again during
enumeration. Extra nonminimal assignments cannot add points outside
`Y`. Coefficient cancellations are removed before support sizes are
measured, and monomial equations are correctly recognized as empty
torus loci.

All tests in this stage are finite exact operations in an explicit
cyclotomic field. The note claims termination, not practical speed.
The rational coefficient hypothesis is essential to this particular
primorial formula; `X-zeta_N` over `Q(zeta_N)` gives the stated
counterexample to a field-independent reuse of the same bound.

## 3. Consistency, Smith normal form, and connected components

An assignment of roots to generating rows must first respect every
integer relation among those rows. This is exactly the requirement
that it induce a homomorphism `L -> mu_q`. The note correctly rejects
inconsistent systems. There are finitely many generating relations
to test, obtainable by integer linear algebra.

For a consistent system, Smith normal form and the corresponding
integer torus automorphism yield

```
y_i^(s_i)=theta_i,   theta_i in mu_q,   s_1 | ... | s_r.
```

Every connected component fixes those first `r` coordinates and leaves
the others free. Choosing the free coordinates equal to one gives a
representative whose order divides `q s_r`: each fixed coordinate is
annihilated by `q s_i`, and all those integers divide `q s_r`.
Unimodular monomial changes preserve point order. The equality
`s_r=exp(L^sat/L)` is the correct lattice invariant.

This bounds a chosen representative of every component. It bounds
every point only when the component has dimension zero. A positive-
dimensional component has torsion points of arbitrarily large order;
the review found no confusion between these statements in the note.

## 4. The sharp minor bound and its numerical interpretation

After the separate monomial shifts, a support of total degree at most
`d` lies in `d Delta_D`. Thus every character difference lies in
`d(Delta_D-Delta_D)`, including differences coming from different
partition blocks. Projecting to any selected `r` coordinates preserves
this containment.

Multilinearity expresses each selected determinant as a convex
combination of determinants with rows `d(e_i-e_j)`, allowing `e_0=0`.
After removing the factor `d^r`, these are reduced directed-incidence
matrices. Their square determinants have absolute value at most one:
expand along a row with at most one nonzero entry, or, if every row
has two opposite entries, use the zero column sum. Therefore every
rank-`r` minor has absolute value at most `d^r`.

The gcd of the nonzero maximal minors equals `s_1 ... s_r`, so

```
s_r <= s_1 ... s_r <= d^r.
```

The binomial chain in the note proves sharpness. Its determinant is
`d^r`, while for every smaller size the shifted consecutive minor is
`+/-1`. Its Smith invariants are consequently `(1,...,1,d^r)`, and
primitive `d^r`-th roots give points of that exact order. A separate
independent arithmetic subaudit confirmed this argument.

For a zero-dimensional coset, `r=D`; hence
`ord(zeta)<=P(S)d^D`. The draft expressly treats this as a numerical
upper bound. It does not incorrectly infer divisibility by
`P(S)d^D`. Its common-exponent alternative using an lcm is valid.
The monomial-count bound `S<=binomial(D+d,D)` is also valid after the
support shifts.

## 5. Constructible boundary and the three outcomes

For each connected coset `K` contained in `Y_i`, containment
`K subset B_i` is equivalent to the vanishing of every defining
equation of `B_i` after restriction to `K`. A computed monomial
parameterization or membership in the binomial prime ideal over its
computed cyclotomic field gives an exact finite test.

If containment fails, `K minus B_i` is nonempty open in the irreducible
coset `K`. Torsion is Zariski dense in `K`, so this piece has torsion
points; when `dim K>0`, their orders are unbounded because only
finitely many ambient torus points have bounded order. If `dim K=0`,
the retained piece is its one point. Thus the finite list has exactly
the torsion points of the actual constructible set, with its deleted
boundary retained in the certificate.

The three alternatives are exhaustive. No surviving piece certifies
no torsion. A surviving positive-dimensional coset certifies
unbounded phase orders. Otherwise finitely many point cosets survive,
each with the explicit numerical bound. The dimension of the closed
set `Y_i` alone is not used; isolated torsion points inside a curve are
captured by full-rank binomial systems. The example `x+y=1` is
consistent with this distinction.

The mate interpretations of these alternatives use the accepted exact
phase obstruction, including the fact that every mate degree is a
positive multiple of the phase order. They do not follow from torsion
density alone.

## 6. Mate bound and degenerate cases

For a nonempty finite surviving torsion set, let `B` bound its orders.
The accepted effectivity premise gives

```
b_min <= e ceil(M/e),   1<=e<=B.
```

For positive integers `e,M`, the least multiple of `e` at least `M`
is at most `M+e-1`. Therefore `b_min<=B+M-1`. The substitutions
`M=5,5,13` yield `B+4,B+4,B+12`. Using the exact finite set of point
orders gives the sharper maximum stated in the note. If no point
survives, nonexistence is the conclusion and no empty maximum or
mate-degree bound is needed.

The incorporated conventions close the remaining edge cases:

- With no remaining equations, `S=0`, `q=P(0)=1`, and the single
  empty binomial system is the whole torus.
- The degree parameter is `d=max(1, shifted degrees)`, with `d=1`
  when the equation list is empty.
- A nonzero monomial or constant equation makes the torus locus empty.
- Rank zero uses the trivial finite-group exponent one.
- For `D=0`, the ambient torus has its one point of order one;
  preprocessing and the boundary test decide whether it survives.

## 7. Limits of this PASS

This is a proved effective reduction for an explicitly supplied
`Q`-constructible phase image, conditional on the accepted geometric
phase theorem used as a premise. It provides a finite algebraic and
cyclotomic certificate procedure and explicit order/mate bounds once
the image equations and boundary are known. It supplies neither those
equations nor numerical values of their degrees and supports for the
three actual families. It does not compute a surviving torsion phase,
exclude any entire actual family, or settle the unrestricted fixed-C0
or universal STCI question. The contact budgets alone are not promoted
to numerical phase-image bounds.

No further mathematical correction is required within this stated
scope. The note remains a new independently reviewed result awaiting
the ordinary repository integration of its proof and this review.

## 8. Addendum: the Section 9 meta-effectivity corollary

Verdict: **PASS for the explicit fixed-three-model input stated in
Section 9.** This addendum audits algorithmic accessibility of the
accepted geometric construction, not its geometric proof again.

The strengthened statement is justified by more than the abstract
existence of a finite-type phase space. It specifies finite rational
polynomial/section/module input and supplies the following effective
chain.

- On a `Q`-prime parameter piece, computations over
  `K=Frac(R)` and `K(x)` are exact and decidable from a presentation
  of `R`. The piece need not be a rational variety.
- The three fixed source section rings have explicit finite normal
  graded presentations. Image equations, finite-module relations,
  syzygies, annihilators and common ideals are therefore computations
  in presented polynomial/module data. The finiteness hypotheses are
  those of the accepted admissible normalization charts.
- Noether coordinates, finite bases and reduced separable primitive
  elements can be found by exact algorithms or by dovetailed searches
  for finite certificates. The accepted generic existence assertions
  guarantee eventual success. No class-group oracle is introduced.
- Spreading also controls the relevant module exact sequences. The
  monic module Groebner basis argument is valid: retaining both basis
  generation directions and the Buchberger reductions, and then
  clearing their finitely many coefficient denominators, gives a
  monic basis after localization. Its standard module monomials are
  free over the localized parameter ring. Applying this to the
  relevant cokernels preserves fibre kernels and inclusions. Clearing
  displayed matrix entries alone would not prove that assertion.
- Primary decomposition of `V(h)` gives finitely many computable
  `Q`-prime components of strictly smaller dimension. Recursing on
  all of them yields a finite tree and retains every exceptional
  stratum. The conductor quotient's monic finiteness identities and
  its denominator zero loci remain subject to the accepted full
  construction.
- Effective algebraically closed field quantifier elimination gives
  the geometric constructible image, including its open conditions;
  computing its closure alone would be insufficient. The already
  audited Mann/SNF/boundary procedure then terminates on that image.

I also independently opened the Derksen--Kemper primary paper linked
in Section 9. Its Theorem 2.13 and Algorithm 2.14 explicitly compute
a generic-freeness localization using a Groebner basis over the
fraction field, on pp. 2114--2115. That displayed result concerns a
domain ring inclusion. The note correctly gives its own monic module
argument for the more general module and base-change control needed
here, rather than attributing that entire argument to the displayed
ring-only algorithm.

There is consequently no additional unproved algorithmic bridge in
the proposed composite procedure within this precise input scope.
It is legitimate to state an in-principle terminating decision
algorithm from the explicit projection-family input, rather than
requiring a phase-image presentation as a separate input. The output
decides existence of any mate-admitting carrier and distinguishes
unbounded least mate degrees from the finite-bound case. The
geometric implications continue to use the accepted phase theorem
as a premise.

No such composite algorithm has been run here. This addendum gives
no practical complexity estimate, equations for an actual phase
image, numerical bound for the three whole families, or decision
which alternative holds for those families. No CAS or accepted-proof
replay was performed.
