# Independent audit of new nonendpoint quintic support reductions

Date: 2026-10-14. Independent auditor: `quintic_new_audit`, with arithmetic
subaudit `h3_literal_witness`.

Status: **NEW GEOMETRIC PROOF AUDIT; ZERO-CUBIC, LAMBDA-ONE AND REGULAR
SOLE-ROOT EXCLUSIONS ACCEPTED. MAIN h=3 CERTIFICATES ARE RECORDED BELOW
WITH THEIR EXACT CURRENT LIMITS.** Older accepted proofs are premises. No accepted
model, conductor, conormal, endpoint, residual-partition, or regular-L1
verifier was rerun. Canonical files were not edited.

This audit reviews the owner notes
[quintic continuation](2026-10-13-generalization-quintic-continuation.md)
and [regular L2](2026-10-13-generalization-quintic-l2.md). The underlying
problem remains restricted to the fixed characteristic-zero rational
quartic C0, the sectional-genus-one degree-five A4 normalization model,
and its actual nonendpoint projections. It does not decide the universal
projective-curve problem, other quintic normalization genera, higher
carriers, or entirely thick presentations.

## 1. Premises and the geometric implication actually being audited

The accepted normalization model and actual center-avoidance conditions
give a finite birational projection `nu:S->X`, with `c` mapped
isomorphically to C0. A mate forces full inverse support
`nu^{-1}(C0)_red=c`. The
[accepted conductor module audit](2026-10-12-session-conductor-quadric-module-independent-audit.md)
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
and its raw output. The first unavailable-runtime-path attempt is retained.

**Audit conclusion for these alternatives: their geometric implications
are sound, with actual original-generator membership witnesses.** The
three-root and multiplicity-at-least-four alternatives are excluded under
the stated units. No expensive repetition of the already asserted 22 MB
witness product is counted as a new independent calculation here.

## 6. The remaining 3+2 support pattern: exact required certificate

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

The new saturation output for these six generators is the unit ideal.
At the time this audit section was written, an original-generator power
witness for this six-generator ideal had not yet been bound to a finished
execution. **The final 3+2 emptiness claim and the complete main h=3
exclusion remain pending that literal witness.** Neither the unfinished
unrestricted multiplicity32 calculation nor the unit-ideal printout alone
is promoted by this audit. Sections 4--5 remain proved without it.

## 7. Regular L2: geometric elimination cover and retained exceptional loci

The owner L2 theorem asserts that, on the accepted finite common-root
incidence and regular chart `qZ(q)!=0`, with `L1!=0,L2=0`, the actual
Taylor coefficients f2,f3,f4,f5 cannot all vanish. Here

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2),
    Z(q)=q Pc U.

The exact coefficient identity
`partial_a f2=-(dq/2)L1 partial_k L2 (mod L2)` justifies solving for a
only where the L2 root is simple and L1 is nonzero. No original fiber
leading coefficient or unstated center parameter is divided out.

The finite cover is complete. q=1 is impossible because L2=d^5. q=2 is
handled by its two-embedding quadratic-field cover. Away from q=1,2,
the D=0 boundary makes L2 genuinely linear in k and is handled separately.
On D!=0, a discriminant-zero root has the displayed L1=0 value and lies
outside the new L1!=0 theorem. The remaining points have the algebraic
coordinate m in owner equations (3)--(4). Both signs are covered because
the inverse formula determines m from the actual k; no chosen square-root
branch is lost. All rational-cover denominators are units under d,q,Pc,
q-1,q-2,D nonzero and m^2!=3.

The audit initially flagged the extra polynomial H removed from the f3
numerator. The owner now records the exact identity

    L1=-3m(q-2)Pc^2 H/
      [q^2(q-1)(m^2-3)^2(qm+3q-6)].

Consequently m and H are units on the retained L1!=0 chart. This repairs
the proof gap that would arise from removing H without this identity.
The three normalizations of f3,f4,f5 therefore preserve every candidate.
A common finite m root forces both fixed-degree resultants R34,R35 to
vanish. This implication is valid even when their m-leading degrees drop;
no converse resultant implication is being used.

The completed literal original-resultant witness combines R34,R35 to
`q^53(q-2)^44 Pc^69`, a unit on this chart. The completed D=0 witness
combines the original f3,f4 numerators to q^4. On D=0 the displayed a
coefficient can vanish only when L1 does, by the same derivative identity;
its additional quartic V is therefore not a missing a-solve stratum.
At q=2 the owner gives an original five-generator witness, over the exact
field QQ(mu), mu^2=3, for f2,f3,f4,f5 together with
`1-z*d*(d+2mu/3)`. Both embeddings apply to the characteristic-zero
algebraically closed ground field, so the two L2 roots are retained.
The inverse equation imposes precisely the stated d,L1 units.

These literal witnesses are saved under
`validation/2026-10-13-generalization-quintic-l2/`; the completed Bezout
source asserts the three coefficient normalizations and both original
products before saving them, and the q2 source asserts its matrix product.
The evidence comprises the actual input pairs, targets, columns and raw
PASS streams, rather than just gcd factors or a saturated ideal printout.
This independent review inspects those exact constructions and accepts
their geometry; it does not count them as fresh independent executions.

