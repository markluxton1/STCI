# Quadratic descent across a smooth elliptic double conductor

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the exact
hypotheses below. This is a conditional geometric exclusion, not a
classification of singular quartic normalizations. The universal
STCI problem and the unrestricted fixed-C0 problem remain open.

## 1. Theorem with actual conductor schemes retained

Let k be an algebraically closed field of characteristic zero. Let
X be an integral quartic surface in P3, let nu:S->X be its finite
normalization, and set H=nu^*O_X(1). Suppose the following hold.

1. There is a smooth integral curve c on S whose image is the fixed
   rational quartic C0=[s^4:s^3t:st^3:t^4], and nu|c is an
   isomorphism onto C0.
2. There is a nonzero global section Q of O_S(2H) whose Weil divisor
   is exactly 2c.
3. The actual downstairs conductor scheme Gamma is a smooth conic.
   The actual upstairs conductor scheme D is a smooth integral
   projective curve of genus one, and D avoids Sing(S).
4. The induced map p:D->Gamma is finite flat of degree two.

Then X has no homogeneous set-theoretic mate for C0, in any positive
degree.

Here “actual conductor” means the closed schemes defined by the
conductor ideal I=Ann_OX(nu_*O_S/O_X), respectively I O_S. Smoothness
of their supports alone does not satisfy hypotheses 3 and 4. The
theorem permits c to pass through singularities of S away from D.
It imposes no parity condition on the degree of a hypothetical mate.

## 2. A mate gives the divisor and the squared power identity

Assume G is a homogeneous mate of degree b>0, so the zero support
of G on X is exactly C0. It is not identically zero on X. Thus
h=nu^*G is a nonzero section of O_S(bH).

The curve C0 is distinct from the conic Gamma. At its generic point
the normalization is therefore an isomorphism: off the conductor
the finite ring extension is an equality. Every curve component of
nu^{-1}(C0) dominates C0 because nu is finite. Hence c is the only
curve component above C0. Consequently the Weil divisor of h is
m c for an integer m>0. Any isolated off-c inverse-image point would
already contradict the zero support of this Cartier section; that
obstruction need not be assumed absent in advance.

The intersection degree with H gives

    b H^2 = m (H.c).

The finite birational quartic normalization has H^2=4, and
H.c=deg(C0)=4. Therefore m=b and

    div_S(h)=b c.

Both h^2 and Q^b are nonzero sections of the same line bundle
O_S(2bH), with identical Weil divisor 2b c. Their quotient is a
rational function with neither zeros nor poles in codimension one.
Normality makes it an invertible regular function on S, and
projectivity and integrality make it a constant. Thus

    h^2=lambda Q^b,        lambda in k^*.

This is why an assumption that b is even is unnecessary. Squaring
the mate gives a descended power of Q for every positive integer b.

## 3. Power invariance gives a global sign on the conductor

Put M=O_Gamma(1). Since H is pulled back from X,

    O_D(H)=p^*M,
    q=Q|D is a section of p^*(M^2).

The section q is nonzero: D is integral of genus one and is distinct
from the rational curve c, while div_S(Q)=2c. Let sigma be the
nontrivial involution of the finite flat double cover p. Its action
on p^*M^2 is the canonical action on a pulled-back line bundle.

The section h|D is pulled back from G|Gamma. Restricting the power
identity to D shows that q^b is invariant under sigma. In the
function field k(D), the ratio r=(sigma q)/q therefore satisfies
r^b=1. The polynomial T^b-1 splits into linear factors over k, and
k(D) is a field. Hence r is a constant root of unity zeta in k.
Applying sigma twice gives zeta^2=1, so

    sigma q=+q       or       sigma q=-q.

These are global equalities of sections, because they hold
generically on the integral curve D. There is no independent sign
choice at different points, and no unexamined pole stratum in this
step. Only the ratio in the function field is used; the equality of
regular sections extends over their zero sets automatically.

## 4. The minus sign contradicts even ramification valuations

The conic Gamma is isomorphic to P1. Riemann--Hurwitz for the smooth
genus-one degree-two cover gives

    0 = 2(-2)+deg(R),       deg(R)=4.

In characteristic zero a degree-two ramification index is two and
its different exponent is one. Thus there are four distinct simple
ramification points. In particular there is at least one such
point P.

At P choose a local frame of M^2 downstairs, and pull it back. This
frame is sigma invariant. In the completed local ring of the smooth
curve D choose a uniformizer w such that sigma(w)=-w. For example,
the trace-zero coordinate of a quadratic algebra is a uniformizer
at a simple ramification point; its square is a base uniformizer
times a unit. Write q=a(w) in the chosen pulled-back frame.

If sigma q=-q, then a(-w)=-a(w). Since a is a nonzero regular power
series and the characteristic is not two, its first nonzero term
has odd degree. Therefore ord_P(q) is odd.

