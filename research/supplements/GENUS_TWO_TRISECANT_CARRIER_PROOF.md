# Trisecant carrier ideals and the reduced-discriminant obstruction

The line classification and complete carrier-ideal calculation are
unconditional for the fixed characteristic-zero curve. The subsequent
nonzero-discriminant obstruction uses the
[actual normal ambient model](GENUS_TWO_AMBIENT_CONIC_MODEL_PROOF.md), now
proved independently. It is a narrower useful proof: the
[full nonendpoint](GENUS_TWO_NONENDPOINT_PROOF.md) and
[endpoint](GENUS_TWO_ENDPOINT_PROOF.md) arguments handle its repeated-
discriminant and endpoint boundaries. Those are not open quartic-mate
cases after the complete theorem.

Work over an algebraically closed field of characteristic zero, with

    C0 = [s^4:s^3 t:s t^3:t^4],
    q = x0 x3 - x1 x2,
    A = x0^2 x2 - x1^3,
    B = x0 x2^2 - x1^2 x3,
    D = x2^3 - x1 x3^2.

The accepted mate correction has `C#+Z ~ L`, with effective rational
exceptional `Z`. In the lambda-one stratum, `C#^2=1`, `f.C#=1`, and
`K.Z=1`. Conditional on the actual blowup realization, the planes through
the conductor line give `f`, so `length(C0 cap Gamma)=4-f.C#=3`.

## 1. All trisecant lines, their actual intersection schemes, and field orbits

The parametrization \(\nu:\mathbf P^1\to C_0\) is an isomorphism: its inverse coordinates on \(x_0\ne0\) and \(x_3\ne0\) are respectively \(t/s=x_1/x_0\) and \(s/t=x_2/x_3\). The curve lies on the smooth quadric

\[
Q=V(x_0x_3-x_1x_2).
\]

Let \(L\) be an ambient line and \(Z=C_0\cap L\), with its actual scheme structure. If \(q|_L\), where \(q=x_0x_3-x_1x_2\), is nonzero, its zero scheme on \(L\simeq\mathbf P^1\) has length two. Since \(q\) vanishes on \(C_0\), the scheme \(Z\) is a closed subscheme of that length-two zero scheme. Hence \(\operatorname{length}Z\ge3\) forces \(q|_L=0\), so \(L\subset Q\). This implication applies to repeated intersections as well as reduced ones.

Under the Segre identification

\[
([u_0:u_1],[v_0:v_1])\longmapsto
[u_0v_0:u_0v_1:u_1v_0:u_1v_1],
\]

the curve is \([s:t]\mapsto([s^3:t^3],[s:t])\). Every line on \(Q\) fixes one factor. Indeed, if rank-one matrices \(u\otimes v\) and \(u'\otimes v'\) span a line of rank-one matrices, the determinant of their linear combinations forces \((u\wedge u')(v\wedge v')=0\). Thus one factor is fixed.

Fixing the first factor at \([1:a]\) gives

\[
\Gamma_a=V(x_2-a x_0,x_3-a x_1),\qquad
\Gamma_\infty=V(x_0,x_1).
\]

The pulled-back generators for finite \(a\) are \(s(t^3-a s^3)\) and \(t(t^3-a s^3)\). Since \(s,t\) locally generate the unit ideal on \(\mathbf P^1\), the pulled-back ideal sheaf is exactly \((t^3-a s^3)\). Thus \(C_0\cap\Gamma_a\) has length exactly three. At infinity the corresponding ideal sheaf is \((s^3)\).

Fixing the second factor at \([1:b]\) instead gives

\[
\Lambda_b=V(x_1-b x_0,x_3-b x_2).
\]

Its pulled-back ideal sheaf is \((t-bs)\), since its generators are \(s^3(t-bs)\) and \(t^3(t-bs)\). Thus its intersection has length one; the endpoint \(\Lambda_\infty=V(x_0,x_2)\) likewise has ideal sheaf \((s)\) and length one. This exhausts all lines on \(Q\), proving the claimed classification and the exact length-three assertion.

### 1.1. Endpoint contacts and equivalence

In characteristic zero, for \(a\ne0,\infty\), the divisor \(V(t^3-a s^3)\) is geometrically reduced. The endpoint divisors are

\[
C_0\cap\Gamma_0=3[1:0:0:0],\qquad
C_0\cap\Gamma_\infty=3[0:0:0:1].
\]

Consequently there is no double-point-plus-simple-point trisecant stratum.

