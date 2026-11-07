# Actual lifting for quadratic roots with spectral two-torsion

Fix the embedded curve `C0=[s^4:s^3t:st^3:t^4]` over Q, with geometric
points over Qbar. Use its actual normal coordinates

```
z=x1/x0,  v=x2/x0-z^3,  u=x3/x0-z^4-(3/2)zv.
```

A basepoint-free moving quadratic root is `f=a(z)u²+b(z)uv+c(z)v²`,
where a,b,c are homogeneous base quadratics. We ask whether a smooth root
with spectral ruling-difference class of order two satisfies both actual
ambient lifting equations of [R-0007](../results/quadratic_root_obstruction_model.md).
The [coefficient determinant criterion](../supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#3-exact-order-two-is-a-coefficient-determinant)
identifies this stratum with rank-two coefficient pencils on the smooth
open. The [spectral splitting proof](spectral_torsion_and_syzygy_splitting.md)
owns the general four-torsion/syzygy classification; it does not make the
embedded operator invariant under arbitrary changes of normal direction.

The results here are independently reviewed deductions and exact
calculations. They exclude every smooth first-compatible diagonal root,
every smooth torsion-two root with a pure square direction, and the complete
exceptional rank-drop fibers in the remaining mixed chart. The three
rank-two pivot charts remain unresolved over Q. These are necessary local
compatibility tests, not a complete STCI criterion.

The actual transition and complete `FIRST` and `R4` representatives are the
inherited [global second model](../computations/generalization_quadratic_root_global_second_model.py).
The diagonal checker and model generator read its AST only through `R4`, stopping before
`ABC` and before the unrelated export side effects. That prefix constructs
the full nonlinear base substitution, normal transition, first equation
unit and quartic Cech representative from exact rational arithmetic. It
reads no saved output or generated model. Its sparse coefficient indexing
is part of the interface, not an incidental formatting choice.

## One scalar excludes the complete smooth diagonal locus

Impose b=0 **in the fixed actual ambient coordinates**. The independently
reviewed [diagonal classification](../supplements/QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit)
reduces first compatibility to four explicit quadrics in the six coefficients
of a,c. For smooth roots these force c2!=0. Normalize only the scalar
of f so c2=1. Its three exhaustive families are as follows, with t!=0:

| Family | a(z) | c(z) | Second scalar |
| --- | --- | --- | --- |
| plus | 4+t z^2 | -8/t+z^2 | -16 |
| minus | -4+t z^2 | 32/t+z^2 | -640 |
| mixed | -4+t z-(5t^2/44)z^2 | 880/t^2+(44/t)z+z^2 | 1648 |

For clarity, the coverage does not use a change of the two rulings.
The inherited classification says a0=4c2 or -4c2. In the first case
a1=c1=0 and a2*c0=-8c2^2. In the second case either a1=c1=0 and
a2*c0=32c2^2, or a2*c0=-100c2^2, a2*c1=-5c2*a1,
a1^2=-(44/5)a2*c2. Taking t=a2 in the even cases and t=a1 in the
last case gives exactly the table after c2=1. Its denominator t is
nonzero in every smooth case; this discards no smooth boundary.

Let R4=sum r_i u^(4-i)v^i be the accepted actual second Cech
representative, after inserting the unique first correction h. Use

    q=(0,-c^3,0,a*c^2,0),
    Lambda(f)=coefficient_(z^-1)(-c^3*r1+a*c^2*r3).

The identity T_f q=0 is immediate for b=0, and q has base degree at
most six, hence is a valid section of W(10). It is the first column
of the accepted complementary-minor matrix. Consequently Lambda is
insensitive to Cech coboundaries and to the unknown next equation unit.
It tests the actual quartic correction, including the nonlinear base
coordinate substitution and the product of the first unit with its correction.

The [standard-library exact checker](../computations/quadratic_root_diagonal_certificate.py)
reuses the accepted chart generator through R4, substitutes the three
families and explicit first corrections, verifies all sixteen first
equations identically, and evaluates this single residue in Q[t,t^-1].
It obtains the table's constants. Restoring scalar c2=C multiplies each
constant by C^4: h is unchanged, R4 has f-degree one, and q has f-degree
three. Since C!=0, all three values remain nonzero in characteristic zero.

Thus the second-zero locus has empty intersection with the smooth
first-compatible b=0 locus. This is an exact negative certificate for
that bounded subfamily; it is stronger than testing its seed or generic
points. It is not an exclusion of the entire spectral torsion-two locus.
An arbitrary direction-coordinate PGL2 transformation diagonalizes an
abstract smooth torsion-two root, but need not preserve the actual
embedded obstruction operator. The distinction is essential to coverage.

## Ordered squares and genuine ambient symmetries

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

## A single resultant eliminates the first correction

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

## Sixteen complete second residues

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

## Exact exclusion of the pure-direction locus

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

## The remaining mixed chart and its full rank stratification

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

## Scalar compression on the finite rank-drop stage

The [finite-algebra scalar-selection lemma](bounded_equation_certificates.md#scalar-selection-on-a-finite-algebra)
applies to a finite commutative unital Q-algebra B and elements
`s0,...,s_(m-1)` generating its unit ideal. If B has rational dimension N,
some integer `0<=t<=(m-1)N` makes `sum t^j s_j` a unit. Its sharper form
counts closed points rather than geometric length; the linked proof also
states why an analogous assertion can fail over a finite ground field.

For the length-76 first-stage algebra and sixteen denominator-cleared second
residues, the completed full-fiber exclusions say those residues generate
the unit ideal. The length bound therefore gives a sufficient search range
`0,...,15*76=1140`. The algebra is a product of a four-dimensional Q-algebra
and a four-dimensional algebra over the degree-18 field K. Each has at most
four closed points over its ground field, hence together at most eight
closed points over Q. The sharper rational bound is `0,...,15*8=120`:
a nonzero polynomial over any residue field has at most fifteen rational
roots, simultaneously across its conjugate embeddings.

No particular successful t or inverse has been computed. Once one is
specified, its inverse can be checked by multiplication in the rational
76-dimensional algebra, or separately in the four-dimensional algebras over
Q and K. This bounds a scalar-selection parameter, not the inverse's bit
size, the algebra presentation or a full negative certificate. The remaining
rank-two parameter charts are not finite algebras, so neither bound compresses
all of the torsion-two problem.

## Relation to the actual bounded degree rows

The [R-0014 six-row reduction](../results/movement_two_six_rows.md)
already bounds the actual degrees in the relevant restricted global class.
Under [R-0013](../results/saturated_actual_generator_movement.md)—actual
homogeneous sole support on C0, saturated first relation, and a full generic
coprime binary-CI initial ideal—with r=2 and movement epsilon=2, the only
unordered numerical possibilities are

    (s;a,b)=(8;8,8) or (12;6,16).

These are necessary rows, not realized STCIs. The owning
[generator and arithmetic proof](../supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md#8-smooth-root-consequence-and-remaining-work)
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

## Exact support, inherited review and reproduction

The diagonal classification, scalar normalization and dual functional were
independently reconstructed. The retained standard-library checker passed
all sixteen first identities and the three exact residues -16,-640,1648.
The accepted embedded transition remains an explicit premise.

The ordered-square coverage, actual torus/reversal, Sylvester solves,
complete dual basis and single-chart coverage passed independent mathematical
review. The generator's four chart cores were compared with the checked
source exports. Both infinity coefficient charts have completed exact
characteristic-zero exclusions. In the C2 chart independent localized runs
returned `UNIT_IDEAL`; the stronger unlocalized resultant-membership test
also has completed exact evidence. No compact multiplication-only C2 witness
was extracted. The A2 boundary has the explicit rational U*P+V*Q identity
above and its retained multiplication-only checker.

The rank-stratum script and its matrix were checked against the retained
generator. Its nineteen-point shape, squarefreeness, degree-18 factor and
rank-zero exclusion have completed exact calculations. The integrated fiber
verifier completed the rational and degree-18 cases, checking the exact shape
and smooth opens, first-stage length four over each field, and both full
unit ideals; total rational first-stage length is 76. An earlier independent
120-second degree-18 rerun timed out while constructing the second residues;
it is not counted as a second completed execution. The later integrated run
completed with a 300-second bound per call. The final timeout-output handling
change preserves partial diagnostics and does not change the mathematics.

The calculation on the remaining mixed chart over F_32003 did complete with
localized ideal {1}. The retained finite/C2/mixed generator matches that
construction. This proves only the corresponding positive-characteristic
incidence statement. The exact rational alternatives did not finish: one
reached its final Groebner computation, while variants reducing after every
multiplication exhausted their bounds before R4 assembly or their proposed
ideal test. The separate Cramer diagnostic exhausted its bound computing only
the substituted first ideal. None establishes rational emptiness, a survivor,
or a lower bound on the best algorithm.

Reproduction uses SymPy 1.14.0 and Singular 4.4.1p5 for the model/fiber checks;
the diagonal checker uses only Python's standard library. The author transfer
executed none of these programs; independent preservation review repeated the
standard-library diagonal check and obtained the same three constants. No new
Singular elimination was run for this transfer. Commands are from the repository root:

```sh
python3 research/computations/quadratic_root_diagonal_certificate.py
python3 research/computations/quadratic_root_torsion_two_model.py \
  --orientation infinity --chart C2 --output /tmp/torsion_two_C2.sing
Singular -q /tmp/torsion_two_C2.sing
Singular -q research/computations/quadratic_root_pure_direction_boundary_certificate.sing
Singular -q research/computations/quadratic_root_torsion_two_rank_strata.sing
python3 research/computations/verify_quadratic_root_rank_fibers.py
```

The model generator never launches Singular; generation alone supplies no
ideal result. The A2 full boundary ideal can be generated with
`--orientation infinity --chart A2`. The C2 stronger sufficient test uses
`--test resultant`; failure of that stronger membership test would not prove
nonemptiness. The mixed finite-field construction uses
`--orientation finite --chart C2 --mixed --characteristic 32003`.
The rank-stratum script measures only the exceptional base, not full fibers.

For a successful exclusion require the expected terminal `UNIT_IDEAL` or
`PASS: exact source substitutions and U*P+V*Q=1 over QQ`, with no preceding
Singular error. Exit zero alone is insufficient. The integrated fiber verifier
also requires `FIRST_LENGTH_4` for each field and rejects engine errors,
`NONUNIT_IDEAL`, failed shape/open checks and timeouts. Expiration of its
300-second per-call bound means incomplete execution, not a nonunit ideal.

## The remaining exact question

The finite rank-two chart has neither a rational exclusion nor a certified
surviving point. For J generated by its four first equations and sixteen
second residues, a possible exact certificate is

```
Omega^N in J,   Omega=k(k-1)Res(A,C)Disc(A)Disc(C),
```

or a point of V(J) with Omega nonzero. Retaining the six root parameters
avoids replacing the linear equations by the observed dense degree-twelve
Cramer substitutions and would cover the pivot boundaries. No adequate N or
small certificate-size bound is proved. The finite-field unit calculation
cannot replace this rational identity.

No actual surface-pair search, full K1/K2 component decomposition, exact-order-
four or singular-root exclusion, or unrestricted STCI decision was performed.
An actual-CI application still needs every [R-0006 hypothesis](../results/actual_ci_smooth_root_bridge.md)
and next normal-relation degree s>4. At s=4 the next relation changes the
obstruction target; no statement here extends the bridge to that case or
converts abstract compatibility into actual global equations.
