# The nonendpoint quintic homogeneous-gcd-three exclusion

Work over an algebraically closed characteristic-zero field in the **admissible nonendpoint sectional-genus-one quintic A4 normalization model**, with its actual center avoidance, finite birational projection, delta≠0 and complete homogeneous gcd-three classification. Every projection in this specified h=3 lane is excluded in every positive mate degree, including zero-conormal-cubic and proportional boundary charts. This is the source-accepted scoped theorem, not a statement about all quintic carriers or an unrestricted STCI result; no new canonical promotion is made here.

The proof combines the independent geometric audit's complete zero/lambda-one/main support analysis with the subsequently completed original-six-generator certificate. An earlier unfinished 3+2 label is superseded by that literal identity, not by a saturated unit-ideal printout. The source arithmetic was not rerun during consolidation. [Nonendpoint conormal and full conductor geometry](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md) and the [complete homogeneous gcd cover](NONENDPOINT_CUBIC_PAIR_COMPLETION.md) remain upstream.

## 1. Premises and the geometric implication actually being audited

The accepted normalization model and actual center-avoidance conditions
give a finite birational projection `nu:S->X`, with `c` mapped
isomorphically to C0. A mate forces full inverse support
`nu^{-1}(C0)_red=c`. The
[accepted conductor module audit](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md)
identifies the upstairs conductor with an actual Cartier divisor in
`|2H|`, whose restriction to c is a nonzero degree-eight binary form F.
The accepted local-ring argument implies

    supp(F) subset supp(H P^epsilon),
    epsilon=1 if Jbar=0, and zero otherwise,

where H is the complete homogeneous gcd of the corrected conormal cubics,
and P=0 is the intrinsic A4 point. This is only a necessary support
condition. In particular, the first-normal multiplicity of H does not
bound the conductor multiplicity of F.

All uses below retain the binary degrees. An affine leading drop is an
actual root at infinity. No argument discards a center minor or interprets
a resultant leading factor as an extra normalization point. When a
certificate excludes a larger coefficient family than the admissible
centers, the exclusion automatically applies to its admissible subset;
that does not replace center avoidance with a new assumption.

## 2. Zero-P and zero-J: complete support exclusions

On the zero-P chart, put `j=Jbar`. The captured exact factorization is

    F=(2/9) S3 Q5,
    S3=p^3-6p^2+6p+3j,
    Q5=p^5+(j/3-13/2)p^4+(27/2)p^3
        +(-12-5j/2)p^2+(9/2-3j/2+j^2)p+9j-3j^2.

Both factors are monic, of their fixed binary degrees. Hence neither has
an infinity root, for any j. For j nonzero the support condition says
every Q5 root lies on S3. At j=0 the additional allowed A4 point is already
a root of S3, since S3(0)=0. The same condition therefore applies for
every j, without discarding the Jbar-zero value.

Support inclusion is equivalent to `Q5 | S3^5`: a Q5 root has multiplicity
at most five, whereas its multiplicity in S3^5 is at least five. The
captured division has remainder degree below five and its five original
coefficient polynomials have a literal Bezout combination equal to one.
Thus they cannot all vanish at any algebraic j. This proves that the
entire zero-P chart fails full inverse support.

The zero-J chart is obtained by the invertible binary transformation
`(P,Q,j)->(P,P-Q,-j)`. The captured octic identity and conormal identity
are polynomial homogeneous identities, including their fixed-degree
powers of P-Q. The transformation preserves the point P=0. It also
retains points that become infinity; it is not merely an affine change
on an open subset. Consequently the zero-J chart fails full inverse
support as well.

The independent standard-library arithmetic audit reads the captured
JSON and checks the original factorization, original division product,
generator binding, all five Bezout products, and both homogeneous
coordinate identities. It uses restricted AST parsing and exact
`fractions.Fraction` arithmetic; it neither imports nor executes the
owner checker. Evidence is
[the literal arithmetic report](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic-report.json),
[source](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic.py)
and [raw output](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic.stdout.txt).

**Audit conclusion: PROVED within the inherited model.** Both charts have
no mate in any degree, because they fail the necessary full support
condition. This conclusion uses every parameter j and every projective
point; it is stronger than the earlier generic-gcd observation.

## 3. Lambda=1: the added A4 root and all leading drops are retained

The actual captured main coefficient lists specialize to

    H3=(d+1)p^3-6p^2+(6-6d)p+4d,
    S5=2d*p*Q4,
    Q4=(90d^2-76d-58)p^4+(-405d^2+458d+203)p^3
        +(675d^2-858d-261)p^2+(-450d^2+800d+174)p-400d.

