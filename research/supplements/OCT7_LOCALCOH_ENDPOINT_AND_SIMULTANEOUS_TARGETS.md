# October 7 local-cohomology endpoint and simultaneous-target mathematics

Preserved source mathematics, not independently re-audited in this migration. The failed bridge is retained only for its substantive failure mode; its retracted proof is not authoritative.

---

## e1-simultaneous

# Simultaneous-target repair for primitive e=1 quartic ancestors

Date: 2026-10-07. Fixed `C0` over an algebraically closed field of
characteristic zero. Status: **PROVED UNDER THE EXPLICIT ACCEPTED INPUTS;
root and independent adversarial audits accepted on 2026-10-07.** Under the already accepted socle
theorem, P-037 and complete primitive-e=1 quartic fibres, this excludes
common quartic ancestors with `e=1,D2=0`. The defective-triple stratum
`e=1,D2>0` remains open.

The original single-multiplier argument is preserved separately as
[`2026-10-07-session-localcoh-mf6-bridge.md`](2026-10-07-session-localcoh-mf6-bridge.md),
explicitly labeled **FAILED**. Its error was treating `F*alpha=u` as
`F=0` in the quadruple rather than a nonzero socle target. This repair
keeps both target equations and their independence throughout.

## 1. Primitive triple, complete fibres and rank-two targets

The accepted quartic-ancestor reduction gives a saturated finite-flat CM
quadruple `Z` whose generic transverse algebra is curvilinear of length
four, with

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Its saturated socle `E3` is an ideal, and `OZ/E3` is torsion-free over
the reduced curve. Since the images of `F,G` in `OZ` are generically
socle elements, both vanish in `OZ/E3` everywhere. They contain the
embedded canonical triple `Z3=Spec(OZ/E3)`.

If `D2=0`, a local generator `ell` of the first quotient has square
generating the second quotient. The triple then has local basis
`1,ell,ell^2` and is primitive, whether or not the quadruple has a
defective last piece. For `e=1` it has `L=O(-6)` and belongs to the four
complete actual torus orbits in
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md).
This proof uses its complete quartic fibres, rather than its individual
carrier cubic-pole bounds or its STCI mate-support argument.

Three of these fibres are two-dimensional pencils. The original
multipliers `F,G` are linearly independent because their images are the
independent classes `u,v`. Thus they form a basis of the full pencil.
For any chosen fixed basis `F0,F1`, its target images `f0,f1` must be
an invertible constant change of `u,v`, and remain a rank-two,
basepoint-free target pencil.

## 2. The global socle and normal frames

The accepted socle-pencil theorem gives the **untwisted** isomorphism

```text
alpha: E3 -> omegaC(-3)=O_P1(-14).
```

After twisting by an ambient quartic it gives

```text
alpha: E3(4) -> omegaC(1)=O_P1(2).
```

Choose the finite socle frame `w` using this isomorphism. In the first
support chart `x0=1,x1=z`, the balanced normal parameters are exactly
the ones used by MF6:

```text
V=x2-z^3, U=q-z*V/2, q=x3-z*x2.
```

The first-normal determinant of `(q,B)` relative to `(U,V)` is `z^3`.
The raw target numerators restrict to `xz=z^3` and `yw=z^5`, so their
socle coefficients are `1,z^2` after cancellation. The accepted socle
theorem verifies that this cancellation extends at the endpoints.
Therefore, in this finite frame,

```text
f0,f1 in span_k(1,z^2),
```

and together they must be a rank-two, basepoint-free basis of that
pencil. The raw numerators are not substituted for these normalized
sections.

For the principal primitive direction, use
`ell=(4/3)U+(1/6)V`; its constant Bezout relation against
`A=1+z,B=-2-8z` is one. For the algebraic directions
`A=r*z,B=1`, use `ell=V`. Hence both represent the actual finite frame
of `L=O(-6)`. On the overlap its first class transforms as
`ell_infinity=z^-6*ell`; normal terms of order at least two do not
affect its cube in a length-four algebra. The moving support-coordinate
correction also contributes only normal order at least four after
multiplication by `ell^3`. Thus

```text
ell_infinity^3=z^-18*ell^3,
w_infinity=z^-14*w,
tau_infinity=z^-4*tau,
```

where `ell^3=tau*w`. Consequently
`tau in H0(Hom(L^3,E3))=H0(O(4))` is a polynomial of degree at most
four on the finite chart.

