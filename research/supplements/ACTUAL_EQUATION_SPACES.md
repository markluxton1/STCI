# Actual homogeneous equation spaces and fixed quadric restrictions

Fix the embedded curve \(C=C_0=[s^4:s^3t:st^3:t^4]\), over an algebraically closed field. Let \(\mathcal I=\mathcal I_C\), \(q=x_0x_3-x_1x_2\), and
\[
V_{d,m}=H^0(\mathbf P^3,\mathcal I^m(d)),\qquad A_m(d)=\dim V_{d,m}.
\]
Powers are ideal sheaf powers, equivalently saturated homogeneous powers; they are not silently replaced by unsaturated polynomial ideal powers. The dimension and fixed-factor calculations below are characteristic free. Balanced normal-symbol statements and search applications use characteristic zero and [R-0020](../results/quartic_conormal_characteristic_jump.md). These deductions have inherited independent review and remain unpromoted.

The [geometric foundations](../synthesis/global_equations_and_constructions.md) prove that \(C\) has class \((1,3)\) on the unique smooth quadric \(Q\). This flag controls actual equations, including terms that first normal symbols do not see.

## Exact global freedom

Set
\[
D(u)=\frac{5u^3+15u^2+16u+6}{6}\qquad(u\ge0).
\]
For every integer \(m\ge1\) and \(d\ge0\),
\[
A_m(d)=
\begin{cases}
0,&d<2m,\\[2mm]
D(d-2m),&2m\le d\le3m,\\[2mm]
\displaystyle\binom{d+3}{3}
-\frac{m(m+1)(4d+1)}2
+\frac{7m(m^2-1)}3,&d\ge3m.
\end{cases} \tag{1}
\]
The two formulas at \(d=3m\) agree. The final polynomial already holds at \(d=3m-1\).

There is more information than the dimension alone. For \(2m\le d\le3m\),
\[
V_{d,m}=Q^{\,3m-d}
V_{3(d-2m),\,d-2m}. \tag{2}
\]
Thus every section has the displayed fixed quadric factor. For example,
\(V_{2m,m}=kQ^m\), and at \(d=2m+2\) the space has dimension 23 for every \(m\ge2\), but consists of \(Q^{m-2}\) times the degree-six, order-two space. This apparent freedom cannot be used as an integral degree-\(2m+2\) carrier when \(m>2\).

Here is the geometric reason. The smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\) contains \(C\) as a Cartier divisor of class \((1,3)\), up to swapping the rulings. The local regular-sequence identity
\((Q)\cap\mathcal I^m=Q\mathcal I^{m-1}\)
gives the flag sequence
\[
0\longrightarrow\mathcal I^{m-1}(d-2)
\xrightarrow{Q}\mathcal I^m(d)
\longrightarrow\mathcal O_Q(d-m,d-3m)\longrightarrow0. \tag{3}
\]
If \(d<3m\), the right-hand term has no sections, proving the forced factor and its iteration. Induction in (3) gives
\(H^1(\mathcal I^m(d))=0\) for \(d\ge3m-1\).
In the range \(d\ge3m\), taking sections yields
\[
A_m(d)=A_{m-1}(d-2)+(d-m+1)(d-3m+1),
\]
which sums to (1). This proves the all-degree formula; finite computations below only check its implementation and boundary values.

## Asymptotic interpretation

For fixed \(m\) and \(d\to\infty\), the number of independent linear conditions is exactly
\[
\operatorname{codim}V_{d,m}
=\frac{m(m+1)(4d+1)}2-\frac{7m(m^2-1)}3
\qquad(d\ge3m-1). \tag{4}
\]
It grows linearly in \(d\), while the ambient form space grows cubically. Vanishing to a fixed normal order therefore becomes inexpensive in large degree.

