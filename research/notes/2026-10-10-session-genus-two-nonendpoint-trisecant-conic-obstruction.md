# Nonendpoint trisecant conductor: a conditional conic-model mate obstruction

Date: 2026-10-10. Author: `trisecant_conic_obstruction`.
Status: **PROVED HERE CONDITIONALLY / parent audit pending**. This is a
complete obstruction for the nonendpoint trisecant position, conditional
on the separate normal-blowup theorem and the already audited
lambda-one special-horizontal-prime reduction. It does not cover the
endpoint triple-contact line, the lambda-zero stratum, or arbitrary
carrier degrees. No canonical frontier file is edited.

## 1. Inputs and exact scope

Use the genus-two notation in the
[adjoint conic model](2026-10-09-session-genus-two-adjoint-conic-model.md).
Assume the proposed
[normal blowup lift](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md)
has passed its separate audit. Thus

    rho:M -> T subset Bl_Gamma(P3),
    T normal Gorenstein with a crepant resolution rho,
    f = the actual planes-through-Gamma pencil,
    D_T = T intersect E is a Cartier divisor,
    E = P1_Gamma x P1_f,       [D_T]=(2,2).

The class convention here gives a fiber over a point of Gamma class
`(1,0)` and a fiber over a point of the pencil class `(0,1)`.
The actual conductor on the finite normalization `S` is a line, with
entire finite-flat degree-two inverse conductor, as proved in the
[conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md).
The proper birational map `T -> S` contracts exactly the horizontal
sigma-exceptional curves. All other sigma-exceptional primes are the
vertical (-2) curves resolved by rho.

Assume a mate exists in the lambda-one stratum. Then `f.c#=1` and

    c# ~ L-Z,       Z effective rational sigma-exceptional,
    K_M.Z=1,       Z.E=-c#.E for every exceptional prime E.

The accepted
[no-zero-horizontal audit](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md)
forces the special horizontal prime

    B=e0-e_i-e_j,       B^2=-3,       f.B=1,       c#.B=0.

There are at most two horizontal primes; any second one is disjoint
from B on M. A horizontal prime maps in E to the entire fiber over
its fixed point on Gamma. Write the image of B as `B_T` and its Gamma
point as `p_B`.

For this note assume Gamma meets C0 in three distinct points. For the
literal rational quartic these are the nonendpoint trisecants: the
ruling lines with fixed `[s^3:t^3]=[alpha:beta]`, where `alpha beta !=0`.
The diagonal automorphisms normalize these to `alpha=beta=1`. The
three contacts then occur at `t^3-s^3=0`, with distinct Gamma coordinates
and distinct f-coordinates. The argument uses only those two
distinctness statements.

## 2. A necessary singleton-fiber test

The image `c_T` of c# in T is a section of the pencil and is isomorphic
to P1. Indeed `f|c#` is degree one, and the image is the section of the
separated morphism `T -> P1` determined by that inverse parameterization.
Thus c_T has only one point over each contact with Gamma.

At a Gamma point lying on C0, the mate polynomial vanishes. It therefore
vanishes at every point of the entire inverse conductor over that point.
Its divisor on S has support only the lifted curve c. In particular,
every point of that conductor fiber must be the point of c over that
Gamma point.

Away from the images of horizontal exceptional curves, `T -> S` is an
isomorphism. Consequently the support of `D_T -> Gamma` over a C0-contact
away from those images must be a singleton. Two distinct points are
impossible. This is a support test on the actual conductor, not an
even-valuation or tangent-only test.

Do not assume at this stage that p_B belongs to C0. The coefficient of
B in the exceptional correction can be zero when another horizontal
prime is present. There are nevertheless at least two C0-contact points
away from p_B, whether p_B is a contact or not.

## 3. Every reducible residual divisor is excluded

Since B_T is a fiber component of D_T, its multiplicity is one or two.

If its multiplicity is two, the remaining divisor has class `(0,2)`.
At least two C0-contact points away from p_B have distinct f-coordinates. Each must
lie in the remaining divisor, so that divisor consists of two distinct
fibers of f. But they give two distinct conductor points over every
Gamma point away from p_B, contradicting section 2. A double f-fiber
cannot contain the two distinct f-contact coordinates.

Now suppose B_T has multiplicity one, and write

    D_T=B_T+R,       [R]=(1,2).

If R is reducible, its components can only have the following classes,
including repetitions:

    (1,1)+(0,1),     or     (1,0)+(0,2).

An irreducible `(1,1)` component is a graph over f and maps isomorphically
to Gamma. Together with an f-fiber it has singleton fibers over at most
one Gamma point: their unique intersection. There are at least two C0-contact
points away from p_B, so the first case fails. Reducibility of the
`(1,1)` component reduces to the second case.

