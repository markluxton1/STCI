# Saturated duality excludes moving pure-power first relations in generic CI thickenings

Date: 2026-10-19.
Status: **PROPOSAL WITH INDEPENDENT REVIEW PASS; not promoted.**
Independent audit: [filtered-bridge review](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md).
Author: filtered-algebra worker, with the degree-s shortcut suggested by
the independent filtered-bridge reviewer. No canonical record is edited
or promoted.

## 1. Exact theorem proposed

Let `k` be algebraically closed of characteristic zero. Let `C` be a
smooth connected projective curve in a smooth threefold `X`, with
balanced split conormal

    E=N_(C/X)^*=H^(-1) tensor V,   dim_k V=2.

Let `Y` be an ACTUAL locally complete-intersection thickening with
`Y_red=C`. Thus `O_Y` is pure of dimension one and Gorenstein. Set
`J=I_C O_Y`, and write

    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Assume the FULL generic ordinary initial ideal is the coprime binary
complete intersection

    gr_(J_eta)(O_(Y,eta)) = k(C)[x,y]/(m^r,g_s),
    2 <= r < s,                 gcd(m,g_s)=1.               (1)

Let `M subset V tensor O_C` be a line subbundle whose generic line is
spanned by `m`, put `W=H^(-1) tensor M`, and assume the ACTUAL first
relation is saturated:

    K_r=W^r as a subbundle of Sym^r E.                    (2)

If `deg M=-e<0`, **no such `Y` exists**.

This concerns the full initial ideal and the actual first relation
sheaf. A repeated factor in a tangent form alone does not give (1) or
(2). No hypothesis is made about normal orders of chosen defining
equations, their joint generation of the first relation, smoothness of
the full root, or flatness of later ordinary layers. The proof below
allows arbitrary such later torsion in advance.

For the fixed rational quartic `C0` in `P3`, the accepted conormal is
`E=O_P1(-7)^2`. The theorem would close this specified actual-thickening
lane; it is not an unrestricted STCI claim. In the broader intersection
problem `C subset Y_red`, the unique-support purity argument below does
not apply to the whole `Y` when other components are present.

## 2. Dependencies and authority

The characteristic-zero apolar bundle calculation is an accepted input
from [the pure-power tower](2026-10-14-generalization-moving-power-obstruction-tower.md)
and [its independent audit](2026-10-14-generalization-moving-purepower-tower-independent-audit.md).
For every `j>=r-1`, it gives

    Sym^j E/(W^r tensor Sym^(j-r)E)
       = H^(-j) tensor M^(-(j-r+1)) tensor Sym^(r-1)V,     (3)

where at `j=r-1` the denominator is zero.

The actual socle line and Gorenstein MCM duality are accepted inputs in
[the independent socle audit](2026-10-13-generalization-socle-independent-audit.md),
sections 2--4. That audit does not itself supply the general saturated
pairing used below; its ordinary pairing statements have more
restrictive equality/torsion-free hypotheses. The new bridge consists
of the saturated pairing, exact early layers, and degree-s contradiction.

[STCI-R-0009](../results/moving_purepower_boundary.md) already excludes a
uniform fiberwise graded CI with this first moving power. The proposed
proof reaches an actual-thickening exclusion directly and does not need
to assume that uniformity or invoke it as an intermediate conclusion.
No inherited proof or computation is rerun.

## 3. Saturated powers and exact global duality

The generic graded algebra in (1) is Gorenstein, with last nonzero degree

    d=r+s-2.

Purity implies `J^(d+1)=0` globally: that ideal is a generically zero
subsheaf of `O_Y`, which has no nonzero finite-support subsheaf.

Let `P_i` be the saturation of `J^i` in `O_Y`, namely the inverse image
of the finite-support torsion of `O_Y/J^i`. Equivalently, locally,

    P_i=O_Y intersect (J_eta)^i inside O_(Y,eta).

Then `P_0=O_Y`, `P_1=J`, `P_(d+1)=0`, and `O_Y/P_i` is pure CM (or
zero). Every `P_i` is MCM as well. Generic multiplication containments
and saturation give

    P_i P_j subset P_(i+j),   J P_i subset P_(i+1).

Thus `B_i=P_i/P_(i+1)` is annihilated by `J`; it is a vector bundle on
`C`, because it is a subsheaf of the pure sheaf `O_Y/P_(i+1)`.

Let `S=Ann_Y(J)` be the actual socle line. For an actual CI of degrees
`a,b` in `P3`, its accepted value is
`S=omega_C tensor O_C(4-a-b)`, but no explicit formula is needed here.

Set `Q_i=Ann_Y(P_i)`. These ideals are saturated: a finite-support
section of `O_Y/Q_i` would multiply `P_i` into a finite-support subsheaf
of `O_Y` and therefore would already lie in `Q_i`. At the generic point,
the graded Gorenstein property in (1) gives

    Ann((J_eta)^i)=(J_eta)^(d+1-i).