**Audit conclusion: the local regular-L2 theorem and its all-mate
single-root consequence are proved by the displayed cover and completed
literal owner certificates, within their precise scope.** The latter
consequence additionally needs Jbar nonzero and q to be the sole common
homogeneous conormal root. Then full support concentrates the actual
nonzero degree-eight binary section at q, forcing order eight, while
nonvanishing of at least one of f2 through f5 gives order at most five.
The regular-L1 geometric bridge is reviewed explicitly in section 8.

This does not prove an order bound on Z=0, target infinity, q=0, Jbar=0,
or the excluded L1 branch. It does not exclude several support points
sharing conductor degree eight. All those distinctions survive handoff.

The independent audit additionally verifies nine small rational-cover
identities directly, without loading F or an inherited source. They
include the compact discriminant, the cover equation and inverse, the
L1/H identity, the D factor, and the D=0 solve. On D=0 the exact relation
is `L1=-q(q-2)V/[8(q-1)]`, confirming directly that V=0 is the already
excluded L1=0 boundary. The original full L2 discriminant at q=2 is
48d^6; the normalized quadratic after removing 2d has discriminant 12d^4.
Either is nonzero for d nonzero. This clarifies an exponent slip in the
owner note without changing its conclusion. The
[new small source](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.m2)
has exit zero and nine literal PASS statements in its
[raw output](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.stdout.txt).
The first version's unparenthesized `diff` expression caused an M2 parse
failure and is retained. An unexecuted Python alternative was abandoned
because the remembered CAS runtime is absent and system Python has no
SymPy; it supplies no evidence.

## 8. Independent review of the existing regular-L1 geometric bridge

The exact identities in the
[October 13 quotient-fiber note](2026-10-13-session-nonendpoint-single-root-quotient-fibers.md)
were already captured and verified, but its geometric bridge still
requested independent review. This section reviews only that implication;
its eleven-identity checker and separate exact double-root checker were
not replayed.

On `qZ(q)!=0`, the actual finite normalization-point reconstruction in
the accepted fiber model applies to common quotient roots. Put
`rho=d/q`. After removing the diagonal factors, the exact linear and
quadratic quotients are L and Q, with normalized quotient norm

    OffNorm=d^2 q^5 U^2 L1.

When Aq!=0, L is a genuine linear polynomial. On L1=0 its unique finite
root also solves Q. When Aq=0, the accepted cubic's quadratic coefficient
is `-q[3d^2q(2-q)]^2`, nonzero on this chart. Thus Q after diagonal
division is a genuine linear polynomial. Its leading coefficient is
nonzero, and OffNorm=0 forces the constant L to vanish identically; Q
still has a finite common root. This retains the leading drop rather
than mistaking a fixed-degree resultant factor Aq for a point.

Full inverse support forces every such root to equal rho; an off-diagonal
root reconstructs an actual normalization point outside c. It follows
that `L(rho)=Q(rho)=0`. A doubled or tripled fiber supported at rho is
allowed at this stage and is not excluded by saturation.

The exact equation `L(rho)=dq*S=0` excludes q=1,2 and gives
`k=d+d^2(2q-3)/[3(q-1)(q-2)]`. The exact Q(rho) equation then forces

    d=Pc(q-2)/[q(q-1)].

That last equation is used even when `P6=q^2-3q+3` vanishes and Aq=0.
The proof does not divide by P6, so this degree-drop component is retained.
The captured actual-section computation on these precise parameters is

    F(q+t)=f2*t^2+terms of degree at least three,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8] != 0.

All factors in this expression are units under the stated chart and the
just-derived exclusions q=1,2. If Jbar!=0 and q is the sole common
homogeneous conormal root, the accepted support bridge requires the
nonzero degree-eight conductor form to be concentrated at q, hence to
have order eight. Its actual order two contradicts that requirement.

**Audit conclusion: the regular-L1 all-mate exclusion is now independently
accepted in exactly this sole-root, Jbar-nonzero, qZ-nonzero scope.** This
supplies the previously pending geometric premise needed for section 7's
combined regular sole-root theorem. No such conclusion is extended to
Z=0, other conormal roots, or an allowed A4 contribution when Jbar=0.

## 9. Continuation boundary and evidence accounting

The new reviewed mathematics already excludes the zero-cubic and
lambda-one h=3 charts, the three-root and multiplicity-at-least-four main
h=3 alternatives, and the regular finite sole-root Jbar-nonzero lane in
every mate degree. The degree-independent root-support lemma in section 4
is an additional reusable result. The final main 3+2 witness is the
specific remaining review item in this note; no global quintic or C0
conclusion is drawn while it is pending.

All exact arithmetic counts in the independent report refer to stated
identity products and coefficient bindings. They do not re-prove the
normalization/conductor theorem, exhaust other parameter strata, or
establish novelty. The failed sources and interrupted direct saturation
and Hermite approaches remain useful provenance, but supply no missing
theorem. Additional completed witnesses can be appended to this audit
without replaying accepted verifiers.