The corrected primitive-triple normal parameter `m+gamma*ell^2` has a
regular socle coefficient `a` in `OZ`. With the accepted MF6 convention
`T=gamma*E-K`, every quartic in its complete fibre has exactly

```text
f_i=h_i*a-T_i*tau.
```

The relevant twists are `h in H0(O(8))`, `f in H0(O(2))`, and
`tau in H0(O(4))`. The corrected normal coefficient `a` and the cubic
coefficient `T` have inhomogeneous transition, so neither is assigned
an unsupported polynomial-degree bound. If the corrected normal frame
changes as `m_corr,infinity=z^-8*m_corr+rho*ell^3`, putting
`sigma=z^14*rho` gives

```text
a_infinity=z^6*a+sigma*tau,
h_infinity=z^-8*h,
T_infinity=z^2*T+z^-4*h*sigma,
f_infinity=z^-2*f.
```

These identities make the nonzero target equation glue correctly.
They do not replace it by an annihilation equation.

## 3. Principal orbit: simultaneous compatibility contradicts basepoint freedom

Put `P=4z^2+2z+1`. The complete principal pencil has

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
T0=(2z+1)*(1536z^5+1152z^4+448z^3+48z^2-24z+4),
T1=(2z+1)*(1536z^8+1152z^7+448z^6+240z^5+120z^4
           +60z^3+30z^2+15z+8).
```

Eliminating `a` from the two correct equations gives

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

Cancel the nonzero polynomial `P` to obtain

```text
(64z^6+8z^3+1)*f0-64z^3*f1
       =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` this requires `3f0(1/2)-8f1(1/2)=0`; at `z=-1/2`
it requires `f0(-1/2)+8f1(-1/2)=0`. Each `f_i` lies in
`span(1,z^2)`, so its values at these two points are equal. The two
independent relations force both targets to vanish there. This
contradicts their basepoint freedom. The principal contradiction needs
no degree bound on `tau`.

For a stronger exact coefficient check, the full remainder matrix
modulo `(2z-1)^3*(2z+1)` has rank three and kernel

```text
(f0,f1)=c*(z^2-1/4, (3/8)*(z^2-1/4)).
```

Thus it even forces the target pencil to rank at most one. Both
checks use the nonzero target terms, unlike the failed shortcut.

## 4. The two algebraic orbits: polynomial-degree contradiction

For `A=r*z,B=1,12r^2+4r+3=0`, the complete pencil has `gamma=0`
and

```text
h0=1, T0=0,
h1=(2r+2/3)*z^8, T1=(8r/9)*z^3.
```

Both scalar coefficients are units modulo the defining quadratic.
The target equations become

```text
a=f0,
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

The first right-hand term has degree at least eight for any nonzero
`f0`; the second has degree at most seven because `deg tau<=4`; and
`deg f1<=2`. Hence `f0=0`. The remaining right-hand term is divisible
by `z^3`, so `f1=0` as well. This contradicts target independence.
The exact quadratic-field unit checks treat both roots without generic
field-specialization inference.

## 5. The fourth orbit and exact evidence

For `A=-z/2,B=1`, the complete fibre is
`q*H0(P3,O(2))`. Hence `F=q*F2,G=q*G2`, and

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This is a degree-two common ancestor, forbidden by the all-stage P-037
theorem. It is the ancestor-specific quadric-factor argument, with no
STCI mate assumption.

The independent exact coefficient verifier is
[`verify_session_localcoh_e1_simultaneous_2026_10_07.py`](../computations/verify_session_localcoh_e1_simultaneous_2026_10_07.py).
It reconstructs the determinant and target remainder matrix from the
displayed accepted pencil coefficients, checks both simple evaluations
and the complete rank-three constraint, and verifies the scalar units
and all forcing degree coefficients over the exact algebraic field.
Its JSON states the required geometric inputs explicitly. Script
agreement is not a substitute for the frame argument in Section 2.

The root independently verified both simultaneous contradictions. The
separate frame audit
[`2026-10-07-session-socle-bridge-adversarial-audit.md`](2026-10-07-session-socle-bridge-adversarial-audit.md)
accepted the global socle frame, normalized targets, quotient-frame
transitions, tau degree bound and complete quadric orbit. The corrected
`e=1,D2=0` ancestor exclusion is therefore accepted. The failed earlier
proof remains clearly labeled as such.


---

## independent-audit

# Independent endpoint audit and one completed exceptional fibre