The more relevant scaling for high multiplicity is \(m/d\to\theta\). For \(0\le\theta\le1/3\),
\[
\frac{A_m(d)}{\binom{d+3}{3}}
\longrightarrow 1-12\theta^2+14\theta^3. \tag{5}
\]
At the boundary \(d=3m\), the limiting fraction is \(5/27\), so the global equation space is still large: \(A_m(3m)\sim5m^3/6\). For \(1/3\le\theta\le1/2\), the fraction is instead
\(5(1-2\theta)^3\), but this entire region has the forced quadric factor in (2). Above \(\theta=1/2\), there are no sections. These are dimensions of equation spaces, not expected dimensions of a STCI locus.

## Actual leading symbols: a small degree margin removes the first obstruction

For an equation of exact order \(r\), its leading normal symbol lies in
\[
H^0(C,\operatorname{Sym}^rE\otimes\mathcal O_C(d))
=H^0\bigl(\mathbf P^1,\mathcal O(4d-7r)\bigr)^{\oplus(r+1)}.
\]
Its actual source image has dimension
\[
\dim\operatorname{im}\sigma_{d,r}=A_r(d)-A_{r+1}(d), \tag{6}
\]
because the kernel is exactly \(V_{d,r+1}\). At the first degrees without a forced quadric factor, the comparison is

| Degree | Actual symbol image dimension | Full symbol target dimension | Codimension |
|---|---:|---:|---:|
| \(d=3r\) | \(5r^2+2\) | \((r+1)(5r+1)\) | \(6r-1\) |
| \(d=3r+1\) | \(5r^2+8r+4\) | \(5(r+1)^2\) | \(2r+1\) |
| \(d\ge3r+2\) | \((r+1)(4d-7r+1)\) | same | 0 |

The last row follows from \(H^1(\mathcal I^{r+1}(d))=0\). It is a surjectivity statement for the first nonzero normal symbol, and does not say that an arbitrary compatible tower of higher symbols comes from a pair of the required fixed degrees.

The small exact examples are useful controls:

| \((d,r)\) | Equation space \(A_r(d)\) | Symbol image | Full target |
|---|---:|---:|---:|
| \((3,1)\) | 7 | 7 | 12 |
| \((4,1)\) | 18 | 17 | 20 |
| \((5,1)\) | 35 | 28 | 28 |
| \((6,2)\) | 23 | 22 | 33 |
| \((7,2)\) | 47 | 40 | 45 |
| \((8,2)\) | 80 | 57 | 57 |
| \((9,3)\) | 54 | 47 | 64 |
| \((10,3)\) | 96 | 73 | 80 |
| \((11,3)\) | 150 | 96 | 96 |

The degree-three and degree-four rows are controls of the source spaces, not reopened STCI cases. At degree \(3r\), most equation freedom lies in higher-order terms: the equation space has cubic growth in \(r\), while its symbol image has quadratic growth. A search should keep these higher terms as adjustable contact data after selecting the leading root pattern.

## What a STCI candidate must do with this freedom

Suppose an actual proper pair \((F_a,G_b)\) has generic normal orders \(r,s\). At the generic point of \(C\), the transverse ambient local ring is regular of dimension two over \(k(C)\). If the two initial binary forms are coprime, their local intersection length is exactly \(rs\). A complete intersection with sole reduced support \(C\) would instead need length
\[
M=ab/4. \tag{7}
\]

For the integral degree-at-least-five representatives supplied by the accepted low-degree/factor reduction, (2) forces
\[
r\le a/3,\qquad s\le b/3.
\]
Consequently a coprime-leading-symbol pair has
\[
M=rs\le ab/9,
\qquad
\deg R=ab-4M\ge5ab/9. \tag{8}
\]
The lower bound in (8) is conditional on coprime leading symbols. It is **not** a residual lower bound on arbitrary pairs: shared leading roots can raise the local intersection length above \(rs\).

This proves a useful necessary search condition: a hypothetical integral STCI pair must have a nontrivial common factor between its leading normal forms over \(k(C)\). It must acquire at least \(ab/4-rs\) additional generic contact units, and the ratio of its required length to the ordinary product is at least \(9/4\). These are exact necessities, not an argument that the extra contact is unavailable.

