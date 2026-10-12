# Endpoint trisecant lane: independent coverage and correction audit

Date: 2026-10-10. Auditor: `endpoint_adversarial_audit`.
Status: **PROVED HERE / independent mathematical audit**, conditional only
on the previously accepted genus-two normal conic-model, marking, and
mate-correction inputs listed below. Under those inputs the endpoint
lambda-one lane is excluded. This note makes no claim about lambda zero,
carriers of other degree, other rational quartics, or the universal STCI
problem. No canonical frontier file is edited here.

The audited sources are the
[full endpoint reduction](2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md),
the [local triple ADE calculation](2026-10-10-session-endpoint-local-ade-correction-audit.md),
and the [double-horizontal calculation](2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md).
The older
[irreducible-residual note](2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md)
was read but is not used as an exhaustion certificate: it covers only one
residual stratum. The entire quartic family is supplied by section 2 of
the [carrier ideal proof](2026-10-10-session-genus-two-trisecant-quartic-carriers.md).

## 1. Exact inputs and claim

The ground field is algebraically closed of characteristic zero, and

    C0=[s^4:s^3t:st^3:t^4].

An integral quartic carrier has normalization S and smooth rational
resolution M. In the lambda-one mate stratum the accepted inputs give

    rho:M -> T subset Bl_Gamma(P3),
    T normal Gorenstein ADE, rho crepant,
    f.c#=1, c#^2=1,
    c# ~ L-Z, Z effective rational sigma-exceptional,
    K_M.Z=1, Z.E=-c#.E for every sigma-exceptional prime E.

The map rho contracts precisely the vertical (-2) primes. Every
horizontal sigma-exceptional prime is a (-3) section and has K-degree
one. There are at most two horizontal primes; their images in T are
distinct fibers over points of Gamma on
`E=P1_Gamma x P1_f`. The special prime B exists and satisfies `c#.B=0`.
The smooth embedded descent and local uniformizer input says that the
strict curve meets exactly one prime in any contacted exceptional
fiber, transversely and with intersection one.

The conclusion audited here is: **no mate of any degree exists when
Gamma is either endpoint trisecant of this fixed C0 and lambda=1**.
Reversal exchanges the two endpoints, so it suffices to use
`Gamma=(x2,x3)`.

## 2. Coverage of the full quartic equation

On the affine blowup chart set

    a=x1/x0, y=x2/x0, b=x3/x2.

The actual lifted curve is `(a,b,y)=(r,r,r^3)` and the exceptional
surface is `y=0`. Its only Gamma-contact is `a=0`, of length three.
The ideal identity

    I(C0) intersect (x2,x3)^2=(q*x2,q*x3,D)

gives every quartic as `q Q+D L0`, where `Q in (x2,x3)_2` and L0 is
linear. The restriction of the full strict-transform equation to E is

    P(a,b)=(b-a)[a0+a1*a+(b0+b1*a)*b]
             -a*b^2*(c0+c1*a).

Every positive horizontal coefficient of Z must map to the sole
Gamma-contact: the pullback of the actual mate has no zero outside the
image of c. Since the horizontal coefficients sum to `K.Z=1`, exactly
one horizontal image H0 over `a=0` has positive coefficient, equal to
one. Other horizontal coefficients can be zero and are retained.
The condition `P(0,b)=0` gives `a0=b0=0`, with no extra restriction.
Thus every possible carrier under a mate has the exact equation

    a[(b-a)(a1+b1*b)-b^2(c0+c1*a)]
      +y[(b-a)(A+B1*b+C*b^2)+c0+c1*a-a*b^2(c2+c3*b)]
      +y^2(c2+c3*b)=0.                                  (1)

This preserves the complete third normal order of C0; it is not a
first-normal truncation. The carrier ideal proof is sound: on q the
divisor `C0+2Gamma` has class `(3,3)` and is the divisor of D. The
remaining equal-bidegree section lifts to P3. Subtracting this multiple
of D leaves `q Q`; order two along Gamma forces Q into its ideal.

## 3. The coefficient-zero B and doubled-H0 gap is repaired

At the C-contact, the derivative in y of (1) is c0. If `c0!=0`, T is
smooth there and `c#.H0=1`, because a restricts to r.