Date: 2026-10-07. Scope: the characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
and pure cubic top coefficient `h=t`. This is an independent audit of
Sections 4--6 of
[`2026-10-06-session-localcoh-progress.md`](2026-10-06-session-localcoh-progress.md).
It proves the stated endpoint classification and the first family's
generic exclusion, and closes its quadratic exceptional locus. It does
not exclude every quartic ancestor or address a nonendpoint top-zero.

## 1. Verdict and precise remaining locus

**PROVED under the previously audited actual top map and multiplication
tensor:** the four one-parameter direction families in the checkpoint
cover all remaining primitive `e=2,h=t` endpoint directions, after the
three corner directions and the reversed parity direction are removed.
Their lower corrections are the complete affine line `a*+lambda*k0`.
The first rational family excludes the target `u` for every `lambda`
outside the roots of its displayed clearing denominator. The formerly
retained locus `k^2-4k+5=0` is now excluded at both roots, again for every
`lambda`, by a complete exact number-field dual.

The first family's unresolved direction parameters are exactly the roots
of the following three polynomials **as exceptions to the available
dual**, without any implication that they support an ancestor:

```text
3k^4-9k^3-19k^2-43k-4
13k^4+26k^3+34k^2+6k-7
729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
 +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
 -1210068k^2-966908k-379834
```

All three are square-free and pairwise coprime. They are coprime to
`(k^2-1)(k^2+2k+3)(9k^4-21k^3+5k^2-31k+134)`, so all **21 geometric
parameter points** remain in the first family's primitive chart. Each
point retains the complete affine `lambda` fibre. The second rational
family and the two `p(0)=0` boundary families also retain their actual
quartic multiplier incidence. Their saved `.m2` inputs do not prove a
kernel or evaluation result; no live process was assumed and no seed
was promoted to an exclusion.

## 2. Surjectivity of the rational normalization

For `p(0)r(0)!=0`, actual torus and common direction scaling give
`p(0)=r(0)=1`. The top-image equations first determine

```text
b1=-6(a1^2+a2)-2a1-3/2,
Q=16a2^2+(16a1^2+12)a2+12a1^2+4a1+3=0.
```

The saved parametrization does more than give solutions. On `2a1+1!=0`
its inverse is the rational function

```text
k=(32a2+16a1^2+12)/(4(2a1+1)^2).
```

Modulo `Q`, its square is `(2a1-3)/(2a1+1)`. Substituting it into
`a1=(k^2+3)/(2(1-k^2))` and
`a2=-(k^2+2k+3)/(2(k+1)^2)` recovers the original coordinates exactly.
Neither `k=1` nor `k=-1` can arise from a finite point of this chart:
`k^2-1=-4/(2a1+1)`. At `2a1+1=0`, the equation is
`4(2a2+1)^2=0`; the last top equation is `2(b2+2)^2=0`.
Thus the unique missing normalization point is
`(a1,a2,b1,b2)=(-1/2,-1/2,1,-2)`, whose quadratic pair has the common
factor `1-t`. It is nonprimitive and loses no candidate. The remaining
top equation factors exactly into the two stated choices of `b2`.

On the separate endpoint boundary `p(0)=0,r(0)!=0`, normalization to
`r(0)=1` gives `b1=8a1^2a2` and precisely

```text
4a2(2a1+1)[(2a1+1)^2b2
           +2a2^2(2a1-1)(16a1^4+8a1^2+5)]=0.
```

For `a2=0`, the full homogeneous quadratic resultant is `a1^2*b2`,
so primitivity requires both factors nonzero. The actual reversal sends
this branch to the already certified parity branch, as in the checkpoint.
For `a2!=0`, torus normalization gives `a2=1`. Then either
`a1!=-1/2` and the displayed rational boundary formula holds, or
`a1=-1/2` and `b2` is free. The latter family has resultant `(b2+8)/4`
and must remain. No division by `a2` or `2a1+1` removes it.

The independent script uses a fixed four-by-four Sylvester determinant,
so its resultant checks include roots at infinity when leading
coefficients specialize to zero. It verifies the rational inverse and
all four saved seeds against the 32-by-30 actual top map. The map has
rank 29, its three annihilator rows have rank three, and its kernel is
one-dimensional. Hence the affine line of lower corrections is complete
at every retained parameter value.

## 3. What the generic polynomial dual actually proves

The saved first-family JSON has a cleared ancestor

```text
A=120(k-1)^9(k+1)^9*(a*(k)+lambda*k0).
```