The ambient projectivity \(T_r=\operatorname{diag}(1,r,r^3,r^4)\) preserves \(C_0\) and sends \(\Gamma_a\) to \(\Gamma_{r^3a}\). Algebraic closure supplies \(r^3=b/a\) for any nonzero \(a,b\). Coordinate reversal \([x_0:x_1:x_2:x_3]\mapsto[x_3:x_2:x_1:x_0]\) also preserves \(C_0\), sends \(a\mapsto1/a\), and exchanges the endpoints. There are therefore exactly two geometric orbits in characteristic zero: nonendpoint lines and endpoint lines. Their intersection schemes distinguish them.

### 1.2. Precise arbitrary-field caveat

Over any characteristic-zero field \(k\), the classification still holds for \(k\)-defined lines, with \(a\in\mathbf P^1(k)\); nonendpoint intersection schemes have degree three and are geometrically reduced but their points need not be individually \(k\)-rational. For \(a,b\in k^\times\), ambient equivalence over \(k\) is exactly

\[
\Gamma_a\sim_k\Gamma_b
\quad\Longleftrightarrow\quad
b/a\in(k^\times)^3\ \text{or}\ ab\in(k^\times)^3.
\]

For necessity, \(Q\) is the unique quadric through \(C_0\): the ten quadratic monomial products restrict to nine distinct binary monomials, with only the duplicate \(x_0x_3=x_1x_2\). Any ambient stabilizer preserves \(Q\). It cannot exchange the two ruling families because the two projections of \(C_0\) have degrees three and one. Its product action \((\phi,\psi)\) satisfies \(\phi\circ f=f\circ\psi\) for \(f(z)=z^3\). The ramification locus of \(f\) is exactly \(\{0,\infty\}\), so \(\psi\) preserves that pair, hence \(\psi(z)=rz\) or \(r/z\) with \(r\in k^\times\). Thus its action on \(a\) is \(r^3a\) or \(r^3/a\). The explicit diagonal and reversal transformations prove sufficiency. For example, \(\Gamma_1\) and \(\Gamma_2\) are inequivalent over \(\mathbf Q\), but equivalent over \(\overline{\mathbf Q}\).

The quadric/ruling length classification does not require characteristic zero. In characteristic three, however, the nonendpoint degree-three divisors are inseparable, so the reducedness and two-orbit conclusions above must not be transferred there.


## 2. The entire carrier ideal has three cubic generators

For finite `a` set

    u=x0, v=x1, z=x2-a x0, w=x3-a x1,
    q=uw-vz,
    T_a=z^3+a u z^2-v w^2 = D-2a B+a^2 A.

Then, as homogeneous ideals,

    I(C0) intersect (z,w)^2 = (qz,qw,T_a).

One geometric proof is on q. A degree-d form restricting to a section
that vanishes on C0 and twice on Gamma has divisor at least
`C0+2 Gamma`, which is the divisor of the cubic T_a on q. Its remaining
section lies in `O_q(d-3,d-3)` and lifts to an ambient form of degree
`d-3`. Subtracting that multiple of T_a leaves a multiple of q.
Since q has normal order one along Gamma, that multiple belongs to
`(z,w)^2` precisely when its quotient belongs to `(z,w)`. This yields
the stated ideal, including all degrees.

For an algebraic unmixedness certificate, the three cubic generators
are the maximal minors of

    [ w     z^2+a u z ]
    [-z        -v w   ]
    [ 0         -q    ].

Their support consists of C0 and Gamma; the generic length along Gamma
is three, exactly the first infinitesimal neighborhood `(z,w)^2`.
This is compatible with a surface having multiplicity two along the
line; it is not a claim that `(z,w)^2` has generic length two.

Here is the complete independent Hilbert--Burch argument for equality,
including specializations of a. Put E=(qz,qw,T_a) and K=I(C0) intersect
(z,w)^2 in R=k[u,v,z,w]. The quadric q is irreducible and does not
divide T_a: at w=0 they specialize to -vz and z^2(z+au), the latter
not divisible by v. Thus E has height two, and the displayed minors
give the exact resolution

    0 -> R(-4) direct_sum R(-5) -> R(-3)^3 -> E -> 0.

Its quotient is unmixed of dimension two, with Hilbert numerator
1-3t^3+t^4+t^5 and degree seven. The evident containment E subset K
and the intersection-of-ideals sequence show that R/K also has degree
4+3=7: the curve and doubled line meet only in a finite projective scheme.
Thus K/E has dimension at most one. As a submodule of the unmixed R/E
it must vanish, proving E=K uniformly in a; this does not infer
special-fiber ideal-intersection commutation from a generic sample.