The resulting candidate generator is concrete:

1. Choose degrees and exact equation orders with \(a,b\ge5\), \(4\mid ab\), \(r\le a/3\), and \(s\le b/3\).
2. Choose a shared-root pattern for the leading symbols, retaining its movement, branching and marked boundary behavior. At \(a=3r\) or \(3r+1\), impose the actual image in (6); at \(a\ge3r+2\), every leading symbol is available. Apply the analogous rule to \(G\).
3. Lift using actual coefficients in \(V_{a,r}\) and \(V_{b,s}\). Compute the full generic local intersection length, allowing cancellations and extra initial generators. Do not substitute the product \(rs\) once the symbols share a root.
4. Retain only proper pairs, compute \(ab-4M\), and test full global support and boundary attachment when the generic length reaches \(ab/4\). Record whether a failure came from a forced surface, inaccessible global symbol, insufficient higher contact, or residual/global boundary behavior.

This workflow uses freedom where it exists and makes each failure update a specific part of the next candidate choice. It does not make any one shared-root type compulsory; the accepted root, conductor and filtration records can test patterns within their exact hypotheses.

## Fixed residuals in a large actual lifting family

### A family with a fixed curve

Work over an algebraically closed field of characteristic zero. Fix
\[
C=C_0=[s^4:s^3t:st^3:t^4],\qquad Q=(q=0),\quad
q=x_0x_3-x_1x_2.
\]
Choose any cubic \(H\in H^0(\mathcal I_C(3))\) not divisible by \(q\).
For \(m\ge1\), put \(d=3m+2\) and take the entire actual source
\[
\mathcal W_H=
H^m\,k[x_0,x_1,x_2,x_3]_2+
H^0(\mathcal I_C^{m+1}(d)).
\tag{1}
\]
The powers are sheaf powers, or saturated homogeneous powers.
For \(m\) even and at least two, \(d\) is an even degree at least eight,
so the pair \((d,d)\) passes the low-degree and degree-divisibility filters.
No claim is made that a generic member is integral or a pair is proper.

The constructive motivation is literal: take
\[
F=f_2H^m+K,\qquad G=g_2H^m+L,
\]
with different quadratic coefficients \(f_2,g_2\) and all available
higher-normal-order corrections \(K,L\). The leading normal forms
have a common factor; their coefficient ratio may be nonconstant on
\(C\), so a constant row subtraction need not cancel them.

Nevertheless, **no two members of (1) can define \(C\) set-theoretically**.
The reviewed [freedom formula](ACTUAL_EQUATION_SPACES.md) gives
\[
H^0(\mathcal I_C^{m+1}(3m+2))
\subset q\,k[x_0,x_1,x_2,x_3]_{3m}.
\]
Indeed \(3m+2<3(m+1)\), so the next-order source has a forced quadric factor.
Thus every member of \(\mathcal W_H\) belongs to \((q,H^m)\), and
\[
V(q,H)\subset V(F,G).
\]
On \(Q\simeq\mathbf P^1\times\mathbf P^1\), the cubic cuts a divisor
of class \((3,3)\), while \(C\) has class \((1,3)\). It contains \(C\)
exactly once: two copies would leave a negative second ruling degree.
Its residual divisor therefore has class \((2,0)\). This is a nonzero
degree-two cycle of ruling lines, possibly a doubled line, and is
genuine support outside \(C\).

There is a stronger scheme-theoretic consequence for every proper pair:
\[
V(q,H^m)\subset V(F,G),\qquad
[V(q,H^m)]=m[C]+mR_H.
\]
At the generic point of each residual ruling, the quotient by \((F,G)\)
surjects onto the quotient by \((q,H^m)\); both lengths are finite.
Consequently the genuine residual cycle of the proper pair satisfies
\[
\boxed{R\ge mR_H,\qquad \deg R\ge2m.}
\]
If \(R_H\) is a doubled line, its multiplicity is retained in this
inequality. Attainment of the floor is not asserted.

