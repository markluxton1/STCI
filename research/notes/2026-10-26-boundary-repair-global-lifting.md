# Can the boundary repair the actual global lifting obstruction?

Date: 2026-10-26. Status: provisional structural continuation, with
[independent review](2026-10-26-boundary-repair-global-lifting-audit.md).
No canonical promotion, new exclusion, or homogeneous realization is claimed.
No isolated example or sampled pair is used.

Continuation, October 27: the
[one-step equation-module comparison](2026-10-27-one-step-boundary-obstruction.md)
proves the proposed repair principle for a fixed lower embedded
thickening and identifies exact vanishing at the final Gorenstein step.
It does not settle a comparison for arbitrary ambient obstruction complexes.

## 1. The general question worth answering

The preceding [genus account](2026-10-26-normal-torsion-spectral-genus-budget.md)
and [intrinsic initial construction](2026-10-26-weighted-initials-normal-boundary.md)
make boundary indices measurable, but have not shown that those indices
control the obstruction to realizing two actual homogeneous equations.
The next target is a comparison theorem between an allowed boundary
modification and a genuine global lifting problem.

For the line/socle budget, assume a proper CI Z of degrees (a,b) in P3,
sole smooth reduced support C, and generic transverse algebra K[y]/(y^m).
Then its saturated layers W_i=L^i(D_i) satisfy the inherited pairing
D_i+D_(m-1-i)=D_soc, with D_0=D_1=0. In particular 0<=D_i<=D_soc, and

    O_C(D_soc)=omega_C tensor O_C(4-a-b) tensor L^(-(m-1)).

The degree delta of D_soc is fixed once (a,b,m,L) are fixed. This is a
specific linear system and paired divisor data, not just an arbitrary
collection of punctual lengths. The higher-rank normal-layer account is
needed when the generic transverse algebra has embedding dimension two.

## 2. A precise repair criterion on any smooth projective curve

Let V be a vector bundle on a smooth connected projective curve C over
an algebraically closed field, and let o in H^1(C,V) be an identified
linear lifting obstruction. For effective D put Q_D=V(D)/V. The exact
sequence

    0 -> V -> V(D) -> Q_D -> 0

gives

    o maps to zero in H^1(V(D))
      iff o belongs to image(H^0(Q_D) -> H^1(V)).          (1)

Thus a permitted pole divisor repairs o exactly when its principal parts
can supply o. A cohomology class does not itself have a zero divisor.

By functorial Serre duality, the dual map to H^1(V) -> H^1(V(D)) is

    H^0(V^vee tensor omega_C(-D)) -> H^0(V^vee tensor omega_C).

Consequently (1) is equivalent to

    o annihilates H^0(V^vee tensor omega_C(-D)).          (2)