Consequently every quartic through C0 and double along Gamma is

    F = q Q + T_a L0,
    Q in (z,w)_2,       L0 an arbitrary ambient linear form.

The quartic space is the direct sum of a seven-dimensional space
`q (z,w)_2` and the four-dimensional space `T_a R_1`, hence has dimension
eleven. The sum is direct because T_a is not divisible by q.
Explicitly the first space uses
`Q in <uz,uw,vz,vw,z^2,zw,w^2>`, the degree-two part of the line ideal,
not just the degree-two part of its square. If qQ=T_a*l with l linear,
primality of q forces q to divide l, hence both sides are zero. Thus
the seven-plus-four dimension remains exact at a=0 as well.
On q its entire divisor is

    div(F|q) = C0 + 2 Gamma + (q cap {L0=0}).

For an integral carrier L0 is nonzero. The final term may be a smooth
conic or two ruling lines. Its degenerations must be retained.

## 3. Mate support forces the discriminant to vanish at each contact

Now assume the actual lift theorem: the strict transform T in
`Bl_Gamma(P3)` is normal, its minimal resolution is M, and M contracts
only vertical ADE curves to T. Its canonical divisor is `-E_Gamma|T`.
The separate map M to the normalization S can contract horizontal
(-3) sections as well.

The entire conductor algebra on S is a quadratic algebra over Gamma.
Under a mate, the complete inverse image of C0 in S has underlying
set c, and c maps isomorphically to C0. Hence over every point of
`Gamma cap C0` the conductor has exactly one geometric point: a split
fiber would give a second normalization point outside c. Its
discriminant therefore vanishes at each contact point.

The discriminant can be read from the first normal quadratic part of
F. Write

    Q = z alpha(u,v) + w beta(u,v) + Q2(z,w),
    L0|Gamma = c0 u + c1 v,
    alpha=a0 u+a1 v,       beta=b0 u+b1 v.

The leading quadratic is

    A2 z^2 + B2 zw + C2 w^2,
    A2=-v alpha+a u L0|Gamma,
    B2=u alpha-v beta,
    C2=u beta-v L0|Gamma.

For Gamma_1 put `r=v/u`. At a contact `r^3=1`, its discriminant obeys

    Delta(r) = (alpha(1,r)+r beta(1,r)-2r^2 L0(1,r))^2.

Vanishing at all three distinct contacts is thus equivalent to

    a0=2c1,       a1=-b0,       b1=2c0.

With these substitutions the entire quartic discriminant is

    Delta = 4(v^3-u^3)
              [(c0^2+b0 c1)v+(b0 c0-c1^2)u].

The identification with the actual conductor algebra uses the
canonical ideal: on the resolution the conductor ideal is
`O_M(K_M)`, and `R sigma_* O_M = O_S`,
`R sigma_* omega_M = omega_S`. The quotient pushes to the actual
conductor structure sheaf. The same argument for the rational ADE
resolution `M -> T`, with `omega_T=O_T(-E_Gamma)`, gives
`sigma_T* O_(D_M)=O_(D_T)` and no higher direct image. Both quotients
therefore have the same pushforward to Gamma as schemes, not only
the same generic quadratic field. On the ambient exceptional divisor
`E_Gamma=P1_Gamma times P1`, the exact sequence

    0 -> O(-2,-2) -> O -> O_(D_T) -> 0

gives `0 -> O_Gamma -> p_*O_(D_T) -> O_Gamma(-2) -> 0` and
`R1 p_* O_(D_T)=0`, even when D_T has vertical components. This is
precisely the quadratic algebra with the displayed discriminant,
including its identically-zero case. Thus isolated changes of its
extension at bad fibers cannot remove the contact vanishing
conditions.

## 4. A nonzero discriminant permits only one horizontal section

A horizontal sigma-exceptional E has `L.E=0`, `f.E=1`, so its image in
the ambient blowup is the entire exceptional fiber P1 above a point
of Gamma. Therefore the whole leading quadratic must vanish there.
The discriminant has a root of multiplicity at least two at that
point. The point lies in C0 because the correction cycle is supported
over c; a horizontal section with zero correction coefficient is also
avoided by c, as positivity gives `Z.E=C#.E=0`.

