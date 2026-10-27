# Independent audit: boundary repair and global lifting

Review date: 2026-10-27. Reviewer: independent `repair_note_audit` agent.
Source: [boundary repair and global lifting](2026-10-26-boundary-repair-global-lifting.md).
Outcome: **PASS within the stated scopes**. The exact repair criteria,
source-image identities, and fixed-degree endpoint are independently
reconstructed below. The controlled boundary-modification comparison
remains an explicitly unproved research target. No canonical promotion,
new STCI exclusion, or homogeneous realization is certified by this review.

## 1. Scope and method

The reviewer read the retrieval index and contribution protocol, then
checked the exact source text. The review distinguishes the following:

- smooth-projective-curve cohomology for a specified vector bundle V;
- the entire effective-divisor family on P1, with B a nonnegative integer;
- normal and jet images from actual homogeneous equations;
- the degree-exhaustion criterion for actual proper complete intersections;
- the proposed, but not yet established, comparison with saturated boundary
  data of a supported generically curvilinear thickening.

The saturated Gorenstein pairing is used only in its inherited scope.
No accepted proof or executable certificate was rerun, and no sampled
example is used as evidence for a universal assertion.

## 2. Principal parts and the dual repair condition

For effective D, the quotient Q_D=V(D)/V is a finite-support sheaf, and
the exact sequence 0 -> V -> V(D) -> Q_D -> 0 gives the exact segment

    H^0(Q_D) -> H^1(V) -> H^1(V(D)).

Thus the kernel of the latter map is exactly the principal-parts image.
This proves the source's criterion for an identified class o in H^1(V).
It does not endow o itself with a zero divisor.

Functorial Serre duality identifies the dual of H^1(V) -> H^1(V(D)) with
the inclusion

    H^0(V^vee tensor omega_C(-D))
      -> H^0(V^vee tensor omega_C).

A class maps to zero if and only if its functional vanishes on the image
of this inclusion. The annihilator criterion therefore has the correct
direction and twist. Both arguments work in arbitrary characteristic.
The source correctly avoids assuming that varying-divisor cohomology
dimensions are constant on an arbitrary higher-genus curve.

## 3. P1: common-divisor kernel and the dimension threshold

For V=O(-r), r>=2, let n=r-2. Serre duality identifies o with a functional
on H^0(O(n)). If D has degree B and is cut out by nonzero h in H^0(O(B)),
then the image of H^0(O(n)(-D)) in H^0(O(n)) is exactly
h H^0(O(n-B)); it is zero when n-B<0.

Consequently repair by D is equivalent to

    o(hg)=0 for every g in H^0(O(n-B)),

which is exactly h in the kernel of the source's multiplication map.
Conversely any nonzero kernel element defines such an effective D.
If a divisor of degree less than B repairs o, adding an effective divisor
to obtain degree B preserves vanishing, since the maps on H^1 factor.
This verifies the stated equivalence with degree at most B. Repeated
factors of h are permitted throughout; no reduced-support restriction
or separability assumption is hidden in the argument.

The dimensions in the threshold argument are B+1 and max(r-1-B,0).
For B>=floor(r/2), the former is strictly greater than the latter.
Hence a nonzero kernel exists for every o. This establishes the stated
limit of a single line-bundle obstruction under an unrestricted pole
allowance. It does not prove an actual boundary or a realizable lift.

For a split bundle, the direct-sum H^1 class maps to zero exactly when
every component does. If one divisor must repair them, the SAME section h
must lie in every component kernel. The stacked map therefore gives the
correct simultaneous condition. Allowing a separate h for each component
would be a weaker test and would lose the common-boundary requirement.
On a fixed splitting-type stratum these maps have fixed source and target
dimensions, so their ranks and degeneracy loci have the stated finite
algebraic meaning. No assertion of universal rank is inferred from a
generic parameter or a selected point.

## 4. The boundary comparison is not proved by these criteria

The inherited relations D_i+D_(m-1-i)=D_soc and effectivity imply
0<=D_i<=D_soc. Accordingly

    Hom(L^i(D_i),L^j(D_j))
      =L^(j-i)(D_j-D_i) subset L^(j-i)(D_soc)

is correct. These are inclusions of possible coefficient bundles. They
do not prove a morphism of lifting problems or identify the obstruction
for an actual multiple curve with its image under a chosen twist.

The source explicitly marks the needed V -> V' -> V(c D_soc) comparison
as unproved, requires the actual lifting complex, and does not identify
ordinary torsion, spectral Delta, and allowed principal parts. This is
the essential remaining dependency. The relaxation to arbitrary divisors
of degree c delta is logically safe only after the comparison is supplied:
failure of the relaxed test excludes permitted repairs; passing it proves
neither the constrained divisor data nor a genuine lift.

## 5. Actual homogeneous jet and symbol images

The source-image formulas follow directly from the sheaf sequences

    0 -> I^(N+1)(d) -> I(d) -> (I/I^(N+1))(d) -> 0,
    0 -> I^(n+1)(d) -> I^n(d) -> Sym^n E(d) -> 0.

Their H^0 images are precisely the displayed connecting-map kernels.
The second sequence uses the regular embedding of C in the smooth
threefold. These are actual global k-linear source images, not arbitrary
K=k(C) normal symbols.

The next-jet sequence with kernel Sym^N E(d) is likewise exact. Its
connecting class is in H^1(C,Sym^N E(d)), as stated. The note correctly
distinguishes this explicit linear jet obstruction from other relation
or ideal lifting problems, whose targets have not been supplied by that
sequence. Choosing allowable graded symbols separately does not specify
one compatible jet, so retaining the whole source U_(d,N) is necessary.

## 6. Fixed-degree generic length and degree exhaustion

Let F,G be actual global forms of degrees a,b defining a proper complete
intersection containing an integral C of degree d, and suppose M=ab/d
is an integer. At eta_C the two equations have finite transverse length
m_C. The fundamental cycle and Bezout give d m_C<=ab, hence m_C<=M.

For any Artin local algebra of length m_C, every nonzero successive
maximal-ideal power strictly decreases length: equality of adjacent
powers would make that power zero by Nakayama. Therefore its maximal
ideal has exponent at most m_C. The quotient by m^(M+1) already retains
the full local algebra R/(F,G), and its length is m_C.

It follows that the truncated length is M exactly when m_C=M. Then the
contribution of C consumes degree ab. Any additional curve component
would contribute positive degree, while purity of the proper complete
intersection rules out embedded components. Conversely sole reduced
support C gives m_C=M. This proves the intrinsic finite endpoint in
the source, with all its properness and actual-global-form hypotheses.

The matrix interpretation requires all truncated multiples. The note
appropriately states that a coefficient/normal chart is chosen for that
calculation: the residue field is not claimed to be canonically embedded
in R/m^(M+1). Fixed chart denominators can be cleared, with coefficients
of the actual forms remaining constants in k. One must retain the proper
pair open locus. No bound uniform in a,b follows from this fixed-degree
criterion.

## Outcome

No substantive correction to the inspected source text is required.
The universal repair test and the exact finite endpoint pass independent
reconstruction. The proposed boundary-to-obstruction comparison remains
open and must not be reported as a completed theorem. The audit supports
using these criteria to choose a class-wide calculation and to diagnose
when a coarse obstruction is too weak; it does not certify any new
exclusion, nonempty realization locus, or canonical result promotion.