The independent audit checks this identity coordinate by coordinate,
and checks `a*(k)` against its actual pure cubic top. The prefactor is
nonzero throughout the retained chart. The standard-library dual
verifier then checks all 18 actual tensor columns and the target value
against its full polynomial denominator. The independent audit also
reconstructs the displayed factorization of that target value exactly.
Thus the exclusion concerns the specified complete affine family of
ancestors, rather than an unrelated tensor kernel.

The factors `k+/-1` lie outside the chart. The factors `k^2+2k+3` and
`9k^4-21k^3+5k^2-31k+134` are precisely nonprimitive loci for the first
family. The additional quadratic `k^2-4k+5` was a genuine primitive
exception to this particular generic dual, and is closed next. The three
remaining factors retain the 21 points listed above.

## 4. Exact closure of the quadratic exception

The saved Macaulay2 output is a 74-entry row over

```text
K[lambda], K=QQ[k]/(k^2-4k+5).
```

Its entry 72 is exactly one. I reduced the actual rational seed and every
dual coefficient modulo the defining polynomial, checking each
denominator is a field unit. The defining polynomial has discriminant
`-4`, so it is irreducible over `QQ`. This is an exact field calculation;
it treats both geometric roots through the two embeddings into an
algebraically closed characteristic-zero field.

The new independent certificate stores each coefficient as `a+b*k` with
`a,b` rational. Its default verifier uses only Python's standard library
and the relation `k^2=4k-5`. It checks:

- the hashes of the actual tensor, coordinate basis, top map, rational
  seed, saved complete dual, evaluation file and module input;
- the actual pure cubic top of the entire affine ancestor, with its
  lower direction in the top-map kernel;
- the target columns `e72,e73` in the saved tensor;
- **all 18** polynomial identities `n^T L=0` over `K[lambda]`;
- `n^T u=1` and a nonzero primitive resultant.

Consequently no member at either quadratic root maps to `u`, for any
`lambda`. This removes `k^2-4k+5` from the unresolved exception list.
The certificate does not require trusting that the saved module's
kernel command or printed evaluation ideal was correct.

## 5. Reproduction and evidence

Run the complete endpoint audit with the repository's SymPy runtime:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/audit_session_localcoh_endpoint_2026_10_07.py
```

Verify the completed quadratic exception with an ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_q2_dual_2026_10_07.py
```

Regenerate its coefficient certificate from the saved rational sources
with the SymPy runtime and `--regenerate` on that same verifier.

The two exact output records are
[`session_localcoh_endpoint_audit_2026_10_07.json`](../computations/session_localcoh_endpoint_audit_2026_10_07.json)
and
[`session_localcoh_q2_dual_audit_2026_10_07.json`](../computations/session_localcoh_q2_dual_audit_2026_10_07.json).
Both were freshly generated and all assertions passed on 2026-10-07.
The uncomputed family inputs and every remaining denominator locus are
preserved for the next session.


---

## mf6-bridge

# FAILED bridge: a nonzero socle target was incorrectly treated as annihilation

Date: 2026-10-07. Fixed `C0` in characteristic zero. Status:
**FAILED; ORIGINAL PROOF RETRACTED.** The original text is retained below
as a failure record and must not be used as a proved exclusion.

The root audit caught the exact flaw: `F*alpha=u` makes the image of F
in OZ a **nonzero socle element**, rather than zero. It vanishes only
in the canonical triple OZ/E3. Section 3 below therefore incorrectly
uses `h*a=T*c^d3*unit`. The actual equation is
`h*a-T*c^d3*unit=f_u`, with a regular nonzero target coefficient.
Dividing by h can introduce extra target poles, so the claimed
single-multiplier cubic polar bound does not follow. The same applies
to G. The canonical-triple containment and the quadric-factor P-037
argument remain valid; the claimed four-orbit conclusion does not follow
from this failed proof. A separate simultaneous-two-target repair is
now saved and independently accepted as
[`2026-10-07-session-localcoh-e1-simultaneous.md`](2026-10-07-session-localcoh-e1-simultaneous.md).
No canonical record should promote the exclusion from the failed text
retained here; use that corrected two-target proof instead.

---

## Historical retracted argument

## 1. Precise corollary

Suppose quartics `F,G` and a local-cohomology ancestor `alpha` satisfy
`F*alpha=u,G*alpha=v`. Its saturated annihilator defines the finite-flat
CM quadruple `Z` from the audited generic-length reduction. Write

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