In the second case the `(1,0)` component is another fiber B'_T over
a Gamma point p_B'. If the `(0,2)` part consists of distinct f-fibers,
the third C0-contact away from p_B and p_B' has two inverse points and
fails the support test. If p_B'=p_B, this was already the
multiplicity-two case. The only remaining possibility is

    D_T=B_T+B'_T+2F0,       p_B' != p_B.

If either p_B or p_B' is outside C0, there are at least two contacts
away from both. Their distinct f-coordinates cannot both lie on the
double f-fiber F0. Therefore p_B and p_B' must be two of the three
contacts in this last remaining possibility. The last contact must
have f-coordinate f0. The f-coordinate of the contact over p_B is
different from f0. At that point D_T is locally just the reduced smooth
component B_T: neither B'_T nor F0 passes there. The defining equation
of T restricted to the smooth E therefore has nonzero differential;
T itself is smooth there. Thus c# actually intersects B on M there,
contradicting `c#.B=0`.

This excludes all reducible and nonreduced residual possibilities,
including double f-fibers and double horizontal fibers. It does not
assume that the entire conductor upstairs is reduced.

## 4. Irreducible R forces only two A-chains on B

An irreducible R of class `(1,2)` is a graph over f. Its two quadratic
coefficient polynomials have no common zero (a common factor would give
an f-fiber component), so R is a smooth P1 and `R -> Gamma` has degree
two. It is separable in characteristic zero.

B is then the only horizontal sigma-exceptional prime: any other one
would supply another Gamma-fiber component in D_T. Therefore
`K_M.Z=1` gives `coeff_B(Z)=1`. The mate does vanish on B after
pullback, and full support forces p_B to belong to C0. This conclusion
is used only in the sole-horizontal case, where its coefficient is
positive. The two C0-contact
points away from p_B must be singleton fibers of R by section 2. They
are its two branch values. A separable degree-two map from P1 has total
ramification degree two, so it is unramified over p_B. Thus R meets B_T
in exactly two distinct transverse points.

Every singular point of T on B_T lies at B_T intersect R. At a point
where R is absent, the restriction of the T equation to E has nonzero
differential, so T is smooth. At either transverse intersection choose
formal coordinates `(u,v,r)` in the smooth ambient blowup, with E
given by r=0 and the two components given by u=0 and v=0. The equation
of T is

    uv+r*h(u,v,r)=0.

If singular, its quadratic part has rank at least two because its
u,v minor is nondegenerate. Since T is Du Val, it is of type A_n.
The formal splitting lemma can be made with r as parameter: the
changes in u,v are zero modulo r, giving the usual form
`xy+r^(n+1)=0`. The two curves in r=0 meet the opposite endpoints of
the exceptional A_n chain. This is the standard rank-two A_n form;
compare [Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
In particular D_n and E_n branching is not permitted at these two
transverse intersections.

The sigma-fiber containing B is therefore B(-3), with at most two
endpoint A-chains. There is no length restriction in this argument.

## 5. The correction coefficient is strictly less than one

The contact of c_T with B_T over p_B must be singular on T, because
c#.B=0. Let the A_n chain over this point have nodes 1,...,n, with B
attached at node 1. The smooth embedded lift meets exactly one node k
transversely, with `1<=k<=n`; this is the accepted singleton-contact
and local-uniformizer consequence. It cannot meet the other chain,
since c_T has just its one f-coordinate over p_B. Write the other
chain length as m>=0 (m=0 means there is no second exceptional chain).

Put `a=coeff_B(Z)`. Solving the first A_n chain gives its neighboring
coefficient

    z1 = n/(n+1)*a + (n+1-k)/(n+1).

The neighboring coefficient of the other chain is
`m/(m+1)*a`. The equation `Z.B=-c#.B=0` therefore gives

    a = ((n+1-k)/(n+1)) /
        (3 - n/(n+1) - m/(m+1)) < 1.

The numerator is strictly less than one; the denominator is strictly
greater than one. The inequality holds for every n>=1, m>=0 and every
contact node k, without a finite graph cutoff.

On the other hand B is the sole horizontal prime, all vertical
exceptional primes have K-degree zero, and `K_M.B=1`. Hence

    a=K_M.Z=1,

a contradiction. This excludes the irreducible residual case.

## 6. Boundary and preserved failed shortcuts

Conditional on the exact structural inputs in section 1, no lambda-one
mate exists when the conductor line is a nonendpoint trisecant of C0.
Sections 3--5 cover all residual divisor strata of D_T.

The endpoint triple-contact lines remain outside this argument. Their
single Gamma-contact does not force two distinct branch values of R.
The full lambda-zero and genus-two problems also remain open.

Two tempting shortcuts are deliberately not used. First, c#.B=0 does
not imply c_T avoids B_T: a vertical ADE chain can separate their
strict transforms. Second, the transverse B_T/R intersection need not
be an A1 singularity; completing `uv+r h` can give an arbitrarily long
A_n chain. The all-length correction calculation, rather than an
A1-only calculation, is the obstruction above.