Both global ideals with those generic fibers are saturated. Hence

    Q_i=P_(d+1-i).                                      (4)

On a Gorenstein curve, MCM duality is exact on MCM modules. Dualize

    0 -> B_i -> O_Y/P_(i+1) -> O_Y/P_i -> 0.

The local `Ext^1_Y(O_Y/P_i,O_Y)` vanishes. Since `J B_i=0`, every map
`B_i -> O_Y` lands in `S`. Exactness and (4) yield

    B_(d-i) = Hom_C(B_i,S),
    B_i tensor B_(d-i) -> S is perfect everywhere.        (5)

The map is induced by actual multiplication. This is a statement about
the SATURATED filtration and makes no assumption that ordinary layers
are torsion-free. No global retraction `Y -> C` is asserted.

## 4. Saturation of the first relation controls all early layers

For `j<r`, `K_j` has generic rank zero. It is a subsheaf of the bundle
`Sym^j E`, so `K_j=0`. Thus

    J^j/J^(j+1)=Sym^j E,                  0<=j<r.         (6)

For `r<=j<s`, products of (2) give

    W^r tensor Sym^(j-r)E subset K_j.

The left side is saturated in `Sym^j E`: choose `W` as one local basis
vector of `E`; the complementary monomials give a free quotient of rank
`r`. Assumption (1) gives equal generic ranks. The quotient between the
two sides is a rank-zero subsheaf of that free quotient, so it vanishes:

    K_j=W^r tensor Sym^(j-r)E,            r<=j<s.         (7)

Every ordinary layer through index `s-1` is therefore a bundle. Its
successive extensions show that `O_Y/J^i` is CM for `i<=s`, whence

    P_i=J^i,                             0<=i<=s.        (8)

Combining (3), (6), and (7),

    B_(r-1)=H^(-(r-1)) tensor Sym^(r-1)V,
    B_(s-1)=H^(-(s-1)) tensor M^(-(s-r))
                                      tensor Sym^(r-1)V. (9)

This is where a SATURATED ACTUAL first relation is indispensable;
generic first-symbol information does not establish (7) or (8).

## 5. The socle degree forces an impossible degree-s quotient map

Write `lambda=deg H` and `g=s-r`. The perfect pairing of the two
rank-r bundles in (9) gives

    deg S=-lambda*d+e*g.                                (10)

Only degrees are needed; the base need not be rational and no
identification of equal-degree line bundles is assumed.

By (8), `P_s=J^s`, so `Sym^s E -> B_s` is surjective. First-relation
multiples vanish, hence there is an induced surjection

    A_s := Sym^s E/(W^r tensor Sym^(s-r)E) -> B_s.        (11)

The source, by (3), is

    A_s=H^(-s) tensor M^(-(g+1)) tensor Sym^(r-1)V.

The target, by (5) and (6), is

    B_s=Hom_C(B_(r-2),S)
       =H^(r-2) tensor S tensor (Sym^(r-2)V)^*.

Its rank is `r-1>0`. Therefore the bundle of homomorphisms in (11) is
a constant vector-space bundle tensored with the line

    H^(s+r-2) tensor S tensor M^(g+1).

Using `s+r-2=d` and (10), that line has degree

    lambda*d + (-lambda*d+e*g) - e(g+1) = -e < 0.

A negative-degree line bundle on a smooth projective curve has no
nonzero global section. Consequently EVERY global map `A_s -> B_s`
is zero, contradicting the surjection (11). This proves the proposed
nonexistence theorem.

An equivalent determinant calculation retains the prospective second
relation: the kernel `T` in (11) would be a line of degree
`-s*lambda+s*e`, and `Hom(T,A_s)` would be a constant vector space
tensored with a line of degree `-(r-1)e<0`. The Hom-vanishing argument
above avoids introducing this unnecessary extra line.

For `C0`, (10) is the exact necessary equality

    mu=7d+14-4(a+b)=e(s-r).

The contradiction uses the actual degree-s quotient map, not this
scalar equality alone.

## 6. Frontier impact and unresolved cases

The separate independent review passed. Within its exact hypotheses,
this closes actual lci thickenings with a
moving pure-power first relation satisfying (1)--(2), even when later
ordinary layers were initially allowed arbitrary special-point
degeneration. It supplies a more direct actual-CI interface for this
specific initial pattern than STCI-R-0006, without its smooth-root,
chosen-symbol, or finite-gap hypotheses.

It does not treat nonsaturated first relations, generic non-CI initial
ideals, or general reducible/nonreduced full root schemes. The
unrestricted characteristic-zero `C0` question remains open.

No computation is required. Independent review must reconstruct (4)--(5),
the rank/saturation step (7), the accepted apolar input (3), and the
surjectivity in (11). Generic CI Hilbert symmetry, actual Gorenstein
duality, and global projectivity all have explicit roles and must not
be silently dropped.
