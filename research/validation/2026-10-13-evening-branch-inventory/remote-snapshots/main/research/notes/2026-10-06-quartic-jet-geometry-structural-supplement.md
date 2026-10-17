# Canonical-status notice

This note was developed on a side branch that forked before the 2026-10-06 audited consolidation. Its geometric lemmas and proposed jet-budget framework are retained as structural research material. **Its repeated statement that the characteristic-zero (4,7), e=2 branch remains open is superseded by `research/AUDITED_STATE_2026-10-06.md`, Section B:** the canonical primitive-triple quartic factorization theorem excludes the e=2 branches of (4,7) and (4,8). Do not use the obsolete frontier language below as a premise. The jet/ruling interpretation may still be useful for e=0/e=1 and broader STCI questions.

---

# Quartic jet geometry and a possible STCI condition-budget framework

Date: 2026-10-06

## Purpose

This note records the geometric reinterpretation of the quartic-incidence calculation for the primitive (4,7), e=2 program for
C = [s^4:s^3t:st^3:t^4] in P^3,
and isolates a possible general research program suggested by it.

The immediate problem remains: a hypothetical (4,7), e=2 carrier must contain the canonical primitive triple C_3. We want to understand H^0(I_{C_3}(4)) geometrically, especially together with P-044. The broader observation is that STCI questions may be organized by a successive "jet-condition budget" for hypersurfaces required to contain primitive multiple structures.

Statements below are labelled PROVED / EXACT COMPUTATIONAL EVIDENCE / HEURISTIC / OPEN. The broader jet-budget program is not a theorem.

---

## 1. The unique quadric and the first-normal codimension three

Let Q = P^1 x P^1 be the unique smooth quadric containing C. With the convention used here, C has bidegree (3,1).

For a quartic F containing the primitive double C_2, its restriction to Q has C as a component:
F|_Q = C + D, with D of bidegree (1,3).

The residual restriction sequence is

    0 -> O_Q(-2,2) -> O_Q(1,3) -> O_C(10) -> 0.

Since H^0(O_Q(-2,2))=0 and H^1(O_Q(1,3))=0, we obtain

    0 -> H^0(O_Q(1,3)) -> H^0(O_C(10))
      -> H^1(O_Q(-2,2)) -> 0.

By Kunneth,

    H^1(O_Q(-2,2))
      = H^1(P^1,O(-2)) tensor H^0(P^1,O(2)),

so this cokernel has dimension 3.

**PROVED.** The previously observed codimension-three first-normal condition is intrinsic: the extendable degree-10 sections are the kernel of the connecting map to H^1(O_Q(-2,2)). In the affine coordinate basis this is the old

    V = <1,z,z^3,z^4,z^6,z^7,z^9,z^10>;

the missing z^2,z^5,z^8 are a coordinate manifestation of the 3-dimensional cohomological obstruction.

## 2. Comparison of the two conormal filtrations

The embedding through the quadric gives

    0 -> O(-8) -> N_C^* = O(-7)^2 -> O(-6) -> 0.

The primitive double gives

    0 -> M=O(-9) -> N_C^*=O(-7)^2 -> L=O(-5) -> 0.

The composite O(-8) -> N_C^* -> L=O(-5) is multiplication by a cubic r in H^0(O_C(3)). In the established affine normalization,

    r = A + (z/2) B.

Let R=Z(r), a degree-three divisor.

**PROVED.** Up to scalar, the induced map M=O(-9) -> O(-6) is also multiplication by r. Thus

    M = O(-6)(-R).

Geometrically, the primitive conormal kernel is the elementary modification of the conormal direction inside Q at R.

After twisting by O_C(4)=O(16),

    M(4)=O(7) -> O(10)

is h |-> rh.

## 3. Intrinsic description of the first-order source K_r

A quartic through C_2, modulo the universal q^2 direction, corresponds to h in H^0(O_C(7)) such that rh extends from C to a section of O_Q(1,3). Therefore

    K_r = ker[ H^0(O_C(7)) -> H^1(O_Q(-2,2)) ],
                 h |-> delta(rh).

Equivalently,

    K_r = H^0(Q,I_{R/Q}(1,3)).

**PROVED.** Generically three points impose three independent conditions on H^0(O_Q(1,3)), whose dimension is 8, so dim K_r=5. Together with q^2, this gives generic h^0(I_{C_2}(4))=6.

### The P-045 rank jump

On P-045, a=-1/2 and b=-2, and

    r = x + (d/2) z^3

(in the dx=1 normalization, r=x+(1/(2x))z^3).

Under affine coordinates for C in Q, z maps to (z,z^3). Hence the three points of R have the same second ruling coordinate: R is the intersection of C with a ruling fiber F_0.

Conversely, from

    r = x + (a+1/2)z + (1+b/2)z^2 + (d/2)z^3,

