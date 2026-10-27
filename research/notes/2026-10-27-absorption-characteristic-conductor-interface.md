# Residual absorption through conductor units and semi-invariant powers

Date: 2026-10-27. Author: characteristic-conductor research lane, with a
targeted independent literature/audit contribution linked below.
**Status:** independently reviewed provisional synthesis, exact local propositions and conditional
construction mechanisms; see the [audit](2026-10-27-absorption-characteristic-conductor-audit.md). No canonical promotion,
no degree-by-degree case program, and no construction or exclusion of an
unrestricted characteristic-zero STCI for the fixed quartic.

The fixed problem is C0=[s^4:s^3t:st^3:t^4] in P3. Intersections containing
C0 may have residual curves. The question here is what can transfer their
degree onto C0 beyond the already known binomial/Frobenius examples, and
what exact global data such a construction must supply.

## 1. Start from what the repository already proves

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), the
[containing-intersections vision](2026-10-27-containing-intersections-research-vision.md),
and the smallest conductor records.

[R-0003](../results/fixed_carrier_conductor_criterion.md) gives the exact
fixed-carrier test in arbitrary characteristic. For a fixed integral
Cohen--Macaulay projective carrier X, finite normalization nu:S->X,
polarization H=nu^*O_X(1), and full reduced inverse support
W=Gamma1 union ... union Gammas with no isolated extra points, use the
relation lattice

    Lambda=ker[Z^(s+1) -> Cl(S)],
    (n1,...,ns,d) |-> sum n_i[Gamma_i]-d[H].

The actual full-conductor unit classes at the finitely many generic
conductor curves away from C define phi:Lambda->G. A mate exists exactly
when some vector with every n_i>0 maps to a torsion element of G. The
result already handles arbitrary mate degrees through one lattice/cone
question. Its [source proof, sections 1 and 8](2026-10-13-generalization-conductor-theorem.md)
already proves the following comparison; it is **inherited**, not a new
theorem of this note:

* In characteristic zero, eventual unit descent requires torsion of the
  reduced phase **and zero full nilpotent logarithmic defect**.
* In characteristic p, torsion of the reduced phase suffices; an additional
  p-power kills the finite nilpotent defect.

[R-0004](../results/projection_phase_reduction.md) already makes the
zero-logarithm locus and torus phase test algebraic in its specified
Cartier-singleton projection families. Their actual admissible phase
images remain uncomputed. The present note does not repeat that reduction
or announce its missing computation as completed.

The [all-mu_q construction](2026-10-27-positive-characteristic-construction-interface.md)
and canonical R-0020, R-0021 and R-0031 explain one actual finite-flat
residual/thickness family. R-0012 remains the obstruction for one specified
embedded characteristic-two Z4 over two specified unramified DVRs; it does
not obstruct all characteristic-zero alternatives.

## 2. An exact all-order limitation of Frobenius unit descent

The following family isolates an important difference between a finite
conductor and an infinite formal neighborhood. It is a local proposition,
not an asserted projective carrier of C0.

**Proposition.** Let K be any field and N>=2. Put

    B=K[[t]],  A_N=K+t^N K[[t]],  u=1+t.

The conductor is t^N B. In characteristic p>0,

    u^m belongs to A_N  iff  p^{v_p(m)}>=N.

Thus the least positive descending exponent is the least p-power at least
N. In characteristic zero no positive power of u belongs to A_N.

**Proof.** Every power series of order at least N belongs to A_N, and
anything with nonzero constant term fails to be in the conductor: multiply
it by t and the resulting first coefficient lies outside A_N. Hence the
conductor has the claimed value. In positive characteristic write
m=p^e M, p not dividing M. Then

    (1+t)^m=(1+t^{p^e})^M
            =1+M t^{p^e}+higher terms.

The first nonconstant term has order exactly p^e, proving both directions.
In characteristic zero the first term after one is m*t, which never
vanishes. This is a proof for all N,m,p, with no finite enumeration. The
Artinian conductor inclusion is precisely K subset K[t]/(t^N), so the
example concerns the full conductor units of a genuine one-branch local
domain. A_N is the complete semigroup ring
K[[t^N,t^(N+1),...,t^(2N-1)]].

Two deductions are useful for construction:

1. The same integral finite-algebra datum Z subset Z[t]/(t^N), u=1+t,
   has eventual descent in every positive-characteristic fiber and none
   over Q. Positive-characteristic witnesses alone do not supply a
   characteristic-zero descending power; their degrees can vary with p.
2. Even in characteristic p, u has infinite order in K[[t]]^*. Modulo
   every t^N it is killed by a sufficiently large p-power, but no single
   exponent kills all truncations. Therefore the quantifiers
   "for each finite level, some exponent works" and "one exponent works
   at every level" cannot be interchanged.

This is compatible with actual positive-characteristic STCI constructions:
the conductor on a fixed finite-type carrier is a **finite** algebra at
its generic points, so one finite p-power suffices there. It warns against
claiming a full formal homogeneous pair merely from unrelated finite-level
Frobenius repairs.

The formal-group calculation is explicit. Principal units have the
multiplicative formal law X+Y+XY; multiplication by m has series (1+T)^m-1. Characteristic-zero
logarithm conjugates multiplication by m to the invertible linear map
z->mz. In characteristic p, multiplication by p^e has series T^{p^e}. Finite nilpotence kills the
latter, while an infinite formal parameter does not. Higher principal-unit
groups in characteristic p need not be direct products of additive groups;
their finite filtrations, rather than a false splitting, explain the
possibly larger p-power exponent.

## 3. Characteristic zero can use semi-invariant powers

Frobenius is not the only way to obtain a pure supported power. There is
an elementary, characteristic-independent **conditional construction**.
Let a finite group act on a normal finitely generated k-domain B, with invariant ring A=B^G, and
let f be a nonzero semi-invariant:

    g(f)=chi(g)*f,

where chi is a character of finite order r. Then f^r belongs to A, and
its zero support on Spec A is exactly the image of V(f) under the finite
quotient. Indeed invariance is immediate, and finite surjectivity gives
the support assertion. A nonzero semi-invariant does not have to split
into separate residual divisors upstairs. Its stable divisor may descend
only after this finite power.

This elementary lemma belongs to standard invariant theory. In a global
projective application one must additionally supply the line-bundle
linearization and show the invariant power is a section of an **actual
ambient twist**, on a carrier which embeds as the required P3 hypersurface.
An arbitrary invariant ring or weighted quotient does not supply those
conditions.

A classical benchmark is the twisted cubic T=[s^3:s^2t:st^2:t^3], a
different curve from C0. It is supported by the proper pair

    Q=x0*x2-x1^2,
    G=x2^3-2*x1*x2*x3+x0*x3^2.

The mixed coefficient 2 is retained. With A=x0*x3-x1*x2 and
B=x1*x3-x2^2 one has actual homogeneous identities

    x0*G=A^2+x2^2*Q,   x2*G=B^2+x3^2*Q.

Thus the square is corrected by a multiple of the carrier equation so it
glues to the global cubic G; the reduced support is T and the cycle is
2[T]. On the cone's vertex chart x3=1, take
x0=u^2,x1=uv,x2=v^2. The sign involution sends u-v^3 to its negative,
and G=(u-v^3)^2 is invariant. This is a cyclic semi-invariant power in
characteristic zero, not inseparable sheet coalescence.

The corresponding divisor relation is 2[T]=3[H] in Cl(Q), with T
non-Cartier of local index two at the vertex. The
[independent benchmark/literature audit](2026-10-27-char0-torsion-benchmark-audit.md)
records primary sources for these classical equations and the exact
scope of the interpretation. They are not a new STCI example.

For C0 this benchmark directs a **construction question**: can an actual
higher-degree carrier realize the fixed C0 as a suitable semi-invariant
divisor, with a positive global Weil-class relation and compatible
homogeneous correction? The benchmark's index-two geometry does not
transfer to C0. [R-0035](../results/normal_carrier_bounded_index_exclusion.md)
already excludes the specified normal-carrier regime in which all actual
on-curve indices are at most four. Higher-index geometry and its global
equations remain an explicit missing bridge, rather than a new list of
mate-degree cases.

## 4. A different positive-characteristic replacement: cancel defects

On a nonnormal carrier, a construction can exploit **several divisor
directions at once**, rather than taking more powers of one section.
This is a constructive corollary of R-0003, not a new general theorem.

