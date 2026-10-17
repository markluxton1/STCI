# Full conormal socle budget: independent audit and general consequences

Date: begun 2026-10-13, completed 2026-10-14. Status: **PROVED**, conditional
only on the stated smooth-support hypotheses and, when used, the slope
bound (S). This is an independent review of the new mathematics in
`2026-10-13-evening-entirely-thick-rees-progress.md`. Previously accepted
quartic, blowup, saturation, and higher-jet results were taken as inputs;
none of their computations was rerun. No canonical-state file is edited.

## 1. Audit verdict and scope

The full conormal-filtration theorem, exact socle line, Frobenius
inequality, defect identity, and balanced-rational equality argument in
Sections 2--7 of the reviewed note are sound. No substantive repair is
needed. The proof correctly permits torsion in intermediate normal
layers, and correctly uses the actual Loewy index of the entire generic
algebra rather than either chosen equation order.

The only clarifications needed for a reusable statement are these:

* For an arbitrary support curve, the real-valued defects need not be
  integers. They are integers in the reviewed C0 specialization.
* The choice lambda = mu_max(N) uses the characteristic-zero symmetric
  slope theorem. The elementary globally generated twist choice works
  in every characteristic and is sufficient for all arguments below.
* Equality gives a globally Gorenstein associated graded algebra on any
  smooth support curve. Its description by a constant algebra requires
  the extra balanced rational normal-bundle hypothesis.

The global STCI problem remains open. These are necessary structure
theorems for a proposed complete-intersection thickening, not an
existence theorem or an unrestricted exclusion.

## 2. Fixed notation

Let C be a smooth integral curve of degree e and genus g in P3, and let
Y = V(F_a,G_b) be a complete intersection with Y_red = C. Put

    J = I_C O_Y,
    n = length O_(Y,eta) = ab/e,
    d = max { j : J_eta^j != 0 },
    L_j = J^j/J^(j+1),
    T_j = torsion(L_j),  B_j = L_j/T_j,
    h_j = rank B_j,
    M = sum j h_j,
    L = e(a+b-4) - (2g-2).

Assume every torsion-free quotient V of Sym^j N_C^* satisfies
deg V >= -lambda j rank V. Write

    delta_j = deg B_j + lambda j h_j,
    t_j = length T_j,
    Delta_j = delta_j + t_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

All delta_j and t_j are nonnegative. The audited theorem gives

    S = Ann_Y(J) = omega_C tensor O_C(4-a-b),
    J^d = S(-D),  D effective,
    n(lambda d-L) = lambda Asym + 2 Delta.       (1)

Here and below deg D means the degree of the effective divisor; when
writing a numerical identity involving D we use deg D explicitly.

## 3. Equality is global self-duality on every smooth support

Suppose lambda d = L. Then (1) forces Asym = 0 and all delta_j = t_j = 0.
The generic Frobenius inclusions all become equalities, so h_i = h_(d-i)
and the generic associated graded algebra is Gorenstein.

The global multiplication maps induce

    B_i -> B_(d-i)^* tensor J^d.                 (2)

These maps are generically isomorphisms. Their two bundles have the
same degree because deg B_j = -lambda j h_j and J^d = S has degree
-lambda d. Thus their determinants are nonzero sections of degree-zero
line bundles on the smooth proper curve. Every map (2) is an
isomorphism. Hence every pairing

    L_i tensor L_(d-i) -> S

is perfect everywhere on C. The entire associated graded algebra is
therefore a sheaf of graded Gorenstein algebras, with socle line S.

This proves more than generic Hilbert-function symmetry. It controls
all closed support points and gives the intrinsic filtered identities

    Ann_Y(J^i) = J^(d-i+1),  1 <= i <= d.        (3)

To prove (3), take a local section z annihilating J^i. If its first
nonzero normal symbol occurs at index j < d-i+1, the perfect pairing
L_j x L_(d-j) -> S gives a section of J^(d-j), hence of J^i, whose
product with z is nonzero. This is a contradiction.