Here d is delta and d is nonzero. Jbar=0, so the allowed support is H3
together with p=0. Since Q4(0)=-400d is nonzero, this added A4 point
cannot cover any root of Q4. Support requires every Q4 root to lie on H3.

On `T=45d^2-38d-29 != 0`, Q4 has degree four. Its finite roots must satisfy
`Q4 | H3^4`, independently of any leading drop of H3 itself. The captured
four remainders have denominators respectively `32,256,512,512` times
T^9. Their original numerator generators have a literal Bezout product
equal to one. No d in this chart satisfies the support condition.

On T=0, the fixed-degree Q4 has an infinity root. H3 has an infinity root
only when d+1=0. The exact polynomial identity

    T-(45d-83)(d+1)=54

shows that these conditions cannot occur together. The additional A4
point p=0 is finite. Thus the entire Q4-leading-drop locus also fails
support. At d=-1, where H3 loses affine degree, T=54 is nonzero, so the
original Bezout chart already covers it.

The independent arithmetic subaudit checks the original numerator
Bezout product, all denominator factors, and the exact binding of the
captured fractions to `H3^4 mod Q4`. A separate exact sparse-polynomial
calculation binds the compact H3 and Q4 to the actual main coefficient
lists at lambda=1; its
[report](../validation/2026-10-14-quintic-independent-audit/lambda-binding-result.json)
also records the nonzero scalar 2d and the infinity separation identity.
The arithmetic report in section 2 contains the original-generator
checks. Failed parser versions are preserved in this independent lineage.

**Audit conclusion: PROVED within the inherited model.** The whole
lambda=1 chart fails full inverse support and has no mate in any degree.

## 4. A degree-independent root-support lemma

Let H and S be nonzero homogeneous binary forms of degrees r and n over
an algebraically closed field, and suppose `supp(S) subset supp(H)`.
Then S has at most r distinct projective roots. If it has exactly r,
H is squarefree and H divides S. Otherwise S has at most r-1 roots;
its multiplicities form a partition of n into at most r-1 positive parts.

Proof: a degree-r binary form has at most r distinct roots. Equality in
the support bound forces H to have exactly those r roots, each of
multiplicity one. Each divides S, so their product H divides S up to
a nonzero scalar. The remaining assertion is just the factorization of
S with its positive root multiplicities. This proof retains infinity
and requires no characteristic assumption. Derivative descriptions of
the resulting incidence need their own characteristic hypotheses.

For r=3,n=5 the complete alternatives are: H divides S, a root of S has
multiplicity at least four, or the exact root pattern is 3+2. This replaces
one very large power-remainder calculation with smaller divisibility and
root-multiplicity incidences. It is a proved structural reduction; it
does not by itself assert that any parameter incidence is empty.

## 5. Main h=3: homogeneous infinity and the first two support alternatives

On the main proportional chart the captured actual factorization is

    F=-d^4 H3 S5/(1296 lambda^6).

The minus sign follows from the captured normalization of H3; only the
nonzero scalar matters for support. The complete Jbar-zero factorization
reduces all lambda!=1, Jbar=0 values to the already excluded G=Jbar=0
all-power locus. That accepted theorem excludes mates there; this audit
does not replace it by an unsupported full-SUP exclusion.

Thus the main support analysis retains

    V=d lambda(lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)d+lambda-1) != 0.

Write c5=LC(S5) and h3=LC(H3)=d+2lambda-1. If c5=0, S5 has an infinity
root, so support would require h3=0. Substituting d=1-2lambda gives the
exact coefficient identity

    c5=-216 lambda^4(2lambda-1)^3=216 lambda^4 d^3,

contradicting d lambda nonzero. This is a complete homogeneous exclusion
of the S5 leading-drop case. If h3=0 while c5!=0, H3 has at most two
finite roots, so the at-least-three-root alternative cannot occur.

On h3 c5!=0 the saved three pseudoremainder coefficients R_i of S5 by
H3 are divided only by the common factor lambda^2, a unit. The literal
original-generator identity is

    sum_i W_i R_i=(V h3 c5)^2.

This excludes H3|S5 on the precise declared chart. The exact witness is
[saved](../validation/2026-10-13-generalization-quintic-h3/h-divides-s-witness.txt),
and the owner source asserts the literal matrix product before saving it.
The original failed extraction omitted c5, found no witness at the stated
bounded exponent, and failed its assertion. Its failure is retained;
the repaired chart is the one used here.