The socle-pencil theorem in
[`2026-10-06-session-localcoh-progress.md`](2026-10-06-session-localcoh-progress.md),
Section 2, forces `degD3=7-3e`. Therefore:

> There is no common quartic ancestor with `e=1,D2=0`.

The accepted MF6 orbit calculations used here are Sections 2--5 of
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md).
Only their complete primitive-triple classification and cubic polar
degree bounds are needed. The further mate-support argument for the
pure quartic carriers is not used in the ancestor setting.

## 2. Why the two multipliers contain the canonical triple

The saturated socle `E3` is an ideal in `OZ`, and `OZ/E3` is torsion-free
over the smooth reduced support. Generically the images of `F,G` in
`OZ` are socle elements. Their images in `OZ/E3` therefore vanish
generically and, by torsion-freeness, vanish everywhere. Thus both
quartics contain the embedded canonical triple

```text
Z3=Spec(OZ/E3).
```

When `D2=0`, the multiplication `L^2 -> E2` is everywhere a unit. In a
completed support DVR, choose a normal parameter `ell` whose first
class generates `L`. Its square generates `E2`. The canonical triple
is locally generated by that one normal parameter, with basis
`1,ell,ell^2`. Consequently it is an embedded primitive triple. This
does not require the quadruple's special fibres to be curvilinear:
the possible extra degeneration lies in its last piece `E3` and has
been quotiented out.

For `e=1`, this is exactly a global primitive triple with
`L=O(-6)`. It therefore belongs to one of the four actual torus orbits
of the independent MF6 classification.

## 3. The cubic pole bound remains valid for a defective quadruple

Fix a completed support DVR `R=k[[c]]`. In a primitive-triple chart take
ambient normal parameters `m,ell` and the regular quadratic correction
`gamma` so that

```text
m+gamma*ell^2=0 in OZ3.
```

Let `w` generate the locally free socle line `E3`. Since this relation
holds in the canonical triple, it has the form
`m+gamma*ell^2=a(c)*w` in `OZ`, with `a(c)` regular. The ordinary cubic
product has the form

```text
ell^3=c^d3*unit*w,
```

where `d3` is the local multiplicity of `D3`. This is precisely the
definition of the saturated multiplication map `L^3 -> E3`.

For a quartic containing `Z3`, let `h` be its first-normal coefficient
and `T` the cubic coefficient after the regular quadratic correction.
If `h` is not identically zero, its vanishing in `OZ` gives, up to the
chosen harmless sign convention,

```text
h*a(c)=T*c^d3*unit.
```

Thus `T/h` has pole order at most `d3`. Summing the exact local pole
orders over the curve gives

```text
deg(cubic pole divisor of that quartic) <= degD3.
```

Only containment in the quadruple and regularity of its socle lattice
are used. No relative Gorenstein-fibre assumption and no mate support
condition enter this inequality.

## 4. The four complete quartic fibres give the contradiction

For the principal orbit `A=1+z,B=-2-8z`, every nonzero quartic in its
complete two-dimensional fibre has a nonzero first-normal symbol, and
its cubic polar degree is at least six. For each of the two conjugate
orbits `A=r*z,B=1,12r^2+4r+3=0`, every nonzero quartic likewise has a
nonzero first symbol and cubic polar degree at least five, including
the directly expanded infinity member. But the ancestor socle theorem
gives `degD3=4` when `e=1`. Section 3 contradicts each of these three
orbits, for either multiplier separately.

In the fourth orbit, `A=-z/2,B=1`, the complete quartic fibre is
`q*H0(P3,O(2))`. This fibre includes members with zero first-normal
symbol, so the polar argument cannot be substituted here. Both
multipliers instead have the form `F=q*F2,G=q*G2`. Their equations give

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This is a common ancestor with degree-two multipliers, prohibited by
the all-stage theorem P-037. The equation `u!=0` also ensures
`q*alpha!=0`. The obstruction is valid for the ancestor equations;
the separate STCI unique-quadric-factor argument is unnecessary.

All four primitive `e=1` directions are therefore excluded in the
common quartic-ancestor problem. The `e=1,D2>0` stratum remains open:
its canonical triple is defective and does not belong to the primitive
classification used in this proof.


---

## q1-exception

# Exact closure of the first endpoint family's Q1 exception

Date: 2026-10-07. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top `h=t`, and the first rational endpoint family from the
independently audited endpoint classification. No assertion here concerns
a nonendpoint top zero, another endpoint family, or the global STCI question.

## Result