The freedom in \(K,L\) cannot alter this residual because all such
corrections vanish identically on \(Q\). This is an all-parameter
global restriction, not the failure of one sampled equation.

### Equation freedom and boundary movement

Write
\[
D(m)=\frac{5m^3+15m^2+16m+6}{6}.
\]
The same reviewed source calculation gives
\[
\dim H^0(\mathcal I_C^{m+1}(3m+2))=D(m).
\]
Multiplication by \(H^m\) injects the ten-dimensional space of quadrics.
Its intersection with the next-order source consists exactly of
\(qH^m\): the cubic has generic normal order one, so the order increases
precisely when the quadratic vanishes on \(C\), and its only quadratic
equation is \(q\). Consequently
\[
\dim\mathcal W_H=D(m)+9.
\]
The full individual equation source has
\[
\dim H^0(\mathcal I_C^m(3m+2))
=D(m)+(m+1)(5m+9).
\]
Hence the excluded fixed-\(H\) family occupies a fraction of vector-space
dimension tending to one, while remaining a proper subspace of positive
codimension for every \(m\). This does not mean that it contains a
generic form or is exhaustive.

The family is not excluded merely because it has no proper pairs.
It has no fixed surface: it contains \(H^mS_2\) and
\(q^{m+1}S_m\), whose common fixed factor is one because \(q\nmid H\).
Over the infinite ground field, a generic second member avoids all
surface factors of a fixed nonzero first member. The proper-pair
locus is therefore nonempty. The quadratic leading coefficients can
also be chosen independent modulo \(q\), so every nonzero scalar
pencil member can retain exact normal order \(m\).

The floor \(2m\) grows with degree, but its ratio to
\((3m+2)^2\) tends to zero. It is not a uniform positive gap in contact
score, and it does not imply a floor for arbitrary sources.

There is a complementary warning for non-existence. The source excluded
by the [weighted-subalgebra line theorem](CARRIER_TEST_CURVES.md)
at degree \(3m\) has dimension asymptotic to \(m^2/4\), whereas the
full \(H^0(\mathcal I_C^m(3m))\) has dimension \(D(m)\sim5m^3/6\).
Its relative dimension is asymptotic to \(3/(10m)\), tending to zero.

Thus an all-degree family theorem need not asymptotically exhaust the
actual source, and a very large actual lifting space need not be able
to repair a fixed global boundary. Neither team may use a raw dimension
count as a substitute for the paired equations and full support test.

### Actual global row operations

Suppose actual homogeneous \(F_a,G_b\) define \(C\) set-theoretically
in characteristic zero, with \(a\le b\).
For every actual polynomial \(A\) of degree \(b-a\), the nonzero form
\[
G_b+A F_a
\tag{2}
\]
cannot have generic normal order greater than \(b/3\).
Otherwise the reviewed fixed-factor formula forces a factor \(q\)
(or forces the form to be zero when its order is too high even for a
nonzero section). A zero form in (2) makes the pair improper.
In the nonzero case
\[
V(F_a,q)\subset V(F_a,G_b+A F_a)=V(F_a,G_b).
\]
The accepted quadric-carrier exclusion and factor reduction say that
\(V(F_a,q)\) cannot have reduced support just \(C\) in characteristic zero.
This contradicts sole support. The corresponding restriction applies
after any mate-preserving homogeneous triangular row operation.

In particular, for equal-degree pairs, no nonzero scalar pencil member
may cross this normal-order threshold. This is a necessary condition
on all actual hypothetical pairs, not only (1).

The missing universal implication is substantial: large generic contact
does not automatically produce such a representative by **actual global
polynomial** row operations. Formal standard-basis cancellation can use
coefficients in \(k(C)\) with poles. No such globalization is proved here.

