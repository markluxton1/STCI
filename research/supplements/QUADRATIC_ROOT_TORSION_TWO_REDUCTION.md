# Torsion-two roots: exact elimination, pure-direction exclusion, and the remaining chart

Exploratory continuation, 2026-10-31, worktree `9cf8/STCI`, base commit
`9eb97a059ba9e06520520fce33e4ec5c092010d7`. These are source-level contributions,
not promoted results. Independent review and executed evidence are recorded
below. No canonical result, navigation, mathematical status, or priority is changed.

## Problem and inherited premises

Work over Q with geometric points over Qbar, for
`C0=[s^4:s^3t:st^3:t^4]` and its fixed actual embedded normal coordinates.
The question is whether a **smooth spectral torsion-two quadratic root** can
satisfy both the first and second ambient lifting equations of
[R-0007](../results/quadratic_root_obstruction_model.md). This is a bounded
necessary compatibility problem, not a complete criterion for STCI.

The [initial exploration](STCI_COMPLEXITY_AND_QUADRATIC_ROOTS.md) gives the
verification/search distinctions, the smooth dual-bundle splitting, and the
complete smooth diagonal exclusion. We reuse the exact chart expansion and
first/second obstruction from
[the accepted global model](../computations/generalization_quadratic_root_global_second_model.py).
The reviewed [torsion-two determinant criterion](QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#3-exact-order-two-is-a-coefficient-determinant)
identifies this spectral stratum with rank-two coefficient matrices on the
smooth open. This criterion is reviewed source-level mathematics; R-0008
provides the separate canonical graded Picard criterion.

The new reduction retains the orientation of the quadratic pencil relative to
the ambient operator. It eliminates all twelve first correction variables,
uses sixteen complete second tests, and excludes the entire locus on which
one of the two square directions is a pure normal coordinate. All unexcluded
smooth torsion-two roots are covered by one six-parameter affine chart.
Its exceptional linear rank-drop locus has nineteen base points and a
first-compatible scheme of length 76; the second obstruction excludes
every one of those fibers. The remaining rank-two locus is covered by
three exact four-parameter pivot charts. Their complete second-zero
calculation remains unresolved.

## 1. Ordered squares and genuine ambient symmetries

Every smooth torsion-two root can be written

    f=A(z) X^2+C(z) Y^2,

where X,Y are independent constant linear forms in u,v and A,C are homogeneous
base quadratics. Indeed, the rank-two pencil has a nondegenerate annihilator;
a degenerate annihilator would make all its binary quadratics have a common
directional factor, contradicting smoothness. Its two intersections with the
conic of squares give X and Y. The smooth open is exactly

    Res(A,C) Disc(A) Disc(C) != 0.

Discriminants and resultant are those of homogeneous binary quadratics;
a simple zero at base infinity is permitted. Distinct branch roots give a
smooth double cover, whereas a multiple root of A or C or a shared zero gives
a singular point of the divisor.

The ambient torus `diag(1,lambda,lambda^3,lambda^4)` preserves C0 and acts by
`z -> lambda*z, u -> lambda^4*u, v -> lambda^3*v`. Up to root scalar it sends
`f(z,u,v)` to `f(lambda*z,u,lambda^-1*v)`. This is an actual ambient symmetry,
including the higher coordinate transition. If one direction is mixed, use
this symmetry to make X=u+v. The other direction then has one of two forms:

| Orientation | Root | Original a,b,c |
| --- | --- | --- |
| finite | A(u+v)^2+C(u+k v)^2, k!=1 | A+C, 2(A+kC), A+k^2 C |
| infinity | A(u+v)^2+C v^2 | A, 2A, A+C |

If neither direction is mixed, the root is diagonal and was already excluded.
These normalizations use one ambient torus parameter and root scalar;
they do not authorize a further arbitrary direction change or coefficient
normalization. The finite chart includes k=-1.

For each orientation, two coefficient charts suffice: C2=1, or C2=0,A2=1.
Both leading coefficients cannot vanish, because that would give a shared
zero at infinity. Only one root scalar has been used here.

There is also an actual reversal

    J:(x0,x1,x2,x3) -> (x3,x2,x1,x0).

In the accepted coordinates `v=x2/x0-z^3`,
`u=x3/x0-z^4-(3/2)zv`, write U',V' for the accepted opposite-chart normal
coordinates. Direct substitution gives `v_new=2U'`, `u_new=V'/2` exactly,
and `U'=z^-7 u+O((u,v)^2)`, `V'=z^-7 v+O((u,v)^2)`.
Thus J exchanges the two pure directions and sends a finite nonzero slope r
to `1/(4r)` while reversing the base. Because J is an ambient automorphism,
it preserves existence of compatible first and second lifts. This conclusion
uses the whole lift, not merely invariance of a displayed leading symbol.

## 2. A single resultant eliminates the first correction

Set `ell=k-1` in the finite chart and `ell=1` at infinity. Transform the
accepted cubic first discrepancy into X,Y, clearing the direction denominator
`ell^3`, and denote its four coefficient polynomials by D0,...,D3, each of
degree at most three in z. The inverse substitutions used are

    finite:   u=(kX-Y)/ell, v=(Y-X)/ell;
    infinity: u=X-Y,        v=Y.

For the first-unit numerator components, scaled by ell^3, the equations are
convolutions with (A,C), respectively with right sides (D0,D2) and (D1,D3).
The same four-by-four Sylvester matrix solves both:

    S = [ A2 A1 A0 0 ; 0 A2 A1 A0 ;
          C2 C1 C0 0 ; 0 C2 C1 C0 ].

Its determinant R is Res(A,C). Solve the first two coefficient rows of each
convolution using S, and the last two rows using S again. The two overlapping
coefficients in each pair must agree. Equivalently, the four first conditions
are the coefficients of z^3 and z^2 in

    (C D0-A D2)/ell,       (C D1-A D3)/ell.

They are polynomials. Since R!=0, these conditions are sufficient as well as
necessary: they give the unique six coefficients of each unit component.
After returning to u,v, a common factor ell cancels and all twelve original
first corrections have the form

    h_i=H_i / (R ell^2).

The [retained generator](../computations/quadratic_root_torsion_two_model.py)
implements these adjugate solves directly from the accepted FIRST equations.
It does not choose one generic twelve-by-twelve minor or omit a rank boundary.

## 3. Sixteen complete second residues

In X,Y coordinates, the two syzygies for `A X^2+C Y^2` are

    q2=(0,C,0,-A,0),       q4=(C^2,0,-AC,0,A^2).

They have base degrees two and four. Their fibers are independent whenever
A,C are not both zero: if one vanishes, the remaining nonzero components
still lie in different slots. Since their degrees add to six, they generate
the full rank-two bundle W with determinant O(-6). Thus they give a global
O(-2)+O(-4) splitting in these square coordinates, including degree drops
of affine representatives. The sixteen sections

    z^j q2 (0<=j<=8),       z^j q4 (0<=j<=6)

are a basis of H0(W(10)). These are complete second tests on this stratum.

For each original quartic normal monomial `u^(4-i)v^i`, expand its numerator
under the inverse direction substitution. Pair its X,Y coefficients with q2
and q4 to obtain original-coordinate dual vectors Q2,Q4. With R4 the accepted
quartic Cech representative, the tests are the residues

    [z^(-1-j)] <Q2,R4>,  0<=j<=8;
    [z^(-1-j)] <Q4,R4>,  0<=j<=6.

The common direction factor ell^4 is invertible. The generator substitutes
the unique h and multiplies R4 by `(R ell^2)^2`, sufficient because its
h-degree is at most two. It reduces in the first ideal before products to
control intermediate expressions. All these replacements are equivalent
on the specified open; boundary components introduced by clearing
denominators are removed by the explicit open equation.

## 4. Exact exclusion of the pure-direction locus

For the infinity orientation, exact characteristic-zero calculations exclude
both coefficient charts. By J, the finite k=0 pure-direction locus is then
excluded as well. Together with the earlier diagonal certificate, this
covers every smooth torsion-two root with a pure square direction.

### The boundary chart C2=0,A2=1 has a small certificate

Smoothness implies C1!=0. Put x=A1, y=C1. The third and fourth first equations
give, successively,

    C0=(10-3x)y,          A0=(3x^2-16x+22)/2.

The first equation gives `y=3(x-2)(3x^2-18x+26)/8`. The second becomes
`3P(x)/16=0`, where

    P=9x^4-72x^3+196x^2-208x+4.

One denominator-cleared second residue, s2x0, reduces modulo the first ideal to

    S=(563624/135)C0*C1+(59591605/54)C1^2
      -(20469592/45)C0-(434673083/180)C1.

After the same substitutions, `S/y=-Q(x)/240`, where

    Q=3381744x^4-336284457x^3+2543733416x^2
      -6776894138x+7031271104.

These quartics are coprime over Q. The retained
[compact certificate](../computations/quadratic_root_pure_direction_boundary_certificate.sing)
verifies every displayed substitution and explicit cubic polynomials U,V with
`UP+VQ=1` by rational polynomial multiplication. It needs no multivariate
Groebner calculation. The derivation of S from the accepted second model was
checked separately against the retained generator.

### The chart C2=1 has an exact algebraic exclusion

The generated localized ideal consists of the four first equations, all
sixteen denominator-cleared second residues, and
`iv*R*Disc(A)*Disc(C)-1`. Its Groebner basis over Q is {1}.
This is a completed computation on the entire chart, not sampling or generic
nonvanishing. A stronger resultant-membership calculation is separately
available through the generator's `--test resultant` option: membership of R
in the unlocalized equation ideal also suffices for exclusion. A nonzero
remainder in that stronger test would not establish nonemptiness.

## 5. The single remaining chart and the cost of further elimination

Both square directions are now mixed. Write

    f=A(z)(u+v)^2+C(z)(u+k v)^2,
    C2=1,  k(k-1)Res(A,C)Disc(A)Disc(C)!=0.

This covers all remaining roots: if initially C2=0, then A2!=0; interchange
the two square labels and use the torus lambda=k. The new second coefficient
is A(kz), with nonzero leading coefficient k^2 A2, and can be scaled to one.
The parameter changes to 1/k. Thus the discarded coefficient chart is covered
by this one; the argument requires k!=0, already guaranteed by the exclusions.

There are six root parameters A0,A1,A2,C0,C1,k and four first equations.
Two first equations are linear in A0,A1,A2. A nonzero two-by-two coefficient
minor lets us eliminate two more variables; all three pivot charts and the
augmented-consistency rank-drop locus must be covered. This is a further
exact stratification, not an assertion that every fiber has generic rank.

The [rank-stratum calculation](../computations/quadratic_root_torsion_two_rank_strata.sing)
makes the exceptional base explicit. Write the two linear equations as
`M(C0,C1,k)*(A0,A1,A2)^t=rhs`. On `k(k-1)(C1^2-4C0)!=0`, all six two-by-two
minors of `[M|rhs]` define a zero-dimensional Q-algebra of dimension 19.
The subcase M=0 is empty on this open, so the augmented-minor test really
does impose consistency on the rank-one locus. The other two first equations
and the second obstruction have not been imposed in this calculation.

Eliminating to k gives a squarefree polynomial of degree 19, factoring as
`(k+1)P18(k)` with P18 irreducible of degree 18 and reciprocal. Its degree
equals the dimension of the whole base algebra, so k generates that algebra:
it is reduced and consists of 19 distinct geometric base points. The rational
point has `k=-1,C0=4,C1=1/5`. Each base point still has a plane of solutions
to the two dependent linear equations in the three A coefficients, before
the two remaining quadratics are imposed. Thus "19 points" describes the
exceptional **base**, not nineteen compatible roots or a completed exclusion.

A subsequent calculation tests the full fibers, rather than only this base.
The lex basis expresses C0,C1 as exact rational polynomials in k. For k=-1,
substitute C0=4,C1=1/5 in the full first-and-second model. For the other
component, use the number field `K=Q[k]/(P18)` as the coefficient field,
substitute the lex-shape values of C0,C1, and retain A0,A1,A2 as free
polynomial variables. In both cases the localized full ideal is {1}.
Irreducibility of P18 makes the second calculation cover all eighteen
conjugates, not merely one numerical choice of k. This conclusion passed
independent source, shape, and scope review. The
[fiber verifier](../computations/verify_quadratic_root_rank_fibers.py)
derives both specializations from the maintained matrix and full model.

The entire rank-drop boundary is therefore excluded from the smooth
second-zero locus. All remaining solutions have rank(M)=2 and lie in the union
of its three nonzero
two-by-two-minor charts. Each chart eliminates two A coefficients exactly,
leaving four parameters and two first equations before the second tests.

The second obstruction is substantive here: independent first-only
calculations give dimension zero and length four over each coefficient field,
after inverting the smooth open. Thus the first-compatible rank-drop scheme
has total rational length `4+18*4=76`, and is nonempty over each of the
nineteen geometric base points. This is length with multiplicity, not a count
of distinct roots. The second stage excludes all of it.

On the pivot using A0,A1, a diagnostic exact substitution gave two remaining
equations of total degree twelve in A2,C0,C1,k, with 334 and 357 terms after
expansion. Their common denominator is the square of a degree-four pivot
polynomial. Fewer parameters therefore produced substantially denser,
higher-degree equations. Over F_32003, a bounded run spent its entire
120 seconds computing the first ideal of these two substituted equations;
it never reached the second obstruction. This explains a concrete limitation
of unrestricted Cramer substitution; it is not a lower bound on the best
algorithm.

## 6. A bounded scalar compression for the finite first stage

Let B be a finite commutative unital Q-algebra of dimension N and suppose
`s0,...,s_(m-1)` generate its unit ideal, with m>=1. Then some integer

    0 <= t <= (m-1)N

makes `s(t)=sum_(j=0)^(m-1) t^j s_j` a unit. After extending to Qbar there
are at most N geometric maximal points. At each, the evaluation of s(T)
is a nonzero polynomial of degree at most m-1, so it has at most m-1 bad
values. The union has at most (m-1)N values. Nilpotents do not change the
criterion that an element nonzero in every residue field is a unit.

Apply this to the length-76 first-stage algebra and the sixteen restricted,
denominator-cleared second residues. The completed fiber exclusions say
that they generate the unit ideal. Therefore some t among 0,...,1140 gives
one scalar second test that is nonzero at **every** first-compatible point
on this rank-drop stratum. Once a successful t is specified, its inverse can
be found and checked by multiplication in the 76-dimensional rational
algebra, equivalently in the four-dimensional algebras over Q and K.

This lemma passed independent mathematical review. No explicit successful
t or inverse was computed. It bounds a scalar-selection parameter, not
the bit size of the inverse, the quotient algebra's presentation, or a full
negative certificate. Its finite-algebra hypothesis does not hold for the
remaining parameter chart, so this is no scalar compression of all T[2].

The subsequent independently reviewed
[closed-point refinement](INTRINSIC_GEOMETRY_AND_STCI_COMPLEXITY.md#6-certificate-selection-depends-on-closed-support-not-total-length)
improves the sufficient range to `0,...,120`. The two four-dimensional
algebras over Q and the degree-18 number field have at most eight closed
points over Q; rational scalar choices work simultaneously over their
conjugate embeddings. No specific successful scalar or inverse has been
computed. The earlier length-based bound remains valid but is weaker.

## 7. Connection to the already bounded actual degree rows

The promoted [R-0014 six-row reduction](../results/movement_two_six_rows.md)
already bounds the actual degrees in the relevant restricted global class.
Under [R-0013](../results/saturated_actual_generator_movement.md)—actual
homogeneous sole support on C0, saturated first relation, and a full generic
coprime binary-CI initial ideal—with r=2 and movement epsilon=2, the only
unordered numerical possibilities are

    (s;a,b)=(8;8,8) or (12;6,16).

These are necessary rows, not realized STCIs. The owning
[generator and arithmetic proof](NORMAL_FLATNESS_AND_FILTERED_CI.md#8-smooth-root-consequence-and-remaining-work)
also derives both actual order-two symbols and their joint generation from
the stated global hypotheses. For a smooth full root the R-0006 bridge
therefore applies, and both rows have s>4.

Consequently the new pure-direction second-obstruction exclusion rules out
every smooth torsion-two pure-direction root in **both** actual numerical
rows. The general operator's different target at s=4 is still a valid caution;
it is not a surviving actual numerical case under these global hypotheses.
The other smooth root shapes, singular roots, and presentations outside
the saturated/full-generic-CI class are not excluded here.

This also refines the complexity interpretation: a conditional witness-degree
bound is already available for this fixed-curve, fixed-normal-order,
fixed-movement class. The remaining difficulty is compatibility and actual
realization within the two rows. That inherited bound says nothing about
arbitrary presentations of C0 or a family of input curves. It must not be
confused with a uniform STCI search bound.

## Review, reproduction, and limits

The ordered-square coverage, actual torus and reversal, Sylvester elimination,
dual basis, and final single-chart coverage passed independent mathematical
review. The generator's original four chart cores were checked against the
exploratory exports; the two infinity cores were independently reconstructed
from the retained generator. The boundary certificate passed independent
source comparison, elimination checks, and exact execution. The independent
reviewer generated the infinity C2 chart afresh from the retained generator
and completed the localized QQ calculation in 25.02 seconds, with no engine
errors and terminal markers `FULL_DONE`, `UNIT_IDEAL`. A separate reviewer
also reran the earlier identical construction and obtained {1} in 25.00
seconds. These timings identify the executed runs, not a benchmark.

The stronger assertion R in (first,second) also has completed exact evidence:
the unlocalized calculation produced a 22-polynomial Groebner basis; two
reviewers checked its source and exact transcription, and reran the zero
remainder for R. One later combined rerun exceeded its 90-second limit and
was interrupted. The fresh localized runs independently establish the
exclusion; no compact multiplication-only certificate for the C2 chart
was extracted. The retained `--test resultant` option reproduces this
stronger membership calculation without retaining a second generated model.

The rank-stratum script and its source matrix were independently checked
against the retained generator, and the dimension, length, squarefreeness,
and factorization computations were rerun. The corollary using R-0013/R-0014
also passed a separate scope check. The review clarified the ell^3 scaling
of the first-unit numerator components; that clarification is incorporated.
Exploratory calculations that spent an already used scalar normalization
again were discarded, and no conclusion here uses them.

For the full rank-drop fibers, the reviewer verified both specialized model
cores against the maintained generator and checked all six augmented minors
and the nonzero open in Q[k]/(P18). The rational full-fiber unit result was
independently rerun. The degree-18 full-fiber unit result has a completed
exact execution with source correspondence independently checked; the
reviewer's separate 120-second rerun reached R4 but timed out during second
residue construction, so it is not represented as a fresh completed check.
The two first-only length-four computations were independently rerun.
The finite-algebra scalar-compression lemma and its parameter bound also
passed independent review.

The final integrated retained fiber verifier then completed successfully
with a 300-second per-call bound. It rederived and verified the base shape,
printed length four and `UNIT_IDEAL` for both coefficient fields, and
reported total first-stage length 76. A subsequent diagnostic-only change
preserves captured stage output on timeout; its syntax was checked and
the mathematical construction is unchanged. This completed integrated run
is distinct from the earlier interrupted 120-second attempts.

Reproduction requires SymPy (used: 1.14.0) and Singular (used: 4.4.1p5).
Generation does not launch the algebra engine and is not evidence of a
completed calculation. For the completed pure-direction charts:

```sh
python3 research/computations/quadratic_root_torsion_two_model.py \
  --orientation infinity --chart C2 --output /tmp/torsion_two_C2.sing
Singular -q /tmp/torsion_two_C2.sing
Singular -q research/computations/quadratic_root_pure_direction_boundary_certificate.sing
Singular -q research/computations/quadratic_root_torsion_two_rank_strata.sing
python3 research/computations/verify_quadratic_root_rank_fibers.py
```

The expected terminal markers are `UNIT_IDEAL` and
`PASS: exact source substitutions and U*P+V*Q=1 over QQ`.
Check that no Singular error lines precede the markers; exit code zero alone
does not establish success. The full boundary ideal can also be regenerated
with `--orientation infinity --chart A2` and gives `UNIT_IDEAL`.
The rank-fiber verifier additionally checks the exact shape and smooth opens,
first-stage length four on each coefficient field, and the two full unit
ideals. It reports total first-stage scheme length 76. It uses a 300-second
bound per Singular call; expiration is an incomplete run, not a nonunit result.

The remaining mixed-direction diagnostic over F_32003 did complete: its
localized ideal is {1}, after 259.39 seconds. The retained construction
with `--orientation finite --chart C2 --mixed --characteristic 32003`
matches that run's construction exactly (moving the same k factor into
the open polynomial). This is a result in positive characteristic only.
It neither certifies rational emptiness nor transports to characteristic zero.

The raw-expression QQ alternative reached the final Groebner computation
but did not finish within 300 seconds. A QQ attempt using reductions after
every multiplication spent its 600-second bound before R4 assembly finished;
a separate 300-second variant likewise never reached its proposed
unlocalized-ideal test. Thus these timings
distinguish equation construction from elimination, rather than treating
every unsuccessful run as an attempted completed ideal computation.

The remaining finite chart has not been excluded and no surviving point has
been certified. Bounded rational and finite-field eliminations that timed out
supply no emptiness result. Positive-characteristic diagnostics have no
automatic characteristic-zero implication. No actual surface-pair search,
full K1/K2 decomposition, exact-order-four exclusion, singular-root exclusion,
or unrestricted STCI decision was performed.

The single most informative next calculation is an exact rational
ideal-membership certificate for the remaining mixed chart while retaining
its six root parameters. With J generated by the four first equations and
sixteen second residues, set `Omega=k(k-1)Res(A,C)Disc(A)Disc(C)` and seek
an identity `Omega^N in J`, or exhibit a point where all equations vanish
and Omega does not. Such a certificate would cover the pivot boundaries
without replacing the two linear equations by the observed dense
degree-twelve substitutions. No suitable exponent or small certificate
size is proved here. The completed finite-field unit computation motivates
this test but cannot replace the rational identity.

An actual-CI application still requires every
[R-0006 hypothesis](../results/actual_ci_smooth_root_bridge.md), with second
normal relation degree s>4. At s=4 the next relation changes the obstruction
target. No present result enlarges those hypotheses or converts abstract
graded compatibility into actual global equations.
