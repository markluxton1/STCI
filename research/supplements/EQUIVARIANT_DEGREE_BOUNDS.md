# Torus weights and degree bounds in positive characteristic

Fix the smooth embedded quartic
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), where \(k\) is
algebraically closed. Besides ordinary degree, give the coordinates weights
\((0,1,3,4)\). A **weight-homogeneous** form has just one weight; equivalently
it is bihomogeneous for the parametrization grading
\((4,0),(3,1),(1,3),(0,4)\).

**Status, October 31, 2026:** independently reviewed provisional theorem;
not promoted to a canonical result. This extends the [one-binomial bound](ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#one-binomial-equation-with-an-arbitrary-mate)
to one weight-homogeneous equation, with an arbitrary mate. Later sections
constrain the extreme components of every pair with \(p\nmid ab\),
prove the sharp linear bound when each equation has at most two weights,
and give a residual-support control for the next weight case.
These are not unrestricted STCI bounds. No claim of priority over the
literature is made.

The [mixed-characteristic extension](MIXED_CHARACTERISTIC_TRACE_OBSTRUCTION.md)
uses the integral trace coefficient near a pair of eigenforms. It constrains
arbitrary simultaneous deformations of both equations, including a
ramification bound and a strong-support \(W_2\) obstruction. Its
special-fiber hypotheses and lifting conclusions differ from the
field-valued degree bounds here.

## The bound and its exact large-prime minimum

Suppose \(F,G\) are homogeneous of positive degrees \(a,b\), and
\(V(F,G)_{\mathrm{red}}=C_0\). If at least one of \(F,G\) is
weight-homogeneous, then characteristic zero is impossible. In
characteristic \(p>0\),
\[
 p\mid ab,\qquad \max(a,b)\ge p.
\tag{1}
\]
Since \(ab=4m_C\), for odd \(p\) this also gives
\(p\mid m_C\) and \(ab\ge4p\). The trace argument alone makes no
claim that \(2\mid m_C\) in characteristic two.

The same conclusions hold, without any weight hypothesis, for every
ordinary homogeneous supported pair which, after exchanging and rescaling
the equations, satisfies
\[
 F\equiv x_1^a\pmod{x_0^2},\qquad
 G\equiv x_2^b\pmod{x_3^2}.
\tag{J}
\]
Indeed the trace proof below uses only these congruences after deriving
them from the weight condition. This is a separate sufficient hypothesis
for the obstruction, not an assertion that arbitrary pairs can be put in
this form.

Let \(\delta_{\mathrm{wt}}(p)\) minimize \(\max(a,b)\) over pairs with
at least one weight-homogeneous equation.
The known weight-homogeneous [degree-\((4,p)\) equations](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic)
attain (1), so
\[
 \boxed{\delta_{\mathrm{wt}}(p)=p\quad\text{for every prime }p\ge7.}
\tag{2}
\]
Both equations may have several monomials. More generally, if either
equation merely has a nonconstant weight-homogeneous factor, the same
lower bound \(\max(a,b)\ge p\) follows by applying (1) to that factor
and the other equation. The divisibility \(p\mid ab\) for the original
degrees is not asserted under this weaker factor hypothesis.

## Trace proof for two weight-homogeneous equations

Write \(X=x_1,Y=x_2\). The coordinate points
\(P_1=[0:1:0:0]\) and \(P_2=[0:0:1:0]\) are outside \(C_0\),
so at each point at least one of \(F,G\) is nonzero. A positive-degree
weight-homogeneous form cannot be nonzero at both: the pure powers
\(X^d,Y^d\) have different weights \(d,3d\) as integer characters,
including in positive characteristic. After exchanging the equations,
\(F\) contains \(X^a\) and has weight \(a\), while \(G\) contains
\(Y^b\) and has weight \(3b\). Rescale their pure-power coefficients
to one.

For a monomial \(x_0^{e_0}X^{e_1}Y^{e_2}x_3^{e_3}\) in \(F\),
ordinary degree and weight give
\[
 e_0=2e_2+3e_3.
\]
Unless it is \(X^a\), its \(x_0\)-exponent is at least two.
Similarly, every monomial of \(G\) other than \(Y^b\) has
\(e_3=3e_0+2e_1\ge2\). Thus
\[
 F\equiv X^a\pmod{x_0^2},\qquad
 G\equiv Y^b\pmod{x_3^2}.
\tag{3}
\]

Put \(A=k[x_0,x_3]\) and \(B=k[x_0,X,Y,x_3]/(F,G)\).
The pair is proper, hence a regular sequence. Modulo \((x_0,x_3)\),
\(B\) becomes \(k[X,Y]/(X^a,Y^b)\). The \(ab\) monomials
\[
 X^iY^j,\qquad0\le i<a,\quad0\le j<b
\tag{4}
\]
therefore generate \(B\) over \(A\), by induction on ordinary degree.
Their free graded \(A\)-module has Hilbert series
\[
 \frac{(1-t^a)(1-t^b)}{(1-t)^4},
\]
which is also the regular-sequence Hilbert series of \(B\). The surjection
is an isomorphism. In particular, \(B\) is free of rank \(ab\) over \(A\),
with basis (4).

Sole support implies that \(q=XY-x_0x_3\) is nilpotent in \(B\).
Indeed the homogeneous affine cones have the same reduced support,
including the origin. Multiplication by \(q\) on
\(B\otimes_A\operatorname{Frac}(A)\) is nilpotent and has trace zero.
Since \(A\) is a domain, the trace already vanishes in \(A\). Consequently
\[
 \operatorname{Tr}_{B/A}(XY)=ab\,x_0x_3.
\tag{5}
\]

Trace on a finite free module commutes with base change. Set
\(\overline A=A/(x_0^2,x_3^2)\). By (3),
\[
 B\otimes_A\overline A
 =\overline A[X,Y]/(X^a,Y^b).
\]
Multiplication by \(XY\) in basis (4) has zero diagonal, so its trace
is zero. Reducing (5) gives \(ab\,x_0x_3=0\) in \(\overline A\).
But \(x_0x_3\) is a nonzero basis element of \(\overline A\) over \(k\).
Thus \(ab=0\) in \(k\). This proves the characteristic-zero exclusion
and \(p\mid ab\) for two weight-homogeneous equations.

## Reduction from one equation and an arbitrary mate

Suppose only \(F\) is weight-homogeneous. Factor it into irreducibles
\(F=c\prod H_j^{r_j}\), of degrees \(a_j\). Each factor is
weight-homogeneous: in the polynomial domain, the difference between the
largest and smallest occurring weights adds under multiplication.
Width zero of \(F\) forces width zero for every factor.

Every \(H_j\) contains \(C_0\), and \(V(H_j,G)_{\mathrm{red}}=C_0\).
To see this, \(H_j\) and \(G\) have no common factor, since \(F,G\)
have none. Their projective intersection contains a curve and is contained
in \(C_0\). Irreducibility of \(C_0\) forces equality of support.

In the weight-graded domain \(R=k[x_0,X,Y,x_3]/(H_j)\), write \(g\)
for the nonzero image of \(G\). Its principal radical is the homogeneous
ideal of \(C_0\) in \(R\). Every nonzero weight component \(g_w\)
therefore belongs to \(\sqrt{(g)}\); for some \(N>0\),
\(g_w^N=g h\) with \(h\ne0\). Additivity of widths in this graded
domain shows that \(g\) has width zero. Taking the corresponding
ordinary-degree-\(b\) weight component \(G_j\) of \(G\), we have
\[
 (H_j,G_j)=(H_j,G).
\]
The trace proof applies to \(H_j,G_j\). In characteristic zero this
is impossible; in characteristic \(p>0\), \(p\mid a_jb\) for every
\(j\). Summing with the multiplicities \(r_j\) yields \(p\mid ab\).

## Scope and literature

The characteristic-zero exclusion of bihomogeneous defining pairs is
already part of the Thoma and Hellus–Hübl theory. See
[Hellus–Hübl, *A result on Macaulay's curve*, introduction and Theorem 1.2](https://arxiv.org/pdf/1312.7661),
and the characteristic-zero application in
[tropical thickenings](../synthesis/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier).
The proof above directly retains the characteristic-dependent scalar
\(ab\); it does not import their characteristic-zero theorem into
positive characteristic.

The [general finite-algebra trace formula](../synthesis/fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers)
already describes the first trace from the two lowest base-degree
corrections. The congruences (J) force its mixed coefficient to vanish.
For arbitrary pairs that coefficient can be nonzero, and the same chapter
gives a [zero-first-trace control with residual curves](../synthesis/fixed_surface_and_endpoint_algebras.md#8-all-three-boundary-supports-are-compatible-with-zero-first-trace).
Thus the extra vanishing here comes from the stated congruences; nilpotence
or trace formalism alone does not give a universal obstruction.

For the unrestricted minimum \(\delta(p)\), only
\(\delta(p)\le\delta_{\mathrm{wt}}(p)\) follows. An arbitrary pair
need not have a weight-homogeneous equation or factor. Torus limits may
acquire a common surface component, as explained in the
[arithmetic chapter](ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#why-degeneration-does-not-cover-every-pair).
The missing global step is a valid reduction covering pairs with two
unrestricted equations; the trace calculation does not supply it.

## Independent review

An independent reconstruction on October 31, 2026 accepted (1), (2), and
the weaker factor-hypothesis bound. It checked factor support, reduction of
the arbitrary mate in a graded domain, the finite free basis and Hilbert
series, nilpotent trace over the fraction field, trace base change, the
characteristic-two limitation, and the actual \((4,p)\) attainment.
The same reviewer checked the extension (J), confirming that no weight
hypothesis is used after the two congruences.
The review does not certify literature priority or any unrestricted
lower bound. The proof is mathematical; no finite computation is used as
a substitute for its all-degree or all-prime quantifiers.

## Extreme components of arbitrary presentations

**Independently reviewed provisional extension.** This section adapts
[Hellus–Hübl, Theorem 1.2](https://arxiv.org/pdf/1312.7661), replacing its
characteristic-zero exclusion of a bihomogeneous supported pair by the
trace theorem above. No literature-priority claim is made.

Let \(F,G\in R=k[x_0,x_1,x_2,x_3]\) have ordinary degrees \(a,b>0\),
with \(\sqrt{(F,G)}=P=I_{C_0}\). Suppose \(\operatorname{char}k=p>0\)
and \(p\nmid ab\). Let \(F_-,G_-\) and \(F_+,G_+\) be their nonzero
minimum- and maximum-weight components for weights \((0,1,3,4)\). Then
\[
 \boxed{\sqrt{(F_-,G_-)}=\sqrt{(h_-)},\qquad
 \sqrt{(F_+,G_+)}=\sqrt{(h_+)},\qquad h_-,h_+\in P,}
 \tag{6}
\]
where \(h_-,h_+\) are the nonunit gcds of the respective component pairs.
Thus both extreme pairs have only height-one minimal primes, and each gcd
contains the curve. Neither original equation can have just one weight
component, by the earlier trace theorem. The same conclusions hold in
characteristic zero by the identical argument.

### Degeneration and connectedness proof

If the minimum weights are \(i_-,j_-\), form the polynomials
\[
 \widetilde F=\lambda^{-i_-}
 F(x_0,\lambda x_1,\lambda^3x_2,\lambda^4x_3),\quad
 \widetilde G=\lambda^{-j_-}
 G(x_0,\lambda x_1,\lambda^3x_2,\lambda^4x_3).
\]
The substitution preserves \(C_0\) when \(\lambda\ne0\), and at zero
these specialize to \(F_-,G_-\). Hence, in \(R[\lambda]\),
\[
 \sqrt{(\widetilde F,\widetilde G)}
 =\sqrt{(\lambda,F_-,G_-)}\cap PR[\lambda].
 \tag{7}
\]
This follows on affine cones, including the origin, by the Nullstellensatz.

Every minimal prime of \((F_-,G_-)\) has height one or two. A height-two
minimal prime \(\mathfrak q\ne P\) would give a height-three minimal
prime \((\lambda,\mathfrak q)\) in (7): it cannot contain
\(PR[\lambda]\), since contraction would give \(P\subset\mathfrak q\),
forcing equality. Nor can it contain another special-fiber minimal prime.
The height theorem for the two-generated left-hand ideal excludes it.
Thus \(P\) is the only possible height-two minimal prime of the
special-fiber ideal.

If \(P\) were its sole minimal prime, \(F_-,G_-\) would be a supported
weight-homogeneous pair of degrees \((a,b)\), contradicting \(p\nmid ab\)
and the trace theorem. There must therefore be a height-one minimal prime.
Set \(h=\gcd(F_-,G_-)\), a nonunit. The preceding argument gives
\[
 \sqrt{(F_-,G_-)}=\sqrt{(h)}\cap P.
 \tag{8}
\]
This equality also holds if \(P\) is not minimal, since both components
already contain \(C_0\) set-theoretically.

It remains to prove \(h\in P\). Work in the regular local ring
\[
 T=R[\lambda]_{(x_0,x_1,x_2,x_3,\lambda)},\qquad
 J=(\widetilde F,\widetilde G)T,\qquad E=T/J.
\]
Equations (7)–(8) give
\(\sqrt J=\sqrt{(\lambda,h)T}\cap PT\). Its minimal primes all have
height two, so \(J\) is a regular-sequence ideal and \(E\) is
Cohen–Macaulay. Let \(\mathfrak a,\mathfrak b\) be the images of
\(\sqrt{(\lambda,h)T}\) and \(PT\) in \(E\). Their intersection is
nilpotent. Neither ideal is nilpotent: the horizontal prime \(PT\) and
the vertical primes \((\lambda,H)T\), for irreducible factors \(H\) of
\(h\), are distinct primes of height two. They all survive localization,
since the factors are homogeneous of positive degree.

The Mayer–Vietoris sequence starts
\[
0\longrightarrow H^0_{\mathfrak a+\mathfrak b}(E)
\longrightarrow H^0_{\mathfrak a}(E)\oplus H^0_{\mathfrak b}(E)
\longrightarrow E\longrightarrow H^1_{\mathfrak a+\mathfrak b}(E).
\]
Both middle summands are nonzero: for large \(N\), the nonzero ideal
\(\mathfrak b^N\) is annihilated by \(\mathfrak a^N\), and conversely.
Depth at least two along \(\mathfrak a+\mathfrak b\) would split the
local ring \(E\), as an \(E\)-module, into two nonzero direct summands.
A local ring has no such idempotent decomposition. The depth is therefore
at most one. Put \(K=PT+(\lambda,h)T\). Its image in \(E\) has the same
radical as \(\mathfrak a+\mathfrak b\). Removing the regular sequence
of length two gives
\[
 \operatorname{grade}(K,T)\le3.
\]
Since \(T\) is regular, \(\operatorname{ht}K\le3\). But if \(h\notin P\),
the images of \(\lambda,h\) are a regular sequence in \(T/PT\): after
setting \(\lambda=0\), the remaining quotient is the local domain
\((R/P)_{(x_0,x_1,x_2,x_3)}\), where the image of \(h\) is nonzero.
Thus \(\operatorname{ht}K=4\), a contradiction. Consequently \(h\in P\).
Primality of \(P\) means it contains an irreducible factor of \(h\),
so it is redundant in (8), proving the minimum assertion in (6).
The inverse torus action proves the maximum assertion.

The torus, height, and local-cohomology steps are characteristic-free.
The only changed input from the characteristic-zero proof is the
exclusion of a supported weight-homogeneous pair of degrees \((a,b)\),
now supplied whenever \(p\nmid ab\).

### An exact bound with at most two weights per equation

Suppose \(\max(a,b)<p\), and each of \(F,G\) has at most two nonzero
weight components. Neither can have just one, so write
\(F=F_-+F_+\), \(G=G_-+G_+\). Equation (6) gives nonunit
weight-homogeneous \(h_-,h_+\in P\). They cannot share an irreducible
factor, since it would divide all four components and hence \(F,G\).
Their common zero set is contained in that of \(F,G\), while both vanish
on \(C_0\). Therefore
\[
 V(h_-,h_+)_{\mathrm{red}}=C_0.
\]
The trace theorem forces \(p\mid\deg(h_-)\deg(h_+)\). Both degrees are
at most \(\min(a,b)<p\), a contradiction. Thus any supported pair with
both degrees below \(p\) must have at least three weight components in
at least one equation, and at least two in the other.

Let \(\delta_{\le2\mathrm{wt}}(p)\) minimize the larger defining degree
when each equation has at most two weights. The known \((4,p)\) pair
attains the resulting lower bound, so
\[
 \boxed{\delta_{\le2\mathrm{wt}}(p)=p\qquad(p\ge7).}
\tag{9}
\]
This includes pairs in which neither equation is weight-homogeneous.
Equation (6) constrains all prime-to-\(p\) degree products, but (9) is
still a class minimum. More weight components remain possible; neither
assertion establishes an unrestricted growing lower bound.

Independent reconstruction on October 31, 2026 accepted (6)–(9). The
review covered the degeneration's radical identity, exclusion of extra
height-two primes, survival of the horizontal and vertical components
under localization, nonzero local-cohomology summands, the grade/height
argument, and the two-weight corollary including its sharp attainment.
The prime-to-\(p\) hypothesis and the remaining class restriction are
essential parts of the reviewed statements.

## Why the next weight case needs full cancellation control

The two-weight proof does not extend by arguing that a middle component
must meet some residual curve away from \(C_0\). The following exact
control works in characteristic zero or \(p\ge7\). Put
\[
 A=x_1^3-x_0^2x_2,\qquad D=x_2^3-x_1x_3^2,\qquad
 q=x_0x_3-x_1x_2.
\]
Set \(F=A^2+q^3+D^2\), \(G=A^2+D^2\). Both have ordinary degree
six. Their weights are \(6,12,18\) and \(6,18\), respectively, so the
extreme gcds are \(h_-=A^2,h_+=D^2\), both in \(I_{C_0}\).
This example satisfies \(4\mid ab\), and for every \(p\ge7\) it also
satisfies \(p\nmid ab\) and \(\max(a,b)<p\).

Use the [Segre calculation](../synthesis/fixed_surface_and_endpoint_algebras.md#2-a-control-residual-curves-can-meet-all-three-fixed-surfaces-only-on-c)
on \(Q=V(q)\):
\[
 (x_0,x_1,x_2,x_3)=(\alpha u,\alpha v,\beta u,\beta v),\quad
 h=\alpha v^3-\beta u^3,\quad A|_Q=\alpha^2h,\quad D|_Q=-\beta^2h.
\]
Since \(\alpha,\beta\) have no common zero, this proves
\[
 V(A^2,D^2,q^3)_{\mathrm{red}}=C_0.
\tag{10}
\]
Thus the middle component removes **every** residual component of the
common extreme-component locus without leaving a point off \(C_0\).

Nevertheless \((F,G)=(G,q^3)\), and
\[
 G|_Q=(\alpha^4+\beta^4)h^2.
\]
The polynomial \(\alpha^4+\beta^4\) has four distinct projective roots
in the asserted characteristics. Since \(q\) is irreducible and does
not divide \(G\), the pair is proper, but its reduced support is \(C_0\)
plus the four corresponding ruling lines \(L_i\) on \(Q\). Its cycle is
\(6[C_0]+3\sum_{i=1}^4[L_i]\), with residual degree twelve. For example,
\([\alpha:0:1:0]\), where \(\alpha^4=-1\), is an extra point with
\(A^2=-1,D^2=1,q=0\). It is outside \(V(A,D)\), so (10) does not see it.

The supported triple (10) and the unsupported pair are distinct. This
control does not construct a supported three/two-weight pair or prove
that none exists. It shows why a proposed extension must control zeros
created by cancellation **outside** the common extreme locus, even after
the middle component has removed all residual curves on that locus.
Here the constant generator change exposes the eigen equation \(F-G=q^3\),
so the earlier trace theorem also detects the failure of sole support.
Independent reconstruction checked the Segre factorization, triple and
pair supports, properness, degree and weight constraints, residual cycle
and extra point. The control is reviewed provisional evidence, not a
canonical promotion.