If H0 is the only horizontal prime, it must be the special B. This
contradicts `c#.B=0`. It also excludes a doubled H0 component; no
reduced-divisor assumption is needed.

If B is a second horizontal over finite `p!=0`, the identity
`P(p,b)=0` gives

    a1=b1=0, c0+c1*p=0,
    D_T=H0+Hp+2F0.

The case `p=infinity` is essential. In the other Gamma chart its
condition is `a1=b1=c1=0`; nonzero P then gives c0 nonzero and
`D_T=H0+H_infinity+2F0`. Thus it has the same geometry.
H0 is smooth on T everywhere: off b=0 the exceptional restriction is
a reduced smooth component, and at b=0 the y-derivative c0 is nonzero.
Hence there are no attached ADE primes. The other horizontal has
coefficient zero, and all its attached coefficients are zero as well.
The correction equation is therefore `-3 z_H0=-1`, giving `z_H0=1/3`,
contrary to the forced value one.

This covers the formerly dangerous possibility `a1=0,b1=c0!=0`, where
the exceptional divisor contains doubled H0. An early argument that
H0 then had at most one A-chain was unjustified: its normal derivative
can have three zeros. The special-B argument above excludes this case
without that shortcut. The corrected proof has been communicated to
the owner and parent.

Every surviving case consequently has `c0=0`, sole horizontal B=H0,
`z_B=1`, and `c#.B=0`. A distinct horizontal would force c0 nonzero.

## 4. Two distinct residual intersections

If `a1!=0`, the residual divisor on B_T is the global binary quadratic
`b(a1+b1*b)`. It has two distinct zeros, including infinity when b1=0.
At each, the two exceptional-divisor branches are transverse; all
other points of B_T are smooth on T. Relative formal Morse splitting
with the exceptional parameter fixed gives A_n chains with B attached
at an endpoint. The relative splitting has been audited separately in
[the branch-preserving Morse note](2026-10-10-session-relative-morse-conductor-branches-independent-audit.md).

If the contacted chain has length n and contact node k, and the other
has length m, then

    z_B=((n+1-k)/(n+1)) /
           (3-n/(n+1)-m/(m+1)) <1.

The numerator is below one and the denominator above one for all
lengths. This contradicts `z_B=1`. Reducibility of the residual away
from these two points is irrelevant and is not excluded by fiat.

## 5. Triple residual intersection: actual A/D positions

For `a1=0,b1=u!=0`, put `v=c1,d=c2,e=c3`. The full equation is

    a*b*(u*(b-a)-v*a*b)
      +y*((b-a)*(A+beta*b+gamma*b^2)+v*a-a*b^2*(d+e*b))
      +y^2*(d+e*b)=0.                                   (2)

The restriction of the residual to B_T is the global quadratic `u b^2`;
all singularities of T on B_T lie at the one contact, including the
other b-chart. The audited local cases are exhaustive:

* If A is nonzero, fixing a gives a nondegenerate transverse factorization
  at `a=0`, namely `y*(A b+...+d y)`. Relative Morse splitting therefore
  puts B at an endpoint of an A_n chain. The correction coefficient is
  below one half for every possible contacted node.
* If `A=0,v!=0`, the equation is exactly quadratic in `(a,y)` over
  `k[[b]]`. Factor its nondegenerate binary quadratic and complete its
  two linear terms. One translated coordinate on B has order exactly
  two; the other has finite order m>=2. On C one coordinate has order
  exactly one. Hence the surface is `A_(m+1)`, B meets `E_(n-1)`, and C
  meets `E_1`, in consistent orientation. The inverse Cartan entries give
  `z_B=2/(n+5)<1`. This controls the dangerous internal attachment rather
  than replacing it by an endpoint assumption.
* If `A=v=0,d!=0`, the cubic in the tangent plane is
  `u*a*b*(b-a)`, with three distinct factors. The first blowup has
  precisely three A1 points in those directions. Its resolution is D4;
  B and C meet different outer arms transversely. The inverse D4 entries
  are 1 on an outer diagonal and 1/2 between distinct outer arms, giving
  `z_B=1/4`.
* If `A=v=d=0`, the surface has multiplicity three, incompatible with ADE.