## Constructive interface on the quadric

For actual forms not divisible by \(q\), factor their restrictions on
the smooth quadric as divisors
\[
F_a|_Q=C^{u}A_Q,\qquad G_b|_Q=C^{v}B_Q,
\]
where \(u,v\) are their exact vanishing orders on \(C\) **inside \(Q\)**,
and
\[
[A_Q]=(a-u,a-3u),\qquad [B_Q]=(b-v,b-3v).
\]
These orders need not equal the ambient normal orders.
Sole support forces the entire common zero support of \(A_Q,B_Q\)
to lie on \(C\), with no common residual curve outside \(C\).
When the two residual divisors have no common component their total
intersection degree is
\[
(a-u)(b-3v)+(a-3u)(b-v).
\]
The problem is to concentrate that full intersection on \(C\), then solve
the remaining ambient contact and support conditions.

This is the constructive response to the fixed-\(H\) failure: choose
global restrictions whose residual factors do not share the fixed
ruling divisor, or move to degrees where next-order lifts can change
the quadric restriction. The obstruction program can independently
seek uniform bounds on this concentration or classify more residual
configurations. Neither response is yet an existence or non-existence
proof for arbitrary pairs.

## Exact support and review boundary

The flag-sequence formula and symbol dimensions were independently reconstructed in the source research. The retained [Macaulay2 calculation](../computations/stci_search_freedom_2026_10_28.m2) checks saturated powers for \(1\le m\le6\), all \(0\le d\le3m+2\), and the displayed symbol rows. The uniform proof is the flag sequence and induction, not the finite checks. The fixed-cubic family and its residual-cycle floor also received independent review. No new computation was needed for this consolidation.

The mechanism is useful in both directions: choose degrees where higher lifts can move the restriction on \(Q\), or show that a specified source cannot move its residual. Formal row operations over \(k(C)\) do not prove that an actual homogeneous triangular row operation crosses the fixed-factor threshold.


## Broader curve controls: global coefficients and Frobenius

These exact controls concern the whole family below, not only the fixed quartic. The scalar-coefficient counterexample received independent source review. The twisted-cubic containment is checked by the retained exact script; it is a positive characteristic-zero control.

Throughout let
\[
 C_n=(s^{n+1}:s^nt:st^n:t^{n+1}),\qquad n\ge2.
\]
It is a smooth rational curve of degree n+1 and class (1,n) on the
smooth quadric \(Q=xw-yz\), up to swapping the two rulings.

## 1. Scalar extension can manufacture a false global witness

Let \(S_n=yw^{n-1}-z^n\). Consider the degree-(n+1) forms
\[
 G_1=yS_n,\qquad G_2=wS_n.
\]
In the chart w=1 take the genuine generic coordinate T=z, and the
normal coordinates
\[
 u=y-T^n,\qquad v=x-yT.
\]
Thus \(Q=v\), \(S_n=u\), and \(K=k(C_n)=k(T)\). The jets satisfy
\[
 G_1=(T^n+u)u,\quad G_2=u,\quad G_1-T^nG_2=u^2.
\]
Consequently the relaxed K-linear combination with Q has local ideal
(v,\(u^2\)), of length two. This matches the proposed global degree
budget \(2(n+1)/(n+1)=2\), even at the sufficient cutoff.

But \(T^n\) is not a constant global surface coefficient. For every
nonzero pair \((\alpha,\beta)\in k^2\), the actual global combination
has
\[
 \alpha G_1+\beta G_2
 =u(\alpha u+\alpha T^n+\beta).
\]
Since T is transcendental, \(\alpha T^n+\beta\ne0\).
The second factor is a unit in the generic local ring, so the actual
intersection with Q has length one. No member of this global pencil
passes the degree-two target.