being pulled back from a linear equation in the second ruling coordinate forces a=-1/2 and b=-2.

**PROVED within the current normalization/conventions.**

    P-045 <=> R is a ruling-fiber divisor on C.

Since O_Q(1,3)|_{F_0}=O_{P^1}(1) for the relevant ruling convention, any (1,3)-section vanishing at all three points of R=C intersect F_0 must contain F_0. Hence

    H^0(I_{R/Q}(1,3)) = H^0(O_Q(1,2)),

and dim K_r=6. This gives a geometric explanation of the source jump at P-045.

## 4. The second-order target is supported on 2R

For the primitive triple,

    I_{C_2/C_3} = L^2 = O(-10).

Twisting by O_C(4)=O(16) gives O(6), hence

    0 -> I_{C_3}(4) -> I_{C_2}(4) --rho--> O_C(6).

The unique quadric satisfies intrinsically

    rho(q^2)=r^2.

Therefore, after quotienting by q^2,

    bar-rho: K_r -> H^0(O(6))/<r^2>.

Because div(r^2)=2R,

    0 -> O_C --r^2--> O_C(6) -> O_{2R}(6) -> 0,

and H^1(O_C)=0, so

    H^0(O(6))/<r^2> = H^0(O_{2R}(6)).

**PROVED.** The essential second-order map is

    bar-rho: K_r -> H^0(O_{2R}(6)).

For reduced R=p_1+p_2+p_3, the six-dimensional target decomposes locally as three length-two contributions. Thus the second-order obstruction is localized at the three points where the primitive and quadric conormal directions meet.

## 5. Local normal form for the second-order condition

This subsection records the local derivation; signs depend on choices of local generators, but the structural content does not.

Choose local coordinates near p in R:
- u along C,
- v normal to C inside Q,
- w an equation for Q.

Then I_C=(v,w). Normalize the primitive quotient locally so that, to first order,

    v |-> epsilon,    w |-> r epsilon.

Write the canonical triple as

    v = epsilon + alpha epsilon^2,
    w = r epsilon + beta epsilon^2  mod epsilon^3,

and set kappa=beta-r alpha.

A quartic containing C_2 has local expansion

    F = h(w-rv) + 1/2(A v^2 + 2Bvw + Cw^2) + O(I_C^3).

Substitution gives

    rho(F) = h kappa + 1/2(A+2Br+Cr^2),

and modulo r^2,

    bar-rho(F) = [h kappa + A/2 + Br]_{2R}.

Restricting F to Q, write F|_Q=v d_h, where d_h=0 is the residual (1,3)-divisor D_h. Then locally

    d_h = -rh + (A/2)v + ...

At a simple p in R, if u=r is used as local parameter,

    partial_u d_h(p) = -h(p),
    partial_v d_h(p) = A(p)/2.

Thus the value component of bar-rho(F)|_{2p} prescribes a relation between the tangent and transverse derivatives of D_h at p:

    partial_v d_h(p) - kappa(p) partial_u d_h(p) = 0

up to the sign convention for kappa.

**PROVED LOCALLY, subject to the stated generator/sign conventions.** One of the two new conditions at each p in R is a prescribed tangent-direction/contact condition for D_h.

The second coefficient modulo r^2 involves a second jet of d_h, not merely its first jet. Therefore it is premature to identify all six new conditions with containment of three fixed doubled points in Q.

## 6. Condition count and the P-045 degeneration

The vector space H^0(O_Q(1,3)) has dimension 8.

For general R, requiring D to contain R imposes 3 independent conditions, leaving 8-3=5, namely K_r.

Passing from C_2 to C_3 asks for two further local conditions at each of the three points, encoded by

    bar-rho: K_r -> H^0(O_{2R}(6)),

whose target has dimension 6.

Hence the naive total is

    3 + 6 = 9

conditions on an 8-dimensional vector space.

**INTERPRETATION, not by itself a proof of nonexistence.** Generic quartic incidence is overdetermined. Survival requires dependencies among the point/jet conditions.

**EXACT COMPUTATIONAL EVIDENCE from the existing verifier.**
- Generically dim K_r=5 and bar-rho is injective, so no quartic contains C_3.
- At P-045, dim K_r=6, the corresponding second-order rank drops to 3, and the full kernel H^0(I_{C_3}(4)) has dimension 4.
- Those four quartics are exactly the multiples H_x H^0(O(1)) of the survivor cubic, so they do not provide genuine irreducible quartic carriers.

The ruling-fiber geometry explains the first jump:

    R=C intersect F_0
      => D=F_0+D', D' in |O_Q(1,2)|.

It is a strong geometric candidate for explaining the second-order rank collapse as well, but a complete intrinsic proof of that rank collapse has not yet been written.

## 7. Immediate open problem for the C_0 program

The desired implication remains

    P-044 + H^0(I_{C_3}(4)) != 0
      => R is a ruling-fiber divisor,