For multiplicity at least four the original four generators are
`S5(x),S5'(x),S5''(x),S5'''(x)`. In characteristic zero their vanishing is
equivalent to a root of multiplicity at least four. The completed owner
source records a literal combination of these original generators equal
to `(V c5)^2`, with x retained as a variable. Its
[22 MB exact witness](../validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness.txt)
is accompanied by exponent two, the original input row, the source
`generalization_quintic_h3_multiplicity_witness.m2`, and passing raw output.
This is an exact membership certificate on all parameters, rather than
a reliance on a printed saturated `ideal(1)` or a root sample.

The independent arithmetic subaudit now also multiplies the original
three R_i entries by their saved 3-by-1 witness, using a strict expanded
monomial parser and denominator-cleared integer convolution. Its residual
is exactly zero against the original `(V h3 c5)^2` target. The R_i contain
69,62,58 terms and the corresponding witnesses contain 436,465,485 terms;
these are descriptive sizes, not additional theorem counts. It binds the
actual captured c5 and the exponent-two file. Evidence is the
[main literal report](../validation/2026-10-14-quintic-independent-audit/main-h3-literal-arithmetic-report.json),
[independent source](../validation/2026-10-14-quintic-independent-audit/main-h3-literal-arithmetic.py)
and its raw output.

**Audit conclusion for these alternatives: their geometric implications
are sound, with actual original-generator membership witnesses.** The
three-root and multiplicity-at-least-four alternatives are excluded under
the stated units. No expensive repetition of the already asserted 22 MB
witness product is counted as a new independent calculation here.


## 6. The final 3+2 support pattern

If x is the triple root of an affine quintic with coefficients c_i, then
division by `(p-x)^3` gives the residual quadratic

    c5 p^2+(c4+3x c5)p+(c3+3x c4+6x^2 c5).

Its discriminant is exactly

    c4^2-4c3c5-6x c4c5-15x^2 c5^2.

With c5 nonzero, discriminant zero makes its double root
`y=-(c4+3x c5)/(2c5)`. Full support requires H3(x)=H3(y)=0. Multiplying
the latter equation by `(2c5)^3` is equivalent to it, even if H3 loses
affine degree, because 2c5 is a unit. Thus the owner's six original
generators retain exactly the necessary equations, all finite x,y,
coalescence into a fifth root, and every H3-leading drop.


## 2. The final original-generator identity

For multiplicities 3+2, choose x to be the triple root. The actual
six-generator row M6 comprises

```
S5(x), S5'(x), S5''(x),
c4^2-4c3 c5-6x c4 c5-15x^2 c5^2,
H3(x), (2c5)^3 H3(-(c4+3x c5)/(2c5)).
```

These are polynomial equations after the stated denominator clearing.
The second root is uniquely the double root of the residual quadratic;
2c5 is a unit. Thus every actual 3+2 support configuration satisfies
all six equations. Coalescence into a fifth root is also retained.

The completed source
[support32 witness](../computations/generalization_quintic_h3_support32_witness.m2)
loads those **original six generators**, finds exponent two, constructs
the column W, and asserts the exact identity

```
M6 W=(V c5)^2.
```

The original-six-generator support32 source has SHA256 `2f8741c5cd8b7e1c97cc60d12ab0bad6409b6a7bc3121dcc09722a12b6b6c55a`. It uses exponent two and asserts the literal generator-product identity before writing the retained exact witness.

At a simultaneous zero of M6 with Vc5 nonzero, this identity says
`0=(Vc5)^2`, impossible. This closes the last support pattern without
interpreting a leading resultant factor as an actual inverse point,
replacing full conductor multiplicity by a first symbol, or relying
only on a printed saturated unit ideal.


## Literal products and coefficient bindings

## Zero charts

`h3-literal-arithmetic.py` independently checks the JSON capture
`research/validation/2026-10-13-h3-zero-chart-conductor-new/new-exact-support-incidence.json`.
The following identities pass:

- `S*Q5 = (9/2)*zero_P_F`, with `Q5` monic of degree five in `p`.
- `S^5 = Q5*captured_quotient + captured_remainder`, and the remainder has
  `p` degree below five.
- The five original generator lists are exactly the five `p` coefficients
  of that remainder.
- Multiplying those five original generators by the five captured Bezout
  coefficients gives exactly `1`.
- The binary coordinate swap takes the captured zero-P octic to zero-J:
  `FJ(p,j)=(p-1)^8*FP(p/(p-1),-j)`.
- The corresponding cubic swap gives the literal zero-J conormal:
  `(-2/3)*(p-1)^3*S(p/(p-1),-j)`.

## Lambda equals one