This is an exact criterion in arbitrary characteristic. The standard
duality input is [Stacks, section 53.4](https://stacks.math.columbia.edu/tag/0E31).
For varying D on a general curve, use the principal-parts incidence
and cohomology/base-change strata; no unqualified closed-locus assertion
across jumping cohomology dimensions is needed.

## 3. On P1, all repair divisors at once give a kernel test

Suppose V=O_P1(-r), r>=2, and n=r-2. Regard o as a linear functional on
H^0(O(n)) by Serre duality. A divisor D of degree B is the zero divisor
of some nonzero h in H^0(O(B)). For B<=n, the subspace in (2) is

    h H^0(O(n-B)) subset H^0(O(n));

for B>n it is zero. Define the multiplication matrix

    C_(B,o): H^0(O(B)) -> H^0(O(n-B))^vee,
    h |-> (g |-> o(hg)),                                (3)

interpreting H^0 of a negative line bundle as zero. Then

    some effective D of degree at most B repairs o
      iff ker C_(B,o) is nonzero.                       (4)

One can pad a divisor to obtain degree exactly B; further twisting
preserves vanishing. Conversely a nonzero kernel element cuts out an
effective degree-B divisor and satisfies (2). Repeated roots of h include
all nonreduced boundary divisors automatically. This is a statement about
an entire divisor family, not a pointwise experiment. It is often called
a catalecticant/multiplication test; its proof here is (1)--(3).

It also gives an immediate limit on the method. If

    B>=floor(r/2),

the source of (3) has dimension B+1 greater than the target dimension
max(r-1-B,0). Every obstruction then has a repair by SOME arbitrary
degree-B divisor. A single line-bundle obstruction cannot exclude using
that relaxed pole allowance. This does not show that an actual boundary
with the required paired divisors and global-source restrictions exists.

For V=direct_sum_i O(-r_i), discard summands with H^1=0, and stack

    C_(B,o): H^0(O(B))
       -> direct_sum_i H^0(O(r_i-2-B))^vee.              (5)

The SAME h must kill every component. Its nonzero kernel is exactly
simultaneous repair by one divisor. Testing each component with its own
divisor discards this common-support and common-multiplicity condition.
Multiple lifting classes can be stacked in the same manner when the
same modification is required to repair them. On fixed splitting-type
strata, (5) is a universal matrix on the actual obstruction parameter
family; full-column-rank and its failure are finite algebraic conditions.

## 4. The unproved comparison needed for our multiple curves

The following is a RESEARCH TARGET, not a consequence of the repair lemma:

    At a specified lifting stage, actual realizations with boundary
    D_soc induce a morphism of obstruction problems in which the
    obstruction o in H^1(V) becomes zero after a controlled modification
    V subset V' subset V(c D_soc), for an explicit integer c.

Proving this requires identifying the lifting complex and how saturation
changes it. There is a reason to try it. For saturated line layers,

    Hom(W_i,W_j)=L^(j-i)(D_j-D_i)
      subset L^(j-i)(D_soc).

Tensor constructions similarly give explicit multiple-divisor bounds.
These inclusions suggest possible correction bundles, but do NOT prove
that an actual realization kills the relevant obstruction in them. The
map between the lifting problems is essential. Depending on the stage,
several correction bundles or different multiples c may be necessary.

After this comparison, (1)--(5) provide necessary tests. Allowing every
divisor of degree c delta is a safe relaxation of allowing only c D_soc
with D_soc in its prescribed linear system. Failure even in the relaxed
test excludes all permitted repairs. Passing it does not prove an actual
correction or a lift: the restricted divisor, paired D_i, nonlinear
equations and actual global source may still fail.

Neither ordinary torsion T_n nor spectral comparison Delta is to be
identified with a pole allowance without proving this bridge. The
existing promoted [R0016](../results/nonsaturated_first_relation_resultant.md)
and [R0019](../results/quasiprimitive_residual_cycles.md) already give
specific conditional divisor comparisons. They are precedents with their
own hypotheses, not authority for the proposed general comparison above.

## 5. Preserve the actual homogeneous source throughout

Let I=I_C and d a carrier degree. The actual finite normal-jet image is

    U_(d,N)=image[H^0(I(d)) -> H^0((I/I^(N+1))(d))].

The ideal-sheaf exact sequence gives the exact description

    U_(d,N)=ker[H^0((I/I^(N+1))(d))
                  -> H^1(P3,I^(N+1)(d))].              (6)

Likewise the possible first nonzero symbols of order n are

    V_(d,n)=image[H^0(I^n(d)) -> H^0(C,Sym^n E(d))]
           =ker[H^0(C,Sym^n E(d))
                  -> H^1(P3,I^(n+1)(d))].              (7)

Separate choices in the V_(d,n) do not imply one compatible finite jet
in U_(d,N). A next-jet lift also has the exact kernel bundle sequence

    0 -> Sym^N E(d) -> (I/I^(N+1))(d)
          -> (I/I^N)(d) -> 0,

whose connecting class lies in H^1(C,Sym^N E(d)). This is one explicit
kind of genuine linear lifting class; other relation/ideal lifting
problems require their own correct targets and maps.

The universal objects should range over admissible lower lifts and
boundary data while imposing (6) for both carrier degrees. Their unknown
coefficients remain constants in k. A generic nonzero obstruction only
excludes a dense open locus; its zero locus must still be studied.
An isolated successful or failed lift does not settle the family.

## 6. An exact finite endpoint for a fixed degree pair

For actual proper global F_a,G_b containing an integral C of degree d,
suppose d divides ab and put M=ab/d. At the generic point of C, let
R=O_(P3,eta_C), with maximal ideal m. Then

    Z_red=C iff length_R R/(F,G,m^(M+1))=M.              (8)

Proof: properness gives a finite generic transverse length m_C, and
Bezout bounds d m_C<=ab. An Artin local algebra of length m_C has
nilpotent maximal ideal of exponent at most m_C. Since m_C<=M, the
truncation in (8) already retains its full length. Equality m_C=M
exhausts degree ab; any residual curve would have positive degree, and
purity of the complete intersection rules out embedded components.
The converse follows in the same way from degree exhaustion.

After a chosen formal coefficient/normal chart, (8) is a finite matrix
rank condition including ALL truncated multiples of F,G. The length
criterion itself is intrinsic. The residue field K=k(C) is not asserted
to be a canonically embedded coefficient field in R/m^(M+1).

Over the universal proper-pair open set in
P H^0(I(a)) times P H^0(I(b)), the finite rank equations concern actual
global coefficients. Fixed coordinate denominators can be cleared and
rational-function identities expanded into finitely many k-equations.
This gives an exact fixed-degree question across all pairs, rather than
a sampled example. It supplies no uniform bound on carrier degrees.

## 7. What the outcomes would teach

- If no permitted boundary repairs any actual-source obstruction on a
  stratum, we obtain an exclusion of that entire stratum.
- If repair occurs only on a proper determinantal locus, it identifies
  precisely which degenerations remain; it is not a universal exclusion.
- If dimensions force repair for every class in the relaxed test, the
  isolated obstruction/pole budget is structurally too weak. Shared
  divisors, actual source images or higher relations must carry the work.
- If abstract repairs exist but (6) fails, the issue is homogeneous
  realization. If (6) passes but the multiplicative lift fails, the
  missing information is filtered ideal/algebra compatibility.
- If the exact final locus (8) is proved nonempty within the proper-pair
  open set, it gives actual fixed-degree existence, unlike survival of
  a lower-order necessary condition.

The first substantive target is the controlled-modification comparison
in section 4, followed by the common-divisor test for its actual
obstruction family. A computation is warranted if it determines a
universal map, proves its rank/zero locus, or exposes a mechanism that
persists on a stated family. No new isolated example is needed here.