or an equivalent statement implying P-045.

If established, the existing P-045 analysis then shows all quartics through C_3 are cubic multiples, killing genuine quartic carriers in the surviving (4,7), e=2 branch.

The next conceptual test is to understand whether P-044 (extension C_3 -> C_4) can itself be localized at R and compared directly with the contact conditions above. If that fails to simplify, a small targeted exact calculation of the combined degeneracy locus is justified; a broad Groebner/saturation attack should remain fallback.

---

# Part II. Proposed general STCI jet-budget program

## 8. Successive jet maps for primitive multiple structures

Let C in P^3 be a smooth integral curve and suppose a primitive multiple structure has filtration

    C=C_1 subset C_2 subset ... subset C_m

with conormal line L and

    I_{C_k/C_{k+1}} = L^k.

For a degree-a hypersurface, each step gives

    0 -> I_{C_{k+1}}(a) -> I_{C_k}(a) -> L^k(a),

and hence a natural map

    rho_k: H^0(I_{C_k}(a)) -> H^0(L^k(a)).

A degree-a hypersurface containing C_m must survive all successive maps.

Define

    s_k = h^0(I_{C_k}(a)),
    c_k = rank(rho_k).

Then s_{k+1}=s_k-c_k. The basic regimes are:

    s_k > c_k : survival dimensionally expected;
    s_k = c_k : borderline/determinantal;
    s_k < c_k : survival requires rank degeneracy.

This is only a bookkeeping principle until the maps and their dependencies are understood geometrically.

## 9. Why this may interact with STCI degree growth

For a primitive complete intersection of surfaces of degrees a,b supported on a degree-d curve, the multiplicity is

    m = ab/d.

Thus increasing carrier degrees has competing effects:
1. it increases the number of available hypersurface sections;
2. it also increases the required multiplicity, hence the number of infinitesimal layers that must be survived.

The relevant comparison is therefore not a single Hilbert-function count. It is the cumulative loss from the successive ranks (or a more invariant replacement accounting for the changing domains) against the initial carrier freedom.

A naive sum of h^0(L^k(a)) is not sufficient: targets can vanish, maps need not be surjective, and dependencies can be forced by geometry. The C_0 ruling-fiber phenomenon is precisely an example where the geometry of the conormal data changes the rank.

## 10. Candidate general principle

**HEURISTIC / RESEARCH PROGRAM.** Define an expected jet budget for candidate carrier data by comparing available hypersurface freedom with the ranks expected from the successive maps rho_k.

Negative expected budget should not be interpreted as an automatic obstruction. Rather:

> When the expected jet budget is negative, existence of a carrier forces the conormal/multiple-structure data into degeneracy loci of the successive jet maps.

The useful theorem would therefore have the form

    negative expected jet budget
      => STCI only on specified geometric degeneracy loci.

The substantive problem is to describe those degeneracy loci geometrically.

This suggests a possible division:
- underdetermined cases: carrier freedom exceeds the independent jet conditions, so survival is dimensionally plausible;
- overdetermined cases: STCI requires special geometric dependencies among the jet conditions.

Known STCI examples should eventually be tested against this distinction.

## 11. Why C_0 is a useful laboratory

The present quartic calculation exhibits the proposed mechanism concretely:

    primitive quotient
      -> R
      -> K_r
      -> localized jet conditions
      -> overdetermination.

The exceptional rank-drop locus has a recognizable geometric feature:

    R = C intersect ruling fiber.

Thus C_0 offers a test of whether algebraic rank-degeneracy loci of successive jet maps systematically admit geometric descriptions. That question should be answered here before attempting a broad abstraction.

## 12. Status summary

### PROVED / structurally established
- The codimension-three first-normal obstruction is H^1(O_Q(-2,2)).
- The cubic r compares the quadric conormal direction with the primitive conormal quotient.
- M = O(-6)(-R).
- K_r = H^0(I_{R/Q}(1,3)).
- P-045 corresponds to R being a ruling-fiber divisor (within the current normalization).
- The essential second-order target is H^0(O_{2R}(6)).
- Locally, one component at each p in R is a prescribed first-order contact direction; the other involves a second jet.

### EXACT COMPUTATIONAL EVIDENCE already present in the repository
- Generic quartic incidence at C_3 is empty.
- At P-045 the source and second-order ranks jump as recorded above.
- The resulting quartics through C_3 are cubic multiples, not genuine carriers.

### OPEN
- Give a fully intrinsic description of the second local condition at each point of R.
- Explain the P-045 second-order rank collapse geometrically.
- Prove or disprove P-044 + H^0(I_{C_3}(4)) != 0 => R ruling fiber.
- Determine whether P-044 localizes naturally at R.
- Formulate a correct general jet-budget invariant and test it on known STCI/non-STCI examples before treating it as a general obstruction theory.