I checked the exact binary-quadratic factorization and branch orders in
the local note, as well as its first blowup formula. The D7 numerical
shield is not a realized parameter case of (2); no arbitrary ADE graph
enumeration is being mistaken for this actual-family computation.

## 6. Doubled horizontal: arbitrary ADE roots are included

The remaining nonzero exceptional polynomial has `a1=b1=0,c1=c!=0` and

    D_T=2B_T+2F0,
    F=-c*a^2*b^2
       +y*((b-a)*(A+B1*b+C*b^2)+c*a-a*b^2*(d+e*b))
       +y^2*(d+e*b).

The normal derivative on B_T is

    h(b)=b*(A+B1*b+C*b^2).

It is a nonzero global section of `O_B(3)`: the relevant line bundle is
`O_B(T-E)`, of degree three. Identical vanishing would make T singular
along all of B_T, contradicting normality. Its zeros, including infinity,
have total multiplicity three.

For an ADE block write `Q=(-E_i.E_j)`, `v_i=B.E_i`,
`g_BB=v^t Q^-1 v`, and at the contacted node j write
`g_BC=v^t Q^-1 e_j`. The equation for B with `z_B=1` is

    sum_blocks g_BB+g_BC=3.                              (3)

At an away-contact root of h of order k, the local divisor is exactly
`div_T(y)=2B_T`. On the crepant resolution choose coordinates `(u,t)`
with B=(u=0), where t is the pulled-back parameter along the smooth
B_T. Write `a=u A0`, `y=u^2 Y0`. Pullback of the hypersurface canonical
generator `da wedge dt/F_y` is a regular unit times `du wedge dt`.
Restricting its coefficient to B gives `A0=unit*h`. Substituting into
the equation and restricting its u^2 coefficient then gives
`Y0=unit*h`, because the coefficient of a^2 is a unit away from b=0.

On the other hand `div_M(y)=2B+sum beta_i E_i` has
`beta=2Q^-1 v`. Restricting its residual divisor to B gives

    2*g_BB=ord(h)=k.                                    (4)

This is an exact equality, valid for arbitrary ADE type, repeated roots,
and multiple attachment points. I independently checked the canonical
residue and divisor arguments; an A-chain-only estimate is unnecessary.

If A is nonzero, both B and C have tangents outside the kernel of the
rank-two Hessian at the contact, since their relevant linear factors
evaluate to A and c, respectively. They meet A_n endpoints. Thus the
contact contribution in (3) is strictly below two; the remaining h-zeros
contribute exactly one by (4), contradicting (3).

If A=0, the contact order of h is k=2 or 3. The exact formal change in
the doubled-horizontal note gives

    X1*Y1=c*b^2*h^2/s^2, s a unit,
    ord_B(X1,Y1)=(k,k+2), ord_C(X1)=1.

Hence the actual contact is `A_(2k+1)`, B meets node k and C an endpoint.
The contact contribution is at most `(k+2)/2`, and all remaining roots
contribute `(3-k)/2`. Their sum is at most `5/2`, contradicting (3).
I verified the formal identities, the exact orders, and this inequality
directly. There is no omitted D/E contact case in this subfamily.

Finally `a1=b1=c1=0` makes P identically zero, giving order at least
three along Gamma, contrary to the accepted genus-two generic order
two. It is not another carrier stratum.

## 7. Verdict and evidence boundary

The cases `c0!=0`, `a1!=0`, `a1=0,b1!=0`, and
`a1=b1=0,c1!=0` exhaust every nonzero exceptional polynomial of the
full quartic family. Their correction equations all contradict the
mate inputs. Reversal covers the opposite endpoint. The endpoint
lambda-one exclusion therefore passes this independent audit.

This verdict rests on the written geometric proof and exact local
identities, not agreement between agents or a finite graph search.
The companion M2 checker of the local triple note supplements those
identities; no execution count is asserted here before inspecting its
separate raw execution record. No computer certificate is used to
replace the arbitrary-degree mate support or arbitrary-ADE argument.

The fixed-curve, characteristic-zero, quartic-carrier, and lambda-one
hypotheses remain essential. The universal STCI question, lambda zero,
and all higher-degree carrier strata remain outside this audit.