All O_Y/J^i and J^i are Cohen--Macaulay sheaves of dimension one: their
successive quotients are vector bundles on C. Since Y is Gorenstein,
Cohen--Macaulay duality then also gives

    Hom_Y(O_Y/J^i, O_Y) = J^(d-i+1),
    Hom_Y(J^i, O_Y) = O_Y/J^(d-i+1).             (4)

The second identity follows by dualizing 0 -> J^i -> O_Y -> O_Y/J^i -> 0;
the sheaf Ext^1 of its Cohen--Macaulay quotient into O_Y vanishes.
This standard input is supplied by Stacks Project
[Lemma 47.16.7](https://stacks.math.columbia.edu/tag/0B5A), specialized to
the normalized dualizing complex O_Y[1] locally. Tensoring (4) with
omega_Y yields the corresponding canonical-module formulation.

Neither (3) nor (4) identifies O_Y with an O_C-algebra. A global
retraction Y -> C and splitting of the embedded formal neighborhood
remain separate questions.

## 4. A stronger torsion identity away from numerical equality

Assume only Asym = 0. This is equivalent to the generic associated
graded algebra being Gorenstein. The maps (2) remain generically
isomorphisms between bundles of equal rank h_i = h_(d-i), hence are
injective with torsion cokernel. Let epsilon_i be its length and put
t = sum t_j. Since

    deg J^d = -lambda d + delta_d,
    delta_d = lambda d-L-deg D,

one gets the individual inequalities

    epsilon_i = h_i delta_d - delta_i - delta_(d-i) >= 0.  (5)

Summing (5), and using (1) with Asym = 0, gives the exact new identity

    sum epsilon_i = 2t - n deg D.               (6)

In particular

    2t >= n deg D.                             (7)

If the entire normal filtration is torsion free, t = 0; then D = 0 and
every epsilon_i = 0. Thus (2)--(4) hold globally even when lambda d > L.
This is a support-point obstruction beyond the scalar budget: failure
of the top power to reach the actual socle forces enough intermediate
torsion to pay at least n deg D/2, and additional torsion measures the
degeneracy of the complementary-layer pairings.

For any order-one presentation, the generic algebra has embedding
dimension one, hence is K[z]/(z^n), with d = n-1 and all h_j = 1.
Consequently Asym = 0 automatically and (5)--(7) apply. If all its
normal layers are torsion free, the natural surjections L_1^j -> L_j
are isomorphisms of line bundles; therefore

    L_1^(n-1) = omega_C tensor O_C(4-a-b).

That is a global Picard-group condition, stronger than equality of
degrees. Torsion is precisely where this primitive-multiple-curve
description can break down.

## 5. Entirely thick presentations force exact early layers

Let m >= 2 be the smallest generic order of an element of the local
complete-intersection ideal; equivalently m = min(p,q) for a chosen
generating pair with exact generic normal orders p,q. For 0 <= j < m,
the conormal quotient map has no generic kernel. Its kernel is a
subsheaf of a vector bundle and therefore vanishes globally. Thus

    L_j = Sym^j N_C^*,  0 <= j < m.             (8)

In particular every entirely thick presentation has L_1 = N_C^*,
including at all special support points. If nu = deg N_C / 2, (8) gives

    Delta_j = j(j+1)(lambda-nu),  j < m,
    2 Delta >= [2m(m^2-1)/3](lambda-nu).        (9)

For characteristic zero, choose lambda = mu_max(N_C). If N_C is
unstable, lambda > nu and the budget has strictly positive compulsory
slack. Numerical equality is possible only when N_C is semistable.
More precisely,

    n(lambda d-L)
       >= lambda Asym + [2m(m^2-1)/3](lambda-nu).  (10)

This is a general normal-bundle obstruction applying to all degrees
simultaneously. In the balanced C0 case lambda = nu = 7, its compulsory
early-layer contribution is zero, so the ambient extension obstruction
must supply additional information.

## 6. Higher moments and uniform Loewy bounds

The companion independent derivation is in
`2026-10-13-generalization-higher-moment-and-loewy-bounds.md`.
Its elementary Frobenius and generic-linear-parameter arguments give,
in every characteristic over an infinite coefficient field:

* The distribution h_j/n is stochastically dominated by its reflection
  j -> d-j. Every odd central moment is nonpositive, and equality in
  any strictly increasing odd central test forces Asym = 0.
* For codimension-two Artin Gorenstein algebras of initial ideal order
  m, the Hilbert function begins 1,2,...,m and thereafter falls at most
  one at each step. Thus

      d <= n-1-(m-1)^2.                        (11)

The companion proof was independently checked at its delicate step:
both A/xA = K[[y]]/(y^m) and gr(A)/(x*) = K[y]/(y^m) are computed by
restricting the original ideal and its initial ideal separately. It
does not interchange quotient and associated graded without proof.
After generic-linear multiplication is surjective from degree m-1,
Nakayama gives m_A^(i+1) = x m_A^i. Frobenius duality identifies Ann(x)
as one K[y] Jordan block, and its intersections with the powers of m_A
have successive drops at most one. The explicit sharpness family has
the stated three-element standard basis; its rectangle of mixed
monomials plus the pure-y chain gives the claimed Hilbert sequence
without characteristic-dependent coefficients.

There is a stronger sharp moment statement. Put k = n-m^2 >= 0. The
Hilbert distribution at fixed n,m is stochastically dominated by the
sequence

    (1,2,...,m,m-1,...,2,1, followed by k extra ones).

Consequently

    M <= M_max(n,m)
      = m^2(m-1)+2(m-1)k+k(k+1)/2
      = [n(n-1)-(m-1)^2(2n-m^2)]/2.            (11a)

This is sharp in every characteristic, as witnessed by the local CI
(x y^(m-1), x^m+y^N), where N = n-(m-1)^2-m+1 >= m. Combining
Riemann--Roch, 2 Delta = 2 lambda M-nL, with (11a) gives

    nL <= lambda[n(n-1)-(m-1)^2(2n-m^2)].      (11b)

With the normal-bundle instability cost retained, its stronger version
is

    lambda[n(n-1)-(m-1)^2(2n-m^2)]-nL
        >= [2m(m^2-1)/3](lambda-nu).           (11c)

For all entirely thick C0 presentations, using m >= 2 already yields

    n[4(a+b)-14] <= 7(n^2-3n+4), n=ab/4.     (11d)

When only a lower bound on m is known, the corresponding bound remains
valid: the correction (m-1)^2(2n-m^2) increases on 1 <= m <= sqrt(n).

Combining (11) with (1) gives a degree-independent necessary inequality

    L <= lambda [n-1-(m-1)^2],                 (12)

and combining with (10) yields

    n{lambda[n-1-(m-1)^2]-L}
        >= [2m(m^2-1)/3](lambda-nu).           (13)

For C0, (12) specializes to

    7ab >= 16(a+b) + 28(m-1)^2 - 28.           (14)

These do not bound degrees uniformly or settle the higher-order branch.
They replace independent degree-by-degree checks with structural tests
of the entire generic algebra and its global normal filtration.

## 7. Continuation boundary

The equality obstruction from the ambient second neighborhood is a
separate new proof being independently reviewed in a companion note.
It must not be folded into the accepted socle-budget theorem without
checking relation lifting and the multiplicity-sensitive coefficient
extraction. The accepted nonzero marked-direction extension class is
used as an input, not recomputed.

The most informative unresolved data away from equality are now the
generic annihilator deficits, the torsion in every normal layer, the
determinant lengths epsilon_i when the generic graded algebra is
Gorenstein, and the degree defects of the first initial-relation bundle.
The structure above preserves all higher normal orders; no tangent-only
multiplicity cap or generic-to-special root comparison has been used.

