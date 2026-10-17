# Quasiprimitive multiplicity-ten filtration: necessary numerical reduction

Date: 2026-10-11.

Status: **DIRECT PROOF AUDIT AND NECESSARY NUMERICAL REDUCTION**. This note
does not exclude degree `(5,8)`, does not classify embedded multiplicity-ten
structures, and does not establish that `C0` is not an STCI.

## 1. Scope and inputs

Work over an algebraically closed field of characteristic zero. Let

`C=C0=[s^4:s^3 t:s t^3:t^4]`,

and suppose `X=V(F5,G8)` has reduced support exactly `C`. The equations have
no common surface factor, so `X` is a projective local complete intersection
of degree 40 and generic multiplicity ten. The argument below requires its
generic transverse algebra to be curvilinear. For a hypothetical defining
pair that requirement follows from the repository's P-011: the quintic must
have generic normal order one. This note audits the filtration argument,
not P-011.

The conormal input is `N_C^*=O_P1(-7)^2`. No assertion is made that `X` is
primitive at every point, that the first-normal quotient of the equations
has regular ratio, or that the ordinary nilradical-power quotients are line
bundles.

Relevant existing records are P-016 and P-042 in
[RESEARCH_RECORD](../RESEARCH_RECORD.md),
[the local multiplicity-six pairing audit](2026-10-05-mf6-pairing-audit.md),
and [the uniform saturated-filtration audit](2026-10-06-session-uniform-audit.md).
The primary source was freshly opened for this audit:
[Manolache, *Duality for Gorenstein multiple structures on smooth algebraic
varieties*, 2023](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf),
printed pp.142–145. The theorem concerns canonical Gorenstein multiplication
duality; its Remark 2 identifies the filtrations for quasiprimitive
structures. The proof below is a direct local algebra proof for this setting.
The Boratyński original was not freshly fetched in this audit.

## 2. Saturated filtration and duality at every support point

Complete at a support point, choose a tangent parameter `t`, and put
`R=k[[t]]`, `K=Frac(R)`. The completed ring `B` of `X` is finite over `R`:
its two normal coordinates are nilpotent. Cohen–Macaulayness makes `t` a
nonzerodivisor, hence `B` is finite free of rank ten. The special fibre is an
Artin complete intersection and is Gorenstein. Lifting a Frobenius functional
from that fibre produces a functional `lambda:B->R` for which
`B -> Hom_R(B,R)`, `b |-> lambda(b * _)`, is an isomorphism. The determinant
is a unit because it is nonzero modulo `t`.

Generically `B_K=K[v]/(v^10)`. Define the canonical saturated ideals

`N_i=B intersect v^i B_K`, for `0<=i<=10`.

Every quotient `B/N_i` is torsion free over the DVR `R`, so the relevant
submodules split as `R`-modules. Each `E_i=N_i/N_(i+1)` has rank one and is
free. Also `B/N_1=R`: it is a finite integral `R`-subalgebra of `K`, and `R`
is integrally closed. Generic computation, followed by torsion freeness,
gives `Ann_B(N_i)=N_(10-i)`.

For any ideal `J`, its orthogonal for the Frobenius pairing equals its
annihilator. Indeed, if `lambda(bJ)=0`, then `lambda(bjc)=0` for all `c`,
and perfectness forces `bj=0` for every `j`. Consequently `N_9` is dual to
`B/N_1=R`. The restriction of `lambda` identifies `N_9` with `R`, and the
induced pairings

`E_i tensor E_(9-i) -> E_9`

are perfect. For example any functional on `E_(9-i)` extends to `B` by the
saturated direct-summand property; its representing element lies in `N_i`,
and its kernel on passage to the graded piece is `N_(i+1)`. This proves the
claim for the actual multiplication maps, including at nonprimitive points.

The filtration glues because it is intrinsically the saturation of nilradical
powers. Put `L=E_1`. The iterated multiplication `L^i->E_i` is generically an
isomorphism of line bundles, with effective zero divisor `D_i`. Thus

`E_i=L^i(D_i)`, `D_0=D_1=0`.

Associativity and perfect complementary multiplication yield identities and
inequalities of actual divisors, rather than only numerical classes:

`D_i+D_j <= D_(i+j)` for `i+j<=9`,

`D_i+D_(9-i)=D_9` for `0<=i<=9`.

The conormal map onto `E_1` is surjective: the ambient ideal of `C` maps onto
the nilradical, and its square maps into `N_2`. Therefore
`O(-7)^2 ->> L` and `l=deg L>=-7`.

## 3. Exact socle and genus identities

The top piece is `Ann_(O_X)(I_C)`. Gorenstein duality identifies it with
`omega_C tensor (omega_X|C)^(-1)`. Complete-intersection adjunction gives
`omega_X=O_X(5+8-4)=O_X(9)`, while `O_C(1)=O_P1(4)` and `omega_C=O(-2)`.
Hence

`E_9=O(-38)`, and `9l+d_9=-38`.

Effectivity of `D_9`, together with the conormal quotient bound, leaves
exactly three possibilities:

