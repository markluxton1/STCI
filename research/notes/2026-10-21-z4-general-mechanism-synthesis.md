# Z4 arithmetic mechanism and characteristic-zero STCI: synthesis

Date: 2026-10-21. Status: **new research evidence, independently reviewed in
the companion audit; unpromoted**. No canonical theorem record is modified.
Base: `research/z4-arithmetic-obstruction-consolidated-2026-10-21`, fetched
at `c1af2e466c4b2251622ee70116613a3b2afb1391`.

The two investigations reached definite outcomes: a defect-sensitive
necessary condition for generically curvilinear STCI presentations, an
embedded obstruction hierarchy, and counterexamples to the unrestricted
bridges suggested by the arithmetic analogy. They do not exclude arbitrary
characteristic-zero STCI presentations of the fixed rational quartic C0.

## 1. New characteristic-zero restriction

Let C be a smooth curve regularly embedded in a smooth threefold, with
ideal I, and let J define a supported complete intersection whose generic
transverse algebra is curvilinear of length m≥3. Saturate its first-normal
image as

    (J+I²)/I² = M(−D) ⊂ M ⊂ E=I/I²,
    q:E→L=E/M,

where D is effective and M,L are line bundles. Put H=M∨⊗L².
The [characteristic-zero report](2026-10-21-z4-characteristic-zero-stci-consequences.md)
proves the necessary condition

    image of o_X(q) in H¹(C,H(D)) is zero.               (A)

The proof uses the image of J inside the canonical extension module:
it projects isomorphically to M(−D) and therefore splits the pulled-back
extension. It does not require an everywhere primitive triple inside the
complete intersection. Equivalently the obstruction must be supplied by
principal parts supported on the *actual* first-normal defect divisor.

For the distinguished marked quotient of C0 with L=O(−6), M=O(−8),
and o=−6[u⁻²], condition (A) implies:

- deg D≥2;
- if deg D=2, a defining binary quadratic for D has zero st coefficient
  in the fixed marking;
- if deg D≥3, this first obstruction alone imposes no further condition.

These statements include nonreduced effective divisors. They concern an
actual pair inducing this q. Other quotients of the same degree can have
zero obstruction: the audited polynomial family has the surjective example
a=h=0, b=d=1. More generally, for the accepted conormal E=O(−7)²,
L=O(ε−7) gives H=O(3ε−7), so the first obstruction group vanishes
for ε≥2. There is no unrestricted new exclusion of surface degrees.

The structural limitation is also proved. A supported lci may be
curvilinear generically and fail to contain any globally primitive triple.
The family J=(x²,y²+t x), free of rank four over k[t], has generic algebra
k(t)[y]/(y⁴) and special algebra k[x,y]/(x²,y²). The latter has no
curvilinear length-three quotient. An ambient triple extending a ribbon
can exist while failing to be contained in J. Thus vanishing of o_X(q)
is weaker than compatibility with a specified complete intersection.

## 2. Does divided Frobenius produce the intrinsic class?

No unconditional identification is proved. The
[intrinsic arithmetic report](2026-10-21-z4-intrinsic-divided-power-mechanism.md)
does recover the accepted full class −6[u⁻²] and the divided variation

    λ(α,β,γ)=γ[u⁻¹]+[u⁻²]+α[u⁻³],
    D(α,β,γ)=γ[u⁻¹]+α[u⁻³].

This uses the full embedded Yoneda extension and the previously audited
Laurent polynomials. It does not isolate a normal-coordinate summand or
derive the full class from a binomial coefficient. The nonzero image in
coker D is intrinsic for the specified marked integral problem.

There is a genuine conditional comparison, with an explicit source and
target. If two quadratic neighborhoods are locally isomorphic over the
same marked first neighborhood A₁ and B=Sym²E, their difference is a
class β in H¹(Der_S(A₁,B)). The canonical sheaf map

    ρ_q:Der_S(A₁,Sym²E)→Hom(M,L²)

restricts a derivation to M and projects by Sym²q. It carries β to
the difference of the Yoneda obstruction classes. The
[quadratic-gluing comparison](2026-10-21-z4-quadratic-gluing-comparison.md)
proves the statement and its coordinate functoriality. The missing arithmetic
bridge is a natural derivation-valued gluing class carrying the full normal
and moving-base data. A divided-power polynomial does not furnish it.

## 3. Strongest general characteristic-p conclusion