Suppose v1,v2 in Lambda have nonnegative inverse-branch multiplicities,
and v1+v2 has strictly positive multiplicity on every component of W.
Let Q1,Q2 be the corresponding regular upstairs sections. Assume their
reduced conductor classes are torsion and their characteristic-zero
logarithmic defects satisfy

    delta(Q1)+delta(Q2)=0

at every off-C generic conductor component. Then the conductor class of
Q1*Q2 is torsion. R-0003 gives a descending power of this product, with
exactly the full image support C. Neither Q1 nor Q2 need have an eventually
descending power individually.

The cancellation is literal local algebra. In characteristic zero take

    A=K,  B=K[epsilon]/(epsilon^2),
    u=1+epsilon,  v=1-epsilon.

No positive power of either unit lies in A, but uv=1 does. The logarithmic
defects are epsilon and -epsilon. This is a way to satisfy conductor
descent without Frobenius, provided the two units arise from compatible
global divisor sections on the **same actual carrier**.

That proviso is substantial. On a normal integral projective S, two
sections of the same line bundle with the same divisor differ by a scalar:
their ratio is a global unit, hence belongs to k^*. A scalar does not
change their conductor class. One cannot freely replace Q by a preferred
local torsion lift while preserving its global zero divisor. On a single
primitive divisor ray, repeated powers only multiply a nonzero
logarithmic defect and cannot remove it in characteristic zero.
Different inverse-branch multiplicity directions provide the possible
cancellation freedom. Constructing those directions and their actual
conductor classes is the missing global step.

## 5. Known geometric restrictions prevent two tempting shortcuts

The primary [Hartshorne--Polini paper](https://arxiv.org/html/1301.3222)
was checked in full HTML and PDF by the targeted reviewer. Three precise
boundaries matter here:

* Proposition 7.1 translates fixed-carrier STCI to positive APic
  proportionality when the curve meets the singular locus finitely.
* Lemma 7.6 makes Pic(X)/Z[H] torsion-free for characteristic-zero
  surfaces in P3. A torsion construction must retain non-Cartier/APic
  or conductor information; arbitrary Cartier Picard torsion is not a
  substitute.
* Proposition 7.3 and Corollary 7.4 impose singleton normalization fibers
  at singular points of a smooth supported curve; for ordinary surfaces
  the intersection with the singular locus occurs only at pinch points.

An elementary pinching control explains the last issue. Normalize
X=(a nodal rational curve) times P1 by S=P1 times P1, identifying two
disjoint ruling fibers pointwise. If an ample smooth Cartier curve c in
S mapped isomorphically to a smooth C with full inverse support exactly
c, ampleness would make c meet one ruling fiber. Full inverse support
would force its distinct paired point on the other fiber into c too,
contradicting injectivity. This is an abstract projective pinching example,
not a P3 carrier. Merely prescribing a root-of-unity torus phase therefore
does not preserve the fixed smooth marked curve or full inverse support.
The benchmark audit records this proof and the stronger known theorem.

## 6. Precise constructive target and result of this pass

There are two coherent characteristic-zero mechanisms to investigate:

1. **Semi-invariant/Weil-class descent on an actual normal carrier.**
   Supply the carrier, local character data, positive global divisor
   relation, and a homogeneous corrected power. The twisted cubic proves
   that this can succeed in characteristic zero; for C0 the admissible
   higher-index global realization is unresolved.
2. **Cancellation in the positive full-conductor relation cone.**
   Supply an actual normalization/projection with the entire inverse
   support, then find one fully positive relation whose combined phase
   is torsion and combined logarithmic defect vanishes. Products can cancel
   defects that powers of one section cannot. The unresolved task is to
   realize such compatible global directions for C0, not to enumerate
   larger mate exponents.

The exact local A_N proposition establishes why characteristic-p success
at every finite level does not automatically supply the characteristic-zero
construction or a uniform full formal exponent. The semi-invariant lemma
and classical corrected-square benchmark establish a genuine alternative
to inseparable collapse. The cancellation corollary identifies additional
freedom deliberately lost by a singleton-ray ansatz. None supplies an
actual new C0 carrier, and no terminal residual-absorption claim is made.

Independent review should test the A_N exponent criterion, the invariant
support lemma, the positivity and global-section requirements in defect
cancellation, and the literal scopes of R-0003, R-0004 and R-0035. The
inherited all-prime construction and accepted conductor proofs were not
re-run. No navigation, canonical record, or Git state was edited.