The same source independently parses the four compact numerator and
denominator captures and the original four-entry Bezout matrix. The original
numerator/witness product is exactly `1`.

Writing `T=45*delta^2-38*delta-29`, the captured remainder denominators are
respectively `32*T^9`, `256*T^9`, `512*T^9`, `512*T^9`. After clearing `T^9`,
the captured numerator/denominator remainder is exactly `H^4 mod Q4`; its
`q` degree is below four. The binding is proved by nine fraction-free
division steps and exact zero residual, without generating a new Bezout
certificate.

The separate `lambda-binding-audit.py` proves that the literal main
coefficient captures specialize to

`main_H(delta,1,q) = H(delta,q)`

and

`main_S(delta,1,q) = 2*delta*q*Q4(delta,q)`.

The factor `2*delta` is a unit on the intended `delta != 0` chart. It is not
a constant unit of `QQ[delta]`; retain that parameter condition when using
the binding.

Both independent arithmetic sources check the leading-drop separation:

`T-(45*delta-83)*(delta+1)=54`,

with `H` infinity coefficient `delta+1` and `Q4` infinity coefficient `2*T`.
Also `Q4(0)=-400*delta`. The captured compact remainder formulas use the
`T != 0` chart; the displayed leading-drop identity does not.

## Main H divides S coefficient witness

`main-h3-literal-arithmetic.py` uses a separate strict expanded-monomial text
parser. Each of the three original entries in `h-divides-s-remainder.txt`
divides exactly by `ll^2`. The resulting generator term counts are
`[69,62,58]`; the three captured witness term counts are `[436,465,485]`.

The captured exponent is `2`. Exact denominator-cleared integer convolution
gives

`sum_i ((original_remainder_i/ll^2)*captured_witness_i) = U^2`,

where

`U = S_coeff5*dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*(dl+2*ll-1)`.

Here `S_coeff5` comes directly from the captured main-S coefficient list.
The target has 229 terms; the identity residual has zero terms. This audit
checks the displayed exponent-two witness and makes no assertion that two
is the minimal possible exponent.


## Exact support and remaining scope

The original H3|S5 three-generator witness, multiplicity-at-least-four original four-generator witness and final3+2 original six-generator witness are distinct proof branches. Retain their exact inputs and coefficient columns: [H-divides-S input/witness source](../computations/generalization_quintic_h3_divisibility_certificate.m2), [multiplicity-four source](../computations/generalization_quintic_h3_multiplicity_witness.m2), and [3+2 source](../computations/generalization_quintic_h3_support32_witness.m2). The [original six-generator input](../validation/2026-10-13-generalization-quintic-h3/support32-input.txt) and [compressed support32 witness](../validation/2026-10-13-generalization-quintic-h3/support32-witness.txt.gz) are essential saved mathematical data; a byte/hash check alone is not a substitute for its asserted original-generator product. The duplicate subset extraction carries the same uncompressed matrix and adds no distinct proof.

The sole-common-root regular-L1/L2 bridges are a different contribution, owned with [single-root incidence](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md) and the full L2 theorem in [the A4 conductor/incidence treatment](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). They do not settle Z=0, target infinity, Jbar=0 or several allowed support points by themselves.

The h=2 incidence, degree-one singular quotient-fiber charts, other quintic normalizations and entirely thick presentations remain separate questions. The coefficient identities are exact characteristic-zero proofs on the stated unit charts. Their geometric setup, scalar inversions, multiplicity derivatives and witness nonvanishing must be verified before any reduction modulo a prime; no arbitrary positive-characteristic exclusion is asserted.

The other two branches retain direct data access: [H3-divides-S5 original remainder generators](../validation/2026-10-13-generalization-quintic-h3/h-divides-s-remainder.txt) and [three-entry witness](../validation/2026-10-13-generalization-quintic-h3/h-divides-s-witness.txt), plus [multiplicity-four original input](../validation/2026-10-13-generalization-quintic-h3/multiplicity4-input.txt) and [four-entry witness](../validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness.txt). These literal coefficient columns support different root-pattern exclusions; they are not interchangeable logs.

## Consolidation review

Independent preservation review compared the complete geometric source/audit and all literal-arithmetic bindings, retained the completed original-six-generator certificate in place of obsolete pending labels, and checked all three branches' live input/witness routes. The zero, lambda-one, homogeneous leading-drop and root-pattern scopes are unchanged. It reused accepted unchanged exact products without rerunning the large coefficient matrices. Full regular-L1/L2 bridges and opposite-ruling geometry were separately reviewed and moved to their thematic homes. No essential code/data retirement or unrestricted theorem follows.
