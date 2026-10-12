# Endpoint trisecant: full quartic exhaustion and mate exclusion

Date: 2026-10-10. Author: `trisecant_endpoint_research`.
Status: **PROVED HERE / combined independent audit PASS**. The local
triple and doubled-horizontal proofs have separate written independent
audits. The binding
[full independent coverage verdict](2026-10-10-session-genus-two-endpoint-full-independent-audit.md)
checks the full family exhaustion and all local interfaces. The conclusion
remains scoped to the fixed curve, characteristic zero, the accepted conic
model, and the lambda-one stratum; root canonical acceptance is separate.
No canonical frontier record is edited by this note.

Work over an algebraically closed field of characteristic zero with the
literal curve `C0=[s^4:s^3 t:s t^3:t^4]`. Use the accepted actual normal ADE
strict transform `T` in the blowup of its genus-two conductor line, and the
accepted lambda-one mate reduction:

    f.c#=1,       c#^2=1,       K_M.Z=1,
    c# ~ L-Z,    Z effective rational sigma-exceptional,
    Z.E=-c#.E for every sigma-exceptional prime E.

The special horizontal prime `B` exists, satisfies `B^2=-3`, `f.B=1`,
and `c#.B=0`. There are at most two horizontal primes. Each horizontal
prime has K-degree one and maps in the ambient exceptional surface to
the whole fiber over one point of Gamma. Distinct horizontal primes
give distinct Gamma-fibers. Vertical exceptional primes are (-2) curves
contracted in the crepant ADE resolution `rho:M -> T`.

The actual full quartic family and endpoint coordinates are from
[the carrier ideal proof](2026-10-10-session-genus-two-trisecant-quartic-carriers.md).
Here the conductor line is `Gamma=(x2,x3)`. On the blowup chart put

    a=x1/x0,       y=x2/x0,       b=x3/x2.

The exceptional surface is `y=0`; the lifted curve is exactly
`(a,b,y)=(r,r,r^3)`. The sole point of `Gamma cap C0` is `a=0`, with
scheme length three. This full parametrization, including the third
normal order, is retained throughout.

## 1. The supporting horizontal fiber is forced to lie over a=0

Every positive coefficient of Z lies over the image of c in S. Indeed
pulling back a mate whose zero divisor on S has support c produces
effective exceptional correction only over c. Thus any horizontal
prime with positive Z coefficient maps to the sole Gamma-contact a=0.
Since `K_M.Z=1`, at least one such horizontal exists. As distinct
horizontal primes have distinct Gamma-images, exactly one horizontal
prime, denoted H0 for now, has positive coefficient, and that coefficient
equals one. Every other horizontal prime has coefficient zero.

This argument does not assume that the special prime B has positive
coefficient. A possible special B at a point p different from zero is
retained below.

## 2. Exact full quartic equation after the necessary horizontal factor

Write the degree-four carrier as `F=q Q+D L0`, where
`Q in (x2,x3)_2` and L0 is any linear form. Its strict transform has
exceptional restriction

    P(a,b)=(b-a)[a0+a1*a+(b0+b1*a)*b]
              -a*b^2*(c0+c1*a).

