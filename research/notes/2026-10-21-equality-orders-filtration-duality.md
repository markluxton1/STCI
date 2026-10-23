# Equality de=4m: generic orders, Hilbert filtration, duality

Status: WORKING NOTE; mathematical statements separated from proposed directions. No canonical promotion. Characteristic zero unless otherwise indicated.

Setup: C=[s^4:s^3t:st^3:t^4] smooth rational quartic, F,G homogeneous degrees d,e with no common surface component, C contained in their intersection. r=ord_C(F), s=ord_C(G), m=length at generic point of C. If de=4m, the entire reduced intersection is C by the residual-cycle proposition.

## Generic orders and full initial algebra

In R=k(C)[[x,y]], F_r,G_s are nonzero binary homogeneous forms. The plane local intersection inequality m>=rs holds. Equality iff gcd(F_r,G_s)=1 (initial forms a regular sequence). In that case the full m-adic initial ideal is (F_r,G_s), and the Hilbert series of the generic associated graded Artin algebra is (1-z^r)(1-z^s)/(1-z)^2. Hence de=4m forces de>=4rs, and de=4rs precisely in the coprime-initial case. If F_r,G_s have a common factor, m>rs; their full initial ideal needs cancellation generators.

For the fixed curve in characteristic zero, N_C/P3=O(7)^2, so a nonzero r-th conormal symbol of a degree-d form lies in H0(P1,O(4d-7r))^(r+1). Necessarily 4d>=7r, and similarly 4e>=7s. This is a generic-order bound independent of the STCI equality. Stronger restrictions (such as d>=3r) in existing results require their stated hypotheses and must not be silently generalized. In characteristic two the normal bundle splitting differs and the 7r bound must not be transplanted.

## Intrinsic filtration

For Z=V(F,G) with Z_red=C, J=I_C O_Z is nilpotent and Q_i=J^i/J^(i+1) are coherent O_C-modules. The generic ranks h_i=dim_k(C)(Q_i)_eta satisfy Σ_i h_i=m and h_0=1. The generic Hilbert function (h_i) is the Hilbert function of the full initial algebra. The natural maps Sym^i(I_C/I_C²) -> Q_i are surjective, hence h_i<=i+1, but no flatness/local freeness of Q_i is assumed.

The Hilbert polynomial of the (d,e) complete intersection Z is P_Z(n)=de*n - de(d+e-4)/2; with de=4m, χ(O_Z)=-2m(d+e-4). Additivity gives Σ_i χ(Q_i)=-2m(d+e-4). Each Q_i has generic rank h_i and may have torsion; if Q_i is locally free, χ(Q_i)=deg(Q_i)+h_i on C=P1. This is an identity, not an obstruction without control on degrees/torsion.

## Duality

Z is Gorenstein and ω_Z=O_Z(d+e-4). Generic local algebra A=O_{Z,η_C} is an Artinian Gorenstein complete intersection. Its socle has dimension one, but the m-adic associated graded algebra need not be Gorenstein; therefore do not assume perfect pairings between opposite graded layers without an additional hypothesis. Globally, the dualizing sheaf and filtration interact through Ext/duality, but the exact associated-graded duality requires care with torsion and nonsaturated layers.

## Characteristic benchmark

F=x1^4-x0³x3, G=x2^4-x0x3³. On x0=1, local coordinates t=x1,u=x2-t³,v=x3-t⁴ yield (v,(t³+u)^4-t¹²). In char 0 generic m=1, hence residual degree 12. In char 2 generic m=4, hence de=4m and reduced support exactly C. In char 2 first symbols of both equations are proportional (r=s=1 generically); this shows that r=s=1 does not imply m=1.

## Canonical scope references

- [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) proves the characteristic-dependent conormal splitting used in the degree bound.
- [STCI-R-0021](../results/quartic_mu4_degeneration.md) establishes the global characteristic benchmark for the specified quartic pair.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md) concern restricted saturated/nonsaturated first-relation settings; the ordinary filtration and duality observations here do not assert their conclusions without those hypotheses.
- The elementary Bézout residual-cycle identity is distinct from the conditional auxiliary-surface residual zero-cycle theorem [STCI-R-0019](../results/quasiprimitive_residual_cycles.md).

## Investigation priorities

Understand constraints on possible generic Hilbert functions h_i given r,s and the local CI property; relate global degrees of Q_i, torsion, and χ to duality without assuming normal flatness; separate characteristic-sensitive normal bundle arguments. No search for counterexamples or numerical exclusion until these structures are clarified.