**PROVED under the audited actual tensor and coordinate bases:** every
member of the complete affine line of quartic ancestors at every geometric
root of

```text
Q1(k)=3k^4-9k^3-19k^2-43k-4
```

fails the target-`u` multiplication incidence. Thus this quartic factor
can be removed from the first family's denominator-exception list. Together
with the previously closed quadratic factor, the remaining exceptions to
that family's available generic dual are the four roots of
`13k^4+26k^3+34k^2+6k-7` and the thirteen roots of the recorded degree-thirteen
factor, each with its complete affine lower-correction fibre. These seventeen
points remain exceptions to the available certificate, rather than evidence
for an ancestor.

## Exact calculation and independent verification

The defining polynomial is irreducible over `QQ`: its reduction modulo 23,
made monic, is

```text
f(k)=k^4+20k^3+9k^2+k+14 in F_23[k].
```

The standard-library verifier checks `k^(23^4)=k (mod f)` and
`gcd(f,k^(23^2)-k)=1` using modular polynomial arithmetic. This is the
degree-four irreducibility test, and also ensures that
`K=QQ[k]/Q1` is a field. All seed denominators were inverted exactly in
this field before exporting the module.

The retained rational seed and its kernel direction give
`alpha=a*(k)+lambda*k0`. From the actual 74-by-542 tensor, the generator
constructs all entries of the 74-by-18 multiplier matrix `L(alpha)`.
Macaulay2 computes the full polynomial left-kernel module over `K[lambda]`.
Its target evaluation ideal is `(1)`. A resulting exact left dual `n`
has 26 nonzero entries, degree at most two in `lambda`, and entry 72 equal
to one.

The subsequent verifier uses only exact rational arithmetic and

```text
k^4=3k^3+(19/3)k^2+(43/3)k+4/3.
```

It checks all eighteen identities `n^T L(alpha)=0` coefficient by coefficient
in `lambda`, and `n^T u=1`, with `u=e72` checked against the tensor's actual
target column. Therefore `u` is outside the image for every `lambda`.
Because Q1 is irreducible and characteristic zero is separable, this exact
field identity applies through all four embeddings into an algebraic closure.

The verifier also checks the 32-by-30 actual pure-top map has rank 29,
the nonzero coefficient of `lambda` is exactly its saved kernel vector,
and the top of every `alpha` is `t*p^i*r^(3-i)` in all 32 coordinates.
This confirms that the entire affine fibre of lower corrections has been
tested. A fixed four-by-four Sylvester determinant verifies the homogeneous
quadratic direction is primitive, including possible leading-coefficient
specializations. Every input is bound to the coefficient certificate by SHA256.

## Reproduction and terminal process status

Generate the reduced module input:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/generate_session_localcoh_q1_module_2026_10_07.py
```

Compute the full polynomial dual:

```sh
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-1-exception-q1.m2
```

Regenerate and independently verify the coefficient certificate:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_q1_dual_2026_10_07.py --regenerate
python3 research/computations/verify_session_localcoh_q1_dual_2026_10_07.py
```

The generator ran in tool session `21852`, the M2 computation in session
`13750`, and certificate regeneration in session `1314`; all three
completed with exit code zero. M2 printed matrix readiness, completed its
polynomial kernel, saved the unit evaluation ideal, and saved the dual.
No computation from this branch remains running.

The complete evidence is retained in
[`session-localcoh-origin-family-1-exception-q1.m2`](../computations/session-localcoh-origin-family-1-exception-q1.m2),
[`session-localcoh-origin-family-1-exception-q1-dual.txt`](../computations/session-localcoh-origin-family-1-exception-q1-dual.txt),
[`session-localcoh-origin-family-1-exception-q1-evaluations.txt`](../computations/session-localcoh-origin-family-1-exception-q1-evaluations.txt),
and
[`session_localcoh_q1_dual_audit_2026_10_07.json`](../computations/session_localcoh_q1_dual_audit_2026_10_07.json).
The default verifier is independent of Macaulay2 and SymPy, so the
certificate remains directly checkable without reproducing the module command.


---

## q13-exception

# Exact closure of the first endpoint family's degree-thirteen exception

Date: 2026-10-07. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top `h=t`, and the first rational endpoint family classified
in the independent endpoint audit. This note does not address another
endpoint family, a nonendpoint top zero, or the universal STCI problem.

## Result and proof certificate

**PROVED under the audited actual multiplication tensor and coordinate
bases:** every member of the complete affine line of quartic lower
corrections at every geometric root of