For every fixed embedded primitive n-fold J_n, n≥2, with inherited q,
there is a canonical exact sequence

    0→L^n→J_n/(I J_n+I^(n+1))→M→0.                    (B)

Its splittings classify compatible primitive (n+1)-fold embedded ideals.
Thus the obstruction is in H¹(M∨⊗L^n), and when it vanishes the choices
form a torsor under H⁰(M∨⊗L^n). This works in arbitrary characteristic
under the regular-immersion and primitive-stage hypotheses. The fixed
stage J_n and the ambient neighborhood are essential data.

The universal p^r binomial arithmetic predicts the least normal order of
its own cross-effect, p^(r−1) when one argument is a unit and the other
is normal. It does not predict the first nonzero class in hierarchy (B).
Explicit triangular gluing gives the same conormal bundle and the same
lower primitive stages but an arbitrary nonzero next-stage class; the split
vector-bundle model admits every stage even though the arithmetic polynomial
is nonzero. Varying an integral gluing coefficient πc gives identical full
special ambient fibers but different divided obstruction classes.

The relative persistent-cokernel theorem is correct when the obstruction
module is locally free, reduction and cohomology comparisons apply, and the
leading section on the marked lift torsor is affine-linear with difference
map D. At higher divided orders, affine linearity is additional content:
the example o(q)=4+q², q=2t gives o/4=1+t² modulo two, with zero ordinary
differential and a cancelling lift. A cokernel of the ordinary differential
cannot replace the nonlinear obstruction image in general.

## 4. Specialization boundary and status

Support-preserving spreading is possible after localization, using finite
ideal containments I^N⊂J⊂I and generic flatness. This produces an open set
of good specializations; it need not include residue characteristic two.
It forces neither the marked quotient nor the prescribed Z4 integral
deformation class. For C0, the accepted lower-carrier exclusions and Bézout
give m=de/4≥9, whereas the prescribed Z4 has m=4. Flat direct specialization
to that whole quadruple is therefore incompatible even with the degree.
Extracting a separate quadruple would be a further theorem.

| Conclusion | Status and boundary |
| --- | --- |
| Defect-twisted necessary condition (A) | Proved here; independently reconstructed; generic curvilinear branch, m≥3 |
| Distinguished q0 defect bound | Proved corollary, with fixed marking; no classification of all quotients |
| Generic curvilinear lci need not contain a primitive triple | Explicit counterexample; no assertion that it occurs on C0 |
| Primitive-stage obstruction hierarchy (B) | Proved here and independently reconstructed; fixed embedded primitive stage |
| Quadratic-gluing comparison | Proved under explicit marked local-isomorphism hypotheses |
| Relative divided obstruction in coker D | Conditional general theorem; Z4 instance imported from the corrected independent audit |
| Conormal/arithmetic data alone determine the obstruction | False, by explicit smooth ambient gluing examples |
| Natural divided-Frobenius identification for the full Z4 class | Open; no nonexistence theorem for every richer possible comparison is claimed |
| Unrestricted characteristic-zero STCI for C0 | Open |

## 5. Single next mathematical step

Test (A) against the *actual global first-normal symbol image* of STCI
surface pairs, beginning with the ε=1 quotient locus and its low-degree
defect divisors. Construct the incidence requiring that the two homogeneous
surface symbols have common saturated line M, actual common divisor D,
and o(q) annihilate H⁰(ω_C⊗H⁻¹(−D)). The symbols must come from global
k-coefficient forms, not arbitrary k(C)-linear choices. Use already accepted
carrier and defect budgets as premises; do not reopen excluded quartics.

The stopping rule is exact emptiness for a stated finite locus, or an
explicit surviving pair of symbols together with its first unresolved lift
condition. This is the next direct use of the new STCI condition. A survivor
does not constitute actual surfaces with exhausted support; cases with both
generic normal orders at least two remain in their separate accepted
blow-up/normal-filtration lanes.

## Verification and review

The two new scripts, the independent audit, and their exact scope are linked
from the reports. They check polynomial/Laurent arithmetic, coordinate
transformations, defect cancellation, local counterexample algebras, and
small-prime illustrations. The structural arguments above are proofs, not
inferences from those finite tests. The inherited carrier exclusions and
accepted full ambient cocycle were used as premises, not re-proved.

The companion [independent audit](2026-10-21-z4-general-mechanism-independent-audit.md)
records reconstruction of the new implications and the cross-investigation
scope checks. All new results remain unpromoted research evidence.