| `l` | quotient direction degree `e=l+7` | `d_9` |
| --- | --- | --- |
| -7 | 0 | 25 |
| -6 | 1 | 16 |
| -5 | 2 | 7 |

The arithmetic genus is `p_a(X)=1+40*9/2=181`, so `chi(O_X)=-180`.
Complementary duality gives `sum_(i=0)^9 d_i=5d_9`; therefore additivity of
Euler characteristic gives

`chi(O_X)=10+45l+5d_9=-180`.

This is precisely five times the socle degree relation, plus ten. It gives
no further independent constraint. A globally primitive structure is
impossible numerically: it would have `D_9=0` and `9l=-38`.

## 4. Complete necessary divisor inequalities in four divisors

Write `A=D_2`, `B=D_3`, `C'=D_4`, and `T=D_9` (the prime on `C'`
distinguishes this divisor from the support curve). The complete defect
sequence is necessarily

`(D_0,...,D_9)=(0,0,A,B,C',T-C',T-B,T-A,T,T)`.

All its effectivity and superadditivity conditions are equivalent to

`0<=A<=B<=C'`,

`2A<=C'`, `2C'<=T`, `A+B+C'<=T`, and `3B<=T`.

Here every inequality holds coefficientwise at every point. To check
equivalence, multiplication by `E_1` gives monotonicity; the new unordered
pairs with both indices at least two are `(2,2)`, `(2,3)`, `(2,4)`, `(2,5)`,
`(2,6)`, `(2,7)`, `(3,3)`, `(3,4)`, `(3,5)`, `(3,6)`, `(4,4)`, and `(4,5)`.
Substitution gives exactly the displayed inequalities, their repetitions,
and complementary equalities. No further pair occurs with index sum at most
nine.

For degrees `a=deg A`, `b=deg B`, `c=deg C'`, this implies:

| `l` | `a` | `b` | `c` |
| --- | --- | --- | --- |
| -7 | 1 through 6 | at most 8 | at most 12 |
| -6 | 0 through 4 | at most 5 | at most 8 |
| -5 | 0 or 1 | at most 2 | at most 3 |

The positive lower bound in the first row additionally uses P-010. If
`l=-7` and `D_2=0`, the canonical embedded triple has pieces `O,L,L^2`;
in codimension two it is primitive everywhere. One normal coordinate
generates its nilradical locally by Nakayama, and a transverse normal
coordinate supplies a smooth local containing surface. Thus it contradicts
the repository's independently audited primitive-triple exclusion. No such
extra lower bound is asserted for `l=-6` or `-5`.

An exact exhaustive enumeration of the resulting degree inequalities gives
198 triples for `l=-7`, 97 for `l=-6`, and 13 for `l=-5`: **308 necessary
degree triples**, not 308 classified structures. The last row is explicitly

`(0,0,0),(0,0,1),(0,0,2),(0,0,3),`

`(0,1,1),(0,1,2),(0,1,3),(0,2,2),(0,2,3),`

`(1,1,2),(1,1,3),(1,2,2),(1,2,3)`.

The standalone enumerator uses only Python's standard library and tests each
retained sequence against every original superadditivity and complementary
condition. It also tests the compact conditions against the original
conditions on every degree triple in the finite bounding boxes. Its source
and exact output are linked in the accompanying execution record:
[multiplicity-ten degree enumeration](../validation/2026-10-11-multiplicity-ten-filtration/execution-record.json).

## 5. Why this does not classify multiplicity-ten structures

Actual coefficientwise divisor data are stronger than the degree
inequalities. Even actual divisor data and perfect graded pairings do not
by themselves construct compatible local saturated ideals, higher normal
jets, or a global embedding in `P^3`. A locally embedded Gorenstein multiple
curve need not be arithmetically Gorenstein. The global complete intersection
requires that stronger property, as recorded in P-035.

The degree of `T` is not the degree of the common first-normal Fitting
divisor. Already the finite-flat multiplicity-ten local complete intersection

`R[[x,y]]/(t*x-y^2,x^5)`

has generic algebra `K[y]/(y^10)`, saturated defects
`D_i=floor(i/2)[t=0]`, and first-normal image `t*x`. Its common Fitting divisor
is `[t=0]`, whereas `D_9=4[t=0]`. The `R`-basis
`x^a*y^b`, `0<=a<5`, `0<=b<2`, proves finite flatness and rank ten;
`x=t^(-1)y^2` proves the asserted filtration. A second model

`R[[x,y]]/(t*x-y^5,x^2)`

has `D_i=floor(i/5)[t=0]`, so its first four defects vanish even though it
is nonprimitive at the special point. These are local shields against false
filtration shortcuts, not projective candidates.

The strongest verified conclusion here is therefore the three possible
line degrees, the exact coefficientwise four-divisor reduction, and the
308 necessary numerical triples. A `(5,8)` exclusion still needs an embedded
extension obstruction, a surface/conductor argument, or another condition
that removes all surviving divisor and higher-jet data.
