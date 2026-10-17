# Independent audit: cohomology for the uniform root-lifting tower

Date: 2026-10-15. Reviewer: `tower_finite_audit`, with a separate
`square_zero_cartier` subreview of the equation-unit issue.
Status: **PASS for the stated cohomology, coefficient twists, and
conditional relation-gap consequence**. The finite-determinacy theorem
also requires the relative embedded-Cartier lifting argument, assigned
to a separate conceptual reviewer. No accepted chart computation,
first-incidence verifier, or second-obstruction verifier was rerun.

Reviewed proposal:
[uniform root-tower finite determinacy](2026-10-15-generalization-uniform-root-tower-finite-determinacy.md).
The accepted first and second obstruction calculations are premises;
this review concerns the new all-order structural input.

## 1. The precise general setting

Let the ground field be fixed, let

    E = P1_base x P1_fiber,
    J = O_E(-lambda,1),

and suppose that `E` is an effective Cartier divisor in a fixed ambient
formal neighborhood with conormal `J`. Here `lambda` is an integer,
`r>=1`, `epsilon>=0`, and

    lambda > 3 epsilon.                              (1)

Let `U` be the open subset of

    P H0(E,O_E(epsilon,r))

parametrizing equations nonzero on every fiber of `E -> P1_base`.
No smoothness or reducedness condition is imposed on their root
divisors. Each root divisor `Z` is an effective Cartier divisor on `E`
and is finite flat of degree `r` over the base. In particular repeated
root directions and nonreduced root divisors are retained.

For a fixed root the proposed step-`k` coefficient sheaf is

    L_k = N_(Z/E) tensor J^k|Z
        = O_Z(epsilon-lambda k,r+k),       k>=1.     (2)

This is the correct sheaf for differences of embedded Cartier ideal
lifts from `V(I_E^k)` to `V(I_E^(k+1))`. It concerns ideals, rather
than chosen local generators of those ideals.

## 2. Uniform H0 vanishing includes every nonreduced root

Write `pi:Z -> P1_base`. For `n=r+k`, restriction of the divisor
sequence and pushforward in the fiber direction gives

    0 -> O(-epsilon)^(k+1)
      -> O^(r+k+1)
      -> W_(r+k)=pi_*O_Z(0,r+k) -> 0.               (3)

The vanishing of the relevant relative `H1` follows from `k>=1`.
Multiplication by the nonzero degree-`r` fiber equation is injective
on every fiber. The last term is therefore a globally generated
vector bundle of rank `r`, with

    deg W_(r+k) = epsilon(k+1).                     (4)

After extending the ground field to an algebraic closure, write

    W_(r+k) = direct_sum_i O(d_i).

Global generation implies `d_i>=0`, and (4) implies

    max_i d_i <= epsilon(k+1).

Twisting by the first degree in (2) bounds every splitting degree by

    epsilon-lambda k+epsilon(k+1)
      = 2 epsilon-k(lambda-epsilon)
      <= 3 epsilon-lambda < 0.                     (5)

Thus

    H0(Z,L_k)=0                     for every k>=1. (6)

Nothing in (3)--(6) uses smoothness, irreducibility, separability, or
reducedness of `Z`. The condition (1) is sufficient; no necessity or
sharpness claim is made.

For `(r,epsilon,lambda)=(2,2,7)`, (4) gives rank two and degree
`2k+2`. The upper bound (5) is `4-5k`, as proposed.

## 3. The H1 rank formula is correct, including boundary values

The divisor sequence for (2) is

    0 -> O_E(-lambda k,k)
      --f--> O_E(epsilon-lambda k,r+k)
      -> O_Z(epsilon-lambda k,r+k) -> 0.            (7)

The two sheaves on `E` have zero `H0` and `H2`. For `H2`, use the
nonnegative fiber degrees `k` and `r+k`; for `H0`, use (1).
The long exact sequence and (6) consequently give

    0 -> H1 O_E(-lambda k,k)
      --f--> H1 O_E(epsilon-lambda k,r+k)
      -> H1(Z,L_k) -> 0.                           (8)

The source and target dimensions are respectively

    a_k=(lambda k-1)(k+1),
    b_k=(lambda k-epsilon-1)(r+k+1).

These formulas also apply when a first factor is zero, for example
`epsilon=0,lambda=1,k=1`. Therefore

    h_k = b_k-a_k
        = k(r lambda-epsilon)-(r epsilon+r+epsilon). (9)

For the fixed quartic data this is

    h_k=12k-8.

This obtains both the stated rank and the injectivity required for
the quotient construction. It does not infer injectivity from a
generic rank computation.

## 4. Universal coefficient twists and arbitrary base change

Let `q:mathcal Z -> U` be the universal root family, and write
`H=O_U(1)`. The universal equation cuts out a divisor with ideal

    I_mathcal Z=O_E(-epsilon,-r) boxtimes H^-1.

