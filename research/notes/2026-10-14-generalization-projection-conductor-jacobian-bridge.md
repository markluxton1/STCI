# Conductor contact and the full first normal symbol

Date: 2026-10-14. Owner: `jacobian_contact_identity`, for
`projection_global_continue/global_phase_duality`. Status: **NEW WRITTEN
PROOF; independent review requested**. Previously accepted normalization,
normal-bundle, and Cartier-lift results are premises and were not rerun.

## 1. Exact local statement

Let `X=(F=0)` be an integral hypersurface in a smooth threefold over an
algebraically closed field of characteristic zero. Let
`nu:S->X` be its finite normalization. Let `C subset X` be a smooth curve
such that the full reduced inverse image is a single smooth Cartier curve
`c`, mapped isomorphically to `C`. Suppose `X` is regular at the generic
point of `C`, and `S` is regular along `c`.

Only a neighborhood of `c` is involved. Finite duality identifies the
conductor ideal on `S` with an invertible ideal

    conductor O_S = O_S(-B),
    omega_S = conductor O_S tensor nu*omega_X.          (1)

Here `B` is effective and has no component `c`. Invertibility in this
neighborhood follows from (1), since both dualizing sheaves are invertible.

Let `A` be the full common-zero divisor of the normal differential

    alpha:O_c(c) -> N_C/ambient.

Let `D_F` be the full common-zero divisor of the actual first normal
symbol of `F`, viewed as a section of
`N_C/ambient^* tensor O_C(X)`. Thus a local first symbol
`a(t)y+b(t)z` contributes
`min(ord_t a,ord_t b)` to `D_F`.

**Proposition.** There is an equality of effective divisors on `c`:

    D_F = B|c + A.                                    (2)

This is a local equality with multiplicities, not an inference from the
degrees of the two sides. It allows isolated rank drops of `alpha`.
If the differential of `nu` has rank two everywhere along `c`, then
`A=0` and (2) specializes to `D_F=B|c`.

## 2. Direct residue and finite-duality proof

Fix a closed point of `c`, and complete the local rings. Choose ambient
coordinates `(x,y,z)` with `C=(y,z)`. The function `x|C` is a uniformizer.
Its pullback, together with a local equation `u` of `c`, is a regular
system of parameters `(t,u)` on `S`, with `nu*x=t`. Write

    nu(t,u) = (t,Y(t,u),Z(t,u)),    Y,Z in (u).

The common-zero ideal of `alpha` in `O_c=k[[t]]` is exactly

    (Y_u(t,0), Z_u(t,0)).                             (3)

Choose a local generator `h` of the conductor on `S`. On the common
function field, use the hypersurface residue generator

    eta = dx wedge dy / F_z = -dx wedge dz / F_y

of `omega_X`, using either expression where its denominator is nonzero.
At least one denominator and the corresponding numerator derivative are
nonzero generically: the normalization is birational and the map is
generically an isomorphism. Pullback gives

    nu*eta = Y_u dt wedge du / (F_z composed with nu)
           = -Z_u dt wedge du / (F_y composed with nu).

Under the common-field identification in finite duality, the generator
`h nu*eta` of the right side of (1) is a generator of `omega_S`.
Consequently it is a unit multiple of `dt wedge du`. There is therefore
a single unit `epsilon` in `k[[t,u]]` such that

    F_z composed with nu = epsilon h Y_u,
    F_y composed with nu = -epsilon h Z_u.             (4)

These equalities are first obtained in the function field and then hold
in the regular local ring. Restricting (4) to `u=0` yields the exact ideal
identity

    (F_y(t,0,0),F_z(t,0,0))
      = (h(t,0)) (Y_u(t,0),Z_u(t,0))                 (5)

in the DVR `k[[t]]`. Since `F(t,0,0)=0`, the remaining partial
`F_x(t,0,0)` is identically zero. Thus the left side of (5) is precisely
the common-zero ideal of the first normal symbol. The two factors on
the right define `B|c` and `A`. Orders in (5) prove (2) point by point.
Faithful flatness of completion gives the original local statement.

The use of finite duality is concrete here: for the finite birational
extension `O_X subset nu*O_S` with common function field,

    Hom_O_X(nu*O_S,O_X)
      = {q in K(X):q O_S subset O_X}
      = conductor.

Tensoring by the invertible `omega_X` is the dualizing module of `S`.
Thus (1) uses the actual conductor, including all closed-point contact;
no reduced conductor support or first-symbol substitute is inserted.

## 3. Relation to the Jacobian-conductor formula

The coordinate identities (4) are the smooth-normalization case of
Ragni Piene, *Ideals associated to a desingularization*, Lecture Notes
in Mathematics 732 (1979), 503--517, Theorem 1 and Corollary 1,
[DOI 10.1007/BFb0066659](https://doi.org/10.1007/BFb0066659).
They give the ideal formula

    Jac(X) O_S = conductor O_S * Fitt_0(Omega_S/X).

The modern explicit coordinate statement is Theorem 3.1 of
Nuño-Ballesteros and Fernández-Hernández,
[*Disentangling mappings defined on ICIS*](https://link.springer.com/article/10.1007/s13163-024-00507-3):
the partial derivatives of an image equation pull back to a common
conductor generator times the signed maximal minors of the differential.
An [institutional full-text copy](https://riunet.upv.es/bitstreams/26a18ad6-9f8e-442c-828d-81c30b29162a/download)
is also available. This reference corroborates (4); the proof above
supplies the algebraic local argument used in this note.

## 4. Global class and the three fixed-C0 targets

Now suppose the ambient threefold is `P3`, `X` has degree `a`,
`C` has degree `d` and genus `g`, and write `H=nu*O_X(1)`.
Since `omega_X=O_X(a-4)`, (1) gives, wherever `S` is Gorenstein,

    B ~ (a-4)H-K_S.                                  (6)

If `S` is globally Gorenstein, this is a global Cartier-divisor identity.
Otherwise it is the local identity near `c` needed below. Adjunction
along the smooth Cartier curve gives

    B.c = d(a-4)+c^2-(2g-2).                         (7)

For the accepted fixed rational quartic `C0`, the singleton Cartier-lift
classification leaves three targets:

| Normalization target | `a` | `c^2` | `B.c` |
| --- | ---: | ---: | ---: |
| Smooth quadric, `c` of type `(1,1)`, `H=2c` | 8 | 2 | 20 |
| Quadric cone, `c` a smooth Cartier conic, `H=2c` | 8 | 2 | 20 |
| `P2`, `c` a line, `H=4c` | 16 | 1 | 51 |

The quadric cone is singular only at its vertex, which does not lie on
the smooth Cartier conic `c`. It is Gorenstein globally, so (6) is valid
globally and the smooth local proof applies all along `c`. No assertion
that this normalization is smooth at the vertex is needed.

## 5. Scope and warning

Formula (2) identifies the conductor contact using **both** the actual
carrier first symbol `D_F` and the transverse differential divisor `A`:

    B|c = D_F-A.

The divisor `A` alone is not the full conductor contact. This distinction
is compatible with the accepted warning that first-normal data alone
does not recover the conductor or higher horizontal multiplicity. Here
finite normalization, its actual conductor via duality, and the smooth
Cartier lift are explicit hypotheses and inputs.

The proposition does not treat a singular normalization along the lift,
a non-Cartier lift, several inverse branches, an inverse curve of higher
degree over `C`, or a carrier singular at the generic point of `C`.
It supplies no automatic bound on split residual phase orders.