```text
Q13(k)=729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
       +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
       -1210068k^2-966908k-379834
```

fails the target-`u` multiplication incidence. This closes all thirteen
parameter points of this exceptional locus for every lower parameter
`lambda`.

The defining polynomial is irreducible over `QQ`. Its monic reduction
modulo 53, written in ascending coefficient order, is

```text
[15,43,6,38,30,45,19,21,8,22,31,2,14,1].
```

The standalone verifier proves irreducibility by exact modular polynomial
arithmetic: `k^(53^13)=k (mod f)` and `gcd(f,k^53-k)=1`. Since the degree
13 is prime, these are the full Rabin irreducibility conditions. Thus
`K=QQ[k]/Q13` is a field, and its thirteen characteristic-zero embeddings
account for every geometric root.

The saved rational seed has lower corrections
`alpha=a*(k)+lambda*k0`. Every seed denominator was inverted exactly
in `K`, before the actual 74-by-18 multiplier matrix was exported.
Macaulay2 computed the polynomial left-kernel module over `K[lambda]`.
Its target-evaluation ideal is `(1)`. The resulting exact left dual has
26 nonzero entries, degree at most two in `lambda`, and entry 72 equal
to one.

The standalone verifier reads the actual 74-by-542 tensor and checks
both target columns against `e72,e73`. It independently verifies all
eighteen identities `n^T L(alpha)=0`, coefficient by coefficient in
`lambda`, and verifies `n^T u=1`. These identities, rather than the
module command or a generic rank calculation, prove exclusion for
every `lambda` and every embedding of `K`.

The verifier also checks the 32-by-30 actual pure-top map has rank 29,
the saved kernel direction is nonzero, and the coefficient of `lambda`
in `alpha` is exactly this kernel direction. Its constant seed and
direction coefficients are independently derived from the saved rational
expressions using an arithmetic-only parser and rational multiplication
matrices in `K`; this replay uses neither SymPy nor Macaulay2. In all
32 top coordinates it checks
`top(alpha)=t*p^i*r^(3-i)`. Consequently the affine line is the entire
lower-correction fibre, rather than a sampled collection of lifts. A
fixed four-by-four Sylvester determinant checks the homogeneous quadratic
pair is primitive, including leading-coefficient specializations.

All source inputs, including the tensor, bases, top map, rational seed,
complete dual, evaluation output, module input and generator, are bound
to the coefficient certificate by SHA256. The certificate SHA256 is

```text
c484ca17078ecfd2e30eb8d3f76e57c313f25f3684c34db286deb047429db65c
```

## Reproduction and evidence

Generate the reduced actual module:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/generate_session_localcoh_q13_module_2026_10_07.py
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-1-exception-q13.m2
```

Regenerate the coefficient certificate from the saved exact dual, then
verify it independently with an ordinary Python:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_q13_dual_2026_10_07.py --regenerate
python3 research/computations/verify_session_localcoh_q13_dual_2026_10_07.py
```

The generator ran in tool session `38119`, the single M2 computation
in session `88486`, and certificate regeneration in session `86666`.
All completed with exit code zero. The initial standard-library replay
in session `27168` also passed. A stronger direct-rational-source replay
was performed subsequently; its terminal status is recorded below.
There was no overlapping copy of the Q13 module computation.

Evidence files:

- [`generate_session_localcoh_q13_module_2026_10_07.py`](../computations/generate_session_localcoh_q13_module_2026_10_07.py)
- [`session-localcoh-origin-family-1-exception-q13.m2`](../computations/session-localcoh-origin-family-1-exception-q13.m2)
- [`session-localcoh-origin-family-1-exception-q13-dual.txt`](../computations/session-localcoh-origin-family-1-exception-q13-dual.txt)
- [`session-localcoh-origin-family-1-exception-q13-evaluations.txt`](../computations/session-localcoh-origin-family-1-exception-q13-evaluations.txt)
- [`session_localcoh_q13_dual_audit_2026_10_07.json`](../computations/session_localcoh_q13_dual_audit_2026_10_07.json)
- [`verify_session_localcoh_q13_dual_2026_10_07.py`](../computations/verify_session_localcoh_q13_dual_2026_10_07.py)
- [`session-localcoh-origin-family-1-exception-q13-verification.out`](../computations/session-localcoh-origin-family-1-exception-q13-verification.out)