Consequently its relative normal bundle is

    N_(mathcal Z/(E x U))=O_mathcal Z(epsilon,r) tensor q^*H.

The actual relative obstruction sheaf is therefore

    mathcal L_k
      =O_mathcal Z(epsilon-lambda k,r+k) tensor q^*H. (10)

The factor `H` is essential globally on projective coefficient space.
One can omit it only on a chart where the equation has been normalized
and `H` trivialized.

Applying the universal version of (7), with (10), gives the finite
presentation

    0 -> H1 O_E(-lambda k,k) tensor O_U
      --f--> H1 O_E(epsilon-lambda k,r+k) tensor H
      -> V_k -> 0,                                 (11)

where `V_k=R1 q_*mathcal L_k`. Equivalently, one may put

    Q_k=coker[a_k O_U(-1) --f--> b_k O_U],
    V_k=Q_k tensor H.

For every geometric point of `U`, the first map in (11) is injective
by (6)--(8). Some maximal minor is therefore a unit locally near each
point, and the map is locally a split inclusion of vector bundles.
Its cokernel is locally free of rank (9), and (11) remains exact after
every base change, including nonflat maps from nonreduced schemes.
The constant source and target cohomology in (7) can be computed by
their usual finite Cech presentations. Since (11) is locally split,
the same presentations after tensoring show universally that

    q_*mathcal L_k=0,
    R1 q_*mathcal L_k=V_k,

and formation of these sheaves commutes with arbitrary base change.
This avoids relying on a false general principle that constant fiber
dimensions by themselves always suffice over a nonreduced base.

## 5. What the cohomology permits in the deformation argument

For clarity, a direct local check of the relevant equation gauges is
as follows. Let `A' -> A` be one ambient square-zero step with kernel
`M=J^k`, and let `(h)` be an already lifted Cartier ideal. Any local
lift `h'` is a nonzerodivisor: `h` is regular in `A`, and the initial
equation `f` is regular on `M`, which is an invertible sheaf on `E`.
Two generator lifts differ by an element of `M`; changing generators
by a unit changes this difference by `fM`. Thus the sheaf of ideal
lifts has differences

    Hom(I_Z/I_Z^2,M/fM)=N_(Z/E) tensor J^k|Z.

Moreover, `A'/(h')` sits in an exact sequence with outer terms
`M/fM` and `A/(h)`. Both are flat over the parameter base, so the
lift remains a relative effective Cartier divisor. This check
retains equation units and works over nilpotent parameter bases.
For the general base-change property of relative effective Cartier
divisors, compare [Stacks Project, Section 31.19](https://stacks.math.columbia.edu/tag/056P).

Given the standard resulting lifting-torsor construction, (11) makes
its obstruction a section of `V_k` on the preceding lifting locus.
Its zero scheme is closed, and (6) gives uniqueness of the resulting
embedded ideal lift over every parameter base. This is exactly the
cohomological package needed for the separate conceptual review; it
does not identify local generator choices as canonical equations.

## 6. Finite determinacy and the relation-gap consequence: scope

If the relative lifting construction produces closed subschemes

    U=K_0 superset K_1 superset K_2 superset ...,

with `K_k` representing Cartier lifting into `V(I_E^(k+1))`, their
ideal sheaves form an ascending chain of coherent ideals on the
Noetherian scheme `U`. Hence the chain is eventually constant
scheme-theoretically; see
[Stacks Project, Lemma 30.10.1](https://stacks.math.columbia.edu/tag/01Y8).
The present cohomology argument supplies the missing all-order
uniqueness and coefficient-bundle input, but does not alone replace
the representability argument.

The resulting cutoff `N` is existential. It depends on the fixed
ambient formal neighborhood and the fixed `(r,epsilon)` family.
Neither the numerical inequality (1) nor Noetherianity gives a
numerical bound for `N`. One equality `K_n=K_(n+1)` is insufficient
to certify that every later locus is equal.

Under the accepted actual-CI bridge hypotheses, a pair whose full
generic initial relation degrees are `(r,s)` gives a Cartier lifting
of the root into `V(I_E^(s-r))`. It therefore lies in `K_k` for

    k < s-r.

Consequently, once an eventual stabilization index `N` exists,

    s > r+N

forces this root into `K_N`, the formal lifting locus. In the
quadratic case this is precisely `s>2+N`.

This last implication retains every hypothesis of the actual-CI
bridge, including actual smoothness of the root divisor where that
bridge requires it. Allowing nonreduced roots in the cohomology and
universal tower does not extend that bridge to nonreduced roots.
There is no algebraization claim, no asserted value of `N`, no proof
that the stabilized locus is empty, and no unrestricted STCI
conclusion. No commit or memory update was made.
