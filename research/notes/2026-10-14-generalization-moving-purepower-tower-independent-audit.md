# Moving pure-power relations: uniform obstruction bundles and finite-order lifts

Date: 2026-10-14. Status: **independently proved new finite-order lifting
theorem**, with the scope stated below. The accepted conormal identification
for the rational quartic is used as a premise. No accepted chart-transition,
normal-bundle, or constant-direction computation is repeated.

This note audits the proposed generalization of the next-order calculation in
[the moving linear relation review](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md).
The apolar quotient, the successive gluing obstruction, the vanishing range,
and the Cohen--Macaulay assertion all pass. The construction supplies embedded
finite-order thickenings; it does not supply a global carrier or an STCI pair.

## 1. Hypotheses and the precise truncation

Let `C` be a smooth curve embedded in a smooth threefold `X` over a field of
characteristic zero. Write `I=I_C` and suppose its actual conormal bundle is

    E=I/I^2=H^-1 tensor V,

where `H` is a line bundle and `V` is a constant two-dimensional vector space.
Let `M` be a line subbundle of `V tensor O_C`, and put

    W=H^-1 tensor M subset E,
    A=W^r subset Sym^r E,       r>=1.

The subbundle assumption means that the moving direction has no base points.
The initial relation is the pure power `m^r`; there is no divisor of zeros
attached to its saturation. Fix a desired truncation `N=r+g`, with `g>=1`.
The construction seeks an ideal sheaf `J_N` in the actual ambient threefold,
containing `I^N`, locally of the form

    J_N=(p,I^N),       initial(p)=m^r.

Its initial relation sheaves in every degree `j<N` must be precisely

    0                                      if j<r,
    W^r tensor Sym^(j-r)E                   if r<=j<N.

Thus the last prescribed principal-relation degree is `N-1=r+g-1`. There
is no asserted second independent relation before that degree. A new full
truncation relation appears in degree `N`.

## 2. The obstruction bundle in every order

For the passage from truncation `r+k` to truncation `r+k+1`, with `k>=1`, put

    B_k=Sym^(r+k)E / (W^r tensor Sym^k E),
    Q_k=Hom(W^r,B_k).

The multiplication image is a subbundle: locally a basis with the first
vector spanning `W` makes its image the span of the `k+1` monomials divisible
by the first vector to power `r`. Its cokernel therefore has rank `r` and
has no torsion.

Let `M_perp` be the annihilator line of `M` inside `V^* tensor O_C`. The
determinant sequence gives

    M_perp=M tensor det(V)^*.

Under the characteristic-zero perfect symmetric pairing, the annihilator of
`M^r Sym^k V` is exactly

    M_perp^(k+1) tensor Sym^(r-1)V^*.

To verify this equality, choose a fiber basis `(x,y)` with `x` spanning `M`.
The relation image has monomials `x^r` times every monomial of degree `k`.
Its annihilator consists of dual monomials with dual `y`-exponent at least
`k+1`. These are exactly `(y^*)^(k+1)` times all degree-`r-1` dual binary
forms. Both sides are rank-`r` bundles, so this fiber calculation proves the
bundle equality, rather than merely a pointwise dimension count.

Restoring the conormal twist and dualizing gives the canonical formula

    Q_k = H^-k tensor M^(-(r+k+1))
          tensor det(V)^(k+1) tensor Sym^(r-1)V.

The determinant factor is constant. Consequently the claimed formula
without this factor is correct after choosing a nonzero element of `det(V)`;
it is the same bundle up to a constant one-dimensional vector-space factor.
The coefficient `r+k+1` of the movement degree is essential.

## 3. Why H^1(Q_k) controls gluing ideals in the actual ambient space

The initial truncation exists without an obstruction: take the preimage of
`W^r` under `I^r -> I^r/I^(r+1)`. It is an ideal because multiplication by
`I` lands in `I^(r+1)`. This gives `J_(r+1)`.

Suppose `J_n`, with `n=r+k`, has already been constructed. On a suitable
open cover choose its local relation generators `p_i` and lift each to the
next ambient truncation. On overlaps there are units `a_ij` such that

    p_i-a_ij p_j belongs to I^n.

The degree-`n` discrepancy, normalized by the leading relation frame, defines
a section of `Hom(W^r,Sym^n E)`. Its image in `Q_k` is independent of the
choice of overlap unit, because a correction of degree `k` to that unit adds
exactly a multiple of the leading relation in `W^r Sym^k E`.

On a triple overlap the discrepancy is a multiple of `p_l`. Modulo
`I^(n+1)`, its degree-`n` part lies in `W^r Sym^k E`. Indeed, multiplication
by the leading form `m^r` is strict for the normal filtration: that form is
a nonzerodivisor in the local symmetric algebra. It follows that the images
of the discrepancies form a Cech 1-cocycle in `Q_k`.

