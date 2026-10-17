# Full-conductor power descent: an independent algebra audit

Date: 2026-10-11. Owner: `power_descent_algebra_audit`, child of
`oct11_quintic_power_descent`.

Status: the algebraic statements below are **PROVED HERE** with explicit
proofs. The application to the degree-five A4 del Pezzo lane uses the
recorded geometric inputs in the
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
particularly the actual conductor, purity of the normalization quotient,
and `div(Q)=5c`. This note does not assert that any projection satisfies
the resulting power criterion, or exclude every quintic carrier.

## 1. Actual membership is stronger than a tensor equalizer

Let `A` be a Noetherian algebra over a characteristic-zero field, and let
`A ⊂ B` be a finite extension. In the normalization application A is an
integral domain and B its finite normalization. Let

    I = {a ∈ A : aB ⊂ A}, R=A/I, T=B/I.

The conductor I is an ideal in both A and B, and the injection R→T gives
the exact identity

    A = B ×_T R.

Indeed, if b modulo I belongs to R, choose a in A representing it;
then b−a belongs to I⊂A. Consequently

    q^k ∈ A  ⇔  (q mod I)^k ∈ R.                 (1)

No reducedness, normality of R or T, flatness, or separability of the
conductor map is needed. Fiber products and their compatibility with
localization are also recorded in
[Stacks, Section 15.5](https://stacks.math.columbia.edu/tag/08KG).

If q is a unit in T, write q1=q⊗1 and q2=1⊗q in E=T⊗_R T. Descent of
q^k implies that u=q1/q2 satisfies u^k=1 in the entire possibly nonreduced
ring E. Over an algebraically closed field, E decomposes by the mutually
orthogonal idempotents

    e_ζ = (1/k) Σ_{j=0}^{k−1} ζ^(−j) u^j,  ζ^k=1,

and on the e_ζ component one has the exact identity q1=ζq2. Thus there
is no additional nilpotent error in this necessary root-of-unity identity.

The converse tensor implication is false without further descent
hypotheses. Here is an explicit finite normalization counterexample.

    A=k[t^3,t^4] ⊂ B=k[t], I=t^6B,
    R=span_k{1,t^3,t^4} ⊂ T=k[t]/(t^6), q=1+t^5.

The conductor follows from the semigroup `<3,4>`: every integer at least
six occurs, but five does not. The element q is a unit in T. In the
tensor product T⊗_R T, with x=t⊗1 and y=1⊗t, the relations x^3=y^3 and
x^4=y^4 imply

    x^5−y^5=(x+y)(x^4−y^4)−xy(x^3−y^3)=0.

Hence q⊗1=1⊗q, and the same is true of every power. Nevertheless

    q^k = 1+k t^5  in T,

which is not in R for any positive integer k in characteristic zero.
An exact tensor equalizer test, even on the unit locus, therefore cannot
replace the actual R-subspace membership test (1).

## 2. Powering cannot repair unit nilpotent jets

Assume more generally that `R ⊂ T` is a finite extension of Noetherian
Q-algebras, and q∈T is a unit. Write Rred and Tred for their reductions.
The induced map Rred→Tred is injective: a member of R which is nilpotent
in T is already nilpotent in R.

**Unit jet lemma.** If qred belongs to Rred, then

    q^k ∈ R for one positive k  ⇔  q ∈ R.        (2)

Proof. Integrality shows that qred is a unit in Rred: an element of Rred
which becomes a unit in the integral extension Tred cannot lie in a
maximal ideal, by lying over. Choose a lift r∈R of qred. The nilradical
of R is nilpotent, so r is a unit of R. Now q/r=1+n with n in the
nilradical N of T; N is nilpotent. Finite polynomials define

    log(1+n)=n−n^2/2+n^3/3−...,
    exp(z)=1+z+z^2/2!+...,

on N, and they are inverse. If q^k∈R, then (q/r)^k∈R and

    k log(q/r)=log((q/r)^k) ∈ R.

Since k is invertible, log(q/r)∈R∩N. Taking its finite exponential gives
q/r∈R and hence q∈R. The reverse implication is immediate. This proof
retains every nilpotent layer of T; it is not a first-jet argument.

There is a useful exact reformulation. For a unit q define

    Ered={n∈Z : qred^n ∈ Rred^×}.

This is a subgroup of Z. If Ered={0}, no positive full power descends.
Otherwise write Ered=dZ with d≥1. Then the set of positive full
descending powers is either empty or precisely

    {d,2d,3d,...}.                               (3)

Indeed, a successful k has k=dm. Applying (2) to the unit q^d shows
that (q^d)^m∈R forces q^d∈R. Conversely its multiples then descend.
Thus the nilpotent structure can invalidate every reduced candidate,
but cannot force a larger multiple of the reduced minimum d to become
the first successful power.

The unit condition is essential. For A=k[t^2,t^3]⊂B=k[t], q=t does not
descend whereas every q^k with k≥2 does. Its conductor residue is
nilpotent and is not a unit.

## 3. Reduced generic phases and the unibranch bound

At a generic conductor point the actual R is Artinian local. Put
K=Rred and write

    Tred=Π_j L_j,

where each L_j/K is a finite field extension. K contains the algebraically
closed characteristic-zero ground field. For a unit tuple α=(α_j), take
all its values under all K-embeddings L_j→Kbar. A positive reduced power
descends precisely when every ratio between these finitely many geometric
values is a root of unity. If that holds, the least reduced exponent d
is the least common multiple of the orders of the ratios to one reference
value. Their common d-th power is Galois invariant, hence belongs to K.

If Tred consists of one field L, this gives a bound

    d=[K(α):K] ≤ [L:K].                          (4)

For completeness, if α^m∈K, then K(α) contains every root ζα of
X^m−α^m because all m-th roots of unity are in K. This polynomial is
separable, so K(α)/K is Galois with a cyclic group of order e. Its image
is the unique order-e subgroup of μ_m; thus α^e is fixed, and minimality
gives d=e.

No bound by the number of geometric branches exists in the split case.
For any root of unity ζ of order m, let

    A={p(t)∈k[t] : p(0)=p(1)}, B=k[t],
    I=t(t−1)B, R=k, T=k×k,
    q=1+(ζ−1)t.

This is an integral finite-type domain with finite normalization B:
t is integral over A via t^2−t−t(t−1)=0, and A=k+t(t−1)k[t]. The
conductor formula is exact because interpolation makes arbitrary pairs
of endpoint values in B. The residue of q is the unit (1,ζ), and

    q^k ∈ A  ⇔  ζ^k=1  ⇔  m divides k.

The reduced conductor has only two branches, while m is unbounded.
In a genuinely degree-two single-field generic conductor, however,
(4) bounds the candidate exponent by two. That degree-two hypothesis
must be established for the actual projection, not assumed from an
average conductor-degree calculation.

There is also a pointwise subintegral statement. Suppose q^k∈A and q
is a unit in B. If over a prime p of A all geometric residue values of
q coincide, then q belongs to A_p. To prove it, set C=A[q]. The fiber
C⊗_Aκ(p) is a quotient of κ(p)[z]/(z^k−q^k), a reduced separable
algebra because q^k is a unit. The common residue value is in κ(p)
in characteristic zero, so this fiber is κ(p). Nakayama applied to
(C/A)_p now gives C_p=A_p. The equal-residue condition is automatic
where B→A is subintegral. It fails in the split root-of-unity example.
Thus power descent forces descent of the section itself on a subintegral
unit locus, but not on every unit locus of a normalization.

## 4. Purity converts generic full membership into global descent

Let ν:S→X be a finite birational normalization of an integral surface,
and let

    M=ν_*O_S/O_X.

Assume M is pure of dimension one: it has no nonzero coherent subsheaf
supported on finitely many points. If L is invertible on X, then a global
section s of ν^*L descends to a section of L if and only if its germ
belongs to L at every generic point of Supp(M).

Proof. Its image σ in M⊗L is a global section. If its generic germs
vanish, the coherent subsheaf generated locally by σ has finite support.
Purity makes this subsheaf zero, so σ=0 and s descends. Necessity follows
from the defining exact sequence. For a one-dimensional Cohen–Macaulay
module, purity follows either from a nonzerodivisor killing no finite
length submodule, or from the absence of embedded associated primes;
the latter is [Stacks, Lemma 10.103.7](https://stacks.math.columbia.edu/tag/00N2).

It is essential that these generic tests use the full Artinian conductor
algebras, rather than only their residue fields. Purity removes an extra
obstruction supported at finitely many points only after the entire
generic obstruction has vanished. The example in section 1 fails this
full generic test.

## 5. Exact application to the quintic A4 lane

The recorded quintic inputs are

    M=ω_Γ(−H), Γ pure Cohen–Macaulay of dimension one,
    Q∈H0(S,4H), div_S(Q)=5c,
    C0 generically regular on X.

The canonical module of the Cohen–Macaulay curve Γ is maximal
Cohen–Macaulay, so M is pure. Since c is not a conductor component,
Q, after trivializing O_X(4H), is a unit at every generic conductor point.
For each such point η form the actual rings

    Rη=O_X,η / Iη  ⊂  Tη=(ν_*O_S)η / Iη,

and let dη be the minimum reduced exponent in section 3, if it exists.
Then an actual power of Q descends if and only if:

1. Every generic conductor point has a finite dη.
2. The full, possibly nonreduced membership test Q^dη ∈ Rη passes at
   every such point, in a local trivialization.

If these conditions hold, D=lcm_η(dη) is the least positive global
descending exponent, and all global descending exponents are its positive
multiples. Proof: (3) supplies the exact local exponent groups; purity
supplies sufficiency and prevents any additional isolated obstruction.

Multiplying a local trivialization by a unit from O_X,η multiplies Q by
a unit of Rη. This changes none of these exponent groups or membership
conditions. The argument concerns sections of the pullback of an actual
downstairs line bundle; a line bundle merely defined upstairs cannot be
treated this way.

For a quintic hypersurface X⊂P3, every section of O_X(4D) lifts to an
ambient homogeneous polynomial: the hypersurface sequence and
H1(P3,O(4D−5))=0 give surjectivity. If Q^D descends, its normalized divisor
is exactly 5D c, and finite surjectivity of ν shows that the resulting
ambient equation cuts X set-theoretically down to C0. Conversely the
recorded quintic structural theorem says every hypothetical mate pulls
back to a scalar Q^k. Hence these generic full-conductor tests are an
exact mate-existence criterion within this already reduced quintic lane.

This is a structural reduction, not a parameter-space solution. In
particular, the split reduced phases can still have arbitrary root-of-unity
orders as the projection varies. What is removed is a separate search over
ever larger multiples to repair generic nilpotent jets, or a search for
extra isolated descent obstructions after full generic membership succeeds.

## 6. Evidence and continuation boundary

The proofs of (1)–(4), the tensor counterexample, the pointwise statement,
and the purity criterion are direct algebraic arguments in this note;
no finite symbolic run is used as a substitute for their quantifiers.
The imported geometric inputs remain those of the linked quintic frontier.
The finite-conductor nilpotent logarithm uses characteristic zero, and is
not transferred to positive characteristic.

The next actual task is to construct Rη⊂Tη and the residue of Q for the
four-parameter projection family, with all nonreduced generic strata
retained. For a single-field component, (4) may bound its candidate power;
for split components, root-of-unity phases and their full jet compatibility
must both be examined. No projection is excluded by this note alone.