There is a stronger, pencil-independent exclusion on this Q. A
degree-(n+1) surface meeting Q properly and with generic multiplicity
two along C_n would require
\[
 (n+1)H-2C_n=(n-1,1-n)
\]
effective on \(\mathbf P^1\times\mathbf P^1\), impossible for n>=2.
Indeed C_n is not STCI on this smooth Q in any second degree because
its class is not proportional to H.

This does not contradict the finite normal-jet criterion. The formal expression with
coefficient \(T^n\) is not a global degree-(n+1) form. Treating T as
the ambient coordinate z after dehomogenization would instead change
the polynomial to \(S_n^2\), of homogeneous degree 2n. Its degree
budget is different, and its intersection with Q has a residual ruling.
The generic formal coefficient field and homogeneous polynomial degree
must be retained together.

**Coefficient contract:** the local matrix is computed over K, but the unknown
surface coefficients must remain in k. Existence of a K-point in a
relaxed coefficient problem is insufficient. The missing datum is liftability from the actual scalar-coefficient global equation space.

## 2. The binomial pair: exact characteristic dependence

Now use the singular first surface S_n and the degree-(n+1) form
\[
 T_n=x^nw-y^{n+1}.
\]
Use normal coordinates \(u=y-T^n\), \(v=x-T^{n+1}\) in the same chart.
The target generic multiplicity is n. Modulo \(S_n=u\), the other
equation becomes
\[
 (T^{n+1}+v)^n-T^{n(n+1)}.
\]

In characteristic zero its linear term is
\(nT^{n^2-1}v\), with nonzero coefficient in K, so the length is one.
The pair therefore fails for every n>=2.

In characteristic p, write \(n=p^e r\), with \(p\nmid r\). Frobenius gives
\[
 (T^{n+1}+v)^n-T^{n(n+1)}
 =\left((T^{n+1}+v)^r-T^{r(n+1)}\right)^{p^e}.
\]
The inner expression has nonzero linear coefficient, so the generic
length is exactly \(p^e\). The direct support calculation below proves
\[
 \boxed{\quad
 V_+(S_n,T_n)_{\mathrm{red}}=C_n
 \quad\Longleftrightarrow\quad n\text{ is a power of }p.
 \quad}
\]
This is an if-and-only-if for this particular binomial pair.
It is not an exclusion of other pairs when n is not a p-power; Moh's
broader projective monomial theorem supplies positive results in those
other cases by different equations.

There is a direct geometric check. Let r=n in characteristic zero and
r=n/p^e in characteristic p. On w=1 the support consists of the r
distinct curves
\[
 x=\zeta z^{n+1},\quad y=z^n,\qquad \zeta^r=1.
\]
Their closures each have degree n+1 and generic multiplicity p^e
(multiplicity one in characteristic zero). They account for the whole
degree \(n(n+1)\). At w=0 the equations force z=y=0 and leave just
(1:0:0:0), already on their closures. Thus no component at infinity
has been silently omitted.

Frobenius merges these distinct components scheme-theoretically into
one support exactly when r=1. It is a genuine global positive mechanism.
In characteristic zero the deficit relative to C_n alone is
\((n-1)(n+1)\); it is residual degree, not an abstract local defect.

## 3. A positive characteristic-zero control

For n=2 the twisted cubic is an STCI, but its second equation on S_2
needs the mixed term:
\[
 F=yw-z^2,\qquad G=x^2w-2xyz+y^3.
\]
For
\[
 I=(xz-y^2,\ xw-yz,\ yw-z^2),
\]
the exact computation gives
\[
 (F,G)\subset I,\qquad I^2\subset(F,G),
 \qquad\deg S/I=3,\quad\deg S/(F,G)=6.
\]
The generic finite jet length is two, exactly the target. These
containments independently certify the radical equality over QQ.
This keeps failure of the simpler binomial pair separate from failure
of the curve to be an STCI.


The retained [finite normal-jet verifier](../computations/finite_normal_jet_certificate.m2) supplies the exact twisted-cubic containments and finite characteristic controls; the uniform family statements have the proofs above.