If `H^1(Q_k)=0`, choose local degree-`n` corrections whose coboundary kills
this cocycle. The remaining discrepancies are in `W^r Sym^k E`. They are
absorbed by degree-`k` corrections to the overlap units, which remain units
since `k>=1`. The corrected local ideals `(p_i,I^(n+1))` therefore glue to
an actual ideal sheaf `J_(n+1)` on `X`.

Every step uses the canonical sheaves `I^n/I^(n+1)` and local choices of
generators. It assumes neither a global projection to `C` nor a global
splitting of the formal neighborhood. At each step, local lifting exists
simply by lifting the local ambient equation; the obstruction is its gluing.

This proves the following finite-order statement: if

    H^1(C,Q_k)=0 for every 1<=k<g,

there exists an embedded thickening `Y_N=V(J_N)` with `N=r+g` and precisely
the principal initial relation sheaves specified in Section 1. Vanishing
does not make the choices canonical; the corresponding `H^0(Q_k)` controls
available changes to each lift.

## 4. The initial algebra and Cohen--Macaulay property

Locally, the leading form of `p` is a nonzerodivisor in `Sym E`. Thus a
product with `p` has precisely the sum of its factors' normal orders.
Truncating by `I^N` gives

    gr_I(O_X/J_N)
      = Sym E / (W^r Sym E, all degrees >=N).

Every remaining homogeneous layer is locally free on `C`, because `W` is
a subbundle. This verifies the claimed initial relation sheaves and retains
the full torsion statement: there is no hidden torsion in any layer below
the truncation.

At a closed point of `C`, each nonzero layer has depth one as an ambient
module, since it is locally free over the smooth curve. Successive uses of
the depth lemma show that `O_X/J_N` has depth at least one. Its support has
dimension one, so `Y_N` is Cohen--Macaulay. This argument is intrinsic to
the filtration and does not need a retraction even for the flatness claim
one might otherwise make in local coordinates.

## 5. Uniform vanishing range on the rational quartic

On `C=P^1`, write `H=O(lambda)` and `M=O(-e)`, with `e>=0`. The constant
factor in Section 2 has dimension `r`, and hence

    Q_k=O(q_k)^r,
    q_k=(r+k+1)e-lambda k.

For the accepted rational-quartic conormal splitting, `lambda=7`. Since
`H^1(P^1,O(q))=0` exactly when `q>=-1`, every prescribed lift up to
truncation `r+g` is unobstructed whenever

    (r+k+1)e-7k>=-1 for every 1<=k<g.

If `e<7`, this affine function decreases with `k`, so the uniform condition
is exactly

    (r+g)e>=7(g-1)-1.

If `e>=7`, all these obstruction groups vanish for every finite `g`. The
case `g=1` has no lifting step and is automatically allowed. For `e=0`,
the formula gives `q_k=-7k`; no vanishing conclusion applies beyond the
initial truncation, in agreement with the accepted constant-direction
obstructions.

For example, a pure power moving with degree one has all prescribed steps
through gap `g` unobstructed whenever `r>=6g-8`. This extends the previously
reviewed one-step threshold `r>=4`. For degree two the corresponding
condition is `2r>=5g-8`. These are sufficient vanishing thresholds, not
necessary compatibility conditions: a nonzero obstruction group can still
contain a zero actual obstruction.

On a curve of positive genus the bundle formula remains valid, but the
`q>=-1` vanishing criterion is specific to `P^1`. The appropriate hypothesis
is the actual vanishing of each line-bundle `H^1` in Section 3.

## 6. Scope and consequences for the research frontier

This proves that finite-order normal compatibility cannot uniformly exclude
moving pure-power first relations in the vanishing range. For any fixed
finite gap, sufficiently large first relation order makes the entire tower
of these obstruction groups vanish, including the actual nonlinear ambient
transition effects encoded by the successive discrepancy cocycles.

The construction gives genuine embedded Cohen--Macaulay finite-order
thickenings, but it does not impose the full-algebra conditions of a complete
intersection presentation. In particular, if `r>1`, the generic top normal
layer of `Y_N` has dimension `r` and is annihilated by the maximal ideal of
the generic Artin algebra. Its socle therefore has dimension at least `r`;
this constructed truncated algebra cannot itself be a zero-dimensional
complete intersection. If `r=1`, it is curvilinear locally, but a global
STCI presentation is still not supplied.

No carrier degree, global equation degree, projective complete-intersection
pair, or algebraization of an infinite compatible tower is claimed. Even
when all finite steps have vanishing obstruction groups, the assertion here
is restricted to finite orders. To progress toward an STCI exclusion, one
must use a new independent relation, Gorenstein/socle constraints, actual
global equations, or another condition beyond this principal-relation tower.

## 7. Audit verdict

**Pass**, with the constant determinant factor made explicit and with the
truncation understood as `J_N=(p,I^N)` for `N=r+g`. The claimed uniform
obstruction bundle, vanishing inequality, induction in the actual ambient
space, exact initial relation sheaves, and Cohen--Macaulay conclusion are
proved above. The stronger global carrier/STCI conclusions are not part of
the theorem and do not follow from it.