On the other hand S is regular along D. At every P in D, the prime
curve c is locally Cartier, even if it is not Cartier at some point
outside D. Let f be a local equation of c where P lies on it. The
equality div_S(Q)=2c gives locally Q=u f^2 with u a unit, after a
local frame for O_S(2H). Restricting to D makes its vanishing order
twice the local intersection multiplicity of c and D. If P does not
lie on c, its vanishing order is zero. Thus every valuation of q
on D is even:

    div_D(q)=2(c.D).

Changing to the pulled-back frame multiplies the representing
function by a unit and does not change this valuation. The odd
valuation forced by anti-invariance is impossible. Consequently

    sigma q=q.

The argument needs regularity of S along the actual D. It does not
discard non-Cartier behavior of c at singular points away from D.

## 5. Descent through the entire conductor square

For a finite flat double cover in characteristic not two, the trace
splitting gives

    (p_*O_D)^sigma=O_Gamma.

This also follows locally by choosing a trace-zero basis element
z with z^2 in the base ring and sigma(z)=-z. The projection formula
therefore identifies invariant sections of p^*M^2 with sections of
M^2. Hence q=p^*qbar for a global section qbar of O_Gamma(2).

The actual conductor square is a fiber-product square, not merely
a generic gluing prescription. Locally, if A is the ring of X, B
its normalization and I their conductor, then

    A = B x_(B/I) (A/I).

Indeed an element of B whose residue belongs to A/I differs from
an element of A by an element of I, and I is contained in A.
Globally this gives the exact sequence

    0 -> O_X -> nu_*O_S direct_sum O_Gamma -> nu_*O_D -> 0,

where the last map subtracts the two restrictions. Tensoring with
the invertible sheaf O_X(2) preserves exactness. The compatible pair
(Q,qbar) therefore comes from a global section Q_X of O_X(2), with

    nu^*Q_X=Q.

There is no H^1 obstruction to this descent: exactness identifies
the kernel already on global sections. Compatibility has been proved
on all of the smooth actual conductor D, including the ramification
points, rather than only at its generic point.

Finally the hypersurface exact sequence

    0 -> O_P3(-2) -> O_P3(2) -> O_X(2) -> 0

and H^1(P3,O(-2))=0 lift Q_X to a homogeneous ambient quadric q_X.
The lift is nonzero since Q is nonzero.

## 6. The fixed-C0 quadric contradiction

The fixed curve C0 lies on exactly one quadric, up to scalar:

    Q0 = V(x0 x3-x1 x2).

This is immediate by restricting the ten degree-two monomials to
[s^4:s^3t:st^3:t^4]: nine resulting monomials are independent and
the only repeated monomial is x0x3=x1x2=s^4t^4. Thus q_X is a
nonzero scalar multiple of this smooth quadric's equation.

The pullback of q_X has divisor 2c, so its zero support on S is
exactly c. Finite surjectivity then makes its zero support on X
exactly C0. Therefore the quartic equation of X, restricted to the
smooth quadric Q0, has an effective divisor supported only on C0.
Its degree is eight, so that divisor must be 2C0.

Under Q0=P1xP1 the fixed C0 has divisor class (1,3), up to swapping
the rulings. One Segre parametrization is

    [s^3:t^3] x [s:t]
        |-> [s^4:s^3t:st^3:t^4].

The divisor cut by a quartic has class (4,4). But 2C0 has class
(2,6), so it cannot be that divisor. Equivalently a residual divisor
after subtracting 2C0 would have class (2,-2), which is not
effective. This contradiction excludes the hypothetical mate G.

## 7. Applicability and boundaries

The explicit four-A1 degree-four del Pezzo projection in
`research/notes/2026-10-09-session-dp4-projection-local-lift.md`
satisfies all four hypotheses: its actual downstairs conductor is
a smooth conic, upstairs it has a smooth elliptic double cover
avoiding the four A1 vertices, and the displayed global quadric has
divisor 2c. That carrier was already excluded by its explicit
nonsingleton fibers. This theorem supplies a second exclusion and
extends to every carrier for which the same hypotheses are proved.

The theorem does not prove that every singular-normalization
quartic has this conductor or the global section Q. It does not
cover nonreduced actual conductor schemes, a singular upstairs
conductor, an upstairs conductor passing through Sing(S), or the
absence of a global doubled-curve quadric. Those hypotheses must
not be inferred solely from the reduced support, a local divisor
class, or a model family containing the explicit example.

## 8. Independent audit and primary inputs

The separate audit is saved in
`research/notes/2026-10-09-session-elliptic-conductor-quadratic-descent-independent-audit.md`.
It accepts the power reduction without a degree parity assumption,
the odd/even valuation contradiction, complete conductor-square
descent, and the final smooth-quadric divisor-class contradiction.
Independent agreement is audit evidence; the proof is the argument
above. No finite symbolic calculation is substituted for this
conditional theorem.

The primary general inputs used here are the
[Stacks Project Riemann--Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B)
for the four simple ramification points, and
[Stacks Project cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS)
for the ambient quadratic lift. The conductor fiber-product equality,
sign reduction and parity obstruction are proved explicitly above.
No literature novelty claim is made.
