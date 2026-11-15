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
The [coefficient determinant criterion](#3-exact-order-two-is-a-coefficient-determinant)
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
reviewed [diagonal classification](#consolidated-historical-supplement-researchsupplementsquadratic_root_and_blowup_incidencemd)
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

The [standard-library exact checker](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/quadratic_root_diagonal_certificate.py)
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
[compact certificate](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/quadratic_root_pure_direction_boundary_certificate.sing)
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
[fiber verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_quadratic_root_rank_fibers.py)
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

The archived command uses [quadratic_root_diagonal_certificate.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/quadratic_root_diagonal_certificate.py), [verify_quadratic_root_rank_fibers.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/verify_quadratic_root_rank_fibers.py) from the pinned repository snapshot.

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


## Consolidated historical supplement: `research/supplements/QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md`

# quadratic root and blowup incidence

The proof units below retain their exact hypotheses, counterexamples and unresolved interfaces. They distinguish abstract graded data, embedded lifts and actual equations.

- [The second ambient obstruction is nonzero on the smooth torsion-two seed](#2026-10-14-generalization-quadratic-root-second-obstruction)
- [Independent review of the actual second obstruction at the smooth seed](#2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit)
- [Independent review of the universal quadratic incidence and smooth seed](#2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit)
- [Saturated first relations turn an actual CI into a primitive root-curve multiple](#2026-10-14-generalization-blowup-root-curve-primitive-bridge)
- [Independent audit of the actual-CI blowup/root-curve bridge](#2026-10-14-generalization-blowup-root-curve-bridge-independent-audit)
- [Independent audit: Cartier rational lifts on normalizations of arbitrary degree](#2026-10-14-generalization-cartier-lift-independent-audit)
- [Universal quadratic root incidence and a smooth torsion-compatible zero](#source-2026-10-14-generalization-quadratic-root-universal-incidencemd)

---

<a id="2026-10-14-generalization-quadratic-root-second-obstruction"></a>

## The second ambient obstruction is nonzero on the smooth torsion-two seed

Date: 2026-10-14. Author: `universal_root_obstruction`.
Status: **Exact actual-chart calculation, independently reviewed below** in [the sparse second-obstruction reconstruction](#2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit).
The accepted embedded chart is an input. The accepted spectral obstruction
interpretation is an input. This note computes one new higher class,
without retesting accepted chart or conormal statements.

### 1. The hierarchy detects geometry that both first tests permit

The [universal quadratic incidence note](#consolidated-historical-supplement-researchsupplementsquadratic_root_and_blowup_incidencemd)
constructs the actual first obstruction scheme `K`, proves it is smooth
of dimension four at the seed

    f=(z²+4)u²+(z²−8)v²,

and proves that this smooth elliptic root curve has ruling-difference
line bundle of exact order two. Hence both the actual first ambient
obstruction and the accepted spectral descent condition permit this
seed. Its **second** ambient obstruction is nonzero.

The second obstruction is relevant when no independent relation has yet
appeared by normal degree four, namely when the next relation degree
`s` satisfies `s>4`. In particular this includes the accepted numerical
abstract families with `s=8` and `s=12`. At `s=4`, the second relation
changes the target; the computation below does not give an exclusion.

This is a statement about the actual ambient first-relation lifting
problem. It becomes a necessary condition for actual supported complete
intersections only within a proved actual-CI-to-root-curve bridge and its
hypotheses. No unrestricted actual CI or STCI conclusion is asserted.

### 2. Retain the full chart, base motion, and equation unit

Use the accepted exact normal chart, with

```
den = z⁴+u+(3/2)zv,
w   = (z³+v)/den,
a'  = z/den−w³,
b'  = 1/den−w⁴,
u'  = a'/2,
v'  = −3w a'+2b'.
```

Its reduced base transition is `w=z^-1`; its first normal transition is
`u'=z^-7u`, `v'=z^-7v`. Set

```
f0=(z²+4)u²+(z²−8)v²,
f1=(1+4w²)u'²+(1−8w²)v'².
```

For the equation transition factor normalized by `z^-16`, choose the
first normal unit coefficient

    L1=(−5z^-4−8z^-6)u+(−(1/8)z^-1−(11/2)z^-3)v.

The first compatible cubic corrections can be chosen as

```
G0=(z/8)u²v−(3/4)uv²+(z/8)v³,
G1=−32w u'³+48u'²v'+64w u'v'².
```

Substitution into the accepted exact chart gives the literal identity
in normal degree three

    [ z¹⁶(f1+G1) ]_3 − G0 − L1*f0 = 0.                (1)

The unit `L1` differs from the quotient preimage `h` in the first-incidence
note by `2z*epsilon`, where `epsilon=[w−z^-1]_1`. This is the first
variation of `z²w²`. Keeping this term, rather than replacing `L1` by
`h`, is necessary in normal degree four. The nonlinear base coordinate
`w` is retained in both `f1` and `G1` throughout the substitution.

Let

    R4=[ z¹⁶(f1+G1) ]_4 − L1*G0.                    (2)

The terms subtracted in (2) come from the product of the first unit and
the first local correction. Unknown second unit coefficients multiply
`f0`; unknown quartic local corrections are Cech coboundaries. Thus the
second actual class is exactly the Laurent projection of (2), modulo
those multiples and coboundaries.

### 3. One sparse Serre-dual pairing proves nonvanishing

The second target is

    H1(Z,O_Z(-12,4))
      =coker[ H1(O(-14,2)) --f0--> H1(O(-12,4)) ],

with dimensions `39 -> 55 -> 16`. Use powers `z^-11,...,z^-1` in the
middle group, and `z^-13,...,z^-1` in the source. The multiplication map
is injective, since its kernel is `H0(Z,O_Z(-12,4))=0`.

Write `R4=sum_(i=0)^4 r_i(z) u^(4-i)v^i`. Only four coefficients are
needed for a nonzero dual pairing:

```
                  coefficient z^-3     coefficient z^-1
r1  (u³v)              5/8                    0
r3  (uv³)              9/8                  −3/32.
```

These coefficients follow from the exact substitution in (2). The
companion script also records every other quartic coefficient, so this
is a bounded computation with full retained output.

Put `a=z²+4`, `c=z²−8` and define

    lambda(r)=coefficient_z^-1[−c*r1+a*r3].           (3)

The polynomial dual vector is `(0,−c,0,a,0)`. It annihilates every
multiple of `f0` by a binary quadratic: on the odd source monomial `uv`
the coefficient is `a*(−c)+c*a=0`, while the other two source monomials
have only even target powers. The degree of each dual polynomial is two,
within the allowed degree ten. Therefore it also annihilates the full
Cech image of `H1(O(-14,2))`. It ignores all removed Cech coboundaries.

Using the displayed four coefficients gives

    lambda(R4)=−5/8+9/8−3/8=1/8 != 0.              (4)

Hence the actual second ambient class is nonzero. The complete rational
matrix calculation independently records multiplication rank `39` and
augmented rank `40`; the sparse identity (3)--(4) is already a proof.

### 4. This is a universal higher-obstruction mechanism on K

The seed calculation has a family-level consequence; it need not lead
to a list of further seeds. On the basepoint-free universal first
compatibility scheme `K`, the first compatible Cartier ideal is unique:
its possible differences lie in `H0(Z,O_Z(-5,3))`, which vanishes on
this entire open. The first corrections therefore glue, up to their
equation units, into the universal first lift.

Consequently there is a canonical second obstruction section over `K`.
Its rank-sixteen vector bundle is the relative version of

    coker[ H1(O(-14,2)) --f--> H1(O(-12,4)) ].

More precisely, on projective coefficient space the exact sequence is

    H1(O(-14,2)) tensor O_K(-1)
       --f--> H1(O(-12,4)) tensor O_K -> Q2 -> 0,

and the obstruction section has values in `Q2 tensor O_K(1)`.
The universal equation contributes the coefficient-space `O(1)` factor.
The multiplication map has constant rank thirty-nine: `pi_*O_Z(4)` is
globally generated of rank two and degree six, so twisting it by
`O(-12)` has no sections. Thus the cokernel is genuinely a vector
bundle, without deleting exceptional coefficient strata inside the
basepoint-free open.

The first class defines `K`; the second class is a section on `K`, not
another unrelated scalar test on the original parameter space. Its
nonzero value (4) proves that it is not identically zero on the
four-dimensional component through the smooth seed. Nonvanishing is
open, so a nonempty open subset of that component, and hence its
generic point, fails the second lifting step. The second zero locus on
that component remains to be determined. A rank-sixteen target on a
four-dimensional component does not by itself prove that zero locus is
empty, and no such claim is made.

This gives the structural next problem: describe the common zero scheme
of the actual higher-obstruction sections on `K`, intersected with the
spectral torsion loci, while retaining all equation-unit and second
relation extensions. The present computation proves that the hierarchy
adds a genuine obstruction after both the first class and Picard torsion
have passed. No additional seed or carrier-degree enumeration is needed
for that conclusion.

### 5. Exact artifacts and boundaries

- [Standard-library exact verifier](../computations/generalization_quadratic_root_seed_second_obstruction.py).
- [Full rational output and sparse dual certificate](../computations/generalization_quadratic_root_seed_second_obstruction.json).

Run with `python3 research/computations/generalization_quadratic_root_seed_second_obstruction.py`.
The verifier computes the accepted chart to normal degree four, verifies
(1), retains both the equation unit and nonlinear base motion in (2),
checks the full multiplication rank, and proves the simple pairing (4)
exactly. It does not sample, use floating point, or invoke a large CAS.

The seed has not been lifted through second exceptional order, so it
supplies no formal or projective CI construction. The result excludes
this first-relation seed from a first-principal-ideal lift through normal
degree four when `s>4`; it does not exclude every smooth root divisor,
every torsion order, or unrestricted `C0`.

---

<a id="2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit"></a>

## Independent review of the actual second obstruction at the smooth seed

Date: 2026-10-14. Author: `geometric_locus`.

Status: **THE NEW SECOND CLASS, SPARSE NONZERO PAIRING, AND STATED
FAMILY CONSEQUENCE PASS INDEPENDENT REVIEW.** The full embedded chart is
accepted input. No accepted chart or spectral theorem audit is repeated.
The calculation concerns the first principal relation through normal
degree four, so its stated CI application requires `s>4` and a proved
actual-CI-to-root-curve bridge with the relevant hypotheses.

Reviewed files:

- `2026-10-14-generalization-quadratic-root-second-obstruction.md`;
- `../computations/generalization_quadratic_root_seed_second_obstruction.py`;
- the accepted exact chart as recorded in
  `../computations/generalization_moving_first_relation_operator.py`.

The nonzero scalar below was derived independently by hand from the full
chart. It does not rely on the parent script's row reduction or on its
larger dual certificate.

### 1. The cubic patch and equation unit are consistent

Use the accepted exact chart

    den=z^4+u+(3/2)zv,
    w=(z^3+v)/den,
    a'=z/den-w^3, b'=1/den-w^4,
    u'=a'/2, v'=-3w a'+2b'.

For the seed put

    f0=(z^2+4)u^2+(z^2-8)v^2,
    f1=(1+4w^2)u'^2+(1-8w^2)v'^2.

The first base displacement is

    epsilon=[w-z^-1]_1=-z^-5 u-(1/2)z^-4 v.

Thus `beta=2z epsilon=-2z^-4 u-z^-3 v` and the proposed equation unit
is exactly `L1=h0+beta`, with `h0` the quotient preimage in the first
independent review. In particular, the unit has retained the base motion.

At normal degree three, the accepted derivation and the base factor give

    [z^16 f1]_3=Df0+beta f0.

The leading linear normal transition gives

    [z^16 G1]_3=-32z^-6 u^3+48z^-5 u^2v+64z^-6 uv^2,

for

    G1=-32w u'^3+48u'^2v'+64w u'v'^2.

The previously checked exact identity for `Df0-f0 h0` then proves

    [z^16(f1+G1)]_3-G0-L1 f0=0,

with

    G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.

This independently verifies the first patch identity, including its unit.

For a quartic local correction and a second unit `L2`, the degree-four
gluing equation contains `L1 G0+L2 f0`. Therefore the proposed discrepancy

    R4=[z^16(f1+G1)]_4-L1 G0

has the correct sign and all required contributions. The unknown `L2`
is precisely a multiple of `f0` in the quotient target. No additional
`L1^2 f0` term is forced: the free second coefficient belongs to the unit
`1+L1+L2`, and would absorb such a reparameterization of the unit.

### 2. Independent sparse quartic calculation

Only the coefficients of `u^3v` and `uv^3` at powers `z^-3` and `z^-1`
are needed. Write `Uj=[u']_j`. The first two layers are

    U1=z^-7 u,
    U2=-(5/2)z^-11 u^2-3z^-10 uv-(3/8)z^-9 v^2.

To obtain the pure `v^3` coefficient in `U3`, set `u=0` and
`t=z^-3 v`. The full chart gives the exact rational expression

    u'=(z^-3/2)*((1+(3/2)t)^2-(1+t)^3)/(1+(3/2)t)^3.

Its numerator is `-(3/4)t^2-t^3`. Expanding the denominator to the
needed order gives

    [u']_(v^3)=(19/16)z^-12 v^3.

Consequently the `uv^3,z^-3` coefficient of `z^16[u'^2]_4` is

    2*(19/16)+2*(-3)*(-3/8)=37/8.              (1)

No other normalized term contributes to the four required coefficients.
This can be checked without expanding their full polynomials. Give
`z,u,v` weights `1,0,-1`. At normal degree `n`, the weights of `w,u',v'`
are respectively `-1-4n,-3-4n,-4-4n`. In normal degree four, the weights
of the four terms of `z^16 f1` are

    u'^2: -6,    4w^2u'^2: -8,
    v'^2: -8,   -8w^2v'^2: -10.

For `u^3v` these allow powers at most `z^-5`; for `uv^3` only the first
term reaches `z^-3`, as computed in (1), and none reaches `z^-1`.
The three normalized `G1` terms have weights `-10,-10,-12`, so they
cannot contribute to these four coefficients either.

Finally multiply the explicit `L1` and `G0`. Their contributions give

```
                         z^-3 coefficient    z^-1 coefficient
R4: u^3v                      5/8                   0
R4: uv^3          37/8-(-5/8+33/8)=9/8          -3/32.
```

This derives all four coefficients in the main note directly from the
full chart and the first patch data.

### 3. The scalar is a valid quotient obstruction

The second target is the Cech quotient

    H1(O(-14,2)) --f0--> H1(O(-12,4)),

with target powers `z^-11,...,z^-1`. Its Serre dual has five polynomial
entries of degree at most ten. Let `a=z^2+4`, `c=z^2-8`. The vector

    q=(0,-c,0,a,0)

belongs to this dual space and annihilates multiplication by `f0`.
Indeed the odd source monomial `uv` gives `-ac+ca=0`, while the two
even source monomials pair with zero entries. Thus

    lambda(R)=coefficient_z^-1(-c R_u3v+a R_uv3)

is a well-defined functional on the cokernel. Its degree-two entries
also annihilate removed Cech powers: powers below `-11` cannot be
shifted to `-1`, and nonnegative powers cannot contribute.

The four checked coefficients give

    lambda(R4)=-(5/8)+(9/8)+4*(-3/32)=1/8 != 0.

This proves nonvanishing of the actual second ambient class. The
multiplication map has rank thirty-nine by the constant-rank argument
below; adjoining a single vector with this nonzero pairing therefore
raises the rank to forty. A full row reduction is not needed for this
conclusion.

### 4. The stated family consequence is valid

On the entire basepoint-free open, the possible difference between two
first Cartier lifts is a section of `O_Z(-5,3)`. The first review proved
that its `H0` vanishes everywhere there, using the globally generated
rank-two pushforward of degree four. Thus the first lift is unique as
an ideal, even though its local equations can differ by units. The
first compatibility scheme is the scheme-theoretic zero locus of the
first obstruction, so local first lifts exist over it and their
uniqueness glues them. This also applies to its nonreduced parameter
structure by the relative cohomology/base-change statement with zero
`H0` and constant-rank presentations.

The second multiplication map has constant rank on this same open.
The finite-flat pushforward has an exact sequence

    0 -> O(-2)^3 -> O^5 -> E4=pi_*O_Z(0,4) -> 0.

The bundle `E4` is globally generated, rank two, degree six. Its
splitting degrees lie between zero and six; after twisting by `O(-12)`
neither has sections. This proves injectivity of the thirty-nine-column
second multiplication map for every basepoint-free coefficient point.

Over projective coefficient space, the universal root equation has
coefficient twist `O(1)`. Hence the natural exact presentation is

    39 O_K(-1) --f--> 55 O_K -> Q2 -> 0,

with `Q2` locally free of rank sixteen. The normalized discrepancy
scales linearly with the universal equation. Its canonical second
obstruction is accordingly a section of `Q2 tensor O_K(1)`, as stated
in the main note. Uniqueness of the first ideal ensures that local
choices of first equations and units give the same quotient section.

At the smooth seed this section is nonzero. The first compatibility
scheme is smooth of dimension four there, so there is a unique
irreducible component through that point. The section is not identically
zero on that component; its nonvanishing locus is a nonempty open
subset and contains the generic point. This proves generic failure
of the second lifting step on that component. It does not prove that
the second zero locus is empty and does not assert torsion throughout
the component.

For `s>4`, no independent second relation has entered by this normal
degree, so the first-principal-ideal obstruction is relevant to the
stated bridge lane. For `s=4` the target can change, and no exclusion
was proved. The result leaves higher zero loci, their intersections
with torsion strata, later ambient extensions, and actual polynomial
realization unresolved.

---

<a id="2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit"></a>

## Independent review of the universal quadratic incidence and smooth seed

Date: 2026-10-14. Author: `geometric_locus`.

Status: **THE NEW UNIVERSAL MATRIX, SMOOTH ZERO, TORSION, AND LOCAL
DIMENSION CLAIMS PASS INDEPENDENT REVIEW.** The accepted actual first
ambient derivation is an input. This note does not repeat its chart audit,
the spectral theorem audit, or the proposed actual-CI-to-root-curve bridge
audit. No higher ambient lift or actual complete intersection is established.

Reviewed files:

- `2026-10-14-generalization-quadratic-root-universal-incidence.md`;
- `../computations/generalization_quadratic_root_curve_universal_incidence.py`.

The displayed formulae were checked independently from the accepted operator.
The explicit seed identity was first derived by hand. Two standard-library
`fractions.Fraction` calculations independently verified the reduced
differential below and the main note's full Jacobian minor `-405`.

### 1. Universal matrix and constant rank

For `f=a u^2+b uv+c v^2`, multiplication by a correction `A u+B v`
has coefficient vector

    (a A, b A+a B, c A+b B, c B).

Projection of a product with `p=p0+p1 z+p2 z^2` from the source powers
`z^-6,...,z^-1` to the target powers `z^-4,...,z^-1` gives exactly the
Toeplitz block `T(p)` in the main note. This checks all blocks of `A_f`.

Applying the accepted operator without projection first gives

    Df = d0 u^3+d1 u^2v+d2 uv^2+d3 v^3,

where

    d0=-5 a z^-4+3 b z^-5+a' z^-3,
    d1=-6 a z^-3-(7/2)b z^-4+6 c z^-5+b' z^-3+(1/2)a' z^-2,
    d2=-(3/4)a z^-2-(21/4)b z^-3-2 c z^-4+c' z^-3+(1/2)b' z^-2,
    d3=-(3/8)b z^-2-(9/2)c z^-3+(1/2)c' z^-2.

Collecting `z^-4,...,z^-1` gives all sixteen entries displayed in the
main note, including its base-derivative contributions.

The injectivity proof works on the entire basepoint-free open, including
singular and nonreduced root divisors. In fact the finite flat projection
`pi:Z->P1` gives

    0 -> O(-2)^2 -> O^4 -> E=pi_*O_Z(0,3) -> 0.

Thus `E` is a globally generated rank-two vector bundle of degree four.
Its two splitting degrees belong to `{0,...,4}`. Therefore
`H0(E(-5))=0`, and the divisor sequence implies that the multiplication
map `H1(O(-7,1))->H1(O(-5,3))` is injective. This establishes rank twelve
everywhere on the stated open.

Consequently the augmented rank condition and the incidence `A_f h=d_f`
give the same scheme there: locally an invertible twelve-row minor solves
uniquely for `h`, and the remaining four equations are the components of
the rank-four quotient obstruction. This is a scheme statement, not only
an equality of sets.

### 2. Exact seed identity and geometric smoothness

Put

    a=z^2+4, c=z^2-8, f0=a u^2+c v^2,
    h0=(-3z^-4-8z^-6)u+(-(1/8)z^-1-(9/2)z^-3)v.

Direct substitution gives

    Df0-f0 h0
      =32z^-6 u^3+((1/8)z-48z^-5)u^2v
       +(-(3/4)-64z^-6)uv^2+(1/8)z v^3.

Its specified Cech projection is zero, so this is an exact compatibility
certificate. In the prescribed source basis the vector is

    (-8,0,-3,0,0,0, 0,0,0,-9/2,0,-1/8).

The homogeneous coefficient quadratics are squarefree and disjoint.
Neither vanishes at base infinity. Over a root of `a`, the fiber point
has `v=0`, and smoothness follows from the simple root of `a`; the same
argument applies to a root of `c`, with `u=0`. Elsewhere a fiber partial
derivative is nonzero. At infinity both coefficients are nonzero, so the
fiber partial derivatives again give smoothness. This proves geometric
smoothness directly in both base charts. Equivalently the double cover
has four distinct branch points. Its root divisor is connected of genus
one.

Thus the first ambient obstruction does vanish on a smooth `(2,2)`
root curve. A proposed universal smooth-root exclusion at this order
would be false.

### 3. Independent differential calculation

The dual of the target Cech space consists of four polynomials
`q0,...,q3` of degree at most three, paired by taking the `z^-1`
coefficient of `sum q_i d_i`. The annihilator of multiplication by `f`
is given exactly by

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0.

At the seed, `b=0` and `gcd(a,c)=1`, so a basis of this four-dimensional
annihilator is

    qE=(c,0,-a,0), z qE,
    qF=(0,c,0,-a), z qF.

The differential of the quotient obstruction can therefore be computed
without choosing an inverse of any universal minor. Its four pairings
with a coefficient variation `delta f` are those of

    D(delta f)-h0 delta f

against this basis. In coefficient order

    (a0,a1,a2,b0,b1,b2,c0,c1,c2),

the resulting matrix is

```
     [  0    2   0   1/4  0   2    0   -2    0  ]
     [  1    0   8    0   4   0   -1    0  -20  ]
R =  [ -5/2  0   4    0   2   0  -1/2   0    2  ].
     [  0    8   0    1   0  -4    0    4    0  ]
```

The minor on columns `(a0,a1,a2,b2)` is `576`. Hence the quotient
differential is surjective. Since the correction directions already
span the twelve-dimensional image of `A_f0`, the full sixteen-equation
incidence Jacobian has rank sixteen.

As a separate consistency check, a second Fraction calculation built
`A_f` from its Toeplitz blocks and `d_f` from the displayed sixteen
formulas, differentiated `A_f h-d_f`, and obtained determinant `-405`
on the precise sixteen columns in the main note. The two computations
therefore verify the rank by different minors and different matrix
sizes.

The affine incidence is smooth of dimension five at `(f0,h0)`.
Projectivizing the nonzero equation `f0` removes one free scalar
direction. Uniqueness of `h` then gives a smooth four-dimensional
compatibility scheme at `[f0]`. Smoothness of the root curve is open,
so the compatible smooth-root locus has this positive local dimension.
This does not say that the ruling difference is torsion throughout it.

### 4. The seed's ruling difference has exact order two

Write `A=O_Z(1,0)`, `B=O_Z(0,1)`, and `eta=B tensor A^-1`.
On any smooth basepoint-free diagonal root curve

    a(z)u^2+c(z)v^2=0,

the section `c` of `A^2` vanishes exactly twice along the divisor of
the section `u` of `B`. Indeed at such a point, `a` and `v` are units
and the equation is `c=-a(u/v)^2`. Hence `A^2` and `B^2` are isomorphic.

The two degree-two complete linear systems cannot be isomorphic:
otherwise the two projections would differ by a projective automorphism
of `P1`, and the embedded curve in `P1 x P1` would be a graph rather
than a smooth divisor of type `(2,2)`. Thus `eta` is nontrivial of exact
order two. This argument proves the claim for the seed and, more
generally, for every smooth diagonal root curve.

An equivalent elliptic argument uses the deck involution
`sigma(z,[u:v])=(z,[-u:v])`: it preserves `B`, whereas its action on
`Pic^2` is `L -> A^2 tensor L^-1`. Again `B^2=A^2`.

Using the already accepted spectral theorem as a premise, the seed
therefore passes its even-degree descent condition. The present review
does not independently re-prove that theorem. First ambient compatibility
and spectral torsion coexist at this exact seed. Actual second ambient
compatibility, later lifts, polynomial realization, and support remain
separate questions.

### 5. Optional diagonal-slice classification

This section is an additional exact lemma, not needed for the preceding
review or the next obstruction calculation. Work geometrically over an
algebraically closed field of characteristic zero and impose `b=0`.
For a smooth diagonal root curve, `a,c` are squarefree, have no common
homogeneous root, and at least one has polynomial degree two.

The preceding dual basis remains exhaustive with

    q=(cL,cM,-aL,-aM), deg L,deg M<=1.

Set `W=ca'-ac'`. Its pairings with `Df` are the `z^-1` and `z^-2`
coefficients of

    E=-3ac z^-4+W z^-3+(3/4)a^2 z^-2,
    F=-(3/2)ac z^-3+6c^2 z^-5+(1/2)W z^-2.

Projection before pairing gives the same residues: discarded powers
below `-4` are at most `-5`, while every dual polynomial has degree at
most three; discarded nonnegative powers also cannot contribute.
The four compatibility equations are therefore

    (3/2)a0 a1-4a1 c2-2a2 c1=0,
    (3/4)a0^2-5a0 c2-3a1 c1-a2 c0=0,
    6c2^2-(5/2)a0 c2-(3/2)a1 c1-(1/2)a2 c0=0,
    -2a0 c1-a1 c0+12c1 c2=0.

Subtracting twice the third equation from the second gives
`a0^2=16c2^2`. Smoothness forces `c2!=0`: if `c2=0`, then `a0=0`
and the first equation gives `a2 c1=0`; either the coefficient
quadratics have a common root at infinity or `c` has a double root
there. Put `C=c2` and `P=a2`.

When `a0=4C`, any solution with `a1,c1` nonzero has `a,c`
proportional, contradicting basepoint freeness. Thus `a1=c1=0`,
`P c0=-8C^2`, and `P!=0`.

When `a0=-4C`, either `a1=c1=0` and `P c0=32C^2`, or

    P c0=-100C^2,
    P c1=-5C a1,
    a1^2=-(44/5)PC.

All three alternatives are smooth. In the last case the two quadratic
discriminants are `(36/5)PC` and `180C^3/P`, both nonzero. The only
possible common finite root is `z=-16C/a1`; substitution into `a`
gives `-(540/11)C`, also nonzero. In the two even alternatives the
squarefreeness and absence of common roots are immediate from the
displayed nonzero constants.

Under scaling of `f` and the compatibility-preserving coordinate change
`z -> lambda z, v -> lambda^-1 v`, every smooth compatible diagonal
curve has one of these three normal forms:

    (z^2+4)u^2+(z^2-8)v^2;
    (z^2-4)u^2+(z^2+32)v^2;
    (z^2+t z-4)u^2+(z^2-5t z-100)v^2, t^2=-44/5.

The two signs of `t` are identified by `lambda=-1`.

---

<a id="2026-10-14-generalization-blowup-root-curve-primitive-bridge"></a>

## Saturated first relations turn an actual CI into a primitive root-curve multiple

Date: 2026-10-14. Author: root. Status: **WRITTEN GEOMETRIC THEOREM;
independently audited under the stated hypotheses**. The
[independent bridge audit](#consolidated-historical-supplement-researchsupplementsquadratic_root_and_blowup_incidencemd)
includes separate local-algebra and conormal reviews, a shorter local
proof, and a defect-boundary family. The spectral root-curve criterion and its
already reviewed ambient obstruction class are premises. This note
supplies a bridge from an actual supported complete intersection to
that obstruction. It does not assert that the obstruction is nonzero.

### 1. Hypotheses

Let C be a smooth curve in a smooth threefold X over an algebraically
closed field of characteristic zero. Let Y=(F,G) be an actual complete
intersection supported exactly on C. Use the ordinary I_C-adic initial
ideal. Assume:

1. Its first nonzero generic normal relation has degree r and its actual
   degree-r relation sheaf R is a saturated line subbundle of Sym^r N_C^*.
2. Both actual equations F,G have generic normal order r. Their leading
   symbols generate R at every point. Equivalently their coefficient
   pair in local frames of R has no common zero on C.
3. The full generic initial ideal is a binary regular sequence (f_r,g_s),
   with s>r, and g_s coprime to f_r. Set k=s-r and assume k>=2.
4. The actual Cartier root divisor Z of f_r on the exceptional divisor
   of Bl_C X is smooth, hence reduced. Smoothness of its reduced support
   alone is insufficient. It may be treated componentwise if disconnected.

The first hypothesis often forces the second when the two equations
generate the whole actual relation sheaf; it is nevertheless stated
explicitly here. A divisor where both leading coefficients vanish is a
genuine excluded hypothesis, not a set to be saturated away. At such
points vertical exceptional components may occur.

Let B=Bl_C X, let E be its exceptional divisor, and let D_F,D_G be the
strict-transform Cartier divisors. Their local equations are obtained
by dividing the pullbacks of F,G by the r-th power of an exceptional
equation. Write Y'=D_F intersect D_G.

### 2. The strict intersection has support exactly Z

Off E the blowup is an isomorphism and the original intersection has
no point off C. Hence Y' is supported on E. On E the two transformed
equations are a f_r and b f_r, where a,b are the actual leading
coefficients. Since a,b have no common zero, their common zero set on
E is exactly Z. In particular no exceptional fiber P1 over a point of
C is a curve component of Y'. Such a fiber could be shared only if
both leading coefficients vanished there, or if f_r vanished on the
whole fiber; both possibilities are excluded by the hypotheses.

The two strict divisors have no common surface component, since their
images would be a common surface component of F,G. They form a
regular sequence on the smooth threefold B. Thus Y' is a pure
one-dimensional complete intersection with reduced support Z; there
is no discarded isolated or embedded component.

At the generic point of C, the usual normal blowup calculation for
the binary regular sequence (f_r,g_s) gives transverse length k=s-r
on every root branch. Indeed one may choose a standard basis of
normal orders r,s generating the actual completed generic ideal: a
lift of g_s together with an original equation whose leading symbol
is f_r generates the full initial ideal, hence the actual ideal by
filtered division. Both original equations were divided by u^r, so
this invertible change of generators preserves their strict-intersection
ideal. On a chart with exceptional parameter u, its generators reduce to

```
f_r+O(u),   u^(s-r)(g_s+O(u)) modulo the first equation.
```

A smooth root is simple over the generic point, and g_s is nonzero
there. Eliminating the first equation leaves u^k. Therefore the
generic algebra of Y' along each component of Z is curvilinear of
length k. This calculation uses the full generic initial regular
sequence, not merely two chosen original normal orders.

### 3. The first normal layer is a line bundle everywhere

The conormal sequence for Z subset E subset B is

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0.          (1)
```

Project the first normal symbols of D_F,D_G to the last term. They
are precisely a df_r,b df_r. Smoothness of Z makes df_r a local
generator of O_Z(-Z_E), and the coefficient pair is basepoint-free.
Thus their joint normal-symbol map surjects onto the last term.
Here df_r is the full conormal differential on E, including its base
direction; it is not just the fiber derivative. Smooth ramification
of Z over C causes no failure of this surjectivity.

Their determinant vanishes generically on every component of Z:
the intersection has transverse length k>=2 and is generically
curvilinear. The determinant is a regular section of a line bundle
on the smooth reduced Z, so it vanishes identically. The two first
symbols therefore have rank one at every point, and at least one
has a unit projection to the last term of (1). Their image K is a
line subbundle, with an isomorphism

```
K -> O_Z(-Z_E).
```

This splits (1). Its quotient is canonically O_Z(-E). In particular
the **actual** first ordinary normal layer of Y' is

```
J/J^2 = O_Z(-E),   J=I_Z O_(Y'),                    (2)
```

without a point-supported torsion term. This conclusion would be
false if joint leading base points had been removed instead of
retained.

### 4. The entire strict intersection is primitive

The preferred proof is local on the smooth strict surface and works
before completion. At a point p of Z, choose one transformed equation
h whose leading coefficient is a unit. Since h|E=a f_r with a(p)!=0
and Z is smooth in E, the surface S=(h) is smooth at p and meets E
transversely along Z. An exceptional equation u therefore cuts out
Z as a reduced Cartier divisor on S.

The other transformed equation h_2 restricts to a nonzero equation
on S supported exactly on Z. The regular local surface ring is a
UFD, so h_2|S is a unit times u^e. Its generic multiplicity is the
already computed k=s-r; consequently e=k and

```
I_(Y',p)=(h,u^k).
```

This proves embedded primitivity everywhere and identifies its
surviving conormal with O_Z(-E). It also realizes Y' locally as a
Cartier divisor on the exceptional thickening E_k=V(I_E^k).

For completeness, the original formal argument is consistent with
this direct proof. At a point of Z complete and lift a curve parameter
t. Purity makes t a nonzerodivisor, and the local ring A of Y' is finite free of
rank k over R0=Bbbk[[t]]. Its nilradical J has J^k=0 everywhere, by
purity and the generic nilpotence bound. From (2), Nakayama makes
J a principal ideal generated by a lift z of its free first layer.
The reduction of A modulo t is consequently generated by z. Thus
R0[z]/(z^k) maps surjectively to A; both are free of rank k, so the
map is an isomorphism.

Hence Y' is an actual embedded primitive k-fold curve everywhere
along Z. Its local smooth containing equation has first relation
K from Section 3, and its surviving conormal is O_Z(-E). This is
stronger than generic curvilinearity or a numerical socle match.
No socle-degree enumeration is needed to obtain primitivity here.

### 5. Consequence for the ambient root-curve obstruction

Let J_E=O_E(-E). The square-zero first neighborhood of E has the
reviewed class

```
kappa in Ext1_E(Omega_E,J_E).
```

For its smooth Cartier root divisor Z, restriction and contraction
with df_r gives the conormal extension (1), whose class is

```
kappa(df_r) in H1(Z,O_Z(Z_E) tensor J_E|Z).           (3)
```

Section 3 splits that extension. Therefore every actual supported
complete intersection satisfying the hypotheses must have

```
kappa(df_r)=0.                                     (4)
```

The local ideal (h,u^k) shows that I_E^k is contained in I_(Y'),
and I_(Y')/I_E^k is locally the invertible ideal generated by h on
E_k. Thus the primitive k-fold structure is an actual global Cartier
lifting of Z into E_k and supplies compatibility of the same
Cartier relation through every exceptional order strictly below k.
Those are the root-curve obstruction bundles already identified in
the spectral note. If their relevant H0 groups vanish, compatible
finite principal ideals are unique, but their actual obstruction
classes must still be evaluated; negative bundle degree is not
itself a nonvanishing theorem.

For the accepted C0 conormal O(-7)^2, E=P1 x P1 and
J_E=O(-7,1). A first quadratic relation of movement degree two
has root divisor of type (2,2). The entire family has first target

```
H1(Z,O_Z(-5,3))
 = coker[H1(O(-7,1)) --f--> H1(O(-5,3))],
dimensions 12 -> 16 -> 4.
```

Thus one universal lifting incidence on the coefficients of f is
necessary for every actual CI in this lane, independently of
both hypersurface degrees. This is the appropriate shared next
problem, rather than enumerating the numerical profiles of the
abstract elliptic graded families.

### 6. Boundaries and audit disposition

The theorem leaves nonzero first-relation defects, singular or
nonreduced root divisors, noncoprime next relations and k=1 outside
the primitive conclusion. The generic normal order of the chosen
two equations, their joint leading base points, and full original
set-theoretic support are substantive hypotheses. None is inferred
from generic Hilbert data alone.

The independent audit passes the generic blowup multiplicity, exact
support and absence of vertical fiber components, global conormal
splitting, entire embedded primitivity, and necessity kappa(df_r)=0.
It retains the first-relation defect boundary explicitly: the family
F=t f_r+h_(r+1), G=F+f_r^q, with f_r squarefree, h_(r+1) coprime,
and q>=2, is supported exactly on C=(x,y) but has actual first
relation t O_C f_r. Both leading coefficients vanish at t=0, and
the strict intersection contains that entire exceptional fiber.
Saturating the first relation cannot discard this boundary.

The actual ambient class still has to be evaluated. The accepted
spectral criterion, normal bundle, ambient chart and earlier carrier
exclusions were not reverified.
The universal STCI question and unrestricted C0 remain open.

---

<a id="2026-10-14-generalization-blowup-root-curve-bridge-independent-audit"></a>

## Independent audit of the actual-CI blowup/root-curve bridge

Date: 2026-10-14. Status: **NEW GEOMETRIC BRIDGE PASSES UNDER ITS
LITERAL HYPOTHESES**. Reviewer: independent bridge-review worker, with
separate local-algebra and conormal subreviews. This is a written
mathematical audit, not a finite computation or a claim of ambient
obstruction nonvanishing.

Reviewed source:
[blowup/root-curve primitive bridge](#consolidated-historical-supplement-researchsupplementsquadratic_root_and_blowup_incidencemd).
The accepted
[spectral root-curve theorem](../supplements/MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-relations)
and its
[independent audit](../supplements/MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-independent-audit)
are premises. Their spectral descent criterion, ambient extension class,
and cohomology targets were not reaudited. No previous CAS or carrier
certificate was replayed.

### 1. Precise conclusion and hypotheses

Let `C` be a smooth curve in a smooth threefold `X` in characteristic
zero. Work on a connected component of `C` when necessary. Let an actual
complete intersection `Y=(F,G)` have reduced support exactly `C`. Retain
all the hypotheses in the reviewed source:

- The first actual ordinary normal relation has degree `r`; its relation
  sheaf is a saturated line subbundle `R` of `Sym^r N_C^*`.
- The two **chosen actual equations** have generic normal order `r`, and
  their degree-`r` symbols jointly generate `R` at every point of `C`.
- At the generic point of `C`, the **full ordinary initial ideal**, not
  just two selected initial forms, is the binary regular sequence
  `(f_r,g_s)`, where `s>r`, `g_s` is coprime to `f_r`, and `k=s-r>=2`.
- The actual Cartier root divisor `Z=(f_r)` on the exceptional divisor
  `E` of `B=Bl_C X` is smooth. In particular, `Z` itself is reduced;
  smoothness of its reduced support alone is insufficient.

Then the intersection `Y'=D_F intersect D_G` of the strict-transform
Cartier divisors has support exactly `Z`, contains no vertical
exceptional-fiber curve component, and is everywhere an embedded
primitive `k`-fold structure on `Z`. Its first ordinary normal layer is
canonically `O_Z(-E)`. The conormal extension

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0             (1)
```

splits, so the actual first ambient root-divisor obstruction obeys

```
kappa(df_r)=0.                                        (2)
```

The conclusion concerns this stated lane of actual supported complete
intersections. It makes no claim that the hypotheses exhaust all STCI
presentations, and it makes no claim that the fixed ambient obstruction
has a nonzero value.

### 2. Support, vertical fibers, and purity

Locally write the exceptional equation as `u`. Because each chosen
equation has normal order `r`, its strict transform is obtained by
dividing its pullback by `u^r`. On `E`, the two transformed equations
restrict to `a f_r,b f_r`. The coefficient pair `a,b` has no common zero
on `C`, and the line-subbundle condition means that `f_r` is not the zero
binary polynomial on any exceptional fiber.

The common zero set on `E` is therefore exactly `Z`. Away from `E`, the
blowup is an isomorphism, and the original pair has no common point away
from `C`. Thus `Supp(Y')=Z`. In particular, no entire exceptional fiber
is a component of the strict intersection.

Neither strict divisor contains `E`. A common surface component outside
`E` would give a common surface component of the original pair. Hence
the strict equations have height two in the smooth threefold `B` and
form a regular sequence. Their intersection is a one-dimensional
Cohen--Macaulay scheme with no embedded or isolated component. No
component or closed point has been discarded in this argument.

### 3. Generic transverse multiplicity really is `s-r`

Let `K` be the function field of `C`, and complete the generic normal
local ring to `K[[x,y]]`. Choose a lift `H` in the actual ideal whose
initial form is `g_s`. Use one original equation with nonzero generic
leading coefficient as `P`; its initial form is a nonzero scalar
multiple of `f_r`. Since these initial forms generate the **entire**
initial ideal, successive filtered division gives

```
(P,H)=(F,G) in K[[x,y]].                              (3)
```

One can also obtain (3) from equality of the two finite colengths: the
coprime homogeneous initial forms of `P,H` give colength `rs`, equal to
the colength determined by the stated full initial ideal of `(F,G)`.
Consequently these two generating pairs differ by an invertible local
matrix. Both original equations were divided by the same `u^r`, so this
change of generators preserves the strict-intersection ideal.

On a normal blowup chart `x=u,y=uv`, that ideal is

```
( P/u^r, H/u^r )
 = ( f_r(1,v)+O(u), u^(s-r)(g_s(1,v)+O(u)) ).          (4)
```

After a finite extension of `K`, each generic root can be treated
separately. The root is simple because the actual root divisor is
smooth and reduced, finite over `C`, and generically separable in
characteristic zero. Coprimality makes the second parenthesis a unit at
that root. The first equation eliminates the root coordinate, leaving
the transverse algebra `L[[u]]/(u^k)`, where `L` is the root field and
`k=s-r`. This proves the claimed multiplicity on every root component.

Two arbitrary selected orders would not justify (3) or (4). The full
generic initial complete-intersection hypothesis is doing substantive
work here.

### 4. Direct local proof of primitivity everywhere

There is a shorter proof than the completion argument in the reviewed
source, and it proves a useful additional local normal form. Fix
`p in Z`. Choose one transformed equation `h` whose leading coefficient
is a unit at `p`. This is possible by joint leading basepoint freeness.
Since

```
h|E = a f_r,                 a(p) != 0,
```

and `Z` is smooth in `E`, the surface `S=(h)` is smooth at `p` and meets
`E` transversely along `Z`. In particular the exceptional equation `u`
cuts out `Z` as a reduced Cartier divisor on the regular local surface
`S`.

Let `h_2` be the other strict equation. Its restriction to `S` is
nonzero and has zero set exactly `Z`. In the regular local ring
`O_(S,p)`, it must therefore be

```
h_2|S = epsilon u^e,              epsilon a unit.       (5)
```

Indeed a two-dimensional regular local ring is a UFD, and `(u)` is the
only height-one prime in its zero set. The generic multiplicity from
Section 3 fixes `e=k`. Lifting the unit in (5) gives the exact local
ambient ideal

```
I_(Y',p) = (h,u^k)                                   (6)
```

already before completion. This proves the entire embedded primitive
conclusion at every point, not only generic curvilinearity. It also
proves directly that the surviving conormal is the exceptional
conormal `O_Z(-E)`.

The source's completion/Nakayama proof passes as well: over a completed
smooth-curve parameter ring the local algebra is finite free of rank
`k`; a generically zero submodule is zero by torsion freeness, so `J^k=0`;
the invertible first layer makes `J` principal; the resulting surjection
from the rank-`k` truncated polynomial algebra is an isomorphism. The
direct proof (6) avoids those auxiliary finiteness and nilpotence steps.
For readability, its coefficient field should be denoted `Bbbk` rather
than `k`, since `k` already denotes the multiplicity.

### 5. Conormal splitting, including ramification points

For an independent check of the source's conormal argument, put

```
L=O_Z(-E), M=O_Z(-Z_E), V=I_Z/I_Z^2.
```

Let `phi` be the map from the two equation line bundles to `V` given by
their first normal symbols. The quotient map `q:V -> M` sends these
symbols to `a f_r,b f_r` in the conormal line, or to `a df_r,b df_r`
under its differential embedding in `Omega_E|Z`. Hence `q phi` is
surjective.

The determinant of `phi` vanishes at the generic point of every
component of `Z`: independent linear terms there would give transverse
length one, contrary to `k>=2`. Since `Z` is reduced, this regular
determinant section vanishes identically. Locally choose a symbol `v`
with `q(v)` a unit and complete it to a basis `v,e` of `V`. Writing the
other symbol as `av+be`, the zero determinant forces `b=0`. Thus

```
K=im(phi) is a line subbundle,  K -> M is an isomorphism,
V/K = L canonically.                                  (7)
```

This splits (1). Moreover, with `J=I_Z O_(Y')`, the ordinary first layer
is exactly

```
J/J^2 = I_Z/(I_Z^2+I_(Y')) = V/K = O_Z(-E),            (8)
```

so no point-supported torsion has been suppressed.

Here `df_r` means the **full differential on `E`**, including the base
direction. No unramifiedness hypothesis on `Z -> C` is needed. For
example, at a smooth ramification point the root equation may be
`f=t-v^2`: its fiber derivative vanishes at the origin, but
`df=dt-2v dv` does not. Using only the fiber derivative would invalidate
this argument.

### 6. Actual exceptional lifts and the obstruction implication

The local form (6) also globalizes the higher-order interpretation.
Writing `E_k=V(I_E^k)`, one has `I_E^k subset I_(Y')`, and
`I_(Y')/I_E^k` is locally generated by the nonzerodivisor `h` on `E_k`.
It is therefore an invertible ideal on `E_k`. Thus `Y'` is an actual
Cartier lifting of `Z` into `E_k`, and restriction gives compatible
Cartier liftings through every exceptional order strictly below `k`.
This does not supply lifts at or beyond order `k`.

The first obstruction implication can also be checked directly from
the conormal diagram. Restrict the ambient cotangent extension to `Z`:

```
0 -> L -> Omega_B|Z -> Omega_E|Z -> 0.
```

Its extension class is the restriction of the accepted first-neighborhood
class `kappa`. Pull it back along

```
df_r:M -> Omega_E|Z.
```

Because `Z` is smooth, the pullback middle term is precisely `V`, giving
(1). Consequently

```
class(1) = df_r^*(kappa|Z)
         in Ext1_Z(M,L)
          = H1(Z,O_Z(Z_E) tensor O_Z(-E)).              (9)
```

The splitting in (7) proves (2). This uses the actual geometric class,
not merely the dimension of its cohomology target. An opposite Cech
extension convention can negate its representative and has no effect
on the vanishing assertion.

### 7. Nonzero first-relation defects must retain their base points

The hypotheses cannot be replaced by saturation of a defective first
relation. The following family exhibits the precise failure without
any degree enumeration.

In `A3_(t,x,y)`, let `C=(x,y)`. Choose a squarefree homogeneous binary
form `f_r(x,y)` and a homogeneous form `h_(r+1)(x,y)` coprime to `f_r`.
For an integer `q>=2`, set

```
F=t f_r+h_(r+1),       G=F+f_r^q.                     (10)
```

This is an actual height-two complete intersection supported exactly on
`C`: its common zero set is `f_r=h_(r+1)=0`, whose only normal-plane point
is the origin. Both chosen equations have generic normal order `r`.
Over `Bbbk(t)`,

```
(F,G)=(t f_r+h_(r+1), h_(r+1)^q),
```

and the coprime initial forms give the full generic initial complete
intersection of degrees `(r,q(r+1))`, with gap at least two. The
saturated first relation has the smooth root divisor given by the
distinct constant root sections of `f_r`.

However, the **actual** degree-`r` relation sheaf is `t O_C f_r`, whose
inclusion has a first-relation defect at `t=0`. Both actual leading
coefficients vanish there. On the exceptional divisor, the restrictions
of the two strict equations are both `t f_r`, so their intersection
contains the entire exceptional fiber over `t=0`.

Thus the nonzero defect is a real boundary stratum. Its joint leading
base point cannot be deleted or cured by replacing `t O_C f_r` with its
saturation. This family is outside the reviewed theorem and does not
contradict it.

### Audit disposition

The generic blowup length, exact support/no-vertical-component claim,
global first-layer splitting, entire embedded primitivity, and necessity
`kappa(df_r)=0` all pass under the literal hypotheses. The direct local
normal form `(h,u^k)` supplies a structural proof with no socle-profile
or degree enumeration. The retained boundaries are the actual
first-relation defect and its base points, singular or nonreduced root
divisors, noncoprime next relation, generic initial ideals outside the
stated binary complete-intersection form, unequal chosen normal orders,
and gap one. The value of the fixed ambient obstruction remains a
separate new problem. The universal STCI question and unrestricted
characteristic-zero `C0` remain open.

---

<a id="2026-10-14-generalization-cartier-lift-independent-audit"></a>

## Independent audit: Cartier rational lifts on normalizations of arbitrary degree

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW SINGULAR-NORMALIZATION EXTENSION UNDER ITS
EXPLICIT CARTIER, SINGLETON AND DEGREE-ONE LIFT HYPOTHESES**.

Source audited:
[Cartier-lift minimal-degree theorem](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md),
SHA-256 `0a120c0caf2847b38c749fd47adddc0896a864c1b44e1646225889b34f7055ba`.
The [smooth-normalization theorem](normal_filtration_boundary_obstructions.md#source-2026-10-13-generalization-smooth-normalization-independent-auditmd)
is an accepted premise and was not rechecked. This audit concerns only the
new singular scope, cone polarization and added consequences. No inherited
verifier, mathematical source or remote branch was reread to reconfirm it.

### 1. Exact theorem and new scope

Over an algebraically closed field of characteristic zero, let a smooth
rational curve C of degree d have an actual mate on an integral degree-a
hypersurface X. Let `nu:S->X` be its finite normalization and
`H=nu*O_X(1)`. Assume the full reduced inverse image is a single smooth
curve c mapping isomorphically to C and **c is Cartier on S**.

Then the complete system |c| identifies S with a normal minimal-degree
surface. In addition to the accepted smooth entries, the only new entry is
a rational-normal cone of degree

    n=c^2=d^2/a>=2,
    H=(d/n)c,
    n divides d.

For fixed C0, the accepted all-quartic theorem leaves exactly three
normalization/polarization targets:

    a=8:  P1xP1, c=(1,1), H=(2,2);
    a=8:  quadric cone, c a smooth Cartier conic, H=2c;
    a=16: P2, c a line, H=4h.

The new target is the quadric cone. Actual projections and complete
conductor descent remain conditions, so none of these entries asserts an
existing mate. Non-Cartier lifts and multiple or nonisomorphic inverse
curves remain outside the theorem.

### 2. Independent review of the extra singular argument

At a closed point of c, let R be the normal surface local ring and f a
local Cartier equation. Since `R/(f)` is the regular one-dimensional
local ring of c, a lift t of its parameter together with f generates
the maximal ideal of R. Thus its embedding dimension is at most two,
equal to its dimension. R is regular. At the generic point normality
already gives a DVR. Therefore S is regular along all of c; over the
algebraically closed characteristic-zero field it is smooth there.
Its possible singularities are isolated and disjoint from c.

The actual mate divisor gives `m c~bH`, `md=ab`. This makes O_S(c)
ample directly: a positive power is the ample O_S(bH). In particular
`n=c^2=d^2/a` is a positive integer. Cartierness supplies the integral
self-intersection even though S may have singularities elsewhere.

Choose a resolution `sigma:M->S` that is an isomorphism near c. No
exceptional component occurs in the pullback of c, because the resolution
centers lie away from its support. Consequently

    c_M=sigma*c,
    c_M^2=n,
    m c_M~b L, where L=sigma*H is nef and big.

Adjunction takes place in the unchanged smooth neighborhood of c_M and
gives `K_M.c_M=-n-2`. Hence

    K_M.L=(m/b)(-n-2)<0.

An effective canonical multiple has nonnegative intersection with the
nef L, so none exists. The already used characteristic-zero surface
classification makes M rational or birationally ruled over a
positive-genus curve. The latter ruling extends after the point
contractions to its minimal ruled model. Its restriction to the rational
c_M is constant, so c_M is a fiber component. Intersecting that effective
fiber with c_M gives

    0=m0*c_M^2+sum mi*(Di.c_M),

with m0>0 and every remaining intersection nonnegative. This contradicts
n>0. Therefore M is rational. Notice that c_M need not be ample on M;
positive self-intersection is enough for this ruling contradiction, and
nefness of L is enough for the canonical argument.

Normality gives `sigma_*O_M=O_S`. The degree-one Leray edge sequence has
an injection

    H1(S,O_S) -> H1(M,O_M)=0.

Thus `H1(S,O_S)=0`. This step requires no vanishing of
`R1 sigma_*O_M` and no prior rational-singularity hypothesis. In
particular the proof has not smuggled such a hypothesis into the new
singular scope.

The accepted complete-system argument now applies using the actual
Cartier sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

Its proof uses ampleness, this restriction surjectivity and the degree
bound, rather than smoothness away from c. It gives a finite birational
map to an integral normal minimal-degree surface. A finite birational
map to a normal target is an isomorphism. The surface classification
therefore supplies the plane, Veronese, smooth scroll or rational-normal
cone; in dimension two there is no additional singular family.

### 3. Cone Picard computation and integral polarization

For the degree-n rational-normal cone with n>=2, its minimal resolution
is F_n. Write its exceptional negative section E and fiber f, with

    E^2=-n, E.f=1, f^2=0.

The hyperplane pullback is `L_c=E+n f`. This is the usual cone
polarization: it has degree zero on the contracted E, degree one on
each ruling f and square n. The smooth Cartier hyperplane c avoids
the vertex, consistently with regularity along c established above.

Pullback on line bundles is injective. Indeed, if a line bundle A
pulls back trivially, the projection formula and
`sigma_*O_M=O_S` give

    A=sigma_*sigma*A=sigma_*O_M=O_S.

Every pulled-back Cartier line bundle has degree zero on the contracted
E. In the free Picard group `Pic(F_n)=ZE+Zf`, a class xE+yf
therefore satisfies

    -n x+y=0,

so it is an integer multiple of L_c. Since c itself pulls back to
L_c, injectivity implies `Pic(S)=Z[c]`, with no unnoticed fractional
or torsion generator. Thus the ample H is an integer multiple q c,
and

    d=H.c=q n,
    q=d/n,
    n divides d,
    a=H^2=d^2/n.

This proves the only extra integrality constraint needed by the singular
extension. For n=1 the cone is P2 and already belongs to the line entry.

For d=4, the new cone degrees are n=2 and n=4. The latter would have
a=4 and is removed by the accepted theorem. The former has a=8 and
is the quadric cone with H=2c. Together with the two accepted smooth
higher targets this gives the complete three-entry list.

### 4. Additional degree-free corollary: downstairs Cartier rational curves

The source's normal-carrier consequence is correct. In fact its scope
can be strengthened without using the characteristic-zero classification.

**Corollary, every characteristic.** Let C be a smooth integral curve of
degree d and genus g over an algebraically closed field. Suppose an
integral degree-a hypersurface X contains C as a Cartier curve and has
an actual mate for C. Then X is normal and

    a divides d^2,
    2g-2=d^2/a+(a-4)d.                         (G)

Consequently a is a positive divisor of d^2 and satisfies the strict
bound `a<4+(2g-2)/d`, independent of the mate degree. For rational C,
the only numerical possibilities are

    X a plane, C a line or smooth conic;
    X a quadric, C a smooth Cartier conic.

In particular every smooth rational curve of degree d>=3 is non-Cartier
on every integral carrier on which it has a mate. This statement is about
Cartierness on X itself; it does not exclude the three nonnormal
Cartier-normalization-lift targets above.

Proof of normality. The same quotient-regular local argument makes X
regular along the smooth Cartier C. The mate's Cartier zero divisor D
has reduced support C. In the regular neighborhood of C it is `m C`
for one positive integer m; away from C both Cartier divisors are zero.
Thus `m C~b O_X(1)` globally, and C is ample. Every codimension-one
nonregular component would be a projective curve disjoint from C.
Its restriction of O_X(C) would be trivial, since the canonical section
has no zero there; ampleness would require strictly positive degree.
This is impossible. Thus X satisfies R1. A hypersurface is Cohen--Macaulay,
hence S2, so Serre's criterion makes X normal. This argument permits
possible isolated singularities away from C.

Now `n=C^2=d^2/a>0` is an integer, proving `a divides d^2`.
Cartier adjunction in the smooth neighborhood of C, together with
`omega_X=O_X(a-4)`, gives equation (G). The strict bound follows by
dividing it by d and retaining the positive summand d/a.
For rational C, this becomes

    (a-4)d=-n-2=-d^2/a-2.                     (A)

Thus a>=4 is impossible. For the three remaining positive carrier
degrees, equation (A) gives respectively

    a=1: (d-1)(d-2)=0;
    a=2: (d-2)^2=0;
    a=3: d^2-3d+6=0.

The last polynomial has negative discriminant, so has no real, hence
no positive integer, root. This proves the numerical list. These are
ordinary integer intersection calculations in every characteristic,
not equations reduced modulo the field characteristic. No Frobenius
or surface-resolution input is used.

For fixed C0, the corollary directly forces a genuine non-Cartier
singularity on every normal mate-admitting carrier, in every degree.
This conclusion does not require repeating the inherited all-quartic
proof. A nonnormal carrier may still have a Cartier lift upstairs while
C is non-Cartier downstairs; complete conductor descent remains the
obstruction in that case.

### 5. Review boundaries and continuation

The extension changes the support lane from smooth S to normal S with
Cartier c. It does not classify the non-Cartier singularities, bound their
Cartier indices, or force every presentation to have a degree-one
singleton lift. A finite inverse curve of degree greater than one, or
several inverse-image primes, requires its actual coefficient-vector
divisor relation.

The three fixed-C0 normalization targets have a primitive normalized
degree-one section Q with divisor 2c or 4c. The source's assertion that
normalized mates are scalar powers follows from the exact polarization
and the fact that two nonzero projective sections with the same divisor
differ by a global unit, hence a scalar. Whether any such power descends
through the full conductor is a separate question. This audit establishes
neither single-field residue bounds nor a uniform bound on split phase
orders for their actual four-coordinate projections.

No mathematical verifier was executed. The review consists of the new
local regularity, resolution/Leray and cone Picard arguments and the
displayed additional adjunction proof. The previously accepted smooth
proof and all-quartic result retain their original provenance. Neither a
universal STCI theorem nor an unrestricted counterexample is claimed.

---

<a id="source-2026-10-14-generalization-quadratic-root-universal-incidencemd"></a>

## Universal quadratic root incidence and a smooth torsion-compatible zero

Date: 2026-10-14. Author: `universal_root_obstruction`.
Status: **Exact reduction and explicit geometric boundary, independently reviewed** in [the universal-incidence reconstruction](#2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit). The accepted spectral root-curve theorem and its
independent audit, together with the accepted actual chart operator,
are premises. No accepted chart or conormal audit is repeated.

### 1. One matrix covers every moving quadratic relation of movement two

Work in characteristic zero with the actual balanced conormal of `C0`.
Write

    f=a(z)u²+b(z)uv+c(z)v²,
    a=a0+a1 z+a2 z², b=b0+b1 z+b2 z², c=c0+c1 z+c2 z².

The coefficients are homogeneous degree-two sections on the base. Let
`U` be the open subset of `P8` where `a,b,c` have no common base zero.
The root divisor `Z=(f=0)` is then finite flat of degree two over the
base, including when it is singular or nonreduced.

The accepted first ambient class is the image of

    d_f=pr[Du f_u+Dv f_v+alpha f_z]

in `coker A_f`, where `pr` retains the Laurent powers `z^-4,...,z^-1`,
and

    Du=−(5/2)z^-4 u²−3z^-3 uv−(3/8)z^-2 v²,
    Dv=3z^-5 u²−z^-4 uv−(9/4)z^-3 v²,
    alpha=z^-3 u+(1/2)z^-2 v.

Use the source basis `z^-6,...,z^-1` first times `u`, then times `v`.
Use the target basis `z^-4,...,z^-1` first times `u³`, then times `u²v`,
then times `uv²`, then times `v³`. For `p=p0+p1 z+p2 z²`, set

```
         [ p2 p1 p0  0  0  0 ]
T(p)  =  [  0 p2 p1 p0  0  0 ].
         [  0  0 p2 p1 p0  0 ]
         [  0  0  0 p2 p1 p0 ]
```

Then the exact `16 by 12` multiplication matrix is

```
          [ T(a)   0    ]
A_f   =   [ T(b)  T(a)  ].
          [ T(c)  T(b)  ]
          [  0    T(c)  ]
```

In the same target basis, the sixteen entries of `d_f` are

```
−5a0+3b1
−4a1+3b2
−3a2
0

6c1−(7/2)b0
6c2−(5/2)b1−6a0
−(3/2)b2−(11/2)a1
−5a2

−2c0
−c1−(21/4)b0
−(19/4)b1−(3/4)a0
−(17/4)b2−(3/4)a1

0
−(9/2)c0
−4c1−(3/8)b0
−(7/2)c2−(3/8)b1.
```

These formulas are obtained by applying the accepted derivation once and
collecting its Cech powers. They retain the base derivative `alpha f_z`.
The discarded multiple of `f` from the line-bundle transition lies in
the image of `A_f` and therefore does not affect this quotient class.

The matrix `A_f` is injective throughout `U`. Indeed
`pi_*O_Z(3)` is a globally generated rank-two bundle of degree four:
its defining exact sequence is

    0 -> O(-2)² -> O⁴ -> pi_*O_Z(3) -> 0.

Its two splitting degrees are nonnegative and sum to four. After
base twist by `O(-5)` neither summand has a section. Consequently
`H0(Z,O_Z(-5,3))=0`, and the divisor sequence gives injectivity of
`H1(O(-7,1)) -> H1(O(-5,3))` even without smoothness.

Thus the single universal compatibility scheme is

    K={ [f] in U : rank[A_f | d_f]=12 },

with scheme structure defined by the `13 by 13` minors of that one
`16 by 13` matrix. Equivalently it is the incidence

    A_f h=d_f,       h in k^12.

Over `U` the vector `h` is unique whenever it exists, so the latter
incidence is the graph of the zero scheme of the rank-four quotient
obstruction. This is independent of both projective hypersurface
degrees and any later second-relation degree.

### 2. The smooth-root locus of K is nonempty

Take

    f0=(z²+4)u²+(z²−8)v².

Its first ambient obstruction vanishes. An exact preimage is

    h0=(−3z^-4−8z^-6)u+(−(1/8)z^-1−(9/2)z^-3)v.

Writing `D=Du partial_u+Dv partial_v+alpha partial_z`, a direct identity is

```
D(f0)−f0*h0
 =32z^-6 u³
  +((1/8)z−48z^-5)u²v
  +(−3/4−64z^-6)uv²
  +(1/8)z v³.
```

Every remaining Laurent power is outside `z^-4,...,z^-1`, proving
`A_f0 h0=d_f0` with the actual accepted ambient operator.

The binary coefficient polynomials `z²+4` and `z²−8` have two simple
roots each, have no common root, and are both nonzero at infinity in
the homogeneous base presentation. Thus the degree-two cover of the
base is branched at four distinct points; its `(2,2)` root divisor is
smooth and connected of genus one. This is a characteristic-zero
statement, so the displayed nonzero constants cause no exceptional
characteristic issue.

This example disproves the possible broad assertion that the actual
first ambient class is nonzero on every smooth `(2,2)` root divisor.
It supplies compatibility through the first exceptional order only.

### 3. Smooth compatibility has positive local dimension

The equations `A_f h-d_f=0` have sixteen components in nine affine
coefficient variables and twelve correction variables. At `(f0,h0)`
their Jacobian has rank sixteen. In the variable order

    a0,a1,a2,b0,b1,b2,c0,c1,c2,h0,...,h11,

where the twelve `h` coordinates follow the source basis in Section 1,
the minor on zero-based columns

    0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16

has determinant exactly `−405`. The companion standard-library Python
script records the full rational Jacobian and verifies this determinant
by exact rational elimination.

The affine incidence is therefore smooth of dimension `21−16=5` at
this point. Since the correction vector is unique and scaling the
nonzero equation `f` gives a free scalar direction, the projective
compatibility scheme `K` is smooth of dimension four at `[f0]`. Being
a smooth root divisor is an open condition. Hence `K` contains a
nonempty four-dimensional local family of smooth root divisors. This
is stronger than an isolated compatibility sample; it does not assert
that ruling-difference torsion holds throughout that local family.

### 4. The explicit zero also passes the spectral torsion condition

On `Z0=(f0=0)`, put

    A=O_Z0(1,0),    B=O_Z0(0,1),    eta=B tensor A^-1.

Then `eta` has exact order two. One elementary divisor proof uses
`c(z)=z²−8`, considered as a section of `A²`. At a zero of `u` on
`Z0`, both `a(z)` and `v` are units, and the equation

    c(z)v²=−a(z)u²

shows that the zero divisor of `c(z)` is twice the zero divisor of
`u`. There are no other zeros. Consequently `A²≅B²`.
If `A≅B`, their two complete degree-two systems would differ by an
automorphism of `P1`, forcing the image in `P1 x P1` to be a graph.
Its actual smooth `(2,2)` image excludes this. Thus `eta` is nontrivial
and has order two.

The accepted spectral criterion consequently permits a coprime second
quotient relation in every even degree `s>2`. In particular it permits
`s=8` and `s=12`, the two second degrees appearing in the accepted
scalar numerical boundary. The second relation remains a quotient
relation with its nonsplit extension; no global second polynomial
line has been constructed.

Thus the actual first ambient compatibility and the exact spectral
torsion descent condition coexist. Their conjunction alone does not
exclude this geometry. Higher actual ambient obstruction classes,
and eventual realization by projective equations with the required
support, remain unresolved.

### 5. Reproducible evidence and scope

The exact matrix, Cech bases, explicit preimage, and Jacobian certificate
are recorded in

- [the standard-library verifier](../computations/generalization_quadratic_root_curve_universal_incidence.py),
- [its exact JSON output](../computations/generalization_quadratic_root_curve_universal_incidence.json).

Run with `python3 research/computations/generalization_quadratic_root_curve_universal_incidence.py`.
No SymPy, parameter sampling, Groebner basis, or generic-rank inference is
used. The matrix identity and one nonzero Jacobian determinant are exact
certificates. The spectral theorem/audit and accepted chart operator were
used as premises; they were not re-audited.

The newly proposed actual-CI-to-root-curve bridge is separate. Once that
bridge passes independent review, `K` is a necessary incidence for its
stated lane. The bridge's hypotheses do not hold by assumption for
every complete intersection. The universal STCI problem and
unrestricted `C0` remain open.



## Consolidated historical supplement: `research/supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md`

# quadratic root second zero and dual compression

Permanent mathematical dossier preserving complete arguments, assumptions, characteristic boundaries, counterexamples and unresolved claims.

---

<a id="2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry"></a>

## Torsion divisors and the second zero locus on quadratic root compatibility

Date: 2026-10-15. Author: `geometric_locus`.

Status: **NEW STRUCTURAL PROOFS; independent review passed.** The
accepted universal first incidence, its smooth seed and differential,
and the accepted canonical second obstruction and its nonzero seed value
are premises. None of those computations is rerun. This note proves a
Picard-theoretic description of the torsion loci and a dimension bound
on one specified torsion branch of the second zero locus. No additional
seed or coefficient profile is computed.

### 1. Setup and scope

Let `U_sm` be the open subset of `P8` parametrizing smooth divisors

    Z_f=(f=0) in P1 x P1,
    f=a(z)u^2+b(z)uv+c(z)v^2,

of type `(2,2)`. Write

    A=O_Z(1,0), B=O_Z(0,1), eta=B tensor A^-1.

Both `A` and `B` have degree two, and `eta` is nontrivial. Indeed if
the two line bundles were isomorphic, their complete degree-two linear
systems would identify the two projections up to a projective
automorphism, forcing the image to be a graph.

Let `C` be the reduced irreducible component of the accepted first
compatibility scheme `K` through

    f0=(z^2+4)u^2+(z^2-8)v^2.

The accepted results give: `C` is smooth of dimension four at `[f0]`;
the second obstruction is a canonical section `sigma2` of the rank
sixteen bundle `Q2(1)` on `K`; and `sigma2(f0)!=0`. Put

    Y=Z(sigma2) intersect C.

In particular `Y` is a proper closed subscheme of `C`, with support
of dimension at most three. The question here is what torsion adds.
Any application to the first-principal-ideal CI lane keeps the accepted
restriction `s>4` and the hypotheses of the actual-CI-to-root-curve bridge.

### 2. The ruling involutions encode the Picard torsion exactly

Let `i_A` and `i_B` be the deck involutions of the two degree-two
projections of the elliptic curve `Z`. Choose an origin temporarily and
identify degree-two divisor classes with their sums in the elliptic
group law. If the sums for `A,B` are `a_A,a_B`, then

    i_A(p)=a_A-p, i_B(p)=a_B-p.

It follows that

    tau=i_B i_A: p -> p+(a_B-a_A)=p+eta.

This identity is independent of the temporary origin. Consequently

    eta has exact order n  <=>  tau has exact order n.

Thus the spectral torsion requirement is a finite-order condition on a
canonical automorphism of the root curve. It is not an assertion that
an ambient coordinate involution exists for every torsion order.

For fixed `n>=2`, define

    T[n]={f in U_sm : eta^n=O_Z}.

These are algebraic relative-Picard zero loci. In characteristic zero
they are smooth divisors of `U_sm`, of dimension seven; exact-order
strata are unions of components of these divisors. Here is a local
moduli proof of this assertion.

After an etale choice of an origin with `A=O_Z(2O)` and, if desired,
level structure to remove finite automorphisms, a smooth `(2,2)`
embedding is specified by an elliptic curve, a nonzero point `eta` of
its degree-zero Picard curve, and frames of the two degree-two linear
systems. Conversely, two distinct degree-two systems embed an elliptic
curve into `P1 x P1`: if two points have the same images, they are
interchanged by both deck involutions, forcing `A=B`; simultaneous
ramification would likewise force `A=B`. The frames give the six
projective-coordinate parameters. The local moduli parameters are
therefore the elliptic modulus and the one-dimensional Picard parameter
`eta`, together with those six coordinate parameters.

Multiplication by `n` on a relative elliptic Picard curve is finite
etale in characteristic zero: its tangent map is multiplication by
the invertible integer `n`. Its torsion subgroup is finite etale over
the elliptic-modulus base. Thus the fixed torsion condition removes
exactly the Picard parameter and is smooth of codimension one. This
also shows that exact torsion order is locally constant inside `T[n]`.

This ambient divisor statement gives no automatic transversality to
`K` or to the second zero scheme. For an irreducible four-dimensional
compatibility component, a fixed torsion divisor either contains the
component or cuts a divisor (possibly empty). Further dimension drops
need further evidence.

### 3. Exact order two is a coefficient determinant

Write

    a=a0+a1 z+a2 z^2, b=b0+b1 z+b2 z^2,
    c=c0+c1 z+c2 z^2,

and form the coefficient matrix

              [ a0 a1 a2 ]
    M(f) =    [ b0 b1 b2 ].
              [ c0 c1 c2 ]

On `U_sm` one has the exact equivalence

    eta has order two  <=>  det M(f)=0.                 (1)

For the forward implication, the deck involution `i_A` acts on
`Pic^2(Z)` by

    i_A^*L=A^2 tensor L^-1.

When `eta^2=O`, it therefore preserves `B`. Its action on `H0(B)`
induces a projective involution on the second `P1`. This involution
is nontrivial: if it were trivial then `i_A` would also be the deck
involution of the second projection, forcing `A=B`. Diagonalize it
in characteristic zero. The root equation is then an eigenvector for
`[u:v] -> [-u:v]`. The odd eigenspace of binary quadratics is the
one-dimensional span of `uv`, which would give a reducible singular
divisor. Therefore the equation lies in the even eigenspace spanned
by `u^2,v^2`, so the coefficient matrix has rank at most two.

Conversely, basepoint freeness excludes rank at most one: then `f`
would have a common homogeneous quadratic factor in the base
coefficients, with a base zero. At rank two, the binary fiber
quadratics of `f` lie in a two-dimensional pencil. If the annihilator
of this pencil is a degenerate binary quadratic, the pencil has a
common direction root, so `f` has a fixed linear direction factor.
The remaining factor meets that fixed section in degree two, contrary
to smoothness. The annihilator is consequently nondegenerate. A
constant change of direction coordinates takes this pencil to the
span of `u^2,v^2`. Thus `f` becomes diagonal. On a smooth diagonal
curve, the defining equation gives `A^2=B^2`: the zero divisor of a
coefficient section of `A^2` is twice the zero divisor of a direction
section of `B`. Since `A!=B`, the order is exactly two. This proves (1).

Thus `T[2]` is the cubic determinantal hypersurface `det M=0` on the
smooth root open. It is smooth there because all of its matrices have
rank exactly two. This provides a concrete equation for the relevant
Picard divisor, independently of any second-obstruction computation.

### 4. The first compatibility component meets this divisor transversely

At the accepted seed,

    M(f0)=[ [4,0,1], [0,0,0], [-8,0,1] ].

Therefore

    d(det M)_(f0)=12 delta b1.                        (2)

Use the already accepted quotient differential of the first obstruction,
in coefficient order `(a0,a1,a2,b0,b1,b2,c0,c1,c2)`:

```
     [  0    2   0   1/4  0   2    0   -2    0  ]
     [  1    0   8    0   4   0   -1    0  -20  ]
R =  [ -5/2  0   4    0   2   0  -1/2   0    2  ].
     [  0    8   0    1   0  -4    0    4    0  ]
```

The coefficient variation

    delta f=zuv+4v^2

has `delta b1=1`, `delta c0=4`, with all other coefficients zero.
It lies in `ker R`, since its four image entries are

    0, 4-4, 2-2, 0.

It is a genuine projective tangent direction, not the scalar direction
of `f0`. Since the accepted first incidence is smooth here, it is a
tangent direction of `C`. Equation (2) evaluates to `12`, not zero.
Thus `C` and `T[2]` meet transversely at `[f0]`.

It follows that their intersection is smooth of dimension three in a
neighborhood of `[f0]`. Let `D` denote the reduced irreducible component
of `C intersect T[2]` through that point; this component is unique at
the seed and has dimension three.

### 5. A proved bound on the torsion-two part of the second zero locus

The accepted scalar pairing for the canonical second section gives
`sigma2(f0)!=0`. Therefore `sigma2|D` is not identically zero. Its zero
scheme is a proper closed subscheme of the irreducible three-dimensional
variety `D`. Consequently

    dim support(Y intersect D) <= 2.                  (3)

Equivalently, a nonempty open subset of this three-dimensional
torsion-two branch fails the second ambient lifting step. Bound (3)
uses a proved torsion equation, a proved tangent direction, and a
known nonzero section value; it is not an expected-dimension argument
from the rank sixteen target.

For every fixed even `n`, the local germ of `T[n]` at the seed equals
the germ of `T[2]`. Indeed the `n`-torsion subgroup of the relative
Picard curve is finite etale, and the order-two component through the
seed is open and closed in it. Equivalently, after writing `n=2m`,
the zero component of `[m]` can be isolated etale-locally near
`[2]eta=0`. Thus the same bound applies to the local torsion branch
through the seed for the fixed spectral degrees `8` and `12`.

Other components of `C intersect T[2]`, exact torsion orders greater
than two, and other components of `Y` are not controlled by (3).
In particular this does not prove that `Y` is empty, nor that its
entire intersection with any fixed torsion divisor has dimension at
most two. A different torsion component could be contained in `Y`.

For unbounded second-relation degree, the union of all torsion orders
is a countable union of algebraic loci, not one fixed torsion divisor.
Noetherianity alone does not replace that union by finitely many
orders. The separate finite-type theorem for a uniquely liftable
higher-obstruction tower concerns its closed zero schemes; it does
not justify such a replacement of torsion loci or an algebraization
to projective equations.

Independent review is recorded in
[the structural torsion audit](#consolidated-historical-supplement-researchsupplementsquadratic_root_second_zero_and_dual_compressionmd).

---

<a id="2026-10-15-generalization-quadratic-root-torsion-second-zero-independent-audit"></a>

## Independent review of torsion geometry on the second zero locus

Date: 2026-10-15. Reviewer: `universal_root_obstruction`.
Status: **PASS for the stated structural Picard, determinant, and
specified-component dimension claims**. The universal first incidence,
its accepted seed differential, and the actual second section's accepted
nonzero value are premises. No accepted certificate was replayed and no
new seed was evaluated.

Reviewed proof:
[torsion divisors and the second zero locus](#consolidated-historical-supplement-researchsupplementsquadratic_root_second_zero_and_dual_compressionmd).

### 1. Intrinsic torsion and its ambient divisors

For a smooth `(2,2)` curve, both ruling systems have degree two. With an
origin on its elliptic normalization, the deck involution of a divisor
class with sum `a` is `p -> a-p`. Therefore the product of the two deck
involutions is translation by the degree-zero difference `eta=B-A`.
Its exact order is exactly the order of `eta`. This statement concerns
automorphisms of the root curve; it does not lift them to the ambient
formal neighborhood.

The local-moduli argument in the proposal is valid after an etale choice
of an origin with `A=O(2O)` and suitable finite level structure. The data
are an elliptic modulus, a nonzero Picard point `eta`, and two projective
coordinate frames. The two distinct degree-two systems give an embedding:
a pair of identified points would be interchanged by both ruling deck
involutions and force their centers, hence the systems, to agree;
a simultaneous ramification point forces the same equality. Thus this
parameter description covers the smooth root open locally with its
correct eight dimensions.

For fixed `n`, multiplication by `n` is etale on the relative elliptic
Picard curve in characteristic zero. Its kernel is finite etale, and
pullback along the free Picard parameter gives a smooth codimension-one
torsion condition. No transversality to the first compatibility scheme
follows from this ambient statement alone. Distinct exact-order strata
are open and closed within the fixed `n`-torsion condition, explaining
the stated equality of local germs at the order-two seed for each fixed
even `n`.

### 2. The cubic determinant is exactly the order-two locus

The equivalence `eta^2=1 <=> det M=0` is correct on the smooth root open.
If `eta^2=1`, the first ruling deck involution preserves the second
line bundle. It induces a nontrivial projective involution on the second
ruling: a trivial induced involution would fix both coordinates of the
embedded curve and hence the curve itself pointwise. A constant direction
coordinate change diagonalizes this involution. The odd quadratic
eigenspace consists only of multiples of `uv`, which cannot cut a smooth
`(2,2)` divisor. The root equation is therefore even, so its coefficient
matrix has rank at most two.

Conversely, rank one is excluded by basepoint freeness: all coefficient
quadratics would be proportional and have a common homogeneous base
zero. Rank two puts the fiber quadratics in a pencil. A degenerate
annihilator of that pencil is evaluation at a direction point, so it
means a common direction root. The corresponding fixed direction section
meets the remaining `(2,1)` component in degree two, contradicting
smoothness. A nondegenerate annihilator can be taken by a constant
projective direction change to the annihilator of `span(u^2,v^2)`.
The diagonal equation then gives `A^2=B^2` by its zero divisors.
The two line bundles are unequal for an embedded smooth `(2,2)` root,
so the order is exactly two.

All determinant-zero matrices on this open have rank exactly two.
The determinant hypersurface is smooth at every rank-two matrix, so
the proposal's global smooth-divisor statement on this open is justified.

### 3. The dimension drop is proved on the named component

At the accepted seed, the determinant differential is `12 delta b1`.
The variation `delta b1=1, delta c0=4` is killed by the accepted first
quotient differential: the only potentially nonzero rows are `4-4`
and `2-2`. It is not scalar variation of the seed. The determinant
functional takes value twelve on it. Thus the smooth four-dimensional
first compatibility component is transverse to the order-two divisor
at this seed. Their intersection has one smooth three-dimensional local
component there, whose reduced global irreducible component is the
specified `D`.

The actual second section is already known to be nonzero at the same
point. Its restriction to `D` is therefore not identically zero. The
support of its zero scheme is a proper closed subset of the irreducible
three-dimensional variety `D`, and hence has dimension at most two.
This is an actual dimension bound, not a dimension expectation from a
rank-sixteen vector bundle.

This argument does not control other components of the torsion
intersection or exact orders greater than two. It applies to the local
branch through the seed for fixed even spectral degrees, including eight
and twelve. It does not bound the entire torsion union, prove emptiness
of the second zero locus, or supply an actual CI. The proposal preserves
all those boundaries, as well as `s>4` in its stated CI application.

---

<a id="2026-10-15-generalization-quadratic-root-global-second-dual-compression"></a>

## A chart-free complete 25-pairing test for the universal second obstruction

Date: 2026-10-15. Author: `universal_root_obstruction`.
Status: **NEW GLOBAL REDUCTION; independent review passed.** Accepted
first/second ambient class constructions, the exact embedded chart, and
their earlier seed certificates are premises. None is rerun. This note
compresses the entire second obstruction into one polynomial family with
no coefficient chart, then exports a single bounded-elimination input.
It does not yet assert that the second zero scheme is empty.

### 1. The global dual presentation removes 39 unit variables

Let `f=a(z)u²+b(z)uv+c(z)v²` have base degree two. Throughout this
section assume only that its three homogeneous base coefficients have
no common zero; the root divisor can be singular or nonreduced. The
transpose of multiplication by `f` in the direction ruling is

```
        [ a b c 0 0 ]
T_f  =  [ 0 a b c 0 ] : O_P1^5 -> O_P1(2)^3.
        [ 0 0 a b c ]
```

It is surjective on every base fiber: its transpose is multiplication
by a nonzero binary quadratic from degree two to degree four, which is
injective. Thus `W=ker T_f` is a rank-two vector bundle with
`det W=O(-6)`.

The complete Serre-dual space of the actual second obstruction consists
of polynomial vectors `q=(q0,...,q4)`, of degree at most ten, such that

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.                                 (1)

It is exactly `H0(P1,W(10))`, of dimension sixteen. This is the dual of
`coker[H1 O(-14,2) --f--> H1 O(-12,4)]`; no first-order normal-symbol
replacement is made.

Dualizing the exact sequence defining `W`, and using the canonical
rank-two identification `W*=W tensor(det W)^-1`, gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.                 (2)

After twisting by `O(4)`, the left term is `O(2)^3` and has no `H1`.
Consequently

    H0(O(4))^5 -> H0(W(10)) -> 0                     (3)

is surjective. Its source dimension is twenty-five and its kernel
dimension is nine. Thus twenty-five scalar pairings give a complete
test for all sixteen actual obstruction coordinates. This works on
the entire basepoint-free family, including every splitting-jump locus.
It makes no choice of an invertible coefficient or matrix minor.

For an explicit polynomial version, form a skew `5 by 5` matrix `P_f`.
With zero-based indices `0,...,4`, put for `i<j`

    (P_f)_ij=(-1)^(i+j+1) det(T_f with columns i,j deleted),
    (P_f)_ji=-(P_f)_ij,    (P_f)_ii=0.                (4)

Then `T_f P_f=0`. Its five columns are the five generating sections of
`W(6)` in (2), written as signed complementary maximal minors. Each
entry has degree at most six in the affine base coordinate and is cubic
in the coefficients of `f`.

Let `R4` be any Cech representative of the actual second class, with
quartic direction components `r0,...,r4` and Laurent powers retained in
`z^-11,...,z^-1`. The second obstruction vanishes if and only if

    coefficient_z^-1 [ z^j sum_i (P_f)_i,l r_i ]=0
                for l=0,...,4 and j=0,...,4.          (5)

The criterion is scheme-theoretic. Indeed the family version of (3) is
a surjection of vector bundles; the twenty-five pairings generate the
same zero ideal as the rank-sixteen second section. It follows that
(5) does not lose exceptional coefficient strata or retain only generic
rank information.

For projective coefficient space `U`, the universal matrix is
`O^5 -> O(2) tensor O_U(1)^3`. Thus
`det W=O(-6) tensor O_U(-3)`, and the globally correct version of (2)
is

    0 -> O(-2) tensor O_U(-1)^3
      -> O^5
      -> W(6) tensor O_U(3) -> 0.

After the same base twist by four and pushforward, (3) becomes an
everywhere-surjective bundle map from `O_U^25` onto
`p_*W(10) tensor O_U(3)`. The dual of the actual second obstruction
bundle is `p_*W(10) tensor O_U(-1)`. Twisting the displayed surjection
by `O_U(-4)` therefore gives a surjection from `O_U(-4)^25` onto that
dual. This verifies the scheme-theoretic claim and the homogeneous
coefficient degree four of the scalar pairings. On the affine coefficient
cone the representatives are exactly (4); the cubic coefficient degree
of the Plucker vectors is a twist, not a denominator.

### 2. A single actual-chart model supplies R4 universally

The accepted full embedded transition is used as input:

```
den=z⁴+u+(3/2)zv, w=(z³+v)/den,
a'=z/den−w³, b'=1/den−w⁴,
u'=a'/2, v'=−3w a'+2b'.
```

Write `f1` for the second-chart root equation obtained by reversing each
quadratic coefficient polynomial:

    f1=(a2+a1w+a0w²)u'²
       +(b2+b1w+b0w²)u'v'
       +(c2+c1w+c0w²)v'².

Expand only through normal degree four. Let

    beta=-2z^-4u-z^-3v,
    h=sum_(k=-6)^(-1) (h_(u,k)u+h_(v,k)v)z^k,
    L1=h+beta,
    S3=[z^16 f1]_3-L1*f.                             (6)

Its sixteen middle Laurent coefficients, on `z^-4,...,z^-1` times
binary cubics, are the universal first equations. They are equivalent
to the accepted `A_f h=d_f`. No new first-incidence rank claim is needed.

Define the local cubic corrections by their regular Cech parts:

    G0 = the z>=0 part of S3,
    z^-5 G1(z^-1;u,v) = - the z<=-5 part of S3.       (7)

All coefficients of `G0` have degree at most one in `z`, and those of
`G1` have degree at most one in `w`; these bounds follow from the finite
supports in (6), with no coefficient open imposed. On the first zero
scheme, (7) gives the exact cubic patch identity

    [z^16(f1+G1)]_3-G0-L1*f=0.

The universal representative used in (5) is

    R4=pr_(z^-11,...,z^-1)
         ( [z^16(f1+G1)]_4 - L1*G0 ).                (8)

Here `G1` is substituted using the full nonlinear coordinates `w,u',v'`.
The base derivative, the first equation unit, and its product with the
first correction are all retained. The unknown next equation unit is
a multiple of `f`; it disappears under every pairing (1). Unknown
quartic local corrections are Cech coboundaries. Therefore no thirty-nine
quartic unit variables are required in the final system.

The model has the nine coefficient variables of `f` and twelve variables
of `h`. Its sixteen first equations are bilinear. Its twenty-five second
equations have total degree at most six, homogeneous degree four in the
coefficients of `f` and degree at most two in `h`. There is one affine
model for the full coefficient cone. Scale of `f` is harmless on the
smooth open and need not be normalized by a coefficient chart.

### 3. The smooth open is one homogeneous binary-quartic discriminant

Put

    Delta(z)=b(z)^2-4a(z)c(z)=d0+d1z+d2z²+d3z³+d4z⁴,

regarded throughout as the binary quartic
`d0 Y⁴+d1 XY³+d2 X²Y²+d3 X³Y+d4 X⁴`.
Define

    I=12d4d0-3d3d1+d2²,
    J=72d4d2d0+9d3d2d1-27d4d1²-27d3²d0-2d2³,
    Disc=(4I³-J²)/27.                                (9)

In characteristic zero this is the homogeneous binary-quartic
discriminant. It is homogeneous of degree twelve in the nine coefficients
of `f`.

The condition `Disc!=0` is exactly the smooth-root condition. A common
base zero of `a,b,c` gives a common homogeneous linear factor and forces
its square to divide `Delta`, so it makes `Disc=0`. Thus the open already
implies basepoint freeness. On that open the double-cover discriminant
is the branch divisor; it has four simple roots exactly when the root
curve is smooth. Conversely every smooth `(2,2)` root gives a finite
separable degree-two map with four simple branch points, so its binary
discriminant is nonzero.

No leading affine coefficient is inverted. In particular `d4=0` with
`d3!=0` represents a simple branch point at infinity and is allowed by
(9). A second zero at infinity gives vanishing discriminant, as required.
The formula does not silently discard degree-drop cases.

The single global smooth-family ideal is therefore generated by the
sixteen equations from (6), the twenty-five pairings (5), and

    smoothInverse*Disc-1.                             (10)

It is the full smooth `K2` incidence, not a finite set of samples or a
union missing coefficient charts. Proving it is the unit ideal would
prove `K2` empty on the entire smooth `(2,2)` family. Failure to finish
an elimination proves nothing about emptiness.

### 4. Exact export and one bounded prospect

The new standard-library sparse generator is
[global second-model generator](../computations/generalization_quadratic_root_global_second_model.py).
It exports
[one characteristic-zero M2 model](https://github.com/markluxton1/STCI/blob/88f2e4f6a418cad6f584a1ce2445787caf653f3a/research/computations/generalization_quadratic_root_global_second_model.m2)
and [its term/count metadata](../computations/generalization_quadratic_root_global_second_model.json).
The new algebraic consistency check verifies `T_f P_f=0` identically;
no accepted seed or previous rank verifier is invoked.

The exported system has twenty-two variables including `smoothInverse`,
sixteen first equations, twenty-five complete dual second equations, and
one discriminant inverse equation. The second equations have at most
535 terms each; the homogeneous discriminant has 1010 terms. These counts
are exact export metadata, not complexity or solvability claims.

The new proof and the exported generator algorithm passed
[the independent compression audit](#consolidated-historical-supplement-researchsupplementsquadratic_root_second_zero_and_dual_compressionmd).
Exactly one bounded M2 launch was made, with the heavy quintic window
held separately. Its supervisor hit a sandbox `PermissionError` when
invoking `/bin/ps` for RSS monitoring. The M2 child had a 45-second CPU
limit. Its PID `32960` was subsequently confirmed absent with authorized
process inspection; the original exit code was not recoverable after the
supervisor failed. Captured stdout contains `MODEL_READY`, but no
`GB_COMPLETE` or unit-ideal marker. Thus the run supplies no elimination
result and no mathematical conclusion.

The bounded global-second launch did not produce a completed Gröbner basis or an emptiness certificate. Its supervisor failure supplies no mathematical restriction on the allowed degree.

The accepted all-orders formal nonexistence theorem proves an existential
empty stage on the smooth family. This compression does not supply a
value of that stage. In particular no `N<=5`, all-smooth second
nonvanishing, actual-CI exclusion, or unrestricted STCI conclusion is
claimed until an exact global certificate or a new geometric proof exists.

---

<a id="2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit"></a>

## Independent audit of the twenty-five global second-obstruction tests

Date: 2026-10-15. Author: `geometric_locus`.

Status: **THE GLOBAL COMPRESSION, UNIVERSAL MODEL ALGORITHM, AND
HOMOGENEOUS SMOOTHNESS CRITERION PASS INDEPENDENT REVIEW.** Accepted first and second obstruction
constructions are inputs. No accepted seed computation, verifier, or
profile calculation is repeated. This audit uses bundle duality,
Laplace identities, and a local double-cover calculation.

Companion note:
`2026-10-15-generalization-quadratic-root-global-second-dual-compression.md`.
The final companion note and
`../computations/generalization_quadratic_root_global_second_model.py`
were read after this mathematical audit was drafted. Their algorithm
was compared with the proof; no old verifier, seed test, or CAS was run.

### 1. The correct dual bundle on the whole basepoint-free locus

Fix a homogeneous basepoint-free triple `a,b,c` of degree two on `P1`.
Let `f=a u^2+b uv+c v^2` and consider

              [ a b c 0 0 ]
    T_f =     [ 0 a b c 0 ] : O^5 -> O(2)^3.
              [ 0 0 a b c ]

At every base point this is the transpose of multiplication by the
nonzero binary quadratic `f` from binary quadratics to binary quartics.
Multiplication by a nonzero polynomial is injective, so the fiber rank
is three everywhere. Therefore

    0 -> W -> O^5 -> O(2)^3 -> 0

is exact with `W` a rank-two vector bundle and `det W=O(-6)`.
Neither smoothness nor reducedness of the root divisor is needed.

The second Cech target has quartic coefficients and powers
`z^-11,...,z^-1`. Its dual consists of five polynomials of degree at
most ten. An element annihilates multiplication by `f` exactly when

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.

Thus the full sixteen-dimensional dual obstruction space is
`H0(P1,W(10))`, with the monomial-dual pairing given by the coefficient
of `z^-1` in `sum q_i r_i`. There are no binomial factors in these
formulas for the specified coefficient bases.

### 2. Rank-two duality supplies a global generating presentation

For a rank-two bundle, the exterior pairing gives a canonical
isomorphism

    W^* = W tensor (det W)^-1 = W(6).

Dualizing the exact sequence in Section 1 and using this isomorphism
gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.

Twisting by `O(4)` gives

    0 -> O(2)^3 -> O(4)^5 -> W(10) -> 0.              (1)

Since `H1(P1,O(2))=0`, global sections of (1) are surjective onto
`H0(W(10))`. In particular the twenty-five sections obtained from the
five displayed generators and the five degree-four base monomials
span the entire dual obstruction space. The kernel on global sections
has dimension nine and the target has dimension `25-9=16`.

This proves spanning uniformly; no splitting choice, minor
localization, or denominator is used. It therefore includes splitting
jumps, repeated direction factors, singular roots, and nonreduced
roots, subject only to the basepoint-free hypothesis.

### 3. The signed complementary minors give those five generators

Index rows and columns of a skew five-by-five matrix `K` by
`0,...,4`. For `i<j`, put

    K_ij=(-1)^(i+j+1) det(T_f with columns i,j omitted),
    K_ji=-K_ij, K_ii=0.                              (2)

Every nonzero entry is a homogeneous degree-six base polynomial and a
homogeneous cubic in the equation coefficients. The Laplace expansion
of a four-by-four determinant with one repeated row gives `T_f K=0`.
Thus each column is a section of `W(6)`.

These are exactly the five generators in the dual presentation, up
to the harmless common sign from choosing the determinant orientation.
Indeed the complementary-minor bivector is the exterior dual of the
three rows of `T_f`; contraction identifies the quotient of `O^5`
by the transpose image with `W tensor (det W)^-1`. At a local frame
where `T_f=[I3 | 0]`, formula (2) has `K_34=1`, `K_43=-1`, and all
other entries zero. It is the required nondegenerate rank-two
alternating pairing on the kernel. Change of frames proves the
identification everywhere.

Formula (2), together with skew symmetry, is necessary: assigning
the same complementary-minor sign to both `K_ij` and `K_ji` would
generally destroy the kernel identity. An overall common sign, or
using rows in place of columns with the corresponding sign, does not
change the zero tests.

On the affine base chart, the twenty-five full dual generators are

    z^k K_column_i, 0<=i<=4, 0<=k<=4.

Homogeneously, `z^k` means the basis
`Z1^k Z0^(4-k)` of `H0(O(4))`; consequently the construction includes
base infinity.

### 4. Exact equivalence with the second class and parameter degrees

Let `R4=sum r_i(z)u^(4-i)v^i` be the actual second discrepancy after
retaining the accepted first cubic correction and equation unit.
Its second class vanishes if and only if all twenty-five scalars

    coefficient_z^-1[ z^k sum_j K_ji r_j ]

vanish. One direction follows because every displayed vector
annihilates multiplication and coboundaries. The converse follows
from the spanning theorem of Section 2 and nondegeneracy of the
finite-dimensional Cech/Serre pairing. This removes the thirty-nine
unknown quartic unit coefficients without replacing the quotient
by a smaller test space.

On projective coefficient space, each `K` entry has coefficient degree
three. Thus there is a fiberwise surjective bundle map

    25 O(-3) -> Q2^*.

Pairing with the accepted canonical section in `Q2(1)` produces
twenty-five sections of `O(4)` on the first compatibility incidence.
When that incidence is written with equation coefficients `f` and
the unique first correction coordinates `h`, these tests can be
written polynomially in `f,h` after the actual first-patch formulas
are exported. The bundle argument does not require a choice of
quartic correction variables. It does not itself compute the
universal `R4` or prove that the twenty-five equations have no smooth
solutions.

The parameter twists in the companion note agree with this statement.
Write `H=O_U(1)`. The universal map is
`O^5 -> (O(2) tensor H)^{direct sum 3}`,
so `det W=O(-6) tensor H^-3`. Rank-two duality gives
`W^*=W(6) tensor H^3`. The pushed-forward generating presentation is

    O_U^25 -> p_*W(10) tensor H^3 -> 0.

Here `Q2^*=p_*W(10)`. The actual obstruction bundle is
`V2=Q2 tensor H`, so its dual is `p_*W(10) tensor H^-1`.
Twisting the last surjection by `H^-4` gives exactly the companion
note's `25 H^-4 -> V2^*`. This is the same as the earlier
`25 H^-3 -> Q2^*`; it introduces no extra coefficient factor or
denominator. In particular the scalar tests have coefficient degree
four, as required.

### 5. The homogeneous quartic discriminant detects smoothness

Let

    Delta=b^2-4ac in H0(P1,O(4)).

For a basepoint-free triple over an algebraically closed field of
characteristic zero, the root divisor `Z_f` is smooth if and only if
the homogeneous binary quartic `Delta` has four distinct zeros, or
equivalently its binary-quartic discriminant is nonzero.

To see this locally, first suppose `a` is a unit. The fiber point
`v=0` is absent there, and the equation in `x=u/v` becomes

    y^2=Delta, y=2a x+b.

The analogous chart works when `c` is a unit. At a zero of `Delta`,
basepoint freeness forces at least one of `a,c` to be a unit, so
these charts cover every possible ramification point. The double
cover is smooth at such a point exactly when the local vanishing
order of `Delta` is one: in the local equation `y^2-Delta(t)=0`,
the fiber derivative vanishes at `y=0`, and the base derivative is
nonzero precisely for a simple zero. Away from `Delta=0`, the cover
is etale and smooth. If only `b` is a unit and `a=c=0` at a base
point, then `Delta=b^2` is nonzero there and the two direction roots
are distinct, so no omitted singularity occurs.

This argument uses a local parameter at every point of the base,
including infinity. The quartic must remain homogeneous: dropping
its apparent affine degree and ignoring its zero at infinity would
not be a valid smoothness test. An identically zero discriminant
section gives a generically nonreduced cover and is excluded.

Conversely, a common base zero of `a,b,c` forces `Delta` to vanish
to order at least two there. Thus a nonzero binary-quartic
discriminant already implies basepoint freeness. The entire smooth
`(2,2)` open is consequently described by this one nonvanishing
condition. The discriminant has degree six in the quartic
coefficients and degree twelve in the original nine coefficients.

The companion note's raw-coefficient formulas

    I=12d4d0-3d3d1+d2^2,
    J=72d4d2d0+9d3d2d1-27d4d1^2-27d3^2d0-2d2^3,
    Disc=(4I^3-J^2)/27

use the correct binary-quartic normalization for
`d0Y^4+d1XY^3+d2X^2Y^2+d3X^3Y+d4X^4`. They do not require
`d4!=0`. In particular a simple root at infinity is retained.

### 6. The universal model algorithm matches the geometric construction

The new generator was inspected without executing it. Its coefficient
ring uses exact rational sparse polynomials; its normal monomials are
truncated only above total normal degree four. The inverse of
`z^4+u+(3/2)zv` is expanded through the fourth power of its linear
correction, which is sufficient for all retained terms. The accepted
chart substitutions for `w,u',v'` are implemented literally.

For coefficient `a_j,b_j,c_j`, the reversed second-chart base factor
is `w^(2-j)`. The generator uses this factor and normalizes by `z^16`.
Its first discrepancy is exactly

    S3=[z^16 f1]_3-(h+beta)f.

The sixteen middle coefficients give the first incidence. Its
nonnegative part is `G0`. A negative term `p z^k u^i v^j`, with
`k<=-5`, gives the second-chart correction
`-p w^(-k-5)u'^i v'^j`. Since `i+j=3`, its normalized leading pullback
is precisely `-p z^k u^i v^j`. Thus the generator's first-patch split
has the correct sign and exponent. The finite support is from `-6`
through `1`, so the two local cubic corrections have base degree at
most one, as claimed.

The quartic representative is then

    pr_-11..-1([z^16(f1+G1)]_4-(h+beta)G0),

which retains nonlinear base motion, the first equation unit, and
its product with the first correction. Unknown second units and
quartic local coboundaries are exactly the terms removed by the dual
quotient. The code forms the signed complementary minors of `T_f`
and pairs their columns after shifts `0,...,4` using coefficient
index `-1-shift-z`. This is the required residue and accounts for
all twenty-five tests.

The resulting discrepancy is linear in the coefficients of `f` and
has degree at most two in `h`. Its pairing with the cubic Plucker
vectors therefore has coefficient degree four in `f`, degree at
most two in `h`, and total degree at most six. The first equations
are linear in `f` and affine linear in `h` (equivalently a bilinear
term minus a linear term). Finally the generator appends
`smoothInverse*Disc-1`, which represents precisely the homogeneous
smooth open. No coefficient chart is omitted. This verifies the
algorithmic model underlying the proposed single global elimination;
it does not evaluate that elimination.

### 7. Scope

The twenty-five equations are a globally valid replacement of the
second quotient-membership test, not a proof of emptiness. The
accepted formal nonexistence theorem supplies an existential finite
empty stage; it does not imply that this second stage is empty.
Any effective elimination must still retain the homogeneous smooth
open and the actual first cubic patches and equation units.


### Archived exact certificate: `research/computations/generalization_quadratic_root_global_second_model.m2`

Original source preserved verbatim, including its limitations and external dependencies.

<details><summary>Historical source</summary>

```macaulay2
-- One global characteristic-zero K1+K2 incidence, no coefficient chart.
-- First/second classes are accepted inputs; this is a new dual compression.
R=QQ[a0,a1,a2,b0,b1,b2,c0,c1,c2,h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,smoothInverse,MonomialOrder=>GRevLex];
firstEquations={-5*a0+3*b1-a0*h2-a1*h1-a2*h0,-4*a1+3*b2-a0*h3-a1*h2-a2*h1,-3*a2-a0*h4-a1*h3-a2*h2,-a0*h5-a1*h4-a2*h3,-7/2*b0+6*c1-a0*h8-a1*h7-a2*h6-b0*h2-b1*h1-b2*h0,-6*a0-5/2*b1+6*c2-a0*h9-a1*h8-a2*h7-b0*h3-b1*h2-b2*h1,-11/2*a1-3/2*b2-a0*h10-a1*h9-a2*h8-b0*h4-b1*h3-b2*h2,-5*a2-a0*h11-a1*h10-a2*h9-b0*h5-b1*h4-b2*h3,-2*c0-b0*h8-b1*h7-b2*h6-c0*h2-c1*h1-c2*h0,-21/4*b0-c1-b0*h9-b1*h8-b2*h7-c0*h3-c1*h2-c2*h1,-3/4*a0-19/4*b1-b0*h10-b1*h9-b2*h8-c0*h4-c1*h3-c2*h2,-3/4*a1-17/4*b2-b0*h11-b1*h10-b2*h9-c0*h5-c1*h4-c2*h3,-c0*h8-c1*h7-c2*h6,-9/2*c0-c0*h9-c1*h8-c2*h7,-3/8*b0-4*c1-c0*h10-c1*h9-c2*h8,-3/8*b1-7/2*c2-c0*h11-c1*h10-c2*h9};
secondEquations={-9/32*a0*a0*b1*c2-9/32*a0*a0*b2*c1+43/8*a0*a0*c2*c2-9/16*a0*a1*b0*c2-9/16*a0*a1*b1*c1-9/16*a0*a1*b2*c0+83/4*a0*a1*c1*c2-9/16*a0*a2*b0*c1-9/16*a0*a2*b1*c0+37/2*a0*a2*c0*c2+37/4*a0*a2*c1*c1+27/32*a0*b0*b1*b2-151/8*a0*b0*b2*c2+9/64*a0*b1*b1*b1-157/16*a0*b1*b1*c2-37/2*a0*b1*b2*c1+65/2*a0*b1*c2*c2-139/16*a0*b2*b2*c0+50*a0*b2*c1*c2-52*a0*c2*c2*c2-9/32*a1*a1*b0*c1-9/32*a1*a1*b1*c0+10*a1*a1*c0*c2+5*a1*a1*c1*c1-9/16*a1*a2*b0*c0+71/4*a1*a2*c0*c1+27/64*a1*b0*b0*b2+27/64*a1*b0*b1*b1-77/4*a1*b0*b1*c2-145/8*a1*b0*b2*c1+127/4*a1*b0*c2*c2-151/16*a1*b1*b1*c1-71/4*a1*b1*b2*c0+99/2*a1*b1*c1*c2+34*a1*b2*c0*c2+69/4*a1*b2*c1*c1-114*a1*c1*c2*c2+31/8*a2*a2*c0*c0+27/64*a2*b0*b0*b1-139/16*a2*b0*b0*c2-17*a2*b0*b1*c1-127/8*a2*b0*b2*c0+91/2*a2*b0*c1*c2-133/16*a2*b1*b1*c0+31*a2*b1*c0*c2+63/4*a2*b1*c1*c1+16*a2*b2*c0*c1-139/2*a2*c0*c2*c2-75*a2*c1*c1*c2+195/16*b0*b0*b2*b2+51/2*b0*b1*b1*b2-457/8*b0*b1*b2*c2-241/16*b0*b2*b2*c1+383/8*b0*b2*c2*c2+71/32*b1*b1*b1*b1-155/16*b1*b1*b1*c2-249/16*b1*b1*b2*c1+87/4*b1*b1*c2*c2-21/16*b1*b2*b2*c0+54*b1*b2*c1*c2-55/2*b1*c2*c2*c2+5*b2*b2*c0*c2+21/4*b2*b2*c1*c1-147/2*b2*c1*c2*c2+26*c2*c2*c2*c2+3/4*a0*a2*c0*c0*h11+3/2*a0*a2*c0*c1*h10+3/2*a0*a2*c0*c2*h9+3/4*a0*a2*c1*c1*h9+3/2*a0*a2*c1*c2*h8-3/4*a0*b0*b2*c0*h11-3/4*a0*b0*b2*c1*h10-3/4*a0*b0*b2*c2*h9+4*a0*b0*c1*c2*h11+2*a0*b0*c2*c2*h10-3/4*a0*b1*b2*c0*h10-3/4*a0*b1*b2*c1*h9-3/4*a0*b1*b2*c2*h8+a0*b1*c1*c1*h11+2*a0*b1*c1*c2*h10-3/4*a0*b2*b2*c0*h9-3/4*a0*b2*b2*c1*h8+3/8*a0*b2*c0*c0*h5+3/4*a0*b2*c0*c1*h4+3/4*a0*b2*c0*c2*h3+3/8*a0*b2*c1*c1*h3-a0*b2*c1*c1*h10+3/4*a0*b2*c1*c2*h2-3/4*a0*b2*c2*c2*h1-4*a0*c0*c1*c2*h5-2*a0*c0*c2*c2*h4-4*a0*c0*c2*c2*h11-a0*c1*c1*c1*h5-a0*c1*c1*c2*h4-6*a0*c1*c1*c2*h11-4*a0*c1*c2*c2*h10+3/4*a1*a2*c0*c0*h10+3/2*a1*a2*c0*c1*h9+3/2*a1*a2*c0*c2*h8+3/4*a1*a2*c1*c1*h8+3/2*a1*a2*c1*c2*h7-3/4*a1*b0*b2*c0*h10-3/4*a1*b0*b2*c1*h9-3/4*a1*b0*b2*c2*h8+a1*b0*c1*c1*h11+2*a1*b0*c1*c2*h10-3/4*a1*b1*b2*c0*h9-3/4*a1*b1*b2*c1*h8-3/4*a1*b1*b2*c2*h7-2*a1*b1*c0*c1*h11+2*a1*b1*c0*c2*h10-3/4*a1*b2*b2*c0*h8-3/4*a1*b2*b2*c1*h7+3/8*a1*b2*c0*c0*h4-2*a1*b2*c0*c0*h11+3/4*a1*b2*c0*c1*h3-2*a1*b2*c0*c1*h10+3/4*a1*b2*c0*c2*h2+3/8*a1*b2*c1*c1*h2+3/4*a1*b2*c1*c2*h1-3/4*a1*b2*c2*c2*h0+2*a1*c0*c0*c2*h5+a1*c0*c1*c1*h5-2*a1*c0*c1*c2*h4+4*a1*c0*c1*c2*h11-4*a1*c0*c2*c2*h10-2*a1*c1*c1*c2*h10+3/4*a2*a2*c0*c0*h9+3/2*a2*a2*c0*c1*h8+3/2*a2*a2*c0*c2*h7+3/4*a2*a2*c1*c1*h7+3/2*a2*a2*c1*c2*h6-3/4*a2*b0*b0*c0*h11-3/4*a2*b0*b0*c1*h10-3/4*a2*b0*b0*c2*h9-3/2*a2*b0*b1*c0*h10-3/2*a2*b0*b1*c1*h9-3/2*a2*b0*b1*c2*h8-9/4*a2*b0*b2*c0*h9-9/4*a2*b0*b2*c1*h8-3/2*a2*b0*b2*c2*h7+3/4*a2*b0*c0*c0*h5+3/2*a2*b0*c0*c1*h4+3/2*a2*b0*c0*c2*h3+3/4*a2*b0*c1*c1*h3-a2*b0*c1*c1*h10+3/2*a2*b0*c1*c2*h2-3/4*a2*b1*b1*c0*h9-3/4*a2*b1*b1*c1*h8-3/4*a2*b1*b1*c2*h7-9/4*a2*b1*b2*c0*h8-9/4*a2*b1*b2*c1*h7-3/2*a2*b1*b2*c2*h6+3/4*a2*b1*c0*c0*h4-2*a2*b1*c0*c0*h11+3/2*a2*b1*c0*c1*h3-2*a2*b1*c0*c1*h10+3/2*a2*b1*c0*c2*h2+3/4*a2*b1*c1*c1*h2+3/2*a2*b1*c1*c2*h1-3/2*a2*b2*b2*c0*h7-3/2*a2*b2*b2*c1*h6+9/8*a2*b2*c0*c0*h3-2*a2*b2*c0*c0*h10+9/4*a2*b2*c0*c1*h2+3*a2*b2*c0*c2*h1+9/8*a2*b2*c1*c1*h1+3*a2*b2*c1*c2*h0+2*a2*c0*c0*c1*h5+2*a2*c0*c0*c2*h4+4*a2*c0*c0*c2*h11+3*a2*c0*c1*c1*h4+2*a2*c0*c1*c1*h11+8*a2*c0*c1*c2*h10+2*a2*c1*c1*c1*h10+3/8*b0*b0*b0*b2*h11+9/8*b0*b0*b1*b2*h10-2*b0*b0*b1*c2*h11+9/8*b0*b0*b2*b2*h9-3/8*b0*b0*b2*c0*h5-3/8*b0*b0*b2*c1*h4-2*b0*b0*b2*c1*h11-3/8*b0*b0*b2*c2*h3-2*b0*b0*b2*c2*h10+2*b0*b0*c1*c2*h5+b0*b0*c2*c2*h4+2*b0*b0*c2*c2*h11+9/8*b0*b1*b1*b2*h9-b0*b1*b1*c1*h11-3*b0*b1*b1*c2*h10+9/4*b0*b1*b2*b2*h8-3/4*b0*b1*b2*c0*h4+4*b0*b1*b2*c0*h11-3/4*b0*b1*b2*c1*h3+2*b0*b1*b2*c1*h10-3/4*b0*b1*b2*c2*h2+b0*b1*c1*c1*h5+2*b0*b1*c1*c2*h4+4*b0*b1*c1*c2*h11+4*b0*b1*c2*c2*h10+3/4*b0*b2*b2*b2*h7-3/4*b0*b2*b2*c0*h3+2*b0*b2*b2*c0*h10-3/4*b0*b2*b2*c1*h2-b0*b2*c1*c1*h4+2*b0*b2*c1*c1*h11-4*b0*c0*c2*c2*h5-6*b0*c1*c1*c2*h5-4*b0*c1*c2*c2*h4+3/8*b1*b1*b1*b2*h8+b1*b1*b1*c0*h11+9/8*b1*b1*b2*b2*h7-3/8*b1*b1*b2*c0*h3+b1*b1*b2*c0*h10-3/8*b1*b1*b2*c1*h2-3/8*b1*b1*b2*c2*h1-b1*b1*c0*c1*h5+b1*b1*c0*c2*h4-2*b1*b1*c0*c2*h11+2*b1*b1*c1*c2*h10+3/4*b1*b2*b2*b2*h6-3/4*b1*b2*b2*c0*h2-3/4*b1*b2*b2*c1*h1-2*b1*b2*c0*c0*h5-2*b1*b2*c0*c1*h4-4*b1*b2*c0*c1*h11-2*b1*b2*c1*c1*h10+4*b1*c0*c1*c2*h5-4*b1*c0*c2*c2*h4-2*b1*c1*c1*c2*h4-3/4*b2*b2*b2*c0*h1-3/4*b2*b2*b2*c1*h0-b2*b2*c0*c0*h4-2*b2*b2*c0*c0*h11-4*b2*b2*c0*c1*h10+4*b2*c0*c0*c2*h5+2*b2*c0*c1*c1*h5+8*b2*c0*c1*c2*h4+2*b2*c1*c1*c1*h4-2*a0*b0*c0*c1*h11*h11-4*a0*b0*c0*c2*h10*h11-2*a0*b0*c1*c1*h10*h11-4*a0*b0*c1*c2*h9*h11-2*a0*b0*c1*c2*h10*h10-2*a0*b0*c2*c2*h8*h11-2*a0*b0*c2*c2*h9*h10+a0*b1*c0*c0*h11*h11-2*a0*b1*c0*c2*h10*h10-a0*b1*c1*c1*h9*h11-2*a0*b1*c1*c2*h8*h11-2*a0*b1*c1*c2*h9*h10-a0*b1*c2*c2*h7*h11-2*a0*b1*c2*c2*h8*h10+2*a0*b2*c0*c0*h10*h11+2*a0*b2*c0*c1*h10*h10-a0*b2*c1*c1*h8*h11+a0*b2*c1*c1*h9*h10-2*a0*b2*c1*c2*h7*h11-a0*b2*c2*c2*h6*h11-a0*b2*c2*c2*h7*h10+2*a0*c0*c0*c1*h5*h11+2*a0*c0*c0*c2*h4*h11+2*a0*c0*c0*c2*h5*h10+2*a0*c0*c1*c1*h4*h11+2*a0*c0*c1*c1*h5*h10+4*a0*c0*c1*c2*h3*h11+4*a0*c0*c1*c2*h4*h10+4*a0*c0*c1*c2*h5*h9+2*a0*c0*c2*c2*h2*h11+2*a0*c0*c2*c2*h3*h10+2*a0*c0*c2*c2*h4*h9+2*a0*c0*c2*c2*h5*h8+a0*c1*c1*c1*h3*h11+a0*c1*c1*c1*h5*h9+3*a0*c1*c1*c2*h2*h11+a0*c1*c1*c2*h3*h10+a0*c1*c1*c2*h4*h9+3*a0*c1*c1*c2*h5*h8+3*a0*c1*c2*c2*h1*h11+2*a0*c1*c2*c2*h2*h10+2*a0*c1*c2*c2*h4*h8+3*a0*c1*c2*c2*h5*h7+a0*c2*c2*c2*h0*h11+a0*c2*c2*c2*h1*h10+a0*c2*c2*c2*h4*h7+a0*c2*c2*c2*h5*h6+a1*b0*c0*c0*h11*h11-2*a1*b0*c0*c2*h10*h10-a1*b0*c1*c1*h9*h11-2*a1*b0*c1*c2*h8*h11-2*a1*b0*c1*c2*h9*h10-a1*b0*c2*c2*h7*h11-2*a1*b0*c2*c2*h8*h10+2*a1*b1*c0*c0*h10*h11+2*a1*b1*c0*c1*h9*h11+2*a1*b1*c0*c2*h8*h11-2*a1*b1*c0*c2*h9*h10-2*a1*b1*c1*c2*h8*h10-2*a1*b1*c2*c2*h7*h10+2*a1*b2*c0*c0*h9*h11+a1*b2*c0*c0*h10*h10+2*a1*b2*c0*c1*h8*h11+2*a1*b2*c0*c1*h9*h10+2*a1*b2*c0*c2*h7*h11+a1*b2*c1*c1*h8*h10-a1*b2*c2*c2*h6*h10-2*a1*c0*c0*c0*h5*h11-2*a1*c0*c0*c1*h4*h11-2*a1*c0*c0*c1*h5*h10-2*a1*c0*c0*c2*h3*h11+2*a1*c0*c0*c2*h4*h10-2*a1*c0*c0*c2*h5*h9-a1*c0*c1*c1*h3*h11-a1*c0*c1*c1*h5*h9-2*a1*c0*c1*c2*h2*h11+2*a1*c0*c1*c2*h3*h10+2*a1*c0*c1*c2*h4*h9-2*a1*c0*c1*c2*h5*h8-a1*c0*c2*c2*h1*h11+2*a1*c0*c2*c2*h2*h10+2*a1*c0*c2*c2*h4*h8-a1*c0*c2*c2*h5*h7+a1*c1*c1*c2*h2*h10+a1*c1*c1*c2*h4*h8+2*a1*c1*c2*c2*h1*h10+2*a1*c1*c2*c2*h4*h7+a1*c2*c2*c2*h0*h10+a1*c2*c2*c2*h4*h6+2*a2*b0*c0*c0*h10*h11+2*a2*b0*c0*c1*h10*h10-a2*b0*c1*c1*h8*h11+a2*b0*c1*c1*h9*h10-2*a2*b0*c1*c2*h7*h11-a2*b0*c2*c2*h6*h11-a2*b0*c2*c2*h7*h10+2*a2*b1*c0*c0*h9*h11+a2*b1*c0*c0*h10*h10+2*a2*b1*c0*c1*h8*h11+2*a2*b1*c0*c1*h9*h10+2*a2*b1*c0*c2*h7*h11+a2*b1*c1*c1*h8*h10-a2*b1*c2*c2*h6*h10+2*a2*b2*c0*c0*h8*h11+2*a2*b2*c0*c0*h9*h10+2*a2*b2*c0*c1*h7*h11+4*a2*b2*c0*c1*h8*h10+2*a2*b2*c0*c2*h6*h11+2*a2*b2*c0*c2*h7*h10+2*a2*b2*c1*c1*h7*h10+2*a2*b2*c1*c2*h6*h10-2*a2*c0*c0*c0*h4*h11-2*a2*c0*c0*c0*h5*h10-2*a2*c0*c0*c1*h3*h11-6*a2*c0*c0*c1*h4*h10-2*a2*c0*c0*c1*h5*h9-2*a2*c0*c0*c2*h2*h11-2*a2*c0*c0*c2*h3*h10-2*a2*c0*c0*c2*h4*h9-2*a2*c0*c0*c2*h5*h8-a2*c0*c1*c1*h2*h11-3*a2*c0*c1*c1*h3*h10-3*a2*c0*c1*c1*h4*h9-a2*c0*c1*c1*h5*h8-2*a2*c0*c1*c2*h1*h11-4*a2*c0*c1*c2*h2*h10-4*a2*c0*c1*c2*h4*h8-2*a2*c0*c1*c2*h5*h7-a2*c0*c2*c2*h0*h11-a2*c0*c2*c2*h1*h10-a2*c0*c2*c2*h4*h7-a2*c0*c2*c2*h5*h6-a2*c1*c1*c1*h2*h10-a2*c1*c1*c1*h4*h8-2*a2*c1*c1*c2*h1*h10-2*a2*c1*c1*c2*h4*h7-a2*c1*c2*c2*h0*h10-a2*c1*c2*c2*h4*h6+b0*b0*b0*c1*h11*h11+2*b0*b0*b0*c2*h10*h11-b0*b0*b1*c0*h11*h11+2*b0*b0*b1*c1*h10*h11+2*b0*b0*b1*c2*h9*h11+3*b0*b0*b1*c2*h10*h10-2*b0*b0*b2*c0*h10*h11+2*b0*b0*b2*c1*h9*h11-b0*b0*b2*c1*h10*h10+2*b0*b0*b2*c2*h8*h11+2*b0*b0*b2*c2*h9*h10-2*b0*b0*c0*c1*h5*h11-2*b0*b0*c0*c2*h4*h11-2*b0*b0*c0*c2*h5*h10-b0*b0*c1*c1*h4*h11-b0*b0*c1*c1*h5*h10-2*b0*b0*c1*c2*h3*h11-2*b0*b0*c1*c2*h4*h10-2*b0*b0*c1*c2*h5*h9-b0*b0*c2*c2*h2*h11-b0*b0*c2*c2*h3*h10-b0*b0*c2*c2*h4*h9-b0*b0*c2*c2*h5*h8-2*b0*b1*b1*c0*h10*h11+b0*b1*b1*c1*h9*h11+b0*b1*b1*c2*h8*h11+3*b0*b1*b1*c2*h9*h10-4*b0*b1*b2*c0*h9*h11-2*b0*b1*b2*c0*h10*h10+2*b0*b1*b2*c1*h8*h11-2*b0*b1*b2*c1*h9*h10+2*b0*b1*b2*c2*h7*h11+4*b0*b1*b2*c2*h8*h10+2*b0*b1*c0*c0*h5*h11-4*b0*b1*c0*c2*h4*h10-b0*b1*c1*c1*h3*h11-b0*b1*c1*c1*h5*h9-2*b0*b1*c1*c2*h2*h11-2*b0*b1*c1*c2*h3*h10-2*b0*b1*c1*c2*h4*h9-2*b0*b1*c1*c2*h5*h8-b0*b1*c2*c2*h1*h11-2*b0*b1*c2*c2*h2*h10-2*b0*b1*c2*c2*h4*h8-b0*b1*c2*c2*h5*h7-2*b0*b2*b2*c0*h8*h11-2*b0*b2*b2*c0*h9*h10+b0*b2*b2*c1*h7*h11-2*b0*b2*b2*c1*h8*h10+b0*b2*b2*c2*h6*h11+b0*b2*b2*c2*h7*h10+2*b0*b2*c0*c0*h4*h11+2*b0*b2*c0*c0*h5*h10+4*b0*b2*c0*c1*h4*h10-b0*b2*c1*c1*h2*h11+b0*b2*c1*c1*h3*h10+b0*b2*c1*c1*h4*h9-b0*b2*c1*c1*h5*h8-2*b0*b2*c1*c2*h1*h11-2*b0*b2*c1*c2*h5*h7-b0*b2*c2*c2*h0*h11-b0*b2*c2*c2*h1*h10-b0*b2*c2*c2*h4*h7-b0*b2*c2*c2*h5*h6+b0*c0*c0*c1*h5*h5+2*b0*c0*c0*c2*h4*h5+2*b0*c0*c1*c1*h4*h5+4*b0*c0*c1*c2*h3*h5+2*b0*c0*c1*c2*h4*h4+2*b0*c0*c2*c2*h2*h5+2*b0*c0*c2*c2*h3*h4+b0*c1*c1*c1*h3*h5+3*b0*c1*c1*c2*h2*h5+b0*c1*c1*c2*h3*h4+3*b0*c1*c2*c2*h1*h5+2*b0*c1*c2*c2*h2*h4+b0*c2*c2*c2*h0*h5+b0*c2*c2*c2*h1*h4-b1*b1*b1*c0*h9*h11+b1*b1*b1*c2*h8*h10-3*b1*b1*b2*c0*h8*h11-b1*b1*b2*c0*h9*h10-b1*b1*b2*c1*h8*h10+2*b1*b1*b2*c2*h7*h10+b1*b1*c0*c0*h4*h11+b1*b1*c0*c0*h5*h10+b1*b1*c0*c1*h3*h11+b1*b1*c0*c1*h5*h9+b1*b1*c0*c2*h2*h11-b1*b1*c0*c2*h3*h10-b1*b1*c0*c2*h4*h9+b1*b1*c0*c2*h5*h8-b1*b1*c1*c2*h2*h10-b1*b1*c1*c2*h4*h8-b1*b1*c2*c2*h1*h10-b1*b1*c2*c2*h4*h7-3*b1*b2*b2*c0*h7*h11-2*b1*b2*b2*c0*h8*h10-2*b1*b2*b2*c1*h7*h10+b1*b2*b2*c2*h6*h10+2*b1*b2*c0*c0*h3*h11+2*b1*b2*c0*c0*h4*h10+2*b1*b2*c0*c0*h5*h9+2*b1*b2*c0*c1*h2*h11+2*b1*b2*c0*c1*h3*h10+2*b1*b2*c0*c1*h4*h9+2*b1*b2*c0*c1*h5*h8+2*b1*b2*c0*c2*h1*h11+2*b1*b2*c0*c2*h5*h7+b1*b2*c1*c1*h2*h10+b1*b2*c1*c1*h4*h8-b1*b2*c2*c2*h0*h10-b1*b2*c2*c2*h4*h6-b1*c0*c0*c0*h5*h5-2*b1*c0*c0*c1*h4*h5-2*b1*c0*c0*c2*h3*h5+b1*c0*c0*c2*h4*h4-b1*c0*c1*c1*h3*h5-2*b1*c0*c1*c2*h2*h5+2*b1*c0*c1*c2*h3*h4-b1*c0*c2*c2*h1*h5+2*b1*c0*c2*c2*h2*h4+b1*c1*c1*c2*h2*h4+2*b1*c1*c2*c2*h1*h4+b1*c2*c2*c2*h0*h4-b2*b2*b2*c0*h6*h11-b2*b2*b2*c0*h7*h10-b2*b2*b2*c1*h6*h10+b2*b2*c0*c0*h2*h11+b2*b2*c0*c0*h3*h10+b2*b2*c0*c0*h4*h9+b2*b2*c0*c0*h5*h8+b2*b2*c0*c1*h1*h11+2*b2*b2*c0*c1*h2*h10+2*b2*b2*c0*c1*h4*h8+b2*b2*c0*c1*h5*h7+b2*b2*c0*c2*h0*h11+b2*b2*c0*c2*h1*h10+b2*b2*c0*c2*h4*h7+b2*b2*c0*c2*h5*h6+b2*b2*c1*c1*h1*h10+b2*b2*c1*c1*h4*h7+b2*b2*c1*c2*h0*h10+b2*b2*c1*c2*h4*h6-2*b2*c0*c0*c0*h4*h5-2*b2*c0*c0*c1*h3*h5-3*b2*c0*c0*c1*h4*h4-2*b2*c0*c0*c2*h2*h5-2*b2*c0*c0*c2*h3*h4-b2*c0*c1*c1*h2*h5-3*b2*c0*c1*c1*h3*h4-2*b2*c0*c1*c2*h1*h5-4*b2*c0*c1*c2*h2*h4-b2*c0*c2*c2*h0*h5-b2*c0*c2*c2*h1*h4-b2*c1*c1*c1*h2*h4-2*b2*c1*c1*c2*h1*h4-b2*c1*c2*c2*h0*h4,-9/32*a0*a0*b0*c2-9/32*a0*a0*b1*c1-9/32*a0*a0*b2*c0+43/4*a0*a0*c1*c2-9/16*a0*a1*b0*c1-9/16*a0*a1*b1*c0+83/4*a0*a1*c0*c2+83/8*a0*a1*c1*c1-9/16*a0*a2*b0*c0+37/2*a0*a2*c0*c1+27/64*a0*b0*b0*b2+27/64*a0*b0*b1*b1-20*a0*b0*b1*c2-151/8*a0*b0*b2*c1+73/2*a0*b0*c2*c2-157/16*a0*b1*b1*c1-37/2*a0*b1*b2*c0+59*a0*b1*c1*c2+87/2*a0*b2*c0*c2+22*a0*b2*c1*c1-297/2*a0*c1*c2*c2-9/32*a1*a1*b0*c0+10*a1*a1*c0*c1+71/8*a1*a2*c0*c0+27/64*a1*b0*b0*b1-157/16*a1*b0*b0*c2-77/4*a1*b0*b1*c1-145/8*a1*b0*b2*c0+115/2*a1*b0*c1*c2-151/16*a1*b1*b1*c0+43*a1*b1*c0*c2+87/4*a1*b1*c1*c1+28*a1*b2*c0*c1-101*a1*c0*c2*c2-213/2*a1*c1*c1*c2+9/64*a2*b0*b0*b0-139/16*a2*b0*b0*c1-17*a2*b0*b1*c0+39*a2*b0*c0*c2+79/4*a2*b0*c1*c1+25*a2*b1*c0*c1+19/4*a2*b2*c0*c0-124*a2*c0*c1*c2-45/2*a2*c1*c1*c1+417/16*b0*b0*b1*b2-521/16*b0*b0*b2*c2+145/16*b0*b1*b1*b1-529/16*b0*b1*b1*c2-313/8*b0*b1*b2*c1+455/8*b0*b1*c2*c2-85/16*b0*b2*b2*c0+323/4*b0*b2*c1*c2-117/2*b0*c2*c2*c2-107/16*b1*b1*b1*c1-93/16*b1*b1*b2*c0+36*b1*b1*c1*c2+28*b1*b2*c0*c2+39/2*b1*b2*c1*c1-165/2*b1*c1*c2*c2-5/2*b2*b2*c0*c1-23*b2*c0*c2*c2-147/2*b2*c1*c1*c2+110*c1*c2*c2*c2-3/4*a0*a1*c2*c2*h7+3/4*a0*a2*c0*c0*h10+3/2*a0*a2*c0*c1*h9+3/2*a0*a2*c0*c2*h8+3/4*a0*a2*c1*c1*h8-3/4*a0*b0*b2*c0*h10-3/4*a0*b0*b2*c1*h9-3/4*a0*b0*b2*c2*h8+2*a0*b0*c0*c2*h11+2*a0*b0*c1*c1*h11+2*a0*b0*c1*c2*h10-3/4*a0*b1*b2*c0*h9-3/4*a0*b1*b2*c1*h8+3/4*a0*b1*b2*c2*h7+2*a0*b1*c0*c2*h10-9/8*a0*b1*c2*c2*h1-3/4*a0*b2*b2*c0*h8+3/8*a0*b2*c0*c0*h4-a0*b2*c0*c0*h11+3/4*a0*b2*c0*c1*h3-2*a0*b2*c0*c1*h10+3/4*a0*b2*c0*c2*h2+3/8*a0*b2*c1*c1*h2-3/2*a0*b2*c1*c2*h1-3/4*a0*b2*c2*c2*h0-33/4*a0*b2*c2*c2*h7-a0*c0*c0*c2*h5-2*a0*c0*c1*c1*h5-2*a0*c0*c1*c2*h4-8*a0*c0*c1*c2*h11-4*a0*c0*c2*c2*h10-2*a0*c1*c1*c1*h11-2*a0*c1*c1*c2*h10+9*a0*c2*c2*c2*h1-3/4*a1*a1*c2*c2*h6+3/4*a1*a2*c0*c0*h9+3/2*a1*a2*c0*c1*h8+3/2*a1*a2*c0*c2*h7+3/4*a1*a2*c1*c1*h7-3/4*a1*b0*b2*c0*h9-3/4*a1*b0*b2*c1*h8+2*a1*b0*c0*c2*h10-3/4*a1*b0*c2*c2*h1-3/4*a1*b1*b2*c0*h8-3/4*a1*b1*b2*c1*h7+3/2*a1*b1*b2*c2*h6-2*a1*b1*c0*c0*h11-15/8*a1*b1*c2*c2*h0-3/4*a1*b2*b2*c0*h7+3/8*a1*b2*c0*c0*h3-a1*b2*c0*c0*h10+3/4*a1*b2*c0*c1*h2+3/2*a1*b2*c0*c2*h1+3/8*a1*b2*c1*c1*h1-3/4*a1*b2*c1*c2*h0-33/4*a1*b2*c2*c2*h6+2*a1*c0*c0*c1*h5-a1*c0*c0*c2*h4+4*a1*c0*c0*c2*h11+2*a1*c0*c1*c1*h11-4*a1*c0*c1*c2*h10+9*a1*c2*c2*c2*h0+3/4*a2*a2*c0*c0*h8+3/2*a2*a2*c0*c1*h7+3/2*a2*a2*c0*c2*h6+3/4*a2*a2*c1*c1*h6-3/4*a2*b0*b0*c0*h10-3/4*a2*b0*b0*c1*h9-3/4*a2*b0*b0*c2*h8-3/2*a2*b0*b1*c0*h9-3/2*a2*b0*b1*c1*h8-3/4*a2*b0*b1*c2*h7-9/4*a2*b0*b2*c0*h8-3/2*a2*b0*b2*c1*h7-3/2*a2*b0*b2*c2*h6+3/4*a2*b0*c0*c0*h4-a2*b0*c0*c0*h11+3/2*a2*b0*c0*c1*h3-2*a2*b0*c0*c1*h10+3/2*a2*b0*c0*c2*h2+3/4*a2*b0*c1*c1*h2-15/2*a2*b0*c2*c2*h7-3/4*a2*b1*b1*c0*h8-3/4*a2*b1*b1*c1*h7-9/4*a2*b1*b2*c0*h7-3/2*a2*b1*b2*c1*h6+3/4*a2*b1*c0*c0*h3-a2*b1*c0*c0*h10+3/2*a2*b1*c0*c1*h2+9/4*a2*b1*c0*c2*h1+3/4*a2*b1*c1*c1*h1+3/4*a2*b1*c1*c2*h0-15/2*a2*b1*c2*c2*h6-3/2*a2*b2*b2*c0*h6+9/8*a2*b2*c0*c0*h2+3*a2*b2*c0*c1*h1+3*a2*b2*c0*c2*h0+27/2*a2*b2*c0*c2*h7+15/8*a2*b2*c1*c1*h0+27/2*a2*b2*c1*c2*h6+a2*c0*c0*c0*h5+3*a2*c0*c0*c1*h4+4*a2*c0*c0*c1*h11+4*a2*c0*c0*c2*h10+6*a2*c0*c1*c1*h10-15/2*a2*c0*c2*c2*h1-15/2*a2*c1*c2*c2*h0+3/8*b0*b0*b0*b2*h10-b0*b0*b0*c2*h11+9/8*b0*b0*b1*b2*h9-2*b0*b0*b1*c1*h11-3*b0*b0*b1*c2*h10+9/8*b0*b0*b2*b2*h8-3/8*b0*b0*b2*c0*h4+b0*b0*b2*c0*h11-3/8*b0*b0*b2*c1*h3+b0*b0*b2*c1*h10-3/8*b0*b0*b2*c2*h2+b0*b0*c0*c2*h5+b0*b0*c1*c1*h5+b0*b0*c1*c2*h4+4*b0*b0*c1*c2*h11+2*b0*b0*c2*c2*h10+9/8*b0*b1*b1*b2*h8+2*b0*b1*b1*c0*h11+9/8*b0*b1*b2*b2*h7-3/4*b0*b1*b2*c0*h3+2*b0*b1*b2*c0*h10-3/4*b0*b1*b2*c1*h2+3/4*b0*b1*b2*c2*h1+2*b0*b1*c0*c2*h4+2*b0*b1*c1*c1*h11+4*b0*b1*c1*c2*h10+3/4*b0*b2*b2*b2*h6-3/4*b0*b2*b2*c0*h2+15/2*b0*b2*b2*c2*h7-b0*b2*c0*c0*h5-2*b0*b2*c0*c1*h4-2*b0*b2*c1*c1*h10-33/4*b0*b2*c2*c2*h1-8*b0*c0*c1*c2*h5-4*b0*c0*c2*c2*h4-2*b0*c1*c1*c1*h5-2*b0*c1*c1*c2*h4+3/8*b1*b1*b1*b2*h7-3/8*b1*b1*b2*c0*h2-3/8*b1*b1*b2*c1*h1+9/8*b1*b1*b2*c2*h0-b1*b1*c0*c0*h5-2*b1*b1*c0*c1*h11+2*b1*b1*c0*c2*h10-15/8*b1*b2*b2*c0*h1-9/8*b1*b2*b2*c1*h0+15/2*b1*b2*b2*c2*h6-b1*b2*c0*c0*h4-4*b1*b2*c0*c0*h11-4*b1*b2*c0*c1*h10-33/4*b1*b2*c2*c2*h0+4*b1*c0*c0*c2*h5+2*b1*c0*c1*c1*h5-4*b1*c0*c1*c2*h4-3/4*b2*b2*b2*c0*h0-27/4*b2*b2*b2*c0*h7-27/4*b2*b2*b2*c1*h6-2*b2*b2*c0*c0*h10+15/2*b2*b2*c0*c2*h1+15/2*b2*b2*c1*c2*h0+4*b2*c0*c0*c1*h5+4*b2*c0*c0*c2*h4+6*b2*c0*c1*c1*h4-2*a0*b0*c0*c1*h10*h11-2*a0*b0*c0*c2*h9*h11-2*a0*b0*c0*c2*h10*h10-2*a0*b0*c1*c1*h9*h11-4*a0*b0*c1*c2*h8*h11-2*a0*b0*c1*c2*h9*h10-2*a0*b0*c2*c2*h7*h11-2*a0*b0*c2*c2*h8*h10+a0*b1*c0*c0*h10*h11-2*a0*b1*c0*c2*h9*h10-a0*b1*c1*c1*h8*h11-2*a0*b1*c1*c2*h7*h11-2*a0*b1*c1*c2*h8*h10-a0*b1*c2*c2*h6*h11-2*a0*b1*c2*c2*h7*h10+a0*b2*c0*c0*h9*h11+a0*b2*c0*c0*h10*h10+2*a0*b2*c0*c1*h9*h10-a0*b2*c1*c1*h7*h11+a0*b2*c1*c1*h8*h10-2*a0*b2*c1*c2*h6*h11-a0*b2*c2*c2*h6*h10+a0*c0*c0*c1*h4*h11+a0*c0*c0*c1*h5*h10+a0*c0*c0*c2*h3*h11+2*a0*c0*c0*c2*h4*h10+a0*c0*c0*c2*h5*h9+2*a0*c0*c1*c1*h3*h11+2*a0*c0*c1*c1*h5*h9+4*a0*c0*c1*c2*h2*h11+2*a0*c0*c1*c2*h3*h10+2*a0*c0*c1*c2*h4*h9+4*a0*c0*c1*c2*h5*h8+2*a0*c0*c2*c2*h1*h11+2*a0*c0*c2*c2*h2*h10+2*a0*c0*c2*c2*h4*h8+2*a0*c0*c2*c2*h5*h7+a0*c1*c1*c1*h2*h11+a0*c1*c1*c1*h5*h8+3*a0*c1*c1*c2*h1*h11+a0*c1*c1*c2*h2*h10+a0*c1*c1*c2*h4*h8+3*a0*c1*c1*c2*h5*h7+3*a0*c1*c2*c2*h0*h11+2*a0*c1*c2*c2*h1*h10+2*a0*c1*c2*c2*h4*h7+3*a0*c1*c2*c2*h5*h6+a0*c2*c2*c2*h0*h10+a0*c2*c2*c2*h4*h6+a1*b0*c0*c0*h10*h11-2*a1*b0*c0*c2*h9*h10-a1*b0*c1*c1*h8*h11-2*a1*b0*c1*c2*h7*h11-2*a1*b0*c1*c2*h8*h10-a1*b0*c2*c2*h6*h11-2*a1*b0*c2*c2*h7*h10+2*a1*b1*c0*c0*h9*h11+2*a1*b1*c0*c1*h8*h11+2*a1*b1*c0*c2*h7*h11-2*a1*b1*c0*c2*h8*h10-2*a1*b1*c1*c2*h7*h10-2*a1*b1*c2*c2*h6*h10+2*a1*b2*c0*c0*h8*h11+a1*b2*c0*c0*h9*h10+2*a1*b2*c0*c1*h7*h11+2*a1*b2*c0*c1*h8*h10+2*a1*b2*c0*c2*h6*h11+a1*b2*c1*c1*h7*h10-a1*c0*c0*c0*h4*h11-a1*c0*c0*c0*h5*h10-2*a1*c0*c0*c1*h3*h11-2*a1*c0*c0*c1*h5*h9-2*a1*c0*c0*c2*h2*h11+a1*c0*c0*c2*h3*h10+a1*c0*c0*c2*h4*h9-2*a1*c0*c0*c2*h5*h8-a1*c0*c1*c1*h2*h11-a1*c0*c1*c1*h5*h8-2*a1*c0*c1*c2*h1*h11+2*a1*c0*c1*c2*h2*h10+2*a1*c0*c1*c2*h4*h8-2*a1*c0*c1*c2*h5*h7-a1*c0*c2*c2*h0*h11+2*a1*c0*c2*c2*h1*h10+2*a1*c0*c2*c2*h4*h7-a1*c0*c2*c2*h5*h6+a1*c1*c1*c2*h1*h10+a1*c1*c1*c2*h4*h7+2*a1*c1*c2*c2*h0*h10+2*a1*c1*c2*c2*h4*h6+a2*b0*c0*c0*h9*h11+a2*b0*c0*c0*h10*h10+2*a2*b0*c0*c1*h9*h10-a2*b0*c1*c1*h7*h11+a2*b0*c1*c1*h8*h10-2*a2*b0*c1*c2*h6*h11-a2*b0*c2*c2*h6*h10+2*a2*b1*c0*c0*h8*h11+a2*b1*c0*c0*h9*h10+2*a2*b1*c0*c1*h7*h11+2*a2*b1*c0*c1*h8*h10+2*a2*b1*c0*c2*h6*h11+a2*b1*c1*c1*h7*h10+2*a2*b2*c0*c0*h7*h11+2*a2*b2*c0*c0*h8*h10+2*a2*b2*c0*c1*h6*h11+4*a2*b2*c0*c1*h7*h10+2*a2*b2*c0*c2*h6*h10+2*a2*b2*c1*c1*h6*h10-a2*c0*c0*c0*h3*h11-2*a2*c0*c0*c0*h4*h10-a2*c0*c0*c0*h5*h9-2*a2*c0*c0*c1*h2*h11-3*a2*c0*c0*c1*h3*h10-3*a2*c0*c0*c1*h4*h9-2*a2*c0*c0*c1*h5*h8-2*a2*c0*c0*c2*h1*h11-2*a2*c0*c0*c2*h2*h10-2*a2*c0*c0*c2*h4*h8-2*a2*c0*c0*c2*h5*h7-a2*c0*c1*c1*h1*h11-3*a2*c0*c1*c1*h2*h10-3*a2*c0*c1*c1*h4*h8-a2*c0*c1*c1*h5*h7-2*a2*c0*c1*c2*h0*h11-4*a2*c0*c1*c2*h1*h10-4*a2*c0*c1*c2*h4*h7-2*a2*c0*c1*c2*h5*h6-a2*c0*c2*c2*h0*h10-a2*c0*c2*c2*h4*h6-a2*c1*c1*c1*h1*h10-a2*c1*c1*c1*h4*h7-2*a2*c1*c1*c2*h0*h10-2*a2*c1*c1*c2*h4*h6+b0*b0*b0*c1*h10*h11+b0*b0*b0*c2*h9*h11+b0*b0*b0*c2*h10*h10-b0*b0*b1*c0*h10*h11+2*b0*b0*b1*c1*h9*h11+2*b0*b0*b1*c2*h8*h11+3*b0*b0*b1*c2*h9*h10-b0*b0*b2*c0*h9*h11-b0*b0*b2*c0*h10*h10+2*b0*b0*b2*c1*h8*h11-b0*b0*b2*c1*h9*h10+2*b0*b0*b2*c2*h7*h11+2*b0*b0*b2*c2*h8*h10-b0*b0*c0*c1*h4*h11-b0*b0*c0*c1*h5*h10-b0*b0*c0*c2*h3*h11-2*b0*b0*c0*c2*h4*h10-b0*b0*c0*c2*h5*h9-b0*b0*c1*c1*h3*h11-b0*b0*c1*c1*h5*h9-2*b0*b0*c1*c2*h2*h11-b0*b0*c1*c2*h3*h10-b0*b0*c1*c2*h4*h9-2*b0*b0*c1*c2*h5*h8-b0*b0*c2*c2*h1*h11-b0*b0*c2*c2*h2*h10-b0*b0*c2*c2*h4*h8-b0*b0*c2*c2*h5*h7-2*b0*b1*b1*c0*h9*h11+b0*b1*b1*c1*h8*h11+b0*b1*b1*c2*h7*h11+3*b0*b1*b1*c2*h8*h10-4*b0*b1*b2*c0*h8*h11-2*b0*b1*b2*c0*h9*h10+2*b0*b1*b2*c1*h7*h11-2*b0*b1*b2*c1*h8*h10+2*b0*b1*b2*c2*h6*h11+4*b0*b1*b2*c2*h7*h10+b0*b1*c0*c0*h4*h11+b0*b1*c0*c0*h5*h10-2*b0*b1*c0*c2*h3*h10-2*b0*b1*c0*c2*h4*h9-b0*b1*c1*c1*h2*h11-b0*b1*c1*c1*h5*h8-2*b0*b1*c1*c2*h1*h11-2*b0*b1*c1*c2*h2*h10-2*b0*b1*c1*c2*h4*h8-2*b0*b1*c1*c2*h5*h7-b0*b1*c2*c2*h0*h11-2*b0*b1*c2*c2*h1*h10-2*b0*b1*c2*c2*h4*h7-b0*b1*c2*c2*h5*h6-2*b0*b2*b2*c0*h7*h11-2*b0*b2*b2*c0*h8*h10+b0*b2*b2*c1*h6*h11-2*b0*b2*b2*c1*h7*h10+b0*b2*b2*c2*h6*h10+b0*b2*c0*c0*h3*h11+2*b0*b2*c0*c0*h4*h10+b0*b2*c0*c0*h5*h9+2*b0*b2*c0*c1*h3*h10+2*b0*b2*c0*c1*h4*h9-b0*b2*c1*c1*h1*h11+b0*b2*c1*c1*h2*h10+b0*b2*c1*c1*h4*h8-b0*b2*c1*c1*h5*h7-2*b0*b2*c1*c2*h0*h11-2*b0*b2*c1*c2*h5*h6-b0*b2*c2*c2*h0*h10-b0*b2*c2*c2*h4*h6+b0*c0*c0*c1*h4*h5+b0*c0*c0*c2*h3*h5+b0*c0*c0*c2*h4*h4+2*b0*c0*c1*c1*h3*h5+4*b0*c0*c1*c2*h2*h5+2*b0*c0*c1*c2*h3*h4+2*b0*c0*c2*c2*h1*h5+2*b0*c0*c2*c2*h2*h4+b0*c1*c1*c1*h2*h5+3*b0*c1*c1*c2*h1*h5+b0*c1*c1*c2*h2*h4+3*b0*c1*c2*c2*h0*h5+2*b0*c1*c2*c2*h1*h4+b0*c2*c2*c2*h0*h4-b1*b1*b1*c0*h8*h11+b1*b1*b1*c2*h7*h10-3*b1*b1*b2*c0*h7*h11-b1*b1*b2*c0*h8*h10-b1*b1*b2*c1*h7*h10+2*b1*b1*b2*c2*h6*h10+b1*b1*c0*c0*h3*h11+b1*b1*c0*c0*h5*h9+b1*b1*c0*c1*h2*h11+b1*b1*c0*c1*h5*h8+b1*b1*c0*c2*h1*h11-b1*b1*c0*c2*h2*h10-b1*b1*c0*c2*h4*h8+b1*b1*c0*c2*h5*h7-b1*b1*c1*c2*h1*h10-b1*b1*c1*c2*h4*h7-b1*b1*c2*c2*h0*h10-b1*b1*c2*c2*h4*h6-3*b1*b2*b2*c0*h6*h11-2*b1*b2*b2*c0*h7*h10-2*b1*b2*b2*c1*h6*h10+2*b1*b2*c0*c0*h2*h11+b1*b2*c0*c0*h3*h10+b1*b2*c0*c0*h4*h9+2*b1*b2*c0*c0*h5*h8+2*b1*b2*c0*c1*h1*h11+2*b1*b2*c0*c1*h2*h10+2*b1*b2*c0*c1*h4*h8+2*b1*b2*c0*c1*h5*h7+2*b1*b2*c0*c2*h0*h11+2*b1*b2*c0*c2*h5*h6+b1*b2*c1*c1*h1*h10+b1*b2*c1*c1*h4*h7-b1*c0*c0*c0*h4*h5-2*b1*c0*c0*c1*h3*h5-2*b1*c0*c0*c2*h2*h5+b1*c0*c0*c2*h3*h4-b1*c0*c1*c1*h2*h5-2*b1*c0*c1*c2*h1*h5+2*b1*c0*c1*c2*h2*h4-b1*c0*c2*c2*h0*h5+2*b1*c0*c2*c2*h1*h4+b1*c1*c1*c2*h1*h4+2*b1*c1*c2*c2*h0*h4-b2*b2*b2*c0*h6*h10+b2*b2*c0*c0*h1*h11+b2*b2*c0*c0*h2*h10+b2*b2*c0*c0*h4*h8+b2*b2*c0*c0*h5*h7+b2*b2*c0*c1*h0*h11+2*b2*b2*c0*c1*h1*h10+2*b2*b2*c0*c1*h4*h7+b2*b2*c0*c1*h5*h6+b2*b2*c0*c2*h0*h10+b2*b2*c0*c2*h4*h6+b2*b2*c1*c1*h0*h10+b2*b2*c1*c1*h4*h6-b2*c0*c0*c0*h3*h5-b2*c0*c0*c0*h4*h4-2*b2*c0*c0*c1*h2*h5-3*b2*c0*c0*c1*h3*h4-2*b2*c0*c0*c2*h1*h5-2*b2*c0*c0*c2*h2*h4-b2*c0*c1*c1*h1*h5-3*b2*c0*c1*c1*h2*h4-2*b2*c0*c1*c2*h0*h5-4*b2*c0*c1*c2*h1*h4-b2*c0*c2*c2*h0*h4-b2*c1*c1*c1*h1*h4-2*b2*c1*c1*c2*h0*h4,-9/32*a0*a0*b0*c1-9/32*a0*a0*b1*c0+43/4*a0*a0*c0*c2+43/8*a0*a0*c1*c1-9/16*a0*a1*b0*c0+83/4*a0*a1*c0*c1+37/4*a0*a2*c0*c0+27/64*a0*b0*b0*b1-163/16*a0*b0*b0*c2-20*a0*b0*b1*c1-151/8*a0*b0*b2*c0+67*a0*b0*c1*c2-157/16*a0*b1*b1*c0+105/2*a0*b1*c0*c2+53/2*a0*b1*c1*c1+75/2*a0*b2*c0*c1-271/2*a0*c0*c2*c2-141*a0*c1*c1*c2+5*a1*a1*c0*c0+9/64*a1*b0*b0*b0-157/16*a1*b0*b0*c1-77/4*a1*b0*b1*c0+51*a1*b0*c0*c2+103/4*a1*b0*c1*c1+37*a1*b1*c0*c1+43/4*a1*b2*c0*c0-187*a1*c0*c1*c2-33*a1*c1*c1*c1-139/16*a2*b0*b0*c0+33*a2*b0*c0*c1+37/4*a2*b1*c0*c0-49*a2*c0*c0*c2-109/2*a2*c0*c1*c1+71/8*b0*b0*b0*b2+111/8*b0*b0*b1*b1-593/16*b0*b0*b1*c2-377/16*b0*b0*b2*c1+281/8*b0*b0*c2*c2-385/16*b0*b1*b1*c1-157/8*b0*b1*b2*c0+395/4*b0*b1*c1*c2+219/4*b0*b2*c0*c2+263/8*b0*b2*c1*c1-351/2*b0*c1*c2*c2-55/16*b1*b1*b1*c0+23*b1*b1*c0*c2+57/4*b1*b1*c1*c1+13*b1*b2*c0*c1-32*b1*c0*c2*c2-165/2*b1*c1*c1*c2-31/4*b2*b2*c0*c0-46*b2*c0*c1*c2-49/2*b2*c1*c1*c1+80*c0*c2*c2*c2+174*c1*c1*c2*c2-3/4*a0*a0*c2*c2*h7-3/2*a0*a1*c1*c2*h7-3/2*a0*a1*c2*c2*h6+3/4*a0*a2*c0*c0*h9+3/2*a0*a2*c0*c1*h8-3/4*a0*b0*b2*c0*h9-3/4*a0*b0*b2*c1*h8+3/2*a0*b0*b2*c2*h7+2*a0*b0*c0*c1*h11+2*a0*b0*c0*c2*h10-15/8*a0*b0*c2*c2*h1+3/4*a0*b1*b1*c2*h7-3/4*a0*b1*b2*c0*h8+3/4*a0*b1*b2*c1*h7+3/2*a0*b1*b2*c2*h6-a0*b1*c0*c0*h11-9/4*a0*b1*c1*c2*h1-15/8*a0*b1*c2*c2*h0-33/4*a0*b1*c2*c2*h7+3/8*a0*b2*c0*c0*h3-a0*b2*c0*c0*h10+3/4*a0*b2*c0*c1*h2-3/4*a0*b2*c0*c2*h1-3/4*a0*b2*c1*c1*h1-3/4*a0*b2*c1*c2*h0-33/2*a0*b2*c1*c2*h7-35/4*a0*b2*c2*c2*h6-a0*c0*c0*c1*h5-a0*c0*c0*c2*h4-2*a0*c0*c0*c2*h11-4*a0*c0*c1*c1*h11-4*a0*c0*c1*c2*h10+27*a0*c1*c2*c2*h1+19/2*a0*c2*c2*c2*h0+6*a0*c2*c2*c2*h7-3/2*a1*a1*c1*c2*h6+3/4*a1*a2*c0*c0*h8+3/2*a1*a2*c0*c1*h7+3/4*a1*b0*b1*c2*h7-3/4*a1*b0*b2*c0*h8+3/2*a1*b0*b2*c2*h6-a1*b0*c0*c0*h11-3/2*a1*b0*c1*c2*h1-15/8*a1*b0*c2*c2*h0-15/2*a1*b0*c2*c2*h7+3/2*a1*b1*b1*c2*h6-3/4*a1*b1*b2*c0*h7+3/2*a1*b1*b2*c1*h6+3/4*a1*b1*c0*c2*h1-3*a1*b1*c1*c2*h0-63/4*a1*b1*c2*c2*h6+3/8*a1*b2*c0*c0*h2+3/2*a1*b2*c0*c1*h1-3/4*a1*b2*c0*c2*h0+27/2*a1*b2*c0*c2*h7-3*a1*b2*c1*c2*h6+a1*c0*c0*c0*h5+4*a1*c0*c0*c1*h11-2*a1*c0*c0*c2*h10-15/2*a1*c0*c2*c2*h1+39/2*a1*c1*c2*c2*h0+6*a1*c2*c2*c2*h6+3/4*a2*a2*c0*c0*h7+3/2*a2*a2*c0*c1*h6-3/4*a2*b0*b0*c0*h9-3/4*a2*b0*b0*c1*h8-3/2*a2*b0*b1*c0*h8-3/4*a2*b0*b1*c1*h7-3/2*a2*b0*b2*c0*h7-3/2*a2*b0*b2*c1*h6+3/4*a2*b0*c0*c0*h3-a2*b0*c0*c0*h10+3/2*a2*b0*c0*c1*h2+3/4*a2*b0*c0*c2*h1+3/4*a2*b0*c1*c2*h0-15*a2*b0*c1*c2*h7-8*a2*b0*c2*c2*h6-3/4*a2*b1*b1*c0*h7-3/2*a2*b1*b2*c0*h6+3/4*a2*b1*c0*c0*h2+9/4*a2*b1*c0*c1*h1+3/4*a2*b1*c0*c2*h0+27/2*a2*b1*c0*c2*h7+3/4*a2*b1*c1*c1*h0-3/2*a2*b1*c1*c2*h6+15/8*a2*b2*c0*c0*h1+15/4*a2*b2*c0*c1*h0+27/2*a2*b2*c0*c1*h7+29/2*a2*b2*c0*c2*h6+27/2*a2*b2*c1*c1*h6+a2*c0*c0*c0*h4+2*a2*c0*c0*c0*h11+6*a2*c0*c0*c1*h10-15*a2*c0*c1*c2*h1-8*a2*c0*c2*c2*h0-3*a2*c0*c2*c2*h7-15*a2*c1*c1*c2*h0-3*a2*c1*c2*c2*h6+3/8*b0*b0*b0*b2*h9-b0*b0*b0*c1*h11-b0*b0*b0*c2*h10+9/8*b0*b0*b1*b2*h8+b0*b0*b1*c0*h11-3/8*b0*b0*b2*c0*h3+b0*b0*b2*c0*h10-3/8*b0*b0*b2*c1*h2+9/8*b0*b0*b2*c2*h1+b0*b0*c0*c1*h5+b0*b0*c0*c2*h4+2*b0*b0*c0*c2*h11+2*b0*b0*c1*c1*h11+2*b0*b0*c1*c2*h10+3/4*b0*b1*b1*c2*h1-3/4*b0*b1*b2*c0*h2+3/4*b0*b1*b2*c1*h1+9/4*b0*b1*b2*c2*h0+15*b0*b1*b2*c2*h7-b0*b1*c0*c0*h5+4*b0*b1*c0*c2*h10-33/4*b0*b1*c2*c2*h1-9/8*b0*b2*b2*c0*h1-9/8*b0*b2*b2*c1*h0+15/2*b0*b2*b2*c1*h7+8*b0*b2*b2*c2*h6-b0*b2*c0*c0*h4-2*b0*b2*c0*c0*h11-4*b0*b2*c0*c1*h10-33/2*b0*b2*c1*c2*h1-35/4*b0*b2*c2*c2*h0-9/2*b0*b2*c2*c2*h7-2*b0*c0*c0*c2*h5-4*b0*c0*c1*c1*h5-4*b0*c0*c1*c2*h4+6*b0*c2*c2*c2*h1-3/4*b1*b1*b1*b2*h6+3/4*b1*b1*b1*c2*h0-3/2*b1*b1*b2*c0*h1+15*b1*b1*b2*c2*h6-2*b1*b1*c0*c0*h11-33/4*b1*b1*c2*c2*h0-9/8*b1*b2*b2*c0*h0-81/4*b1*b2*b2*c0*h7-51/4*b1*b2*b2*c1*h6-2*b1*b2*c0*c0*h10+15*b1*b2*c0*c2*h1-3/2*b1*b2*c1*c2*h0-9/2*b1*b2*c2*c2*h6+4*b1*c0*c0*c1*h5-2*b1*c0*c0*c2*h4+6*b1*c2*c2*c2*h0-29/4*b2*b2*b2*c0*h6+15/2*b2*b2*c0*c1*h1+8*b2*b2*c0*c2*h0+3*b2*b2*c0*c2*h7+15/2*b2*b2*c1*c1*h0+3*b2*b2*c1*c2*h6+2*b2*c0*c0*c0*h5+6*b2*c0*c0*c1*h4-9/2*b2*c0*c2*c2*h1-9/2*b2*c1*c2*c2*h0-2*a0*b0*c0*c1*h9*h11-2*a0*b0*c0*c2*h8*h11-2*a0*b0*c0*c2*h9*h10-2*a0*b0*c1*c1*h8*h11-4*a0*b0*c1*c2*h7*h11-2*a0*b0*c1*c2*h8*h10-2*a0*b0*c2*c2*h6*h11-2*a0*b0*c2*c2*h7*h10+a0*b1*c0*c0*h9*h11-2*a0*b1*c0*c2*h8*h10-a0*b1*c1*c1*h7*h11-2*a0*b1*c1*c2*h6*h11-2*a0*b1*c1*c2*h7*h10-2*a0*b1*c2*c2*h6*h10+a0*b2*c0*c0*h8*h11+a0*b2*c0*c0*h9*h10+2*a0*b2*c0*c1*h8*h10-a0*b2*c1*c1*h6*h11+a0*b2*c1*c1*h7*h10+a0*c0*c0*c1*h3*h11+a0*c0*c0*c1*h5*h9+a0*c0*c0*c2*h2*h11+a0*c0*c0*c2*h3*h10+a0*c0*c0*c2*h4*h9+a0*c0*c0*c2*h5*h8+2*a0*c0*c1*c1*h2*h11+2*a0*c0*c1*c1*h5*h8+4*a0*c0*c1*c2*h1*h11+2*a0*c0*c1*c2*h2*h10+2*a0*c0*c1*c2*h4*h8+4*a0*c0*c1*c2*h5*h7+2*a0*c0*c2*c2*h0*h11+2*a0*c0*c2*c2*h1*h10+2*a0*c0*c2*c2*h4*h7+2*a0*c0*c2*c2*h5*h6+a0*c1*c1*c1*h1*h11+a0*c1*c1*c1*h5*h7+3*a0*c1*c1*c2*h0*h11+a0*c1*c1*c2*h1*h10+a0*c1*c1*c2*h4*h7+3*a0*c1*c1*c2*h5*h6+2*a0*c1*c2*c2*h0*h10+2*a0*c1*c2*c2*h4*h6+a1*b0*c0*c0*h9*h11-2*a1*b0*c0*c2*h8*h10-a1*b0*c1*c1*h7*h11-2*a1*b0*c1*c2*h6*h11-2*a1*b0*c1*c2*h7*h10-2*a1*b0*c2*c2*h6*h10+2*a1*b1*c0*c0*h8*h11+2*a1*b1*c0*c1*h7*h11+2*a1*b1*c0*c2*h6*h11-2*a1*b1*c0*c2*h7*h10-2*a1*b1*c1*c2*h6*h10+2*a1*b2*c0*c0*h7*h11+a1*b2*c0*c0*h8*h10+2*a1*b2*c0*c1*h6*h11+2*a1*b2*c0*c1*h7*h10+a1*b2*c1*c1*h6*h10-a1*c0*c0*c0*h3*h11-a1*c0*c0*c0*h5*h9-2*a1*c0*c0*c1*h2*h11-2*a1*c0*c0*c1*h5*h8-2*a1*c0*c0*c2*h1*h11+a1*c0*c0*c2*h2*h10+a1*c0*c0*c2*h4*h8-2*a1*c0*c0*c2*h5*h7-a1*c0*c1*c1*h1*h11-a1*c0*c1*c1*h5*h7-2*a1*c0*c1*c2*h0*h11+2*a1*c0*c1*c2*h1*h10+2*a1*c0*c1*c2*h4*h7-2*a1*c0*c1*c2*h5*h6+2*a1*c0*c2*c2*h0*h10+2*a1*c0*c2*c2*h4*h6+a1*c1*c1*c2*h0*h10+a1*c1*c1*c2*h4*h6+a2*b0*c0*c0*h8*h11+a2*b0*c0*c0*h9*h10+2*a2*b0*c0*c1*h8*h10-a2*b0*c1*c1*h6*h11+a2*b0*c1*c1*h7*h10+2*a2*b1*c0*c0*h7*h11+a2*b1*c0*c0*h8*h10+2*a2*b1*c0*c1*h6*h11+2*a2*b1*c0*c1*h7*h10+a2*b1*c1*c1*h6*h10+2*a2*b2*c0*c0*h6*h11+2*a2*b2*c0*c0*h7*h10+4*a2*b2*c0*c1*h6*h10-a2*c0*c0*c0*h2*h11-a2*c0*c0*c0*h3*h10-a2*c0*c0*c0*h4*h9-a2*c0*c0*c0*h5*h8-2*a2*c0*c0*c1*h1*h11-3*a2*c0*c0*c1*h2*h10-3*a2*c0*c0*c1*h4*h8-2*a2*c0*c0*c1*h5*h7-2*a2*c0*c0*c2*h0*h11-2*a2*c0*c0*c2*h1*h10-2*a2*c0*c0*c2*h4*h7-2*a2*c0*c0*c2*h5*h6-a2*c0*c1*c1*h0*h11-3*a2*c0*c1*c1*h1*h10-3*a2*c0*c1*c1*h4*h7-a2*c0*c1*c1*h5*h6-4*a2*c0*c1*c2*h0*h10-4*a2*c0*c1*c2*h4*h6-a2*c1*c1*c1*h0*h10-a2*c1*c1*c1*h4*h6+b0*b0*b0*c1*h9*h11+b0*b0*b0*c2*h8*h11+b0*b0*b0*c2*h9*h10-b0*b0*b1*c0*h9*h11+2*b0*b0*b1*c1*h8*h11+2*b0*b0*b1*c2*h7*h11+3*b0*b0*b1*c2*h8*h10-b0*b0*b2*c0*h8*h11-b0*b0*b2*c0*h9*h10+2*b0*b0*b2*c1*h7*h11-b0*b0*b2*c1*h8*h10+2*b0*b0*b2*c2*h6*h11+2*b0*b0*b2*c2*h7*h10-b0*b0*c0*c1*h3*h11-b0*b0*c0*c1*h5*h9-b0*b0*c0*c2*h2*h11-b0*b0*c0*c2*h3*h10-b0*b0*c0*c2*h4*h9-b0*b0*c0*c2*h5*h8-b0*b0*c1*c1*h2*h11-b0*b0*c1*c1*h5*h8-2*b0*b0*c1*c2*h1*h11-b0*b0*c1*c2*h2*h10-b0*b0*c1*c2*h4*h8-2*b0*b0*c1*c2*h5*h7-b0*b0*c2*c2*h0*h11-b0*b0*c2*c2*h1*h10-b0*b0*c2*c2*h4*h7-b0*b0*c2*c2*h5*h6-2*b0*b1*b1*c0*h8*h11+b0*b1*b1*c1*h7*h11+b0*b1*b1*c2*h6*h11+3*b0*b1*b1*c2*h7*h10-4*b0*b1*b2*c0*h7*h11-2*b0*b1*b2*c0*h8*h10+2*b0*b1*b2*c1*h6*h11-2*b0*b1*b2*c1*h7*h10+4*b0*b1*b2*c2*h6*h10+b0*b1*c0*c0*h3*h11+b0*b1*c0*c0*h5*h9-2*b0*b1*c0*c2*h2*h10-2*b0*b1*c0*c2*h4*h8-b0*b1*c1*c1*h1*h11-b0*b1*c1*c1*h5*h7-2*b0*b1*c1*c2*h0*h11-2*b0*b1*c1*c2*h1*h10-2*b0*b1*c1*c2*h4*h7-2*b0*b1*c1*c2*h5*h6-2*b0*b1*c2*c2*h0*h10-2*b0*b1*c2*c2*h4*h6-2*b0*b2*b2*c0*h6*h11-2*b0*b2*b2*c0*h7*h10-2*b0*b2*b2*c1*h6*h10+b0*b2*c0*c0*h2*h11+b0*b2*c0*c0*h3*h10+b0*b2*c0*c0*h4*h9+b0*b2*c0*c0*h5*h8+2*b0*b2*c0*c1*h2*h10+2*b0*b2*c0*c1*h4*h8-b0*b2*c1*c1*h0*h11+b0*b2*c1*c1*h1*h10+b0*b2*c1*c1*h4*h7-b0*b2*c1*c1*h5*h6+b0*c0*c0*c1*h3*h5+b0*c0*c0*c2*h2*h5+b0*c0*c0*c2*h3*h4+2*b0*c0*c1*c1*h2*h5+4*b0*c0*c1*c2*h1*h5+2*b0*c0*c1*c2*h2*h4+2*b0*c0*c2*c2*h0*h5+2*b0*c0*c2*c2*h1*h4+b0*c1*c1*c1*h1*h5+3*b0*c1*c1*c2*h0*h5+b0*c1*c1*c2*h1*h4+2*b0*c1*c2*c2*h0*h4-b1*b1*b1*c0*h7*h11+b1*b1*b1*c2*h6*h10-3*b1*b1*b2*c0*h6*h11-b1*b1*b2*c0*h7*h10-b1*b1*b2*c1*h6*h10+b1*b1*c0*c0*h2*h11+b1*b1*c0*c0*h5*h8+b1*b1*c0*c1*h1*h11+b1*b1*c0*c1*h5*h7+b1*b1*c0*c2*h0*h11-b1*b1*c0*c2*h1*h10-b1*b1*c0*c2*h4*h7+b1*b1*c0*c2*h5*h6-b1*b1*c1*c2*h0*h10-b1*b1*c1*c2*h4*h6-2*b1*b2*b2*c0*h6*h10+2*b1*b2*c0*c0*h1*h11+b1*b2*c0*c0*h2*h10+b1*b2*c0*c0*h4*h8+2*b1*b2*c0*c0*h5*h7+2*b1*b2*c0*c1*h0*h11+2*b1*b2*c0*c1*h1*h10+2*b1*b2*c0*c1*h4*h7+2*b1*b2*c0*c1*h5*h6+b1*b2*c1*c1*h0*h10+b1*b2*c1*c1*h4*h6-b1*c0*c0*c0*h3*h5-2*b1*c0*c0*c1*h2*h5-2*b1*c0*c0*c2*h1*h5+b1*c0*c0*c2*h2*h4-b1*c0*c1*c1*h1*h5-2*b1*c0*c1*c2*h0*h5+2*b1*c0*c1*c2*h1*h4+2*b1*c0*c2*c2*h0*h4+b1*c1*c1*c2*h0*h4+b2*b2*c0*c0*h0*h11+b2*b2*c0*c0*h1*h10+b2*b2*c0*c0*h4*h7+b2*b2*c0*c0*h5*h6+2*b2*b2*c0*c1*h0*h10+2*b2*b2*c0*c1*h4*h6-b2*c0*c0*c0*h2*h5-b2*c0*c0*c0*h3*h4-2*b2*c0*c0*c1*h1*h5-3*b2*c0*c0*c1*h2*h4-2*b2*c0*c0*c2*h0*h5-2*b2*c0*c0*c2*h1*h4-b2*c0*c1*c1*h0*h5-3*b2*c0*c1*c1*h1*h4-4*b2*c0*c1*c2*h0*h4-b2*c1*c1*c1*h0*h4,-9/32*a0*a0*b0*c0+43/4*a0*a0*c0*c1+83/8*a0*a1*c0*c0+9/64*a0*b0*b0*b0-163/16*a0*b0*b0*c1-20*a0*b0*b1*c0+121/2*a0*b0*c0*c2+61/2*a0*b0*c1*c1+93/2*a0*b1*c0*c1+31/2*a0*b2*c0*c0-256*a0*c0*c1*c2-89/2*a0*c1*c1*c1-157/16*a1*b0*b0*c0+45*a1*b0*c0*c1+61/4*a1*b1*c0*c0-161/2*a1*c0*c0*c2-86*a1*c0*c1*c1+53/4*a2*b0*c0*c0-83/2*a2*c0*c0*c1+151/16*b0*b0*b0*b1-219/16*b0*b0*b0*c2-449/16*b0*b0*b1*c1-221/16*b0*b0*b2*c0+251/4*b0*b0*c1*c2-229/16*b0*b1*b1*c0+291/4*b0*b1*c0*c2+335/8*b0*b1*c1*c1+159/4*b0*b2*c0*c1-125*b0*c0*c2*c2-351/2*b0*c1*c1*c2+31/2*b1*b1*c0*c1-13/2*b1*b2*c0*c0-64*b1*c0*c1*c2-55/2*b1*c1*c1*c1+55/2*b2*c0*c0*c2-23*b2*c0*c1*c1+258*c0*c1*c2*c2+122*c1*c1*c1*c2-3/2*a0*a0*c1*c2*h7-3/4*a0*a0*c2*c2*h6-3/2*a0*a1*c0*c2*h7-3/4*a0*a1*c1*c1*h7-3*a0*a1*c1*c2*h6+3/4*a0*a2*c0*c0*h8+9/4*a0*b0*b1*c2*h7-3/4*a0*b0*b2*c0*h8+3/2*a0*b0*b2*c1*h7+3/2*a0*b0*b2*c2*h6-15/4*a0*b0*c1*c2*h1-15/8*a0*b0*c2*c2*h0-63/4*a0*b0*c2*c2*h7+3/4*a0*b1*b1*c1*h7+3/2*a0*b1*b1*c2*h6+3/4*a0*b1*b2*c0*h7+3/2*a0*b1*b2*c1*h6-3/2*a0*b1*c0*c2*h1-9/8*a0*b1*c1*c1*h1-3*a0*b1*c1*c2*h0-33/2*a0*b1*c1*c2*h7-65/4*a0*b1*c2*c2*h6+3/8*a0*b2*c0*c0*h2-3/4*a0*b2*c0*c1*h1-3/4*a0*b2*c0*c2*h0-3*a0*b2*c0*c2*h7-33/4*a0*b2*c1*c1*h7-4*a0*b2*c1*c2*h6-2*a0*c0*c0*c1*h11-2*a0*c0*c0*c2*h10+39/2*a0*c0*c2*c2*h1+27*a0*c1*c1*c2*h1+21*a0*c1*c2*c2*h0+18*a0*c1*c2*c2*h7+7*a0*c2*c2*c2*h6-3/2*a1*a1*c0*c2*h6-3/4*a1*a1*c1*c1*h6+3/4*a1*a2*c0*c0*h7+3/4*a1*b0*b0*c2*h7+3/4*a1*b0*b1*c1*h7+3*a1*b0*b1*c2*h6+3/2*a1*b0*b2*c1*h6-3/4*a1*b0*c0*c2*h1-3/4*a1*b0*c1*c1*h1-3*a1*b0*c1*c2*h0-15*a1*b0*c1*c2*h7-65/4*a1*b0*c2*c2*h6+3/2*a1*b1*b1*c1*h6+3/2*a1*b1*b2*c0*h6+3/4*a1*b1*c0*c1*h1-3*a1*b1*c0*c2*h0+27/2*a1*b1*c0*c2*h7-9/8*a1*b1*c1*c1*h0-18*a1*b1*c1*c2*h6+9/8*a1*b2*c0*c0*h1+27/2*a1*b2*c0*c1*h7-2*a1*b2*c0*c2*h6+21/4*a1*b2*c1*c1*h6+2*a1*c0*c0*c0*h11-15*a1*c0*c1*c2*h1+19*a1*c0*c2*c2*h0-3*a1*c0*c2*c2*h7+12*a1*c1*c1*c2*h0+15*a1*c1*c2*c2*h6+3/4*a2*a2*c0*c0*h6-3/4*a2*b0*b0*c0*h8-3/4*a2*b0*b1*c0*h7-3/2*a2*b0*b2*c0*h6+3/4*a2*b0*c0*c0*h2+3/4*a2*b0*c0*c1*h1+3/4*a2*b0*c0*c2*h0-3/2*a2*b0*c0*c2*h7+3/4*a2*b0*c1*c1*h0-15/2*a2*b0*c1*c1*h7-5/2*a2*b0*c1*c2*h6+3/2*a2*b1*c0*c0*h1+3/2*a2*b1*c0*c1*h0+27/2*a2*b1*c0*c1*h7-1/2*a2*b1*c0*c2*h6+6*a2*b1*c1*c1*h6+15/8*a2*b2*c0*c0*h0+27/2*a2*b2*c0*c0*h7+28*a2*b2*c0*c1*h6+2*a2*c0*c0*c0*h10-15*a2*c0*c0*c2*h1-15/2*a2*c0*c1*c1*h1-31*a2*c0*c1*c2*h0-6*a2*c0*c1*c2*h7-4*a2*c0*c2*c2*h6-15/2*a2*c1*c1*c1*h0-6*a2*c1*c1*c2*h6+3/8*b0*b0*b0*b2*h8-9/8*b0*b0*b1*b2*h7+3/2*b0*b0*b1*c2*h1-3/8*b0*b0*b2*c0*h2+9/8*b0*b0*b2*c1*h1+9/8*b0*b0*b2*c2*h0+15*b0*b0*b2*c2*h7+2*b0*b0*c0*c1*h11+2*b0*b0*c0*c2*h10-33/4*b0*b0*c2*c2*h1-3/8*b0*b1*b1*b1*h7-9/4*b0*b1*b1*b2*h6+3/4*b0*b1*b1*c1*h1+9/4*b0*b1*b1*c2*h0+15/2*b0*b1*b1*c2*h7-3/2*b0*b1*b2*c0*h1+15*b0*b1*b2*c1*h7+31*b0*b1*b2*c2*h6-2*b0*b1*c0*c0*h11-33/2*b0*b1*c1*c2*h1-17*b0*b1*c2*c2*h0-9/2*b0*b1*c2*c2*h7-9/8*b0*b2*b2*c0*h0-51/4*b0*b2*b2*c0*h7-49/4*b0*b2*b2*c1*h6-2*b0*b2*c0*c0*h10-3/2*b0*b2*c0*c2*h1-33/4*b0*b2*c1*c1*h1-5/2*b0*b2*c1*c2*h0-9*b0*b2*c1*c2*h7-11/2*b0*b2*c2*c2*h6-2*b0*c0*c0*c1*h5-2*b0*c0*c0*c2*h4+18*b0*c1*c2*c2*h1+7*b0*c2*c2*c2*h0-6*b0*c2*c2*c2*h7-3/8*b1*b1*b1*b1*h6-3/8*b1*b1*b1*c0*h1+3/8*b1*b1*b1*c1*h0+15/2*b1*b1*b1*c2*h6-81/4*b1*b1*b2*c0*h7-21/4*b1*b1*b2*c1*h6+15/2*b1*b1*c0*c2*h1-9*b1*b1*c1*c2*h0-9/2*b1*b1*c2*c2*h6-57/4*b1*b2*b2*c0*h6+15*b1*b2*c0*c1*h1-1/2*b1*b2*c0*c2*h0+6*b1*b2*c0*c2*h7+27/4*b1*b2*c1*c1*h0-3*b1*b2*c1*c2*h6+2*b1*c0*c0*c0*h5-9/2*b1*c0*c2*c2*h1+27/2*b1*c1*c2*c2*h0-6*b1*c2*c2*c2*h6+15/2*b2*b2*c0*c0*h1+31/2*b2*b2*c0*c1*h0+3*b2*b2*c0*c1*h7+4*b2*b2*c0*c2*h6+3*b2*b2*c1*c1*h6+2*b2*c0*c0*c0*h4-9*b2*c0*c1*c2*h1-11/2*b2*c0*c2*c2*h0+9*b2*c0*c2*c2*h7-9*b2*c1*c1*c2*h0+9*b2*c1*c2*c2*h6-6*c0*c2*c2*c2*h1-6*c1*c2*c2*c2*h0-2*a0*b0*c0*c1*h8*h11-2*a0*b0*c0*c2*h7*h11-2*a0*b0*c0*c2*h8*h10-2*a0*b0*c1*c1*h7*h11-4*a0*b0*c1*c2*h6*h11-2*a0*b0*c1*c2*h7*h10-2*a0*b0*c2*c2*h6*h10+a0*b1*c0*c0*h8*h11-2*a0*b1*c0*c2*h7*h10-a0*b1*c1*c1*h6*h11-2*a0*b1*c1*c2*h6*h10+a0*b2*c0*c0*h7*h11+a0*b2*c0*c0*h8*h10+2*a0*b2*c0*c1*h7*h10+a0*b2*c1*c1*h6*h10+a0*c0*c0*c1*h2*h11+a0*c0*c0*c1*h5*h8+a0*c0*c0*c2*h1*h11+a0*c0*c0*c2*h2*h10+a0*c0*c0*c2*h4*h8+a0*c0*c0*c2*h5*h7+2*a0*c0*c1*c1*h1*h11+2*a0*c0*c1*c1*h5*h7+4*a0*c0*c1*c2*h0*h11+2*a0*c0*c1*c2*h1*h10+2*a0*c0*c1*c2*h4*h7+4*a0*c0*c1*c2*h5*h6+2*a0*c0*c2*c2*h0*h10+2*a0*c0*c2*c2*h4*h6+a0*c1*c1*c1*h0*h11+a0*c1*c1*c1*h5*h6+a0*c1*c1*c2*h0*h10+a0*c1*c1*c2*h4*h6+a1*b0*c0*c0*h8*h11-2*a1*b0*c0*c2*h7*h10-a1*b0*c1*c1*h6*h11-2*a1*b0*c1*c2*h6*h10+2*a1*b1*c0*c0*h7*h11+2*a1*b1*c0*c1*h6*h11-2*a1*b1*c0*c2*h6*h10+2*a1*b2*c0*c0*h6*h11+a1*b2*c0*c0*h7*h10+2*a1*b2*c0*c1*h6*h10-a1*c0*c0*c0*h2*h11-a1*c0*c0*c0*h5*h8-2*a1*c0*c0*c1*h1*h11-2*a1*c0*c0*c1*h5*h7-2*a1*c0*c0*c2*h0*h11+a1*c0*c0*c2*h1*h10+a1*c0*c0*c2*h4*h7-2*a1*c0*c0*c2*h5*h6-a1*c0*c1*c1*h0*h11-a1*c0*c1*c1*h5*h6+2*a1*c0*c1*c2*h0*h10+2*a1*c0*c1*c2*h4*h6+a2*b0*c0*c0*h7*h11+a2*b0*c0*c0*h8*h10+2*a2*b0*c0*c1*h7*h10+a2*b0*c1*c1*h6*h10+2*a2*b1*c0*c0*h6*h11+a2*b1*c0*c0*h7*h10+2*a2*b1*c0*c1*h6*h10+2*a2*b2*c0*c0*h6*h10-a2*c0*c0*c0*h1*h11-a2*c0*c0*c0*h2*h10-a2*c0*c0*c0*h4*h8-a2*c0*c0*c0*h5*h7-2*a2*c0*c0*c1*h0*h11-3*a2*c0*c0*c1*h1*h10-3*a2*c0*c0*c1*h4*h7-2*a2*c0*c0*c1*h5*h6-2*a2*c0*c0*c2*h0*h10-2*a2*c0*c0*c2*h4*h6-3*a2*c0*c1*c1*h0*h10-3*a2*c0*c1*c1*h4*h6+b0*b0*b0*c1*h8*h11+b0*b0*b0*c2*h7*h11+b0*b0*b0*c2*h8*h10-b0*b0*b1*c0*h8*h11+2*b0*b0*b1*c1*h7*h11+2*b0*b0*b1*c2*h6*h11+3*b0*b0*b1*c2*h7*h10-b0*b0*b2*c0*h7*h11-b0*b0*b2*c0*h8*h10+2*b0*b0*b2*c1*h6*h11-b0*b0*b2*c1*h7*h10+2*b0*b0*b2*c2*h6*h10-b0*b0*c0*c1*h2*h11-b0*b0*c0*c1*h5*h8-b0*b0*c0*c2*h1*h11-b0*b0*c0*c2*h2*h10-b0*b0*c0*c2*h4*h8-b0*b0*c0*c2*h5*h7-b0*b0*c1*c1*h1*h11-b0*b0*c1*c1*h5*h7-2*b0*b0*c1*c2*h0*h11-b0*b0*c1*c2*h1*h10-b0*b0*c1*c2*h4*h7-2*b0*b0*c1*c2*h5*h6-b0*b0*c2*c2*h0*h10-b0*b0*c2*c2*h4*h6-2*b0*b1*b1*c0*h7*h11+b0*b1*b1*c1*h6*h11+3*b0*b1*b1*c2*h6*h10-4*b0*b1*b2*c0*h6*h11-2*b0*b1*b2*c0*h7*h10-2*b0*b1*b2*c1*h6*h10+b0*b1*c0*c0*h2*h11+b0*b1*c0*c0*h5*h8-2*b0*b1*c0*c2*h1*h10-2*b0*b1*c0*c2*h4*h7-b0*b1*c1*c1*h0*h11-b0*b1*c1*c1*h5*h6-2*b0*b1*c1*c2*h0*h10-2*b0*b1*c1*c2*h4*h6-2*b0*b2*b2*c0*h6*h10+b0*b2*c0*c0*h1*h11+b0*b2*c0*c0*h2*h10+b0*b2*c0*c0*h4*h8+b0*b2*c0*c0*h5*h7+2*b0*b2*c0*c1*h1*h10+2*b0*b2*c0*c1*h4*h7+b0*b2*c1*c1*h0*h10+b0*b2*c1*c1*h4*h6+b0*c0*c0*c1*h2*h5+b0*c0*c0*c2*h1*h5+b0*c0*c0*c2*h2*h4+2*b0*c0*c1*c1*h1*h5+4*b0*c0*c1*c2*h0*h5+2*b0*c0*c1*c2*h1*h4+2*b0*c0*c2*c2*h0*h4+b0*c1*c1*c1*h0*h5+b0*c1*c1*c2*h0*h4-b1*b1*b1*c0*h6*h11-b1*b1*b2*c0*h6*h10+b1*b1*c0*c0*h1*h11+b1*b1*c0*c0*h5*h7+b1*b1*c0*c1*h0*h11+b1*b1*c0*c1*h5*h6-b1*b1*c0*c2*h0*h10-b1*b1*c0*c2*h4*h6+2*b1*b2*c0*c0*h0*h11+b1*b2*c0*c0*h1*h10+b1*b2*c0*c0*h4*h7+2*b1*b2*c0*c0*h5*h6+2*b1*b2*c0*c1*h0*h10+2*b1*b2*c0*c1*h4*h6-b1*c0*c0*c0*h2*h5-2*b1*c0*c0*c1*h1*h5-2*b1*c0*c0*c2*h0*h5+b1*c0*c0*c2*h1*h4-b1*c0*c1*c1*h0*h5+2*b1*c0*c1*c2*h0*h4+b2*b2*c0*c0*h0*h10+b2*b2*c0*c0*h4*h6-b2*c0*c0*c0*h1*h5-b2*c0*c0*c0*h2*h4-2*b2*c0*c0*c1*h0*h5-3*b2*c0*c0*c1*h1*h4-2*b2*c0*c0*c2*h0*h4-3*b2*c0*c1*c1*h0*h4,43/8*a0*a0*c0*c0-163/16*a0*b0*b0*c0+109/2*a0*b0*c0*c1+20*a0*b1*c0*c0-115*a0*c0*c0*c2-241/2*a0*c0*c1*c1+77/4*a1*b0*c0*c0-73*a1*c0*c0*c1-19/2*a2*c0*c0*c0+77/32*b0*b0*b0*b0-171/16*b0*b0*b0*c1-293/16*b0*b0*b1*c0+199/4*b0*b0*c0*c2+221/8*b0*b0*c1*c1+231/4*b0*b1*c0*c1+55/8*b0*b2*c0*c0-250*b0*c0*c1*c2-117/2*b0*c1*c1*c1+5/4*b1*b1*c0*c0+37/2*b1*c0*c0*c2-32*b1*c0*c1*c1+55/2*b2*c0*c0*c1+84*c0*c0*c2*c2+276*c0*c1*c1*c2+32*c1*c1*c1*c1-3/2*a0*a0*c0*c2*h7-3/4*a0*a0*c1*c1*h7-3/2*a0*a0*c1*c2*h6-3/2*a0*a1*c0*c1*h7-3*a0*a1*c0*c2*h6-3/2*a0*a1*c1*c1*h6+3/2*a0*b0*b0*c2*h7+9/4*a0*b0*b1*c1*h7+3*a0*b0*b1*c2*h6+3/2*a0*b0*b2*c0*h7+3/2*a0*b0*b2*c1*h6-3*a0*b0*c0*c2*h1-15/8*a0*b0*c1*c1*h1-3*a0*b0*c1*c2*h0-63/2*a0*b0*c1*c2*h7-67/4*a0*b0*c2*c2*h6+3/4*a0*b1*b1*c0*h7+3/2*a0*b1*b1*c1*h6+3/2*a0*b1*b2*c0*h6-3/2*a0*b1*c0*c1*h1-3*a0*b1*c0*c2*h0-3*a0*b1*c0*c2*h7-9/8*a0*b1*c1*c1*h0-33/4*a0*b1*c1*c1*h7-19*a0*b1*c1*c2*h6-3*a0*b2*c0*c1*h7-3*a0*b2*c0*c2*h6+19/4*a0*b2*c1*c1*h6+39*a0*c0*c1*c2*h1+41/2*a0*c0*c2*c2*h0+15*a0*c0*c2*c2*h7+9*a0*c1*c1*c1*h1+27/2*a0*c1*c1*c2*h0+18*a0*c1*c1*c2*h7+18*a0*c1*c2*c2*h6-3/2*a1*a1*c0*c1*h6+3/4*a1*b0*b0*c1*h7+3/2*a1*b0*b0*c2*h6+3/4*a1*b0*b1*c0*h7+3*a1*b0*b1*c1*h6+3/2*a1*b0*b2*c0*h6-3/4*a1*b0*c0*c1*h1-3*a1*b0*c0*c2*h0-3/2*a1*b0*c0*c2*h7-9/8*a1*b0*c1*c1*h0-15/2*a1*b0*c1*c1*h7-19*a1*b0*c1*c2*h6+3/2*a1*b1*b1*c0*h6+3/4*a1*b1*c0*c0*h1-9/4*a1*b1*c0*c1*h0+27/2*a1*b1*c0*c1*h7-17*a1*b1*c0*c2*h6-9/4*a1*b1*c1*c1*h6+27/2*a1*b2*c0*c0*h7+23/2*a1*b2*c0*c1*h6-15*a1*c0*c0*c2*h1-15/2*a1*c0*c1*c1*h1+23*a1*c0*c1*c2*h0-6*a1*c0*c1*c2*h7+14*a1*c0*c2*c2*h6+3/2*a1*c1*c1*c1*h0+12*a1*c1*c1*c2*h6+3/4*a2*b0*c0*c0*h1+3/2*a2*b0*c0*c1*h0-3/2*a2*b0*c0*c1*h7-3/2*a2*b0*c0*c2*h6+11/2*a2*b0*c1*c1*h6+3/4*a2*b1*c0*c0*h0+27/2*a2*b1*c0*c0*h7+13*a2*b1*c0*c1*h6+29/2*a2*b2*c0*c0*h6-15*a2*c0*c0*c1*h1-16*a2*c0*c0*c2*h0-6*a2*c0*c0*c2*h7-23*a2*c0*c1*c1*h0-3*a2*c0*c1*c1*h7-14*a2*c0*c1*c2*h6-3*a2*c1*c1*c1*h6-3/4*b0*b0*b0*b2*h7+3/4*b0*b0*b0*c2*h1-9/8*b0*b0*b1*b1*h7-9/4*b0*b0*b1*b2*h6+3/2*b0*b0*b1*c1*h1+9/4*b0*b0*b1*c2*h0+15*b0*b0*b1*c2*h7+15*b0*b0*b2*c1*h7+16*b0*b0*b2*c2*h6-33/2*b0*b0*c1*c2*h1-35/4*b0*b0*c2*c2*h0-9/2*b0*b0*c2*c2*h7-3/2*b0*b1*b1*b1*h6-3/8*b0*b1*b1*c0*h1+9/8*b0*b1*b1*c1*h0+15/2*b0*b1*b1*c1*h7+23*b0*b1*b1*c2*h6-51/2*b0*b1*b2*c0*h7-19/2*b0*b1*b2*c1*h6-3/2*b0*b1*c0*c2*h1-33/4*b0*b1*c1*c1*h1-19*b0*b1*c1*c2*h0-9*b0*b1*c1*c2*h7-10*b0*b1*c2*c2*h6-55/4*b0*b2*b2*c0*h6-3/2*b0*b2*c0*c1*h1-3/2*b0*b2*c0*c2*h0-3*b0*b2*c0*c2*h7+25/4*b0*b2*c1*c1*h0-9/2*b0*b2*c1*c1*h7-5*b0*b2*c1*c2*h6+27/2*b0*c0*c2*c2*h1+18*b0*c1*c1*c2*h1+33/2*b0*c1*c2*c2*h0-18*b0*c1*c2*c2*h7-6*b0*c2*c2*c2*h6+3/8*b1*b1*b1*c0*h0-27/4*b1*b1*b1*c0*h7+3/4*b1*b1*b1*c1*h6-27/4*b1*b1*b2*c0*h6+15/2*b1*b1*c0*c1*h1-17/2*b1*b1*c0*c2*h0+3*b1*b1*c0*c2*h7-3/4*b1*b1*c1*c1*h0-6*b1*b1*c1*c2*h6+15*b1*b2*c0*c0*h1+29/2*b1*b2*c0*c1*h0+6*b1*b2*c0*c1*h7-b1*b2*c0*c2*h6+3/2*b1*b2*c1*c1*h6-9*b1*c0*c1*c2*h1+25/2*b1*c0*c2*c2*h0+9*b1*c0*c2*c2*h7+9*b1*c1*c1*c2*h0-9*b1*c1*c2*c2*h6+8*b2*b2*c0*c0*h0+3*b2*b2*c0*c0*h7+7*b2*b2*c0*c1*h6-9*b2*c0*c0*c2*h1-9/2*b2*c0*c1*c1*h1-20*b2*c0*c1*c2*h0+18*b2*c0*c1*c2*h7+9*b2*c0*c2*c2*h6-9/2*b2*c1*c1*c1*h0+18*b2*c1*c1*c2*h6-18*c0*c1*c2*c2*h1-6*c0*c2*c2*c2*h0-18*c1*c1*c2*c2*h0-2*a0*b0*c0*c1*h7*h11-2*a0*b0*c0*c2*h6*h11-2*a0*b0*c0*c2*h7*h10-2*a0*b0*c1*c1*h6*h11-2*a0*b0*c1*c2*h6*h10+a0*b1*c0*c0*h7*h11-2*a0*b1*c0*c2*h6*h10+a0*b2*c0*c0*h6*h11+a0*b2*c0*c0*h7*h10+2*a0*b2*c0*c1*h6*h10+a0*c0*c0*c1*h1*h11+a0*c0*c0*c1*h5*h7+a0*c0*c0*c2*h0*h11+a0*c0*c0*c2*h1*h10+a0*c0*c0*c2*h4*h7+a0*c0*c0*c2*h5*h6+2*a0*c0*c1*c1*h0*h11+2*a0*c0*c1*c1*h5*h6+2*a0*c0*c1*c2*h0*h10+2*a0*c0*c1*c2*h4*h6+a1*b0*c0*c0*h7*h11-2*a1*b0*c0*c2*h6*h10+2*a1*b1*c0*c0*h6*h11+a1*b2*c0*c0*h6*h10-a1*c0*c0*c0*h1*h11-a1*c0*c0*c0*h5*h7-2*a1*c0*c0*c1*h0*h11-2*a1*c0*c0*c1*h5*h6+a1*c0*c0*c2*h0*h10+a1*c0*c0*c2*h4*h6+a2*b0*c0*c0*h6*h11+a2*b0*c0*c0*h7*h10+2*a2*b0*c0*c1*h6*h10+a2*b1*c0*c0*h6*h10-a2*c0*c0*c0*h0*h11-a2*c0*c0*c0*h1*h10-a2*c0*c0*c0*h4*h7-a2*c0*c0*c0*h5*h6-3*a2*c0*c0*c1*h0*h10-3*a2*c0*c0*c1*h4*h6+b0*b0*b0*c1*h7*h11+b0*b0*b0*c2*h6*h11+b0*b0*b0*c2*h7*h10-b0*b0*b1*c0*h7*h11+2*b0*b0*b1*c1*h6*h11+3*b0*b0*b1*c2*h6*h10-b0*b0*b2*c0*h6*h11-b0*b0*b2*c0*h7*h10-b0*b0*b2*c1*h6*h10-b0*b0*c0*c1*h1*h11-b0*b0*c0*c1*h5*h7-b0*b0*c0*c2*h0*h11-b0*b0*c0*c2*h1*h10-b0*b0*c0*c2*h4*h7-b0*b0*c0*c2*h5*h6-b0*b0*c1*c1*h0*h11-b0*b0*c1*c1*h5*h6-b0*b0*c1*c2*h0*h10-b0*b0*c1*c2*h4*h6-2*b0*b1*b1*c0*h6*h11-2*b0*b1*b2*c0*h6*h10+b0*b1*c0*c0*h1*h11+b0*b1*c0*c0*h5*h7-2*b0*b1*c0*c2*h0*h10-2*b0*b1*c0*c2*h4*h6+b0*b2*c0*c0*h0*h11+b0*b2*c0*c0*h1*h10+b0*b2*c0*c0*h4*h7+b0*b2*c0*c0*h5*h6+2*b0*b2*c0*c1*h0*h10+2*b0*b2*c0*c1*h4*h6+b0*c0*c0*c1*h1*h5+b0*c0*c0*c2*h0*h5+b0*c0*c0*c2*h1*h4+2*b0*c0*c1*c1*h0*h5+2*b0*c0*c1*c2*h0*h4+b1*b1*c0*c0*h0*h11+b1*b1*c0*c0*h5*h6+b1*b2*c0*c0*h0*h10+b1*b2*c0*c0*h4*h6-b1*c0*c0*c0*h1*h5-2*b1*c0*c0*c1*h0*h5+b1*c0*c0*c2*h0*h4-b2*c0*c0*c0*h0*h5-b2*c0*c0*c0*h1*h4-3*b2*c0*c0*c1*h0*h4,27/64*a0*a0*a1*c2+27/64*a0*a0*a2*c1-9/32*a0*a0*b1*b2+225/32*a0*a0*b2*c2+27/64*a0*a1*a1*c1+27/32*a0*a1*a2*c0-9/16*a0*a1*b0*b2-9/32*a0*a1*b1*b1+237/16*a0*a1*b1*c2+219/16*a0*a1*b2*c1-327/8*a0*a1*c2*c2-9/16*a0*a2*b0*b1+225/16*a0*a2*b0*c2+219/16*a0*a2*b1*c1+201/16*a0*a2*b2*c0-255/4*a0*a2*c1*c2-183/32*a0*b0*b2*b2-195/32*a0*b1*b1*b2+119/8*a0*b1*b2*c2+35/16*a0*b2*b2*c1-51/4*a0*b2*c2*c2+9/64*a1*a1*a1*c0-9/32*a1*a1*b0*b1+237/32*a1*a1*b0*c2+231/32*a1*a1*b1*c1+213/32*a1*a1*b2*c0-265/8*a1*a1*c1*c2-9/32*a1*a2*b0*b0+219/16*a1*a2*b0*c1+213/16*a1*a2*b1*c0-191/4*a1*a2*c0*c2-193/8*a1*a2*c1*c1-201/16*a1*b0*b1*b2+151/8*a1*b0*b2*c2-71/32*a1*b1*b1*b1+155/16*a1*b1*b1*c2+71/8*a1*b1*b2*c1-87/4*a1*b1*c2*c2-17/16*a1*b2*b2*c0-18*a1*b2*c1*c2+247/4*a1*c2*c2*c2+201/32*a2*a2*b0*c0-119/8*a2*a2*c0*c1-207/32*a2*b0*b0*b2-219/32*a2*b0*b1*b1+187/8*a2*b0*b1*c2+103/8*a2*b0*b2*c1-281/8*a2*b0*c2*c2+107/16*a2*b1*b1*c1+19/8*a2*b1*b2*c0-36*a2*b1*c1*c2-5*a2*b2*c0*c2-21/4*a2*b2*c1*c1+669/4*a2*c1*c2*c2-35/2*b2*c2*c2*c2+3/8*a0*a0*b2*c0*h11+3/8*a0*a0*b2*c1*h10+3/8*a0*a0*b2*c2*h9-2*a0*a0*c1*c2*h11-a0*a0*c2*c2*h10+3/4*a0*a1*b2*c0*h10+3/4*a0*a1*b2*c1*h9+3/4*a0*a1*b2*c2*h8-a0*a1*c1*c1*h11-2*a0*a1*c1*c2*h10+3/4*a0*a2*b0*c0*h11+3/4*a0*a2*b0*c1*h10+3/4*a0*a2*b0*c2*h9+3/4*a0*a2*b1*c0*h10+3/4*a0*a2*b1*c1*h9+3/4*a0*a2*b1*c2*h8+3/2*a0*a2*b2*c0*h9+3/2*a0*a2*b2*c1*h8+3/4*a0*a2*b2*c2*h7-3/4*a0*a2*c0*c0*h5-3/2*a0*a2*c0*c1*h4-3/2*a0*a2*c0*c2*h3-3/4*a0*a2*c1*c1*h3+a0*a2*c1*c1*h10-3/2*a0*a2*c1*c2*h2+3/8*a0*a2*c2*c2*h1-3/8*a0*b0*b0*b2*h11-3/4*a0*b0*b1*b2*h10+a0*b0*b1*c2*h11-3/4*a0*b0*b2*b2*h9+3/8*a0*b0*b2*c0*h5+3/8*a0*b0*b2*c1*h4+a0*b0*b2*c1*h11+3/8*a0*b0*b2*c2*h3+a0*b0*b2*c2*h10-2*a0*b0*c1*c2*h5-a0*b0*c2*c2*h4-2*a0*b0*c2*c2*h11-3/8*a0*b1*b1*b2*h9+a0*b1*b1*c2*h10-3/4*a0*b1*b2*b2*h8+3/8*a0*b1*b2*c0*h4-2*a0*b1*b2*c0*h11+3/8*a0*b1*b2*c1*h3-a0*b1*b2*c1*h10+3/8*a0*b1*b2*c2*h2+a0*b1*c0*c2*h5-a0*b1*c1*c2*h4-2*a0*b1*c2*c2*h10-3/8*a0*b2*b2*b2*h7+3/8*a0*b2*b2*c0*h3-a0*b2*b2*c0*h10+3/8*a0*b2*b2*c1*h2+3/8*a0*b2*b2*c2*h1+a0*b2*c0*c1*h5+a0*b2*c0*c2*h4+2*a0*b2*c0*c2*h11+a0*b2*c1*c1*h4+2*a0*b2*c1*c2*h10+4*a0*c0*c2*c2*h5+6*a0*c1*c1*c2*h5+4*a0*c1*c2*c2*h4+3/8*a1*a1*b2*c0*h9+3/8*a1*a1*b2*c1*h8+3/8*a1*a1*b2*c2*h7+a1*a1*c0*c1*h11-a1*a1*c0*c2*h10+3/4*a1*a2*b0*c0*h10+3/4*a1*a2*b0*c1*h9+3/4*a1*a2*b0*c2*h8+3/4*a1*a2*b1*c0*h9+3/4*a1*a2*b1*c1*h8+3/4*a1*a2*b1*c2*h7+3/2*a1*a2*b2*c0*h8+3/2*a1*a2*b2*c1*h7+3/4*a1*a2*b2*c2*h6-3/4*a1*a2*c0*c0*h4+2*a1*a2*c0*c0*h11-3/2*a1*a2*c0*c1*h3+2*a1*a2*c0*c1*h10-3/2*a1*a2*c0*c2*h2-3/4*a1*a2*c1*c1*h2-3/2*a1*a2*c1*c2*h1+3/8*a1*a2*c2*c2*h0-3/8*a1*b0*b0*b2*h10+a1*b0*b0*c2*h11-3/4*a1*b0*b1*b2*h9+a1*b0*b1*c1*h11+2*a1*b0*b1*c2*h10-3/4*a1*b0*b2*b2*h8+3/8*a1*b0*b2*c0*h4-a1*b0*b2*c0*h11+3/8*a1*b0*b2*c1*h3-a1*b0*b2*c1*h10+3/8*a1*b0*b2*c2*h2-a1*b0*c0*c2*h5-a1*b0*c1*c1*h5-a1*b0*c1*c2*h4-4*a1*b0*c1*c2*h11-2*a1*b0*c2*c2*h10-3/8*a1*b1*b1*b2*h8-a1*b1*b1*c0*h11-3/4*a1*b1*b2*b2*h7+3/8*a1*b1*b2*c0*h3-a1*b1*b2*c0*h10+3/8*a1*b1*b2*c1*h2+3/8*a1*b1*b2*c2*h1+a1*b1*c0*c1*h5-a1*b1*c0*c2*h4+2*a1*b1*c0*c2*h11-2*a1*b1*c1*c2*h10-3/8*a1*b2*b2*b2*h6+3/8*a1*b2*b2*c0*h2+3/8*a1*b2*b2*c1*h1+3/8*a1*b2*b2*c2*h0+a1*b2*c0*c0*h5+2*a1*b2*c0*c1*h4+2*a1*b2*c0*c1*h11+2*a1*b2*c0*c2*h10+2*a1*b2*c1*c1*h10-4*a1*c0*c1*c2*h5+4*a1*c0*c2*c2*h4+2*a1*c1*c1*c2*h4+3/4*a2*a2*b0*c0*h9+3/4*a2*a2*b0*c1*h8+3/8*a2*a2*b0*c2*h7+3/4*a2*a2*b1*c0*h8+3/4*a2*a2*b1*c1*h7+3/8*a2*a2*b1*c2*h6+9/8*a2*a2*b2*c0*h7+9/8*a2*a2*b2*c1*h6-3/4*a2*a2*c0*c0*h3+a2*a2*c0*c0*h10-3/2*a2*a2*c0*c1*h2-15/8*a2*a2*c0*c2*h1-3/4*a2*a2*c1*c1*h1-15/8*a2*a2*c1*c2*h0-3/8*a2*b0*b0*b2*h9+a2*b0*b0*c1*h11+a2*b0*b0*c2*h10-3/4*a2*b0*b1*b2*h8-a2*b0*b1*c0*h11-3/8*a2*b0*b2*b2*h7+3/8*a2*b0*b2*c0*h3-a2*b0*b2*c0*h10+3/8*a2*b0*b2*c1*h2-3/8*a2*b0*b2*c2*h1-a2*b0*c0*c1*h5-a2*b0*c0*c2*h4-2*a2*b0*c0*c2*h11-2*a2*b0*c1*c1*h11-2*a2*b0*c1*c2*h10-3/8*a2*b1*b1*b2*h7-3/8*a2*b1*b2*b2*h6+3/8*a2*b1*b2*c0*h2+3/8*a2*b1*b2*c1*h1-3/8*a2*b1*b2*c2*h0+a2*b1*c0*c0*h5+2*a2*b1*c0*c1*h11-2*a2*b1*c0*c2*h10+3/4*a2*b2*b2*c0*h1+3/4*a2*b2*b2*c1*h0+a2*b2*c0*c0*h4+2*a2*b2*c0*c0*h11+4*a2*b2*c0*c1*h10-4*a2*c0*c0*c2*h5-2*a2*c0*c1*c1*h5-8*a2*c0*c1*c2*h4-2*a2*c1*c1*c1*h4+a0*a0*c0*c1*h11*h11+2*a0*a0*c0*c2*h10*h11+a0*a0*c1*c1*h10*h11+2*a0*a0*c1*c2*h9*h11+a0*a0*c1*c2*h10*h10+a0*a0*c2*c2*h8*h11+a0*a0*c2*c2*h9*h10-a0*a1*c0*c0*h11*h11+2*a0*a1*c0*c2*h10*h10+a0*a1*c1*c1*h9*h11+2*a0*a1*c1*c2*h8*h11+2*a0*a1*c1*c2*h9*h10+a0*a1*c2*c2*h7*h11+2*a0*a1*c2*c2*h8*h10-2*a0*a2*c0*c0*h10*h11-2*a0*a2*c0*c1*h10*h10+a0*a2*c1*c1*h8*h11-a0*a2*c1*c1*h9*h10+2*a0*a2*c1*c2*h7*h11+a0*a2*c2*c2*h6*h11+a0*a2*c2*c2*h7*h10-a0*b0*b0*c1*h11*h11-2*a0*b0*b0*c2*h10*h11+a0*b0*b1*c0*h11*h11-a0*b0*b1*c1*h10*h11-a0*b0*b1*c2*h9*h11-2*a0*b0*b1*c2*h10*h10+2*a0*b0*b2*c0*h10*h11-a0*b0*b2*c1*h9*h11+a0*b0*b2*c1*h10*h10-a0*b0*b2*c2*h8*h11-a0*b0*b2*c2*h9*h10+2*a0*b0*c0*c1*h5*h11+2*a0*b0*c0*c2*h4*h11+2*a0*b0*c0*c2*h5*h10+a0*b0*c1*c1*h4*h11+a0*b0*c1*c1*h5*h10+2*a0*b0*c1*c2*h3*h11+2*a0*b0*c1*c2*h4*h10+2*a0*b0*c1*c2*h5*h9+a0*b0*c2*c2*h2*h11+a0*b0*c2*c2*h3*h10+a0*b0*c2*c2*h4*h9+a0*b0*c2*c2*h5*h8+a0*b1*b1*c0*h10*h11-a0*b1*b1*c2*h9*h10+2*a0*b1*b2*c0*h9*h11+a0*b1*b2*c0*h10*h10+a0*b1*b2*c1*h9*h10-a0*b1*b2*c2*h8*h10-2*a0*b1*c0*c0*h5*h11-a0*b1*c0*c1*h4*h11-a0*b1*c0*c1*h5*h10-a0*b1*c0*c2*h3*h11+2*a0*b1*c0*c2*h4*h10-a0*b1*c0*c2*h5*h9+a0*b1*c1*c2*h3*h10+a0*b1*c1*c2*h4*h9+a0*b1*c2*c2*h2*h10+a0*b1*c2*c2*h4*h8+a0*b2*b2*c0*h8*h11+a0*b2*b2*c0*h9*h10+a0*b2*b2*c1*h8*h10-2*a0*b2*c0*c0*h4*h11-2*a0*b2*c0*c0*h5*h10-a0*b2*c0*c1*h3*h11-4*a0*b2*c0*c1*h4*h10-a0*b2*c0*c1*h5*h9-a0*b2*c0*c2*h2*h11-a0*b2*c0*c2*h3*h10-a0*b2*c0*c2*h4*h9-a0*b2*c0*c2*h5*h8-a0*b2*c1*c1*h3*h10-a0*b2*c1*c1*h4*h9-a0*b2*c1*c2*h2*h10-a0*b2*c1*c2*h4*h8-a0*c0*c0*c1*h5*h5-2*a0*c0*c0*c2*h4*h5-2*a0*c0*c1*c1*h4*h5-4*a0*c0*c1*c2*h3*h5-2*a0*c0*c1*c2*h4*h4-2*a0*c0*c2*c2*h2*h5-2*a0*c0*c2*c2*h3*h4-a0*c1*c1*c1*h3*h5-3*a0*c1*c1*c2*h2*h5-a0*c1*c1*c2*h3*h4-3*a0*c1*c2*c2*h1*h5-2*a0*c1*c2*c2*h2*h4-a0*c2*c2*c2*h0*h5-a0*c2*c2*c2*h1*h4-a1*a1*c0*c0*h10*h11-a1*a1*c0*c1*h9*h11-a1*a1*c0*c2*h8*h11+a1*a1*c0*c2*h9*h10+a1*a1*c1*c2*h8*h10+a1*a1*c2*c2*h7*h10-2*a1*a2*c0*c0*h9*h11-a1*a2*c0*c0*h10*h10-2*a1*a2*c0*c1*h8*h11-2*a1*a2*c0*c1*h9*h10-2*a1*a2*c0*c2*h7*h11-a1*a2*c1*c1*h8*h10+a1*a2*c2*c2*h6*h10-a1*b0*b0*c1*h10*h11-a1*b0*b0*c2*h9*h11-a1*b0*b0*c2*h10*h10+a1*b0*b1*c0*h10*h11-a1*b0*b1*c1*h9*h11-a1*b0*b1*c2*h8*h11-2*a1*b0*b1*c2*h9*h10+a1*b0*b2*c0*h9*h11+a1*b0*b2*c0*h10*h10-a1*b0*b2*c1*h8*h11+a1*b0*b2*c1*h9*h10-a1*b0*b2*c2*h7*h11-a1*b0*b2*c2*h8*h10+a1*b0*c0*c1*h4*h11+a1*b0*c0*c1*h5*h10+a1*b0*c0*c2*h3*h11+2*a1*b0*c0*c2*h4*h10+a1*b0*c0*c2*h5*h9+a1*b0*c1*c1*h3*h11+a1*b0*c1*c1*h5*h9+2*a1*b0*c1*c2*h2*h11+a1*b0*c1*c2*h3*h10+a1*b0*c1*c2*h4*h9+2*a1*b0*c1*c2*h5*h8+a1*b0*c2*c2*h1*h11+a1*b0*c2*c2*h2*h10+a1*b0*c2*c2*h4*h8+a1*b0*c2*c2*h5*h7+a1*b1*b1*c0*h9*h11-a1*b1*b1*c2*h8*h10+2*a1*b1*b2*c0*h8*h11+a1*b1*b2*c0*h9*h10+a1*b1*b2*c1*h8*h10-a1*b1*b2*c2*h7*h10-a1*b1*c0*c0*h4*h11-a1*b1*c0*c0*h5*h10-a1*b1*c0*c1*h3*h11-a1*b1*c0*c1*h5*h9-a1*b1*c0*c2*h2*h11+a1*b1*c0*c2*h3*h10+a1*b1*c0*c2*h4*h9-a1*b1*c0*c2*h5*h8+a1*b1*c1*c2*h2*h10+a1*b1*c1*c2*h4*h8+a1*b1*c2*c2*h1*h10+a1*b1*c2*c2*h4*h7+a1*b2*b2*c0*h7*h11+a1*b2*b2*c0*h8*h10+a1*b2*b2*c1*h7*h10-a1*b2*c0*c0*h3*h11-2*a1*b2*c0*c0*h4*h10-a1*b2*c0*c0*h5*h9-a1*b2*c0*c1*h2*h11-2*a1*b2*c0*c1*h3*h10-2*a1*b2*c0*c1*h4*h9-a1*b2*c0*c1*h5*h8-a1*b2*c0*c2*h1*h11-a1*b2*c0*c2*h2*h10-a1*b2*c0*c2*h4*h8-a1*b2*c0*c2*h5*h7-a1*b2*c1*c1*h2*h10-a1*b2*c1*c1*h4*h8-a1*b2*c1*c2*h1*h10-a1*b2*c1*c2*h4*h7+a1*c0*c0*c0*h5*h5+2*a1*c0*c0*c1*h4*h5+2*a1*c0*c0*c2*h3*h5-a1*c0*c0*c2*h4*h4+a1*c0*c1*c1*h3*h5+2*a1*c0*c1*c2*h2*h5-2*a1*c0*c1*c2*h3*h4+a1*c0*c2*c2*h1*h5-2*a1*c0*c2*c2*h2*h4-a1*c1*c1*c2*h2*h4-2*a1*c1*c2*c2*h1*h4-a1*c2*c2*c2*h0*h4-a2*a2*c0*c0*h8*h11-a2*a2*c0*c0*h9*h10-a2*a2*c0*c1*h7*h11-2*a2*a2*c0*c1*h8*h10-a2*a2*c0*c2*h6*h11-a2*a2*c0*c2*h7*h10-a2*a2*c1*c1*h7*h10-a2*a2*c1*c2*h6*h10-a2*b0*b0*c1*h9*h11-a2*b0*b0*c2*h8*h11-a2*b0*b0*c2*h9*h10+a2*b0*b1*c0*h9*h11-a2*b0*b1*c1*h8*h11-a2*b0*b1*c2*h7*h11-2*a2*b0*b1*c2*h8*h10+a2*b0*b2*c0*h8*h11+a2*b0*b2*c0*h9*h10-a2*b0*b2*c1*h7*h11+a2*b0*b2*c1*h8*h10-a2*b0*b2*c2*h6*h11-a2*b0*b2*c2*h7*h10+a2*b0*c0*c1*h3*h11+a2*b0*c0*c1*h5*h9+a2*b0*c0*c2*h2*h11+a2*b0*c0*c2*h3*h10+a2*b0*c0*c2*h4*h9+a2*b0*c0*c2*h5*h8+a2*b0*c1*c1*h2*h11+a2*b0*c1*c1*h5*h8+2*a2*b0*c1*c2*h1*h11+a2*b0*c1*c2*h2*h10+a2*b0*c1*c2*h4*h8+2*a2*b0*c1*c2*h5*h7+a2*b0*c2*c2*h0*h11+a2*b0*c2*c2*h1*h10+a2*b0*c2*c2*h4*h7+a2*b0*c2*c2*h5*h6+a2*b1*b1*c0*h8*h11-a2*b1*b1*c2*h7*h10+2*a2*b1*b2*c0*h7*h11+a2*b1*b2*c0*h8*h10+a2*b1*b2*c1*h7*h10-a2*b1*b2*c2*h6*h10-a2*b1*c0*c0*h3*h11-a2*b1*c0*c0*h5*h9-a2*b1*c0*c1*h2*h11-a2*b1*c0*c1*h5*h8-a2*b1*c0*c2*h1*h11+a2*b1*c0*c2*h2*h10+a2*b1*c0*c2*h4*h8-a2*b1*c0*c2*h5*h7+a2*b1*c1*c2*h1*h10+a2*b1*c1*c2*h4*h7+a2*b1*c2*c2*h0*h10+a2*b1*c2*c2*h4*h6+a2*b2*b2*c0*h6*h11+a2*b2*b2*c0*h7*h10+a2*b2*b2*c1*h6*h10-a2*b2*c0*c0*h2*h11-a2*b2*c0*c0*h3*h10-a2*b2*c0*c0*h4*h9-a2*b2*c0*c0*h5*h8-a2*b2*c0*c1*h1*h11-2*a2*b2*c0*c1*h2*h10-2*a2*b2*c0*c1*h4*h8-a2*b2*c0*c1*h5*h7-a2*b2*c0*c2*h0*h11-a2*b2*c0*c2*h1*h10-a2*b2*c0*c2*h4*h7-a2*b2*c0*c2*h5*h6-a2*b2*c1*c1*h1*h10-a2*b2*c1*c1*h4*h7-a2*b2*c1*c2*h0*h10-a2*b2*c1*c2*h4*h6+2*a2*c0*c0*c0*h4*h5+2*a2*c0*c0*c1*h3*h5+3*a2*c0*c0*c1*h4*h4+2*a2*c0*c0*c2*h2*h5+2*a2*c0*c0*c2*h3*h4+a2*c0*c1*c1*h2*h5+3*a2*c0*c1*c1*h3*h4+2*a2*c0*c1*c2*h1*h5+4*a2*c0*c1*c2*h2*h4+a2*c0*c2*c2*h0*h5+a2*c0*c2*c2*h1*h4+a2*c1*c1*c1*h2*h4+2*a2*c1*c1*c2*h1*h4+a2*c1*c2*c2*h0*h4,9/64*a0*a0*a0*c2+27/64*a0*a0*a1*c1+27/64*a0*a0*a2*c0-9/32*a0*a0*b0*b2-9/64*a0*a0*b1*b1+243/32*a0*a0*b1*c2+225/32*a0*a0*b2*c1-365/16*a0*a0*c2*c2+27/64*a0*a1*a1*c0-9/16*a0*a1*b0*b1+243/16*a0*a1*b0*c2+237/16*a0*a1*b1*c1+219/16*a0*a1*b2*c0-303/4*a0*a1*c1*c2-9/32*a0*a2*b0*b0+225/16*a0*a2*b0*c1+219/16*a0*a2*b1*c0-229/4*a0*a2*c0*c2-231/8*a0*a2*c1*c1-201/16*a0*b0*b1*b2+151/8*a0*b0*b2*c2-71/32*a0*b1*b1*b1+155/16*a0*b1*b1*c2+71/8*a0*b1*b2*c1-87/4*a0*b1*c2*c2-17/16*a0*b2*b2*c0-18*a0*b2*c1*c2+275/4*a0*c2*c2*c2-9/64*a1*a1*b0*b0+237/32*a1*a1*b0*c1+231/32*a1*a1*b1*c0-239/8*a1*a1*c0*c2-241/16*a1*a1*c1*c1+219/16*a1*a2*b0*c0-167/4*a1*a2*c0*c1-207/32*a1*b0*b0*b2-219/32*a1*b0*b1*b1+187/8*a1*b0*b1*c2+103/8*a1*b0*b2*c1-281/8*a1*b0*c2*c2+107/16*a1*b1*b1*c1+19/8*a1*b1*b2*c0-36*a1*b1*c1*c2-5*a1*b2*c0*c2-21/4*a1*b2*c1*c1+741/4*a1*c1*c2*c2-93/16*a2*a2*c0*c0-225/32*a2*b0*b0*b1+219/16*a2*b0*b0*c2+139/8*a2*b0*b1*c1+51/8*a2*b0*b2*c0-251/4*a2*b0*c1*c2+55/16*a2*b1*b1*c0-23*a2*b1*c0*c2-57/4*a2*b1*c1*c1+5/2*a2*b2*c0*c1+467/4*a2*c0*c2*c2+669/4*a2*c1*c1*c2-41/2*b1*c2*c2*c2-105/2*b2*c1*c2*c2+9*c2*c2*c2*c2+3/8*a0*a0*b2*c0*h10+3/8*a0*a0*b2*c1*h9+3/8*a0*a0*b2*c2*h8-a0*a0*c0*c2*h11-a0*a0*c1*c1*h11-a0*a0*c1*c2*h10+3/4*a0*a1*b2*c0*h9+3/4*a0*a1*b2*c1*h8-2*a0*a1*c0*c2*h10+9/8*a0*a1*c2*c2*h1+3/4*a0*a2*b0*c0*h10+3/4*a0*a2*b0*c1*h9+3/4*a0*a2*b0*c2*h8+3/4*a0*a2*b1*c0*h9+3/4*a0*a2*b1*c1*h8+3/2*a0*a2*b2*c0*h8+3/4*a0*a2*b2*c1*h7+3/4*a0*a2*b2*c2*h6-3/4*a0*a2*c0*c0*h4+a0*a2*c0*c0*h11-3/2*a0*a2*c0*c1*h3+2*a0*a2*c0*c1*h10-3/2*a0*a2*c0*c2*h2-3/4*a0*a2*c1*c1*h2+3/4*a0*a2*c1*c2*h1+3/8*a0*a2*c2*c2*h0+33/4*a0*a2*c2*c2*h7-3/8*a0*b0*b0*b2*h10+a0*b0*b0*c2*h11-3/4*a0*b0*b1*b2*h9+a0*b0*b1*c1*h11+2*a0*b0*b1*c2*h10-3/4*a0*b0*b2*b2*h8+3/8*a0*b0*b2*c0*h4-a0*b0*b2*c0*h11+3/8*a0*b0*b2*c1*h3-a0*b0*b2*c1*h10+3/8*a0*b0*b2*c2*h2-a0*b0*c0*c2*h5-a0*b0*c1*c1*h5-a0*b0*c1*c2*h4-4*a0*b0*c1*c2*h11-2*a0*b0*c2*c2*h10-3/8*a0*b1*b1*b2*h8-a0*b1*b1*c0*h11-3/4*a0*b1*b2*b2*h7+3/8*a0*b1*b2*c0*h3-a0*b1*b2*c0*h10+3/8*a0*b1*b2*c1*h2+3/8*a0*b1*b2*c2*h1+a0*b1*c0*c1*h5-a0*b1*c0*c2*h4+2*a0*b1*c0*c2*h11-2*a0*b1*c1*c2*h10-3/8*a0*b2*b2*b2*h6+3/8*a0*b2*b2*c0*h2+3/8*a0*b2*b2*c1*h1+3/8*a0*b2*b2*c2*h0+a0*b2*c0*c0*h5+2*a0*b2*c0*c1*h4+2*a0*b2*c0*c1*h11+2*a0*b2*c0*c2*h10+2*a0*b2*c1*c1*h10+8*a0*c0*c1*c2*h5+4*a0*c0*c2*c2*h4+2*a0*c1*c1*c1*h5+2*a0*c1*c1*c2*h4+3/8*a1*a1*b2*c0*h8+3/8*a1*a1*b2*c1*h7-3/8*a1*a1*b2*c2*h6+a1*a1*c0*c0*h11+9/8*a1*a1*c2*c2*h0+3/4*a1*a2*b0*c0*h9+3/4*a1*a2*b0*c1*h8+3/4*a1*a2*b1*c0*h8+3/4*a1*a2*b1*c1*h7-3/4*a1*a2*b1*c2*h6+3/2*a1*a2*b2*c0*h7+3/4*a1*a2*b2*c1*h6-3/4*a1*a2*c0*c0*h3+a1*a2*c0*c0*h10-3/2*a1*a2*c0*c1*h2-9/4*a1*a2*c0*c2*h1-3/4*a1*a2*c1*c1*h1+33/4*a1*a2*c2*c2*h6-3/8*a1*b0*b0*b2*h9+a1*b0*b0*c1*h11+a1*b0*b0*c2*h10-3/4*a1*b0*b1*b2*h8-a1*b0*b1*c0*h11-3/8*a1*b0*b2*b2*h7+3/8*a1*b0*b2*c0*h3-a1*b0*b2*c0*h10+3/8*a1*b0*b2*c1*h2-3/8*a1*b0*b2*c2*h1-a1*b0*c0*c1*h5-a1*b0*c0*c2*h4-2*a1*b0*c0*c2*h11-2*a1*b0*c1*c1*h11-2*a1*b0*c1*c2*h10-3/8*a1*b1*b1*b2*h7-3/8*a1*b1*b2*b2*h6+3/8*a1*b1*b2*c0*h2+3/8*a1*b1*b2*c1*h1-3/8*a1*b1*b2*c2*h0+a1*b1*c0*c0*h5+2*a1*b1*c0*c1*h11-2*a1*b1*c0*c2*h10+3/4*a1*b2*b2*c0*h1+3/4*a1*b2*b2*c1*h0+a1*b2*c0*c0*h4+2*a1*b2*c0*c0*h11+4*a1*b2*c0*c1*h10-4*a1*c0*c0*c2*h5-2*a1*c0*c1*c1*h5+4*a1*c0*c1*c2*h4+3/4*a2*a2*b0*c0*h8+3/8*a2*a2*b0*c1*h7+3/8*a2*a2*b0*c2*h6+3/4*a2*a2*b1*c0*h7+3/8*a2*a2*b1*c1*h6+9/8*a2*a2*b2*c0*h6-3/4*a2*a2*c0*c0*h2-15/8*a2*a2*c0*c1*h1-15/8*a2*a2*c0*c2*h0-27/4*a2*a2*c0*c2*h7-9/8*a2*a2*c1*c1*h0-27/4*a2*a2*c1*c2*h6-3/8*a2*b0*b0*b2*h8-3/4*a2*b0*b1*c2*h1-3/8*a2*b0*b2*b2*h6+3/8*a2*b0*b2*c0*h2-3/8*a2*b0*b2*c1*h1-3/8*a2*b0*b2*c2*h0-15/2*a2*b0*b2*c2*h7-2*a2*b0*c0*c1*h11-2*a2*b0*c0*c2*h10+33/4*a2*b0*c2*c2*h1+3/8*a2*b1*b1*b2*h6-3/4*a2*b1*b1*c2*h0+9/8*a2*b1*b2*c0*h1+3/8*a2*b1*b2*c1*h0-15/2*a2*b1*b2*c2*h6+2*a2*b1*c0*c0*h11+33/4*a2*b1*c2*c2*h0+3/4*a2*b2*b2*c0*h0+27/4*a2*b2*b2*c0*h7+27/4*a2*b2*b2*c1*h6+2*a2*b2*c0*c0*h10-15/2*a2*b2*c0*c2*h1-15/2*a2*b2*c1*c2*h0-4*a2*c0*c0*c1*h5-4*a2*c0*c0*c2*h4-6*a2*c0*c1*c1*h4+a0*a0*c0*c1*h10*h11+a0*a0*c0*c2*h9*h11+a0*a0*c0*c2*h10*h10+a0*a0*c1*c1*h9*h11+2*a0*a0*c1*c2*h8*h11+a0*a0*c1*c2*h9*h10+a0*a0*c2*c2*h7*h11+a0*a0*c2*c2*h8*h10-a0*a1*c0*c0*h10*h11+2*a0*a1*c0*c2*h9*h10+a0*a1*c1*c1*h8*h11+2*a0*a1*c1*c2*h7*h11+2*a0*a1*c1*c2*h8*h10+a0*a1*c2*c2*h6*h11+2*a0*a1*c2*c2*h7*h10-a0*a2*c0*c0*h9*h11-a0*a2*c0*c0*h10*h10-2*a0*a2*c0*c1*h9*h10+a0*a2*c1*c1*h7*h11-a0*a2*c1*c1*h8*h10+2*a0*a2*c1*c2*h6*h11+a0*a2*c2*c2*h6*h10-a0*b0*b0*c1*h10*h11-a0*b0*b0*c2*h9*h11-a0*b0*b0*c2*h10*h10+a0*b0*b1*c0*h10*h11-a0*b0*b1*c1*h9*h11-a0*b0*b1*c2*h8*h11-2*a0*b0*b1*c2*h9*h10+a0*b0*b2*c0*h9*h11+a0*b0*b2*c0*h10*h10-a0*b0*b2*c1*h8*h11+a0*b0*b2*c1*h9*h10-a0*b0*b2*c2*h7*h11-a0*b0*b2*c2*h8*h10+a0*b0*c0*c1*h4*h11+a0*b0*c0*c1*h5*h10+a0*b0*c0*c2*h3*h11+2*a0*b0*c0*c2*h4*h10+a0*b0*c0*c2*h5*h9+a0*b0*c1*c1*h3*h11+a0*b0*c1*c1*h5*h9+2*a0*b0*c1*c2*h2*h11+a0*b0*c1*c2*h3*h10+a0*b0*c1*c2*h4*h9+2*a0*b0*c1*c2*h5*h8+a0*b0*c2*c2*h1*h11+a0*b0*c2*c2*h2*h10+a0*b0*c2*c2*h4*h8+a0*b0*c2*c2*h5*h7+a0*b1*b1*c0*h9*h11-a0*b1*b1*c2*h8*h10+2*a0*b1*b2*c0*h8*h11+a0*b1*b2*c0*h9*h10+a0*b1*b2*c1*h8*h10-a0*b1*b2*c2*h7*h10-a0*b1*c0*c0*h4*h11-a0*b1*c0*c0*h5*h10-a0*b1*c0*c1*h3*h11-a0*b1*c0*c1*h5*h9-a0*b1*c0*c2*h2*h11+a0*b1*c0*c2*h3*h10+a0*b1*c0*c2*h4*h9-a0*b1*c0*c2*h5*h8+a0*b1*c1*c2*h2*h10+a0*b1*c1*c2*h4*h8+a0*b1*c2*c2*h1*h10+a0*b1*c2*c2*h4*h7+a0*b2*b2*c0*h7*h11+a0*b2*b2*c0*h8*h10+a0*b2*b2*c1*h7*h10-a0*b2*c0*c0*h3*h11-2*a0*b2*c0*c0*h4*h10-a0*b2*c0*c0*h5*h9-a0*b2*c0*c1*h2*h11-2*a0*b2*c0*c1*h3*h10-2*a0*b2*c0*c1*h4*h9-a0*b2*c0*c1*h5*h8-a0*b2*c0*c2*h1*h11-a0*b2*c0*c2*h2*h10-a0*b2*c0*c2*h4*h8-a0*b2*c0*c2*h5*h7-a0*b2*c1*c1*h2*h10-a0*b2*c1*c1*h4*h8-a0*b2*c1*c2*h1*h10-a0*b2*c1*c2*h4*h7-a0*c0*c0*c1*h4*h5-a0*c0*c0*c2*h3*h5-a0*c0*c0*c2*h4*h4-2*a0*c0*c1*c1*h3*h5-4*a0*c0*c1*c2*h2*h5-2*a0*c0*c1*c2*h3*h4-2*a0*c0*c2*c2*h1*h5-2*a0*c0*c2*c2*h2*h4-a0*c1*c1*c1*h2*h5-3*a0*c1*c1*c2*h1*h5-a0*c1*c1*c2*h2*h4-3*a0*c1*c2*c2*h0*h5-2*a0*c1*c2*c2*h1*h4-a0*c2*c2*c2*h0*h4-a1*a1*c0*c0*h9*h11-a1*a1*c0*c1*h8*h11-a1*a1*c0*c2*h7*h11+a1*a1*c0*c2*h8*h10+a1*a1*c1*c2*h7*h10+a1*a1*c2*c2*h6*h10-2*a1*a2*c0*c0*h8*h11-a1*a2*c0*c0*h9*h10-2*a1*a2*c0*c1*h7*h11-2*a1*a2*c0*c1*h8*h10-2*a1*a2*c0*c2*h6*h11-a1*a2*c1*c1*h7*h10-a1*b0*b0*c1*h9*h11-a1*b0*b0*c2*h8*h11-a1*b0*b0*c2*h9*h10+a1*b0*b1*c0*h9*h11-a1*b0*b1*c1*h8*h11-a1*b0*b1*c2*h7*h11-2*a1*b0*b1*c2*h8*h10+a1*b0*b2*c0*h8*h11+a1*b0*b2*c0*h9*h10-a1*b0*b2*c1*h7*h11+a1*b0*b2*c1*h8*h10-a1*b0*b2*c2*h6*h11-a1*b0*b2*c2*h7*h10+a1*b0*c0*c1*h3*h11+a1*b0*c0*c1*h5*h9+a1*b0*c0*c2*h2*h11+a1*b0*c0*c2*h3*h10+a1*b0*c0*c2*h4*h9+a1*b0*c0*c2*h5*h8+a1*b0*c1*c1*h2*h11+a1*b0*c1*c1*h5*h8+2*a1*b0*c1*c2*h1*h11+a1*b0*c1*c2*h2*h10+a1*b0*c1*c2*h4*h8+2*a1*b0*c1*c2*h5*h7+a1*b0*c2*c2*h0*h11+a1*b0*c2*c2*h1*h10+a1*b0*c2*c2*h4*h7+a1*b0*c2*c2*h5*h6+a1*b1*b1*c0*h8*h11-a1*b1*b1*c2*h7*h10+2*a1*b1*b2*c0*h7*h11+a1*b1*b2*c0*h8*h10+a1*b1*b2*c1*h7*h10-a1*b1*b2*c2*h6*h10-a1*b1*c0*c0*h3*h11-a1*b1*c0*c0*h5*h9-a1*b1*c0*c1*h2*h11-a1*b1*c0*c1*h5*h8-a1*b1*c0*c2*h1*h11+a1*b1*c0*c2*h2*h10+a1*b1*c0*c2*h4*h8-a1*b1*c0*c2*h5*h7+a1*b1*c1*c2*h1*h10+a1*b1*c1*c2*h4*h7+a1*b1*c2*c2*h0*h10+a1*b1*c2*c2*h4*h6+a1*b2*b2*c0*h6*h11+a1*b2*b2*c0*h7*h10+a1*b2*b2*c1*h6*h10-a1*b2*c0*c0*h2*h11-a1*b2*c0*c0*h3*h10-a1*b2*c0*c0*h4*h9-a1*b2*c0*c0*h5*h8-a1*b2*c0*c1*h1*h11-2*a1*b2*c0*c1*h2*h10-2*a1*b2*c0*c1*h4*h8-a1*b2*c0*c1*h5*h7-a1*b2*c0*c2*h0*h11-a1*b2*c0*c2*h1*h10-a1*b2*c0*c2*h4*h7-a1*b2*c0*c2*h5*h6-a1*b2*c1*c1*h1*h10-a1*b2*c1*c1*h4*h7-a1*b2*c1*c2*h0*h10-a1*b2*c1*c2*h4*h6+a1*c0*c0*c0*h4*h5+2*a1*c0*c0*c1*h3*h5+2*a1*c0*c0*c2*h2*h5-a1*c0*c0*c2*h3*h4+a1*c0*c1*c1*h2*h5+2*a1*c0*c1*c2*h1*h5-2*a1*c0*c1*c2*h2*h4+a1*c0*c2*c2*h0*h5-2*a1*c0*c2*c2*h1*h4-a1*c1*c1*c2*h1*h4-2*a1*c1*c2*c2*h0*h4-a2*a2*c0*c0*h7*h11-a2*a2*c0*c0*h8*h10-a2*a2*c0*c1*h6*h11-2*a2*a2*c0*c1*h7*h10-a2*a2*c0*c2*h6*h10-a2*a2*c1*c1*h6*h10-a2*b0*b0*c1*h8*h11-a2*b0*b0*c2*h7*h11-a2*b0*b0*c2*h8*h10+a2*b0*b1*c0*h8*h11-a2*b0*b1*c1*h7*h11-a2*b0*b1*c2*h6*h11-2*a2*b0*b1*c2*h7*h10+a2*b0*b2*c0*h7*h11+a2*b0*b2*c0*h8*h10-a2*b0*b2*c1*h6*h11+a2*b0*b2*c1*h7*h10-a2*b0*b2*c2*h6*h10+a2*b0*c0*c1*h2*h11+a2*b0*c0*c1*h5*h8+a2*b0*c0*c2*h1*h11+a2*b0*c0*c2*h2*h10+a2*b0*c0*c2*h4*h8+a2*b0*c0*c2*h5*h7+a2*b0*c1*c1*h1*h11+a2*b0*c1*c1*h5*h7+2*a2*b0*c1*c2*h0*h11+a2*b0*c1*c2*h1*h10+a2*b0*c1*c2*h4*h7+2*a2*b0*c1*c2*h5*h6+a2*b0*c2*c2*h0*h10+a2*b0*c2*c2*h4*h6+a2*b1*b1*c0*h7*h11-a2*b1*b1*c2*h6*h10+2*a2*b1*b2*c0*h6*h11+a2*b1*b2*c0*h7*h10+a2*b1*b2*c1*h6*h10-a2*b1*c0*c0*h2*h11-a2*b1*c0*c0*h5*h8-a2*b1*c0*c1*h1*h11-a2*b1*c0*c1*h5*h7-a2*b1*c0*c2*h0*h11+a2*b1*c0*c2*h1*h10+a2*b1*c0*c2*h4*h7-a2*b1*c0*c2*h5*h6+a2*b1*c1*c2*h0*h10+a2*b1*c1*c2*h4*h6+a2*b2*b2*c0*h6*h10-a2*b2*c0*c0*h1*h11-a2*b2*c0*c0*h2*h10-a2*b2*c0*c0*h4*h8-a2*b2*c0*c0*h5*h7-a2*b2*c0*c1*h0*h11-2*a2*b2*c0*c1*h1*h10-2*a2*b2*c0*c1*h4*h7-a2*b2*c0*c1*h5*h6-a2*b2*c0*c2*h0*h10-a2*b2*c0*c2*h4*h6-a2*b2*c1*c1*h0*h10-a2*b2*c1*c1*h4*h6+a2*c0*c0*c0*h3*h5+a2*c0*c0*c0*h4*h4+2*a2*c0*c0*c1*h2*h5+3*a2*c0*c0*c1*h3*h4+2*a2*c0*c0*c2*h1*h5+2*a2*c0*c0*c2*h2*h4+a2*c0*c1*c1*h1*h5+3*a2*c0*c1*c1*h2*h4+2*a2*c0*c1*c2*h0*h5+4*a2*c0*c1*c2*h1*h4+a2*c0*c2*c2*h0*h4+a2*c1*c1*c1*h1*h4+2*a2*c1*c1*c2*h0*h4,9/64*a0*a0*a0*c1+27/64*a0*a0*a1*c0-9/32*a0*a0*b0*b1+249/32*a0*a0*b0*c2+243/32*a0*a0*b1*c1+225/32*a0*a0*b2*c0-341/8*a0*a0*c1*c2-9/32*a0*a1*b0*b0+243/16*a0*a1*b0*c1+237/16*a0*a1*b1*c0-277/4*a0*a1*c0*c2-279/8*a0*a1*c1*c1+225/16*a0*a2*b0*c0-205/4*a0*a2*c0*c1-207/32*a0*b0*b0*b2-219/32*a0*b0*b1*b1+187/8*a0*b0*b1*c2+103/8*a0*b0*b2*c1-281/8*a0*b0*c2*c2+107/16*a0*b1*b1*c1+19/8*a0*b1*b2*c0-36*a0*b1*c1*c2-5*a0*b2*c0*c2-21/4*a0*b2*c1*c1+825/4*a0*c1*c2*c2+237/32*a1*a1*b0*c0-215/8*a1*a1*c0*c1-141/8*a1*a2*c0*c0-225/32*a1*b0*b0*b1+219/16*a1*b0*b0*c2+139/8*a1*b0*b1*c1+51/8*a1*b0*b2*c0-251/4*a1*b0*c1*c2+55/16*a1*b1*b1*c0-23*a1*b1*c0*c2-57/4*a1*b1*c1*c1+5/2*a1*b2*c0*c1+539/4*a1*c0*c2*c2+741/4*a1*c1*c1*c2-77/32*a2*b0*b0*b0+171/16*a2*b0*b0*c1+87/8*a2*b0*b1*c0-199/4*a2*b0*c0*c2-221/8*a2*b0*c1*c1-31/2*a2*b1*c0*c1+31/4*a2*b2*c0*c0+467/2*a2*c0*c1*c2+223/4*a2*c1*c1*c1-b0*c2*c2*c2-123/2*b1*c1*c2*c2-105/2*b2*c0*c2*c2-105/2*b2*c1*c1*c2+36*c1*c2*c2*c2+3/8*a0*a0*b2*c0*h9+3/8*a0*a0*b2*c1*h8-3/8*a0*a0*b2*c2*h7-a0*a0*c0*c1*h11-a0*a0*c0*c2*h10+9/8*a0*a0*c2*c2*h1-3/4*a0*a1*b1*c2*h7+3/4*a0*a1*b2*c0*h8-3/4*a0*a1*b2*c2*h6+a0*a1*c0*c0*h11+9/4*a0*a1*c1*c2*h1+9/4*a0*a1*c2*c2*h0+33/4*a0*a1*c2*c2*h7+3/4*a0*a2*b0*c0*h9+3/4*a0*a2*b0*c1*h8-3/4*a0*a2*b0*c2*h7+3/4*a0*a2*b1*c0*h8-3/4*a0*a2*b1*c2*h6+3/4*a0*a2*b2*c0*h7+3/4*a0*a2*b2*c1*h6-3/4*a0*a2*c0*c0*h3+a0*a2*c0*c0*h10-3/2*a0*a2*c0*c1*h2+3/8*a0*a2*c1*c1*h1+33/2*a0*a2*c1*c2*h7+35/4*a0*a2*c2*c2*h6-3/8*a0*b0*b0*b2*h9+a0*b0*b0*c1*h11+a0*b0*b0*c2*h10-3/4*a0*b0*b1*b2*h8-a0*b0*b1*c0*h11-3/8*a0*b0*b2*b2*h7+3/8*a0*b0*b2*c0*h3-a0*b0*b2*c0*h10+3/8*a0*b0*b2*c1*h2-3/8*a0*b0*b2*c2*h1-a0*b0*c0*c1*h5-a0*b0*c0*c2*h4-2*a0*b0*c0*c2*h11-2*a0*b0*c1*c1*h11-2*a0*b0*c1*c2*h10-3/8*a0*b1*b1*b2*h7-3/8*a0*b1*b2*b2*h6+3/8*a0*b1*b2*c0*h2+3/8*a0*b1*b2*c1*h1-3/8*a0*b1*b2*c2*h0+a0*b1*c0*c0*h5+2*a0*b1*c0*c1*h11-2*a0*b1*c0*c2*h10+3/4*a0*b2*b2*c0*h1+3/4*a0*b2*b2*c1*h0+a0*b2*c0*c0*h4+2*a0*b2*c0*c0*h11+4*a0*b2*c0*c1*h10+2*a0*c0*c0*c2*h5+4*a0*c0*c1*c1*h5+4*a0*c0*c1*c2*h4-15/2*a0*c2*c2*c2*h1-3/8*a1*a1*b0*c2*h7-9/8*a1*a1*b1*c2*h6+3/8*a1*a1*b2*c0*h7-3/8*a1*a1*b2*c1*h6-3/8*a1*a1*c0*c2*h1+15/8*a1*a1*c1*c2*h0+33/4*a1*a1*c2*c2*h6+3/4*a1*a2*b0*c0*h8-3/4*a1*a2*b0*c2*h6+3/4*a1*a2*b1*c0*h7-3/4*a1*a2*b1*c1*h6+3/4*a1*a2*b2*c0*h6-3/4*a1*a2*c0*c0*h2-9/4*a1*a2*c0*c1*h1-27/2*a1*a2*c0*c2*h7-3/8*a1*a2*c1*c1*h0+3*a1*a2*c1*c2*h6-3/8*a1*b0*b0*b2*h8-3/4*a1*b0*b1*c2*h1-3/8*a1*b0*b2*b2*h6+3/8*a1*b0*b2*c0*h2-3/8*a1*b0*b2*c1*h1-3/8*a1*b0*b2*c2*h0-15/2*a1*b0*b2*c2*h7-2*a1*b0*c0*c1*h11-2*a1*b0*c0*c2*h10+33/4*a1*b0*c2*c2*h1+3/8*a1*b1*b1*b2*h6-3/4*a1*b1*b1*c2*h0+9/8*a1*b1*b2*c0*h1+3/8*a1*b1*b2*c1*h0-15/2*a1*b1*b2*c2*h6+2*a1*b1*c0*c0*h11+33/4*a1*b1*c2*c2*h0+3/4*a1*b2*b2*c0*h0+27/4*a1*b2*b2*c0*h7+27/4*a1*b2*b2*c1*h6+2*a1*b2*c0*c0*h10-15/2*a1*b2*c0*c2*h1-15/2*a1*b2*c1*c2*h0-4*a1*c0*c0*c1*h5+2*a1*c0*c0*c2*h4-15/2*a1*c2*c2*c2*h0+3/8*a2*a2*b0*c0*h7+3/8*a2*a2*b0*c1*h6+3/8*a2*a2*b1*c0*h6-9/8*a2*a2*c0*c0*h1-9/4*a2*a2*c0*c1*h0-27/4*a2*a2*c0*c1*h7-29/4*a2*a2*c0*c2*h6-27/4*a2*a2*c1*c1*h6+3/8*a2*b0*b0*b2*h7-3/4*a2*b0*b0*c2*h1+3/8*a2*b0*b1*b1*h7+3/4*a2*b0*b1*b2*h6-3/4*a2*b0*b1*c1*h1-3/2*a2*b0*b1*c2*h0-15/2*a2*b0*b1*c2*h7+3/8*a2*b0*b2*c0*h1+3/8*a2*b0*b2*c1*h0-15/2*a2*b0*b2*c1*h7-8*a2*b0*b2*c2*h6+33/2*a2*b0*c1*c2*h1+35/4*a2*b0*c2*c2*h0+9/2*a2*b0*c2*c2*h7+3/8*a2*b1*b1*b1*h6+3/8*a2*b1*b1*c0*h1-3/8*a2*b1*b1*c1*h0-15/2*a2*b1*b1*c2*h6+3/8*a2*b1*b2*c0*h0+27/2*a2*b1*b2*c0*h7+6*a2*b1*b2*c1*h6-15/2*a2*b1*c0*c2*h1+9*a2*b1*c1*c2*h0+9/2*a2*b1*c2*c2*h6+29/4*a2*b2*b2*c0*h6-15/2*a2*b2*c0*c1*h1-8*a2*b2*c0*c2*h0-3*a2*b2*c0*c2*h7-15/2*a2*b2*c1*c1*h0-3*a2*b2*c1*c2*h6-2*a2*c0*c0*c0*h5-6*a2*c0*c0*c1*h4+9/2*a2*c0*c2*c2*h1+9/2*a2*c1*c2*c2*h0+a0*a0*c0*c1*h9*h11+a0*a0*c0*c2*h8*h11+a0*a0*c0*c2*h9*h10+a0*a0*c1*c1*h8*h11+2*a0*a0*c1*c2*h7*h11+a0*a0*c1*c2*h8*h10+a0*a0*c2*c2*h6*h11+a0*a0*c2*c2*h7*h10-a0*a1*c0*c0*h9*h11+2*a0*a1*c0*c2*h8*h10+a0*a1*c1*c1*h7*h11+2*a0*a1*c1*c2*h6*h11+2*a0*a1*c1*c2*h7*h10+2*a0*a1*c2*c2*h6*h10-a0*a2*c0*c0*h8*h11-a0*a2*c0*c0*h9*h10-2*a0*a2*c0*c1*h8*h10+a0*a2*c1*c1*h6*h11-a0*a2*c1*c1*h7*h10-a0*b0*b0*c1*h9*h11-a0*b0*b0*c2*h8*h11-a0*b0*b0*c2*h9*h10+a0*b0*b1*c0*h9*h11-a0*b0*b1*c1*h8*h11-a0*b0*b1*c2*h7*h11-2*a0*b0*b1*c2*h8*h10+a0*b0*b2*c0*h8*h11+a0*b0*b2*c0*h9*h10-a0*b0*b2*c1*h7*h11+a0*b0*b2*c1*h8*h10-a0*b0*b2*c2*h6*h11-a0*b0*b2*c2*h7*h10+a0*b0*c0*c1*h3*h11+a0*b0*c0*c1*h5*h9+a0*b0*c0*c2*h2*h11+a0*b0*c0*c2*h3*h10+a0*b0*c0*c2*h4*h9+a0*b0*c0*c2*h5*h8+a0*b0*c1*c1*h2*h11+a0*b0*c1*c1*h5*h8+2*a0*b0*c1*c2*h1*h11+a0*b0*c1*c2*h2*h10+a0*b0*c1*c2*h4*h8+2*a0*b0*c1*c2*h5*h7+a0*b0*c2*c2*h0*h11+a0*b0*c2*c2*h1*h10+a0*b0*c2*c2*h4*h7+a0*b0*c2*c2*h5*h6+a0*b1*b1*c0*h8*h11-a0*b1*b1*c2*h7*h10+2*a0*b1*b2*c0*h7*h11+a0*b1*b2*c0*h8*h10+a0*b1*b2*c1*h7*h10-a0*b1*b2*c2*h6*h10-a0*b1*c0*c0*h3*h11-a0*b1*c0*c0*h5*h9-a0*b1*c0*c1*h2*h11-a0*b1*c0*c1*h5*h8-a0*b1*c0*c2*h1*h11+a0*b1*c0*c2*h2*h10+a0*b1*c0*c2*h4*h8-a0*b1*c0*c2*h5*h7+a0*b1*c1*c2*h1*h10+a0*b1*c1*c2*h4*h7+a0*b1*c2*c2*h0*h10+a0*b1*c2*c2*h4*h6+a0*b2*b2*c0*h6*h11+a0*b2*b2*c0*h7*h10+a0*b2*b2*c1*h6*h10-a0*b2*c0*c0*h2*h11-a0*b2*c0*c0*h3*h10-a0*b2*c0*c0*h4*h9-a0*b2*c0*c0*h5*h8-a0*b2*c0*c1*h1*h11-2*a0*b2*c0*c1*h2*h10-2*a0*b2*c0*c1*h4*h8-a0*b2*c0*c1*h5*h7-a0*b2*c0*c2*h0*h11-a0*b2*c0*c2*h1*h10-a0*b2*c0*c2*h4*h7-a0*b2*c0*c2*h5*h6-a0*b2*c1*c1*h1*h10-a0*b2*c1*c1*h4*h7-a0*b2*c1*c2*h0*h10-a0*b2*c1*c2*h4*h6-a0*c0*c0*c1*h3*h5-a0*c0*c0*c2*h2*h5-a0*c0*c0*c2*h3*h4-2*a0*c0*c1*c1*h2*h5-4*a0*c0*c1*c2*h1*h5-2*a0*c0*c1*c2*h2*h4-2*a0*c0*c2*c2*h0*h5-2*a0*c0*c2*c2*h1*h4-a0*c1*c1*c1*h1*h5-3*a0*c1*c1*c2*h0*h5-a0*c1*c1*c2*h1*h4-2*a0*c1*c2*c2*h0*h4-a1*a1*c0*c0*h8*h11-a1*a1*c0*c1*h7*h11-a1*a1*c0*c2*h6*h11+a1*a1*c0*c2*h7*h10+a1*a1*c1*c2*h6*h10-2*a1*a2*c0*c0*h7*h11-a1*a2*c0*c0*h8*h10-2*a1*a2*c0*c1*h6*h11-2*a1*a2*c0*c1*h7*h10-a1*a2*c1*c1*h6*h10-a1*b0*b0*c1*h8*h11-a1*b0*b0*c2*h7*h11-a1*b0*b0*c2*h8*h10+a1*b0*b1*c0*h8*h11-a1*b0*b1*c1*h7*h11-a1*b0*b1*c2*h6*h11-2*a1*b0*b1*c2*h7*h10+a1*b0*b2*c0*h7*h11+a1*b0*b2*c0*h8*h10-a1*b0*b2*c1*h6*h11+a1*b0*b2*c1*h7*h10-a1*b0*b2*c2*h6*h10+a1*b0*c0*c1*h2*h11+a1*b0*c0*c1*h5*h8+a1*b0*c0*c2*h1*h11+a1*b0*c0*c2*h2*h10+a1*b0*c0*c2*h4*h8+a1*b0*c0*c2*h5*h7+a1*b0*c1*c1*h1*h11+a1*b0*c1*c1*h5*h7+2*a1*b0*c1*c2*h0*h11+a1*b0*c1*c2*h1*h10+a1*b0*c1*c2*h4*h7+2*a1*b0*c1*c2*h5*h6+a1*b0*c2*c2*h0*h10+a1*b0*c2*c2*h4*h6+a1*b1*b1*c0*h7*h11-a1*b1*b1*c2*h6*h10+2*a1*b1*b2*c0*h6*h11+a1*b1*b2*c0*h7*h10+a1*b1*b2*c1*h6*h10-a1*b1*c0*c0*h2*h11-a1*b1*c0*c0*h5*h8-a1*b1*c0*c1*h1*h11-a1*b1*c0*c1*h5*h7-a1*b1*c0*c2*h0*h11+a1*b1*c0*c2*h1*h10+a1*b1*c0*c2*h4*h7-a1*b1*c0*c2*h5*h6+a1*b1*c1*c2*h0*h10+a1*b1*c1*c2*h4*h6+a1*b2*b2*c0*h6*h10-a1*b2*c0*c0*h1*h11-a1*b2*c0*c0*h2*h10-a1*b2*c0*c0*h4*h8-a1*b2*c0*c0*h5*h7-a1*b2*c0*c1*h0*h11-2*a1*b2*c0*c1*h1*h10-2*a1*b2*c0*c1*h4*h7-a1*b2*c0*c1*h5*h6-a1*b2*c0*c2*h0*h10-a1*b2*c0*c2*h4*h6-a1*b2*c1*c1*h0*h10-a1*b2*c1*c1*h4*h6+a1*c0*c0*c0*h3*h5+2*a1*c0*c0*c1*h2*h5+2*a1*c0*c0*c2*h1*h5-a1*c0*c0*c2*h2*h4+a1*c0*c1*c1*h1*h5+2*a1*c0*c1*c2*h0*h5-2*a1*c0*c1*c2*h1*h4-2*a1*c0*c2*c2*h0*h4-a1*c1*c1*c2*h0*h4-a2*a2*c0*c0*h6*h11-a2*a2*c0*c0*h7*h10-2*a2*a2*c0*c1*h6*h10-a2*b0*b0*c1*h7*h11-a2*b0*b0*c2*h6*h11-a2*b0*b0*c2*h7*h10+a2*b0*b1*c0*h7*h11-a2*b0*b1*c1*h6*h11-2*a2*b0*b1*c2*h6*h10+a2*b0*b2*c0*h6*h11+a2*b0*b2*c0*h7*h10+a2*b0*b2*c1*h6*h10+a2*b0*c0*c1*h1*h11+a2*b0*c0*c1*h5*h7+a2*b0*c0*c2*h0*h11+a2*b0*c0*c2*h1*h10+a2*b0*c0*c2*h4*h7+a2*b0*c0*c2*h5*h6+a2*b0*c1*c1*h0*h11+a2*b0*c1*c1*h5*h6+a2*b0*c1*c2*h0*h10+a2*b0*c1*c2*h4*h6+a2*b1*b1*c0*h6*h11+a2*b1*b2*c0*h6*h10-a2*b1*c0*c0*h1*h11-a2*b1*c0*c0*h5*h7-a2*b1*c0*c1*h0*h11-a2*b1*c0*c1*h5*h6+a2*b1*c0*c2*h0*h10+a2*b1*c0*c2*h4*h6-a2*b2*c0*c0*h0*h11-a2*b2*c0*c0*h1*h10-a2*b2*c0*c0*h4*h7-a2*b2*c0*c0*h5*h6-2*a2*b2*c0*c1*h0*h10-2*a2*b2*c0*c1*h4*h6+a2*c0*c0*c0*h2*h5+a2*c0*c0*c0*h3*h4+2*a2*c0*c0*c1*h1*h5+3*a2*c0*c0*c1*h2*h4+2*a2*c0*c0*c2*h0*h5+2*a2*c0*c0*c2*h1*h4+a2*c0*c1*c1*h0*h5+3*a2*c0*c1*c1*h1*h4+4*a2*c0*c1*c2*h0*h4+a2*c1*c1*c1*h0*h4,9/64*a0*a0*a0*c0-9/64*a0*a0*b0*b0+249/32*a0*a0*b0*c1+243/32*a0*a0*b1*c0-315/8*a0*a0*c0*c2-317/16*a0*a0*c1*c1+243/16*a0*a1*b0*c0-253/4*a0*a1*c0*c1-179/8*a0*a2*c0*c0-225/32*a0*b0*b0*b1+219/16*a0*b0*b0*c2+139/8*a0*b0*b1*c1+51/8*a0*b0*b2*c0-251/4*a0*b0*c1*c2+55/16*a0*b1*b1*c0-23*a0*b1*c0*c2-57/4*a0*b1*c1*c1+5/2*a0*b2*c0*c1+623/4*a0*c0*c2*c2+825/4*a0*c1*c1*c2-189/16*a1*a1*c0*c0-77/32*a1*b0*b0*b0+171/16*a1*b0*b0*c1+87/8*a1*b0*b1*c0-199/4*a1*b0*c0*c2-221/8*a1*b0*c1*c1-31/2*a1*b1*c0*c1+31/4*a1*b2*c0*c0+539/2*a1*c0*c1*c2+247/4*a1*c1*c1*c1+119/16*a2*b0*b0*c0-169/4*a2*b0*c0*c1-5/4*a2*b1*c0*c0+265/4*a2*c0*c0*c2+467/4*a2*c0*c1*c1-3*b0*c1*c2*c2-123/2*b1*c0*c2*c2-123/2*b1*c1*c1*c2-105*b2*c0*c1*c2-35/2*b2*c1*c1*c1+18*c0*c2*c2*c2+54*c1*c1*c2*c2-3/4*a0*a0*b1*c2*h7+3/8*a0*a0*b2*c0*h8-3/8*a0*a0*b2*c1*h7-3/8*a0*a0*b2*c2*h6+9/4*a0*a0*c1*c2*h1+9/8*a0*a0*c2*c2*h0+33/4*a0*a0*c2*c2*h7-3/2*a0*a1*b0*c2*h7-3/4*a0*a1*b1*c1*h7-9/4*a0*a1*b1*c2*h6-3/4*a0*a1*b2*c1*h6+3/2*a0*a1*c0*c2*h1+9/8*a0*a1*c1*c1*h1+15/4*a0*a1*c1*c2*h0+33/2*a0*a1*c1*c2*h7+17*a0*a1*c2*c2*h6+3/4*a0*a2*b0*c0*h8-3/4*a0*a2*b0*c1*h7-3/4*a0*a2*b0*c2*h6-3/4*a0*a2*b1*c1*h6+3/4*a0*a2*b2*c0*h6-3/4*a0*a2*c0*c0*h2+3*a0*a2*c0*c2*h7-3/8*a0*a2*c1*c1*h0+33/4*a0*a2*c1*c1*h7+4*a0*a2*c1*c2*h6-3/8*a0*b0*b0*b2*h8-3/4*a0*b0*b1*c2*h1-3/8*a0*b0*b2*b2*h6+3/8*a0*b0*b2*c0*h2-3/8*a0*b0*b2*c1*h1-3/8*a0*b0*b2*c2*h0-15/2*a0*b0*b2*c2*h7-2*a0*b0*c0*c1*h11-2*a0*b0*c0*c2*h10+33/4*a0*b0*c2*c2*h1+3/8*a0*b1*b1*b2*h6-3/4*a0*b1*b1*c2*h0+9/8*a0*b1*b2*c0*h1+3/8*a0*b1*b2*c1*h0-15/2*a0*b1*b2*c2*h6+2*a0*b1*c0*c0*h11+33/4*a0*b1*c2*c2*h0+3/4*a0*b2*b2*c0*h0+27/4*a0*b2*b2*c0*h7+27/4*a0*b2*b2*c1*h6+2*a0*b2*c0*c0*h10-15/2*a0*b2*c0*c2*h1-15/2*a0*b2*c1*c2*h0+2*a0*c0*c0*c1*h5+2*a0*c0*c0*c2*h4-45/2*a0*c1*c2*c2*h1-17/2*a0*c2*c2*c2*h0+3*a0*c2*c2*c2*h7-3/8*a1*a1*b0*c1*h7-9/8*a1*a1*b0*c2*h6-9/8*a1*a1*b1*c1*h6-3/8*a1*a1*b2*c0*h6-3/8*a1*a1*c0*c1*h1+15/8*a1*a1*c0*c2*h0-27/4*a1*a1*c0*c2*h7+3/4*a1*a1*c1*c1*h0+39/4*a1*a1*c1*c2*h6-3/4*a1*a2*b0*c1*h6-3/4*a1*a2*b1*c0*h6-3/2*a1*a2*c0*c0*h1-3/4*a1*a2*c0*c1*h0-27/2*a1*a2*c0*c1*h7+2*a1*a2*c0*c2*h6-21/4*a1*a2*c1*c1*h6+3/8*a1*b0*b0*b2*h7-3/4*a1*b0*b0*c2*h1+3/8*a1*b0*b1*b1*h7+3/4*a1*b0*b1*b2*h6-3/4*a1*b0*b1*c1*h1-3/2*a1*b0*b1*c2*h0-15/2*a1*b0*b1*c2*h7+3/8*a1*b0*b2*c0*h1+3/8*a1*b0*b2*c1*h0-15/2*a1*b0*b2*c1*h7-8*a1*b0*b2*c2*h6+33/2*a1*b0*c1*c2*h1+35/4*a1*b0*c2*c2*h0+9/2*a1*b0*c2*c2*h7+3/8*a1*b1*b1*b1*h6+3/8*a1*b1*b1*c0*h1-3/8*a1*b1*b1*c1*h0-15/2*a1*b1*b1*c2*h6+3/8*a1*b1*b2*c0*h0+27/2*a1*b1*b2*c0*h7+6*a1*b1*b2*c1*h6-15/2*a1*b1*c0*c2*h1+9*a1*b1*c1*c2*h0+9/2*a1*b1*c2*c2*h6+29/4*a1*b2*b2*c0*h6-15/2*a1*b2*c0*c1*h1-8*a1*b2*c0*c2*h0-3*a1*b2*c0*c2*h7-15/2*a1*b2*c1*c1*h0-3*a1*b2*c1*c2*h6-2*a1*c0*c0*c0*h5+9/2*a1*c0*c2*c2*h1-18*a1*c1*c2*c2*h0+3*a1*c2*c2*c2*h6+3/8*a2*a2*b0*c0*h6-9/8*a2*a2*c0*c0*h0-27/4*a2*a2*c0*c0*h7-14*a2*a2*c0*c1*h6+3/4*a2*b0*b0*b1*h7+3/8*a2*b0*b0*b2*h6-3/4*a2*b0*b0*c1*h1-3/4*a2*b0*b0*c2*h0-15/2*a2*b0*b0*c2*h7+9/8*a2*b0*b1*b1*h6-3/4*a2*b0*b1*c1*h0-15/2*a2*b0*b1*c1*h7-31/2*a2*b0*b1*c2*h6+3/8*a2*b0*b2*c0*h0+6*a2*b0*b2*c0*h7+11/2*a2*b0*b2*c1*h6+9*a2*b0*c0*c2*h1+33/4*a2*b0*c1*c1*h1+10*a2*b0*c1*c2*h0+9*a2*b0*c1*c2*h7+11/2*a2*b0*c2*c2*h6-3/8*a2*b1*b1*c0*h0+27/4*a2*b1*b1*c0*h7-3/4*a2*b1*b1*c1*h6+7*a2*b1*b2*c0*h6-15/2*a2*b1*c0*c1*h1+17/2*a2*b1*c0*c2*h0-3*a2*b1*c0*c2*h7+3/4*a2*b1*c1*c1*h0+6*a2*b1*c1*c2*h6-15/2*a2*b2*c0*c0*h1-31/2*a2*b2*c0*c1*h0-3*a2*b2*c0*c1*h7-4*a2*b2*c0*c2*h6-3*a2*b2*c1*c1*h6-2*a2*c0*c0*c0*h4+9*a2*c0*c1*c2*h1+11/2*a2*c0*c2*c2*h0-9*a2*c0*c2*c2*h7+9*a2*c1*c1*c2*h0-9*a2*c1*c2*c2*h6+3*b0*c2*c2*c2*h1+3*b1*c2*c2*c2*h0+a0*a0*c0*c1*h8*h11+a0*a0*c0*c2*h7*h11+a0*a0*c0*c2*h8*h10+a0*a0*c1*c1*h7*h11+2*a0*a0*c1*c2*h6*h11+a0*a0*c1*c2*h7*h10+a0*a0*c2*c2*h6*h10-a0*a1*c0*c0*h8*h11+2*a0*a1*c0*c2*h7*h10+a0*a1*c1*c1*h6*h11+2*a0*a1*c1*c2*h6*h10-a0*a2*c0*c0*h7*h11-a0*a2*c0*c0*h8*h10-2*a0*a2*c0*c1*h7*h10-a0*a2*c1*c1*h6*h10-a0*b0*b0*c1*h8*h11-a0*b0*b0*c2*h7*h11-a0*b0*b0*c2*h8*h10+a0*b0*b1*c0*h8*h11-a0*b0*b1*c1*h7*h11-a0*b0*b1*c2*h6*h11-2*a0*b0*b1*c2*h7*h10+a0*b0*b2*c0*h7*h11+a0*b0*b2*c0*h8*h10-a0*b0*b2*c1*h6*h11+a0*b0*b2*c1*h7*h10-a0*b0*b2*c2*h6*h10+a0*b0*c0*c1*h2*h11+a0*b0*c0*c1*h5*h8+a0*b0*c0*c2*h1*h11+a0*b0*c0*c2*h2*h10+a0*b0*c0*c2*h4*h8+a0*b0*c0*c2*h5*h7+a0*b0*c1*c1*h1*h11+a0*b0*c1*c1*h5*h7+2*a0*b0*c1*c2*h0*h11+a0*b0*c1*c2*h1*h10+a0*b0*c1*c2*h4*h7+2*a0*b0*c1*c2*h5*h6+a0*b0*c2*c2*h0*h10+a0*b0*c2*c2*h4*h6+a0*b1*b1*c0*h7*h11-a0*b1*b1*c2*h6*h10+2*a0*b1*b2*c0*h6*h11+a0*b1*b2*c0*h7*h10+a0*b1*b2*c1*h6*h10-a0*b1*c0*c0*h2*h11-a0*b1*c0*c0*h5*h8-a0*b1*c0*c1*h1*h11-a0*b1*c0*c1*h5*h7-a0*b1*c0*c2*h0*h11+a0*b1*c0*c2*h1*h10+a0*b1*c0*c2*h4*h7-a0*b1*c0*c2*h5*h6+a0*b1*c1*c2*h0*h10+a0*b1*c1*c2*h4*h6+a0*b2*b2*c0*h6*h10-a0*b2*c0*c0*h1*h11-a0*b2*c0*c0*h2*h10-a0*b2*c0*c0*h4*h8-a0*b2*c0*c0*h5*h7-a0*b2*c0*c1*h0*h11-2*a0*b2*c0*c1*h1*h10-2*a0*b2*c0*c1*h4*h7-a0*b2*c0*c1*h5*h6-a0*b2*c0*c2*h0*h10-a0*b2*c0*c2*h4*h6-a0*b2*c1*c1*h0*h10-a0*b2*c1*c1*h4*h6-a0*c0*c0*c1*h2*h5-a0*c0*c0*c2*h1*h5-a0*c0*c0*c2*h2*h4-2*a0*c0*c1*c1*h1*h5-4*a0*c0*c1*c2*h0*h5-2*a0*c0*c1*c2*h1*h4-2*a0*c0*c2*c2*h0*h4-a0*c1*c1*c1*h0*h5-a0*c1*c1*c2*h0*h4-a1*a1*c0*c0*h7*h11-a1*a1*c0*c1*h6*h11+a1*a1*c0*c2*h6*h10-2*a1*a2*c0*c0*h6*h11-a1*a2*c0*c0*h7*h10-2*a1*a2*c0*c1*h6*h10-a1*b0*b0*c1*h7*h11-a1*b0*b0*c2*h6*h11-a1*b0*b0*c2*h7*h10+a1*b0*b1*c0*h7*h11-a1*b0*b1*c1*h6*h11-2*a1*b0*b1*c2*h6*h10+a1*b0*b2*c0*h6*h11+a1*b0*b2*c0*h7*h10+a1*b0*b2*c1*h6*h10+a1*b0*c0*c1*h1*h11+a1*b0*c0*c1*h5*h7+a1*b0*c0*c2*h0*h11+a1*b0*c0*c2*h1*h10+a1*b0*c0*c2*h4*h7+a1*b0*c0*c2*h5*h6+a1*b0*c1*c1*h0*h11+a1*b0*c1*c1*h5*h6+a1*b0*c1*c2*h0*h10+a1*b0*c1*c2*h4*h6+a1*b1*b1*c0*h6*h11+a1*b1*b2*c0*h6*h10-a1*b1*c0*c0*h1*h11-a1*b1*c0*c0*h5*h7-a1*b1*c0*c1*h0*h11-a1*b1*c0*c1*h5*h6+a1*b1*c0*c2*h0*h10+a1*b1*c0*c2*h4*h6-a1*b2*c0*c0*h0*h11-a1*b2*c0*c0*h1*h10-a1*b2*c0*c0*h4*h7-a1*b2*c0*c0*h5*h6-2*a1*b2*c0*c1*h0*h10-2*a1*b2*c0*c1*h4*h6+a1*c0*c0*c0*h2*h5+2*a1*c0*c0*c1*h1*h5+2*a1*c0*c0*c2*h0*h5-a1*c0*c0*c2*h1*h4+a1*c0*c1*c1*h0*h5-2*a1*c0*c1*c2*h0*h4-a2*a2*c0*c0*h6*h10-a2*b0*b0*c1*h6*h11-a2*b0*b0*c2*h6*h10+a2*b0*b1*c0*h6*h11+a2*b0*b2*c0*h6*h10+a2*b0*c0*c1*h0*h11+a2*b0*c0*c1*h5*h6+a2*b0*c0*c2*h0*h10+a2*b0*c0*c2*h4*h6-a2*b1*c0*c0*h0*h11-a2*b1*c0*c0*h5*h6-a2*b2*c0*c0*h0*h10-a2*b2*c0*c0*h4*h6+a2*c0*c0*c0*h1*h5+a2*c0*c0*c0*h2*h4+2*a2*c0*c0*c1*h0*h5+3*a2*c0*c0*c1*h1*h4+2*a2*c0*c0*c2*h0*h4+3*a2*c0*c1*c1*h0*h4,249/32*a0*a0*b0*c0-291/8*a0*a0*c0*c1-227/8*a0*a1*c0*c0-77/32*a0*b0*b0*b0+171/16*a0*b0*b0*c1+87/8*a0*b0*b1*c0-199/4*a0*b0*c0*c2-221/8*a0*b0*c1*c1-31/2*a0*b1*c0*c1+31/4*a0*b2*c0*c0+623/2*a0*c0*c1*c2+275/4*a0*c1*c1*c1+119/16*a1*b0*b0*c0-169/4*a1*b0*c0*c1-5/4*a1*b1*c0*c0+337/4*a1*c0*c0*c2+539/4*a1*c0*c1*c1-117/8*a2*b0*c0*c0+265/4*a2*c0*c0*c1-3*b0*c0*c2*c2-3*b0*c1*c1*c2-123*b1*c0*c1*c2-41/2*b1*c1*c1*c1-105/2*b2*c0*c0*c2-105/2*b2*c0*c1*c1+54*c0*c1*c2*c2+36*c1*c1*c1*c2-9/8*a0*a0*b0*c2*h7-3/4*a0*a0*b1*c1*h7-9/8*a0*a0*b1*c2*h6-3/8*a0*a0*b2*c0*h7-3/8*a0*a0*b2*c1*h6+15/8*a0*a0*c0*c2*h1+9/8*a0*a0*c1*c1*h1+15/8*a0*a0*c1*c2*h0+33/2*a0*a0*c1*c2*h7+35/4*a0*a0*c2*c2*h6-3/2*a0*a1*b0*c1*h7-9/4*a0*a1*b0*c2*h6-3/4*a0*a1*b1*c0*h7-9/4*a0*a1*b1*c1*h6-3/4*a0*a1*b2*c0*h6+3/2*a0*a1*c0*c1*h1+15/4*a0*a1*c0*c2*h0+3*a0*a1*c0*c2*h7+3/2*a0*a1*c1*c1*h0+33/4*a0*a1*c1*c1*h7+41/2*a0*a1*c1*c2*h6-3/4*a0*a2*b0*c0*h7-3/4*a0*a2*b0*c1*h6-3/4*a0*a2*b1*c0*h6-3/8*a0*a2*c0*c0*h1-3/4*a0*a2*c0*c1*h0+3*a0*a2*c0*c1*h7+3*a0*a2*c0*c2*h6-19/4*a0*a2*c1*c1*h6+3/8*a0*b0*b0*b2*h7-3/4*a0*b0*b0*c2*h1+3/8*a0*b0*b1*b1*h7+3/4*a0*b0*b1*b2*h6-3/4*a0*b0*b1*c1*h1-3/2*a0*b0*b1*c2*h0-15/2*a0*b0*b1*c2*h7+3/8*a0*b0*b2*c0*h1+3/8*a0*b0*b2*c1*h0-15/2*a0*b0*b2*c1*h7-8*a0*b0*b2*c2*h6+33/2*a0*b0*c1*c2*h1+35/4*a0*b0*c2*c2*h0+9/2*a0*b0*c2*c2*h7+3/8*a0*b1*b1*b1*h6+3/8*a0*b1*b1*c0*h1-3/8*a0*b1*b1*c1*h0-15/2*a0*b1*b1*c2*h6+3/8*a0*b1*b2*c0*h0+27/2*a0*b1*b2*c0*h7+6*a0*b1*b2*c1*h6-15/2*a0*b1*c0*c2*h1+9*a0*b1*c1*c2*h0+9/2*a0*b1*c2*c2*h6+29/4*a0*b2*b2*c0*h6-15/2*a0*b2*c0*c1*h1-8*a0*b2*c0*c2*h0-3*a0*b2*c0*c2*h7-15/2*a0*b2*c1*c1*h0-3*a0*b2*c1*c2*h6-18*a0*c0*c2*c2*h1-45/2*a0*c1*c1*c2*h1-21*a0*c1*c2*c2*h0+9*a0*c1*c2*c2*h7+3*a0*c2*c2*c2*h6-3/8*a1*a1*b0*c0*h7-9/8*a1*a1*b0*c1*h6-9/8*a1*a1*b1*c0*h6-3/8*a1*a1*c0*c0*h1+3/2*a1*a1*c0*c1*h0-27/4*a1*a1*c0*c1*h7+37/4*a1*a1*c0*c2*h6+3/2*a1*a1*c1*c1*h6-3/4*a1*a2*b0*c0*h6-3/8*a1*a2*c0*c0*h0-27/2*a1*a2*c0*c0*h7-23/2*a1*a2*c0*c1*h6+3/4*a1*b0*b0*b1*h7+3/8*a1*b0*b0*b2*h6-3/4*a1*b0*b0*c1*h1-3/4*a1*b0*b0*c2*h0-15/2*a1*b0*b0*c2*h7+9/8*a1*b0*b1*b1*h6-3/4*a1*b0*b1*c1*h0-15/2*a1*b0*b1*c1*h7-31/2*a1*b0*b1*c2*h6+3/8*a1*b0*b2*c0*h0+6*a1*b0*b2*c0*h7+11/2*a1*b0*b2*c1*h6+9*a1*b0*c0*c2*h1+33/4*a1*b0*c1*c1*h1+10*a1*b0*c1*c2*h0+9*a1*b0*c1*c2*h7+11/2*a1*b0*c2*c2*h6-3/8*a1*b1*b1*c0*h0+27/4*a1*b1*b1*c0*h7-3/4*a1*b1*b1*c1*h6+7*a1*b1*b2*c0*h6-15/2*a1*b1*c0*c1*h1+17/2*a1*b1*c0*c2*h0-3*a1*b1*c0*c2*h7+3/4*a1*b1*c1*c1*h0+6*a1*b1*c1*c2*h6-15/2*a1*b2*c0*c0*h1-31/2*a1*b2*c0*c1*h0-3*a1*b2*c0*c1*h7-4*a1*b2*c0*c2*h6-3*a1*b2*c1*c1*h6+9*a1*c0*c1*c2*h1-17*a1*c0*c2*c2*h0-9*a1*c0*c2*c2*h7-27/2*a1*c1*c1*c2*h0-29/4*a2*a2*c0*c0*h6+3/8*a2*b0*b0*b0*h7+9/8*a2*b0*b0*b1*h6-3/8*a2*b0*b0*c0*h1-3/8*a2*b0*b0*c1*h0-15/2*a2*b0*b0*c1*h7-8*a2*b0*b0*c2*h6-3/4*a2*b0*b1*c0*h0+6*a2*b0*b1*c0*h7-2*a2*b0*b1*c1*h6+13/2*a2*b0*b2*c0*h6+9*a2*b0*c0*c1*h1+19/2*a2*b0*c0*c2*h0+6*a2*b0*c0*c2*h7+5/4*a2*b0*c1*c1*h0+9/2*a2*b0*c1*c1*h7+8*a2*b0*c1*c2*h6-1/4*a2*b1*b1*c0*h6-15/2*a2*b1*c0*c0*h1+a2*b1*c0*c1*h0-3*a2*b1*c0*c1*h7+5*a2*b1*c0*c2*h6+3/2*a2*b1*c1*c1*h6-8*a2*b2*c0*c0*h0-3*a2*b2*c0*c0*h7-7*a2*b2*c0*c1*h6+9*a2*c0*c0*c2*h1+9/2*a2*c0*c1*c1*h1+20*a2*c0*c1*c2*h0-18*a2*c0*c1*c2*h7-9*a2*c0*c2*c2*h6+9/2*a2*c1*c1*c1*h0-18*a2*c1*c1*c2*h6+9*b0*c1*c2*c2*h1+3*b0*c2*c2*c2*h0+9*b1*c1*c2*c2*h0+a0*a0*c0*c1*h7*h11+a0*a0*c0*c2*h6*h11+a0*a0*c0*c2*h7*h10+a0*a0*c1*c1*h6*h11+a0*a0*c1*c2*h6*h10-a0*a1*c0*c0*h7*h11+2*a0*a1*c0*c2*h6*h10-a0*a2*c0*c0*h6*h11-a0*a2*c0*c0*h7*h10-2*a0*a2*c0*c1*h6*h10-a0*b0*b0*c1*h7*h11-a0*b0*b0*c2*h6*h11-a0*b0*b0*c2*h7*h10+a0*b0*b1*c0*h7*h11-a0*b0*b1*c1*h6*h11-2*a0*b0*b1*c2*h6*h10+a0*b0*b2*c0*h6*h11+a0*b0*b2*c0*h7*h10+a0*b0*b2*c1*h6*h10+a0*b0*c0*c1*h1*h11+a0*b0*c0*c1*h5*h7+a0*b0*c0*c2*h0*h11+a0*b0*c0*c2*h1*h10+a0*b0*c0*c2*h4*h7+a0*b0*c0*c2*h5*h6+a0*b0*c1*c1*h0*h11+a0*b0*c1*c1*h5*h6+a0*b0*c1*c2*h0*h10+a0*b0*c1*c2*h4*h6+a0*b1*b1*c0*h6*h11+a0*b1*b2*c0*h6*h10-a0*b1*c0*c0*h1*h11-a0*b1*c0*c0*h5*h7-a0*b1*c0*c1*h0*h11-a0*b1*c0*c1*h5*h6+a0*b1*c0*c2*h0*h10+a0*b1*c0*c2*h4*h6-a0*b2*c0*c0*h0*h11-a0*b2*c0*c0*h1*h10-a0*b2*c0*c0*h4*h7-a0*b2*c0*c0*h5*h6-2*a0*b2*c0*c1*h0*h10-2*a0*b2*c0*c1*h4*h6-a0*c0*c0*c1*h1*h5-a0*c0*c0*c2*h0*h5-a0*c0*c0*c2*h1*h4-2*a0*c0*c1*c1*h0*h5-2*a0*c0*c1*c2*h0*h4-a1*a1*c0*c0*h6*h11-a1*a2*c0*c0*h6*h10-a1*b0*b0*c1*h6*h11-a1*b0*b0*c2*h6*h10+a1*b0*b1*c0*h6*h11+a1*b0*b2*c0*h6*h10+a1*b0*c0*c1*h0*h11+a1*b0*c0*c1*h5*h6+a1*b0*c0*c2*h0*h10+a1*b0*c0*c2*h4*h6-a1*b1*c0*c0*h0*h11-a1*b1*c0*c0*h5*h6-a1*b2*c0*c0*h0*h10-a1*b2*c0*c0*h4*h6+a1*c0*c0*c0*h1*h5+2*a1*c0*c0*c1*h0*h5-a1*c0*c0*c2*h0*h4+a2*c0*c0*c0*h0*h5+a2*c0*c0*c0*h1*h4+3*a2*c0*c0*c1*h0*h4,27/64*a0*a0*a1*b2+27/64*a0*a0*a2*b1-117/8*a0*a0*a2*c2+53/32*a0*a0*b2*b2+27/64*a0*a1*a1*b1-123/8*a0*a1*a1*c2+27/32*a0*a1*a2*b0-57/2*a0*a1*a2*c1+31/4*a0*a1*b1*b2-83/8*a0*a1*b2*c2-105/8*a0*a2*a2*c0+65/8*a0*a2*b0*b2+71/16*a0*a2*b1*b1-155/8*a0*a2*b1*c2-35/8*a0*a2*b2*c1+82*a0*a2*c2*c2+9/64*a1*a1*a1*b0-5*a1*a1*a1*c1-111/8*a1*a1*a2*c0+65/16*a1*a1*b0*b2+71/32*a1*a1*b1*b1-155/16*a1*a1*b1*c2-35/16*a1*a1*b2*c1+81/2*a1*a1*c2*c2+37/4*a1*a2*b0*b1-219/8*a1*a2*b0*c2-107/8*a1*a2*b1*c1+17/8*a1*a2*b2*c0+126*a1*a2*c1*c2-149/4*a1*b2*c2*c2+77/32*a2*a2*b0*b0-171/16*a2*a2*b0*c1-55/16*a2*a2*b1*c0+79/2*a2*a2*c0*c2+45/2*a2*a2*c1*c1-113/4*a2*b1*c2*c2-125/2*a2*b2*c1*c2-26*a2*c2*c2*c2+35/2*b2*b2*c2*c2-3/4*a0*a0*a2*c0*h11-3/4*a0*a0*a2*c1*h10-3/4*a0*a0*a2*c2*h9+3/8*a0*a0*b0*b2*h11+3/8*a0*a0*b1*b2*h10+3/8*a0*a0*b2*b2*h9-3/8*a0*a0*b2*c0*h5-3/8*a0*a0*b2*c1*h4-3/8*a0*a0*b2*c2*h3+2*a0*a0*c1*c2*h5+a0*a0*c2*c2*h4+2*a0*a0*c2*c2*h11-3/2*a0*a1*a2*c0*h10-3/2*a0*a1*a2*c1*h9-3/2*a0*a1*a2*c2*h8+3/4*a0*a1*b0*b2*h10-2*a0*a1*b0*c2*h11+3/4*a0*a1*b1*b2*h9-2*a0*a1*b1*c2*h10+3/4*a0*a1*b2*b2*h8-3/4*a0*a1*b2*c0*h4+2*a0*a1*b2*c0*h11-3/4*a0*a1*b2*c1*h3+2*a0*a1*b2*c1*h10-3/4*a0*a1*b2*c2*h2+a0*a1*c1*c1*h5+2*a0*a1*c1*c2*h4+4*a0*a1*c1*c2*h11+4*a0*a1*c2*c2*h10-3/2*a0*a2*a2*c0*h9-3/2*a0*a2*a2*c1*h8-3/4*a0*a2*a2*c2*h7+3/4*a0*a2*b0*b2*h9-2*a0*a2*b0*c1*h11-2*a0*a2*b0*c2*h10+3/4*a0*a2*b1*b2*h8+2*a0*a2*b1*c0*h11+3/4*a0*a2*b2*b2*h7-3/4*a0*a2*b2*c0*h3+2*a0*a2*b2*c0*h10-3/4*a0*a2*b2*c1*h2-3/4*a0*a2*b2*c2*h1-a0*a2*c1*c1*h4+2*a0*a2*c1*c1*h11-4*a0*b1*c1*c2*h5-4*a0*b2*c0*c2*h5-2*a0*b2*c1*c1*h5-4*a0*b2*c1*c2*h4-3/4*a1*a1*a2*c0*h9-3/4*a1*a1*a2*c1*h8-3/4*a1*a1*a2*c2*h7+3/8*a1*a1*b0*b2*h9-a1*a1*b0*c1*h11-a1*a1*b0*c2*h10+3/8*a1*a1*b1*b2*h8+a1*a1*b1*c0*h11+3/8*a1*a1*b2*b2*h7-3/8*a1*a1*b2*c0*h3+a1*a1*b2*c0*h10-3/8*a1*a1*b2*c1*h2-3/8*a1*a1*b2*c2*h1-a1*a1*c0*c1*h5+a1*a1*c0*c2*h4-2*a1*a1*c0*c2*h11+2*a1*a1*c1*c2*h10-3/2*a1*a2*a2*c0*h8-3/2*a1*a2*a2*c1*h7-3/4*a1*a2*a2*c2*h6+3/4*a1*a2*b0*b2*h8+3/4*a1*a2*b1*b2*h7+3/4*a1*a2*b2*b2*h6-3/4*a1*a2*b2*c0*h2-3/4*a1*a2*b2*c1*h1-3/4*a1*a2*b2*c2*h0-2*a1*a2*c0*c0*h5-2*a1*a2*c0*c1*h4-4*a1*a2*c0*c1*h11-2*a1*a2*c1*c1*h10+4*a1*b0*c1*c2*h5-4*a1*b2*c0*c2*h4-2*a1*b2*c1*c1*h4-3/4*a2*a2*a2*c0*h7-3/4*a2*a2*a2*c1*h6+3/4*a2*a2*b0*c2*h1+3/4*a2*a2*b1*c2*h0-3/4*a2*a2*b2*c0*h1-3/4*a2*a2*b2*c1*h0-a2*a2*c0*c0*h4-2*a2*a2*c0*c0*h11-4*a2*a2*c0*c1*h10+4*a2*b0*c0*c2*h5+2*a2*b0*c1*c1*h5+4*a2*b0*c1*c2*h4+4*a2*b1*c0*c2*h4+2*a2*b1*c1*c1*h4+a0*a0*b0*c1*h11*h11+2*a0*a0*b0*c2*h10*h11-a0*a0*b1*c0*h11*h11+a0*a0*b1*c2*h10*h10-2*a0*a0*b2*c0*h10*h11-a0*a0*b2*c1*h10*h10-2*a0*a0*c0*c1*h5*h11-2*a0*a0*c0*c2*h4*h11-2*a0*a0*c0*c2*h5*h10-a0*a0*c1*c1*h4*h11-a0*a0*c1*c1*h5*h10-2*a0*a0*c1*c2*h3*h11-2*a0*a0*c1*c2*h4*h10-2*a0*a0*c1*c2*h5*h9-a0*a0*c2*c2*h2*h11-a0*a0*c2*c2*h3*h10-a0*a0*c2*c2*h4*h9-a0*a0*c2*c2*h5*h8+2*a0*a1*b0*c1*h10*h11+2*a0*a1*b0*c2*h9*h11+2*a0*a1*b0*c2*h10*h10-2*a0*a1*b1*c0*h10*h11+2*a0*a1*b1*c2*h9*h10-2*a0*a1*b2*c0*h9*h11-2*a0*a1*b2*c0*h10*h10-2*a0*a1*b2*c1*h9*h10+2*a0*a1*c0*c0*h5*h11-4*a0*a1*c0*c2*h4*h10-a0*a1*c1*c1*h3*h11-a0*a1*c1*c1*h5*h9-2*a0*a1*c1*c2*h2*h11-2*a0*a1*c1*c2*h3*h10-2*a0*a1*c1*c2*h4*h9-2*a0*a1*c1*c2*h5*h8-a0*a1*c2*c2*h1*h11-2*a0*a1*c2*c2*h2*h10-2*a0*a1*c2*c2*h4*h8-a0*a1*c2*c2*h5*h7+2*a0*a2*b0*c1*h9*h11+2*a0*a2*b0*c2*h8*h11+2*a0*a2*b0*c2*h9*h10-2*a0*a2*b1*c0*h9*h11+2*a0*a2*b1*c2*h8*h10-2*a0*a2*b2*c0*h8*h11-2*a0*a2*b2*c0*h9*h10-2*a0*a2*b2*c1*h8*h10+2*a0*a2*c0*c0*h4*h11+2*a0*a2*c0*c0*h5*h10+4*a0*a2*c0*c1*h4*h10-a0*a2*c1*c1*h2*h11+a0*a2*c1*c1*h3*h10+a0*a2*c1*c1*h4*h9-a0*a2*c1*c1*h5*h8-2*a0*a2*c1*c2*h1*h11-2*a0*a2*c1*c2*h5*h7-a0*a2*c2*c2*h0*h11-a0*a2*c2*c2*h1*h10-a0*a2*c2*c2*h4*h7-a0*a2*c2*c2*h5*h6+a0*b1*c0*c0*h5*h5+2*a0*b1*c0*c1*h4*h5+2*a0*b1*c0*c2*h3*h5+a0*b1*c1*c1*h3*h5+2*a0*b1*c1*c2*h2*h5+a0*b1*c2*c2*h1*h5+2*a0*b2*c0*c0*h4*h5+2*a0*b2*c0*c1*h3*h5+2*a0*b2*c0*c1*h4*h4+2*a0*b2*c0*c2*h2*h5+2*a0*b2*c0*c2*h3*h4+a0*b2*c1*c1*h2*h5+a0*b2*c1*c1*h3*h4+2*a0*b2*c1*c2*h1*h5+2*a0*b2*c1*c2*h2*h4+a0*b2*c2*c2*h0*h5+a0*b2*c2*c2*h1*h4+a1*a1*b0*c1*h9*h11+a1*a1*b0*c2*h8*h11+a1*a1*b0*c2*h9*h10-a1*a1*b1*c0*h9*h11+a1*a1*b1*c2*h8*h10-a1*a1*b2*c0*h8*h11-a1*a1*b2*c0*h9*h10-a1*a1*b2*c1*h8*h10+a1*a1*c0*c0*h4*h11+a1*a1*c0*c0*h5*h10+a1*a1*c0*c1*h3*h11+a1*a1*c0*c1*h5*h9+a1*a1*c0*c2*h2*h11-a1*a1*c0*c2*h3*h10-a1*a1*c0*c2*h4*h9+a1*a1*c0*c2*h5*h8-a1*a1*c1*c2*h2*h10-a1*a1*c1*c2*h4*h8-a1*a1*c2*c2*h1*h10-a1*a1*c2*c2*h4*h7+2*a1*a2*b0*c1*h8*h11+2*a1*a2*b0*c2*h7*h11+2*a1*a2*b0*c2*h8*h10-2*a1*a2*b1*c0*h8*h11+2*a1*a2*b1*c2*h7*h10-2*a1*a2*b2*c0*h7*h11-2*a1*a2*b2*c0*h8*h10-2*a1*a2*b2*c1*h7*h10+2*a1*a2*c0*c0*h3*h11+2*a1*a2*c0*c0*h4*h10+2*a1*a2*c0*c0*h5*h9+2*a1*a2*c0*c1*h2*h11+2*a1*a2*c0*c1*h3*h10+2*a1*a2*c0*c1*h4*h9+2*a1*a2*c0*c1*h5*h8+2*a1*a2*c0*c2*h1*h11+2*a1*a2*c0*c2*h5*h7+a1*a2*c1*c1*h2*h10+a1*a2*c1*c1*h4*h8-a1*a2*c2*c2*h0*h10-a1*a2*c2*c2*h4*h6-a1*b0*c0*c0*h5*h5-2*a1*b0*c0*c1*h4*h5-2*a1*b0*c0*c2*h3*h5-a1*b0*c1*c1*h3*h5-2*a1*b0*c1*c2*h2*h5-a1*b0*c2*c2*h1*h5+a1*b2*c0*c0*h4*h4+2*a1*b2*c0*c1*h3*h4+2*a1*b2*c0*c2*h2*h4+a1*b2*c1*c1*h2*h4+2*a1*b2*c1*c2*h1*h4+a1*b2*c2*c2*h0*h4+a2*a2*b0*c1*h7*h11+a2*a2*b0*c2*h6*h11+a2*a2*b0*c2*h7*h10-a2*a2*b1*c0*h7*h11+a2*a2*b1*c2*h6*h10-a2*a2*b2*c0*h6*h11-a2*a2*b2*c0*h7*h10-a2*a2*b2*c1*h6*h10+a2*a2*c0*c0*h2*h11+a2*a2*c0*c0*h3*h10+a2*a2*c0*c0*h4*h9+a2*a2*c0*c0*h5*h8+a2*a2*c0*c1*h1*h11+2*a2*a2*c0*c1*h2*h10+2*a2*a2*c0*c1*h4*h8+a2*a2*c0*c1*h5*h7+a2*a2*c0*c2*h0*h11+a2*a2*c0*c2*h1*h10+a2*a2*c0*c2*h4*h7+a2*a2*c0*c2*h5*h6+a2*a2*c1*c1*h1*h10+a2*a2*c1*c1*h4*h7+a2*a2*c1*c2*h0*h10+a2*a2*c1*c2*h4*h6-2*a2*b0*c0*c0*h4*h5-2*a2*b0*c0*c1*h3*h5-2*a2*b0*c0*c1*h4*h4-2*a2*b0*c0*c2*h2*h5-2*a2*b0*c0*c2*h3*h4-a2*b0*c1*c1*h2*h5-a2*b0*c1*c1*h3*h4-2*a2*b0*c1*c2*h1*h5-2*a2*b0*c1*c2*h2*h4-a2*b0*c2*c2*h0*h5-a2*b0*c2*c2*h1*h4-a2*b1*c0*c0*h4*h4-2*a2*b1*c0*c1*h3*h4-2*a2*b1*c0*c2*h2*h4-a2*b1*c1*c1*h2*h4-2*a2*b1*c1*c2*h1*h4-a2*b1*c2*c2*h0*h4,9/64*a0*a0*a0*b2+27/64*a0*a0*a1*b1-63/4*a0*a0*a1*c2+27/64*a0*a0*a2*b0-117/8*a0*a0*a2*c1+31/8*a0*a0*b1*b2-83/16*a0*a0*b2*c2+27/64*a0*a1*a1*b0-123/8*a0*a1*a1*c1-57/2*a0*a1*a2*c0+65/8*a0*a1*b0*b2+71/16*a0*a1*b1*b1-155/8*a0*a1*b1*c2-35/8*a0*a1*b2*c1+185/2*a0*a1*c2*c2+37/4*a0*a2*b0*b1-219/8*a0*a2*b0*c2-107/8*a0*a2*b1*c1+17/8*a0*a2*b2*c0+149*a0*a2*c1*c2-177/4*a0*b2*c2*c2-5*a1*a1*a1*c0+37/8*a1*a1*b0*b1-219/16*a1*a1*b0*c2-107/16*a1*a1*b1*c1+17/16*a1*a1*b2*c0+147/2*a1*a1*c1*c2+77/16*a1*a2*b0*b0-171/8*a1*a2*b0*c1-55/8*a1*a2*b1*c0+100*a1*a2*c0*c2+111/2*a1*a2*c1*c1-137/4*a1*b1*c2*c2-149/2*a1*b2*c1*c2-26*a1*c2*c2*c2-119/16*a2*a2*b0*c0+32*a2*a2*c0*c1+11/4*a2*b0*c2*c2-113/2*a2*b1*c1*c2-125/2*a2*b2*c0*c2-125/4*a2*b2*c1*c1-84*a2*c1*c2*c2+38*b1*b2*c2*c2+35*b2*b2*c1*c2-9*b2*c2*c2*c2-3/4*a0*a0*a2*c0*h10-3/4*a0*a0*a2*c1*h9-3/4*a0*a0*a2*c2*h8+3/8*a0*a0*b0*b2*h10-a0*a0*b0*c2*h11+3/8*a0*a0*b1*b2*h9-a0*a0*b1*c2*h10+3/8*a0*a0*b2*b2*h8-3/8*a0*a0*b2*c0*h4+a0*a0*b2*c0*h11-3/8*a0*a0*b2*c1*h3+a0*a0*b2*c1*h10-3/8*a0*a0*b2*c2*h2+a0*a0*c0*c2*h5+a0*a0*c1*c1*h5+a0*a0*c1*c2*h4+4*a0*a0*c1*c2*h11+2*a0*a0*c2*c2*h10-3/2*a0*a1*a2*c0*h9-3/2*a0*a1*a2*c1*h8+3/4*a0*a1*b0*b2*h9-2*a0*a1*b0*c1*h11-2*a0*a1*b0*c2*h10+3/4*a0*a1*b1*b2*h8+2*a0*a1*b1*c0*h11+3/4*a0*a1*b2*b2*h7-3/4*a0*a1*b2*c0*h3+2*a0*a1*b2*c0*h10-3/4*a0*a1*b2*c1*h2-3/4*a0*a1*b2*c2*h1+2*a0*a1*c0*c2*h4+2*a0*a1*c1*c1*h11+4*a0*a1*c1*c2*h10-3/2*a0*a2*a2*c0*h8-3/4*a0*a2*a2*c1*h7-3/4*a0*a2*a2*c2*h6+3/4*a0*a2*b0*b2*h8+3/4*a0*a2*b1*b2*h7+3/4*a0*a2*b2*b2*h6-3/4*a0*a2*b2*c0*h2-3/4*a0*a2*b2*c1*h1-3/4*a0*a2*b2*c2*h0-a0*a2*c0*c0*h5-2*a0*a2*c0*c1*h4-2*a0*a2*c1*c1*h10-9*a0*a2*c2*c2*h1-4*a0*b1*c0*c2*h5-2*a0*b1*c1*c1*h5-4*a0*b2*c0*c1*h5-4*a0*b2*c0*c2*h4-2*a0*b2*c1*c1*h4-3/4*a1*a1*a2*c0*h8-3/4*a1*a1*a2*c1*h7+3/4*a1*a1*a2*c2*h6+3/8*a1*a1*b0*b2*h8+3/8*a1*a1*b1*b2*h7+3/8*a1*a1*b2*b2*h6-3/8*a1*a1*b2*c0*h2-3/8*a1*a1*b2*c1*h1-3/8*a1*a1*b2*c2*h0-a1*a1*c0*c0*h5-2*a1*a1*c0*c1*h11+2*a1*a1*c0*c2*h10-3/2*a1*a2*a2*c0*h7-3/4*a1*a2*a2*c1*h6+3/2*a1*a2*b0*c2*h1+3/2*a1*a2*b1*c2*h0-3/2*a1*a2*b2*c0*h1-3/2*a1*a2*b2*c1*h0-a1*a2*c0*c0*h4-4*a1*a2*c0*c0*h11-4*a1*a2*c0*c1*h10-9*a1*a2*c2*c2*h0+4*a1*b0*c0*c2*h5+2*a1*b0*c1*c1*h5-4*a1*b2*c0*c1*h4-3/4*a2*a2*a2*c0*h6-3/8*a2*a2*b0*b1*h7+3/4*a2*a2*b0*c1*h1+3/4*a2*a2*b0*c2*h0+15/2*a2*a2*b0*c2*h7-3/8*a2*a2*b1*b1*h6-3/8*a2*a2*b1*c0*h1+3/8*a2*a2*b1*c1*h0+15/2*a2*a2*b1*c2*h6-3/4*a2*a2*b2*c0*h0-27/4*a2*a2*b2*c0*h7-27/4*a2*a2*b2*c1*h6-2*a2*a2*c0*c0*h10+15/2*a2*a2*c0*c2*h1+15/2*a2*a2*c1*c2*h0+4*a2*b0*c0*c1*h5+4*a2*b0*c0*c2*h4+2*a2*b0*c1*c1*h4+4*a2*b1*c0*c1*h4+a0*a0*b0*c1*h10*h11+a0*a0*b0*c2*h9*h11+a0*a0*b0*c2*h10*h10-a0*a0*b1*c0*h10*h11+a0*a0*b1*c2*h9*h10-a0*a0*b2*c0*h9*h11-a0*a0*b2*c0*h10*h10-a0*a0*b2*c1*h9*h10-a0*a0*c0*c1*h4*h11-a0*a0*c0*c1*h5*h10-a0*a0*c0*c2*h3*h11-2*a0*a0*c0*c2*h4*h10-a0*a0*c0*c2*h5*h9-a0*a0*c1*c1*h3*h11-a0*a0*c1*c1*h5*h9-2*a0*a0*c1*c2*h2*h11-a0*a0*c1*c2*h3*h10-a0*a0*c1*c2*h4*h9-2*a0*a0*c1*c2*h5*h8-a0*a0*c2*c2*h1*h11-a0*a0*c2*c2*h2*h10-a0*a0*c2*c2*h4*h8-a0*a0*c2*c2*h5*h7+2*a0*a1*b0*c1*h9*h11+2*a0*a1*b0*c2*h8*h11+2*a0*a1*b0*c2*h9*h10-2*a0*a1*b1*c0*h9*h11+2*a0*a1*b1*c2*h8*h10-2*a0*a1*b2*c0*h8*h11-2*a0*a1*b2*c0*h9*h10-2*a0*a1*b2*c1*h8*h10+a0*a1*c0*c0*h4*h11+a0*a1*c0*c0*h5*h10-2*a0*a1*c0*c2*h3*h10-2*a0*a1*c0*c2*h4*h9-a0*a1*c1*c1*h2*h11-a0*a1*c1*c1*h5*h8-2*a0*a1*c1*c2*h1*h11-2*a0*a1*c1*c2*h2*h10-2*a0*a1*c1*c2*h4*h8-2*a0*a1*c1*c2*h5*h7-a0*a1*c2*c2*h0*h11-2*a0*a1*c2*c2*h1*h10-2*a0*a1*c2*c2*h4*h7-a0*a1*c2*c2*h5*h6+2*a0*a2*b0*c1*h8*h11+2*a0*a2*b0*c2*h7*h11+2*a0*a2*b0*c2*h8*h10-2*a0*a2*b1*c0*h8*h11+2*a0*a2*b1*c2*h7*h10-2*a0*a2*b2*c0*h7*h11-2*a0*a2*b2*c0*h8*h10-2*a0*a2*b2*c1*h7*h10+a0*a2*c0*c0*h3*h11+2*a0*a2*c0*c0*h4*h10+a0*a2*c0*c0*h5*h9+2*a0*a2*c0*c1*h3*h10+2*a0*a2*c0*c1*h4*h9-a0*a2*c1*c1*h1*h11+a0*a2*c1*c1*h2*h10+a0*a2*c1*c1*h4*h8-a0*a2*c1*c1*h5*h7-2*a0*a2*c1*c2*h0*h11-2*a0*a2*c1*c2*h5*h6-a0*a2*c2*c2*h0*h10-a0*a2*c2*c2*h4*h6+a0*b1*c0*c0*h4*h5+2*a0*b1*c0*c1*h3*h5+2*a0*b1*c0*c2*h2*h5+a0*b1*c1*c1*h2*h5+2*a0*b1*c1*c2*h1*h5+a0*b1*c2*c2*h0*h5+a0*b2*c0*c0*h3*h5+a0*b2*c0*c0*h4*h4+2*a0*b2*c0*c1*h2*h5+2*a0*b2*c0*c1*h3*h4+2*a0*b2*c0*c2*h1*h5+2*a0*b2*c0*c2*h2*h4+a0*b2*c1*c1*h1*h5+a0*b2*c1*c1*h2*h4+2*a0*b2*c1*c2*h0*h5+2*a0*b2*c1*c2*h1*h4+a0*b2*c2*c2*h0*h4+a1*a1*b0*c1*h8*h11+a1*a1*b0*c2*h7*h11+a1*a1*b0*c2*h8*h10-a1*a1*b1*c0*h8*h11+a1*a1*b1*c2*h7*h10-a1*a1*b2*c0*h7*h11-a1*a1*b2*c0*h8*h10-a1*a1*b2*c1*h7*h10+a1*a1*c0*c0*h3*h11+a1*a1*c0*c0*h5*h9+a1*a1*c0*c1*h2*h11+a1*a1*c0*c1*h5*h8+a1*a1*c0*c2*h1*h11-a1*a1*c0*c2*h2*h10-a1*a1*c0*c2*h4*h8+a1*a1*c0*c2*h5*h7-a1*a1*c1*c2*h1*h10-a1*a1*c1*c2*h4*h7-a1*a1*c2*c2*h0*h10-a1*a1*c2*c2*h4*h6+2*a1*a2*b0*c1*h7*h11+2*a1*a2*b0*c2*h6*h11+2*a1*a2*b0*c2*h7*h10-2*a1*a2*b1*c0*h7*h11+2*a1*a2*b1*c2*h6*h10-2*a1*a2*b2*c0*h6*h11-2*a1*a2*b2*c0*h7*h10-2*a1*a2*b2*c1*h6*h10+2*a1*a2*c0*c0*h2*h11+a1*a2*c0*c0*h3*h10+a1*a2*c0*c0*h4*h9+2*a1*a2*c0*c0*h5*h8+2*a1*a2*c0*c1*h1*h11+2*a1*a2*c0*c1*h2*h10+2*a1*a2*c0*c1*h4*h8+2*a1*a2*c0*c1*h5*h7+2*a1*a2*c0*c2*h0*h11+2*a1*a2*c0*c2*h5*h6+a1*a2*c1*c1*h1*h10+a1*a2*c1*c1*h4*h7-a1*b0*c0*c0*h4*h5-2*a1*b0*c0*c1*h3*h5-2*a1*b0*c0*c2*h2*h5-a1*b0*c1*c1*h2*h5-2*a1*b0*c1*c2*h1*h5-a1*b0*c2*c2*h0*h5+a1*b2*c0*c0*h3*h4+2*a1*b2*c0*c1*h2*h4+2*a1*b2*c0*c2*h1*h4+a1*b2*c1*c1*h1*h4+2*a1*b2*c1*c2*h0*h4+a2*a2*b0*c1*h6*h11+a2*a2*b0*c2*h6*h10-a2*a2*b1*c0*h6*h11-a2*a2*b2*c0*h6*h10+a2*a2*c0*c0*h1*h11+a2*a2*c0*c0*h2*h10+a2*a2*c0*c0*h4*h8+a2*a2*c0*c0*h5*h7+a2*a2*c0*c1*h0*h11+2*a2*a2*c0*c1*h1*h10+2*a2*a2*c0*c1*h4*h7+a2*a2*c0*c1*h5*h6+a2*a2*c0*c2*h0*h10+a2*a2*c0*c2*h4*h6+a2*a2*c1*c1*h0*h10+a2*a2*c1*c1*h4*h6-a2*b0*c0*c0*h3*h5-a2*b0*c0*c0*h4*h4-2*a2*b0*c0*c1*h2*h5-2*a2*b0*c0*c1*h3*h4-2*a2*b0*c0*c2*h1*h5-2*a2*b0*c0*c2*h2*h4-a2*b0*c1*c1*h1*h5-a2*b0*c1*c1*h2*h4-2*a2*b0*c1*c2*h0*h5-2*a2*b0*c1*c2*h1*h4-a2*b0*c2*c2*h0*h4-a2*b1*c0*c0*h3*h4-2*a2*b1*c0*c1*h2*h4-2*a2*b1*c0*c2*h1*h4-a2*b1*c1*c1*h1*h4-2*a2*b1*c1*c2*h0*h4,9/64*a0*a0*a0*b1-43/8*a0*a0*a0*c2+27/64*a0*a0*a1*b0-63/4*a0*a0*a1*c1-117/8*a0*a0*a2*c0+65/16*a0*a0*b0*b2+71/32*a0*a0*b1*b1-155/16*a0*a0*b1*c2-35/16*a0*a0*b2*c1+52*a0*a0*c2*c2-123/8*a0*a1*a1*c0+37/4*a0*a1*b0*b1-219/8*a0*a1*b0*c2-107/8*a0*a1*b1*c1+17/8*a0*a1*b2*c0+170*a0*a1*c1*c2+77/16*a0*a2*b0*b0-171/8*a0*a2*b0*c1-55/8*a0*a2*b1*c0+123*a0*a2*c0*c2+67*a0*a2*c1*c1-165/4*a0*b1*c2*c2-177/2*a0*b2*c1*c2-26*a0*c2*c2*c2+77/32*a1*a1*b0*b0-171/16*a1*a1*b0*c1-55/16*a1*a1*b1*c0+121/2*a1*a1*c0*c2+33*a1*a1*c1*c1-119/8*a1*a2*b0*c0+85*a1*a2*c0*c1-13/4*a1*b0*c2*c2-137/2*a1*b1*c1*c2-149/2*a1*b2*c0*c2-149/4*a1*b2*c1*c1-84*a1*c1*c2*c2+19/2*a2*a2*c0*c0+11/2*a2*b0*c1*c2-113/2*a2*b1*c0*c2-113/4*a2*b1*c1*c1-125/2*a2*b2*c0*c1-54*a2*c0*c2*c2-90*a2*c1*c1*c2+37/2*b0*b2*c2*c2+41/2*b1*b1*c2*c2+76*b1*b2*c1*c2-9*b1*c2*c2*c2+35*b2*b2*c0*c2+35/2*b2*b2*c1*c1-27*b2*c1*c2*c2-3/4*a0*a0*a2*c0*h9-3/4*a0*a0*a2*c1*h8+3/4*a0*a0*a2*c2*h7+3/8*a0*a0*b0*b2*h9-a0*a0*b0*c1*h11-a0*a0*b0*c2*h10+3/8*a0*a0*b1*b2*h8+a0*a0*b1*c0*h11+3/8*a0*a0*b2*b2*h7-3/8*a0*a0*b2*c0*h3+a0*a0*b2*c0*h10-3/8*a0*a0*b2*c1*h2-3/8*a0*a0*b2*c2*h1+a0*a0*c0*c1*h5+a0*a0*c0*c2*h4+2*a0*a0*c0*c2*h11+2*a0*a0*c1*c1*h11+2*a0*a0*c1*c2*h10+3/4*a0*a1*a1*c2*h7-3/2*a0*a1*a2*c0*h8+3/2*a0*a1*a2*c2*h6+3/4*a0*a1*b0*b2*h8+3/4*a0*a1*b1*b2*h7+3/4*a0*a1*b2*b2*h6-3/4*a0*a1*b2*c0*h2-3/4*a0*a1*b2*c1*h1-3/4*a0*a1*b2*c2*h0-a0*a1*c0*c0*h5+4*a0*a1*c0*c2*h10-9*a0*a1*c2*c2*h1-3/4*a0*a2*a2*c0*h7-3/4*a0*a2*a2*c1*h6+3/2*a0*a2*b0*c2*h1+3/2*a0*a2*b1*c2*h0-3/2*a0*a2*b2*c0*h1-3/2*a0*a2*b2*c1*h0-a0*a2*c0*c0*h4-2*a0*a2*c0*c0*h11-4*a0*a2*c0*c1*h10-18*a0*a2*c1*c2*h1-19/2*a0*a2*c2*c2*h0-6*a0*a2*c2*c2*h7-4*a0*b1*c0*c1*h5-2*a0*b2*c0*c0*h5-4*a0*b2*c0*c1*h4+15/2*a0*b2*c2*c2*h1+3/4*a1*a1*a1*c2*h6-3/4*a1*a1*a2*c0*h7+3/4*a1*a1*a2*c1*h6+3/4*a1*a1*b0*c2*h1+3/4*a1*a1*b1*c2*h0-3/4*a1*a1*b2*c0*h1-3/4*a1*a1*b2*c1*h0-2*a1*a1*c0*c0*h11-9*a1*a1*c2*c2*h0-3/4*a1*a2*a2*c0*h6-3/4*a1*a2*b0*b1*h7+3/2*a1*a2*b0*c1*h1+3/2*a1*a2*b0*c2*h0+15*a1*a2*b0*c2*h7-3/4*a1*a2*b1*b1*h6-3/4*a1*a2*b1*c0*h1+3/4*a1*a2*b1*c1*h0+15*a1*a2*b1*c2*h6-3/2*a1*a2*b2*c0*h0-27/2*a1*a2*b2*c0*h7-27/2*a1*a2*b2*c1*h6-2*a1*a2*c0*c0*h10+15*a1*a2*c0*c2*h1-3*a1*a2*c1*c2*h0-6*a1*a2*c2*c2*h6+4*a1*b0*c0*c1*h5-2*a1*b2*c0*c0*h4+15/2*a1*b2*c2*c2*h0-3/8*a2*a2*b0*b0*h7-3/4*a2*a2*b0*b1*h6+3/8*a2*a2*b0*c0*h1+3/8*a2*a2*b0*c1*h0+15/2*a2*a2*b0*c1*h7+8*a2*a2*b0*c2*h6+3/8*a2*a2*b1*c0*h0-27/4*a2*a2*b1*c0*h7+3/4*a2*a2*b1*c1*h6-29/4*a2*a2*b2*c0*h6+15/2*a2*a2*c0*c1*h1+8*a2*a2*c0*c2*h0+3*a2*a2*c0*c2*h7+15/2*a2*a2*c1*c1*h0+3*a2*a2*c1*c2*h6+2*a2*b0*c0*c0*h5+4*a2*b0*c0*c1*h4-6*a2*b0*c2*c2*h1+2*a2*b1*c0*c0*h4-6*a2*b1*c2*c2*h0+a0*a0*b0*c1*h9*h11+a0*a0*b0*c2*h8*h11+a0*a0*b0*c2*h9*h10-a0*a0*b1*c0*h9*h11+a0*a0*b1*c2*h8*h10-a0*a0*b2*c0*h8*h11-a0*a0*b2*c0*h9*h10-a0*a0*b2*c1*h8*h10-a0*a0*c0*c1*h3*h11-a0*a0*c0*c1*h5*h9-a0*a0*c0*c2*h2*h11-a0*a0*c0*c2*h3*h10-a0*a0*c0*c2*h4*h9-a0*a0*c0*c2*h5*h8-a0*a0*c1*c1*h2*h11-a0*a0*c1*c1*h5*h8-2*a0*a0*c1*c2*h1*h11-a0*a0*c1*c2*h2*h10-a0*a0*c1*c2*h4*h8-2*a0*a0*c1*c2*h5*h7-a0*a0*c2*c2*h0*h11-a0*a0*c2*c2*h1*h10-a0*a0*c2*c2*h4*h7-a0*a0*c2*c2*h5*h6+2*a0*a1*b0*c1*h8*h11+2*a0*a1*b0*c2*h7*h11+2*a0*a1*b0*c2*h8*h10-2*a0*a1*b1*c0*h8*h11+2*a0*a1*b1*c2*h7*h10-2*a0*a1*b2*c0*h7*h11-2*a0*a1*b2*c0*h8*h10-2*a0*a1*b2*c1*h7*h10+a0*a1*c0*c0*h3*h11+a0*a1*c0*c0*h5*h9-2*a0*a1*c0*c2*h2*h10-2*a0*a1*c0*c2*h4*h8-a0*a1*c1*c1*h1*h11-a0*a1*c1*c1*h5*h7-2*a0*a1*c1*c2*h0*h11-2*a0*a1*c1*c2*h1*h10-2*a0*a1*c1*c2*h4*h7-2*a0*a1*c1*c2*h5*h6-2*a0*a1*c2*c2*h0*h10-2*a0*a1*c2*c2*h4*h6+2*a0*a2*b0*c1*h7*h11+2*a0*a2*b0*c2*h6*h11+2*a0*a2*b0*c2*h7*h10-2*a0*a2*b1*c0*h7*h11+2*a0*a2*b1*c2*h6*h10-2*a0*a2*b2*c0*h6*h11-2*a0*a2*b2*c0*h7*h10-2*a0*a2*b2*c1*h6*h10+a0*a2*c0*c0*h2*h11+a0*a2*c0*c0*h3*h10+a0*a2*c0*c0*h4*h9+a0*a2*c0*c0*h5*h8+2*a0*a2*c0*c1*h2*h10+2*a0*a2*c0*c1*h4*h8-a0*a2*c1*c1*h0*h11+a0*a2*c1*c1*h1*h10+a0*a2*c1*c1*h4*h7-a0*a2*c1*c1*h5*h6+a0*b1*c0*c0*h3*h5+2*a0*b1*c0*c1*h2*h5+2*a0*b1*c0*c2*h1*h5+a0*b1*c1*c1*h1*h5+2*a0*b1*c1*c2*h0*h5+a0*b2*c0*c0*h2*h5+a0*b2*c0*c0*h3*h4+2*a0*b2*c0*c1*h1*h5+2*a0*b2*c0*c1*h2*h4+2*a0*b2*c0*c2*h0*h5+2*a0*b2*c0*c2*h1*h4+a0*b2*c1*c1*h0*h5+a0*b2*c1*c1*h1*h4+2*a0*b2*c1*c2*h0*h4+a1*a1*b0*c1*h7*h11+a1*a1*b0*c2*h6*h11+a1*a1*b0*c2*h7*h10-a1*a1*b1*c0*h7*h11+a1*a1*b1*c2*h6*h10-a1*a1*b2*c0*h6*h11-a1*a1*b2*c0*h7*h10-a1*a1*b2*c1*h6*h10+a1*a1*c0*c0*h2*h11+a1*a1*c0*c0*h5*h8+a1*a1*c0*c1*h1*h11+a1*a1*c0*c1*h5*h7+a1*a1*c0*c2*h0*h11-a1*a1*c0*c2*h1*h10-a1*a1*c0*c2*h4*h7+a1*a1*c0*c2*h5*h6-a1*a1*c1*c2*h0*h10-a1*a1*c1*c2*h4*h6+2*a1*a2*b0*c1*h6*h11+2*a1*a2*b0*c2*h6*h10-2*a1*a2*b1*c0*h6*h11-2*a1*a2*b2*c0*h6*h10+2*a1*a2*c0*c0*h1*h11+a1*a2*c0*c0*h2*h10+a1*a2*c0*c0*h4*h8+2*a1*a2*c0*c0*h5*h7+2*a1*a2*c0*c1*h0*h11+2*a1*a2*c0*c1*h1*h10+2*a1*a2*c0*c1*h4*h7+2*a1*a2*c0*c1*h5*h6+a1*a2*c1*c1*h0*h10+a1*a2*c1*c1*h4*h6-a1*b0*c0*c0*h3*h5-2*a1*b0*c0*c1*h2*h5-2*a1*b0*c0*c2*h1*h5-a1*b0*c1*c1*h1*h5-2*a1*b0*c1*c2*h0*h5+a1*b2*c0*c0*h2*h4+2*a1*b2*c0*c1*h1*h4+2*a1*b2*c0*c2*h0*h4+a1*b2*c1*c1*h0*h4+a2*a2*c0*c0*h0*h11+a2*a2*c0*c0*h1*h10+a2*a2*c0*c0*h4*h7+a2*a2*c0*c0*h5*h6+2*a2*a2*c0*c1*h0*h10+2*a2*a2*c0*c1*h4*h6-a2*b0*c0*c0*h2*h5-a2*b0*c0*c0*h3*h4-2*a2*b0*c0*c1*h1*h5-2*a2*b0*c0*c1*h2*h4-2*a2*b0*c0*c2*h0*h5-2*a2*b0*c0*c2*h1*h4-a2*b0*c1*c1*h0*h5-a2*b0*c1*c1*h1*h4-2*a2*b0*c1*c2*h0*h4-a2*b1*c0*c0*h2*h4-2*a2*b1*c0*c1*h1*h4-2*a2*b1*c0*c2*h0*h4-a2*b1*c1*c1*h0*h4,9/64*a0*a0*a0*b0-43/8*a0*a0*a0*c1-63/4*a0*a0*a1*c0+37/8*a0*a0*b0*b1-219/16*a0*a0*b0*c2-107/16*a0*a0*b1*c1+17/16*a0*a0*b2*c0+193/2*a0*a0*c1*c2+77/16*a0*a1*b0*b0-171/8*a0*a1*b0*c1-55/8*a0*a1*b1*c0+144*a0*a1*c0*c2+155/2*a0*a1*c1*c1-119/8*a0*a2*b0*c0+108*a0*a2*c0*c1-41/4*a0*b0*c2*c2-165/2*a0*b1*c1*c2-177/2*a0*b2*c0*c2-177/4*a0*b2*c1*c1-84*a0*c1*c2*c2-119/16*a1*a1*b0*c0+53*a1*a1*c0*c1+59/2*a1*a2*c0*c0-13/2*a1*b0*c1*c2-137/2*a1*b1*c0*c2-137/4*a1*b1*c1*c1-149/2*a1*b2*c0*c1-54*a1*c0*c2*c2-90*a1*c1*c1*c2+11/2*a2*b0*c0*c2+11/4*a2*b0*c1*c1-113/2*a2*b1*c0*c1-125/4*a2*b2*c0*c0-120*a2*c0*c1*c2-32*a2*c1*c1*c1+43/2*b0*b1*c2*c2+37*b0*b2*c1*c2-9*b0*c2*c2*c2+41*b1*b1*c1*c2+76*b1*b2*c0*c2+38*b1*b2*c1*c1-27*b1*c1*c2*c2+35*b2*b2*c0*c1-9*b2*c0*c2*c2-27*b2*c1*c1*c2+3/2*a0*a0*a1*c2*h7-3/4*a0*a0*a2*c0*h8+3/4*a0*a0*a2*c1*h7+3/4*a0*a0*a2*c2*h6+3/8*a0*a0*b0*b2*h8+3/8*a0*a0*b1*b2*h7+3/8*a0*a0*b2*b2*h6-3/8*a0*a0*b2*c0*h2-3/8*a0*a0*b2*c1*h1-3/8*a0*a0*b2*c2*h0+2*a0*a0*c0*c1*h11+2*a0*a0*c0*c2*h10-9*a0*a0*c2*c2*h1+3/4*a0*a1*a1*c1*h7+9/4*a0*a1*a1*c2*h6+3/2*a0*a1*a2*c1*h6+3/2*a0*a1*b0*c2*h1+3/2*a0*a1*b1*c2*h0-3/2*a0*a1*b2*c0*h1-3/2*a0*a1*b2*c1*h0-2*a0*a1*c0*c0*h11-18*a0*a1*c1*c2*h1-37/2*a0*a1*c2*c2*h0-6*a0*a1*c2*c2*h7-3/4*a0*a2*a2*c0*h6-3/4*a0*a2*b0*b1*h7+3/2*a0*a2*b0*c1*h1+3/2*a0*a2*b0*c2*h0+15*a0*a2*b0*c2*h7-3/4*a0*a2*b1*b1*h6-3/4*a0*a2*b1*c0*h1+3/4*a0*a2*b1*c1*h0+15*a0*a2*b1*c2*h6-3/2*a0*a2*b2*c0*h0-27/2*a0*a2*b2*c0*h7-27/2*a0*a2*b2*c1*h6-2*a0*a2*c0*c0*h10-3*a0*a2*c0*c2*h1-9*a0*a2*c1*c1*h1-4*a0*a2*c1*c2*h0-12*a0*a2*c1*c2*h7-7*a0*a2*c2*c2*h6-2*a0*b1*c0*c0*h5+15/2*a0*b1*c2*c2*h1-2*a0*b2*c0*c0*h4+15*a0*b2*c1*c2*h1+17/2*a0*b2*c2*c2*h0-3*a0*b2*c2*c2*h7+3/4*a1*a1*a1*c1*h6+3/4*a1*a1*a2*c0*h6-3/8*a1*a1*b0*b1*h7+3/4*a1*a1*b0*c1*h1+3/4*a1*a1*b0*c2*h0+15/2*a1*a1*b0*c2*h7-3/8*a1*a1*b1*b1*h6-3/8*a1*a1*b1*c0*h1+3/8*a1*a1*b1*c1*h0+15/2*a1*a1*b1*c2*h6-3/4*a1*a1*b2*c0*h0-27/4*a1*a1*b2*c0*h7-27/4*a1*a1*b2*c1*h6+15/2*a1*a1*c0*c2*h1-21/2*a1*a1*c1*c2*h0-6*a1*a1*c2*c2*h6-3/4*a1*a2*b0*b0*h7-3/2*a1*a2*b0*b1*h6+3/4*a1*a2*b0*c0*h1+3/4*a1*a2*b0*c1*h0+15*a1*a2*b0*c1*h7+16*a1*a2*b0*c2*h6+3/4*a1*a2*b1*c0*h0-27/2*a1*a2*b1*c0*h7+3/2*a1*a2*b1*c1*h6-29/2*a1*a2*b2*c0*h6+15*a1*a2*c0*c1*h1-2*a1*a2*c0*c2*h0+6*a1*a2*c0*c2*h7+6*a1*a2*c1*c1*h0-6*a1*a2*c1*c2*h6+2*a1*b0*c0*c0*h5-6*a1*b0*c2*c2*h1+3/2*a1*b1*c2*c2*h0+15*a1*b2*c1*c2*h0-3*a1*b2*c2*c2*h6-3/8*a2*a2*b0*b0*h6+3/8*a2*a2*b0*c0*h0+3/4*a2*a2*b0*c0*h7+5/4*a2*a2*b0*c1*h6+1/4*a2*a2*b1*c0*h6+15/2*a2*a2*c0*c0*h1+31/2*a2*a2*c0*c1*h0+3*a2*a2*c0*c1*h7+4*a2*a2*c0*c2*h6+3*a2*a2*c1*c1*h6+2*a2*b0*c0*c0*h4-12*a2*b0*c1*c2*h1-7*a2*b0*c2*c2*h0+6*a2*b0*c2*c2*h7-12*a2*b1*c1*c2*h0+6*a2*b1*c2*c2*h6+6*a2*c0*c2*c2*h1+6*a2*c1*c2*c2*h0-3*b0*b2*c2*c2*h1-3*b1*b2*c2*c2*h0+a0*a0*b0*c1*h8*h11+a0*a0*b0*c2*h7*h11+a0*a0*b0*c2*h8*h10-a0*a0*b1*c0*h8*h11+a0*a0*b1*c2*h7*h10-a0*a0*b2*c0*h7*h11-a0*a0*b2*c0*h8*h10-a0*a0*b2*c1*h7*h10-a0*a0*c0*c1*h2*h11-a0*a0*c0*c1*h5*h8-a0*a0*c0*c2*h1*h11-a0*a0*c0*c2*h2*h10-a0*a0*c0*c2*h4*h8-a0*a0*c0*c2*h5*h7-a0*a0*c1*c1*h1*h11-a0*a0*c1*c1*h5*h7-2*a0*a0*c1*c2*h0*h11-a0*a0*c1*c2*h1*h10-a0*a0*c1*c2*h4*h7-2*a0*a0*c1*c2*h5*h6-a0*a0*c2*c2*h0*h10-a0*a0*c2*c2*h4*h6+2*a0*a1*b0*c1*h7*h11+2*a0*a1*b0*c2*h6*h11+2*a0*a1*b0*c2*h7*h10-2*a0*a1*b1*c0*h7*h11+2*a0*a1*b1*c2*h6*h10-2*a0*a1*b2*c0*h6*h11-2*a0*a1*b2*c0*h7*h10-2*a0*a1*b2*c1*h6*h10+a0*a1*c0*c0*h2*h11+a0*a1*c0*c0*h5*h8-2*a0*a1*c0*c2*h1*h10-2*a0*a1*c0*c2*h4*h7-a0*a1*c1*c1*h0*h11-a0*a1*c1*c1*h5*h6-2*a0*a1*c1*c2*h0*h10-2*a0*a1*c1*c2*h4*h6+2*a0*a2*b0*c1*h6*h11+2*a0*a2*b0*c2*h6*h10-2*a0*a2*b1*c0*h6*h11-2*a0*a2*b2*c0*h6*h10+a0*a2*c0*c0*h1*h11+a0*a2*c0*c0*h2*h10+a0*a2*c0*c0*h4*h8+a0*a2*c0*c0*h5*h7+2*a0*a2*c0*c1*h1*h10+2*a0*a2*c0*c1*h4*h7+a0*a2*c1*c1*h0*h10+a0*a2*c1*c1*h4*h6+a0*b1*c0*c0*h2*h5+2*a0*b1*c0*c1*h1*h5+2*a0*b1*c0*c2*h0*h5+a0*b1*c1*c1*h0*h5+a0*b2*c0*c0*h1*h5+a0*b2*c0*c0*h2*h4+2*a0*b2*c0*c1*h0*h5+2*a0*b2*c0*c1*h1*h4+2*a0*b2*c0*c2*h0*h4+a0*b2*c1*c1*h0*h4+a1*a1*b0*c1*h6*h11+a1*a1*b0*c2*h6*h10-a1*a1*b1*c0*h6*h11-a1*a1*b2*c0*h6*h10+a1*a1*c0*c0*h1*h11+a1*a1*c0*c0*h5*h7+a1*a1*c0*c1*h0*h11+a1*a1*c0*c1*h5*h6-a1*a1*c0*c2*h0*h10-a1*a1*c0*c2*h4*h6+2*a1*a2*c0*c0*h0*h11+a1*a2*c0*c0*h1*h10+a1*a2*c0*c0*h4*h7+2*a1*a2*c0*c0*h5*h6+2*a1*a2*c0*c1*h0*h10+2*a1*a2*c0*c1*h4*h6-a1*b0*c0*c0*h2*h5-2*a1*b0*c0*c1*h1*h5-2*a1*b0*c0*c2*h0*h5-a1*b0*c1*c1*h0*h5+a1*b2*c0*c0*h1*h4+2*a1*b2*c0*c1*h0*h4+a2*a2*c0*c0*h0*h10+a2*a2*c0*c0*h4*h6-a2*b0*c0*c0*h1*h5-a2*b0*c0*c0*h2*h4-2*a2*b0*c0*c1*h0*h5-2*a2*b0*c0*c1*h1*h4-2*a2*b0*c0*c2*h0*h4-a2*b0*c1*c1*h0*h4-a2*b1*c0*c0*h1*h4-2*a2*b1*c0*c1*h0*h4,-43/8*a0*a0*a0*c0+77/32*a0*a0*b0*b0-171/16*a0*a0*b0*c1-55/16*a0*a0*b1*c0+167/2*a0*a0*c0*c2+89/2*a0*a0*c1*c1-119/8*a0*a1*b0*c0+129*a0*a1*c0*c1+41*a0*a2*c0*c0-41/2*a0*b0*c1*c2-165/2*a0*b1*c0*c2-165/4*a0*b1*c1*c1-177/2*a0*b2*c0*c1-54*a0*c0*c2*c2-90*a0*c1*c1*c2+20*a1*a1*c0*c0-13/2*a1*b0*c0*c2-13/4*a1*b0*c1*c1-137/2*a1*b1*c0*c1-149/4*a1*b2*c0*c0-120*a1*c0*c1*c2-32*a1*c1*c1*c1+11/2*a2*b0*c0*c1-113/4*a2*b1*c0*c0-30*a2*c0*c0*c2-66*a2*c0*c1*c1+b0*b0*c2*c2+43*b0*b1*c1*c2+37*b0*b2*c0*c2+37/2*b0*b2*c1*c1-27*b0*c1*c2*c2+41*b1*b1*c0*c2+41/2*b1*b1*c1*c1+76*b1*b2*c0*c1-9*b1*c0*c2*c2-27*b1*c1*c1*c2+35/2*b2*b2*c0*c0-18*b2*c0*c1*c2-9*b2*c1*c1*c1+3/4*a0*a0*a0*c2*h7+3/2*a0*a0*a1*c1*h7+9/4*a0*a0*a1*c2*h6+3/4*a0*a0*a2*c0*h7+3/4*a0*a0*a2*c1*h6+3/4*a0*a0*b0*c2*h1+3/4*a0*a0*b1*c2*h0-3/4*a0*a0*b2*c0*h1-3/4*a0*a0*b2*c1*h0-18*a0*a0*c1*c2*h1-19/2*a0*a0*c2*c2*h0-6*a0*a0*c2*c2*h7+3/4*a0*a1*a1*c0*h7+9/4*a0*a1*a1*c1*h6+3/2*a0*a1*a2*c0*h6-3/4*a0*a1*b0*b1*h7+3/2*a0*a1*b0*c1*h1+3/2*a0*a1*b0*c2*h0+15*a0*a1*b0*c2*h7-3/4*a0*a1*b1*b1*h6-3/4*a0*a1*b1*c0*h1+3/4*a0*a1*b1*c1*h0+15*a0*a1*b1*c2*h6-3/2*a0*a1*b2*c0*h0-27/2*a0*a1*b2*c0*h7-27/2*a0*a1*b2*c1*h6-3*a0*a1*c0*c2*h1-9*a0*a1*c1*c1*h1-22*a0*a1*c1*c2*h0-12*a0*a1*c1*c2*h7-13*a0*a1*c2*c2*h6-3/4*a0*a2*b0*b0*h7-3/2*a0*a2*b0*b1*h6+3/4*a0*a2*b0*c0*h1+3/4*a0*a2*b0*c1*h0+15*a0*a2*b0*c1*h7+16*a0*a2*b0*c2*h6+3/4*a0*a2*b1*c0*h0-27/2*a0*a2*b1*c0*h7+3/2*a0*a2*b1*c1*h6-29/2*a0*a2*b2*c0*h6-3*a0*a2*c0*c1*h1-3*a0*a2*c0*c2*h0-6*a0*a2*c0*c2*h7+11/2*a0*a2*c1*c1*h0-6*a0*a2*c1*c1*h7-8*a0*a2*c1*c2*h6+3/2*a0*b0*c2*c2*h1+15*a0*b1*c1*c2*h1+5/2*a0*b1*c2*c2*h0-3*a0*b1*c2*c2*h7+15*a0*b2*c0*c2*h1+15/2*a0*b2*c1*c1*h1+17*a0*b2*c1*c2*h0-6*a0*b2*c1*c2*h7-3*a0*b2*c2*c2*h6+3/4*a1*a1*a1*c0*h6-3/8*a1*a1*b0*b0*h7-3/4*a1*a1*b0*b1*h6+3/8*a1*a1*b0*c0*h1+3/8*a1*a1*b0*c1*h0+15/2*a1*a1*b0*c1*h7+8*a1*a1*b0*c2*h6+3/8*a1*a1*b1*c0*h0-27/4*a1*a1*b1*c0*h7+3/4*a1*a1*b1*c1*h6-29/4*a1*a1*b2*c0*h6+15/2*a1*a1*c0*c1*h1-10*a1*a1*c0*c2*h0+3*a1*a1*c0*c2*h7-3/2*a1*a1*c1*c1*h0-9*a1*a1*c1*c2*h6-3/4*a1*a2*b0*b0*h6+3/4*a1*a2*b0*c0*h0+3/2*a1*a2*b0*c0*h7+5/2*a1*a2*b0*c1*h6+1/2*a1*a2*b1*c0*h6+15*a1*a2*c0*c0*h1+13*a1*a2*c0*c1*h0+6*a1*a2*c0*c1*h7-4*a1*a2*c0*c2*h6-12*a1*b0*c1*c2*h1+1/2*a1*b0*c2*c2*h0+6*a1*b0*c2*c2*h7+3*a1*b1*c1*c2*h0+3*a1*b1*c2*c2*h6+15*a1*b2*c0*c2*h0+15/2*a1*b2*c1*c1*h0-6*a1*b2*c1*c2*h6+6*a1*c0*c2*c2*h1+6*a1*c1*c2*c2*h0+3/4*a2*a2*b0*c0*h6+8*a2*a2*c0*c0*h0+3*a2*a2*c0*c0*h7+7*a2*a2*c0*c1*h6-12*a2*b0*c0*c2*h1-6*a2*b0*c1*c1*h1-14*a2*b0*c1*c2*h0+12*a2*b0*c1*c2*h7+6*a2*b0*c2*c2*h6-12*a2*b1*c0*c2*h0-6*a2*b1*c1*c1*h0+12*a2*b1*c1*c2*h6+12*a2*c0*c1*c2*h1+6*a2*c0*c2*c2*h0+12*a2*c1*c1*c2*h0-3*b0*b1*c2*c2*h1-6*b0*b2*c1*c2*h1-3*b0*b2*c2*c2*h0-3*b1*b1*c2*c2*h0-6*b1*b2*c1*c2*h0+a0*a0*b0*c1*h7*h11+a0*a0*b0*c2*h6*h11+a0*a0*b0*c2*h7*h10-a0*a0*b1*c0*h7*h11+a0*a0*b1*c2*h6*h10-a0*a0*b2*c0*h6*h11-a0*a0*b2*c0*h7*h10-a0*a0*b2*c1*h6*h10-a0*a0*c0*c1*h1*h11-a0*a0*c0*c1*h5*h7-a0*a0*c0*c2*h0*h11-a0*a0*c0*c2*h1*h10-a0*a0*c0*c2*h4*h7-a0*a0*c0*c2*h5*h6-a0*a0*c1*c1*h0*h11-a0*a0*c1*c1*h5*h6-a0*a0*c1*c2*h0*h10-a0*a0*c1*c2*h4*h6+2*a0*a1*b0*c1*h6*h11+2*a0*a1*b0*c2*h6*h10-2*a0*a1*b1*c0*h6*h11-2*a0*a1*b2*c0*h6*h10+a0*a1*c0*c0*h1*h11+a0*a1*c0*c0*h5*h7-2*a0*a1*c0*c2*h0*h10-2*a0*a1*c0*c2*h4*h6+a0*a2*c0*c0*h0*h11+a0*a2*c0*c0*h1*h10+a0*a2*c0*c0*h4*h7+a0*a2*c0*c0*h5*h6+2*a0*a2*c0*c1*h0*h10+2*a0*a2*c0*c1*h4*h6+a0*b1*c0*c0*h1*h5+2*a0*b1*c0*c1*h0*h5+a0*b2*c0*c0*h0*h5+a0*b2*c0*c0*h1*h4+2*a0*b2*c0*c1*h0*h4+a1*a1*c0*c0*h0*h11+a1*a1*c0*c0*h5*h6+a1*a2*c0*c0*h0*h10+a1*a2*c0*c0*h4*h6-a1*b0*c0*c0*h1*h5-2*a1*b0*c0*c1*h0*h5+a1*b2*c0*c0*h0*h4-a2*b0*c0*c0*h0*h5-a2*b0*c0*c0*h1*h4-2*a2*b0*c0*c1*h0*h4-a2*b1*c0*c0*h0*h4,-27/16*a0*a0*a1*a2-159/32*a0*a0*a2*b2-9/16*a0*a1*a1*a1-159/32*a0*a1*a1*b2-213/16*a0*a1*a2*b1+847/8*a0*a1*a2*c2-231/32*a0*a2*a2*b0+607/16*a0*a2*a2*c1-113/2*a0*a2*b2*c2-71/32*a1*a1*a1*b1+289/16*a1*a1*a1*c2-231/32*a1*a1*a2*b0+627/16*a1*a1*a2*c1-111/4*a1*a1*b2*c2+375/16*a1*a2*a2*c0-27*a1*a2*b1*c2-45*a1*a2*b2*c1-235/2*a1*a2*c2*c2+149/4*a1*b2*b2*c2+41/8*a2*a2*b0*c2-33/4*a2*a2*b1*c1-69/4*a2*a2*b2*c0-223/2*a2*a2*c1*c2+119/2*a2*b1*b2*c2+125/4*a2*b2*b2*c1+87/2*a2*b2*c2*c2-35/2*b2*b2*b2*c2-3/8*a0*a0*a0*b2*h11-9/8*a0*a0*a1*b2*h10+2*a0*a0*a1*c2*h11-9/8*a0*a0*a2*b2*h9+3/4*a0*a0*a2*c0*h5+3/4*a0*a0*a2*c1*h4+2*a0*a0*a2*c1*h11+3/4*a0*a0*a2*c2*h3+2*a0*a0*a2*c2*h10-a0*a0*b1*c2*h5-a0*a0*b2*c1*h5-a0*a0*b2*c2*h4-2*a0*a0*b2*c2*h11-2*a0*a0*c2*c2*h5-9/8*a0*a1*a1*b2*h9+a0*a1*a1*c1*h11+3*a0*a1*a1*c2*h10-9/4*a0*a1*a2*b2*h8+3/2*a0*a1*a2*c0*h4-4*a0*a1*a2*c0*h11+3/2*a0*a1*a2*c1*h3-2*a0*a1*a2*c1*h10+3/2*a0*a1*a2*c2*h2+a0*a1*b0*c2*h5-a0*a1*b1*c1*h5-2*a0*a1*b1*c2*h11-a0*a1*b2*c0*h5-2*a0*a1*b2*c1*h4-2*a0*a1*b2*c1*h11-4*a0*a1*b2*c2*h10-4*a0*a1*c1*c2*h5-4*a0*a1*c2*c2*h4-9/8*a0*a2*a2*b2*h7+3/2*a0*a2*a2*c0*h3-2*a0*a2*a2*c0*h10+3/2*a0*a2*a2*c1*h2+3/8*a0*a2*a2*c2*h1+a0*a2*b0*c1*h5+a0*a2*b0*c2*h4+2*a0*a2*b0*c2*h11-a0*a2*b1*c0*h5+a0*a2*b1*c1*h4-2*a0*a2*b1*c1*h11+2*a0*a2*b1*c2*h10-a0*a2*b2*c0*h4-2*a0*a2*b2*c0*h11-2*a0*a2*b2*c1*h10-2*a0*a2*c1*c1*h5+2*a0*b0*b2*c2*h5+2*a0*b1*b1*c2*h5+4*a0*b1*b2*c1*h5+2*a0*b1*b2*c2*h4+2*a0*b2*b2*c0*h5+2*a0*b2*b2*c1*h4-3/8*a1*a1*a1*b2*h8-a1*a1*a1*c0*h11-9/8*a1*a1*a2*b2*h7+3/4*a1*a1*a2*c0*h3-a1*a1*a2*c0*h10+3/4*a1*a1*a2*c1*h2+3/4*a1*a1*a2*c2*h1+a1*a1*b0*c1*h5+2*a1*a1*b0*c2*h11-a1*a1*b2*c0*h4-2*a1*a1*b2*c1*h10+2*a1*a1*c0*c2*h5-2*a1*a1*c1*c2*h4-9/8*a1*a2*a2*b2*h6+3/2*a1*a2*a2*c0*h2+3/2*a1*a2*a2*c1*h1+3/8*a1*a2*a2*c2*h0+2*a1*a2*b0*c0*h5+a1*a2*b0*c1*h4+4*a1*a2*b0*c1*h11+2*a1*a2*b0*c2*h10+a1*a2*b1*c0*h4+2*a1*a2*b1*c1*h10-2*a1*a2*b2*c0*h10+4*a1*a2*c0*c1*h5+2*a1*a2*c1*c1*h4-2*a1*b0*b1*c2*h5-2*a1*b0*b2*c1*h5+2*a1*b0*b2*c2*h4+2*a1*b1*b2*c1*h4+2*a1*b2*b2*c0*h4+3/8*a2*a2*a2*b0*h7+3/8*a2*a2*a2*b1*h6+9/8*a2*a2*a2*c0*h1+9/8*a2*a2*a2*c1*h0+a2*a2*b0*c0*h4+2*a2*a2*b0*c0*h11+2*a2*a2*b0*c1*h10+2*a2*a2*b1*c0*h10+2*a2*a2*c0*c0*h5+4*a2*a2*c0*c1*h4-2*a2*b0*b0*c2*h5-2*a2*b0*b1*c1*h5-4*a2*b0*b1*c2*h4-2*a2*b0*b2*c0*h5-2*a2*b0*b2*c1*h4-2*a2*b1*b1*c1*h4-2*a2*b1*b2*c0*h4-a0*a0*a0*c1*h11*h11-2*a0*a0*a0*c2*h10*h11+a0*a0*a1*c0*h11*h11-2*a0*a0*a1*c1*h10*h11-2*a0*a0*a1*c2*h9*h11-3*a0*a0*a1*c2*h10*h10+2*a0*a0*a2*c0*h10*h11-2*a0*a0*a2*c1*h9*h11+a0*a0*a2*c1*h10*h10-2*a0*a0*a2*c2*h8*h11-2*a0*a0*a2*c2*h9*h10+2*a0*a0*b1*c0*h5*h11+a0*a0*b1*c1*h4*h11+a0*a0*b1*c1*h5*h10+a0*a0*b1*c2*h3*h11+a0*a0*b1*c2*h5*h9+2*a0*a0*b2*c0*h4*h11+2*a0*a0*b2*c0*h5*h10+a0*a0*b2*c1*h3*h11+2*a0*a0*b2*c1*h4*h10+a0*a0*b2*c1*h5*h9+a0*a0*b2*c2*h2*h11+a0*a0*b2*c2*h3*h10+a0*a0*b2*c2*h4*h9+a0*a0*b2*c2*h5*h8+a0*a0*c0*c1*h5*h5+2*a0*a0*c0*c2*h4*h5+a0*a0*c1*c1*h4*h5+2*a0*a0*c1*c2*h3*h5+a0*a0*c1*c2*h4*h4+a0*a0*c2*c2*h2*h5+a0*a0*c2*c2*h3*h4+2*a0*a1*a1*c0*h10*h11-a0*a1*a1*c1*h9*h11-a0*a1*a1*c2*h8*h11-3*a0*a1*a1*c2*h9*h10+4*a0*a1*a2*c0*h9*h11+2*a0*a1*a2*c0*h10*h10-2*a0*a1*a2*c1*h8*h11+2*a0*a1*a2*c1*h9*h10-2*a0*a1*a2*c2*h7*h11-4*a0*a1*a2*c2*h8*h10-2*a0*a1*b0*c0*h5*h11-a0*a1*b0*c1*h4*h11-a0*a1*b0*c1*h5*h10-a0*a1*b0*c2*h3*h11-a0*a1*b0*c2*h5*h9+a0*a1*b1*c0*h4*h11+a0*a1*b1*c0*h5*h10+a0*a1*b1*c1*h3*h11+a0*a1*b1*c1*h5*h9+a0*a1*b1*c2*h2*h11+a0*a1*b1*c2*h5*h8+a0*a1*b2*c0*h3*h11+4*a0*a1*b2*c0*h4*h10+a0*a1*b2*c0*h5*h9+a0*a1*b2*c1*h2*h11+2*a0*a1*b2*c1*h3*h10+2*a0*a1*b2*c1*h4*h9+a0*a1*b2*c1*h5*h8+a0*a1*b2*c2*h1*h11+2*a0*a1*b2*c2*h2*h10+2*a0*a1*b2*c2*h4*h8+a0*a1*b2*c2*h5*h7-a0*a1*c0*c0*h5*h5+2*a0*a1*c0*c2*h4*h4+a0*a1*c1*c1*h3*h5+2*a0*a1*c1*c2*h2*h5+2*a0*a1*c1*c2*h3*h4+a0*a1*c2*c2*h1*h5+2*a0*a1*c2*c2*h2*h4+2*a0*a2*a2*c0*h8*h11+2*a0*a2*a2*c0*h9*h10-a0*a2*a2*c1*h7*h11+2*a0*a2*a2*c1*h8*h10-a0*a2*a2*c2*h6*h11-a0*a2*a2*c2*h7*h10-2*a0*a2*b0*c0*h4*h11-2*a0*a2*b0*c0*h5*h10-a0*a2*b0*c1*h3*h11-2*a0*a2*b0*c1*h4*h10-a0*a2*b0*c1*h5*h9-a0*a2*b0*c2*h2*h11-a0*a2*b0*c2*h3*h10-a0*a2*b0*c2*h4*h9-a0*a2*b0*c2*h5*h8+a0*a2*b1*c0*h3*h11-2*a0*a2*b1*c0*h4*h10+a0*a2*b1*c0*h5*h9+a0*a2*b1*c1*h2*h11-a0*a2*b1*c1*h3*h10-a0*a2*b1*c1*h4*h9+a0*a2*b1*c1*h5*h8+a0*a2*b1*c2*h1*h11-a0*a2*b1*c2*h2*h10-a0*a2*b1*c2*h4*h8+a0*a2*b1*c2*h5*h7+a0*a2*b2*c0*h2*h11+a0*a2*b2*c0*h3*h10+a0*a2*b2*c0*h4*h9+a0*a2*b2*c0*h5*h8+a0*a2*b2*c1*h1*h11+a0*a2*b2*c1*h2*h10+a0*a2*b2*c1*h4*h8+a0*a2*b2*c1*h5*h7+a0*a2*b2*c2*h0*h11+a0*a2*b2*c2*h1*h10+a0*a2*b2*c2*h4*h7+a0*a2*b2*c2*h5*h6-2*a0*a2*c0*c0*h4*h5-2*a0*a2*c0*c1*h4*h4+a0*a2*c1*c1*h2*h5-a0*a2*c1*c1*h3*h4+2*a0*a2*c1*c2*h1*h5+a0*a2*c2*c2*h0*h5+a0*a2*c2*c2*h1*h4-a0*b0*b1*c0*h5*h5-a0*b0*b1*c1*h4*h5-a0*b0*b1*c2*h3*h5-2*a0*b0*b2*c0*h4*h5-a0*b0*b2*c1*h3*h5-a0*b0*b2*c1*h4*h4-a0*b0*b2*c2*h2*h5-a0*b0*b2*c2*h3*h4-a0*b1*b1*c0*h4*h5-a0*b1*b1*c1*h3*h5-a0*b1*b1*c2*h2*h5-2*a0*b1*b2*c0*h3*h5-a0*b1*b2*c0*h4*h4-2*a0*b1*b2*c1*h2*h5-a0*b1*b2*c1*h3*h4-2*a0*b1*b2*c2*h1*h5-a0*b1*b2*c2*h2*h4-a0*b2*b2*c0*h2*h5-a0*b2*b2*c0*h3*h4-a0*b2*b2*c1*h1*h5-a0*b2*b2*c1*h2*h4-a0*b2*b2*c2*h0*h5-a0*b2*b2*c2*h1*h4+a1*a1*a1*c0*h9*h11-a1*a1*a1*c2*h8*h10+3*a1*a1*a2*c0*h8*h11+a1*a1*a2*c0*h9*h10+a1*a1*a2*c1*h8*h10-2*a1*a1*a2*c2*h7*h10-a1*a1*b0*c0*h4*h11-a1*a1*b0*c0*h5*h10-a1*a1*b0*c1*h3*h11-a1*a1*b0*c1*h5*h9-a1*a1*b0*c2*h2*h11-a1*a1*b0*c2*h5*h8+a1*a1*b2*c0*h3*h10+a1*a1*b2*c0*h4*h9+a1*a1*b2*c1*h2*h10+a1*a1*b2*c1*h4*h8+a1*a1*b2*c2*h1*h10+a1*a1*b2*c2*h4*h7-a1*a1*c0*c0*h4*h5-a1*a1*c0*c1*h3*h5-a1*a1*c0*c2*h2*h5+a1*a1*c0*c2*h3*h4+a1*a1*c1*c2*h2*h4+a1*a1*c2*c2*h1*h4+3*a1*a2*a2*c0*h7*h11+2*a1*a2*a2*c0*h8*h10+2*a1*a2*a2*c1*h7*h10-a1*a2*a2*c2*h6*h10-2*a1*a2*b0*c0*h3*h11-2*a1*a2*b0*c0*h4*h10-2*a1*a2*b0*c0*h5*h9-2*a1*a2*b0*c1*h2*h11-a1*a2*b0*c1*h3*h10-a1*a2*b0*c1*h4*h9-2*a1*a2*b0*c1*h5*h8-2*a1*a2*b0*c2*h1*h11-a1*a2*b0*c2*h2*h10-a1*a2*b0*c2*h4*h8-2*a1*a2*b0*c2*h5*h7-a1*a2*b1*c0*h3*h10-a1*a2*b1*c0*h4*h9-a1*a2*b1*c1*h2*h10-a1*a2*b1*c1*h4*h8-a1*a2*b1*c2*h1*h10-a1*a2*b1*c2*h4*h7+a1*a2*b2*c0*h2*h10+a1*a2*b2*c0*h4*h8+a1*a2*b2*c1*h1*h10+a1*a2*b2*c1*h4*h7+a1*a2*b2*c2*h0*h10+a1*a2*b2*c2*h4*h6-2*a1*a2*c0*c0*h3*h5-a1*a2*c0*c0*h4*h4-2*a1*a2*c0*c1*h2*h5-2*a1*a2*c0*c1*h3*h4-2*a1*a2*c0*c2*h1*h5-a1*a2*c1*c1*h2*h4+a1*a2*c2*c2*h0*h4+a1*b0*b0*c0*h5*h5+a1*b0*b0*c1*h4*h5+a1*b0*b0*c2*h3*h5+a1*b0*b1*c0*h4*h5+a1*b0*b1*c1*h3*h5+a1*b0*b1*c2*h2*h5+a1*b0*b2*c0*h3*h5-a1*b0*b2*c0*h4*h4+a1*b0*b2*c1*h2*h5-a1*b0*b2*c1*h3*h4+a1*b0*b2*c2*h1*h5-a1*b0*b2*c2*h2*h4-a1*b1*b2*c0*h3*h4-a1*b1*b2*c1*h2*h4-a1*b1*b2*c2*h1*h4-a1*b2*b2*c0*h2*h4-a1*b2*b2*c1*h1*h4-a1*b2*b2*c2*h0*h4+a2*a2*a2*c0*h6*h11+a2*a2*a2*c0*h7*h10+a2*a2*a2*c1*h6*h10-a2*a2*b0*c0*h2*h11-a2*a2*b0*c0*h3*h10-a2*a2*b0*c0*h4*h9-a2*a2*b0*c0*h5*h8-a2*a2*b0*c1*h1*h11-a2*a2*b0*c1*h2*h10-a2*a2*b0*c1*h4*h8-a2*a2*b0*c1*h5*h7-a2*a2*b0*c2*h0*h11-a2*a2*b0*c2*h1*h10-a2*a2*b0*c2*h4*h7-a2*a2*b0*c2*h5*h6-a2*a2*b1*c0*h2*h10-a2*a2*b1*c0*h4*h8-a2*a2*b1*c1*h1*h10-a2*a2*b1*c1*h4*h7-a2*a2*b1*c2*h0*h10-a2*a2*b1*c2*h4*h6-a2*a2*c0*c0*h2*h5-a2*a2*c0*c0*h3*h4-a2*a2*c0*c1*h1*h5-2*a2*a2*c0*c1*h2*h4-a2*a2*c0*c2*h0*h5-a2*a2*c0*c2*h1*h4-a2*a2*c1*c1*h1*h4-a2*a2*c1*c2*h0*h4+2*a2*b0*b0*c0*h4*h5+a2*b0*b0*c1*h3*h5+a2*b0*b0*c1*h4*h4+a2*b0*b0*c2*h2*h5+a2*b0*b0*c2*h3*h4+a2*b0*b1*c0*h3*h5+2*a2*b0*b1*c0*h4*h4+a2*b0*b1*c1*h2*h5+2*a2*b0*b1*c1*h3*h4+a2*b0*b1*c2*h1*h5+2*a2*b0*b1*c2*h2*h4+a2*b0*b2*c0*h2*h5+a2*b0*b2*c0*h3*h4+a2*b0*b2*c1*h1*h5+a2*b0*b2*c1*h2*h4+a2*b0*b2*c2*h0*h5+a2*b0*b2*c2*h1*h4+a2*b1*b1*c0*h3*h4+a2*b1*b1*c1*h2*h4+a2*b1*b1*c2*h1*h4+a2*b1*b2*c0*h2*h4+a2*b1*b2*c1*h1*h4+a2*b1*b2*c2*h0*h4,-9/16*a0*a0*a0*a2-27/32*a0*a0*a1*a1-159/32*a0*a0*a1*b2-213/32*a0*a0*a2*b1+923/16*a0*a0*a2*c2-213/32*a0*a1*a1*b1+943/16*a0*a1*a1*c2-231/16*a0*a1*a2*b0+703/8*a0*a1*a2*c1-67*a0*a1*b2*c2+451/16*a0*a2*a2*c0-77/2*a0*a2*b1*c2-113/2*a0*a2*b2*c1-249/2*a0*a2*c2*c2+177/4*a0*b2*b2*c2-77/32*a1*a1*a1*b0+241/16*a1*a1*a1*c1+471/16*a1*a1*a2*c0-75/4*a1*a1*b1*c2-111/4*a1*a1*b2*c1-247/4*a1*a1*c2*c2-1/4*a1*a2*b0*c2-27*a1*a2*b1*c1-45*a1*a2*b2*c0-235*a1*a2*c1*c2+143/2*a1*b1*b2*c2+149/4*a1*b2*b2*c1+87/2*a1*b2*c2*c2+41/8*a2*a2*b0*c1-33/4*a2*a2*b1*c0-61*a2*a2*c0*c2-223/4*a2*a2*c1*c1+57/2*a2*b0*b2*c2+113/4*a2*b1*b1*c2+119/2*a2*b1*b2*c1+93/2*a2*b1*c2*c2+125/4*a2*b2*b2*c0+93*a2*b2*c1*c2-9*a2*c2*c2*c2-111/2*b1*b2*b2*c2-35/2*b2*b2*b2*c1+9*b2*b2*c2*c2-3/8*a0*a0*a0*b2*h10+a0*a0*a0*c2*h11-9/8*a0*a0*a1*b2*h9+2*a0*a0*a1*c1*h11+3*a0*a0*a1*c2*h10-9/8*a0*a0*a2*b2*h8+3/4*a0*a0*a2*c0*h4-a0*a0*a2*c0*h11+3/4*a0*a0*a2*c1*h3-a0*a0*a2*c1*h10+3/4*a0*a0*a2*c2*h2-a0*a0*b1*c1*h5-2*a0*a0*b1*c2*h11-a0*a0*b2*c0*h5-a0*a0*b2*c1*h4-2*a0*a0*b2*c1*h11-2*a0*a0*b2*c2*h10-4*a0*a0*c1*c2*h5-2*a0*a0*c2*c2*h4-9/8*a0*a1*a1*b2*h8-2*a0*a1*a1*c0*h11-9/4*a0*a1*a2*b2*h7+3/2*a0*a1*a2*c0*h3-2*a0*a1*a2*c0*h10+3/2*a0*a1*a2*c1*h2-3/4*a0*a1*a2*c2*h1+a0*a1*b0*c1*h5+2*a0*a1*b0*c2*h11-a0*a1*b1*c0*h5-2*a0*a1*b1*c1*h11-2*a0*a1*b2*c0*h4-2*a0*a1*b2*c0*h11-4*a0*a1*b2*c1*h10-2*a0*a1*c1*c1*h5-4*a0*a1*c1*c2*h4-9/8*a0*a2*a2*b2*h6+3/2*a0*a2*a2*c0*h2+3/8*a0*a2*a2*c1*h1+3/8*a0*a2*a2*c2*h0-33/4*a0*a2*a2*c2*h7+a0*a2*b0*c0*h5+a0*a2*b0*c1*h4+2*a0*a2*b0*c1*h11+2*a0*a2*b0*c2*h10+a0*a2*b1*c0*h4-2*a0*a2*b1*c0*h11+2*a0*a2*b1*c1*h10-2*a0*a2*b2*c0*h10+9*a0*a2*b2*c2*h1+2*a0*a2*c1*c1*h4+2*a0*b0*b1*c2*h5+2*a0*b0*b2*c1*h5+2*a0*b0*b2*c2*h4+2*a0*b1*b1*c1*h5+4*a0*b1*b2*c0*h5+2*a0*b1*b2*c1*h4+2*a0*b2*b2*c0*h4-3/8*a1*a1*a1*b2*h7-9/8*a1*a1*a2*b2*h6+3/4*a1*a1*a2*c0*h2+3/4*a1*a1*a2*c1*h1-3/2*a1*a1*a2*c2*h0+a1*a1*b0*c0*h5+2*a1*a1*b0*c1*h11-2*a1*a1*b2*c0*h10+2*a1*a1*c0*c1*h5-2*a1*a1*c0*c2*h4+9/8*a1*a2*a2*b0*h7+9/8*a1*a2*a2*b1*h6+21/8*a1*a2*a2*c0*h1+3/2*a1*a2*a2*c1*h0-33/4*a1*a2*a2*c2*h6+a1*a2*b0*c0*h4+4*a1*a2*b0*c0*h11+2*a1*a2*b0*c1*h10+2*a1*a2*b1*c0*h10+9*a1*a2*b2*c2*h0+4*a1*a2*c0*c0*h5+4*a1*a2*c0*c1*h4-2*a1*b0*b0*c2*h5-2*a1*b0*b1*c1*h5-2*a1*b0*b2*c0*h5+2*a1*b0*b2*c1*h4+2*a1*b1*b2*c0*h4+3/8*a2*a2*a2*b0*h6+9/8*a2*a2*a2*c0*h0+27/4*a2*a2*a2*c0*h7+27/4*a2*a2*a2*c1*h6+2*a2*a2*b0*c0*h10-33/4*a2*a2*b0*c2*h1-33/4*a2*a2*b1*c2*h0+2*a2*a2*c0*c0*h4-2*a2*b0*b0*c1*h5-2*a2*b0*b0*c2*h4-2*a2*b0*b1*c0*h5-4*a2*b0*b1*c1*h4-2*a2*b0*b2*c0*h4-2*a2*b1*b1*c0*h4-a0*a0*a0*c1*h10*h11-a0*a0*a0*c2*h9*h11-a0*a0*a0*c2*h10*h10+a0*a0*a1*c0*h10*h11-2*a0*a0*a1*c1*h9*h11-2*a0*a0*a1*c2*h8*h11-3*a0*a0*a1*c2*h9*h10+a0*a0*a2*c0*h9*h11+a0*a0*a2*c0*h10*h10-2*a0*a0*a2*c1*h8*h11+a0*a0*a2*c1*h9*h10-2*a0*a0*a2*c2*h7*h11-2*a0*a0*a2*c2*h8*h10+a0*a0*b1*c0*h4*h11+a0*a0*b1*c0*h5*h10+a0*a0*b1*c1*h3*h11+a0*a0*b1*c1*h5*h9+a0*a0*b1*c2*h2*h11+a0*a0*b1*c2*h5*h8+a0*a0*b2*c0*h3*h11+2*a0*a0*b2*c0*h4*h10+a0*a0*b2*c0*h5*h9+a0*a0*b2*c1*h2*h11+a0*a0*b2*c1*h3*h10+a0*a0*b2*c1*h4*h9+a0*a0*b2*c1*h5*h8+a0*a0*b2*c2*h1*h11+a0*a0*b2*c2*h2*h10+a0*a0*b2*c2*h4*h8+a0*a0*b2*c2*h5*h7+a0*a0*c0*c1*h4*h5+a0*a0*c0*c2*h3*h5+a0*a0*c0*c2*h4*h4+a0*a0*c1*c1*h3*h5+2*a0*a0*c1*c2*h2*h5+a0*a0*c1*c2*h3*h4+a0*a0*c2*c2*h1*h5+a0*a0*c2*c2*h2*h4+2*a0*a1*a1*c0*h9*h11-a0*a1*a1*c1*h8*h11-a0*a1*a1*c2*h7*h11-3*a0*a1*a1*c2*h8*h10+4*a0*a1*a2*c0*h8*h11+2*a0*a1*a2*c0*h9*h10-2*a0*a1*a2*c1*h7*h11+2*a0*a1*a2*c1*h8*h10-2*a0*a1*a2*c2*h6*h11-4*a0*a1*a2*c2*h7*h10-a0*a1*b0*c0*h4*h11-a0*a1*b0*c0*h5*h10-a0*a1*b0*c1*h3*h11-a0*a1*b0*c1*h5*h9-a0*a1*b0*c2*h2*h11-a0*a1*b0*c2*h5*h8+a0*a1*b1*c0*h3*h11+a0*a1*b1*c0*h5*h9+a0*a1*b1*c1*h2*h11+a0*a1*b1*c1*h5*h8+a0*a1*b1*c2*h1*h11+a0*a1*b1*c2*h5*h7+a0*a1*b2*c0*h2*h11+2*a0*a1*b2*c0*h3*h10+2*a0*a1*b2*c0*h4*h9+a0*a1*b2*c0*h5*h8+a0*a1*b2*c1*h1*h11+2*a0*a1*b2*c1*h2*h10+2*a0*a1*b2*c1*h4*h8+a0*a1*b2*c1*h5*h7+a0*a1*b2*c2*h0*h11+2*a0*a1*b2*c2*h1*h10+2*a0*a1*b2*c2*h4*h7+a0*a1*b2*c2*h5*h6-a0*a1*c0*c0*h4*h5+2*a0*a1*c0*c2*h3*h4+a0*a1*c1*c1*h2*h5+2*a0*a1*c1*c2*h1*h5+2*a0*a1*c1*c2*h2*h4+a0*a1*c2*c2*h0*h5+2*a0*a1*c2*c2*h1*h4+2*a0*a2*a2*c0*h7*h11+2*a0*a2*a2*c0*h8*h10-a0*a2*a2*c1*h6*h11+2*a0*a2*a2*c1*h7*h10-a0*a2*a2*c2*h6*h10-a0*a2*b0*c0*h3*h11-2*a0*a2*b0*c0*h4*h10-a0*a2*b0*c0*h5*h9-a0*a2*b0*c1*h2*h11-a0*a2*b0*c1*h3*h10-a0*a2*b0*c1*h4*h9-a0*a2*b0*c1*h5*h8-a0*a2*b0*c2*h1*h11-a0*a2*b0*c2*h2*h10-a0*a2*b0*c2*h4*h8-a0*a2*b0*c2*h5*h7+a0*a2*b1*c0*h2*h11-a0*a2*b1*c0*h3*h10-a0*a2*b1*c0*h4*h9+a0*a2*b1*c0*h5*h8+a0*a2*b1*c1*h1*h11-a0*a2*b1*c1*h2*h10-a0*a2*b1*c1*h4*h8+a0*a2*b1*c1*h5*h7+a0*a2*b1*c2*h0*h11-a0*a2*b1*c2*h1*h10-a0*a2*b1*c2*h4*h7+a0*a2*b1*c2*h5*h6+a0*a2*b2*c0*h1*h11+a0*a2*b2*c0*h2*h10+a0*a2*b2*c0*h4*h8+a0*a2*b2*c0*h5*h7+a0*a2*b2*c1*h0*h11+a0*a2*b2*c1*h1*h10+a0*a2*b2*c1*h4*h7+a0*a2*b2*c1*h5*h6+a0*a2*b2*c2*h0*h10+a0*a2*b2*c2*h4*h6-a0*a2*c0*c0*h3*h5-a0*a2*c0*c0*h4*h4-2*a0*a2*c0*c1*h3*h4+a0*a2*c1*c1*h1*h5-a0*a2*c1*c1*h2*h4+2*a0*a2*c1*c2*h0*h5+a0*a2*c2*c2*h0*h4-a0*b0*b1*c0*h4*h5-a0*b0*b1*c1*h3*h5-a0*b0*b1*c2*h2*h5-a0*b0*b2*c0*h3*h5-a0*b0*b2*c0*h4*h4-a0*b0*b2*c1*h2*h5-a0*b0*b2*c1*h3*h4-a0*b0*b2*c2*h1*h5-a0*b0*b2*c2*h2*h4-a0*b1*b1*c0*h3*h5-a0*b1*b1*c1*h2*h5-a0*b1*b1*c2*h1*h5-2*a0*b1*b2*c0*h2*h5-a0*b1*b2*c0*h3*h4-2*a0*b1*b2*c1*h1*h5-a0*b1*b2*c1*h2*h4-2*a0*b1*b2*c2*h0*h5-a0*b1*b2*c2*h1*h4-a0*b2*b2*c0*h1*h5-a0*b2*b2*c0*h2*h4-a0*b2*b2*c1*h0*h5-a0*b2*b2*c1*h1*h4-a0*b2*b2*c2*h0*h4+a1*a1*a1*c0*h8*h11-a1*a1*a1*c2*h7*h10+3*a1*a1*a2*c0*h7*h11+a1*a1*a2*c0*h8*h10+a1*a1*a2*c1*h7*h10-2*a1*a1*a2*c2*h6*h10-a1*a1*b0*c0*h3*h11-a1*a1*b0*c0*h5*h9-a1*a1*b0*c1*h2*h11-a1*a1*b0*c1*h5*h8-a1*a1*b0*c2*h1*h11-a1*a1*b0*c2*h5*h7+a1*a1*b2*c0*h2*h10+a1*a1*b2*c0*h4*h8+a1*a1*b2*c1*h1*h10+a1*a1*b2*c1*h4*h7+a1*a1*b2*c2*h0*h10+a1*a1*b2*c2*h4*h6-a1*a1*c0*c0*h3*h5-a1*a1*c0*c1*h2*h5-a1*a1*c0*c2*h1*h5+a1*a1*c0*c2*h2*h4+a1*a1*c1*c2*h1*h4+a1*a1*c2*c2*h0*h4+3*a1*a2*a2*c0*h6*h11+2*a1*a2*a2*c0*h7*h10+2*a1*a2*a2*c1*h6*h10-2*a1*a2*b0*c0*h2*h11-a1*a2*b0*c0*h3*h10-a1*a2*b0*c0*h4*h9-2*a1*a2*b0*c0*h5*h8-2*a1*a2*b0*c1*h1*h11-a1*a2*b0*c1*h2*h10-a1*a2*b0*c1*h4*h8-2*a1*a2*b0*c1*h5*h7-2*a1*a2*b0*c2*h0*h11-a1*a2*b0*c2*h1*h10-a1*a2*b0*c2*h4*h7-2*a1*a2*b0*c2*h5*h6-a1*a2*b1*c0*h2*h10-a1*a2*b1*c0*h4*h8-a1*a2*b1*c1*h1*h10-a1*a2*b1*c1*h4*h7-a1*a2*b1*c2*h0*h10-a1*a2*b1*c2*h4*h6+a1*a2*b2*c0*h1*h10+a1*a2*b2*c0*h4*h7+a1*a2*b2*c1*h0*h10+a1*a2*b2*c1*h4*h6-2*a1*a2*c0*c0*h2*h5-a1*a2*c0*c0*h3*h4-2*a1*a2*c0*c1*h1*h5-2*a1*a2*c0*c1*h2*h4-2*a1*a2*c0*c2*h0*h5-a1*a2*c1*c1*h1*h4+a1*b0*b0*c0*h4*h5+a1*b0*b0*c1*h3*h5+a1*b0*b0*c2*h2*h5+a1*b0*b1*c0*h3*h5+a1*b0*b1*c1*h2*h5+a1*b0*b1*c2*h1*h5+a1*b0*b2*c0*h2*h5-a1*b0*b2*c0*h3*h4+a1*b0*b2*c1*h1*h5-a1*b0*b2*c1*h2*h4+a1*b0*b2*c2*h0*h5-a1*b0*b2*c2*h1*h4-a1*b1*b2*c0*h2*h4-a1*b1*b2*c1*h1*h4-a1*b1*b2*c2*h0*h4-a1*b2*b2*c0*h1*h4-a1*b2*b2*c1*h0*h4+a2*a2*a2*c0*h6*h10-a2*a2*b0*c0*h1*h11-a2*a2*b0*c0*h2*h10-a2*a2*b0*c0*h4*h8-a2*a2*b0*c0*h5*h7-a2*a2*b0*c1*h0*h11-a2*a2*b0*c1*h1*h10-a2*a2*b0*c1*h4*h7-a2*a2*b0*c1*h5*h6-a2*a2*b0*c2*h0*h10-a2*a2*b0*c2*h4*h6-a2*a2*b1*c0*h1*h10-a2*a2*b1*c0*h4*h7-a2*a2*b1*c1*h0*h10-a2*a2*b1*c1*h4*h6-a2*a2*c0*c0*h1*h5-a2*a2*c0*c0*h2*h4-a2*a2*c0*c1*h0*h5-2*a2*a2*c0*c1*h1*h4-a2*a2*c0*c2*h0*h4-a2*a2*c1*c1*h0*h4+a2*b0*b0*c0*h3*h5+a2*b0*b0*c0*h4*h4+a2*b0*b0*c1*h2*h5+a2*b0*b0*c1*h3*h4+a2*b0*b0*c2*h1*h5+a2*b0*b0*c2*h2*h4+a2*b0*b1*c0*h2*h5+2*a2*b0*b1*c0*h3*h4+a2*b0*b1*c1*h1*h5+2*a2*b0*b1*c1*h2*h4+a2*b0*b1*c2*h0*h5+2*a2*b0*b1*c2*h1*h4+a2*b0*b2*c0*h1*h5+a2*b0*b2*c0*h2*h4+a2*b0*b2*c1*h0*h5+a2*b0*b2*c1*h1*h4+a2*b0*b2*c2*h0*h4+a2*b1*b1*c0*h2*h4+a2*b1*b1*c1*h1*h4+a2*b1*b1*c2*h0*h4+a2*b1*b2*c0*h1*h4+a2*b1*b2*c1*h0*h4,-9/16*a0*a0*a0*a1-53/32*a0*a0*a0*b2-213/32*a0*a0*a1*b1+1019/16*a0*a0*a1*c2-231/32*a0*a0*a2*b0+779/16*a0*a0*a2*c1-157/4*a0*a0*b2*c2-231/32*a0*a1*a1*b0+799/16*a0*a1*a1*c1+547/8*a0*a1*a2*c0-49*a0*a1*b1*c2-67*a0*a1*b2*c1-261/2*a0*a1*c2*c2-47/4*a0*a2*b0*c2-77/2*a0*a2*b1*c1-113/2*a0*a2*b2*c0-249*a0*a2*c1*c2+171/2*a0*b1*b2*c2+177/4*a0*b2*b2*c1+87/2*a0*b2*c2*c2+189/16*a1*a1*a1*c0-43/8*a1*a1*b0*c2-75/4*a1*a1*b1*c1-111/4*a1*a1*b2*c0-247/2*a1*a1*c1*c2-1/4*a1*a2*b0*c1-27*a1*a2*b1*c0-134*a1*a2*c0*c2-235/2*a1*a2*c1*c1+81/2*a1*b0*b2*c2+137/4*a1*b1*b1*c2+143/2*a1*b1*b2*c1+93/2*a1*b1*c2*c2+149/4*a1*b2*b2*c0+93*a1*b2*c1*c2-9*a1*c2*c2*c2+41/8*a2*a2*b0*c0-61*a2*a2*c0*c1+51/2*a2*b0*b1*c2+57/2*a2*b0*b2*c1+27*a2*b0*c2*c2+113/4*a2*b1*b1*c1+119/2*a2*b1*b2*c0+99*a2*b1*c1*c2+63*a2*b2*c0*c2+99/2*a2*b2*c1*c1-27*a2*c1*c2*c2-36*b0*b2*b2*c2-117/2*b1*b1*b2*c2-111/2*b1*b2*b2*c1+18*b1*b2*c2*c2-35/2*b2*b2*b2*c0+18*b2*b2*c1*c2-3/8*a0*a0*a0*b2*h9+a0*a0*a0*c1*h11+a0*a0*a0*c2*h10-9/8*a0*a0*a1*b2*h8-a0*a0*a1*c0*h11-9/8*a0*a0*a2*b2*h7+3/4*a0*a0*a2*c0*h3-a0*a0*a2*c0*h10+3/4*a0*a0*a2*c1*h2-3/2*a0*a0*a2*c2*h1-a0*a0*b1*c0*h5-2*a0*a0*b1*c1*h11-a0*a0*b2*c0*h4-2*a0*a0*b2*c0*h11-2*a0*a0*b2*c1*h10-2*a0*a0*c0*c2*h5-2*a0*a0*c1*c1*h5-2*a0*a0*c1*c2*h4-9/8*a0*a1*a1*b2*h7-9/8*a0*a1*a1*c2*h1-9/4*a0*a1*a2*b2*h6+3/2*a0*a1*a2*c0*h2-3/4*a0*a1*a2*c1*h1-3*a0*a1*a2*c2*h0-33/2*a0*a1*a2*c2*h7+a0*a1*b0*c0*h5+2*a0*a1*b0*c1*h11-2*a0*a1*b1*c0*h11-4*a0*a1*b2*c0*h10+9*a0*a1*b2*c2*h1-4*a0*a1*c0*c2*h4+9/8*a0*a2*a2*b0*h7+9/8*a0*a2*a2*b1*h6+3/2*a0*a2*a2*c0*h1+3/2*a0*a2*a2*c1*h0-33/4*a0*a2*a2*c1*h7-35/4*a0*a2*a2*c2*h6+a0*a2*b0*c0*h4+2*a0*a2*b0*c0*h11+2*a0*a2*b0*c1*h10+2*a0*a2*b1*c0*h10+9*a0*a2*b1*c2*h1+9*a0*a2*b2*c1*h1+19/2*a0*a2*b2*c2*h0+6*a0*a2*b2*c2*h7+2*a0*a2*c0*c0*h5+4*a0*a2*c0*c1*h4+15/2*a0*a2*c2*c2*h1+2*a0*b0*b1*c1*h5+2*a0*b0*b2*c0*h5+2*a0*b0*b2*c1*h4+2*a0*b1*b1*c0*h5+2*a0*b1*b2*c0*h4-15/2*a0*b2*b2*c2*h1-3/8*a1*a1*a1*b2*h6-9/8*a1*a1*a1*c2*h0+9/8*a1*a1*a2*b0*h7+9/8*a1*a1*a2*b1*h6+15/8*a1*a1*a2*c0*h1-3/8*a1*a1*a2*c1*h0-33/2*a1*a1*a2*c2*h6+2*a1*a1*b0*c0*h11+9*a1*a1*b2*c2*h0+2*a1*a1*c0*c0*h5+9/8*a1*a2*a2*b0*h6+3/2*a1*a2*a2*c0*h0+81/4*a1*a2*a2*c0*h7+12*a1*a2*a2*c1*h6+2*a1*a2*b0*c0*h10-33/2*a1*a2*b0*c2*h1-15/2*a1*a2*b1*c2*h0+9*a1*a2*b2*c1*h0+6*a1*a2*b2*c2*h6+2*a1*a2*c0*c0*h4+15/2*a1*a2*c2*c2*h0-2*a1*b0*b0*c1*h5-2*a1*b0*b1*c0*h5+2*a1*b0*b2*c0*h4-15/2*a1*b2*b2*c2*h0+29/4*a2*a2*a2*c0*h6-33/4*a2*a2*b0*c1*h1-35/4*a2*a2*b0*c2*h0-9/2*a2*a2*b0*c2*h7-33/4*a2*a2*b1*c1*h0-9/2*a2*a2*b1*c2*h6-9/2*a2*a2*c0*c2*h1-9/2*a2*a2*c1*c2*h0-2*a2*b0*b0*c0*h5-2*a2*b0*b0*c1*h4-4*a2*b0*b1*c0*h4+6*a2*b0*b2*c2*h1+6*a2*b1*b2*c2*h0-a0*a0*a0*c1*h9*h11-a0*a0*a0*c2*h8*h11-a0*a0*a0*c2*h9*h10+a0*a0*a1*c0*h9*h11-2*a0*a0*a1*c1*h8*h11-2*a0*a0*a1*c2*h7*h11-3*a0*a0*a1*c2*h8*h10+a0*a0*a2*c0*h8*h11+a0*a0*a2*c0*h9*h10-2*a0*a0*a2*c1*h7*h11+a0*a0*a2*c1*h8*h10-2*a0*a0*a2*c2*h6*h11-2*a0*a0*a2*c2*h7*h10+a0*a0*b1*c0*h3*h11+a0*a0*b1*c0*h5*h9+a0*a0*b1*c1*h2*h11+a0*a0*b1*c1*h5*h8+a0*a0*b1*c2*h1*h11+a0*a0*b1*c2*h5*h7+a0*a0*b2*c0*h2*h11+a0*a0*b2*c0*h3*h10+a0*a0*b2*c0*h4*h9+a0*a0*b2*c0*h5*h8+a0*a0*b2*c1*h1*h11+a0*a0*b2*c1*h2*h10+a0*a0*b2*c1*h4*h8+a0*a0*b2*c1*h5*h7+a0*a0*b2*c2*h0*h11+a0*a0*b2*c2*h1*h10+a0*a0*b2*c2*h4*h7+a0*a0*b2*c2*h5*h6+a0*a0*c0*c1*h3*h5+a0*a0*c0*c2*h2*h5+a0*a0*c0*c2*h3*h4+a0*a0*c1*c1*h2*h5+2*a0*a0*c1*c2*h1*h5+a0*a0*c1*c2*h2*h4+a0*a0*c2*c2*h0*h5+a0*a0*c2*c2*h1*h4+2*a0*a1*a1*c0*h8*h11-a0*a1*a1*c1*h7*h11-a0*a1*a1*c2*h6*h11-3*a0*a1*a1*c2*h7*h10+4*a0*a1*a2*c0*h7*h11+2*a0*a1*a2*c0*h8*h10-2*a0*a1*a2*c1*h6*h11+2*a0*a1*a2*c1*h7*h10-4*a0*a1*a2*c2*h6*h10-a0*a1*b0*c0*h3*h11-a0*a1*b0*c0*h5*h9-a0*a1*b0*c1*h2*h11-a0*a1*b0*c1*h5*h8-a0*a1*b0*c2*h1*h11-a0*a1*b0*c2*h5*h7+a0*a1*b1*c0*h2*h11+a0*a1*b1*c0*h5*h8+a0*a1*b1*c1*h1*h11+a0*a1*b1*c1*h5*h7+a0*a1*b1*c2*h0*h11+a0*a1*b1*c2*h5*h6+a0*a1*b2*c0*h1*h11+2*a0*a1*b2*c0*h2*h10+2*a0*a1*b2*c0*h4*h8+a0*a1*b2*c0*h5*h7+a0*a1*b2*c1*h0*h11+2*a0*a1*b2*c1*h1*h10+2*a0*a1*b2*c1*h4*h7+a0*a1*b2*c1*h5*h6+2*a0*a1*b2*c2*h0*h10+2*a0*a1*b2*c2*h4*h6-a0*a1*c0*c0*h3*h5+2*a0*a1*c0*c2*h2*h4+a0*a1*c1*c1*h1*h5+2*a0*a1*c1*c2*h0*h5+2*a0*a1*c1*c2*h1*h4+2*a0*a1*c2*c2*h0*h4+2*a0*a2*a2*c0*h6*h11+2*a0*a2*a2*c0*h7*h10+2*a0*a2*a2*c1*h6*h10-a0*a2*b0*c0*h2*h11-a0*a2*b0*c0*h3*h10-a0*a2*b0*c0*h4*h9-a0*a2*b0*c0*h5*h8-a0*a2*b0*c1*h1*h11-a0*a2*b0*c1*h2*h10-a0*a2*b0*c1*h4*h8-a0*a2*b0*c1*h5*h7-a0*a2*b0*c2*h0*h11-a0*a2*b0*c2*h1*h10-a0*a2*b0*c2*h4*h7-a0*a2*b0*c2*h5*h6+a0*a2*b1*c0*h1*h11-a0*a2*b1*c0*h2*h10-a0*a2*b1*c0*h4*h8+a0*a2*b1*c0*h5*h7+a0*a2*b1*c1*h0*h11-a0*a2*b1*c1*h1*h10-a0*a2*b1*c1*h4*h7+a0*a2*b1*c1*h5*h6-a0*a2*b1*c2*h0*h10-a0*a2*b1*c2*h4*h6+a0*a2*b2*c0*h0*h11+a0*a2*b2*c0*h1*h10+a0*a2*b2*c0*h4*h7+a0*a2*b2*c0*h5*h6+a0*a2*b2*c1*h0*h10+a0*a2*b2*c1*h4*h6-a0*a2*c0*c0*h2*h5-a0*a2*c0*c0*h3*h4-2*a0*a2*c0*c1*h2*h4+a0*a2*c1*c1*h0*h5-a0*a2*c1*c1*h1*h4-a0*b0*b1*c0*h3*h5-a0*b0*b1*c1*h2*h5-a0*b0*b1*c2*h1*h5-a0*b0*b2*c0*h2*h5-a0*b0*b2*c0*h3*h4-a0*b0*b2*c1*h1*h5-a0*b0*b2*c1*h2*h4-a0*b0*b2*c2*h0*h5-a0*b0*b2*c2*h1*h4-a0*b1*b1*c0*h2*h5-a0*b1*b1*c1*h1*h5-a0*b1*b1*c2*h0*h5-2*a0*b1*b2*c0*h1*h5-a0*b1*b2*c0*h2*h4-2*a0*b1*b2*c1*h0*h5-a0*b1*b2*c1*h1*h4-a0*b1*b2*c2*h0*h4-a0*b2*b2*c0*h0*h5-a0*b2*b2*c0*h1*h4-a0*b2*b2*c1*h0*h4+a1*a1*a1*c0*h7*h11-a1*a1*a1*c2*h6*h10+3*a1*a1*a2*c0*h6*h11+a1*a1*a2*c0*h7*h10+a1*a1*a2*c1*h6*h10-a1*a1*b0*c0*h2*h11-a1*a1*b0*c0*h5*h8-a1*a1*b0*c1*h1*h11-a1*a1*b0*c1*h5*h7-a1*a1*b0*c2*h0*h11-a1*a1*b0*c2*h5*h6+a1*a1*b2*c0*h1*h10+a1*a1*b2*c0*h4*h7+a1*a1*b2*c1*h0*h10+a1*a1*b2*c1*h4*h6-a1*a1*c0*c0*h2*h5-a1*a1*c0*c1*h1*h5-a1*a1*c0*c2*h0*h5+a1*a1*c0*c2*h1*h4+a1*a1*c1*c2*h0*h4+2*a1*a2*a2*c0*h6*h10-2*a1*a2*b0*c0*h1*h11-a1*a2*b0*c0*h2*h10-a1*a2*b0*c0*h4*h8-2*a1*a2*b0*c0*h5*h7-2*a1*a2*b0*c1*h0*h11-a1*a2*b0*c1*h1*h10-a1*a2*b0*c1*h4*h7-2*a1*a2*b0*c1*h5*h6-a1*a2*b0*c2*h0*h10-a1*a2*b0*c2*h4*h6-a1*a2*b1*c0*h1*h10-a1*a2*b1*c0*h4*h7-a1*a2*b1*c1*h0*h10-a1*a2*b1*c1*h4*h6+a1*a2*b2*c0*h0*h10+a1*a2*b2*c0*h4*h6-2*a1*a2*c0*c0*h1*h5-a1*a2*c0*c0*h2*h4-2*a1*a2*c0*c1*h0*h5-2*a1*a2*c0*c1*h1*h4-a1*a2*c1*c1*h0*h4+a1*b0*b0*c0*h3*h5+a1*b0*b0*c1*h2*h5+a1*b0*b0*c2*h1*h5+a1*b0*b1*c0*h2*h5+a1*b0*b1*c1*h1*h5+a1*b0*b1*c2*h0*h5+a1*b0*b2*c0*h1*h5-a1*b0*b2*c0*h2*h4+a1*b0*b2*c1*h0*h5-a1*b0*b2*c1*h1*h4-a1*b0*b2*c2*h0*h4-a1*b1*b2*c0*h1*h4-a1*b1*b2*c1*h0*h4-a1*b2*b2*c0*h0*h4-a2*a2*b0*c0*h0*h11-a2*a2*b0*c0*h1*h10-a2*a2*b0*c0*h4*h7-a2*a2*b0*c0*h5*h6-a2*a2*b0*c1*h0*h10-a2*a2*b0*c1*h4*h6-a2*a2*b1*c0*h0*h10-a2*a2*b1*c0*h4*h6-a2*a2*c0*c0*h0*h5-a2*a2*c0*c0*h1*h4-2*a2*a2*c0*c1*h0*h4+a2*b0*b0*c0*h2*h5+a2*b0*b0*c0*h3*h4+a2*b0*b0*c1*h1*h5+a2*b0*b0*c1*h2*h4+a2*b0*b0*c2*h0*h5+a2*b0*b0*c2*h1*h4+a2*b0*b1*c0*h1*h5+2*a2*b0*b1*c0*h2*h4+a2*b0*b1*c1*h0*h5+2*a2*b0*b1*c1*h1*h4+2*a2*b0*b1*c2*h0*h4+a2*b0*b2*c0*h0*h5+a2*b0*b2*c0*h1*h4+a2*b0*b2*c1*h0*h4+a2*b1*b1*c0*h1*h4+a2*b1*b1*c1*h0*h4+a2*b1*b2*c0*h0*h4,-9/64*a0*a0*a0*a0-71/32*a0*a0*a0*b1+365/16*a0*a0*a0*c2-231/32*a0*a0*a1*b0+875/16*a0*a0*a1*c1+623/16*a0*a0*a2*c0-121/4*a0*a0*b1*c2-157/4*a0*a0*b2*c1-275/4*a0*a0*c2*c2+643/16*a0*a1*a1*c0-89/4*a0*a1*b0*c2-49*a0*a1*b1*c1-67*a0*a1*b2*c0-261*a0*a1*c1*c2-47/4*a0*a2*b0*c1-77/2*a0*a2*b1*c0-148*a0*a2*c0*c2-249/2*a0*a2*c1*c1+109/2*a0*b0*b2*c2+165/4*a0*b1*b1*c2+171/2*a0*b1*b2*c1+93/2*a0*b1*c2*c2+177/4*a0*b2*b2*c0+93*a0*b2*c1*c2-9*a0*c2*c2*c2-43/8*a1*a1*b0*c1-75/4*a1*a1*b1*c0-73*a1*a1*c0*c2-247/4*a1*a1*c1*c1-1/4*a1*a2*b0*c0-134*a1*a2*c0*c1+75/2*a1*b0*b1*c2+81/2*a1*b0*b2*c1+27*a1*b0*c2*c2+137/4*a1*b1*b1*c1+143/2*a1*b1*b2*c0+99*a1*b1*c1*c2+63*a1*b2*c0*c2+99/2*a1*b2*c1*c1-27*a1*c1*c2*c2-21/4*a2*a2*c0*c0-11/4*a2*b0*b0*c2+51/2*a2*b0*b1*c1+57/2*a2*b0*b2*c0+60*a2*b0*c1*c2+113/4*a2*b1*b1*c0+69*a2*b1*c0*c2+105/2*a2*b1*c1*c1+69*a2*b2*c0*c1-9*a2*c0*c2*c2-27*a2*c1*c1*c2-78*b0*b1*b2*c2-36*b0*b2*b2*c1+18*b0*b2*c2*c2-41/2*b1*b1*b1*c2-117/2*b1*b1*b2*c1+9*b1*b1*c2*c2-111/2*b1*b2*b2*c0+36*b1*b2*c1*c2+9*b2*b2*c1*c1-3/8*a0*a0*a0*b2*h8-9/8*a0*a0*a1*b2*h7-9/4*a0*a0*a1*c2*h1-9/8*a0*a0*a2*b2*h6+3/4*a0*a0*a2*c0*h2-3/2*a0*a0*a2*c1*h1-3/2*a0*a0*a2*c2*h0-33/2*a0*a0*a2*c2*h7-2*a0*a0*b1*c0*h11-2*a0*a0*b2*c0*h10+9*a0*a0*b2*c2*h1-2*a0*a0*c0*c1*h5-2*a0*a0*c0*c2*h4-9/8*a0*a1*a1*b2*h6-9/8*a0*a1*a1*c1*h1-27/8*a0*a1*a1*c2*h0-33/4*a0*a1*a1*c2*h7+9/4*a0*a1*a2*b0*h7+9/4*a0*a1*a2*b1*h6+3/2*a0*a1*a2*c0*h1-3/4*a0*a1*a2*c1*h0-33/2*a0*a1*a2*c1*h7-34*a0*a1*a2*c2*h6+2*a0*a1*b0*c0*h11+9*a0*a1*b1*c2*h1+9*a0*a1*b2*c1*h1+37/2*a0*a1*b2*c2*h0+6*a0*a1*b2*c2*h7+2*a0*a1*c0*c0*h5+15/2*a0*a1*c2*c2*h1+9/8*a0*a2*a2*b0*h6+3/2*a0*a2*a2*c0*h0+12*a0*a2*a2*c0*h7+23/2*a0*a2*a2*c1*h6+2*a0*a2*b0*c0*h10-15/2*a0*a2*b0*c2*h1+9*a0*a2*b1*c1*h1-7*a0*a2*b1*c2*h0+6*a0*a2*b1*c2*h7+9*a0*a2*b2*c0*h1+19/2*a0*a2*b2*c1*h0+6*a0*a2*b2*c1*h7+7*a0*a2*b2*c2*h6+2*a0*a2*c0*c0*h4+15*a0*a2*c1*c2*h1+17/2*a0*a2*c2*c2*h0-3*a0*a2*c2*c2*h7+2*a0*b0*b1*c0*h5+2*a0*b0*b2*c0*h4-15*a0*b1*b2*c2*h1-15/2*a0*b2*b2*c1*h1-17/2*a0*b2*b2*c2*h0+3*a0*b2*b2*c2*h7+3/8*a1*a1*a1*b0*h7+3/8*a1*a1*a1*b1*h6+3/8*a1*a1*a1*c0*h1-3/4*a1*a1*a1*c1*h0-33/4*a1*a1*a1*c2*h6+9/8*a1*a1*a2*b0*h6-3/8*a1*a1*a2*c0*h0+81/4*a1*a1*a2*c0*h7+15/4*a1*a1*a2*c1*h6-33/4*a1*a1*b0*c2*h1+3/4*a1*a1*b1*c2*h0+9*a1*a1*b2*c1*h0+6*a1*a1*b2*c2*h6+15/2*a1*a1*c2*c2*h0+27/2*a1*a2*a2*c0*h6-33/2*a1*a2*b0*c1*h1-17/2*a1*a2*b0*c2*h0-9*a1*a2*b0*c2*h7-15/2*a1*a2*b1*c1*h0-3*a1*a2*b1*c2*h6+9*a1*a2*b2*c0*h0+6*a1*a2*b2*c1*h6-9*a1*a2*c0*c2*h1+6*a1*a2*c1*c2*h0-3*a1*a2*c2*c2*h6-2*a1*b0*b0*c0*h5+6*a1*b0*b2*c2*h1-9*a1*b1*b2*c2*h0-15/2*a1*b2*b2*c1*h0+3*a1*b2*b2*c2*h6-33/4*a2*a2*b0*c0*h1-35/4*a2*a2*b0*c1*h0-9/2*a2*a2*b0*c1*h7-11/2*a2*a2*b0*c2*h6-33/4*a2*a2*b1*c0*h0-9/2*a2*a2*b1*c1*h6-9/2*a2*a2*c0*c1*h1-11/2*a2*a2*c0*c2*h0+9*a2*a2*c0*c2*h7-9/2*a2*a2*c1*c1*h0+9*a2*a2*c1*c2*h6-2*a2*b0*b0*c0*h4+6*a2*b0*b1*c2*h1+6*a2*b0*b2*c1*h1+7*a2*b0*b2*c2*h0-6*a2*b0*b2*c2*h7-3*a2*b0*c2*c2*h1+6*a2*b1*b1*c2*h0+6*a2*b1*b2*c1*h0-6*a2*b1*b2*c2*h6-3*a2*b1*c2*c2*h0-6*a2*b2*c0*c2*h1-6*a2*b2*c1*c2*h0+3*b0*b2*b2*c2*h1+3*b1*b2*b2*c2*h0-a0*a0*a0*c1*h8*h11-a0*a0*a0*c2*h7*h11-a0*a0*a0*c2*h8*h10+a0*a0*a1*c0*h8*h11-2*a0*a0*a1*c1*h7*h11-2*a0*a0*a1*c2*h6*h11-3*a0*a0*a1*c2*h7*h10+a0*a0*a2*c0*h7*h11+a0*a0*a2*c0*h8*h10-2*a0*a0*a2*c1*h6*h11+a0*a0*a2*c1*h7*h10-2*a0*a0*a2*c2*h6*h10+a0*a0*b1*c0*h2*h11+a0*a0*b1*c0*h5*h8+a0*a0*b1*c1*h1*h11+a0*a0*b1*c1*h5*h7+a0*a0*b1*c2*h0*h11+a0*a0*b1*c2*h5*h6+a0*a0*b2*c0*h1*h11+a0*a0*b2*c0*h2*h10+a0*a0*b2*c0*h4*h8+a0*a0*b2*c0*h5*h7+a0*a0*b2*c1*h0*h11+a0*a0*b2*c1*h1*h10+a0*a0*b2*c1*h4*h7+a0*a0*b2*c1*h5*h6+a0*a0*b2*c2*h0*h10+a0*a0*b2*c2*h4*h6+a0*a0*c0*c1*h2*h5+a0*a0*c0*c2*h1*h5+a0*a0*c0*c2*h2*h4+a0*a0*c1*c1*h1*h5+2*a0*a0*c1*c2*h0*h5+a0*a0*c1*c2*h1*h4+a0*a0*c2*c2*h0*h4+2*a0*a1*a1*c0*h7*h11-a0*a1*a1*c1*h6*h11-3*a0*a1*a1*c2*h6*h10+4*a0*a1*a2*c0*h6*h11+2*a0*a1*a2*c0*h7*h10+2*a0*a1*a2*c1*h6*h10-a0*a1*b0*c0*h2*h11-a0*a1*b0*c0*h5*h8-a0*a1*b0*c1*h1*h11-a0*a1*b0*c1*h5*h7-a0*a1*b0*c2*h0*h11-a0*a1*b0*c2*h5*h6+a0*a1*b1*c0*h1*h11+a0*a1*b1*c0*h5*h7+a0*a1*b1*c1*h0*h11+a0*a1*b1*c1*h5*h6+a0*a1*b2*c0*h0*h11+2*a0*a1*b2*c0*h1*h10+2*a0*a1*b2*c0*h4*h7+a0*a1*b2*c0*h5*h6+2*a0*a1*b2*c1*h0*h10+2*a0*a1*b2*c1*h4*h6-a0*a1*c0*c0*h2*h5+2*a0*a1*c0*c2*h1*h4+a0*a1*c1*c1*h0*h5+2*a0*a1*c1*c2*h0*h4+2*a0*a2*a2*c0*h6*h10-a0*a2*b0*c0*h1*h11-a0*a2*b0*c0*h2*h10-a0*a2*b0*c0*h4*h8-a0*a2*b0*c0*h5*h7-a0*a2*b0*c1*h0*h11-a0*a2*b0*c1*h1*h10-a0*a2*b0*c1*h4*h7-a0*a2*b0*c1*h5*h6-a0*a2*b0*c2*h0*h10-a0*a2*b0*c2*h4*h6+a0*a2*b1*c0*h0*h11-a0*a2*b1*c0*h1*h10-a0*a2*b1*c0*h4*h7+a0*a2*b1*c0*h5*h6-a0*a2*b1*c1*h0*h10-a0*a2*b1*c1*h4*h6+a0*a2*b2*c0*h0*h10+a0*a2*b2*c0*h4*h6-a0*a2*c0*c0*h1*h5-a0*a2*c0*c0*h2*h4-2*a0*a2*c0*c1*h1*h4-a0*a2*c1*c1*h0*h4-a0*b0*b1*c0*h2*h5-a0*b0*b1*c1*h1*h5-a0*b0*b1*c2*h0*h5-a0*b0*b2*c0*h1*h5-a0*b0*b2*c0*h2*h4-a0*b0*b2*c1*h0*h5-a0*b0*b2*c1*h1*h4-a0*b0*b2*c2*h0*h4-a0*b1*b1*c0*h1*h5-a0*b1*b1*c1*h0*h5-2*a0*b1*b2*c0*h0*h5-a0*b1*b2*c0*h1*h4-a0*b1*b2*c1*h0*h4-a0*b2*b2*c0*h0*h4+a1*a1*a1*c0*h6*h11+a1*a1*a2*c0*h6*h10-a1*a1*b0*c0*h1*h11-a1*a1*b0*c0*h5*h7-a1*a1*b0*c1*h0*h11-a1*a1*b0*c1*h5*h6+a1*a1*b2*c0*h0*h10+a1*a1*b2*c0*h4*h6-a1*a1*c0*c0*h1*h5-a1*a1*c0*c1*h0*h5+a1*a1*c0*c2*h0*h4-2*a1*a2*b0*c0*h0*h11-a1*a2*b0*c0*h1*h10-a1*a2*b0*c0*h4*h7-2*a1*a2*b0*c0*h5*h6-a1*a2*b0*c1*h0*h10-a1*a2*b0*c1*h4*h6-a1*a2*b1*c0*h0*h10-a1*a2*b1*c0*h4*h6-2*a1*a2*c0*c0*h0*h5-a1*a2*c0*c0*h1*h4-2*a1*a2*c0*c1*h0*h4+a1*b0*b0*c0*h2*h5+a1*b0*b0*c1*h1*h5+a1*b0*b0*c2*h0*h5+a1*b0*b1*c0*h1*h5+a1*b0*b1*c1*h0*h5+a1*b0*b2*c0*h0*h5-a1*b0*b2*c0*h1*h4-a1*b0*b2*c1*h0*h4-a1*b1*b2*c0*h0*h4-a2*a2*b0*c0*h0*h10-a2*a2*b0*c0*h4*h6-a2*a2*c0*c0*h0*h4+a2*b0*b0*c0*h1*h5+a2*b0*b0*c0*h2*h4+a2*b0*b0*c1*h0*h5+a2*b0*b0*c1*h1*h4+a2*b0*b0*c2*h0*h4+a2*b0*b1*c0*h0*h5+2*a2*b0*b1*c0*h1*h4+2*a2*b0*b1*c1*h0*h4+a2*b0*b2*c0*h0*h4+a2*b1*b1*c0*h0*h4,-77/32*a0*a0*a0*b0+317/16*a0*a0*a0*c1+719/16*a0*a0*a1*c0-135/8*a0*a0*b0*c2-121/4*a0*a0*b1*c1-157/4*a0*a0*b2*c0-275/2*a0*a0*c1*c2-89/4*a0*a1*b0*c1-49*a0*a1*b1*c0-160*a0*a1*c0*c2-261/2*a0*a1*c1*c1-47/4*a0*a2*b0*c0-148*a0*a2*c0*c1+103/2*a0*b0*b1*c2+109/2*a0*b0*b2*c1+27*a0*b0*c2*c2+165/4*a0*b1*b1*c1+171/2*a0*b1*b2*c0+99*a0*b1*c1*c2+63*a0*b2*c0*c2+99/2*a0*b2*c1*c1-27*a0*c1*c2*c2-43/8*a1*a1*b0*c0-73*a1*a1*c0*c1-33/2*a1*a2*c0*c0+13/4*a1*b0*b0*c2+75/2*a1*b0*b1*c1+81/2*a1*b0*b2*c0+60*a1*b0*c1*c2+137/4*a1*b1*b1*c0+69*a1*b1*c0*c2+105/2*a1*b1*c1*c1+69*a1*b2*c0*c1-9*a1*c0*c2*c2-27*a1*c1*c1*c2-11/4*a2*b0*b0*c1+51/2*a2*b0*b1*c0+30*a2*b0*c0*c2+33*a2*b0*c1*c1+75*a2*b1*c0*c1+39/2*a2*b2*c0*c0-18*a2*c0*c1*c2-9*a2*c1*c1*c1-39/2*b0*b0*b2*c2-42*b0*b1*b1*c2-78*b0*b1*b2*c1+18*b0*b1*c2*c2-36*b0*b2*b2*c0+36*b0*b2*c1*c2-41/2*b1*b1*b1*c1-117/2*b1*b1*b2*c0+18*b1*b1*c1*c2+18*b1*b2*c1*c1-3/8*a0*a0*a0*b2*h7-9/8*a0*a0*a0*c2*h1-9/8*a0*a0*a1*b2*h6-9/4*a0*a0*a1*c1*h1-27/8*a0*a0*a1*c2*h0-33/2*a0*a0*a1*c2*h7+9/8*a0*a0*a2*b0*h7+9/8*a0*a0*a2*b1*h6-3/8*a0*a0*a2*c0*h1-3/8*a0*a0*a2*c1*h0-33/2*a0*a0*a2*c1*h7-35/2*a0*a0*a2*c2*h6+9*a0*a0*b1*c2*h1+9*a0*a0*b2*c1*h1+19/2*a0*a0*b2*c2*h0+6*a0*a0*b2*c2*h7+15/2*a0*a0*c2*c2*h1+9/8*a0*a1*a1*b0*h7+9/8*a0*a1*a1*b1*h6-9/4*a0*a1*a1*c1*h0-33/4*a0*a1*a1*c1*h7-101/4*a0*a1*a1*c2*h6+9/4*a0*a1*a2*b0*h6-3/4*a0*a1*a2*c0*h0+24*a0*a1*a2*c0*h7+13/2*a0*a1*a2*c1*h6-15/2*a0*a1*b0*c2*h1+9*a0*a1*b1*c1*h1+2*a0*a1*b1*c2*h0+6*a0*a1*b1*c2*h7+9*a0*a1*b2*c0*h1+37/2*a0*a1*b2*c1*h0+6*a0*a1*b2*c1*h7+13*a0*a1*b2*c2*h6+15*a0*a1*c1*c2*h1+16*a0*a1*c2*c2*h0-3*a0*a1*c2*c2*h7+13*a0*a2*a2*c0*h6-15/2*a0*a2*b0*c1*h1-8*a0*a2*b0*c2*h0-3*a0*a2*b0*c2*h7+9*a0*a2*b1*c0*h1-7*a0*a2*b1*c1*h0+6*a0*a2*b1*c1*h7-2*a0*a2*b1*c2*h6+19/2*a0*a2*b2*c0*h0+6*a0*a2*b2*c0*h7+7*a0*a2*b2*c1*h6+6*a0*a2*c0*c2*h1+15/2*a0*a2*c1*c1*h1+8*a0*a2*c1*c2*h0-6*a0*a2*c1*c2*h7-3*a0*a2*c2*c2*h6-9*a0*b0*b2*c2*h1-15/2*a0*b1*b1*c2*h1-15*a0*b1*b2*c1*h1-11*a0*b1*b2*c2*h0+6*a0*b1*b2*c2*h7-15/2*a0*b2*b2*c0*h1-17/2*a0*b2*b2*c1*h0+3*a0*b2*b2*c1*h7+3*a0*b2*b2*c2*h6+3/8*a1*a1*a1*b0*h6-3/4*a1*a1*a1*c0*h0+27/4*a1*a1*a1*c0*h7-3/2*a1*a1*a1*c1*h6+21/4*a1*a1*a2*c0*h6-33/4*a1*a1*b0*c1*h1+1/4*a1*a1*b0*c2*h0-9/2*a1*a1*b0*c2*h7+3/4*a1*a1*b1*c1*h0+3/2*a1*a1*b1*c2*h6+9*a1*a1*b2*c0*h0+6*a1*a1*b2*c1*h6-9/2*a1*a1*c0*c2*h1+21/2*a1*a1*c1*c2*h0-3*a1*a1*c2*c2*h6-33/2*a1*a2*b0*c0*h1-17/2*a1*a2*b0*c1*h0-9*a1*a2*b0*c1*h7-5*a1*a2*b0*c2*h6-15/2*a1*a2*b1*c0*h0-3*a1*a2*b1*c1*h6+6*a1*a2*b2*c0*h6-9*a1*a2*c0*c1*h1+4*a1*a2*c0*c2*h0+18*a1*a2*c0*c2*h7-3/2*a1*a2*c1*c1*h0+12*a1*a2*c1*c2*h6+6*a1*b0*b1*c2*h1+6*a1*b0*b2*c1*h1-8*a1*b0*b2*c2*h0-6*a1*b0*b2*c2*h7-3*a1*b0*c2*c2*h1-3/2*a1*b1*b1*c2*h0-9*a1*b1*b2*c1*h0-3*a1*b1*c2*c2*h0-15/2*a1*b2*b2*c0*h0+3*a1*b2*b2*c1*h6-6*a1*b2*c0*c2*h1-6*a1*b2*c1*c2*h0-35/4*a2*a2*b0*c0*h0-9/2*a2*a2*b0*c0*h7-11/2*a2*a2*b0*c1*h6-9/2*a2*a2*b1*c0*h6-9/2*a2*a2*c0*c0*h1-10*a2*a2*c0*c1*h0+9*a2*a2*c0*c1*h7+9*a2*a2*c0*c2*h6+9*a2*a2*c1*c1*h6+6*a2*b0*b0*c2*h1+6*a2*b0*b1*c1*h1+13*a2*b0*b1*c2*h0-6*a2*b0*b1*c2*h7+6*a2*b0*b2*c0*h1+7*a2*b0*b2*c1*h0-6*a2*b0*b2*c1*h7-6*a2*b0*b2*c2*h6-6*a2*b0*c1*c2*h1-3*a2*b0*c2*c2*h0+6*a2*b1*b1*c1*h0-6*a2*b1*b1*c2*h6+6*a2*b1*b2*c0*h0-6*a2*b1*b2*c1*h6-6*a2*b1*c0*c2*h1-12*a2*b1*c1*c2*h0-6*a2*b2*c0*c1*h1-6*a2*b2*c0*c2*h0-6*a2*b2*c1*c1*h0+6*b0*b1*b2*c2*h1+3*b0*b2*b2*c1*h1+3*b0*b2*b2*c2*h0+6*b1*b1*b2*c2*h0+3*b1*b2*b2*c1*h0-a0*a0*a0*c1*h7*h11-a0*a0*a0*c2*h6*h11-a0*a0*a0*c2*h7*h10+a0*a0*a1*c0*h7*h11-2*a0*a0*a1*c1*h6*h11-3*a0*a0*a1*c2*h6*h10+a0*a0*a2*c0*h6*h11+a0*a0*a2*c0*h7*h10+a0*a0*a2*c1*h6*h10+a0*a0*b1*c0*h1*h11+a0*a0*b1*c0*h5*h7+a0*a0*b1*c1*h0*h11+a0*a0*b1*c1*h5*h6+a0*a0*b2*c0*h0*h11+a0*a0*b2*c0*h1*h10+a0*a0*b2*c0*h4*h7+a0*a0*b2*c0*h5*h6+a0*a0*b2*c1*h0*h10+a0*a0*b2*c1*h4*h6+a0*a0*c0*c1*h1*h5+a0*a0*c0*c2*h0*h5+a0*a0*c0*c2*h1*h4+a0*a0*c1*c1*h0*h5+a0*a0*c1*c2*h0*h4+2*a0*a1*a1*c0*h6*h11+2*a0*a1*a2*c0*h6*h10-a0*a1*b0*c0*h1*h11-a0*a1*b0*c0*h5*h7-a0*a1*b0*c1*h0*h11-a0*a1*b0*c1*h5*h6+a0*a1*b1*c0*h0*h11+a0*a1*b1*c0*h5*h6+2*a0*a1*b2*c0*h0*h10+2*a0*a1*b2*c0*h4*h6-a0*a1*c0*c0*h1*h5+2*a0*a1*c0*c2*h0*h4-a0*a2*b0*c0*h0*h11-a0*a2*b0*c0*h1*h10-a0*a2*b0*c0*h4*h7-a0*a2*b0*c0*h5*h6-a0*a2*b0*c1*h0*h10-a0*a2*b0*c1*h4*h6-a0*a2*b1*c0*h0*h10-a0*a2*b1*c0*h4*h6-a0*a2*c0*c0*h0*h5-a0*a2*c0*c0*h1*h4-2*a0*a2*c0*c1*h0*h4-a0*b0*b1*c0*h1*h5-a0*b0*b1*c1*h0*h5-a0*b0*b2*c0*h0*h5-a0*b0*b2*c0*h1*h4-a0*b0*b2*c1*h0*h4-a0*b1*b1*c0*h0*h5-a0*b1*b2*c0*h0*h4-a1*a1*b0*c0*h0*h11-a1*a1*b0*c0*h5*h6-a1*a1*c0*c0*h0*h5-a1*a2*b0*c0*h0*h10-a1*a2*b0*c0*h4*h6-a1*a2*c0*c0*h0*h4+a1*b0*b0*c0*h1*h5+a1*b0*b0*c1*h0*h5+a1*b0*b1*c0*h0*h5-a1*b0*b2*c0*h0*h4+a2*b0*b0*c0*h0*h5+a2*b0*b0*c0*h1*h4+a2*b0*b0*c1*h0*h4+2*a2*b0*b1*c0*h0*h4,111/4*a0*a0*a2*a2+231/4*a0*a1*a1*a2-299/4*a0*a1*a2*b2-143/8*a0*a2*a2*b1-112*a0*a2*a2*c2+113/2*a0*a2*b2*b2+5*a1*a1*a1*a1-103/8*a1*a1*a1*b2-153/8*a1*a1*a2*b1-111*a1*a1*a2*c2+111/4*a1*a1*b2*b2-9/8*a1*a2*a2*b0-78*a1*a2*a2*c1+72*a1*a2*b1*b2+186*a1*a2*b2*c2-149/4*a1*b2*b2*b2-19/2*a2*a2*a2*c0+97/8*a2*a2*b0*b2+33/4*a2*a2*b1*b1+84*a2*a2*b1*c2+87*a2*a2*b2*c1+26*a2*a2*c2*c2-363/4*a2*b1*b2*b2-61*a2*b2*b2*c2+35/2*b2*b2*b2*b2+3/4*a0*a0*a0*a2*h11+3/8*a0*a0*a0*b2*h5+9/4*a0*a0*a1*a2*h10+9/8*a0*a0*a1*b2*h4-2*a0*a0*a1*b2*h11-2*a0*a0*a1*c2*h5+9/4*a0*a0*a2*a2*h9-3/4*a0*a0*a2*b0*h5-3/4*a0*a0*a2*b1*h4-2*a0*a0*a2*b1*h11+3/8*a0*a0*a2*b2*h3-2*a0*a0*a2*b2*h10-2*a0*a0*a2*c1*h5-2*a0*a0*a2*c2*h4-4*a0*a0*a2*c2*h11+2*a0*a0*b1*b2*h5+a0*a0*b2*b2*h4+2*a0*a0*b2*b2*h11+4*a0*a0*b2*c2*h5+9/4*a0*a1*a1*a2*h9-a0*a1*a1*b1*h11+9/8*a0*a1*a1*b2*h3-3*a0*a1*a1*b2*h10-a0*a1*a1*c1*h5-3*a0*a1*a1*c2*h4-2*a0*a1*a1*c2*h11+9/2*a0*a1*a2*a2*h8-3/2*a0*a1*a2*b0*h4+4*a0*a1*a2*b0*h11-3/2*a0*a1*a2*b1*h3+2*a0*a1*a2*b1*h10+3/4*a0*a1*a2*b2*h2+4*a0*a1*a2*c0*h5+2*a0*a1*a2*c1*h4-4*a0*a1*a2*c1*h11-8*a0*a1*a2*c2*h10+a0*a1*b1*b1*h5+2*a0*a1*b1*b2*h4+4*a0*a1*b1*b2*h11+4*a0*a1*b1*c2*h5+4*a0*a1*b2*b2*h10+4*a0*a1*b2*c1*h5+8*a0*a1*b2*c2*h4+3/2*a0*a2*a2*a2*h7-3/2*a0*a2*a2*b0*h3+2*a0*a2*a2*b0*h10-3/2*a0*a2*a2*b1*h2+3/4*a0*a2*a2*b2*h1+2*a0*a2*a2*c0*h4+4*a0*a2*a2*c0*h11+4*a0*a2*a2*c1*h10-a0*a2*b1*b1*h4+2*a0*a2*b1*b1*h11+4*a0*a2*b1*c1*h5-4*a0*b0*b2*b2*h5-6*a0*b1*b1*b2*h5-4*a0*b1*b2*b2*h4+3/4*a1*a1*a1*a2*h8+a1*a1*a1*b0*h11+3/8*a1*a1*a1*b2*h2+a1*a1*a1*c0*h5-2*a1*a1*a1*c2*h10+9/4*a1*a1*a2*a2*h7-3/4*a1*a1*a2*b0*h3+a1*a1*a2*b0*h10-3/4*a1*a1*a2*b1*h2+3/8*a1*a1*a2*b2*h1+a1*a1*a2*c0*h4+6*a1*a1*a2*c0*h11+2*a1*a1*a2*c1*h10-a1*a1*b0*b1*h5+a1*a1*b0*b2*h4-2*a1*a1*b0*b2*h11-2*a1*a1*b0*c2*h5+2*a1*a1*b1*b2*h10+2*a1*a1*b1*c2*h4-2*a1*a1*b2*c0*h5+2*a1*a1*b2*c1*h4+3/2*a1*a2*a2*a2*h6-3/2*a1*a2*a2*b0*h2-3/2*a1*a2*a2*b1*h1+3/4*a1*a2*a2*b2*h0+4*a1*a2*a2*c0*h10-2*a1*a2*b0*b0*h5-2*a1*a2*b0*b1*h4-4*a1*a2*b0*b1*h11-4*a1*a2*b0*c1*h5-2*a1*a2*b1*b1*h10-4*a1*a2*b1*c0*h5-4*a1*a2*b1*c1*h4+4*a1*b0*b1*b2*h5-4*a1*b0*b2*b2*h4-2*a1*b1*b1*b2*h4-3/2*a2*a2*a2*b0*h1-3/2*a2*a2*a2*b1*h0-a2*a2*b0*b0*h4-2*a2*a2*b0*b0*h11-4*a2*a2*b0*b1*h10-4*a2*a2*b0*c0*h5-4*a2*a2*b0*c1*h4-4*a2*a2*b1*c0*h4+4*a2*b0*b0*b2*h5+2*a2*b0*b1*b1*h5+8*a2*b0*b1*b2*h4+2*a2*b1*b1*b1*h4+a0*a0*a0*b1*h11*h11+2*a0*a0*a0*b2*h10*h11+2*a0*a0*a0*c1*h5*h11+2*a0*a0*a0*c2*h4*h11+2*a0*a0*a0*c2*h5*h10-a0*a0*a1*b0*h11*h11+2*a0*a0*a1*b1*h10*h11+2*a0*a0*a1*b2*h9*h11+3*a0*a0*a1*b2*h10*h10-2*a0*a0*a1*c0*h5*h11+2*a0*a0*a1*c1*h4*h11+2*a0*a0*a1*c1*h5*h10+2*a0*a0*a1*c2*h3*h11+6*a0*a0*a1*c2*h4*h10+2*a0*a0*a1*c2*h5*h9-2*a0*a0*a2*b0*h10*h11+2*a0*a0*a2*b1*h9*h11-a0*a0*a2*b1*h10*h10+2*a0*a0*a2*b2*h8*h11+2*a0*a0*a2*b2*h9*h10-2*a0*a0*a2*c0*h4*h11-2*a0*a0*a2*c0*h5*h10+2*a0*a0*a2*c1*h3*h11-2*a0*a0*a2*c1*h4*h10+2*a0*a0*a2*c1*h5*h9+2*a0*a0*a2*c2*h2*h11+2*a0*a0*a2*c2*h3*h10+2*a0*a0*a2*c2*h4*h9+2*a0*a0*a2*c2*h5*h8-2*a0*a0*b0*b1*h5*h11-2*a0*a0*b0*b2*h4*h11-2*a0*a0*b0*b2*h5*h10-a0*a0*b0*c1*h5*h5-2*a0*a0*b0*c2*h4*h5-a0*a0*b1*b1*h4*h11-a0*a0*b1*b1*h5*h10-2*a0*a0*b1*b2*h3*h11-2*a0*a0*b1*b2*h4*h10-2*a0*a0*b1*b2*h5*h9-a0*a0*b1*c0*h5*h5-2*a0*a0*b1*c1*h4*h5-2*a0*a0*b1*c2*h3*h5-a0*a0*b1*c2*h4*h4-a0*a0*b2*b2*h2*h11-a0*a0*b2*b2*h3*h10-a0*a0*b2*b2*h4*h9-a0*a0*b2*b2*h5*h8-2*a0*a0*b2*c0*h4*h5-2*a0*a0*b2*c1*h3*h5-a0*a0*b2*c1*h4*h4-2*a0*a0*b2*c2*h2*h5-2*a0*a0*b2*c2*h3*h4-2*a0*a1*a1*b0*h10*h11+a0*a1*a1*b1*h9*h11+a0*a1*a1*b2*h8*h11+3*a0*a1*a1*b2*h9*h10-2*a0*a1*a1*c0*h4*h11-2*a0*a1*a1*c0*h5*h10+a0*a1*a1*c1*h3*h11+a0*a1*a1*c1*h5*h9+a0*a1*a1*c2*h2*h11+3*a0*a1*a1*c2*h3*h10+3*a0*a1*a1*c2*h4*h9+a0*a1*a1*c2*h5*h8-4*a0*a1*a2*b0*h9*h11-2*a0*a1*a2*b0*h10*h10+2*a0*a1*a2*b1*h8*h11-2*a0*a1*a2*b1*h9*h10+2*a0*a1*a2*b2*h7*h11+4*a0*a1*a2*b2*h8*h10-4*a0*a1*a2*c0*h3*h11-4*a0*a1*a2*c0*h4*h10-4*a0*a1*a2*c0*h5*h9+2*a0*a1*a2*c1*h2*h11-2*a0*a1*a2*c1*h3*h10-2*a0*a1*a2*c1*h4*h9+2*a0*a1*a2*c1*h5*h8+2*a0*a1*a2*c2*h1*h11+4*a0*a1*a2*c2*h2*h10+4*a0*a1*a2*c2*h4*h8+2*a0*a1*a2*c2*h5*h7+2*a0*a1*b0*b0*h5*h11-4*a0*a1*b0*b2*h4*h10+2*a0*a1*b0*c0*h5*h5-2*a0*a1*b0*c2*h4*h4-a0*a1*b1*b1*h3*h11-a0*a1*b1*b1*h5*h9-2*a0*a1*b1*b2*h2*h11-2*a0*a1*b1*b2*h3*h10-2*a0*a1*b1*b2*h4*h9-2*a0*a1*b1*b2*h5*h8-2*a0*a1*b1*c1*h3*h5-2*a0*a1*b1*c2*h2*h5-2*a0*a1*b1*c2*h3*h4-a0*a1*b2*b2*h1*h11-2*a0*a1*b2*b2*h2*h10-2*a0*a1*b2*b2*h4*h8-a0*a1*b2*b2*h5*h7-2*a0*a1*b2*c0*h4*h4-2*a0*a1*b2*c1*h2*h5-2*a0*a1*b2*c1*h3*h4-2*a0*a1*b2*c2*h1*h5-4*a0*a1*b2*c2*h2*h4-2*a0*a2*a2*b0*h8*h11-2*a0*a2*a2*b0*h9*h10+a0*a2*a2*b1*h7*h11-2*a0*a2*a2*b1*h8*h10+a0*a2*a2*b2*h6*h11+a0*a2*a2*b2*h7*h10-2*a0*a2*a2*c0*h2*h11-2*a0*a2*a2*c0*h3*h10-2*a0*a2*a2*c0*h4*h9-2*a0*a2*a2*c0*h5*h8+a0*a2*a2*c1*h1*h11-2*a0*a2*a2*c1*h2*h10-2*a0*a2*a2*c1*h4*h8+a0*a2*a2*c1*h5*h7+a0*a2*a2*c2*h0*h11+a0*a2*a2*c2*h1*h10+a0*a2*a2*c2*h4*h7+a0*a2*a2*c2*h5*h6+2*a0*a2*b0*b0*h4*h11+2*a0*a2*b0*b0*h5*h10+4*a0*a2*b0*b1*h4*h10+4*a0*a2*b0*c0*h4*h5+2*a0*a2*b0*c1*h4*h4-a0*a2*b1*b1*h2*h11+a0*a2*b1*b1*h3*h10+a0*a2*b1*b1*h4*h9-a0*a2*b1*b1*h5*h8-2*a0*a2*b1*b2*h1*h11-2*a0*a2*b1*b2*h5*h7+2*a0*a2*b1*c0*h4*h4-2*a0*a2*b1*c1*h2*h5+2*a0*a2*b1*c1*h3*h4-2*a0*a2*b1*c2*h1*h5-a0*a2*b2*b2*h0*h11-a0*a2*b2*b2*h1*h10-a0*a2*b2*b2*h4*h7-a0*a2*b2*b2*h5*h6-2*a0*a2*b2*c1*h1*h5-2*a0*a2*b2*c2*h0*h5-2*a0*a2*b2*c2*h1*h4+a0*b0*b0*b1*h5*h5+2*a0*b0*b0*b2*h4*h5+2*a0*b0*b1*b1*h4*h5+4*a0*b0*b1*b2*h3*h5+2*a0*b0*b1*b2*h4*h4+2*a0*b0*b2*b2*h2*h5+2*a0*b0*b2*b2*h3*h4+a0*b1*b1*b1*h3*h5+3*a0*b1*b1*b2*h2*h5+a0*b1*b1*b2*h3*h4+3*a0*b1*b2*b2*h1*h5+2*a0*b1*b2*b2*h2*h4+a0*b2*b2*b2*h0*h5+a0*b2*b2*b2*h1*h4-a1*a1*a1*b0*h9*h11+a1*a1*a1*b2*h8*h10-a1*a1*a1*c0*h3*h11-a1*a1*a1*c0*h5*h9+a1*a1*a1*c2*h2*h10+a1*a1*a1*c2*h4*h8-3*a1*a1*a2*b0*h8*h11-a1*a1*a2*b0*h9*h10-a1*a1*a2*b1*h8*h10+2*a1*a1*a2*b2*h7*h10-3*a1*a1*a2*c0*h2*h11-a1*a1*a2*c0*h3*h10-a1*a1*a2*c0*h4*h9-3*a1*a1*a2*c0*h5*h8-a1*a1*a2*c1*h2*h10-a1*a1*a2*c1*h4*h8+2*a1*a1*a2*c2*h1*h10+2*a1*a1*a2*c2*h4*h7+a1*a1*b0*b0*h4*h11+a1*a1*b0*b0*h5*h10+a1*a1*b0*b1*h3*h11+a1*a1*b0*b1*h5*h9+a1*a1*b0*b2*h2*h11-a1*a1*b0*b2*h3*h10-a1*a1*b0*b2*h4*h9+a1*a1*b0*b2*h5*h8+2*a1*a1*b0*c0*h4*h5+a1*a1*b0*c1*h3*h5+a1*a1*b0*c2*h2*h5-a1*a1*b0*c2*h3*h4-a1*a1*b1*b2*h2*h10-a1*a1*b1*b2*h4*h8+a1*a1*b1*c0*h3*h5-a1*a1*b1*c2*h2*h4-a1*a1*b2*b2*h1*h10-a1*a1*b2*b2*h4*h7+a1*a1*b2*c0*h2*h5-a1*a1*b2*c0*h3*h4-a1*a1*b2*c1*h2*h4-2*a1*a1*b2*c2*h1*h4-3*a1*a2*a2*b0*h7*h11-2*a1*a2*a2*b0*h8*h10-2*a1*a2*a2*b1*h7*h10+a1*a2*a2*b2*h6*h10-3*a1*a2*a2*c0*h1*h11-2*a1*a2*a2*c0*h2*h10-2*a1*a2*a2*c0*h4*h8-3*a1*a2*a2*c0*h5*h7-2*a1*a2*a2*c1*h1*h10-2*a1*a2*a2*c1*h4*h7+a1*a2*a2*c2*h0*h10+a1*a2*a2*c2*h4*h6+2*a1*a2*b0*b0*h3*h11+2*a1*a2*b0*b0*h4*h10+2*a1*a2*b0*b0*h5*h9+2*a1*a2*b0*b1*h2*h11+2*a1*a2*b0*b1*h3*h10+2*a1*a2*b0*b1*h4*h9+2*a1*a2*b0*b1*h5*h8+2*a1*a2*b0*b2*h1*h11+2*a1*a2*b0*b2*h5*h7+4*a1*a2*b0*c0*h3*h5+2*a1*a2*b0*c0*h4*h4+2*a1*a2*b0*c1*h2*h5+2*a1*a2*b0*c1*h3*h4+2*a1*a2*b0*c2*h1*h5+a1*a2*b1*b1*h2*h10+a1*a2*b1*b1*h4*h8+2*a1*a2*b1*c0*h2*h5+2*a1*a2*b1*c0*h3*h4+2*a1*a2*b1*c1*h2*h4-a1*a2*b2*b2*h0*h10-a1*a2*b2*b2*h4*h6+2*a1*a2*b2*c0*h1*h5-2*a1*a2*b2*c2*h0*h4-a1*b0*b0*b0*h5*h5-2*a1*b0*b0*b1*h4*h5-2*a1*b0*b0*b2*h3*h5+a1*b0*b0*b2*h4*h4-a1*b0*b1*b1*h3*h5-2*a1*b0*b1*b2*h2*h5+2*a1*b0*b1*b2*h3*h4-a1*b0*b2*b2*h1*h5+2*a1*b0*b2*b2*h2*h4+a1*b1*b1*b2*h2*h4+2*a1*b1*b2*b2*h1*h4+a1*b2*b2*b2*h0*h4-a2*a2*a2*b0*h6*h11-a2*a2*a2*b0*h7*h10-a2*a2*a2*b1*h6*h10-a2*a2*a2*c0*h0*h11-a2*a2*a2*c0*h1*h10-a2*a2*a2*c0*h4*h7-a2*a2*a2*c0*h5*h6-a2*a2*a2*c1*h0*h10-a2*a2*a2*c1*h4*h6+a2*a2*b0*b0*h2*h11+a2*a2*b0*b0*h3*h10+a2*a2*b0*b0*h4*h9+a2*a2*b0*b0*h5*h8+a2*a2*b0*b1*h1*h11+2*a2*a2*b0*b1*h2*h10+2*a2*a2*b0*b1*h4*h8+a2*a2*b0*b1*h5*h7+a2*a2*b0*b2*h0*h11+a2*a2*b0*b2*h1*h10+a2*a2*b0*b2*h4*h7+a2*a2*b0*b2*h5*h6+2*a2*a2*b0*c0*h2*h5+2*a2*a2*b0*c0*h3*h4+a2*a2*b0*c1*h1*h5+2*a2*a2*b0*c1*h2*h4+a2*a2*b0*c2*h0*h5+a2*a2*b0*c2*h1*h4+a2*a2*b1*b1*h1*h10+a2*a2*b1*b1*h4*h7+a2*a2*b1*b2*h0*h10+a2*a2*b1*b2*h4*h6+a2*a2*b1*c0*h1*h5+2*a2*a2*b1*c0*h2*h4+2*a2*a2*b1*c1*h1*h4+a2*a2*b1*c2*h0*h4+a2*a2*b2*c0*h0*h5+a2*a2*b2*c0*h1*h4+a2*a2*b2*c1*h0*h4-2*a2*b0*b0*b0*h4*h5-2*a2*b0*b0*b1*h3*h5-3*a2*b0*b0*b1*h4*h4-2*a2*b0*b0*b2*h2*h5-2*a2*b0*b0*b2*h3*h4-a2*b0*b1*b1*h2*h5-3*a2*b0*b1*b1*h3*h4-2*a2*b0*b1*b2*h1*h5-4*a2*b0*b1*b2*h2*h4-a2*b0*b2*b2*h0*h5-a2*b0*b2*b2*h1*h4-a2*b1*b1*b1*h2*h4-2*a2*b1*b1*b2*h1*h4-a2*b1*b2*b2*h0*h4,471/8*a0*a0*a1*a2-337/8*a0*a0*a2*b2+163/8*a0*a1*a1*a1-347/8*a0*a1*a1*b2-191/4*a0*a1*a2*b1-245*a0*a1*a2*c2+67*a0*a1*b2*b2-47/8*a0*a2*a2*b0-179/2*a0*a2*a2*c1+95*a0*a2*b1*b2+200*a0*a2*b2*c2-177/4*a0*b2*b2*b2-67/8*a1*a1*a1*b1-81/2*a1*a1*a1*c2-57/8*a1*a1*a2*b0-177/2*a1*a1*a2*c1+93/2*a1*a1*b1*b2+99*a1*a1*b2*c2-39*a1*a2*a2*c0+181/4*a1*a2*b0*b2+27*a1*a2*b1*b1+180*a1*a2*b1*c2+186*a1*a2*b2*c1+52*a1*a2*c2*c2-435/4*a1*b1*b2*b2-61*a1*b2*b2*c2+25/8*a2*a2*b0*b1+53*a2*a2*b0*c2+84*a2*a2*b1*c1+73/2*a2*a2*b2*c0+58*a2*a2*c1*c2-239/4*a2*b0*b2*b2-351/4*a2*b1*b1*b2-128*a2*b1*b2*c2-67*a2*b2*b2*c1+18*a2*b2*c2*c2+73*b1*b2*b2*b2-9*b2*b2*b2*c2+3/4*a0*a0*a0*a2*h10+3/8*a0*a0*a0*b2*h4-a0*a0*a0*b2*h11-a0*a0*a0*c2*h5+9/4*a0*a0*a1*a2*h9-2*a0*a0*a1*b1*h11+9/8*a0*a0*a1*b2*h3-3*a0*a0*a1*b2*h10-2*a0*a0*a1*c1*h5-3*a0*a0*a1*c2*h4-4*a0*a0*a1*c2*h11+9/4*a0*a0*a2*a2*h8-3/4*a0*a0*a2*b0*h4+a0*a0*a2*b0*h11-3/4*a0*a0*a2*b1*h3+a0*a0*a2*b1*h10+3/8*a0*a0*a2*b2*h2+a0*a0*a2*c0*h5+a0*a0*a2*c1*h4-4*a0*a0*a2*c1*h11-4*a0*a0*a2*c2*h10+a0*a0*b0*b2*h5+a0*a0*b1*b1*h5+a0*a0*b1*b2*h4+4*a0*a0*b1*b2*h11+4*a0*a0*b1*c2*h5+2*a0*a0*b2*b2*h10+4*a0*a0*b2*c1*h5+4*a0*a0*b2*c2*h4+9/4*a0*a1*a1*a2*h8+2*a0*a1*a1*b0*h11+9/8*a0*a1*a1*b2*h2+2*a0*a1*a1*c0*h5-2*a0*a1*a1*c1*h11-6*a0*a1*a1*c2*h10+9/4*a0*a1*a2*a2*h7-3/2*a0*a1*a2*b0*h3+2*a0*a1*a2*b0*h10-3/2*a0*a1*a2*b1*h2+3*a0*a1*a2*b2*h1+2*a0*a1*a2*c0*h4+8*a0*a1*a2*c0*h11+4*a0*a1*a2*c1*h10+2*a0*a1*b0*b2*h4+2*a0*a1*b1*b1*h11+4*a0*a1*b1*b2*h10+4*a0*a1*b1*c1*h5+4*a0*a1*b1*c2*h4+4*a0*a1*b2*c1*h4+3/2*a0*a2*a2*a2*h6-3/2*a0*a2*a2*b0*h2-3/8*a0*a2*a2*b1*h1+3/4*a0*a2*a2*b2*h0+33/4*a0*a2*a2*b2*h7+4*a0*a2*a2*c0*h10+9*a0*a2*a2*c2*h1-a0*a2*b0*b0*h5-2*a0*a2*b0*b1*h4-2*a0*a2*b1*b1*h10-4*a0*a2*b1*c1*h4-9*a0*a2*b2*b2*h1-8*a0*b0*b1*b2*h5-4*a0*b0*b2*b2*h4-2*a0*b1*b1*b1*h5-2*a0*b1*b1*b2*h4+3/4*a1*a1*a1*a2*h7+3/8*a1*a1*a1*b2*h1+2*a1*a1*a1*c0*h11-3/4*a1*a1*a2*b0*h2-3/4*a1*a1*a2*b1*h1+21/8*a1*a1*a2*b2*h0+2*a1*a1*a2*c0*h10-a1*a1*b0*b0*h5-2*a1*a1*b0*b1*h11+2*a1*a1*b0*b2*h10-2*a1*a1*b0*c1*h5+2*a1*a1*b0*c2*h4-2*a1*a1*b1*c0*h5+2*a1*a1*b2*c0*h4-15/4*a1*a2*a2*b0*h1-21/8*a1*a2*a2*b1*h0+33/4*a1*a2*a2*b2*h6+9*a1*a2*a2*c2*h0-a1*a2*b0*b0*h4-4*a1*a2*b0*b0*h11-4*a1*a2*b0*b1*h10-8*a1*a2*b0*c0*h5-4*a1*a2*b0*c1*h4-4*a1*a2*b1*c0*h4-9*a1*a2*b2*b2*h0+4*a1*b0*b0*b2*h5+2*a1*b0*b1*b1*h5-4*a1*b0*b1*b2*h4-3/2*a2*a2*a2*b0*h0-15/2*a2*a2*a2*b0*h7-15/2*a2*a2*a2*b1*h6-15/2*a2*a2*a2*c0*h1-15/2*a2*a2*a2*c1*h0-2*a2*a2*b0*b0*h10+33/4*a2*a2*b0*b2*h1-4*a2*a2*b0*c0*h4+33/4*a2*a2*b1*b2*h0+4*a2*b0*b0*b1*h5+4*a2*b0*b0*b2*h4+6*a2*b0*b1*b1*h4+a0*a0*a0*b1*h10*h11+a0*a0*a0*b2*h9*h11+a0*a0*a0*b2*h10*h10+a0*a0*a0*c1*h4*h11+a0*a0*a0*c1*h5*h10+a0*a0*a0*c2*h3*h11+2*a0*a0*a0*c2*h4*h10+a0*a0*a0*c2*h5*h9-a0*a0*a1*b0*h10*h11+2*a0*a0*a1*b1*h9*h11+2*a0*a0*a1*b2*h8*h11+3*a0*a0*a1*b2*h9*h10-a0*a0*a1*c0*h4*h11-a0*a0*a1*c0*h5*h10+2*a0*a0*a1*c1*h3*h11+2*a0*a0*a1*c1*h5*h9+2*a0*a0*a1*c2*h2*h11+3*a0*a0*a1*c2*h3*h10+3*a0*a0*a1*c2*h4*h9+2*a0*a0*a1*c2*h5*h8-a0*a0*a2*b0*h9*h11-a0*a0*a2*b0*h10*h10+2*a0*a0*a2*b1*h8*h11-a0*a0*a2*b1*h9*h10+2*a0*a0*a2*b2*h7*h11+2*a0*a0*a2*b2*h8*h10-a0*a0*a2*c0*h3*h11-2*a0*a0*a2*c0*h4*h10-a0*a0*a2*c0*h5*h9+2*a0*a0*a2*c1*h2*h11-a0*a0*a2*c1*h3*h10-a0*a0*a2*c1*h4*h9+2*a0*a0*a2*c1*h5*h8+2*a0*a0*a2*c2*h1*h11+2*a0*a0*a2*c2*h2*h10+2*a0*a0*a2*c2*h4*h8+2*a0*a0*a2*c2*h5*h7-a0*a0*b0*b1*h4*h11-a0*a0*b0*b1*h5*h10-a0*a0*b0*b2*h3*h11-2*a0*a0*b0*b2*h4*h10-a0*a0*b0*b2*h5*h9-a0*a0*b0*c1*h4*h5-a0*a0*b0*c2*h3*h5-a0*a0*b0*c2*h4*h4-a0*a0*b1*b1*h3*h11-a0*a0*b1*b1*h5*h9-2*a0*a0*b1*b2*h2*h11-a0*a0*b1*b2*h3*h10-a0*a0*b1*b2*h4*h9-2*a0*a0*b1*b2*h5*h8-a0*a0*b1*c0*h4*h5-2*a0*a0*b1*c1*h3*h5-2*a0*a0*b1*c2*h2*h5-a0*a0*b1*c2*h3*h4-a0*a0*b2*b2*h1*h11-a0*a0*b2*b2*h2*h10-a0*a0*b2*b2*h4*h8-a0*a0*b2*b2*h5*h7-a0*a0*b2*c0*h3*h5-a0*a0*b2*c0*h4*h4-2*a0*a0*b2*c1*h2*h5-a0*a0*b2*c1*h3*h4-2*a0*a0*b2*c2*h1*h5-2*a0*a0*b2*c2*h2*h4-2*a0*a1*a1*b0*h9*h11+a0*a1*a1*b1*h8*h11+a0*a1*a1*b2*h7*h11+3*a0*a1*a1*b2*h8*h10-2*a0*a1*a1*c0*h3*h11-2*a0*a1*a1*c0*h5*h9+a0*a1*a1*c1*h2*h11+a0*a1*a1*c1*h5*h8+a0*a1*a1*c2*h1*h11+3*a0*a1*a1*c2*h2*h10+3*a0*a1*a1*c2*h4*h8+a0*a1*a1*c2*h5*h7-4*a0*a1*a2*b0*h8*h11-2*a0*a1*a2*b0*h9*h10+2*a0*a1*a2*b1*h7*h11-2*a0*a1*a2*b1*h8*h10+2*a0*a1*a2*b2*h6*h11+4*a0*a1*a2*b2*h7*h10-4*a0*a1*a2*c0*h2*h11-2*a0*a1*a2*c0*h3*h10-2*a0*a1*a2*c0*h4*h9-4*a0*a1*a2*c0*h5*h8+2*a0*a1*a2*c1*h1*h11-2*a0*a1*a2*c1*h2*h10-2*a0*a1*a2*c1*h4*h8+2*a0*a1*a2*c1*h5*h7+2*a0*a1*a2*c2*h0*h11+4*a0*a1*a2*c2*h1*h10+4*a0*a1*a2*c2*h4*h7+2*a0*a1*a2*c2*h5*h6+a0*a1*b0*b0*h4*h11+a0*a1*b0*b0*h5*h10-2*a0*a1*b0*b2*h3*h10-2*a0*a1*b0*b2*h4*h9+2*a0*a1*b0*c0*h4*h5-2*a0*a1*b0*c2*h3*h4-a0*a1*b1*b1*h2*h11-a0*a1*b1*b1*h5*h8-2*a0*a1*b1*b2*h1*h11-2*a0*a1*b1*b2*h2*h10-2*a0*a1*b1*b2*h4*h8-2*a0*a1*b1*b2*h5*h7-2*a0*a1*b1*c1*h2*h5-2*a0*a1*b1*c2*h1*h5-2*a0*a1*b1*c2*h2*h4-a0*a1*b2*b2*h0*h11-2*a0*a1*b2*b2*h1*h10-2*a0*a1*b2*b2*h4*h7-a0*a1*b2*b2*h5*h6-2*a0*a1*b2*c0*h3*h4-2*a0*a1*b2*c1*h1*h5-2*a0*a1*b2*c1*h2*h4-2*a0*a1*b2*c2*h0*h5-4*a0*a1*b2*c2*h1*h4-2*a0*a2*a2*b0*h7*h11-2*a0*a2*a2*b0*h8*h10+a0*a2*a2*b1*h6*h11-2*a0*a2*a2*b1*h7*h10+a0*a2*a2*b2*h6*h10-2*a0*a2*a2*c0*h1*h11-2*a0*a2*a2*c0*h2*h10-2*a0*a2*a2*c0*h4*h8-2*a0*a2*a2*c0*h5*h7+a0*a2*a2*c1*h0*h11-2*a0*a2*a2*c1*h1*h10-2*a0*a2*a2*c1*h4*h7+a0*a2*a2*c1*h5*h6+a0*a2*a2*c2*h0*h10+a0*a2*a2*c2*h4*h6+a0*a2*b0*b0*h3*h11+2*a0*a2*b0*b0*h4*h10+a0*a2*b0*b0*h5*h9+2*a0*a2*b0*b1*h3*h10+2*a0*a2*b0*b1*h4*h9+2*a0*a2*b0*c0*h3*h5+2*a0*a2*b0*c0*h4*h4+2*a0*a2*b0*c1*h3*h4-a0*a2*b1*b1*h1*h11+a0*a2*b1*b1*h2*h10+a0*a2*b1*b1*h4*h8-a0*a2*b1*b1*h5*h7-2*a0*a2*b1*b2*h0*h11-2*a0*a2*b1*b2*h5*h6+2*a0*a2*b1*c0*h3*h4-2*a0*a2*b1*c1*h1*h5+2*a0*a2*b1*c1*h2*h4-2*a0*a2*b1*c2*h0*h5-a0*a2*b2*b2*h0*h10-a0*a2*b2*b2*h4*h6-2*a0*a2*b2*c1*h0*h5-2*a0*a2*b2*c2*h0*h4+a0*b0*b0*b1*h4*h5+a0*b0*b0*b2*h3*h5+a0*b0*b0*b2*h4*h4+2*a0*b0*b1*b1*h3*h5+4*a0*b0*b1*b2*h2*h5+2*a0*b0*b1*b2*h3*h4+2*a0*b0*b2*b2*h1*h5+2*a0*b0*b2*b2*h2*h4+a0*b1*b1*b1*h2*h5+3*a0*b1*b1*b2*h1*h5+a0*b1*b1*b2*h2*h4+3*a0*b1*b2*b2*h0*h5+2*a0*b1*b2*b2*h1*h4+a0*b2*b2*b2*h0*h4-a1*a1*a1*b0*h8*h11+a1*a1*a1*b2*h7*h10-a1*a1*a1*c0*h2*h11-a1*a1*a1*c0*h5*h8+a1*a1*a1*c2*h1*h10+a1*a1*a1*c2*h4*h7-3*a1*a1*a2*b0*h7*h11-a1*a1*a2*b0*h8*h10-a1*a1*a2*b1*h7*h10+2*a1*a1*a2*b2*h6*h10-3*a1*a1*a2*c0*h1*h11-a1*a1*a2*c0*h2*h10-a1*a1*a2*c0*h4*h8-3*a1*a1*a2*c0*h5*h7-a1*a1*a2*c1*h1*h10-a1*a1*a2*c1*h4*h7+2*a1*a1*a2*c2*h0*h10+2*a1*a1*a2*c2*h4*h6+a1*a1*b0*b0*h3*h11+a1*a1*b0*b0*h5*h9+a1*a1*b0*b1*h2*h11+a1*a1*b0*b1*h5*h8+a1*a1*b0*b2*h1*h11-a1*a1*b0*b2*h2*h10-a1*a1*b0*b2*h4*h8+a1*a1*b0*b2*h5*h7+2*a1*a1*b0*c0*h3*h5+a1*a1*b0*c1*h2*h5+a1*a1*b0*c2*h1*h5-a1*a1*b0*c2*h2*h4-a1*a1*b1*b2*h1*h10-a1*a1*b1*b2*h4*h7+a1*a1*b1*c0*h2*h5-a1*a1*b1*c2*h1*h4-a1*a1*b2*b2*h0*h10-a1*a1*b2*b2*h4*h6+a1*a1*b2*c0*h1*h5-a1*a1*b2*c0*h2*h4-a1*a1*b2*c1*h1*h4-2*a1*a1*b2*c2*h0*h4-3*a1*a2*a2*b0*h6*h11-2*a1*a2*a2*b0*h7*h10-2*a1*a2*a2*b1*h6*h10-3*a1*a2*a2*c0*h0*h11-2*a1*a2*a2*c0*h1*h10-2*a1*a2*a2*c0*h4*h7-3*a1*a2*a2*c0*h5*h6-2*a1*a2*a2*c1*h0*h10-2*a1*a2*a2*c1*h4*h6+2*a1*a2*b0*b0*h2*h11+a1*a2*b0*b0*h3*h10+a1*a2*b0*b0*h4*h9+2*a1*a2*b0*b0*h5*h8+2*a1*a2*b0*b1*h1*h11+2*a1*a2*b0*b1*h2*h10+2*a1*a2*b0*b1*h4*h8+2*a1*a2*b0*b1*h5*h7+2*a1*a2*b0*b2*h0*h11+2*a1*a2*b0*b2*h5*h6+4*a1*a2*b0*c0*h2*h5+2*a1*a2*b0*c0*h3*h4+2*a1*a2*b0*c1*h1*h5+2*a1*a2*b0*c1*h2*h4+2*a1*a2*b0*c2*h0*h5+a1*a2*b1*b1*h1*h10+a1*a2*b1*b1*h4*h7+2*a1*a2*b1*c0*h1*h5+2*a1*a2*b1*c0*h2*h4+2*a1*a2*b1*c1*h1*h4+2*a1*a2*b2*c0*h0*h5-a1*b0*b0*b0*h4*h5-2*a1*b0*b0*b1*h3*h5-2*a1*b0*b0*b2*h2*h5+a1*b0*b0*b2*h3*h4-a1*b0*b1*b1*h2*h5-2*a1*b0*b1*b2*h1*h5+2*a1*b0*b1*b2*h2*h4-a1*b0*b2*b2*h0*h5+2*a1*b0*b2*b2*h1*h4+a1*b1*b1*b2*h1*h4+2*a1*b1*b2*b2*h0*h4-a2*a2*a2*b0*h6*h10-a2*a2*a2*c0*h0*h10-a2*a2*a2*c0*h4*h6+a2*a2*b0*b0*h1*h11+a2*a2*b0*b0*h2*h10+a2*a2*b0*b0*h4*h8+a2*a2*b0*b0*h5*h7+a2*a2*b0*b1*h0*h11+2*a2*a2*b0*b1*h1*h10+2*a2*a2*b0*b1*h4*h7+a2*a2*b0*b1*h5*h6+a2*a2*b0*b2*h0*h10+a2*a2*b0*b2*h4*h6+2*a2*a2*b0*c0*h1*h5+2*a2*a2*b0*c0*h2*h4+a2*a2*b0*c1*h0*h5+2*a2*a2*b0*c1*h1*h4+a2*a2*b0*c2*h0*h4+a2*a2*b1*b1*h0*h10+a2*a2*b1*b1*h4*h6+a2*a2*b1*c0*h0*h5+2*a2*a2*b1*c0*h1*h4+2*a2*a2*b1*c1*h0*h4+a2*a2*b2*c0*h0*h4-a2*b0*b0*b0*h3*h5-a2*b0*b0*b0*h4*h4-2*a2*b0*b0*b1*h2*h5-3*a2*b0*b0*b1*h3*h4-2*a2*b0*b0*b2*h1*h5-2*a2*b0*b0*b2*h2*h4-a2*b0*b1*b1*h1*h5-3*a2*b0*b1*b1*h2*h4-2*a2*b0*b1*b2*h0*h5-4*a2*b0*b1*b2*h1*h4-a2*b0*b2*b2*h0*h4-a2*b1*b1*b1*h1*h4-2*a2*b1*b1*b2*h0*h4,20*a0*a0*a0*a2+249/8*a0*a0*a1*a1-385/8*a0*a0*a1*b2-229/8*a0*a0*a2*b1-134*a0*a0*a2*c2+157/4*a0*a0*b2*b2-239/8*a0*a1*a1*b1-133*a0*a1*a1*c2-95/4*a0*a1*a2*b0-200*a0*a1*a2*c1+116*a0*a1*b1*b2+212*a0*a1*b2*c2-101/2*a0*a2*a2*c0+273/4*a0*a2*b0*b2+77/2*a0*a2*b1*b1+194*a0*a2*b1*c2+200*a0*a2*b2*c1+52*a0*a2*c2*c2-519/4*a0*b1*b2*b2-61*a0*b2*b2*c2-35/8*a1*a1*a1*b0-33*a1*a1*a1*c1-99/2*a1*a1*a2*c0+265/8*a1*a1*b0*b2+75/4*a1*a1*b1*b1+96*a1*a1*b1*c2+99*a1*a1*b2*c1+26*a1*a1*c2*c2+109/4*a1*a2*b0*b1+118*a1*a2*b0*c2+180*a1*a2*b1*c1+85*a1*a2*b2*c0+116*a1*a2*c1*c2-311/4*a1*b0*b2*b2-423/4*a1*b1*b1*b2-128*a1*b1*b2*c2-67*a1*b2*b2*c1+18*a1*b2*c2*c2-41/8*a2*a2*b0*b0+53*a2*a2*b0*c1+67/2*a2*a2*b1*c0+28*a2*a2*c0*c2+32*a2*a2*c1*c1-227/2*a2*b0*b1*b2-89*a2*b0*b2*c2-113/4*a2*b1*b1*b1-67*a2*b1*b1*c2-140*a2*b1*b2*c1+18*a2*b1*c2*c2-37*a2*b2*b2*c0+36*a2*b2*c1*c2+107/2*b0*b2*b2*b2+114*b1*b1*b2*b2-27*b1*b2*b2*c2-9*b2*b2*b2*c1+3/4*a0*a0*a0*a2*h9-a0*a0*a0*b1*h11+3/8*a0*a0*a0*b2*h3-a0*a0*a0*b2*h10-a0*a0*a0*c1*h5-a0*a0*a0*c2*h4-2*a0*a0*a0*c2*h11+9/4*a0*a0*a1*a2*h8+a0*a0*a1*b0*h11+9/8*a0*a0*a1*b2*h2+a0*a0*a1*c0*h5-4*a0*a0*a1*c1*h11-6*a0*a0*a1*c2*h10-3/4*a0*a0*a2*b0*h3+a0*a0*a2*b0*h10-3/4*a0*a0*a2*b1*h2+21/8*a0*a0*a2*b2*h1+a0*a0*a2*c0*h4+2*a0*a0*a2*c0*h11+2*a0*a0*a2*c1*h10+a0*a0*b0*b1*h5+a0*a0*b0*b2*h4+2*a0*a0*b0*b2*h11+2*a0*a0*b0*c2*h5+2*a0*a0*b1*b1*h11+2*a0*a0*b1*b2*h10+4*a0*a0*b1*c1*h5+2*a0*a0*b1*c2*h4+2*a0*a0*b2*c0*h5+2*a0*a0*b2*c1*h4+9/4*a0*a1*a1*b2*h1+4*a0*a1*a1*c0*h11-3/2*a0*a1*a2*b0*h2+3/4*a0*a1*a2*b1*h1+21/4*a0*a1*a2*b2*h0+33/2*a0*a1*a2*b2*h7+4*a0*a1*a2*c0*h10+18*a0*a1*a2*c2*h1-a0*a1*b0*b0*h5+4*a0*a1*b0*b2*h10+4*a0*a1*b0*c2*h4-9*a0*a1*b2*b2*h1+4*a0*a1*b2*c0*h4-21/8*a0*a2*a2*b0*h1-21/8*a0*a2*a2*b1*h0+33/4*a0*a2*a2*b1*h7+35/4*a0*a2*a2*b2*h6+9*a0*a2*a2*c1*h1+19/2*a0*a2*a2*c2*h0+6*a0*a2*a2*c2*h7-a0*a2*b0*b0*h4-2*a0*a2*b0*b0*h11-4*a0*a2*b0*b1*h10-4*a0*a2*b0*c0*h5-4*a0*a2*b0*c1*h4-18*a0*a2*b1*b2*h1-4*a0*a2*b1*c0*h4-19/2*a0*a2*b2*b2*h0-6*a0*a2*b2*b2*h7-15*a0*a2*b2*c2*h1-2*a0*b0*b0*b2*h5-4*a0*b0*b1*b1*h5-4*a0*b0*b1*b2*h4+15/2*a0*b2*b2*b2*h1-3/2*a1*a1*a1*a2*h6+3/2*a1*a1*a1*b2*h0-3*a1*a1*a2*b0*h1-3/4*a1*a1*a2*b1*h0+33/2*a1*a1*a2*b2*h6+18*a1*a1*a2*c2*h0-2*a1*a1*b0*b0*h11-4*a1*a1*b0*c0*h5-9*a1*a1*b2*b2*h0-21/8*a1*a2*a2*b0*h0-45/2*a1*a2*a2*b0*h7-57/4*a1*a2*a2*b1*h6-45/2*a1*a2*a2*c0*h1-27/2*a1*a2*a2*c1*h0+6*a1*a2*a2*c2*h6-2*a1*a2*b0*b0*h10+33/2*a1*a2*b0*b2*h1-4*a1*a2*b0*c0*h4-3/2*a1*a2*b1*b2*h0-6*a1*a2*b2*b2*h6-15*a1*a2*b2*c2*h0+4*a1*b0*b0*b1*h5-2*a1*b0*b0*b2*h4+15/2*a1*b2*b2*b2*h0-8*a2*a2*a2*b0*h6-8*a2*a2*a2*c0*h0-3*a2*a2*a2*c0*h7-3*a2*a2*a2*c1*h6+33/4*a2*a2*b0*b1*h1+35/4*a2*a2*b0*b2*h0+9/2*a2*a2*b0*b2*h7+6*a2*a2*b0*c2*h1+33/4*a2*a2*b1*b1*h0+9/2*a2*a2*b1*b2*h6+6*a2*a2*b1*c2*h0+9/2*a2*a2*b2*c0*h1+9/2*a2*a2*b2*c1*h0+2*a2*b0*b0*b0*h5+6*a2*b0*b0*b1*h4-6*a2*b0*b2*b2*h1-6*a2*b1*b2*b2*h0+a0*a0*a0*b1*h9*h11+a0*a0*a0*b2*h8*h11+a0*a0*a0*b2*h9*h10+a0*a0*a0*c1*h3*h11+a0*a0*a0*c1*h5*h9+a0*a0*a0*c2*h2*h11+a0*a0*a0*c2*h3*h10+a0*a0*a0*c2*h4*h9+a0*a0*a0*c2*h5*h8-a0*a0*a1*b0*h9*h11+2*a0*a0*a1*b1*h8*h11+2*a0*a0*a1*b2*h7*h11+3*a0*a0*a1*b2*h8*h10-a0*a0*a1*c0*h3*h11-a0*a0*a1*c0*h5*h9+2*a0*a0*a1*c1*h2*h11+2*a0*a0*a1*c1*h5*h8+2*a0*a0*a1*c2*h1*h11+3*a0*a0*a1*c2*h2*h10+3*a0*a0*a1*c2*h4*h8+2*a0*a0*a1*c2*h5*h7-a0*a0*a2*b0*h8*h11-a0*a0*a2*b0*h9*h10+2*a0*a0*a2*b1*h7*h11-a0*a0*a2*b1*h8*h10+2*a0*a0*a2*b2*h6*h11+2*a0*a0*a2*b2*h7*h10-a0*a0*a2*c0*h2*h11-a0*a0*a2*c0*h3*h10-a0*a0*a2*c0*h4*h9-a0*a0*a2*c0*h5*h8+2*a0*a0*a2*c1*h1*h11-a0*a0*a2*c1*h2*h10-a0*a0*a2*c1*h4*h8+2*a0*a0*a2*c1*h5*h7+2*a0*a0*a2*c2*h0*h11+2*a0*a0*a2*c2*h1*h10+2*a0*a0*a2*c2*h4*h7+2*a0*a0*a2*c2*h5*h6-a0*a0*b0*b1*h3*h11-a0*a0*b0*b1*h5*h9-a0*a0*b0*b2*h2*h11-a0*a0*b0*b2*h3*h10-a0*a0*b0*b2*h4*h9-a0*a0*b0*b2*h5*h8-a0*a0*b0*c1*h3*h5-a0*a0*b0*c2*h2*h5-a0*a0*b0*c2*h3*h4-a0*a0*b1*b1*h2*h11-a0*a0*b1*b1*h5*h8-2*a0*a0*b1*b2*h1*h11-a0*a0*b1*b2*h2*h10-a0*a0*b1*b2*h4*h8-2*a0*a0*b1*b2*h5*h7-a0*a0*b1*c0*h3*h5-2*a0*a0*b1*c1*h2*h5-2*a0*a0*b1*c2*h1*h5-a0*a0*b1*c2*h2*h4-a0*a0*b2*b2*h0*h11-a0*a0*b2*b2*h1*h10-a0*a0*b2*b2*h4*h7-a0*a0*b2*b2*h5*h6-a0*a0*b2*c0*h2*h5-a0*a0*b2*c0*h3*h4-2*a0*a0*b2*c1*h1*h5-a0*a0*b2*c1*h2*h4-2*a0*a0*b2*c2*h0*h5-2*a0*a0*b2*c2*h1*h4-2*a0*a1*a1*b0*h8*h11+a0*a1*a1*b1*h7*h11+a0*a1*a1*b2*h6*h11+3*a0*a1*a1*b2*h7*h10-2*a0*a1*a1*c0*h2*h11-2*a0*a1*a1*c0*h5*h8+a0*a1*a1*c1*h1*h11+a0*a1*a1*c1*h5*h7+a0*a1*a1*c2*h0*h11+3*a0*a1*a1*c2*h1*h10+3*a0*a1*a1*c2*h4*h7+a0*a1*a1*c2*h5*h6-4*a0*a1*a2*b0*h7*h11-2*a0*a1*a2*b0*h8*h10+2*a0*a1*a2*b1*h6*h11-2*a0*a1*a2*b1*h7*h10+4*a0*a1*a2*b2*h6*h10-4*a0*a1*a2*c0*h1*h11-2*a0*a1*a2*c0*h2*h10-2*a0*a1*a2*c0*h4*h8-4*a0*a1*a2*c0*h5*h7+2*a0*a1*a2*c1*h0*h11-2*a0*a1*a2*c1*h1*h10-2*a0*a1*a2*c1*h4*h7+2*a0*a1*a2*c1*h5*h6+4*a0*a1*a2*c2*h0*h10+4*a0*a1*a2*c2*h4*h6+a0*a1*b0*b0*h3*h11+a0*a1*b0*b0*h5*h9-2*a0*a1*b0*b2*h2*h10-2*a0*a1*b0*b2*h4*h8+2*a0*a1*b0*c0*h3*h5-2*a0*a1*b0*c2*h2*h4-a0*a1*b1*b1*h1*h11-a0*a1*b1*b1*h5*h7-2*a0*a1*b1*b2*h0*h11-2*a0*a1*b1*b2*h1*h10-2*a0*a1*b1*b2*h4*h7-2*a0*a1*b1*b2*h5*h6-2*a0*a1*b1*c1*h1*h5-2*a0*a1*b1*c2*h0*h5-2*a0*a1*b1*c2*h1*h4-2*a0*a1*b2*b2*h0*h10-2*a0*a1*b2*b2*h4*h6-2*a0*a1*b2*c0*h2*h4-2*a0*a1*b2*c1*h0*h5-2*a0*a1*b2*c1*h1*h4-4*a0*a1*b2*c2*h0*h4-2*a0*a2*a2*b0*h6*h11-2*a0*a2*a2*b0*h7*h10-2*a0*a2*a2*b1*h6*h10-2*a0*a2*a2*c0*h0*h11-2*a0*a2*a2*c0*h1*h10-2*a0*a2*a2*c0*h4*h7-2*a0*a2*a2*c0*h5*h6-2*a0*a2*a2*c1*h0*h10-2*a0*a2*a2*c1*h4*h6+a0*a2*b0*b0*h2*h11+a0*a2*b0*b0*h3*h10+a0*a2*b0*b0*h4*h9+a0*a2*b0*b0*h5*h8+2*a0*a2*b0*b1*h2*h10+2*a0*a2*b0*b1*h4*h8+2*a0*a2*b0*c0*h2*h5+2*a0*a2*b0*c0*h3*h4+2*a0*a2*b0*c1*h2*h4-a0*a2*b1*b1*h0*h11+a0*a2*b1*b1*h1*h10+a0*a2*b1*b1*h4*h7-a0*a2*b1*b1*h5*h6+2*a0*a2*b1*c0*h2*h4-2*a0*a2*b1*c1*h0*h5+2*a0*a2*b1*c1*h1*h4+a0*b0*b0*b1*h3*h5+a0*b0*b0*b2*h2*h5+a0*b0*b0*b2*h3*h4+2*a0*b0*b1*b1*h2*h5+4*a0*b0*b1*b2*h1*h5+2*a0*b0*b1*b2*h2*h4+2*a0*b0*b2*b2*h0*h5+2*a0*b0*b2*b2*h1*h4+a0*b1*b1*b1*h1*h5+3*a0*b1*b1*b2*h0*h5+a0*b1*b1*b2*h1*h4+2*a0*b1*b2*b2*h0*h4-a1*a1*a1*b0*h7*h11+a1*a1*a1*b2*h6*h10-a1*a1*a1*c0*h1*h11-a1*a1*a1*c0*h5*h7+a1*a1*a1*c2*h0*h10+a1*a1*a1*c2*h4*h6-3*a1*a1*a2*b0*h6*h11-a1*a1*a2*b0*h7*h10-a1*a1*a2*b1*h6*h10-3*a1*a1*a2*c0*h0*h11-a1*a1*a2*c0*h1*h10-a1*a1*a2*c0*h4*h7-3*a1*a1*a2*c0*h5*h6-a1*a1*a2*c1*h0*h10-a1*a1*a2*c1*h4*h6+a1*a1*b0*b0*h2*h11+a1*a1*b0*b0*h5*h8+a1*a1*b0*b1*h1*h11+a1*a1*b0*b1*h5*h7+a1*a1*b0*b2*h0*h11-a1*a1*b0*b2*h1*h10-a1*a1*b0*b2*h4*h7+a1*a1*b0*b2*h5*h6+2*a1*a1*b0*c0*h2*h5+a1*a1*b0*c1*h1*h5+a1*a1*b0*c2*h0*h5-a1*a1*b0*c2*h1*h4-a1*a1*b1*b2*h0*h10-a1*a1*b1*b2*h4*h6+a1*a1*b1*c0*h1*h5-a1*a1*b1*c2*h0*h4+a1*a1*b2*c0*h0*h5-a1*a1*b2*c0*h1*h4-a1*a1*b2*c1*h0*h4-2*a1*a2*a2*b0*h6*h10-2*a1*a2*a2*c0*h0*h10-2*a1*a2*a2*c0*h4*h6+2*a1*a2*b0*b0*h1*h11+a1*a2*b0*b0*h2*h10+a1*a2*b0*b0*h4*h8+2*a1*a2*b0*b0*h5*h7+2*a1*a2*b0*b1*h0*h11+2*a1*a2*b0*b1*h1*h10+2*a1*a2*b0*b1*h4*h7+2*a1*a2*b0*b1*h5*h6+4*a1*a2*b0*c0*h1*h5+2*a1*a2*b0*c0*h2*h4+2*a1*a2*b0*c1*h0*h5+2*a1*a2*b0*c1*h1*h4+a1*a2*b1*b1*h0*h10+a1*a2*b1*b1*h4*h6+2*a1*a2*b1*c0*h0*h5+2*a1*a2*b1*c0*h1*h4+2*a1*a2*b1*c1*h0*h4-a1*b0*b0*b0*h3*h5-2*a1*b0*b0*b1*h2*h5-2*a1*b0*b0*b2*h1*h5+a1*b0*b0*b2*h2*h4-a1*b0*b1*b1*h1*h5-2*a1*b0*b1*b2*h0*h5+2*a1*b0*b1*b2*h1*h4+2*a1*b0*b2*b2*h0*h4+a1*b1*b1*b2*h0*h4+a2*a2*b0*b0*h0*h11+a2*a2*b0*b0*h1*h10+a2*a2*b0*b0*h4*h7+a2*a2*b0*b0*h5*h6+2*a2*a2*b0*b1*h0*h10+2*a2*a2*b0*b1*h4*h6+2*a2*a2*b0*c0*h0*h5+2*a2*a2*b0*c0*h1*h4+2*a2*a2*b0*c1*h0*h4+2*a2*a2*b1*c0*h0*h4-a2*b0*b0*b0*h2*h5-a2*b0*b0*b0*h3*h4-2*a2*b0*b0*b1*h1*h5-3*a2*b0*b0*b1*h2*h4-2*a2*b0*b0*b2*h0*h5-2*a2*b0*b0*b2*h1*h4-a2*b0*b1*b1*h0*h5-3*a2*b0*b1*b1*h1*h4-4*a2*b0*b1*b2*h0*h4-a2*b1*b1*b1*h0*h4,169/8*a0*a0*a0*a1-141/8*a0*a0*a0*b2-277/8*a0*a0*a1*b1-289/2*a0*a0*a1*c2-133/8*a0*a0*a2*b0-223/2*a0*a0*a2*c1+139/2*a0*a0*b1*b2+113*a0*a0*b2*c2-143/8*a0*a1*a1*b0-221/2*a0*a1*a1*c1-122*a0*a1*a2*c0+357/4*a0*a1*b0*b2+49*a0*a1*b1*b1+206*a0*a1*b1*c2+212*a0*a1*b2*c1+52*a0*a1*c2*c2+201/4*a0*a2*b0*b1+132*a0*a2*b0*c2+194*a0*a2*b1*c1+99*a0*a2*b2*c0+116*a0*a2*c1*c2-395/4*a0*b0*b2*b2-507/4*a0*b1*b1*b2-128*a0*b1*b2*c2-67*a0*b2*b2*c1+18*a0*b2*c2*c2-20*a1*a1*a1*c0+193/8*a1*a1*b0*b1+65*a1*a1*b0*c2+96*a1*a1*b1*c1+97/2*a1*a1*b2*c0+58*a1*a1*c1*c2+1/4*a1*a2*b0*b0+118*a1*a2*b0*c1+79*a1*a2*b1*c0+56*a1*a2*c0*c2+64*a1*a2*c1*c1-299/2*a1*b0*b1*b2-89*a1*b0*b2*c2-137/4*a1*b1*b1*b1-67*a1*b1*b1*c2-140*a1*b1*b2*c1+18*a1*b1*c2*c2-37*a1*b2*b2*c0+36*a1*b2*c1*c2+5/2*a2*a2*b0*c0+34*a2*a2*c0*c1-103/4*a2*b0*b0*b2-215/4*a2*b0*b1*b1-95*a2*b0*b1*c2-101*a2*b0*b2*c1+18*a2*b0*c2*c2-73*a2*b1*b1*c1-80*a2*b1*b2*c0+36*a2*b1*c1*c2+18*a2*b2*c1*c1+339/2*b0*b1*b2*b2-27*b0*b2*b2*c2+79*b1*b1*b1*b2-27*b1*b1*b2*c2-27*b1*b2*b2*c1+9*b2*b2*b2*c0+3/4*a0*a0*a0*a2*h8+3/8*a0*a0*a0*b2*h2-2*a0*a0*a0*c1*h11-2*a0*a0*a0*c2*h10-9/4*a0*a0*a1*a2*h7+27/8*a0*a0*a1*b2*h1+2*a0*a0*a1*c0*h11-3/4*a0*a0*a2*b0*h2+3/2*a0*a0*a2*b1*h1+21/8*a0*a0*a2*b2*h0+33/2*a0*a0*a2*b2*h7+2*a0*a0*a2*c0*h10+18*a0*a0*a2*c2*h1+2*a0*a0*b0*b1*h11+2*a0*a0*b0*b2*h10+2*a0*a0*b0*c1*h5+2*a0*a0*b0*c2*h4+2*a0*a0*b1*c0*h5-9*a0*a0*b2*b2*h1+2*a0*a0*b2*c0*h4-3/4*a0*a1*a1*a1*h7-9/2*a0*a1*a1*a2*h6+9/8*a0*a1*a1*b1*h1+9/2*a0*a1*a1*b2*h0+33/4*a0*a1*a1*b2*h7+9*a0*a1*a1*c2*h1-15/4*a0*a1*a2*b0*h1-3/2*a0*a1*a2*b1*h0+33/2*a0*a1*a2*b1*h7+34*a0*a1*a2*b2*h6+18*a0*a1*a2*c1*h1+37*a0*a1*a2*c2*h0+12*a0*a1*a2*c2*h7-2*a0*a1*b0*b0*h11-4*a0*a1*b0*c0*h5-18*a0*a1*b1*b2*h1-37/2*a0*a1*b2*b2*h0-6*a0*a1*b2*b2*h7-15*a0*a1*b2*c2*h1-21/8*a0*a2*a2*b0*h0-57/4*a0*a2*a2*b0*h7-55/4*a0*a2*a2*b1*h6-27/2*a0*a2*a2*c0*h1-13*a0*a2*a2*c1*h0+6*a0*a2*a2*c1*h7+7*a0*a2*a2*c2*h6-2*a0*a2*b0*b0*h10-3/2*a0*a2*b0*b2*h1-4*a0*a2*b0*c0*h4-9*a0*a2*b1*b1*h1-5/2*a0*a2*b1*b2*h0-12*a0*a2*b1*b2*h7-15*a0*a2*b1*c2*h1-7*a0*a2*b2*b2*h6-15*a0*a2*b2*c1*h1-17*a0*a2*b2*c2*h0+6*a0*a2*b2*c2*h7-2*a0*b0*b0*b1*h5-2*a0*b0*b0*b2*h4+45/2*a0*b1*b2*b2*h1+17/2*a0*b2*b2*b2*h0-3*a0*b2*b2*b2*h7-3/4*a1*a1*a1*a1*h6-3/4*a1*a1*a1*b0*h1+3/8*a1*a1*a1*b1*h0+33/4*a1*a1*a1*b2*h6+9*a1*a1*a1*c2*h0-3/4*a1*a1*a2*b0*h0-45/2*a1*a1*a2*b0*h7-6*a1*a1*a2*b1*h6-45/2*a1*a1*a2*c0*h1-9/2*a1*a1*a2*c1*h0+12*a1*a1*a2*c2*h6+33/4*a1*a1*b0*b2*h1-39/4*a1*a1*b1*b2*h0-6*a1*a1*b2*b2*h6-15*a1*a1*b2*c2*h0-63/4*a1*a2*a2*b0*h6-15*a1*a2*a2*c0*h0-9*a1*a2*a2*c0*h7-3*a1*a2*a2*c1*h6+33/2*a1*a2*b0*b1*h1-1/2*a1*a2*b0*b2*h0+9*a1*a2*b0*b2*h7+12*a1*a2*b0*c2*h1+15/2*a1*a2*b1*b1*h0-3*a1*a2*b1*b2*h6-3*a1*a2*b1*c2*h0+9*a1*a2*b2*c0*h1-6*a1*a2*b2*c1*h0+6*a1*a2*b2*c2*h6+2*a1*b0*b0*b0*h5-6*a1*b0*b2*b2*h1+33/2*a1*b1*b2*b2*h0-3*a1*b2*b2*b2*h6-4*a2*a2*a2*c0*h6+33/4*a2*a2*b0*b0*h1+17*a2*a2*b0*b1*h0+9/2*a2*a2*b0*b1*h7+11/2*a2*a2*b0*b2*h6+6*a2*a2*b0*c1*h1+7*a2*a2*b0*c2*h0-6*a2*a2*b0*c2*h7+9/2*a2*a2*b1*b1*h6+9/2*a2*a2*b1*c0*h1+21/2*a2*a2*b1*c1*h0-6*a2*a2*b1*c2*h6+11/2*a2*a2*b2*c0*h0-9*a2*a2*b2*c0*h7-9*a2*a2*b2*c1*h6-6*a2*a2*c0*c2*h1-6*a2*a2*c1*c2*h0+2*a2*b0*b0*b0*h4-12*a2*b0*b1*b2*h1-7*a2*b0*b2*b2*h0+6*a2*b0*b2*b2*h7+6*a2*b0*b2*c2*h1-12*a2*b1*b1*b2*h0+6*a2*b1*b2*b2*h6+6*a2*b1*b2*c2*h0+6*a2*b2*b2*c0*h1+6*a2*b2*b2*c1*h0-3*b0*b2*b2*b2*h1-3*b1*b2*b2*b2*h0+a0*a0*a0*b1*h8*h11+a0*a0*a0*b2*h7*h11+a0*a0*a0*b2*h8*h10+a0*a0*a0*c1*h2*h11+a0*a0*a0*c1*h5*h8+a0*a0*a0*c2*h1*h11+a0*a0*a0*c2*h2*h10+a0*a0*a0*c2*h4*h8+a0*a0*a0*c2*h5*h7-a0*a0*a1*b0*h8*h11+2*a0*a0*a1*b1*h7*h11+2*a0*a0*a1*b2*h6*h11+3*a0*a0*a1*b2*h7*h10-a0*a0*a1*c0*h2*h11-a0*a0*a1*c0*h5*h8+2*a0*a0*a1*c1*h1*h11+2*a0*a0*a1*c1*h5*h7+2*a0*a0*a1*c2*h0*h11+3*a0*a0*a1*c2*h1*h10+3*a0*a0*a1*c2*h4*h7+2*a0*a0*a1*c2*h5*h6-a0*a0*a2*b0*h7*h11-a0*a0*a2*b0*h8*h10+2*a0*a0*a2*b1*h6*h11-a0*a0*a2*b1*h7*h10+2*a0*a0*a2*b2*h6*h10-a0*a0*a2*c0*h1*h11-a0*a0*a2*c0*h2*h10-a0*a0*a2*c0*h4*h8-a0*a0*a2*c0*h5*h7+2*a0*a0*a2*c1*h0*h11-a0*a0*a2*c1*h1*h10-a0*a0*a2*c1*h4*h7+2*a0*a0*a2*c1*h5*h6+2*a0*a0*a2*c2*h0*h10+2*a0*a0*a2*c2*h4*h6-a0*a0*b0*b1*h2*h11-a0*a0*b0*b1*h5*h8-a0*a0*b0*b2*h1*h11-a0*a0*b0*b2*h2*h10-a0*a0*b0*b2*h4*h8-a0*a0*b0*b2*h5*h7-a0*a0*b0*c1*h2*h5-a0*a0*b0*c2*h1*h5-a0*a0*b0*c2*h2*h4-a0*a0*b1*b1*h1*h11-a0*a0*b1*b1*h5*h7-2*a0*a0*b1*b2*h0*h11-a0*a0*b1*b2*h1*h10-a0*a0*b1*b2*h4*h7-2*a0*a0*b1*b2*h5*h6-a0*a0*b1*c0*h2*h5-2*a0*a0*b1*c1*h1*h5-2*a0*a0*b1*c2*h0*h5-a0*a0*b1*c2*h1*h4-a0*a0*b2*b2*h0*h10-a0*a0*b2*b2*h4*h6-a0*a0*b2*c0*h1*h5-a0*a0*b2*c0*h2*h4-2*a0*a0*b2*c1*h0*h5-a0*a0*b2*c1*h1*h4-2*a0*a0*b2*c2*h0*h4-2*a0*a1*a1*b0*h7*h11+a0*a1*a1*b1*h6*h11+3*a0*a1*a1*b2*h6*h10-2*a0*a1*a1*c0*h1*h11-2*a0*a1*a1*c0*h5*h7+a0*a1*a1*c1*h0*h11+a0*a1*a1*c1*h5*h6+3*a0*a1*a1*c2*h0*h10+3*a0*a1*a1*c2*h4*h6-4*a0*a1*a2*b0*h6*h11-2*a0*a1*a2*b0*h7*h10-2*a0*a1*a2*b1*h6*h10-4*a0*a1*a2*c0*h0*h11-2*a0*a1*a2*c0*h1*h10-2*a0*a1*a2*c0*h4*h7-4*a0*a1*a2*c0*h5*h6-2*a0*a1*a2*c1*h0*h10-2*a0*a1*a2*c1*h4*h6+a0*a1*b0*b0*h2*h11+a0*a1*b0*b0*h5*h8-2*a0*a1*b0*b2*h1*h10-2*a0*a1*b0*b2*h4*h7+2*a0*a1*b0*c0*h2*h5-2*a0*a1*b0*c2*h1*h4-a0*a1*b1*b1*h0*h11-a0*a1*b1*b1*h5*h6-2*a0*a1*b1*b2*h0*h10-2*a0*a1*b1*b2*h4*h6-2*a0*a1*b1*c1*h0*h5-2*a0*a1*b1*c2*h0*h4-2*a0*a1*b2*c0*h1*h4-2*a0*a1*b2*c1*h0*h4-2*a0*a2*a2*b0*h6*h10-2*a0*a2*a2*c0*h0*h10-2*a0*a2*a2*c0*h4*h6+a0*a2*b0*b0*h1*h11+a0*a2*b0*b0*h2*h10+a0*a2*b0*b0*h4*h8+a0*a2*b0*b0*h5*h7+2*a0*a2*b0*b1*h1*h10+2*a0*a2*b0*b1*h4*h7+2*a0*a2*b0*c0*h1*h5+2*a0*a2*b0*c0*h2*h4+2*a0*a2*b0*c1*h1*h4+a0*a2*b1*b1*h0*h10+a0*a2*b1*b1*h4*h6+2*a0*a2*b1*c0*h1*h4+2*a0*a2*b1*c1*h0*h4+a0*b0*b0*b1*h2*h5+a0*b0*b0*b2*h1*h5+a0*b0*b0*b2*h2*h4+2*a0*b0*b1*b1*h1*h5+4*a0*b0*b1*b2*h0*h5+2*a0*b0*b1*b2*h1*h4+2*a0*b0*b2*b2*h0*h4+a0*b1*b1*b1*h0*h5+a0*b1*b1*b2*h0*h4-a1*a1*a1*b0*h6*h11-a1*a1*a1*c0*h0*h11-a1*a1*a1*c0*h5*h6-a1*a1*a2*b0*h6*h10-a1*a1*a2*c0*h0*h10-a1*a1*a2*c0*h4*h6+a1*a1*b0*b0*h1*h11+a1*a1*b0*b0*h5*h7+a1*a1*b0*b1*h0*h11+a1*a1*b0*b1*h5*h6-a1*a1*b0*b2*h0*h10-a1*a1*b0*b2*h4*h6+2*a1*a1*b0*c0*h1*h5+a1*a1*b0*c1*h0*h5-a1*a1*b0*c2*h0*h4+a1*a1*b1*c0*h0*h5-a1*a1*b2*c0*h0*h4+2*a1*a2*b0*b0*h0*h11+a1*a2*b0*b0*h1*h10+a1*a2*b0*b0*h4*h7+2*a1*a2*b0*b0*h5*h6+2*a1*a2*b0*b1*h0*h10+2*a1*a2*b0*b1*h4*h6+4*a1*a2*b0*c0*h0*h5+2*a1*a2*b0*c0*h1*h4+2*a1*a2*b0*c1*h0*h4+2*a1*a2*b1*c0*h0*h4-a1*b0*b0*b0*h2*h5-2*a1*b0*b0*b1*h1*h5-2*a1*b0*b0*b2*h0*h5+a1*b0*b0*b2*h1*h4-a1*b0*b1*b1*h0*h5+2*a1*b0*b1*b2*h0*h4+a2*a2*b0*b0*h0*h10+a2*a2*b0*b0*h4*h6+2*a2*a2*b0*c0*h0*h4-a2*b0*b0*b0*h1*h5-a2*b0*b0*b0*h2*h4-2*a2*b0*b0*b1*h0*h5-3*a2*b0*b0*b1*h1*h4-2*a2*b0*b0*b2*h0*h4-3*a2*b0*b1*b1*h0*h4,43/8*a0*a0*a0*a0-105/8*a0*a0*a0*b1-52*a0*a0*a0*c2-181/8*a0*a0*a1*b0-122*a0*a0*a1*c1-145/2*a0*a0*a2*c0+449/8*a0*a0*b0*b2+121/4*a0*a0*b1*b1+110*a0*a0*b1*c2+113*a0*a0*b2*c1+26*a0*a0*c2*c2-143/2*a0*a1*a1*c0+285/4*a0*a1*b0*b1+144*a0*a1*b0*c2+206*a0*a1*b1*c1+111*a0*a1*b2*c0+116*a0*a1*c1*c2+47/4*a0*a2*b0*b0+132*a0*a2*b0*c1+93*a0*a2*b1*c0+56*a0*a2*c0*c2+64*a0*a2*c1*c1-383/2*a0*b0*b1*b2-89*a0*b0*b2*c2-165/4*a0*b1*b1*b1-67*a0*b1*b1*c2-140*a0*b1*b2*c1+18*a0*b1*c2*c2-37*a0*b2*b2*c0+36*a0*b2*c1*c2+43/8*a1*a1*b0*b0+65*a1*a1*b0*c1+91/2*a1*a1*b1*c0+28*a1*a1*c0*c2+32*a1*a1*c1*c1+17*a1*a2*b0*c0+68*a1*a2*c0*c1-175/4*a1*b0*b0*b2-287/4*a1*b0*b1*b1-95*a1*b0*b1*c2-101*a1*b0*b2*c1+18*a1*b0*c2*c2-73*a1*b1*b1*c1-80*a1*b1*b2*c0+36*a1*b1*c1*c2+18*a1*b2*c1*c1+2*a2*a2*c0*c0-91/4*a2*b0*b0*b1-28*a2*b0*b0*c2-107*a2*b0*b1*c1-41*a2*b0*b2*c0+36*a2*b0*c1*c2-43*a2*b1*b1*c0+18*a2*b1*c1*c1+111/2*b0*b0*b2*b2+357/2*b0*b1*b1*b2-54*b0*b1*b2*c2-27*b0*b2*b2*c1+41/2*b1*b1*b1*b1-9*b1*b1*b1*c2-27*b1*b1*b2*c1+27*b1*b2*b2*c0-3/2*a0*a0*a0*a2*h7+3/2*a0*a0*a0*b2*h1-9/4*a0*a0*a1*a1*h7-9/2*a0*a0*a1*a2*h6+9/4*a0*a0*a1*b1*h1+9/2*a0*a0*a1*b2*h0+33/2*a0*a0*a1*b2*h7+18*a0*a0*a1*c2*h1-3/4*a0*a0*a2*b0*h1-3/4*a0*a0*a2*b1*h0+33/2*a0*a0*a2*b1*h7+35/2*a0*a0*a2*b2*h6+18*a0*a0*a2*c1*h1+19*a0*a0*a2*c2*h0+12*a0*a0*a2*c2*h7-18*a0*a0*b1*b2*h1-19/2*a0*a0*b2*b2*h0-6*a0*a0*b2*b2*h7-15*a0*a0*b2*c2*h1-3*a0*a1*a1*a1*h6-9/8*a0*a1*a1*b0*h1+9/8*a0*a1*a1*b1*h0+33/4*a0*a1*a1*b1*h7+101/4*a0*a1*a1*b2*h6+9*a0*a1*a1*c1*h1+55/2*a0*a1*a1*c2*h0+6*a0*a1*a1*c2*h7-3/2*a0*a1*a2*b0*h0-57/2*a0*a1*a2*b0*h7-11*a0*a1*a2*b1*h6-27*a0*a1*a2*c0*h1-8*a0*a1*a2*c1*h0+12*a0*a1*a2*c1*h7+26*a0*a1*a2*c2*h6-3/2*a0*a1*b0*b2*h1-9*a0*a1*b1*b1*h1-41/2*a0*a1*b1*b2*h0-12*a0*a1*b1*b2*h7-15*a0*a1*b1*c2*h1-13*a0*a1*b2*b2*h6-15*a0*a1*b2*c1*h1-32*a0*a1*b2*c2*h0+6*a0*a1*b2*c2*h7-61/4*a0*a2*a2*b0*h6-29/2*a0*a2*a2*c0*h0-3*a0*a2*a2*c0*h7-2*a0*a2*a2*c1*h6-3/2*a0*a2*b0*b1*h1-3/2*a0*a2*b0*b2*h0-3*a0*a2*b0*b2*h7-3*a0*a2*b0*c2*h1+7*a0*a2*b1*b1*h0-6*a0*a2*b1*b1*h7-5*a0*a2*b1*b2*h6-15*a0*a2*b1*c1*h1-5*a0*a2*b1*c2*h0+6*a0*a2*b1*c2*h7-6*a0*a2*b2*c0*h1-8*a0*a2*b2*c1*h0+6*a0*a2*b2*c1*h7+6*a0*a2*b2*c2*h6+33/2*a0*b0*b2*b2*h1+45/2*a0*b1*b1*b2*h1+39/2*a0*b1*b2*b2*h0-9*a0*b1*b2*b2*h7-3*a0*b2*b2*b2*h6+3/8*a1*a1*a1*b0*h0-15/2*a1*a1*a1*b0*h7+3/4*a1*a1*a1*b1*h6-15/2*a1*a1*a1*c0*h1+3/2*a1*a1*a1*c1*h0+6*a1*a1*a1*c2*h6-15/2*a1*a1*a2*b0*h6-6*a1*a1*a2*c0*h0-9*a1*a1*a2*c0*h7+3*a1*a1*a2*c1*h6+33/4*a1*a1*b0*b1*h1-37/4*a1*a1*b0*b2*h0+9/2*a1*a1*b0*b2*h7+6*a1*a1*b0*c2*h1-3/4*a1*a1*b1*b1*h0-15/2*a1*a1*b1*b2*h6-9*a1*a1*b1*c2*h0+9/2*a1*a1*b2*c0*h1-21/2*a1*a1*b2*c1*h0+6*a1*a1*b2*c2*h6-6*a1*a2*a2*c0*h6+33/2*a1*a2*b0*b0*h1+16*a1*a2*b0*b1*h0+9*a1*a2*b0*b1*h7-a1*a2*b0*b2*h6+12*a1*a2*b0*c1*h1-a1*a2*b0*c2*h0-12*a1*a2*b0*c2*h7+3*a1*a2*b1*b1*h6+9*a1*a2*b1*c0*h1+6*a1*a2*b1*c1*h0-6*a1*a2*b1*c2*h6-4*a1*a2*b2*c0*h0-18*a1*a2*b2*c0*h7-12*a1*a2*b2*c1*h6-12*a1*a2*c0*c2*h1-12*a1*a2*c1*c2*h0-12*a1*b0*b1*b2*h1+31/2*a1*b0*b2*b2*h0+6*a1*b0*b2*b2*h7+6*a1*b0*b2*c2*h1+21/2*a1*b1*b1*b2*h0-3*a1*b1*b2*b2*h6+6*a1*b1*b2*c2*h0+6*a1*b2*b2*c0*h1+6*a1*b2*b2*c1*h0+35/4*a2*a2*b0*b0*h0+9/2*a2*a2*b0*b0*h7+10*a2*a2*b0*b1*h6+21/2*a2*a2*b0*c0*h1+23/2*a2*a2*b0*c1*h0-6*a2*a2*b0*c1*h7-6*a2*a2*b0*c2*h6+23/2*a2*a2*b1*c0*h0-9*a2*a2*b1*c0*h7-15*a2*a2*b1*c1*h6-9*a2*a2*b2*c0*h6-6*a2*a2*c0*c1*h1-6*a2*a2*c0*c2*h0-6*a2*a2*c1*c1*h0-12*a2*b0*b0*b2*h1-6*a2*b0*b1*b1*h1-26*a2*b0*b1*b2*h0+12*a2*b0*b1*b2*h7+6*a2*b0*b1*c2*h1+6*a2*b0*b2*b2*h6+6*a2*b0*b2*c1*h1+6*a2*b0*b2*c2*h0-6*a2*b1*b1*b1*h0+12*a2*b1*b1*b2*h6+6*a2*b1*b1*c2*h0+12*a2*b1*b2*c0*h1+18*a2*b1*b2*c1*h0+6*a2*b2*b2*c0*h0-9*b0*b1*b2*b2*h1-3*b0*b2*b2*b2*h0-9*b1*b1*b2*b2*h0+a0*a0*a0*b1*h7*h11+a0*a0*a0*b2*h6*h11+a0*a0*a0*b2*h7*h10+a0*a0*a0*c1*h1*h11+a0*a0*a0*c1*h5*h7+a0*a0*a0*c2*h0*h11+a0*a0*a0*c2*h1*h10+a0*a0*a0*c2*h4*h7+a0*a0*a0*c2*h5*h6-a0*a0*a1*b0*h7*h11+2*a0*a0*a1*b1*h6*h11+3*a0*a0*a1*b2*h6*h10-a0*a0*a1*c0*h1*h11-a0*a0*a1*c0*h5*h7+2*a0*a0*a1*c1*h0*h11+2*a0*a0*a1*c1*h5*h6+3*a0*a0*a1*c2*h0*h10+3*a0*a0*a1*c2*h4*h6-a0*a0*a2*b0*h6*h11-a0*a0*a2*b0*h7*h10-a0*a0*a2*b1*h6*h10-a0*a0*a2*c0*h0*h11-a0*a0*a2*c0*h1*h10-a0*a0*a2*c0*h4*h7-a0*a0*a2*c0*h5*h6-a0*a0*a2*c1*h0*h10-a0*a0*a2*c1*h4*h6-a0*a0*b0*b1*h1*h11-a0*a0*b0*b1*h5*h7-a0*a0*b0*b2*h0*h11-a0*a0*b0*b2*h1*h10-a0*a0*b0*b2*h4*h7-a0*a0*b0*b2*h5*h6-a0*a0*b0*c1*h1*h5-a0*a0*b0*c2*h0*h5-a0*a0*b0*c2*h1*h4-a0*a0*b1*b1*h0*h11-a0*a0*b1*b1*h5*h6-a0*a0*b1*b2*h0*h10-a0*a0*b1*b2*h4*h6-a0*a0*b1*c0*h1*h5-2*a0*a0*b1*c1*h0*h5-a0*a0*b1*c2*h0*h4-a0*a0*b2*c0*h0*h5-a0*a0*b2*c0*h1*h4-a0*a0*b2*c1*h0*h4-2*a0*a1*a1*b0*h6*h11-2*a0*a1*a1*c0*h0*h11-2*a0*a1*a1*c0*h5*h6-2*a0*a1*a2*b0*h6*h10-2*a0*a1*a2*c0*h0*h10-2*a0*a1*a2*c0*h4*h6+a0*a1*b0*b0*h1*h11+a0*a1*b0*b0*h5*h7-2*a0*a1*b0*b2*h0*h10-2*a0*a1*b0*b2*h4*h6+2*a0*a1*b0*c0*h1*h5-2*a0*a1*b0*c2*h0*h4-2*a0*a1*b2*c0*h0*h4+a0*a2*b0*b0*h0*h11+a0*a2*b0*b0*h1*h10+a0*a2*b0*b0*h4*h7+a0*a2*b0*b0*h5*h6+2*a0*a2*b0*b1*h0*h10+2*a0*a2*b0*b1*h4*h6+2*a0*a2*b0*c0*h0*h5+2*a0*a2*b0*c0*h1*h4+2*a0*a2*b0*c1*h0*h4+2*a0*a2*b1*c0*h0*h4+a0*b0*b0*b1*h1*h5+a0*b0*b0*b2*h0*h5+a0*b0*b0*b2*h1*h4+2*a0*b0*b1*b1*h0*h5+2*a0*b0*b1*b2*h0*h4+a1*a1*b0*b0*h0*h11+a1*a1*b0*b0*h5*h6+2*a1*a1*b0*c0*h0*h5+a1*a2*b0*b0*h0*h10+a1*a2*b0*b0*h4*h6+2*a1*a2*b0*c0*h0*h4-a1*b0*b0*b0*h1*h5-2*a1*b0*b0*b1*h0*h5+a1*b0*b0*b2*h0*h4-a2*b0*b0*b0*h0*h5-a2*b0*b0*b0*h1*h4-3*a2*b0*b0*b1*h0*h4};
smoothDiscriminant=65536*a0*a0*a0*a0*a0*a2*c0*c2*c2*c2*c2*c2-16384*a0*a0*a0*a0*a0*a2*c1*c1*c2*c2*c2*c2-16384*a0*a0*a0*a0*a0*b2*b2*c0*c2*c2*c2*c2+4096*a0*a0*a0*a0*a0*b2*b2*c1*c1*c2*c2*c2-16384*a0*a0*a0*a0*a1*a1*c0*c2*c2*c2*c2*c2+4096*a0*a0*a0*a0*a1*a1*c1*c1*c2*c2*c2*c2-131072*a0*a0*a0*a0*a1*a2*c0*c1*c2*c2*c2*c2+32768*a0*a0*a0*a0*a1*a2*c1*c1*c1*c2*c2*c2+16384*a0*a0*a0*a0*a1*b1*b2*c0*c2*c2*c2*c2-4096*a0*a0*a0*a0*a1*b1*b2*c1*c1*c2*c2*c2+24576*a0*a0*a0*a0*a1*b2*b2*c0*c1*c2*c2*c2-6144*a0*a0*a0*a0*a1*b2*b2*c1*c1*c1*c2*c2-262144*a0*a0*a0*a0*a2*a2*c0*c0*c2*c2*c2*c2+196608*a0*a0*a0*a0*a2*a2*c0*c1*c1*c2*c2*c2-32768*a0*a0*a0*a0*a2*a2*c1*c1*c1*c1*c2*c2-16384*a0*a0*a0*a0*a2*b0*b0*c2*c2*c2*c2*c2+16384*a0*a0*a0*a0*a2*b0*b1*c1*c2*c2*c2*c2-131072*a0*a0*a0*a0*a2*b0*b2*c0*c2*c2*c2*c2+24576*a0*a0*a0*a0*a2*b0*b2*c1*c1*c2*c2*c2-65536*a0*a0*a0*a0*a2*b1*b1*c0*c2*c2*c2*c2+12288*a0*a0*a0*a0*a2*b1*b1*c1*c1*c2*c2*c2+180224*a0*a0*a0*a0*a2*b1*b2*c0*c1*c2*c2*c2-40960*a0*a0*a0*a0*a2*b1*b2*c1*c1*c1*c2*c2+196608*a0*a0*a0*a0*a2*b2*b2*c0*c0*c2*c2*c2-200704*a0*a0*a0*a0*a2*b2*b2*c0*c1*c1*c2*c2+36864*a0*a0*a0*a0*a2*b2*b2*c1*c1*c1*c1*c2+4096*a0*a0*a0*a0*b0*b0*b2*b2*c2*c2*c2*c2-4096*a0*a0*a0*a0*b0*b1*b2*b2*c1*c2*c2*c2+32768*a0*a0*a0*a0*b0*b2*b2*b2*c0*c2*c2*c2-6144*a0*a0*a0*a0*b0*b2*b2*b2*c1*c1*c2*c2+12288*a0*a0*a0*a0*b1*b1*b2*b2*c0*c2*c2*c2-2048*a0*a0*a0*a0*b1*b1*b2*b2*c1*c1*c2*c2-40960*a0*a0*a0*a0*b1*b2*b2*b2*c0*c1*c2*c2+9216*a0*a0*a0*a0*b1*b2*b2*b2*c1*c1*c1*c2-32768*a0*a0*a0*a0*b2*b2*b2*b2*c0*c0*c2*c2+36864*a0*a0*a0*a0*b2*b2*b2*b2*c0*c1*c1*c2-6912*a0*a0*a0*a0*b2*b2*b2*b2*c1*c1*c1*c1+32768*a0*a0*a0*a1*a1*a1*c0*c1*c2*c2*c2*c2-8192*a0*a0*a0*a1*a1*a1*c1*c1*c1*c2*c2*c2+196608*a0*a0*a0*a1*a1*a2*c0*c0*c2*c2*c2*c2-16384*a0*a0*a0*a1*a1*a2*c0*c1*c1*c2*c2*c2-8192*a0*a0*a0*a1*a1*a2*c1*c1*c1*c1*c2*c2+4096*a0*a0*a0*a1*a1*b0*b0*c2*c2*c2*c2*c2-4096*a0*a0*a0*a1*a1*b0*b1*c1*c2*c2*c2*c2+24576*a0*a0*a0*a1*a1*b0*b2*c0*c2*c2*c2*c2-4096*a0*a0*a0*a1*a1*b0*b2*c1*c1*c2*c2*c2+12288*a0*a0*a0*a1*a1*b1*b1*c0*c2*c2*c2*c2-2048*a0*a0*a0*a1*a1*b1*b1*c1*c1*c2*c2*c2-69632*a0*a0*a0*a1*a1*b1*b2*c0*c1*c2*c2*c2+16384*a0*a0*a0*a1*a1*b1*b2*c1*c1*c1*c2*c2-61440*a0*a0*a0*a1*a1*b2*b2*c0*c0*c2*c2*c2+40960*a0*a0*a0*a1*a1*b2*b2*c0*c1*c1*c2*c2-6144*a0*a0*a0*a1*a1*b2*b2*c1*c1*c1*c1*c2+131072*a0*a0*a0*a1*a2*a2*c0*c0*c1*c2*c2*c2-163840*a0*a0*a0*a1*a2*a2*c0*c1*c1*c1*c2*c2+32768*a0*a0*a0*a1*a2*a2*c1*c1*c1*c1*c1*c2+24576*a0*a0*a0*a1*a2*b0*b0*c1*c2*c2*c2*c2+180224*a0*a0*a0*a1*a2*b0*b1*c0*c2*c2*c2*c2-69632*a0*a0*a0*a1*a2*b0*b1*c1*c1*c2*c2*c2+32768*a0*a0*a0*a1*a2*b0*b2*c0*c1*c2*c2*c2+4096*a0*a0*a0*a1*a2*b0*b2*c1*c1*c1*c2*c2+16384*a0*a0*a0*a1*a2*b1*b1*c0*c1*c2*c2*c2+2048*a0*a0*a0*a1*a2*b1*b1*c1*c1*c1*c2*c2-376832*a0*a0*a0*a1*a2*b1*b2*c0*c0*c2*c2*c2+53248*a0*a0*a0*a1*a2*b1*b2*c0*c1*c1*c2*c2+4096*a0*a0*a0*a1*a2*b1*b2*c1*c1*c1*c1*c2+106496*a0*a0*a0*a1*a2*b2*b2*c0*c0*c1*c2*c2+53248*a0*a0*a0*a1*a2*b2*b2*c0*c1*c1*c1*c2-18432*a0*a0*a0*a1*a2*b2*b2*c1*c1*c1*c1*c1-4096*a0*a0*a0*a1*b0*b0*b1*b2*c2*c2*c2*c2-4096*a0*a0*a0*a1*b0*b0*b2*b2*c1*c2*c2*c2+4096*a0*a0*a0*a1*b0*b1*b1*b2*c1*c2*c2*c2-69632*a0*a0*a0*a1*b0*b1*b2*b2*c0*c2*c2*c2+19456*a0*a0*a0*a1*b0*b1*b2*b2*c1*c1*c2*c2+4096*a0*a0*a0*a1*b0*b2*b2*b2*c0*c1*c2*c2-3072*a0*a0*a0*a1*b0*b2*b2*b2*c1*c1*c1*c2-12288*a0*a0*a0*a1*b1*b1*b1*b2*c0*c2*c2*c2+2048*a0*a0*a0*a1*b1*b1*b1*b2*c1*c1*c2*c2+47104*a0*a0*a0*a1*b1*b1*b2*b2*c0*c1*c2*c2-11776*a0*a0*a0*a1*b1*b1*b2*b2*c1*c1*c1*c2+106496*a0*a0*a0*a1*b1*b2*b2*b2*c0*c0*c2*c2-60416*a0*a0*a0*a1*b1*b2*b2*b2*c0*c1*c1*c2+9216*a0*a0*a0*a1*b1*b2*b2*b2*c1*c1*c1*c1-40960*a0*a0*a0*a1*b2*b2*b2*b2*c0*c0*c1*c2+9216*a0*a0*a0*a1*b2*b2*b2*b2*c0*c1*c1*c1+393216*a0*a0*a0*a2*a2*a2*c0*c0*c0*c2*c2*c2-360448*a0*a0*a0*a2*a2*a2*c0*c0*c1*c1*c2*c2+131072*a0*a0*a0*a2*a2*a2*c0*c1*c1*c1*c1*c2-16384*a0*a0*a0*a2*a2*a2*c1*c1*c1*c1*c1*c1+196608*a0*a0*a0*a2*a2*b0*b0*c0*c2*c2*c2*c2-61440*a0*a0*a0*a2*a2*b0*b0*c1*c1*c2*c2*c2-376832*a0*a0*a0*a2*a2*b0*b1*c0*c1*c2*c2*c2+106496*a0*a0*a0*a2*a2*b0*b1*c1*c1*c1*c2*c2+131072*a0*a0*a0*a2*a2*b0*b2*c0*c0*c2*c2*c2+106496*a0*a0*a0*a2*a2*b0*b2*c0*c1*c1*c2*c2-40960*a0*a0*a0*a2*a2*b0*b2*c1*c1*c1*c1*c2+65536*a0*a0*a0*a2*a2*b1*b1*c0*c0*c2*c2*c2+53248*a0*a0*a0*a2*a2*b1*b1*c0*c1*c1*c2*c2-20480*a0*a0*a0*a2*a2*b1*b1*c1*c1*c1*c1*c2+180224*a0*a0*a0*a2*a2*b1*b2*c0*c0*c1*c2*c2-131072*a0*a0*a0*a2*a2*b1*b2*c0*c1*c1*c1*c2+24576*a0*a0*a0*a2*a2*b1*b2*c1*c1*c1*c1*c1-360448*a0*a0*a0*a2*a2*b2*b2*c0*c0*c0*c2*c2+126976*a0*a0*a0*a2*a2*b2*b2*c0*c0*c1*c1*c2-12288*a0*a0*a0*a2*a2*b2*b2*c0*c1*c1*c1*c1+32768*a0*a0*a0*a2*b0*b0*b0*b2*c2*c2*c2*c2+12288*a0*a0*a0*a2*b0*b0*b1*b1*c2*c2*c2*c2-69632*a0*a0*a0*a2*b0*b0*b1*b2*c1*c2*c2*c2-16384*a0*a0*a0*a2*b0*b0*b2*b2*c0*c2*c2*c2+40960*a0*a0*a0*a2*b0*b0*b2*b2*c1*c1*c2*c2-12288*a0*a0*a0*a2*b0*b1*b1*b1*c1*c2*c2*c2+16384*a0*a0*a0*a2*b0*b1*b1*b2*c0*c2*c2*c2+47104*a0*a0*a0*a2*b0*b1*b1*b2*c1*c1*c2*c2+53248*a0*a0*a0*a2*b0*b1*b2*b2*c0*c1*c2*c2-60416*a0*a0*a0*a2*b0*b1*b2*b2*c1*c1*c1*c2-163840*a0*a0*a0*a2*b0*b2*b2*b2*c0*c0*c2*c2+53248*a0*a0*a0*a2*b0*b2*b2*b2*c0*c1*c1*c2+9216*a0*a0*a0*a2*b0*b2*b2*b2*c1*c1*c1*c1+24576*a0*a0*a0*a2*b1*b1*b1*b1*c0*c2*c2*c2-3072*a0*a0*a0*a2*b1*b1*b1*b1*c1*c1*c2*c2-94208*a0*a0*a0*a2*b1*b1*b1*b2*c0*c1*c2*c2+11264*a0*a0*a0*a2*b1*b1*b1*b2*c1*c1*c1*c2+53248*a0*a0*a0*a2*b1*b1*b2*b2*c0*c0*c2*c2+77824*a0*a0*a0*a2*b1*b1*b2*b2*c0*c1*c1*c2-7680*a0*a0*a0*a2*b1*b1*b2*b2*c1*c1*c1*c1-131072*a0*a0*a0*a2*b1*b2*b2*b2*c0*c0*c1*c2+3072*a0*a0*a0*a2*b1*b2*b2*b2*c0*c1*c1*c1+131072*a0*a0*a0*a2*b2*b2*b2*b2*c0*c0*c0*c2-12288*a0*a0*a0*a2*b2*b2*b2*b2*c0*c0*c1*c1-8192*a0*a0*a0*b0*b0*b0*b2*b2*b2*c2*c2*c2-2048*a0*a0*a0*b0*b0*b1*b1*b2*b2*c2*c2*c2+16384*a0*a0*a0*b0*b0*b1*b2*b2*b2*c1*c2*c2-8192*a0*a0*a0*b0*b0*b2*b2*b2*b2*c0*c2*c2-6144*a0*a0*a0*b0*b0*b2*b2*b2*b2*c1*c1*c2+2048*a0*a0*a0*b0*b1*b1*b1*b2*b2*c1*c2*c2+2048*a0*a0*a0*b0*b1*b1*b2*b2*b2*c0*c2*c2-11776*a0*a0*a0*b0*b1*b1*b2*b2*b2*c1*c1*c2+4096*a0*a0*a0*b0*b1*b2*b2*b2*b2*c0*c1*c2+9216*a0*a0*a0*b0*b1*b2*b2*b2*b2*c1*c1*c1+32768*a0*a0*a0*b0*b2*b2*b2*b2*b2*c0*c0*c2-18432*a0*a0*a0*b0*b2*b2*b2*b2*b2*c0*c1*c1-3072*a0*a0*a0*b1*b1*b1*b1*b2*b2*c0*c2*c2+256*a0*a0*a0*b1*b1*b1*b1*b2*b2*c1*c1*c2+11264*a0*a0*a0*b1*b1*b1*b2*b2*b2*c0*c1*c2-256*a0*a0*a0*b1*b1*b1*b2*b2*b2*c1*c1*c1-20480*a0*a0*a0*b1*b1*b2*b2*b2*b2*c0*c0*c2-7680*a0*a0*a0*b1*b1*b2*b2*b2*b2*c0*c1*c1+24576*a0*a0*a0*b1*b2*b2*b2*b2*b2*c0*c0*c1-16384*a0*a0*a0*b2*b2*b2*b2*b2*b2*c0*c0*c0-32768*a0*a0*a1*a1*a1*a1*c0*c0*c2*c2*c2*c2-8192*a0*a0*a1*a1*a1*a1*c0*c1*c1*c2*c2*c2+4096*a0*a0*a1*a1*a1*a1*c1*c1*c1*c1*c2*c2-163840*a0*a0*a1*a1*a1*a2*c0*c0*c1*c2*c2*c2+73728*a0*a0*a1*a1*a1*a2*c0*c1*c1*c1*c2*c2-8192*a0*a0*a1*a1*a1*a2*c1*c1*c1*c1*c1*c2-6144*a0*a0*a1*a1*a1*b0*b0*c1*c2*c2*c2*c2-40960*a0*a0*a1*a1*a1*b0*b1*c0*c2*c2*c2*c2+16384*a0*a0*a1*a1*a1*b0*b1*c1*c1*c2*c2*c2+4096*a0*a0*a1*a1*a1*b0*b2*c0*c1*c2*c2*c2-4096*a0*a0*a1*a1*a1*b0*b2*c1*c1*c1*c2*c2+2048*a0*a0*a1*a1*a1*b1*b1*c0*c1*c2*c2*c2-2048*a0*a0*a1*a1*a1*b1*b1*c1*c1*c1*c2*c2+106496*a0*a0*a1*a1*a1*b1*b2*c0*c0*c2*c2*c2-4096*a0*a0*a1*a1*a1*b1*b2*c0*c1*c1*c2*c2-4096*a0*a0*a1*a1*a1*b1*b2*c1*c1*c1*c1*c2-14336*a0*a0*a1*a1*a1*b2*b2*c0*c0*c1*c2*c2-14336*a0*a0*a1*a1*a1*b2*b2*c0*c1*c1*c1*c2+4096*a0*a0*a1*a1*a1*b2*b2*c1*c1*c1*c1*c1-360448*a0*a0*a1*a1*a2*a2*c0*c0*c0*c2*c2*c2+417792*a0*a0*a1*a1*a2*a2*c0*c0*c1*c1*c2*c2-98304*a0*a0*a1*a1*a2*a2*c0*c1*c1*c1*c1*c2+4096*a0*a0*a1*a1*a2*a2*c1*c1*c1*c1*c1*c1-200704*a0*a0*a1*a1*a2*b0*b0*c0*c2*c2*c2*c2+40960*a0*a0*a1*a1*a2*b0*b0*c1*c1*c2*c2*c2+53248*a0*a0*a1*a1*a2*b0*b1*c0*c1*c2*c2*c2-4096*a0*a0*a1*a1*a2*b0*b1*c1*c1*c1*c2*c2+106496*a0*a0*a1*a1*a2*b0*b2*c0*c0*c2*c2*c2-110592*a0*a0*a1*a1*a2*b0*b2*c0*c1*c1*c2*c2+16384*a0*a0*a1*a1*a2*b0*b2*c1*c1*c1*c1*c2+53248*a0*a0*a1*a1*a2*b1*b1*c0*c0*c2*c2*c2-55296*a0*a0*a1*a1*a2*b1*b1*c0*c1*c1*c2*c2+8192*a0*a0*a1*a1*a2*b1*b1*c1*c1*c1*c1*c2+86016*a0*a0*a1*a1*a2*b1*b2*c0*c0*c1*c2*c2+4096*a0*a0*a1*a1*a2*b1*b2*c0*c1*c1*c1*c2-4096*a0*a0*a1*a1*a2*b1*b2*c1*c1*c1*c1*c1+126976*a0*a0*a1*a1*a2*b2*b2*c0*c0*c0*c2*c2-196608*a0*a0*a1*a1*a2*b2*b2*c0*c0*c1*c1*c2+38912*a0*a0*a1*a1*a2*b2*b2*c0*c1*c1*c1*c1-6144*a0*a0*a1*a1*b0*b0*b0*b2*c2*c2*c2*c2-2048*a0*a0*a1*a1*b0*b0*b1*b1*c2*c2*c2*c2+19456*a0*a0*a1*a1*b0*b0*b1*b2*c1*c2*c2*c2+40960*a0*a0*a1*a1*b0*b0*b2*b2*c0*c2*c2*c2-16896*a0*a0*a1*a1*b0*b0*b2*b2*c1*c1*c2*c2+2048*a0*a0*a1*a1*b0*b1*b1*b1*c1*c2*c2*c2+47104*a0*a0*a1*a1*b0*b1*b1*b2*c0*c2*c2*c2-27648*a0*a0*a1*a1*b0*b1*b1*b2*c1*c1*c2*c2-30720*a0*a0*a1*a1*b0*b1*b2*b2*c0*c1*c2*c2+19456*a0*a0*a1*a1*b0*b1*b2*b2*c1*c1*c1*c2-14336*a0*a0*a1*a1*b0*b2*b2*b2*c0*c0*c2*c2+19456*a0*a0*a1*a1*b0*b2*b2*b2*c0*c1*c1*c2-6144*a0*a0*a1*a1*b0*b2*b2*b2*c1*c1*c1*c1-3072*a0*a0*a1*a1*b1*b1*b1*b1*c0*c2*c2*c2+256*a0*a0*a1*a1*b1*b1*b1*b1*c1*c1*c2*c2+7168*a0*a0*a1*a1*b1*b1*b1*b2*c0*c1*c2*c2+2048*a0*a0*a1*a1*b1*b1*b1*b2*c1*c1*c1*c2-116736*a0*a0*a1*a1*b1*b1*b2*b2*c0*c0*c2*c2+19968*a0*a0*a1*a1*b1*b1*b2*b2*c0*c1*c1*c2-2048*a0*a0*a1*a1*b1*b1*b2*b2*c1*c1*c1*c1+80896*a0*a0*a1*a1*b1*b2*b2*b2*c0*c0*c1*c2-13312*a0*a0*a1*a1*b1*b2*b2*b2*c0*c1*c1*c1-12288*a0*a0*a1*a1*b2*b2*b2*b2*c0*c0*c0*c2-512*a0*a0*a1*a1*b2*b2*b2*b2*c0*c0*c1*c1+131072*a0*a0*a1*a2*a2*a2*c0*c0*c0*c1*c2*c2-163840*a0*a0*a1*a2*a2*a2*c0*c0*c1*c1*c1*c2+32768*a0*a0*a1*a2*a2*a2*c0*c1*c1*c1*c1*c1+106496*a0*a0*a1*a2*a2*b0*b0*c0*c1*c2*c2*c2-14336*a0*a0*a1*a2*a2*b0*b0*c1*c1*c1*c2*c2+180224*a0*a0*a1*a2*a2*b0*b1*c0*c0*c2*c2*c2+86016*a0*a0*a1*a2*a2*b0*b1*c0*c1*c1*c2*c2-45056*a0*a0*a1*a2*a2*b0*b1*c1*c1*c1*c1*c2-589824*a0*a0*a1*a2*a2*b0*b2*c0*c0*c1*c2*c2+188416*a0*a0*a1*a2*a2*b0*b2*c0*c1*c1*c1*c2-4096*a0*a0*a1*a2*a2*b0*b2*c1*c1*c1*c1*c1-294912*a0*a0*a1*a2*a2*b1*b1*c0*c0*c1*c2*c2+94208*a0*a0*a1*a2*a2*b1*b1*c0*c1*c1*c1*c2-2048*a0*a0*a1*a2*a2*b1*b1*c1*c1*c1*c1*c1+180224*a0*a0*a1*a2*a2*b1*b2*c0*c0*c0*c2*c2+86016*a0*a0*a1*a2*a2*b1*b2*c0*c0*c1*c1*c2-45056*a0*a0*a1*a2*a2*b1*b2*c0*c1*c1*c1*c1+106496*a0*a0*a1*a2*a2*b2*b2*c0*c0*c0*c1*c2-14336*a0*a0*a1*a2*a2*b2*b2*c0*c0*c1*c1*c1-40960*a0*a0*a1*a2*b0*b0*b0*b1*c2*c2*c2*c2+4096*a0*a0*a1*a2*b0*b0*b0*b2*c1*c2*c2*c2+47104*a0*a0*a1*a2*b0*b0*b1*b1*c1*c2*c2*c2+53248*a0*a0*a1*a2*b0*b0*b1*b2*c0*c2*c2*c2-30720*a0*a0*a1*a2*b0*b0*b1*b2*c1*c1*c2*c2-110592*a0*a0*a1*a2*b0*b0*b2*b2*c0*c1*c2*c2+19456*a0*a0*a1*a2*b0*b0*b2*b2*c1*c1*c1*c2-94208*a0*a0*a1*a2*b0*b1*b1*b1*c0*c2*c2*c2+7168*a0*a0*a1*a2*b0*b1*b1*b1*c1*c1*c2*c2+110592*a0*a0*a1*a2*b0*b1*b1*b2*c0*c1*c2*c2-20480*a0*a0*a1*a2*b0*b1*b1*b2*c1*c1*c1*c2+86016*a0*a0*a1*a2*b0*b1*b2*b2*c0*c0*c2*c2-107520*a0*a0*a1*a2*b0*b1*b2*b2*c0*c1*c1*c2+31744*a0*a0*a1*a2*b0*b1*b2*b2*c1*c1*c1*c1+188416*a0*a0*a1*a2*b0*b2*b2*b2*c0*c0*c1*c2-66560*a0*a0*a1*a2*b0*b2*b2*b2*c0*c1*c1*c1+16384*a0*a0*a1*a2*b1*b1*b1*b1*c0*c1*c2*c2-2560*a0*a0*a1*a2*b1*b1*b1*b1*c1*c1*c1*c2+40960*a0*a0*a1*a2*b1*b1*b1*b2*c0*c0*c2*c2-17408*a0*a0*a1*a2*b1*b1*b1*b2*c0*c1*c1*c2+2048*a0*a0*a1*a2*b1*b1*b1*b2*c1*c1*c1*c1-12288*a0*a0*a1*a2*b1*b1*b2*b2*c0*c0*c1*c2-12800*a0*a0*a1*a2*b1*b1*b2*b2*c0*c1*c1*c1-131072*a0*a0*a1*a2*b1*b2*b2*b2*c0*c0*c0*c2+80896*a0*a0*a1*a2*b1*b2*b2*b2*c0*c0*c1*c1-40960*a0*a0*a1*a2*b2*b2*b2*b2*c0*c0*c0*c1+16384*a0*a0*a1*b0*b0*b0*b1*b2*b2*c2*c2*c2-4096*a0*a0*a1*b0*b0*b0*b2*b2*b2*c1*c2*c2+2048*a0*a0*a1*b0*b0*b1*b1*b1*b2*c2*c2*c2-27648*a0*a0*a1*b0*b0*b1*b1*b2*b2*c1*c2*c2-4096*a0*a0*a1*b0*b0*b1*b2*b2*b2*c0*c2*c2+19456*a0*a0*a1*b0*b0*b1*b2*b2*b2*c1*c1*c2+16384*a0*a0*a1*b0*b0*b2*b2*b2*b2*c0*c1*c2-6144*a0*a0*a1*b0*b0*b2*b2*b2*b2*c1*c1*c1-2048*a0*a0*a1*b0*b1*b1*b1*b1*b2*c1*c2*c2+7168*a0*a0*a1*b0*b1*b1*b1*b2*b2*c0*c2*c2+14592*a0*a0*a1*b0*b1*b1*b1*b2*b2*c1*c1*c2-20480*a0*a0*a1*b0*b1*b1*b2*b2*b2*c0*c1*c2-11776*a0*a0*a1*b0*b1*b1*b2*b2*b2*c1*c1*c1-45056*a0*a0*a1*b0*b1*b2*b2*b2*b2*c0*c0*c2+31744*a0*a0*a1*b0*b1*b2*b2*b2*b2*c0*c1*c1-4096*a0*a0*a1*b0*b2*b2*b2*b2*b2*c0*c0*c1+3072*a0*a0*a1*b1*b1*b1*b1*b1*b2*c0*c2*c2-256*a0*a0*a1*b1*b1*b1*b1*b1*b2*c1*c1*c2-14336*a0*a0*a1*b1*b1*b1*b1*b2*b2*c0*c1*c2+256*a0*a0*a1*b1*b1*b1*b1*b2*b2*c1*c1*c1+29696*a0*a0*a1*b1*b1*b1*b2*b2*b2*c0*c0*c2+10496*a0*a0*a1*b1*b1*b1*b2*b2*b2*c0*c1*c1-35840*a0*a0*a1*b1*b1*b2*b2*b2*b2*c0*c0*c1+24576*a0*a0*a1*b1*b2*b2*b2*b2*b2*c0*c0*c0-262144*a0*a0*a2*a2*a2*a2*c0*c0*c0*c0*c2*c2+196608*a0*a0*a2*a2*a2*a2*c0*c0*c0*c1*c1*c2-32768*a0*a0*a2*a2*a2*a2*c0*c0*c1*c1*c1*c1-360448*a0*a0*a2*a2*a2*b0*b0*c0*c0*c2*c2*c2+126976*a0*a0*a2*a2*a2*b0*b0*c0*c1*c1*c2*c2-12288*a0*a0*a2*a2*a2*b0*b0*c1*c1*c1*c1*c2+180224*a0*a0*a2*a2*a2*b0*b1*c0*c0*c1*c2*c2-131072*a0*a0*a2*a2*a2*b0*b1*c0*c1*c1*c1*c2+24576*a0*a0*a2*a2*a2*b0*b1*c1*c1*c1*c1*c1+131072*a0*a0*a2*a2*a2*b0*b2*c0*c0*c0*c2*c2+106496*a0*a0*a2*a2*a2*b0*b2*c0*c0*c1*c1*c2-40960*a0*a0*a2*a2*a2*b0*b2*c0*c1*c1*c1*c1+65536*a0*a0*a2*a2*a2*b1*b1*c0*c0*c0*c2*c2+53248*a0*a0*a2*a2*a2*b1*b1*c0*c0*c1*c1*c2-20480*a0*a0*a2*a2*a2*b1*b1*c0*c1*c1*c1*c1-376832*a0*a0*a2*a2*a2*b1*b2*c0*c0*c0*c1*c2+106496*a0*a0*a2*a2*a2*b1*b2*c0*c0*c1*c1*c1+196608*a0*a0*a2*a2*a2*b2*b2*c0*c0*c0*c0*c2-61440*a0*a0*a2*a2*a2*b2*b2*c0*c0*c0*c1*c1-32768*a0*a0*a2*a2*b0*b0*b0*b0*c2*c2*c2*c2+106496*a0*a0*a2*a2*b0*b0*b0*b1*c1*c2*c2*c2-163840*a0*a0*a2*a2*b0*b0*b0*b2*c0*c2*c2*c2-14336*a0*a0*a2*a2*b0*b0*b0*b2*c1*c1*c2*c2+53248*a0*a0*a2*a2*b0*b0*b1*b1*c0*c2*c2*c2-116736*a0*a0*a2*a2*b0*b0*b1*b1*c1*c1*c2*c2+86016*a0*a0*a2*a2*b0*b0*b1*b2*c0*c1*c2*c2+80896*a0*a0*a2*a2*b0*b0*b1*b2*c1*c1*c1*c2+417792*a0*a0*a2*a2*b0*b0*b2*b2*c0*c0*c2*c2-196608*a0*a0*a2*a2*b0*b0*b2*b2*c0*c1*c1*c2-512*a0*a0*a2*a2*b0*b0*b2*b2*c1*c1*c1*c1+40960*a0*a0*a2*a2*b0*b1*b1*b1*c0*c1*c2*c2+29696*a0*a0*a2*a2*b0*b1*b1*b1*c1*c1*c1*c2-294912*a0*a0*a2*a2*b0*b1*b1*b2*c0*c0*c2*c2-12288*a0*a0*a2*a2*b0*b1*b1*b2*c0*c1*c1*c2-35840*a0*a0*a2*a2*b0*b1*b1*b2*c1*c1*c1*c1+86016*a0*a0*a2*a2*b0*b1*b2*b2*c0*c0*c1*c2+80896*a0*a0*a2*a2*b0*b1*b2*b2*c0*c1*c1*c1-163840*a0*a0*a2*a2*b0*b2*b2*b2*c0*c0*c0*c2-14336*a0*a0*a2*a2*b0*b2*b2*b2*c0*c0*c1*c1+16384*a0*a0*a2*a2*b1*b1*b1*b1*c0*c0*c2*c2-26624*a0*a0*a2*a2*b1*b1*b1*b1*c0*c1*c1*c2+256*a0*a0*a2*a2*b1*b1*b1*b1*c1*c1*c1*c1+40960*a0*a0*a2*a2*b1*b1*b1*b2*c0*c0*c1*c2+29696*a0*a0*a2*a2*b1*b1*b1*b2*c0*c1*c1*c1+53248*a0*a0*a2*a2*b1*b1*b2*b2*c0*c0*c0*c2-116736*a0*a0*a2*a2*b1*b1*b2*b2*c0*c0*c1*c1+106496*a0*a0*a2*a2*b1*b2*b2*b2*c0*c0*c0*c1-32768*a0*a0*a2*a2*b2*b2*b2*b2*c0*c0*c0*c0-8192*a0*a0*a2*b0*b0*b0*b0*b2*b2*c2*c2*c2+2048*a0*a0*a2*b0*b0*b0*b1*b1*b2*c2*c2*c2-4096*a0*a0*a2*b0*b0*b0*b1*b2*b2*c1*c2*c2+73728*a0*a0*a2*b0*b0*b0*b2*b2*b2*c0*c2*c2-14336*a0*a0*a2*b0*b0*b0*b2*b2*b2*c1*c1*c2-3072*a0*a0*a2*b0*b0*b1*b1*b1*b1*c2*c2*c2+7168*a0*a0*a2*b0*b0*b1*b1*b1*b2*c1*c2*c2-55296*a0*a0*a2*b0*b0*b1*b1*b2*b2*c0*c2*c2+19968*a0*a0*a2*b0*b0*b1*b1*b2*b2*c1*c1*c2+4096*a0*a0*a2*b0*b0*b1*b2*b2*b2*c0*c1*c2-13312*a0*a0*a2*b0*b0*b1*b2*b2*b2*c1*c1*c1-98304*a0*a0*a2*b0*b0*b2*b2*b2*b2*c0*c0*c2+38912*a0*a0*a2*b0*b0*b2*b2*b2*b2*c0*c1*c1+3072*a0*a0*a2*b0*b1*b1*b1*b1*b1*c1*c2*c2+16384*a0*a0*a2*b0*b1*b1*b1*b1*b2*c0*c2*c2-14336*a0*a0*a2*b0*b1*b1*b1*b1*b2*c1*c1*c2-17408*a0*a0*a2*b0*b1*b1*b1*b2*b2*c0*c1*c2+10496*a0*a0*a2*b0*b1*b1*b1*b2*b2*c1*c1*c1+94208*a0*a0*a2*b0*b1*b1*b2*b2*b2*c0*c0*c2-12800*a0*a0*a2*b0*b1*b1*b2*b2*b2*c0*c1*c1-45056*a0*a0*a2*b0*b1*b2*b2*b2*b2*c0*c0*c1+32768*a0*a0*a2*b0*b2*b2*b2*b2*b2*c0*c0*c0-4096*a0*a0*a2*b1*b1*b1*b1*b1*b1*c0*c2*c2+256*a0*a0*a2*b1*b1*b1*b1*b1*b1*c1*c1*c2+13312*a0*a0*a2*b1*b1*b1*b1*b1*b2*c0*c1*c2-256*a0*a0*a2*b1*b1*b1*b1*b1*b2*c1*c1*c1-26624*a0*a0*a2*b1*b1*b1*b1*b2*b2*c0*c0*c2-8448*a0*a0*a2*b1*b1*b1*b1*b2*b2*c0*c1*c1+29696*a0*a0*a2*b1*b1*b1*b2*b2*b2*c0*c0*c1-20480*a0*a0*a2*b1*b1*b2*b2*b2*b2*c0*c0*c0+4096*a0*a0*b0*b0*b0*b0*b2*b2*b2*b2*c2*c2-2048*a0*a0*b0*b0*b0*b1*b1*b2*b2*b2*c2*c2-4096*a0*a0*b0*b0*b0*b1*b2*b2*b2*b2*c1*c2-8192*a0*a0*b0*b0*b0*b2*b2*b2*b2*b2*c0*c2+4096*a0*a0*b0*b0*b0*b2*b2*b2*b2*b2*c1*c1+256*a0*a0*b0*b0*b1*b1*b1*b1*b2*b2*c2*c2+2048*a0*a0*b0*b0*b1*b1*b1*b2*b2*b2*c1*c2+8192*a0*a0*b0*b0*b1*b1*b2*b2*b2*b2*c0*c2-2048*a0*a0*b0*b0*b1*b1*b2*b2*b2*b2*c1*c1-4096*a0*a0*b0*b0*b1*b2*b2*b2*b2*b2*c0*c1+4096*a0*a0*b0*b0*b2*b2*b2*b2*b2*b2*c0*c0-256*a0*a0*b0*b1*b1*b1*b1*b1*b2*b2*c1*c2-2560*a0*a0*b0*b1*b1*b1*b1*b2*b2*b2*c0*c2+256*a0*a0*b0*b1*b1*b1*b1*b2*b2*b2*c1*c1+2048*a0*a0*b0*b1*b1*b1*b2*b2*b2*b2*c0*c1-2048*a0*a0*b0*b1*b1*b2*b2*b2*b2*b2*c0*c0+256*a0*a0*b1*b1*b1*b1*b1*b1*b2*b2*c0*c2-256*a0*a0*b1*b1*b1*b1*b1*b2*b2*b2*c0*c1+256*a0*a0*b1*b1*b1*b1*b2*b2*b2*b2*c0*c0+32768*a0*a1*a1*a1*a1*a1*c0*c0*c1*c2*c2*c2-8192*a0*a1*a1*a1*a1*a1*c0*c1*c1*c1*c2*c2+131072*a0*a1*a1*a1*a1*a2*c0*c0*c0*c2*c2*c2-98304*a0*a1*a1*a1*a1*a2*c0*c0*c1*c1*c2*c2+16384*a0*a1*a1*a1*a1*a2*c0*c1*c1*c1*c1*c2+36864*a0*a1*a1*a1*a1*b0*b0*c0*c2*c2*c2*c2-6144*a0*a1*a1*a1*a1*b0*b0*c1*c1*c2*c2*c2+4096*a0*a1*a1*a1*a1*b0*b1*c0*c1*c2*c2*c2-4096*a0*a1*a1*a1*a1*b0*b1*c1*c1*c1*c2*c2-40960*a0*a1*a1*a1*a1*b0*b2*c0*c0*c2*c2*c2+16384*a0*a1*a1*a1*a1*b0*b2*c0*c1*c1*c2*c2-20480*a0*a1*a1*a1*a1*b1*b1*c0*c0*c2*c2*c2+8192*a0*a1*a1*a1*a1*b1*b1*c0*c1*c1*c2*c2-45056*a0*a1*a1*a1*a1*b1*b2*c0*c0*c1*c2*c2+8192*a0*a1*a1*a1*a1*b1*b2*c0*c1*c1*c1*c2-12288*a0*a1*a1*a1*a1*b2*b2*c0*c0*c0*c2*c2+38912*a0*a1*a1*a1*a1*b2*b2*c0*c0*c1*c1*c2-8192*a0*a1*a1*a1*a1*b2*b2*c0*c1*c1*c1*c1-163840*a0*a1*a1*a1*a2*a2*c0*c0*c0*c1*c2*c2+73728*a0*a1*a1*a1*a2*a2*c0*c0*c1*c1*c1*c2-8192*a0*a1*a1*a1*a2*a2*c0*c1*c1*c1*c1*c1+53248*a0*a1*a1*a1*a2*b0*b0*c0*c1*c2*c2*c2-14336*a0*a1*a1*a1*a2*b0*b0*c1*c1*c1*c2*c2-131072*a0*a1*a1*a1*a2*b0*b1*c0*c0*c2*c2*c2+4096*a0*a1*a1*a1*a2*b0*b1*c0*c1*c1*c2*c2+8192*a0*a1*a1*a1*a2*b0*b1*c1*c1*c1*c1*c2+188416*a0*a1*a1*a1*a2*b0*b2*c0*c0*c1*c2*c2-49152*a0*a1*a1*a1*a2*b0*b2*c0*c1*c1*c1*c2+94208*a0*a1*a1*a1*a2*b1*b1*c0*c0*c1*c2*c2-24576*a0*a1*a1*a1*a2*b1*b1*c0*c1*c1*c1*c2-131072*a0*a1*a1*a1*a2*b1*b2*c0*c0*c0*c2*c2+4096*a0*a1*a1*a1*a2*b1*b2*c0*c0*c1*c1*c2+8192*a0*a1*a1*a1*a2*b1*b2*c0*c1*c1*c1*c1+53248*a0*a1*a1*a1*a2*b2*b2*c0*c0*c0*c1*c2-14336*a0*a1*a1*a1*a2*b2*b2*c0*c0*c1*c1*c1+9216*a0*a1*a1*a1*b0*b0*b0*b1*c2*c2*c2*c2-3072*a0*a1*a1*a1*b0*b0*b0*b2*c1*c2*c2*c2-11776*a0*a1*a1*a1*b0*b0*b1*b1*c1*c2*c2*c2-60416*a0*a1*a1*a1*b0*b0*b1*b2*c0*c2*c2*c2+19456*a0*a1*a1*a1*b0*b0*b1*b2*c1*c1*c2*c2+19456*a0*a1*a1*a1*b0*b0*b2*b2*c0*c1*c2*c2-4096*a0*a1*a1*a1*b0*b0*b2*b2*c1*c1*c1*c2+11264*a0*a1*a1*a1*b0*b1*b1*b1*c0*c2*c2*c2+2048*a0*a1*a1*a1*b0*b1*b1*b1*c1*c1*c2*c2-20480*a0*a1*a1*a1*b0*b1*b1*b2*c0*c1*c2*c2+4096*a0*a1*a1*a1*b0*b1*b1*b2*c1*c1*c1*c2+80896*a0*a1*a1*a1*b0*b1*b2*b2*c0*c0*c2*c2-14336*a0*a1*a1*a1*b0*b1*b2*b2*c0*c1*c1*c2-4096*a0*a1*a1*a1*b0*b1*b2*b2*c1*c1*c1*c1-66560*a0*a1*a1*a1*b0*b2*b2*b2*c0*c0*c1*c2+20480*a0*a1*a1*a1*b0*b2*b2*b2*c0*c1*c1*c1-2560*a0*a1*a1*a1*b1*b1*b1*b1*c0*c1*c2*c2+29696*a0*a1*a1*a1*b1*b1*b1*b2*c0*c0*c2*c2-8192*a0*a1*a1*a1*b1*b1*b1*b2*c0*c1*c1*c2-12800*a0*a1*a1*a1*b1*b1*b2*b2*c0*c0*c1*c2+8192*a0*a1*a1*a1*b1*b1*b2*b2*c0*c1*c1*c1+3072*a0*a1*a1*a1*b1*b2*b2*b2*c0*c0*c0*c2-13312*a0*a1*a1*a1*b1*b2*b2*b2*c0*c0*c1*c1+9216*a0*a1*a1*a1*b2*b2*b2*b2*c0*c0*c0*c1+196608*a0*a1*a1*a2*a2*a2*c0*c0*c0*c0*c2*c2-16384*a0*a1*a1*a2*a2*a2*c0*c0*c0*c1*c1*c2-8192*a0*a1*a1*a2*a2*a2*c0*c0*c1*c1*c1*c1+126976*a0*a1*a1*a2*a2*b0*b0*c0*c0*c2*c2*c2-196608*a0*a1*a1*a2*a2*b0*b0*c0*c1*c1*c2*c2+38912*a0*a1*a1*a2*a2*b0*b0*c1*c1*c1*c1*c2+86016*a0*a1*a1*a2*a2*b0*b1*c0*c0*c1*c2*c2+4096*a0*a1*a1*a2*a2*b0*b1*c0*c1*c1*c1*c2-4096*a0*a1*a1*a2*a2*b0*b1*c1*c1*c1*c1*c1+106496*a0*a1*a1*a2*a2*b0*b2*c0*c0*c0*c2*c2-110592*a0*a1*a1*a2*a2*b0*b2*c0*c0*c1*c1*c2+16384*a0*a1*a1*a2*a2*b0*b2*c0*c1*c1*c1*c1+53248*a0*a1*a1*a2*a2*b1*b1*c0*c0*c0*c2*c2-55296*a0*a1*a1*a2*a2*b1*b1*c0*c0*c1*c1*c2+8192*a0*a1*a1*a2*a2*b1*b1*c0*c1*c1*c1*c1+53248*a0*a1*a1*a2*a2*b1*b2*c0*c0*c0*c1*c2-4096*a0*a1*a1*a2*a2*b1*b2*c0*c0*c1*c1*c1-200704*a0*a1*a1*a2*a2*b2*b2*c0*c0*c0*c0*c2+40960*a0*a1*a1*a2*a2*b2*b2*c0*c0*c0*c1*c1+36864*a0*a1*a1*a2*b0*b0*b0*b0*c2*c2*c2*c2-60416*a0*a1*a1*a2*b0*b0*b0*b1*c1*c2*c2*c2+53248*a0*a1*a1*a2*b0*b0*b0*b2*c0*c2*c2*c2+19456*a0*a1*a1*a2*b0*b0*b0*b2*c1*c1*c2*c2+77824*a0*a1*a1*a2*b0*b0*b1*b1*c0*c2*c2*c2+19968*a0*a1*a1*a2*b0*b0*b1*b1*c1*c1*c2*c2-107520*a0*a1*a1*a2*b0*b0*b1*b2*c0*c1*c2*c2-14336*a0*a1*a1*a2*b0*b0*b1*b2*c1*c1*c1*c2-196608*a0*a1*a1*a2*b0*b0*b2*b2*c0*c0*c2*c2+178176*a0*a1*a1*a2*b0*b0*b2*b2*c0*c1*c1*c2-20480*a0*a1*a1*a2*b0*b0*b2*b2*c1*c1*c1*c1-17408*a0*a1*a1*a2*b0*b1*b1*b1*c0*c1*c2*c2-8192*a0*a1*a1*a2*b0*b1*b1*b1*c1*c1*c1*c2-12288*a0*a1*a1*a2*b0*b1*b1*b2*c0*c0*c2*c2+61440*a0*a1*a1*a2*b0*b1*b1*b2*c0*c1*c1*c2+4096*a0*a1*a1*a2*b0*b1*b1*b2*c1*c1*c1*c1-107520*a0*a1*a1*a2*b0*b1*b2*b2*c0*c0*c1*c2-14336*a0*a1*a1*a2*b0*b1*b2*b2*c0*c1*c1*c1+53248*a0*a1*a1*a2*b0*b2*b2*b2*c0*c0*c0*c2+19456*a0*a1*a1*a2*b0*b2*b2*b2*c0*c0*c1*c1-26624*a0*a1*a1*a2*b1*b1*b1*b1*c0*c0*c2*c2+13312*a0*a1*a1*a2*b1*b1*b1*b1*c0*c1*c1*c2-17408*a0*a1*a1*a2*b1*b1*b1*b2*c0*c0*c1*c2-8192*a0*a1*a1*a2*b1*b1*b1*b2*c0*c1*c1*c1+77824*a0*a1*a1*a2*b1*b1*b2*b2*c0*c0*c0*c2+19968*a0*a1*a1*a2*b1*b1*b2*b2*c0*c0*c1*c1-60416*a0*a1*a1*a2*b1*b2*b2*b2*c0*c0*c0*c1+36864*a0*a1*a1*a2*b2*b2*b2*b2*c0*c0*c0*c0-6144*a0*a1*a1*b0*b0*b0*b0*b2*b2*c2*c2*c2-11776*a0*a1*a1*b0*b0*b0*b1*b1*b2*c2*c2*c2+19456*a0*a1*a1*b0*b0*b0*b1*b2*b2*c1*c2*c2-14336*a0*a1*a1*b0*b0*b0*b2*b2*b2*c0*c2*c2-4096*a0*a1*a1*b0*b0*b0*b2*b2*b2*c1*c1*c2+256*a0*a1*a1*b0*b0*b1*b1*b1*b1*c2*c2*c2+14592*a0*a1*a1*b0*b0*b1*b1*b1*b2*c1*c2*c2+19968*a0*a1*a1*b0*b0*b1*b1*b2*b2*c0*c2*c2-27648*a0*a1*a1*b0*b0*b1*b1*b2*b2*c1*c1*c2-14336*a0*a1*a1*b0*b0*b1*b2*b2*b2*c0*c1*c2+16384*a0*a1*a1*b0*b0*b1*b2*b2*b2*c1*c1*c1+38912*a0*a1*a1*b0*b0*b2*b2*b2*b2*c0*c0*c2-20480*a0*a1*a1*b0*b0*b2*b2*b2*b2*c0*c1*c1-256*a0*a1*a1*b0*b1*b1*b1*b1*b1*c1*c2*c2-14336*a0*a1*a1*b0*b1*b1*b1*b1*b2*c0*c2*c2-2048*a0*a1*a1*b0*b1*b1*b1*b1*b2*c1*c1*c2+30208*a0*a1*a1*b0*b1*b1*b1*b2*b2*c0*c1*c2+2048*a0*a1*a1*b0*b1*b1*b1*b2*b2*c1*c1*c1-12800*a0*a1*a1*b0*b1*b1*b2*b2*b2*c0*c0*c2-21504*a0*a1*a1*b0*b1*b1*b2*b2*b2*c0*c1*c1+31744*a0*a1*a1*b0*b1*b2*b2*b2*b2*c0*c0*c1-18432*a0*a1*a1*b0*b2*b2*b2*b2*b2*c0*c0*c0+256*a0*a1*a1*b1*b1*b1*b1*b1*b1*c0*c2*c2+2560*a0*a1*a1*b1*b1*b1*b1*b1*b2*c0*c1*c2-8448*a0*a1*a1*b1*b1*b1*b1*b2*b2*c0*c0*c2-2560*a0*a1*a1*b1*b1*b1*b1*b2*b2*c0*c1*c1+10496*a0*a1*a1*b1*b1*b1*b2*b2*b2*c0*c0*c1-7680*a0*a1*a1*b1*b1*b2*b2*b2*b2*c0*c0*c0-131072*a0*a1*a2*a2*a2*a2*c0*c0*c0*c0*c1*c2+32768*a0*a1*a2*a2*a2*a2*c0*c0*c0*c1*c1*c1+106496*a0*a1*a2*a2*a2*b0*b0*c0*c0*c1*c2*c2+53248*a0*a1*a2*a2*a2*b0*b0*c0*c1*c1*c1*c2-18432*a0*a1*a2*a2*a2*b0*b0*c1*c1*c1*c1*c1-376832*a0*a1*a2*a2*a2*b0*b1*c0*c0*c0*c2*c2+53248*a0*a1*a2*a2*a2*b0*b1*c0*c0*c1*c1*c2+4096*a0*a1*a2*a2*a2*b0*b1*c0*c1*c1*c1*c1+32768*a0*a1*a2*a2*a2*b0*b2*c0*c0*c0*c1*c2+4096*a0*a1*a2*a2*a2*b0*b2*c0*c0*c1*c1*c1+16384*a0*a1*a2*a2*a2*b1*b1*c0*c0*c0*c1*c2+2048*a0*a1*a2*a2*a2*b1*b1*c0*c0*c1*c1*c1+180224*a0*a1*a2*a2*a2*b1*b2*c0*c0*c0*c0*c2-69632*a0*a1*a2*a2*a2*b1*b2*c0*c0*c0*c1*c1+24576*a0*a1*a2*a2*a2*b2*b2*c0*c0*c0*c0*c1-40960*a0*a1*a2*a2*b0*b0*b0*b0*c1*c2*c2*c2-131072*a0*a1*a2*a2*b0*b0*b0*b1*c0*c2*c2*c2+80896*a0*a1*a2*a2*b0*b0*b0*b1*c1*c1*c2*c2+188416*a0*a1*a2*a2*b0*b0*b0*b2*c0*c1*c2*c2-66560*a0*a1*a2*a2*b0*b0*b0*b2*c1*c1*c1*c2-12288*a0*a1*a2*a2*b0*b0*b1*b1*c0*c1*c2*c2-12800*a0*a1*a2*a2*b0*b0*b1*b1*c1*c1*c1*c2+86016*a0*a1*a2*a2*b0*b0*b1*b2*c0*c0*c2*c2-107520*a0*a1*a2*a2*b0*b0*b1*b2*c0*c1*c1*c2+31744*a0*a1*a2*a2*b0*b0*b1*b2*c1*c1*c1*c1-110592*a0*a1*a2*a2*b0*b0*b2*b2*c0*c0*c1*c2+19456*a0*a1*a2*a2*b0*b0*b2*b2*c0*c1*c1*c1+40960*a0*a1*a2*a2*b0*b1*b1*b1*c0*c0*c2*c2-17408*a0*a1*a2*a2*b0*b1*b1*b1*c0*c1*c1*c2+2048*a0*a1*a2*a2*b0*b1*b1*b1*c1*c1*c1*c1+110592*a0*a1*a2*a2*b0*b1*b1*b2*c0*c0*c1*c2-20480*a0*a1*a2*a2*b0*b1*b1*b2*c0*c1*c1*c1+53248*a0*a1*a2*a2*b0*b1*b2*b2*c0*c0*c0*c2-30720*a0*a1*a2*a2*b0*b1*b2*b2*c0*c0*c1*c1+4096*a0*a1*a2*a2*b0*b2*b2*b2*c0*c0*c0*c1+16384*a0*a1*a2*a2*b1*b1*b1*b1*c0*c0*c1*c2-2560*a0*a1*a2*a2*b1*b1*b1*b1*c0*c1*c1*c1-94208*a0*a1*a2*a2*b1*b1*b1*b2*c0*c0*c0*c2+7168*a0*a1*a2*a2*b1*b1*b1*b2*c0*c0*c1*c1+47104*a0*a1*a2*a2*b1*b1*b2*b2*c0*c0*c0*c1-40960*a0*a1*a2*a2*b1*b2*b2*b2*c0*c0*c0*c0+4096*a0*a1*a2*b0*b0*b0*b0*b1*b2*c2*c2*c2+16384*a0*a1*a2*b0*b0*b0*b0*b2*b2*c1*c2*c2+11264*a0*a1*a2*b0*b0*b0*b1*b1*b1*c2*c2*c2-20480*a0*a1*a2*b0*b0*b0*b1*b1*b2*c1*c2*c2+4096*a0*a1*a2*b0*b0*b0*b1*b2*b2*c0*c2*c2-14336*a0*a1*a2*b0*b0*b0*b1*b2*b2*c1*c1*c2-49152*a0*a1*a2*b0*b0*b0*b2*b2*b2*c0*c1*c2+20480*a0*a1*a2*b0*b0*b0*b2*b2*b2*c1*c1*c1-14336*a0*a1*a2*b0*b0*b1*b1*b1*b1*c1*c2*c2-17408*a0*a1*a2*b0*b0*b1*b1*b1*b2*c0*c2*c2+30208*a0*a1*a2*b0*b0*b1*b1*b1*b2*c1*c1*c2+61440*a0*a1*a2*b0*b0*b1*b1*b2*b2*c0*c1*c2-21504*a0*a1*a2*b0*b0*b1*b1*b2*b2*c1*c1*c1+4096*a0*a1*a2*b0*b0*b1*b2*b2*b2*c0*c0*c2-14336*a0*a1*a2*b0*b0*b1*b2*b2*b2*c0*c1*c1+16384*a0*a1*a2*b0*b0*b2*b2*b2*b2*c0*c0*c1+13312*a0*a1*a2*b0*b1*b1*b1*b1*b1*c0*c2*c2+2560*a0*a1*a2*b0*b1*b1*b1*b1*b1*c1*c1*c2-36864*a0*a1*a2*b0*b1*b1*b1*b1*b2*c0*c1*c2-2048*a0*a1*a2*b0*b1*b1*b1*b1*b2*c1*c1*c1-17408*a0*a1*a2*b0*b1*b1*b1*b2*b2*c0*c0*c2+30208*a0*a1*a2*b0*b1*b1*b1*b2*b2*c0*c1*c1-20480*a0*a1*a2*b0*b1*b1*b2*b2*b2*c0*c0*c1+4096*a0*a1*a2*b0*b1*b2*b2*b2*b2*c0*c0*c0-3072*a0*a1*a2*b1*b1*b1*b1*b1*b1*c0*c1*c2+13312*a0*a1*a2*b1*b1*b1*b1*b1*b2*c0*c0*c2+2560*a0*a1*a2*b1*b1*b1*b1*b1*b2*c0*c1*c1-14336*a0*a1*a2*b1*b1*b1*b1*b2*b2*c0*c0*c1+11264*a0*a1*a2*b1*b1*b1*b2*b2*b2*c0*c0*c0-4096*a0*a1*b0*b0*b0*b0*b1*b2*b2*b2*c2*c2+2048*a0*a1*b0*b0*b0*b1*b1*b1*b2*b2*c2*c2+4096*a0*a1*b0*b0*b0*b1*b1*b2*b2*b2*c1*c2+8192*a0*a1*b0*b0*b0*b1*b2*b2*b2*b2*c0*c2-4096*a0*a1*b0*b0*b0*b1*b2*b2*b2*b2*c1*c1-256*a0*a1*b0*b0*b1*b1*b1*b1*b1*b2*c2*c2-2048*a0*a1*b0*b0*b1*b1*b1*b1*b2*b2*c1*c2-8192*a0*a1*b0*b0*b1*b1*b1*b2*b2*b2*c0*c2+2048*a0*a1*b0*b0*b1*b1*b1*b2*b2*b2*c1*c1+4096*a0*a1*b0*b0*b1*b1*b2*b2*b2*b2*c0*c1-4096*a0*a1*b0*b0*b1*b2*b2*b2*b2*b2*c0*c0+256*a0*a1*b0*b1*b1*b1*b1*b1*b1*b2*c1*c2+2560*a0*a1*b0*b1*b1*b1*b1*b1*b2*b2*c0*c2-256*a0*a1*b0*b1*b1*b1*b1*b1*b2*b2*c1*c1-2048*a0*a1*b0*b1*b1*b1*b1*b2*b2*b2*c0*c1+2048*a0*a1*b0*b1*b1*b1*b2*b2*b2*b2*c0*c0-256*a0*a1*b1*b1*b1*b1*b1*b1*b1*b2*c0*c2+256*a0*a1*b1*b1*b1*b1*b1*b1*b2*b2*c0*c1-256*a0*a1*b1*b1*b1*b1*b1*b2*b2*b2*c0*c0+65536*a0*a2*a2*a2*a2*a2*c0*c0*c0*c0*c0*c2-16384*a0*a2*a2*a2*a2*a2*c0*c0*c0*c0*c1*c1+196608*a0*a2*a2*a2*a2*b0*b0*c0*c0*c0*c2*c2-200704*a0*a2*a2*a2*a2*b0*b0*c0*c0*c1*c1*c2+36864*a0*a2*a2*a2*a2*b0*b0*c0*c1*c1*c1*c1+180224*a0*a2*a2*a2*a2*b0*b1*c0*c0*c0*c1*c2-40960*a0*a2*a2*a2*a2*b0*b1*c0*c0*c1*c1*c1-131072*a0*a2*a2*a2*a2*b0*b2*c0*c0*c0*c0*c2+24576*a0*a2*a2*a2*a2*b0*b2*c0*c0*c0*c1*c1-65536*a0*a2*a2*a2*a2*b1*b1*c0*c0*c0*c0*c2+12288*a0*a2*a2*a2*a2*b1*b1*c0*c0*c0*c1*c1+16384*a0*a2*a2*a2*a2*b1*b2*c0*c0*c0*c0*c1-16384*a0*a2*a2*a2*a2*b2*b2*c0*c0*c0*c0*c0+131072*a0*a2*a2*a2*b0*b0*b0*b0*c0*c2*c2*c2-12288*a0*a2*a2*a2*b0*b0*b0*b0*c1*c1*c2*c2-131072*a0*a2*a2*a2*b0*b0*b0*b1*c0*c1*c2*c2+3072*a0*a2*a2*a2*b0*b0*b0*b1*c1*c1*c1*c2-163840*a0*a2*a2*a2*b0*b0*b0*b2*c0*c0*c2*c2+53248*a0*a2*a2*a2*b0*b0*b0*b2*c0*c1*c1*c2+9216*a0*a2*a2*a2*b0*b0*b0*b2*c1*c1*c1*c1+53248*a0*a2*a2*a2*b0*b0*b1*b1*c0*c0*c2*c2+77824*a0*a2*a2*a2*b0*b0*b1*b1*c0*c1*c1*c2-7680*a0*a2*a2*a2*b0*b0*b1*b1*c1*c1*c1*c1+53248*a0*a2*a2*a2*b0*b0*b1*b2*c0*c0*c1*c2-60416*a0*a2*a2*a2*b0*b0*b1*b2*c0*c1*c1*c1-16384*a0*a2*a2*a2*b0*b0*b2*b2*c0*c0*c0*c2+40960*a0*a2*a2*a2*b0*b0*b2*b2*c0*c0*c1*c1-94208*a0*a2*a2*a2*b0*b1*b1*b1*c0*c0*c1*c2+11264*a0*a2*a2*a2*b0*b1*b1*b1*c0*c1*c1*c1+16384*a0*a2*a2*a2*b0*b1*b1*b2*c0*c0*c0*c2+47104*a0*a2*a2*a2*b0*b1*b1*b2*c0*c0*c1*c1-69632*a0*a2*a2*a2*b0*b1*b2*b2*c0*c0*c0*c1+32768*a0*a2*a2*a2*b0*b2*b2*b2*c0*c0*c0*c0+24576*a0*a2*a2*a2*b1*b1*b1*b1*c0*c0*c0*c2-3072*a0*a2*a2*a2*b1*b1*b1*b1*c0*c0*c1*c1-12288*a0*a2*a2*a2*b1*b1*b1*b2*c0*c0*c0*c1+12288*a0*a2*a2*a2*b1*b1*b2*b2*c0*c0*c0*c0+32768*a0*a2*a2*b0*b0*b0*b0*b0*b2*c2*c2*c2-20480*a0*a2*a2*b0*b0*b0*b0*b1*b1*c2*c2*c2-45056*a0*a2*a2*b0*b0*b0*b0*b1*b2*c1*c2*c2-98304*a0*a2*a2*b0*b0*b0*b0*b2*b2*c0*c2*c2+38912*a0*a2*a2*b0*b0*b0*b0*b2*b2*c1*c1*c2+29696*a0*a2*a2*b0*b0*b0*b1*b1*b1*c1*c2*c2+94208*a0*a2*a2*b0*b0*b0*b1*b1*b2*c0*c2*c2-12800*a0*a2*a2*b0*b0*b0*b1*b1*b2*c1*c1*c2+4096*a0*a2*a2*b0*b0*b0*b1*b2*b2*c0*c1*c2-13312*a0*a2*a2*b0*b0*b0*b1*b2*b2*c1*c1*c1+73728*a0*a2*a2*b0*b0*b0*b2*b2*b2*c0*c0*c2-14336*a0*a2*a2*b0*b0*b0*b2*b2*b2*c0*c1*c1-26624*a0*a2*a2*b0*b0*b1*b1*b1*b1*c0*c2*c2-8448*a0*a2*a2*b0*b0*b1*b1*b1*b1*c1*c1*c2-17408*a0*a2*a2*b0*b0*b1*b1*b1*b2*c0*c1*c2+10496*a0*a2*a2*b0*b0*b1*b1*b1*b2*c1*c1*c1-55296*a0*a2*a2*b0*b0*b1*b1*b2*b2*c0*c0*c2+19968*a0*a2*a2*b0*b0*b1*b1*b2*b2*c0*c1*c1-4096*a0*a2*a2*b0*b0*b1*b2*b2*b2*c0*c0*c1-8192*a0*a2*a2*b0*b0*b2*b2*b2*b2*c0*c0*c0+13312*a0*a2*a2*b0*b1*b1*b1*b1*b1*c0*c1*c2-256*a0*a2*a2*b0*b1*b1*b1*b1*b1*c1*c1*c1+16384*a0*a2*a2*b0*b1*b1*b1*b1*b2*c0*c0*c2-14336*a0*a2*a2*b0*b1*b1*b1*b1*b2*c0*c1*c1+7168*a0*a2*a2*b0*b1*b1*b1*b2*b2*c0*c0*c1+2048*a0*a2*a2*b0*b1*b1*b2*b2*b2*c0*c0*c0-4096*a0*a2*a2*b1*b1*b1*b1*b1*b1*c0*c0*c2+256*a0*a2*a2*b1*b1*b1*b1*b1*b1*c0*c1*c1+3072*a0*a2*a2*b1*b1*b1*b1*b1*b2*c0*c0*c1-3072*a0*a2*a2*b1*b1*b1*b1*b2*b2*c0*c0*c0-8192*a0*a2*b0*b0*b0*b0*b0*b2*b2*b2*c2*c2+8192*a0*a2*b0*b0*b0*b0*b1*b1*b2*b2*c2*c2+8192*a0*a2*b0*b0*b0*b0*b1*b2*b2*b2*c1*c2+16384*a0*a2*b0*b0*b0*b0*b2*b2*b2*b2*c0*c2-8192*a0*a2*b0*b0*b0*b0*b2*b2*b2*b2*c1*c1-2560*a0*a2*b0*b0*b0*b1*b1*b1*b1*b2*c2*c2-8192*a0*a2*b0*b0*b0*b1*b1*b1*b2*b2*c1*c2-24576*a0*a2*b0*b0*b0*b1*b1*b2*b2*b2*c0*c2+8192*a0*a2*b0*b0*b0*b1*b1*b2*b2*b2*c1*c1+8192*a0*a2*b0*b0*b0*b1*b2*b2*b2*b2*c0*c1-8192*a0*a2*b0*b0*b0*b2*b2*b2*b2*b2*c0*c0+256*a0*a2*b0*b0*b1*b1*b1*b1*b1*b1*c2*c2+2560*a0*a2*b0*b0*b1*b1*b1*b1*b1*b2*c1*c2+13312*a0*a2*b0*b0*b1*b1*b1*b1*b2*b2*c0*c2-2560*a0*a2*b0*b0*b1*b1*b1*b1*b2*b2*c1*c1-8192*a0*a2*b0*b0*b1*b1*b1*b2*b2*b2*c0*c1+8192*a0*a2*b0*b0*b1*b1*b2*b2*b2*b2*c0*c0-256*a0*a2*b0*b1*b1*b1*b1*b1*b1*b1*c1*c2-3072*a0*a2*b0*b1*b1*b1*b1*b1*b1*b2*c0*c2+256*a0*a2*b0*b1*b1*b1*b1*b1*b1*b2*c1*c1+2560*a0*a2*b0*b1*b1*b1*b1*b1*b2*b2*c0*c1-2560*a0*a2*b0*b1*b1*b1*b1*b2*b2*b2*c0*c0+256*a0*a2*b1*b1*b1*b1*b1*b1*b1*b1*c0*c2-256*a0*a2*b1*b1*b1*b1*b1*b1*b1*b2*c0*c1+256*a0*a2*b1*b1*b1*b1*b1*b1*b2*b2*c0*c0-16384*a1*a1*a1*a1*a1*a1*c0*c0*c0*c2*c2*c2+4096*a1*a1*a1*a1*a1*a1*c0*c0*c1*c1*c2*c2+32768*a1*a1*a1*a1*a1*a2*c0*c0*c0*c1*c2*c2-8192*a1*a1*a1*a1*a1*a2*c0*c0*c1*c1*c1*c2-18432*a1*a1*a1*a1*a1*b0*b0*c0*c1*c2*c2*c2+4096*a1*a1*a1*a1*a1*b0*b0*c1*c1*c1*c2*c2+24576*a1*a1*a1*a1*a1*b0*b1*c0*c0*c2*c2*c2-4096*a1*a1*a1*a1*a1*b0*b1*c0*c1*c1*c2*c2-4096*a1*a1*a1*a1*a1*b0*b2*c0*c0*c1*c2*c2-2048*a1*a1*a1*a1*a1*b1*b1*c0*c0*c1*c2*c2+24576*a1*a1*a1*a1*a1*b1*b2*c0*c0*c0*c2*c2-4096*a1*a1*a1*a1*a1*b1*b2*c0*c0*c1*c1*c2-18432*a1*a1*a1*a1*a1*b2*b2*c0*c0*c0*c1*c2+4096*a1*a1*a1*a1*a1*b2*b2*c0*c0*c1*c1*c1-32768*a1*a1*a1*a1*a2*a2*c0*c0*c0*c0*c2*c2-8192*a1*a1*a1*a1*a2*a2*c0*c0*c0*c1*c1*c2+4096*a1*a1*a1*a1*a2*a2*c0*c0*c1*c1*c1*c1-12288*a1*a1*a1*a1*a2*b0*b0*c0*c0*c2*c2*c2+38912*a1*a1*a1*a1*a2*b0*b0*c0*c1*c1*c2*c2-8192*a1*a1*a1*a1*a2*b0*b0*c1*c1*c1*c1*c2-45056*a1*a1*a1*a1*a2*b0*b1*c0*c0*c1*c2*c2+8192*a1*a1*a1*a1*a2*b0*b1*c0*c1*c1*c1*c2-40960*a1*a1*a1*a1*a2*b0*b2*c0*c0*c0*c2*c2+16384*a1*a1*a1*a1*a2*b0*b2*c0*c0*c1*c1*c2-20480*a1*a1*a1*a1*a2*b1*b1*c0*c0*c0*c2*c2+8192*a1*a1*a1*a1*a2*b1*b1*c0*c0*c1*c1*c2+4096*a1*a1*a1*a1*a2*b1*b2*c0*c0*c0*c1*c2-4096*a1*a1*a1*a1*a2*b1*b2*c0*c0*c1*c1*c1+36864*a1*a1*a1*a1*a2*b2*b2*c0*c0*c0*c0*c2-6144*a1*a1*a1*a1*a2*b2*b2*c0*c0*c0*c1*c1-6912*a1*a1*a1*a1*b0*b0*b0*b0*c2*c2*c2*c2+9216*a1*a1*a1*a1*b0*b0*b0*b1*c1*c2*c2*c2+9216*a1*a1*a1*a1*b0*b0*b0*b2*c0*c2*c2*c2-6144*a1*a1*a1*a1*b0*b0*b0*b2*c1*c1*c2*c2-7680*a1*a1*a1*a1*b0*b0*b1*b1*c0*c2*c2*c2-2048*a1*a1*a1*a1*b0*b0*b1*b1*c1*c1*c2*c2+31744*a1*a1*a1*a1*b0*b0*b1*b2*c0*c1*c2*c2-4096*a1*a1*a1*a1*b0*b0*b1*b2*c1*c1*c1*c2-512*a1*a1*a1*a1*b0*b0*b2*b2*c0*c0*c2*c2-20480*a1*a1*a1*a1*b0*b0*b2*b2*c0*c1*c1*c2+4096*a1*a1*a1*a1*b0*b0*b2*b2*c1*c1*c1*c1+2048*a1*a1*a1*a1*b0*b1*b1*b1*c0*c1*c2*c2-35840*a1*a1*a1*a1*b0*b1*b1*b2*c0*c0*c2*c2+4096*a1*a1*a1*a1*b0*b1*b1*b2*c0*c1*c1*c2+31744*a1*a1*a1*a1*b0*b1*b2*b2*c0*c0*c1*c2-4096*a1*a1*a1*a1*b0*b1*b2*b2*c0*c1*c1*c1+9216*a1*a1*a1*a1*b0*b2*b2*b2*c0*c0*c0*c2-6144*a1*a1*a1*a1*b0*b2*b2*b2*c0*c0*c1*c1+256*a1*a1*a1*a1*b1*b1*b1*b1*c0*c0*c2*c2+2048*a1*a1*a1*a1*b1*b1*b1*b2*c0*c0*c1*c2-7680*a1*a1*a1*a1*b1*b1*b2*b2*c0*c0*c0*c2-2048*a1*a1*a1*a1*b1*b1*b2*b2*c0*c0*c1*c1+9216*a1*a1*a1*a1*b1*b2*b2*b2*c0*c0*c0*c1-6912*a1*a1*a1*a1*b2*b2*b2*b2*c0*c0*c0*c0+32768*a1*a1*a1*a2*a2*a2*c0*c0*c0*c0*c1*c2-8192*a1*a1*a1*a2*a2*a2*c0*c0*c0*c1*c1*c1-14336*a1*a1*a1*a2*a2*b0*b0*c0*c0*c1*c2*c2-14336*a1*a1*a1*a2*a2*b0*b0*c0*c1*c1*c1*c2+4096*a1*a1*a1*a2*a2*b0*b0*c1*c1*c1*c1*c1+106496*a1*a1*a1*a2*a2*b0*b1*c0*c0*c0*c2*c2-4096*a1*a1*a1*a2*a2*b0*b1*c0*c0*c1*c1*c2-4096*a1*a1*a1*a2*a2*b0*b1*c0*c1*c1*c1*c1+4096*a1*a1*a1*a2*a2*b0*b2*c0*c0*c0*c1*c2-4096*a1*a1*a1*a2*a2*b0*b2*c0*c0*c1*c1*c1+2048*a1*a1*a1*a2*a2*b1*b1*c0*c0*c0*c1*c2-2048*a1*a1*a1*a2*a2*b1*b1*c0*c0*c1*c1*c1-40960*a1*a1*a1*a2*a2*b1*b2*c0*c0*c0*c0*c2+16384*a1*a1*a1*a2*a2*b1*b2*c0*c0*c0*c1*c1-6144*a1*a1*a1*a2*a2*b2*b2*c0*c0*c0*c0*c1+9216*a1*a1*a1*a2*b0*b0*b0*b0*c1*c2*c2*c2+3072*a1*a1*a1*a2*b0*b0*b0*b1*c0*c2*c2*c2-13312*a1*a1*a1*a2*b0*b0*b0*b1*c1*c1*c2*c2-66560*a1*a1*a1*a2*b0*b0*b0*b2*c0*c1*c2*c2+20480*a1*a1*a1*a2*b0*b0*b0*b2*c1*c1*c1*c2-12800*a1*a1*a1*a2*b0*b0*b1*b1*c0*c1*c2*c2+8192*a1*a1*a1*a2*b0*b0*b1*b1*c1*c1*c1*c2+80896*a1*a1*a1*a2*b0*b0*b1*b2*c0*c0*c2*c2-14336*a1*a1*a1*a2*b0*b0*b1*b2*c0*c1*c1*c2-4096*a1*a1*a1*a2*b0*b0*b1*b2*c1*c1*c1*c1+19456*a1*a1*a1*a2*b0*b0*b2*b2*c0*c0*c1*c2-4096*a1*a1*a1*a2*b0*b0*b2*b2*c0*c1*c1*c1+29696*a1*a1*a1*a2*b0*b1*b1*b1*c0*c0*c2*c2-8192*a1*a1*a1*a2*b0*b1*b1*b1*c0*c1*c1*c2-20480*a1*a1*a1*a2*b0*b1*b1*b2*c0*c0*c1*c2+4096*a1*a1*a1*a2*b0*b1*b1*b2*c0*c1*c1*c1-60416*a1*a1*a1*a2*b0*b1*b2*b2*c0*c0*c0*c2+19456*a1*a1*a1*a2*b0*b1*b2*b2*c0*c0*c1*c1-3072*a1*a1*a1*a2*b0*b2*b2*b2*c0*c0*c0*c1-2560*a1*a1*a1*a2*b1*b1*b1*b1*c0*c0*c1*c2+11264*a1*a1*a1*a2*b1*b1*b1*b2*c0*c0*c0*c2+2048*a1*a1*a1*a2*b1*b1*b1*b2*c0*c0*c1*c1-11776*a1*a1*a1*a2*b1*b1*b2*b2*c0*c0*c0*c1+9216*a1*a1*a1*a2*b1*b2*b2*b2*c0*c0*c0*c0+9216*a1*a1*a1*b0*b0*b0*b0*b1*b2*c2*c2*c2-6144*a1*a1*a1*b0*b0*b0*b0*b2*b2*c1*c2*c2-256*a1*a1*a1*b0*b0*b0*b1*b1*b1*c2*c2*c2-11776*a1*a1*a1*b0*b0*b0*b1*b1*b2*c1*c2*c2-13312*a1*a1*a1*b0*b0*b0*b1*b2*b2*c0*c2*c2+16384*a1*a1*a1*b0*b0*b0*b1*b2*b2*c1*c1*c2+20480*a1*a1*a1*b0*b0*b0*b2*b2*b2*c0*c1*c2-8192*a1*a1*a1*b0*b0*b0*b2*b2*b2*c1*c1*c1+256*a1*a1*a1*b0*b0*b1*b1*b1*b1*c1*c2*c2+10496*a1*a1*a1*b0*b0*b1*b1*b1*b2*c0*c2*c2+2048*a1*a1*a1*b0*b0*b1*b1*b1*b2*c1*c1*c2-21504*a1*a1*a1*b0*b0*b1*b1*b2*b2*c0*c1*c2-2048*a1*a1*a1*b0*b0*b1*b1*b2*b2*c1*c1*c1-13312*a1*a1*a1*b0*b0*b1*b2*b2*b2*c0*c0*c2+16384*a1*a1*a1*b0*b0*b1*b2*b2*b2*c0*c1*c1-6144*a1*a1*a1*b0*b0*b2*b2*b2*b2*c0*c0*c1-256*a1*a1*a1*b0*b1*b1*b1*b1*b1*c0*c2*c2-2048*a1*a1*a1*b0*b1*b1*b1*b1*b2*c0*c1*c2+10496*a1*a1*a1*b0*b1*b1*b1*b2*b2*c0*c0*c2+2048*a1*a1*a1*b0*b1*b1*b1*b2*b2*c0*c1*c1-11776*a1*a1*a1*b0*b1*b1*b2*b2*b2*c0*c0*c1+9216*a1*a1*a1*b0*b1*b2*b2*b2*b2*c0*c0*c0-256*a1*a1*a1*b1*b1*b1*b1*b1*b2*c0*c0*c2+256*a1*a1*a1*b1*b1*b1*b1*b2*b2*c0*c0*c1-256*a1*a1*a1*b1*b1*b1*b2*b2*b2*c0*c0*c0-16384*a1*a1*a2*a2*a2*a2*c0*c0*c0*c0*c0*c2+4096*a1*a1*a2*a2*a2*a2*c0*c0*c0*c0*c1*c1-61440*a1*a1*a2*a2*a2*b0*b0*c0*c0*c0*c2*c2+40960*a1*a1*a2*a2*a2*b0*b0*c0*c0*c1*c1*c2-6144*a1*a1*a2*a2*a2*b0*b0*c0*c1*c1*c1*c1-69632*a1*a1*a2*a2*a2*b0*b1*c0*c0*c0*c1*c2+16384*a1*a1*a2*a2*a2*b0*b1*c0*c0*c1*c1*c1+24576*a1*a1*a2*a2*a2*b0*b2*c0*c0*c0*c0*c2-4096*a1*a1*a2*a2*a2*b0*b2*c0*c0*c0*c1*c1+12288*a1*a1*a2*a2*a2*b1*b1*c0*c0*c0*c0*c2-2048*a1*a1*a2*a2*a2*b1*b1*c0*c0*c0*c1*c1-4096*a1*a1*a2*a2*a2*b1*b2*c0*c0*c0*c0*c1+4096*a1*a1*a2*a2*a2*b2*b2*c0*c0*c0*c0*c0-12288*a1*a1*a2*a2*b0*b0*b0*b0*c0*c2*c2*c2-512*a1*a1*a2*a2*b0*b0*b0*b0*c1*c1*c2*c2+80896*a1*a1*a2*a2*b0*b0*b0*b1*c0*c1*c2*c2-13312*a1*a1*a2*a2*b0*b0*b0*b1*c1*c1*c1*c2-14336*a1*a1*a2*a2*b0*b0*b0*b2*c0*c0*c2*c2+19456*a1*a1*a2*a2*b0*b0*b0*b2*c0*c1*c1*c2-6144*a1*a1*a2*a2*b0*b0*b0*b2*c1*c1*c1*c1-116736*a1*a1*a2*a2*b0*b0*b1*b1*c0*c0*c2*c2+19968*a1*a1*a2*a2*b0*b0*b1*b1*c0*c1*c1*c2-2048*a1*a1*a2*a2*b0*b0*b1*b1*c1*c1*c1*c1-30720*a1*a1*a2*a2*b0*b0*b1*b2*c0*c0*c1*c2+19456*a1*a1*a2*a2*b0*b0*b1*b2*c0*c1*c1*c1+40960*a1*a1*a2*a2*b0*b0*b2*b2*c0*c0*c0*c2-16896*a1*a1*a2*a2*b0*b0*b2*b2*c0*c0*c1*c1+7168*a1*a1*a2*a2*b0*b1*b1*b1*c0*c0*c1*c2+2048*a1*a1*a2*a2*b0*b1*b1*b1*c0*c1*c1*c1+47104*a1*a1*a2*a2*b0*b1*b1*b2*c0*c0*c0*c2-27648*a1*a1*a2*a2*b0*b1*b1*b2*c0*c0*c1*c1+19456*a1*a1*a2*a2*b0*b1*b2*b2*c0*c0*c0*c1-6144*a1*a1*a2*a2*b0*b2*b2*b2*c0*c0*c0*c0-3072*a1*a1*a2*a2*b1*b1*b1*b1*c0*c0*c0*c2+256*a1*a1*a2*a2*b1*b1*b1*b1*c0*c0*c1*c1+2048*a1*a1*a2*a2*b1*b1*b1*b2*c0*c0*c0*c1-2048*a1*a1*a2*a2*b1*b1*b2*b2*c0*c0*c0*c0-18432*a1*a1*a2*b0*b0*b0*b0*b0*b2*c2*c2*c2-7680*a1*a1*a2*b0*b0*b0*b0*b1*b1*c2*c2*c2+31744*a1*a1*a2*b0*b0*b0*b0*b1*b2*c1*c2*c2+38912*a1*a1*a2*b0*b0*b0*b0*b2*b2*c0*c2*c2-20480*a1*a1*a2*b0*b0*b0*b0*b2*b2*c1*c1*c2+10496*a1*a1*a2*b0*b0*b0*b1*b1*b1*c1*c2*c2-12800*a1*a1*a2*b0*b0*b0*b1*b1*b2*c0*c2*c2-21504*a1*a1*a2*b0*b0*b0*b1*b1*b2*c1*c1*c2-14336*a1*a1*a2*b0*b0*b0*b1*b2*b2*c0*c1*c2+16384*a1*a1*a2*b0*b0*b0*b1*b2*b2*c1*c1*c1-14336*a1*a1*a2*b0*b0*b0*b2*b2*b2*c0*c0*c2-4096*a1*a1*a2*b0*b0*b0*b2*b2*b2*c0*c1*c1-8448*a1*a1*a2*b0*b0*b1*b1*b1*b1*c0*c2*c2-2560*a1*a1*a2*b0*b0*b1*b1*b1*b1*c1*c1*c2+30208*a1*a1*a2*b0*b0*b1*b1*b1*b2*c0*c1*c2+2048*a1*a1*a2*b0*b0*b1*b1*b1*b2*c1*c1*c1+19968*a1*a1*a2*b0*b0*b1*b1*b2*b2*c0*c0*c2-27648*a1*a1*a2*b0*b0*b1*b1*b2*b2*c0*c1*c1+19456*a1*a1*a2*b0*b0*b1*b2*b2*b2*c0*c0*c1-6144*a1*a1*a2*b0*b0*b2*b2*b2*b2*c0*c0*c0+2560*a1*a1*a2*b0*b1*b1*b1*b1*b1*c0*c1*c2-14336*a1*a1*a2*b0*b1*b1*b1*b1*b2*c0*c0*c2-2048*a1*a1*a2*b0*b1*b1*b1*b1*b2*c0*c1*c1+14592*a1*a1*a2*b0*b1*b1*b1*b2*b2*c0*c0*c1-11776*a1*a1*a2*b0*b1*b1*b2*b2*b2*c0*c0*c0+256*a1*a1*a2*b1*b1*b1*b1*b1*b1*c0*c0*c2-256*a1*a1*a2*b1*b1*b1*b1*b1*b2*c0*c0*c1+256*a1*a1*a2*b1*b1*b1*b1*b2*b2*c0*c0*c0+4096*a1*a1*b0*b0*b0*b0*b0*b2*b2*b2*c2*c2-2048*a1*a1*b0*b0*b0*b0*b1*b1*b2*b2*c2*c2-4096*a1*a1*b0*b0*b0*b0*b1*b2*b2*b2*c1*c2-8192*a1*a1*b0*b0*b0*b0*b2*b2*b2*b2*c0*c2+4096*a1*a1*b0*b0*b0*b0*b2*b2*b2*b2*c1*c1+256*a1*a1*b0*b0*b0*b1*b1*b1*b1*b2*c2*c2+2048*a1*a1*b0*b0*b0*b1*b1*b1*b2*b2*c1*c2+8192*a1*a1*b0*b0*b0*b1*b1*b2*b2*b2*c0*c2-2048*a1*a1*b0*b0*b0*b1*b1*b2*b2*b2*c1*c1-4096*a1*a1*b0*b0*b0*b1*b2*b2*b2*b2*c0*c1+4096*a1*a1*b0*b0*b0*b2*b2*b2*b2*b2*c0*c0-256*a1*a1*b0*b0*b1*b1*b1*b1*b1*b2*c1*c2-2560*a1*a1*b0*b0*b1*b1*b1*b1*b2*b2*c0*c2+256*a1*a1*b0*b0*b1*b1*b1*b1*b2*b2*c1*c1+2048*a1*a1*b0*b0*b1*b1*b1*b2*b2*b2*c0*c1-2048*a1*a1*b0*b0*b1*b1*b2*b2*b2*b2*c0*c0+256*a1*a1*b0*b1*b1*b1*b1*b1*b1*b2*c0*c2-256*a1*a1*b0*b1*b1*b1*b1*b1*b2*b2*c0*c1+256*a1*a1*b0*b1*b1*b1*b1*b2*b2*b2*c0*c0+24576*a1*a2*a2*a2*a2*b0*b0*c0*c0*c0*c1*c2-6144*a1*a2*a2*a2*a2*b0*b0*c0*c0*c1*c1*c1+16384*a1*a2*a2*a2*a2*b0*b1*c0*c0*c0*c0*c2-4096*a1*a2*a2*a2*a2*b0*b1*c0*c0*c0*c1*c1-40960*a1*a2*a2*a2*b0*b0*b0*b0*c0*c1*c2*c2+9216*a1*a2*a2*a2*b0*b0*b0*b0*c1*c1*c1*c2+106496*a1*a2*a2*a2*b0*b0*b0*b1*c0*c0*c2*c2-60416*a1*a2*a2*a2*b0*b0*b0*b1*c0*c1*c1*c2+9216*a1*a2*a2*a2*b0*b0*b0*b1*c1*c1*c1*c1+4096*a1*a2*a2*a2*b0*b0*b0*b2*c0*c0*c1*c2-3072*a1*a2*a2*a2*b0*b0*b0*b2*c0*c1*c1*c1+47104*a1*a2*a2*a2*b0*b0*b1*b1*c0*c0*c1*c2-11776*a1*a2*a2*a2*b0*b0*b1*b1*c0*c1*c1*c1-69632*a1*a2*a2*a2*b0*b0*b1*b2*c0*c0*c0*c2+19456*a1*a2*a2*a2*b0*b0*b1*b2*c0*c0*c1*c1-4096*a1*a2*a2*a2*b0*b0*b2*b2*c0*c0*c0*c1-12288*a1*a2*a2*a2*b0*b1*b1*b1*c0*c0*c0*c2+2048*a1*a2*a2*a2*b0*b1*b1*b1*c0*c0*c1*c1+4096*a1*a2*a2*a2*b0*b1*b1*b2*c0*c0*c0*c1-4096*a1*a2*a2*a2*b0*b1*b2*b2*c0*c0*c0*c0+24576*a1*a2*a2*b0*b0*b0*b0*b0*b1*c2*c2*c2-4096*a1*a2*a2*b0*b0*b0*b0*b0*b2*c1*c2*c2-35840*a1*a2*a2*b0*b0*b0*b0*b1*b1*c1*c2*c2-45056*a1*a2*a2*b0*b0*b0*b0*b1*b2*c0*c2*c2+31744*a1*a2*a2*b0*b0*b0*b0*b1*b2*c1*c1*c2+16384*a1*a2*a2*b0*b0*b0*b0*b2*b2*c0*c1*c2-6144*a1*a2*a2*b0*b0*b0*b0*b2*b2*c1*c1*c1+29696*a1*a2*a2*b0*b0*b0*b1*b1*b1*c0*c2*c2+10496*a1*a2*a2*b0*b0*b0*b1*b1*b1*c1*c1*c2-20480*a1*a2*a2*b0*b0*b0*b1*b1*b2*c0*c1*c2-11776*a1*a2*a2*b0*b0*b0*b1*b1*b2*c1*c1*c1-4096*a1*a2*a2*b0*b0*b0*b1*b2*b2*c0*c0*c2+19456*a1*a2*a2*b0*b0*b0*b1*b2*b2*c0*c1*c1-4096*a1*a2*a2*b0*b0*b0*b2*b2*b2*c0*c0*c1-14336*a1*a2*a2*b0*b0*b1*b1*b1*b1*c0*c1*c2+256*a1*a2*a2*b0*b0*b1*b1*b1*b1*c1*c1*c1+7168*a1*a2*a2*b0*b0*b1*b1*b1*b2*c0*c0*c2+14592*a1*a2*a2*b0*b0*b1*b1*b1*b2*c0*c1*c1-27648*a1*a2*a2*b0*b0*b1*b1*b2*b2*c0*c0*c1+16384*a1*a2*a2*b0*b0*b1*b2*b2*b2*c0*c0*c0+3072*a1*a2*a2*b0*b1*b1*b1*b1*b1*c0*c0*c2-256*a1*a2*a2*b0*b1*b1*b1*b1*b1*c0*c1*c1-2048*a1*a2*a2*b0*b1*b1*b1*b1*b2*c0*c0*c1+2048*a1*a2*a2*b0*b1*b1*b1*b2*b2*c0*c0*c0-4096*a1*a2*b0*b0*b0*b0*b0*b1*b2*b2*c2*c2+2048*a1*a2*b0*b0*b0*b0*b1*b1*b1*b2*c2*c2+4096*a1*a2*b0*b0*b0*b0*b1*b1*b2*b2*c1*c2+8192*a1*a2*b0*b0*b0*b0*b1*b2*b2*b2*c0*c2-4096*a1*a2*b0*b0*b0*b0*b1*b2*b2*b2*c1*c1-256*a1*a2*b0*b0*b0*b1*b1*b1*b1*b1*c2*c2-2048*a1*a2*b0*b0*b0*b1*b1*b1*b1*b2*c1*c2-8192*a1*a2*b0*b0*b0*b1*b1*b1*b2*b2*c0*c2+2048*a1*a2*b0*b0*b0*b1*b1*b1*b2*b2*c1*c1+4096*a1*a2*b0*b0*b0*b1*b1*b2*b2*b2*c0*c1-4096*a1*a2*b0*b0*b0*b1*b2*b2*b2*b2*c0*c0+256*a1*a2*b0*b0*b1*b1*b1*b1*b1*b1*c1*c2+2560*a1*a2*b0*b0*b1*b1*b1*b1*b1*b2*c0*c2-256*a1*a2*b0*b0*b1*b1*b1*b1*b1*b2*c1*c1-2048*a1*a2*b0*b0*b1*b1*b1*b1*b2*b2*c0*c1+2048*a1*a2*b0*b0*b1*b1*b1*b2*b2*b2*c0*c0-256*a1*a2*b0*b1*b1*b1*b1*b1*b1*b1*c0*c2+256*a1*a2*b0*b1*b1*b1*b1*b1*b1*b2*c0*c1-256*a1*a2*b0*b1*b1*b1*b1*b1*b2*b2*c0*c0-16384*a2*a2*a2*a2*a2*b0*b0*c0*c0*c0*c0*c2+4096*a2*a2*a2*a2*a2*b0*b0*c0*c0*c0*c1*c1-32768*a2*a2*a2*a2*b0*b0*b0*b0*c0*c0*c2*c2+36864*a2*a2*a2*a2*b0*b0*b0*b0*c0*c1*c1*c2-6912*a2*a2*a2*a2*b0*b0*b0*b0*c1*c1*c1*c1-40960*a2*a2*a2*a2*b0*b0*b0*b1*c0*c0*c1*c2+9216*a2*a2*a2*a2*b0*b0*b0*b1*c0*c1*c1*c1+32768*a2*a2*a2*a2*b0*b0*b0*b2*c0*c0*c0*c2-6144*a2*a2*a2*a2*b0*b0*b0*b2*c0*c0*c1*c1+12288*a2*a2*a2*a2*b0*b0*b1*b1*c0*c0*c0*c2-2048*a2*a2*a2*a2*b0*b0*b1*b1*c0*c0*c1*c1-4096*a2*a2*a2*a2*b0*b0*b1*b2*c0*c0*c0*c1+4096*a2*a2*a2*a2*b0*b0*b2*b2*c0*c0*c0*c0-16384*a2*a2*a2*b0*b0*b0*b0*b0*b0*c2*c2*c2+24576*a2*a2*a2*b0*b0*b0*b0*b0*b1*c1*c2*c2+32768*a2*a2*a2*b0*b0*b0*b0*b0*b2*c0*c2*c2-18432*a2*a2*a2*b0*b0*b0*b0*b0*b2*c1*c1*c2-20480*a2*a2*a2*b0*b0*b0*b0*b1*b1*c0*c2*c2-7680*a2*a2*a2*b0*b0*b0*b0*b1*b1*c1*c1*c2+4096*a2*a2*a2*b0*b0*b0*b0*b1*b2*c0*c1*c2+9216*a2*a2*a2*b0*b0*b0*b0*b1*b2*c1*c1*c1-8192*a2*a2*a2*b0*b0*b0*b0*b2*b2*c0*c0*c2-6144*a2*a2*a2*b0*b0*b0*b0*b2*b2*c0*c1*c1+11264*a2*a2*a2*b0*b0*b0*b1*b1*b1*c0*c1*c2-256*a2*a2*a2*b0*b0*b0*b1*b1*b1*c1*c1*c1+2048*a2*a2*a2*b0*b0*b0*b1*b1*b2*c0*c0*c2-11776*a2*a2*a2*b0*b0*b0*b1*b1*b2*c0*c1*c1+16384*a2*a2*a2*b0*b0*b0*b1*b2*b2*c0*c0*c1-8192*a2*a2*a2*b0*b0*b0*b2*b2*b2*c0*c0*c0-3072*a2*a2*a2*b0*b0*b1*b1*b1*b1*c0*c0*c2+256*a2*a2*a2*b0*b0*b1*b1*b1*b1*c0*c1*c1+2048*a2*a2*a2*b0*b0*b1*b1*b1*b2*c0*c0*c1-2048*a2*a2*a2*b0*b0*b1*b1*b2*b2*c0*c0*c0+4096*a2*a2*b0*b0*b0*b0*b0*b0*b2*b2*c2*c2-2048*a2*a2*b0*b0*b0*b0*b0*b1*b1*b2*c2*c2-4096*a2*a2*b0*b0*b0*b0*b0*b1*b2*b2*c1*c2-8192*a2*a2*b0*b0*b0*b0*b0*b2*b2*b2*c0*c2+4096*a2*a2*b0*b0*b0*b0*b0*b2*b2*b2*c1*c1+256*a2*a2*b0*b0*b0*b0*b1*b1*b1*b1*c2*c2+2048*a2*a2*b0*b0*b0*b0*b1*b1*b1*b2*c1*c2+8192*a2*a2*b0*b0*b0*b0*b1*b1*b2*b2*c0*c2-2048*a2*a2*b0*b0*b0*b0*b1*b1*b2*b2*c1*c1-4096*a2*a2*b0*b0*b0*b0*b1*b2*b2*b2*c0*c1+4096*a2*a2*b0*b0*b0*b0*b2*b2*b2*b2*c0*c0-256*a2*a2*b0*b0*b0*b1*b1*b1*b1*b1*c1*c2-2560*a2*a2*b0*b0*b0*b1*b1*b1*b1*b2*c0*c2+256*a2*a2*b0*b0*b0*b1*b1*b1*b1*b2*c1*c1+2048*a2*a2*b0*b0*b0*b1*b1*b1*b2*b2*c0*c1-2048*a2*a2*b0*b0*b0*b1*b1*b2*b2*b2*c0*c0+256*a2*a2*b0*b0*b1*b1*b1*b1*b1*b1*c0*c2-256*a2*a2*b0*b0*b1*b1*b1*b1*b1*b2*c0*c1+256*a2*a2*b0*b0*b1*b1*b1*b1*b2*b2*c0*c0;
globalSecondIdeal=ideal join(firstEquations,secondEquations,{smoothInverse*smoothDiscriminant-1});
print("MODEL_READY: 16 first equations, 25 complete second dual equations, one smooth inverse");
print("NO_ELIMINATION_RUN_BY_INPUT_FILE");
```
</details>