In the `Delta != 0` case, two horizontal sections cannot have positive
correction coefficients: the three C0-contact roots and two double
roots would require quartic degree at least five. There is therefore
exactly one horizontal section in the correction support, with
coefficient one since `K.Z=1`. A horizontal section outside the
correction support cannot meet that support, because `Z.E=0` and
effectiveness make each such intersection nonnegative. It does not
change its connected exceptional fiber.

Normalize the supporting contact to r=1 by cube-root diagonal
scaling. Whole-quadratic vanishing gives

    b0=c1-c0,
    Delta=4 kappa (v^3-u^3)(v-u),
    kappa=c0^2-c0 c1+c1^2.

For `kappa != 0`, the exceptional intersection on T is

    D_T = E_p + D',

where the residual `(1,2)` curve meets E_p in two distinct points.
Indeed after removing its common linear factor on Gamma, its
quadratic discriminant at p is nonzero. At either intersection the
ambient exceptional-divisor section D_T is an ordinary node.

Away from these points E_p is a smooth Cartier curve on T. A smooth
Cartier curve cannot pass through a singular surface point: if the
quotient of a two-dimensional local ring by one nonzerodivisor is a
regular one-dimensional ring, its maximal ideal has at most two
generators, so the surface local ring is regular. Hence T is smooth
along E_p away from the two nodes.

At each node the local ambient equation has the form

    xy + t R(x,y,t) = 0,

with the exceptional section `t=0`. If T is singular there, formal
Morse splitting in x,y yields `xy+g(t)=0`. Normality makes g nonzero,
and the rational Gorenstein singularity is A_n. The branches E_p and
D' meet opposite endpoints of the minimal-resolution A_n chain.
Consequently the connected sigma-exceptional graph containing the
(-3) section E has at most two endpoint A_n arms.

## 5. An exceptional correction cannot exist on that graph

Its coefficient at E is one. A chain arm of n (-2) curves, numbered
from E, has coefficients z_i satisfying

    2z_i-z_(i-1)-z_(i+1) = epsilon_i,
    z_0=1,       z_(n+1)=0,

where `epsilon_i=C#.F_i`. Smooth embedded descent supplies at most
one contact prime in the connected fiber, with intersection one.
With no contact on an arm its first coefficient is

    z_1=n/(n+1)<1.

With the unique contact at position j it is

    z_1=n/(n+1)+(n+1-j)/(n+1)<2.

If c contacts E, its equation requires the sum of its at most two
neighbor coefficients to equal two; both are strictly below one.
If c contacts an arm, the E equation requires that sum to equal
three; the contacted arm is strictly below two and the other strictly
below one. If it does not contact this graph, the required sum is
three while both terms are below one. Every possibility contradicts
the intersection equations.

Thus, conditional on the actual normal-blowup realization and the
scheme/discriminant interface above, the generic-trisecant lambda-one
mate branch with `Delta != 0` is excluded.

The full positive inverse-chain formula, with the positive contact sign retained, is
\[
(A_n^{-1})_{ij}=\frac{\min(i,j)(n+1-\max(i,j))}{n+1},
\qquad A_n(z_1,\ldots,z_n)^t=e_1+(\epsilon_1,\ldots,\epsilon_n)^t.
\]
An absent arm is encoded by length zero and contributes zero; it has no
valid contact index. The central equation is a separate geometric
hypothesis, not a consequence of solving the arms. No integrality or
effectivity of the rational coefficients is required for the strict
finite-arm contradiction. The graph is also automatically negative
definite: eliminating its negative arm blocks leaves central Schur
complement \(-3+\sum n/(n+1)<-1\). This sign is consistent with the
surface application, though negative definiteness is not needed for the
coefficient-one contradiction itself.

## 6. What this particular discriminant argument does not treat

This argument does not treat `kappa=0`, hence `Delta identically zero`.
The residual exceptional curve may then be nonreduced; node and
endpoint-chain arguments cannot be imported to that boundary. The
two endpoint trisecant lines are likewise outside this particular argument. At `a=0`,
the sole discriminant vanishing condition is `a0=0`, which forces a
factor `v^2` but does not give three distinct contact roots. The
lambda-zero bisecant branch is not addressed by this note.

The three-distinct-contact split uses invertibility of three. In
characteristic three the ruling map on C0 is inseparable and all its
fibers are triple contacts. The ideal calculation retains its algebraic
meaning; the characteristic-zero branch and differential arguments do
not follow merely from that ideal.