The separately recorded Q1 and Q3 closures, together with this Q13
closure and the previous quadratic closure, remove the first family's
available generic dual's remaining primitive parameter exceptions after
those certificates are accepted. The other three endpoint families and
nonendpoint top-zero strata retain their prior unresolved scope.


---

## q3-exception

# Exact closure of the first endpoint family's Q3 exception

Date: 2026-10-07. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top `h=t`, and the first rational endpoint family from the
independently audited endpoint classification. No assertion here concerns
a nonendpoint top zero, another endpoint family, or the global STCI question.

## Result

**PROVED under the audited actual tensor and coordinate bases:** every
member of the complete affine line of quartic ancestors at every geometric
root of

```text
Q3(k)=13k^4+26k^3+34k^2+6k-7
```

fails the target-`u` multiplication incidence. Thus this quartic factor
can be removed from the first family's denominator-exception list. Together
with the previously closed quadratic factor and Q1, the only remaining
exceptions to that family's available generic dual at this checkpoint are
the thirteen roots of the recorded degree-thirteen factor, each with its
complete affine lower-correction fibre. These thirteen points remain
exceptions to the available certificate, rather than evidence for an ancestor.

## Exact calculation and independent verification

The defining polynomial is irreducible over `QQ`: its reduction modulo 17,
made monic, is

```text
f(k)=k^4+2k^3+7k+6 in F_17[k].
```

The standard-library verifier checks `k^(17^4)=k (mod f)` and
`gcd(f,k^(17^2)-k)=1` using modular polynomial arithmetic. This is the
degree-four irreducibility test, and also ensures that
`K=QQ[k]/Q3` is a field. All seed denominators were inverted exactly in
this field before exporting the module.

The retained rational seed and its kernel direction give
`alpha=a*(k)+lambda*k0`. From the actual 74-by-542 tensor, the generator
constructs all entries of the 74-by-18 multiplier matrix `L(alpha)`.
Macaulay2 computes the full polynomial left-kernel module over `K[lambda]`.
Its target evaluation ideal is `(1)`. A resulting exact left dual `n`
has 26 nonzero entries, degree at most one in `lambda`, and entry 72 equal
to one.

The subsequent verifier uses only exact rational arithmetic and

```text
k^4=-2k^3-(34/13)k^2-(6/13)k+7/13.
```

It checks all eighteen identities `n^T L(alpha)=0` coefficient by coefficient
in `lambda`, and `n^T u=1`, with `u=e72` checked against the tensor's actual
target column. Therefore `u` is outside the image for every `lambda`.
Because Q3 is irreducible and characteristic zero is separable, this exact
field identity applies through all four embeddings into an algebraic closure.

The verifier also checks the 32-by-30 actual pure-top map has rank 29,
the nonzero coefficient of `lambda` is exactly its saved kernel vector,
and the top of every `alpha` is `t*p^i*r^(3-i)` in all 32 coordinates.
This confirms that the entire affine fibre of lower corrections has been
tested. A fixed four-by-four Sylvester determinant verifies the homogeneous
quadratic direction is primitive, including possible leading-coefficient
specializations. Every input is bound to the coefficient certificate by SHA256.

## Reproduction and terminal process status

Generate the reduced module input:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/generate_session_localcoh_q3_module_2026_10_07.py
```

Compute the full polynomial dual:

```sh
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-1-exception-q3.m2
```

Regenerate and independently verify the coefficient certificate:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_q3_dual_2026_10_07.py --regenerate
python3 research/computations/verify_session_localcoh_q3_dual_2026_10_07.py
```

The generator ran in tool session `99512`, the M2 computation in session
`34782`, and certificate regeneration in session `88461`; all three
completed with exit code zero. M2 printed matrix readiness, completed its
polynomial kernel, saved the unit evaluation ideal, and saved the dual.
No computation from this branch remains running.

The complete evidence is retained in
[`session-localcoh-origin-family-1-exception-q3.m2`](../computations/session-localcoh-origin-family-1-exception-q3.m2),
[`session-localcoh-origin-family-1-exception-q3-dual.txt`](../computations/session-localcoh-origin-family-1-exception-q3-dual.txt),
[`session-localcoh-origin-family-1-exception-q3-evaluations.txt`](../computations/session-localcoh-origin-family-1-exception-q3-evaluations.txt),
and
[`session_localcoh_q3_dual_audit_2026_10_07.json`](../computations/session_localcoh_q3_dual_audit_2026_10_07.json).
The default verifier is independent of Macaulay2 and SymPy, so the
certificate remains directly checkable without reproducing the module command.
