# Genus-two bisection: every even fiber blowup count is excluded

Date: 2026-10-10. Author and auditor: `bisection_second_pencil_audit`,
with a separate adversarial acceptance by `fiber_weight_parity_audit`.
Status: **PROVED HERE, conditional on the accepted genus-two mate
reduction and the independently checked second-pencil theorem**.
This strengthens the [second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md).
It does not exclude the whole bisection stratum. No canonical files
were edited.

## 1. The actual correction and the missing local implication

Use exactly the notation and characteristic-zero hypotheses of the
second-pencil audit. Thus `sigma:M->S` is the minimal resolution of
the actual normal quartic normalization, c is the smooth strict
transform of the smooth embedded downstairs rational curve `c_S`,
and Z is its effective rational sigma-exceptional correction. We have

    L equivalent_Q to c+Z,   (c+Z).E=0 for every sigma-exceptional E,
    Z+R=(1/2)sum_t k_t F_t,  sum_t k_t=4,
    R=sum_i e_i,   c.R=0,   c.F_t=2.

The accepted [entire-conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
establishes that S has rational singularities. This is needed below:
integral numerical correction does not imply local Cartierness for
arbitrary normal surface singularities.

Fix a parameter t with `k_t>0`. Splitting the actual fiber equality
gives

    Z_t=(k_t/2)F_t-R_t,
    c.Z_t=k_t.

If k_t is even, Z_t is an integral effective sigma-exceptional divisor.
We show this contradicts the smooth embedded curve, regardless of the
other fiber counts.

## 2. Positive correction contains complete exceptional graphs

Suppose a sigma-exceptional prime E has zero coefficient in Z and
meets a prime having positive coefficient. Effectivity and positivity
of intersections between distinct curves give `Z.E>0`. But

    0=L.E=c.E+Z.E,

and `c.E>=0`, a contradiction. Therefore the positive support of Z
is a union of entire connected sigma-exceptional graphs. Connectedness
of the exceptional fiber over a normal surface point ensures that
each such graph is the complete exceptional fiber over its point.

Every prime having positive Z coefficient is vertical for f and is
a smooth rational `(-2)` curve. A connected graph of such primes lies
in one full f-fiber. Hence, over each singular point contacted by
`Z_t`, its complete exceptional correction `Z_p` is contained in
Z_t. When k_t is even, every coefficient of Z_p is integral.

No classification of the graph, star-shape assumption, or unproved
injectivity of a numerical Picard map is used here.

## 3. The exact line-bundle descent theorem

For a rational surface singularity, a line bundle on a log minimal
resolution having degree zero on every exceptional component descends
to a locally free rank-one sheaf; the natural pullback map is an
isomorphism. This is [Kollár, Chapter 2, Proposition 76(1), PDF pages
35--36](https://web.math.princeton.edu/~kollar/book/chap2.pdf).

The cited proof starts from rationality to obtain `H1(O_A)=0` for
every effective exceptional cycle A. It then identifies line bundles
on these cycles by their component degrees and applies formal
functions to obtain local freeness and the pullback isomorphism.
Thus the theorem supplies exactly the descent implication required
here; it is stronger than a bare statement that the surface is
Q-factorial.

If one refines the local resolution to a log resolution, the pullback
of a degree-zero line bundle still has degree zero on every strict
exceptional component and on every newly created exceptional curve.
Consequently the same descent conclusion applies to the original
resolution. Equivalently, the rational-singularity proof of the
proposition works with those refinements directly.

## 4. Integral correction makes the actual downstairs curve Cartier

Let p be a singular point whose exceptional graph is in positive
`Supp(Z_t)`. Choose a local neighborhood U of p with no other singular
point and write `Z_p` for the complete correction above p. If k_t is
even, the genuine line bundle

    N=O_{sigma^(-1)(U)}(c+Z_p)

exists, because Z_p is integral. For every component E of the
exceptional fiber above p,

    deg_E N=(c+Z_p).E=(c+Z).E=0.

The descent theorem gives a line bundle P on U with `N=sigma^*P`.
Away from p, sigma is an isomorphism and Z_p disappears. Therefore
P restricts there to `O_U(c_S)`. Both P and the divisorial sheaf
`O_U(c_S)` are reflexive on normal U. They agree off the codimension-two
point p, so they agree on U. In particular the actual Weil curve c_S
is Cartier at p. This is a local assertion about c_S, rather than
only a multiple of it.

Because `c.Z_t=k_t>0`, at least one positive-coefficient exceptional
prime meets c. Its image p belongs to c_S and is singular: sigma is
the minimal resolution and has no exceptional fiber over a regular
surface point. Thus a point p as above really exists.

## 5. A smooth Cartier curve forces the surface to be regular

Let `A=O_{S,p}`. Local Cartierness and effectivity give a nonzerodivisor
g with `O_{c_S,p}=A/(g)`. Since the embedded curve c_S is smooth, this
quotient is a regular local ring of dimension one. Lift a generator
u of its maximal ideal. The maximal ideal of A is generated by u and
g, by Nakayama's lemma. Hence

    embedding_dimension(A)<=2=dimension(A),

so A is regular. This contradicts the singularity of p. Therefore
every positive even k_t is impossible.

## 6. Consequences and surviving scope

Every nonzero count k_t is odd, and their sum is four. Thus precisely
the following two necessary partitions remain:

    [3,1] and [1,1,1,1].

The mixed partition `[2,1,1]` is now excluded. The earlier exclusions
of `[4]` and `[2,2]` also follow fiber by fiber from this argument.

The hypotheses allow reducible and nonreduced fibers, degenerate
branch curves, and infinitely near centers. Their component
multiplicities are already included in the exact `Z_t` formula; no
reduced-fiber shortcut enters this proof.

There is no exclusion of `[3,1]` or `[1,1,1,1]` in this note, and the
lambda-one section lane is unchanged. The previously preserved
second-pencil audit remains a valid weaker snapshot; its table's
retained `[2,1,1]` entry is superseded by this explicit extension.

The separate auditor verified the primary Proposition 76 statement,
positive-support closure, the entire local correction, reflexive
extension to the actual curve's divisorial sheaf and prime scheme
ideal, and the regular-local-ring contradiction. The verdict was
acceptance of every even-count exclusion, with the two odd partitions
explicitly retained.
