# A paired elliptic construction passes polarization and fails node gluing

October 31, 2026. **Independently reviewed provisional result**; see the
[independent audit](2026-10-31-paired-elliptic-construction-audit.md).
Work over an algebraically closed field of characteristic zero, with
`C0=[s^4:s^3t:st^3:t^4]` fixed. The construction supplies actual elliptic
target functions and the previously missing component polarization.
Its next, nodal gluing condition fails by a degree-three versus
degree-four comparison. No carrier, mate, or unrestricted exclusion follows.

## 1. Constructive input and literature boundary

The [previous target](2026-10-31-palindromic-polarization-spin.md) had
nontrivial induced spin. A replacement needs both trivial spin and actual
ruling functions, not just a branching pattern. In general, if
`div(f)=3D0+U0-3Dinf-Uinf`, with degrees six and two respectively, then
`beta=[D0-Dinf]` is the obstruction to a function B with this divisor.
The relation `Uinf-U0 ~ 3(D0-Dinf)` permits a nontrivial three-torsion
ambiguity even when a function A with divisor Uinf-U0 exists. If beta=0,
setting A=B^3/f recovers both functions. A spin condition alone does not
assert beta=0.

[Artebani–Pirola](https://arxiv.org/abs/math/0312025) constructs alternating
monodromy functions by exact-square differentials, but its degree-existence
theorem does not prescribe these fibers or their ruling divisors.
[Moschetti–Pirola, §§2–3 and 5](https://arxiv.org/html/2011.12159v1)
studies odd covers equivariant for a hyperelliptic involution, including
degree-four elliptic maps with effective spin. This motivates pairing
the branch points within each divisor. The explicit algebraic base change
below supplies that pairing and proves existence directly; no general
claim about lifting a topological involution is required.

## 2. Explicit base change

Choose the definite constants

\[
a=-7+4\sqrt3,\quad u=(a-1)/4=-2+\sqrt3,\quad
k=8/3,\quad s=2\sqrt6/3.
\]

Thus `a^2+14a+1=0`, `u^2=-a`, and `s^2=k`. Put

\[
F(x)=(x-1)^3(x-a),\quad r(x)=F(x)/x^2,\quad R_0=r(u),
\]
\[
D(x)=-6F(x)+R_0(2s+3)x^2,\qquad
N(x)=12sF(x)-3R_0(2s+3)x^2,\qquad q(x)=N(x)/D(x).
\tag{1}
\]

Here q is an auxiliary rational map, not the defining polynomial of the
target quadric. Direct differentiation gives

\[
r'(x)=2(x-1)^2(x-u)^2/x^3.
\]

The degree-four map r has exactly the fibers of types (3,1), (3,1),
(2,2) over 0, R_0, infinity. They are distinct: u avoids 0,1,a, so
R_0 is finite and nonzero. The postcomposition in (1) sends these three
values to -3, 3, -2s. These are distinct from each other and from 2s.
Thus q is unramified over 2s and infinity. In particular D has four
distinct roots, none at 0,1,u,a or infinity.

Let E be the smooth projective normalization of

\[
h+k/h=q(x).
\tag{2}
\]

The double cover x:E→P1 branches at the four simple points q=2s.
The two double points q=-2s and the simple poles of q give even
discriminant orders and no branching after normalization. Therefore E
is a connected smooth elliptic curve. Its involution is
`j(x,h)=(x,k/h)`. The four fixed points of j form h=s; choose one as
origin so j is elliptic negation.

The function h has degree four. Its only ramification consists of two
index-three points over x=1 and two over x=u. At the normalized points
over q=-2s, h+s is a uniformizer; at q=2s, h-s is a uniformizer. Thus
these do not add ramification for h. The four triple points contribute
eight, exhausting elliptic Riemann–Hurwitz for degree four.

## 3. Actual ruling functions and component polarization

Define

\[
g(z)=\frac{(z-1)^3(3z^2+9z+8)}
           {(z+1)^3(3z^2-9z+8)},\qquad f=g(h),
\]
\[
T(x)=\frac{x-1}{x-u},\qquad
B=T(x)\frac{h-1}{h+1},\qquad
A=T(x)^3\frac{q(x)-3}{q(x)+3}.
\tag{3}
\]

The quotient coordinate z+k/z pairs the two roots of each quadratic
factor of g separately. Equation (2) consequently gives

\[
f=\left(\frac{h-1}{h+1}\right)^3\frac{q+3}{q-3}
=B^3/A.
\tag{4}
\]

The remaining simple point of r=R_0 is `v=a+3-3u=u+4`.
The triple parts of q±3 cancel in A, so

\[
A=c_A\frac{x-v}{x-a},\qquad c_A\ne0.
\tag{5}
\]

Its degree on E is two. The zeros of B are the four simple points h=1
and the two points x=1; its poles are the four points h=-1 and the two
points x=u. All these points are distinct. The A-boundaries are x=v
and x=a, each reduced of degree two and disjoint from the B-boundaries.
All boundary statements include infinity: q=±11/3, corresponding to
h=±1, is unramified and differs from its three branch values.

The functions A,B recover x by (5) and h by (3). Thus they give a
birational normalization map
`h_E:E -> Q=P1_A x P1_B` onto an integral curve C' of class (6,2).

Let H_x be the degree-two x-fiber class and H_h the degree-four h-fiber
class. The h=s fiber consists of all four fixed points of j. On the
elliptic curve their sum is linearly equivalent to 4 times the chosen
origin, and H_x is twice that origin. Hence H_h~2H_x. The four
ramification points of h are two x-fibers, also of class 2H_x, proving
that h has trivial induced theta characteristic. Composition with the
odd-ramification rational function g preserves it.

More strongly, the actual divisors in (3) give, with
`L=A^*O(1)` and `M=B^*O(1)`,

\[
L=\mathcal O_E(H_x),\qquad M=L^3,\qquad
\mathcal O_E(Z)=L^2,\quad Z=h^{-1}(\infty).
\tag{6}
\]

The degree-twenty f has full fibers `(3^6,1^2)` over zero and infinity
and `5Z` over one. The four points of Z lie over the four distinct roots
x_i of D. At them,

\[
t_i=B(P_i)=T(x_i),\qquad A(P_i)=t_i^3.
\]

The t_i are distinct, finite and nonzero. A is unramified there, and
no two marks have the same A-value. They therefore give four smooth
target points, each with contact five with the literal C0. There are no
additional inverse points over C0, including the ruling boundaries.

This verifies the complete input to the
[canonical-extension criterion](2026-10-31-elliptic-canonical-extension.md).
For the nodal union Y=E∪P1_t, both component polarizations match.
The canonical source quadric is a cone: t_i is a Möbius function of
A(P_i), so the degree-two interpolation argument of that criterion
excludes a smooth source. This statement constructs the abstract source
quadric, not an extension of the target coordinates to it.

## 4. The node-gluing class is nontrivial

After independent review of this construction, the recommendation to test
one residue class, stopping on its first failure, was reported before
the gate below was checked. No other cover or target was assigned.

An explicit normalized quartic model follows from (1):

\[
Y_0=\frac{(2h-q)D}{x},\qquad
Y_0^2=\frac{N^2-4s^2D^2}{x^2}
=\frac53R_0\left(24sF-R_0(2s+3)^2x^2\right).
\tag{7}
\]

The right side is a separable quartic with nonzero constant and leading
coefficients. Its roots are exactly q=2s. In particular x=0 and infinity
each have two normalized unramified points. Put `omega=dx/Y_0`.

The target coordinate x0 has divisor
`x^*(a)+x^*(u)+(h=-1)` on E: it is the sum of the two disjoint ruling
pole divisors. If H_inf=x^*(infinity), then

\[
\operatorname{div}(Y_0)=\operatorname{Ram}_x-2H_{\infty},\quad
\operatorname{div}(h-s)=\operatorname{Ram}_x-Z.
\]

Consequently, under an isomorphism from the target hyperplane bundle to
`omega_E^2(2Z)`, x0 is represented, up to one nonzero scalar, by

\[
\tau_E=(x-a)(x-u)(h+1)(h-s)\frac{dx^2}{Y_0^3}.
\tag{8}
\]

Its divisor as a rational quadratic differential is exactly the target
x0 divisor minus 2Z; this checks the component identification globally.
At P_i∈Z, choose the branch h=infinity, for which
`Y_0(P_i)=N(x_i)/x_i`. The other sign is the branch h=0 and is not a
mark. Since `h~N(x_i)/(D'(x_i)(x-x_i))`, its quadratic residue is

\[
\rho_i=\frac{x_i^3(x_i-a)(x_i-u)}{N(x_i)D'(x_i)^2}.
\tag{9}
\]

Let `R_mark(t)=product(t-t_i)`. The Möbius change in (3) gives, for a
nonzero constant c,

\[
R_{\rm mark}(T(x))=c\frac{D(x)}{(x-u)^4},\qquad
R_{\rm mark}'(t_i)=\frac{cD'(x_i)}{(1-u)(x_i-u)^2}.
\]

At a root of D, `N(x_i)=(5/3)R_0 x_i^2`. Hence the four gluing entries
of the canonical criterion, `rho_i R_mark'(t_i)^2`, are a common
nonzero multiple of

\[
J(x_i),\qquad J(x)=\frac{x(x-a)}{(x-u)^3}.
\tag{10}
\]

They cannot all agree. Otherwise the polynomial
`x(x-a)-lambda(x-u)^3`, of degree at most three, would vanish at the
four distinct x_i. It would be identically zero, which is impossible.
Equivalently, a degree-three morphism J:P1→P1 cannot put four distinct
points in one fiber. Therefore

\[
\boxed{\kappa(Y,h_E)\ne1.}
\]

This is a failure in the gluing between components, despite the genuine
equalities (6) on E. Rescaling the component isomorphism multiplies all
four entries together and cannot fix it. The calculation uses the full
divisor and the correct normalized branches; no numerical approximation
or enumeration is involved.

## 5. Extraction, review, and stopping decision

The positive contribution is an explicit mechanism giving odd spin,
principal ruling divisors, and correct marked contact simultaneously.
The general divisor criterion beta=0 explains why arbitrary odd-spin
covers would not have sufficed. The subsequent obstruction is geometric:
the node-gluing ratios descend to a degree-three map, while the marked
fiber contains four distinct points. More generally, a nonconstant
degree-d ratio map cannot identify n>d distinct marked points; applying
this observation requires deriving the actual gluing map first.

The target is stopped at this residue gate. Source-section recovery,
first-normal contact, carrier construction and full mate descent were
not run. No theorem about every elliptic target, every degree-eight
carrier, or arbitrary STCI equations follows. A future construction in
this interface must control node gluing as well as spin and ruling
divisors; another branching pattern alone supplies none of those data.
The canonical-extension theorem remains available as a sufficient tool.

The producer was a fresh `gpt-6-astra/xhigh` worker. A fresh
`gpt-6.1-sol/high` reviewer independently checked the algebraic construction
and supported the one residue experiment, then reviewed the lead's
residue calculation in a coherent continuation. The audit reconstructs
the normalization, divisors, marks and quadratic differential, not merely
the final degree comparison. Both assignments are complete. The separate
ribbon-source retrieval found the existing net and projection evidence;
no closed quartic-carrier case was reopened. No canonical promotion or
unrestricted mathematical status change is made.