The supporting horizontal fiber H0 requires `P(0,b)=0` identically.
Therefore `a0=b0=0`, and the entire strict-transform equation is

    T: a[(b-a)(a1+b1*b)-b^2(c0+c1*a)]
       +y[(b-a)(A+B1*b+C*b^2)+c0+c1*a
                      -a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (1)

The coefficient named B1 here is a scalar, not the horizontal prime B.
The actual exceptional divisor `D_T=T intersect E` is the full divisor
of P on `P1_Gamma x P1_f`, of class `(2,2)`.

An additional horizontal fiber over a finite `a=p !=0` forces all coefficients
of P(p,b)/p to vanish. Reading the constant, linear, and quadratic
terms in b gives

    a1=0,       b1=0,       c0+c1*p=0.            (2)

In that finite case c1 is nonzero (otherwise P vanishes identically), and

    D_T=H0+Hp+2F0.

The notation F0 denotes the fixed f-fiber b=0. Repeated components are
retained; this is a scheme statement, not only a support statement.

There is also the other Gamma-chart: a horizontal fiber at `p=infinity`
forces `a1=b1=c1=0`. Nonzero P then requires c0 nonzero and gives
`D_T=H0+H_infinity+2F0`. Thus every possible second horizontal, including
infinity, forces c0 nonzero and has the same displayed divisor form.

## 3. All c0 !=0 and coefficient-zero-special-B cases are excluded

At the actual contact `(a,b,y)=(0,0,0)`, equation (1) has
`partial T/partial y=c0`. If c0 is nonzero, T is smooth there, and c#
meets the strict transform of H0 with intersection one, because
`a|c=r` has order one.

If H0 is the only horizontal prime, it is the special prime B. This
contradicts `c#.B=0`. This also covers cases in which H0 occurs twice
in D_T; no reduced-horizontal assumption is being made.

If H0 is not B, the special B must give a second horizontal fiber Hp,
with p different from zero, possibly infinity. The finite and infinite
calculations in section 2 give exactly `D_T=H0+Hp+2F0`.
On H0 the remaining divisor meets only at b=0. Away from that point
the exceptional section of T is reduced smooth H0, so T is smooth.
At b=0 T is smooth by c0 nonzero. Hence H0 has no vertical ADE primes
attached anywhere, including the other f-chart.

The coefficient of Z along Hp is zero by section 1, and positivity
forces all exceptional coefficients attached to Hp to be zero too.
The correction equation for H0 is therefore simply

    -3*coeff_H0(Z)=-c#.H0=-1.

It gives `coeff_H0(Z)=1/3`, contradicting the coefficient one forced
by K_M.Z=1. This excludes the possibility that B has coefficient zero
and another horizontal supplies the mate correction.

Consequently every surviving endpoint configuration satisfies

    c0=0,       H0=B,       coeff_B(Z)=1,
    c#.B=0,    B is the sole horizontal prime.

The last assertion follows from (2): a distinct horizontal would force
c0 nonzero. If the residual contains H0 again, it is a multiplicity
statement about the same sole prime, not a second horizontal prime.

## 4. The a1 !=0 branch has two endpoint A-chains and is excluded

With c0=0 put

    R=(b-a)(a1+b1*b)-c1*a*b^2,       D_T=B_T+R.

Its restriction to B_T is the homogeneous degree-two polynomial
`b(a1+b1*b)`. If a1 is nonzero, this has two distinct zeros on P1_f,
including the zero at b=0; if b1=0, the other zero is at infinity.
At both points the derivative of R along B_T is nonzero. Thus the
exceptional section consists of two transverse branches there, even
if R itself is reducible elsewhere.

Every singularity of T on B_T lies at these two points. Each is an
A_n singularity with B attached to an endpoint of its resolution
chain: formal Morse splitting of `uv+y h` preserves y as parameter.
Let the contacted chain have length n and contact node k; let the
other chain have length m, allowing m=0. The smooth embedded descent
meets exactly one exceptional prime transversely. Solving the
intersection equations gives

    coeff_B(Z)=((n+1-k)/(n+1)) /
                  (3-n/(n+1)-m/(m+1)) <1.

The numerator is strictly below one and the denominator strictly above
one. This contradicts `coeff_B(Z)=1`. No finite chain cutoff and no
irreducibility assumption on R are used.

## 5. The a1=0, b1 !=0 branch is an exact local triple case

The equation becomes

    a*b[b1*(b-a)-c1*a*b]
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (3)

The only intersection of B_T with the residual exceptional divisor is
b=0, of multiplicity two. Thus every singularity of T on B_T is at
this one point. The full local proof is in
[the exact local ADE correction audit](2026-10-10-session-endpoint-local-ade-correction-audit.md).
It preserves the complete polynomial (3) and proves:

* A nonzero: B attaches to an endpoint of an A_n chain, giving its
  correction coefficient below 1/2.
* A=0 and c1 nonzero: exact quadratic factorization over k[[b]] puts
  the surface in `XY=b^(n+1)*unit`. B has factor orders `(n-1,2)`;
  c has orders `(1,n)` in the opposite orientation. The correction
  coefficient is exactly `2/(n+5)`, below one, for n>=3.
* A=c1=0 and c2 nonzero: the ordinary triple cubic after completing
  the square gives precisely D4; B and c meet distinct outer arms.
  The correction coefficient is 1/4.
* A=c1=c2=0: multiplicity is at least three, incompatible with ADE.

The abstract D7 numerical graph shield cannot be imported to this
equation without verifying actual realization. The ordinary triple
cubic here has three distinct factors b1*a*b*(b-a), which gives D4.

## 6. The doubled-horizontal subcase is also excluded

If a1=b1=0, nonzero P requires c1 nonzero, and

    D_T=2B_T+2F0.

Its full actual equation is

    -c1*a^2*b^2
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (4)

The normal coefficient along B_T is the global degree-three section

    h_B(b)=b*(A+B1*b+C*b^2).

Thus additional singular points of T on B_T can occur away from the
contact at the other zeros of h_B, including infinity. The earlier
two-node endpoint-chain shortcut does not apply here. The complete
proof is in
[the doubled-horizontal independent audit](2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md).
Here is its structural calculation.

For an ADE block let Q be its positive Cartan matrix and let v encode
the intersections of B with its exceptional primes. At the contact
block let e_j encode the unique transverse c# contact. Since the B
coefficient is one, the B intersection equation requires

    sum_blocks v^t Q^(-1) v + v^t Q^(-1) e_j =3.      (5)

Away from the contact, write `a=u*A0`, `y=u^2*Y0` on M, with B given
by u=0 and its f-parameter unchanged. Crepancy of the hypersurface
canonical generator `da wedge db/F_y` forces
`A0|B=unit*h_B`. Equation (4) then forces `Y0|B=unit*h_B` as well.
If an away-contact root has multiplicity k, comparison with the
total transform of div(y) gives the exact identity

    2*v^t Q^(-1) v=k.                              (6)

This retains arbitrary ADE types, multiple graph attachments, and
the other f-chart; it does not replace such blocks by A1 points.

If A is nonzero, both B and c have tangent outside the rank-two
quadratic kernel, and hence meet endpoints of the contact A_n chain.
Their combined contribution to (5) is strictly below two. The
remaining degree-two zero divisor of h_B contributes one by (6).
This contradicts (5). As an additional global check, A=c1 would make
T singular along all of the fixed conductor component F0, since
`F_y|F0=a*(c1-A)` and all other partial derivatives vanish there.
It is excluded by normality, independently of the numerical bound.
In fact A nonzero and A different from c1 forces precisely A3:
the quartic term restricted to the quadratic kernel is nonzero.
B and c meet the same endpoint, so the contact contribution is 3/2
and the total bound is 5/2, as detailed in the independent audit.

If A=0, normality leaves `k=ord_0(h_B)` equal to two or three.
The exact quadratic factorization in the independent audit gives
an `A_(2k+1)` contact, with B at node k and c at an endpoint.
The contact contribution to (5) is at most `(k+2)/2`; the other
zeros of h_B have total multiplicity `3-k` and contribute
`(3-k)/2` by (6). Thus the entire left side of (5) is at most
`5/2`, again less than three. This excludes all of (4).

If a1=b1=c1=0, P vanishes identically. The actual quartic then has
generic normal order at least three along Gamma, contrary to the
accepted genus-two generic multiplicity two. It is not another
surviving genus-two carrier stratum.

## 7. Full endpoint conclusion and surviving larger scope

Sections 3--6 exhaust the full eleven-dimensional quartic carrier
family after the necessary supporting-horizontal factor. They exclude
every endpoint-trisecant lambda-one mate for the literal C0 over an
algebraically closed field of characteristic zero, using the accepted
genus-two normal conic model and correction/contact reductions.

The proof explicitly includes a zero coefficient of the special B,
a second horizontal fiber at a finite point or infinity, repeated
horizontal and vertical conductor components, internal A-chain
attachments, D4, arbitrary ADE blocks away from the contact, and
repeated normal-coefficient roots. Neither a tangent-only argument nor
an abstract all-A-chain assumption is used.

This endpoint theorem requires the separate nonendpoint theorem to
close the lambda-one stratum. The lambda-zero stratum requires its
separate double-curve argument. No conclusion about all carrier
degrees, arbitrary integral curves, or the universal STCI problem
follows from this note alone.
