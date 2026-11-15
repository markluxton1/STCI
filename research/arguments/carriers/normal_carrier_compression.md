# Divisor compression and bounds on generically regular carriers

These are reusable conditional theorems, not an exclusion for arbitrary
higher-degree carriers. Global compression requires a normal hypersurface
and a rational **whole** resolution. The order-one normal-line inequality
also applies to a generically regular nonnormal carrier, by the independently
reviewed [pullback defect proof](numerical_surface_pullback.md). Characteristic
zero is retained for the fixed-quartic normal-bundle, BF and surface-classification
applications; the Picard/section-lifting compression itself is valid on rational
surfaces in other characteristics when its same geometric hypotheses hold.

## 1. Global denominator compression

Let `S` be a normal integral hypersurface of degree `a`, with smooth
rational projective resolution `sigma:M->S`, and let `C` be an integral curve of degree
`delta`. A degree-`b` mate gives an effective Cartier divisor `rC` with
`r delta=ab`. Put `H=sigma^*O_S(1)` and write the numerical pullback of
`C` as `c+Z`. Then `c+Z == (delta/a)H` in the numerical divisor space.

Let `n` be the least positive integer clearing the denominators of both `Z` and `delta/a`. The divisor

    n((delta/a)H-c-Z)

is integral and numerically trivial. On a smooth projective rational
surface numerical triviality implies linear triviality: this is true on
`P^2` and on a Hirzebruch surface, and a blowup adds a free exceptional
Picard summand. One can also use a common smooth resolution of a
birational map to one of these surfaces. This includes the absence of
numerically trivial torsion, not merely the vanishing of `Pic^0`.

The integral divisor is therefore principal. Pushforward of a principal
divisor under the birational map is the principal divisor of the same
rational function on the normal surface; exceptional prime divisors
disappear. Consequently

    nC ~ (n delta/a)H_S

as **Weil divisors** on `S`. Because the divisor on the right is Cartier,
`nC` is Cartier. Its effective divisor supplies a nonzero section of
`O_S(n delta/a)`. The hypersurface restriction sequence lifts that section
to `P^3`, since `H^1(P^3,O(t))=0` for every integer `t`. Its zero support
on `S` is precisely `C`.

Normality matters twice: principal-divisor pushforward has the expected
Weil-divisor meaning, and the effective Cartier divisor determined by the
section has the specified support. Rationality of the **whole** resolution
matters for numerical-to-linear equivalence. The argument makes no
assertion that numerical coincidence on a nonrational resolution suffices.

For `a=delta=4`, the integer `n` is the least common denominator of `Z`.
Every actual mate degree `b` makes `b(c+Z)` an integral Cartier pullback,
so every coefficient denominator divides `b`. Hence `n|b`. Compression
then produces a degree-`n` mate, making `n` the exact least mate degree for
this fixed normal quartic carrier under the existence hypothesis. It
legitimately removes possible local torsion inflation in this global
rational-resolution setting; it does not assume a cancellation law in an
arbitrary local class group.

## 2. A determinant bound with singular or nonreduced anticanonical divisor

For this section add the **normal-quartic rational-resolution**
classification hypotheses: the resolution is minimal, there is an
effective exceptional anticanonical divisor \(E=-K_M\), and
\(d=-E^2\in\{1,2,3\}\) with \(\rho(M)=10+d\). These are extra
geometric inputs from the classified normal quartics, not consequences
of the arbitrary-degree compression theorem in Section1.

Take **all** exceptional prime curves `E_i` of the minimal resolution and
write

    A_ij=-E_i.E_j,  b_i=-E_i^2,  E=sum a_i E_i.

Here `A` is positive definite, each `b_i` is a positive integer, and each
`a_i` is a nonnegative integer. Exceptional classes are independent and
orthogonal to `H`, which has positive square. Therefore

    r<=rho(M)-1=9+d.

Relative nefness and adjunction for an integral curve on a smooth surface
give

    (Aa)_i=K_M.E_i=b_i+2p_a(E_i)-2>=0.

Arithmetic genus, rather than geometric genus, is the correct invariant
here. It is nonnegative even when the prime curve is singular. If `a_i=0`,
the expression also equals `-E.E_i<=0`; therefore it is zero. Since
`b_i>0`, this forces `b_i=2`, `p_a(E_i)=0`, and disjointness from the
support of `E`. In particular a vertex with `b_i>2` has `a_i>=1`.

All terms in the following sum are nonnegative:

    d=a^T A a=sum a_i(b_i+2p_a(E_i)-2).

For every vertex with `b_i>2`, its summand is at least `b_i-2`. Thus

    sum (b_i-2)_+ <= d.

The integer inequality `b<=2(3/2)^((b-2)_+)` holds for every `b>=1`;
after `b=3` it follows by multiplying successively by ratios at most
`3/2`. Hadamard's inequality consequently yields

    det A <= product b_i
          <= 2^r (3/2)^d
          <= 512*3^d.

The numerical correction is `Z=A^(-1)m` with integral
`m_i=c.E_i`. The adjugate formula implies that its common denominator
divides `det A`. Combining with section 1 gives compressed mate bounds
`1536`, `4608`, and `13824` for `d=1`, `2`, and `3`, respectively.

No step assumed that `a_i=1`, that the components are smooth rational
curves, or that the dual graph is a reduced cusp cycle. The use of
arithmetic genus and the nonnegative integer multiplicities is exactly
what allows singular, reducible and nonreduced anticanonical divisors.
The estimate would not follow from an arbitrary further blowup, since
that could introduce exceptional `(-1)` curves and destroy relative
nefness; the source explicitly supplies the required minimal resolution.

## 3. A small cusp numerical survivor is killed by the compression

A reduced rational cycle with intersection matrix

`A=[[3,-1,0,-1],[-1,2,-1,0],[0,-1,2,-1],[-1,0,-1,2]]`

has `E=sum E_i`, `E^2=-1`, and determinant four. A smooth-curve
intersection vector meeting the vertex opposite the `(-3)` vertex would
be `m=(0,0,1,0)`. The correction is

`A^(-1)m=(1,3/2,2,3/2)` and `m^T A^(-1)m=2`.

Adding six independent `A1` intersections gives total correction five,
with numerical denominator two. If this configuration belonged to an
actual mate-compatible rational normal quartic, §1 would produce a
quadric mate, contradicting the unique-quadric obstruction.

This is an exact numerical illustration, not a claim that the specified
smooth curve passage or first-normal order exists on a quartic. In
particular assigning a local first-normal order of three at this cusp
has not been justified. The point is that a numerical configuration
which survives a coarse genus/rank budget may still be eliminated by
global denominator compression.

## 4. The normal-line bound for an order-one carrier

Let `(F_a,G_b)` define a characteristic-zero smooth rational quartic
set-theoretically, with `F_a` of generic normal order one. Every
irreducible factor of `F_a` must contain `C`: its intersection with
`G_b` has a curve component in projective three-space, and the complete
intersection has reduced support only `C`. A common factor of both
equations would give an impermissible surface component. Two factors
containing `C`, including a repeated factor, would give normal order at
least two. Thus `F_a` defines an integral surface `S`, regular at the
generic point of `C`.

The identification of the BF line bundle with the normal sheaf can be
made explicit. If `N_C^*=O(-7)^2`, the first symbol of `F_a` defines a
rank-one image whose saturation is a line subbundle. The conormal of
`C` in `S` is the cokernel of that symbol; after removing torsion it is
the quotient by the saturated image. The mate has the same generic first
symbol direction, or zero first symbol: independent directions would
make the transverse intersection length one, whereas `ab/4>=4`.
Consequently this saturated quotient is the BF first piece

    L=O(e-7),

and `deg N_(C/S)=7-e`. Zeros of the carrier symbol contribute torsion,
not a change of this torsion-free quotient. This prevents an accidental
extra divisor from entering (U4).

Since the carrier is regular at generic `C`, its normalization is an
isomorphism there. The unique curve `C^nu` above `C` maps isomorphically
to the smooth curve `C`: its rational lift extends across each point by
properness, giving a section and hence a closed immersion. Normalization
is finite, so it has no exceptional curve over a closed point of `S`.
The mate's Cartier divisor on the normalization is exactly `mC^nu`,
where `m=ab/4`. On a resolution, its Cartier pullback shows

    (C^nu)^# == (b/m)H = (4/a)H,
    ((C^nu)^#)^2 = 16/a.

The [numerical-pullback proof](numerical_surface_pullback.md) gives the exact comparison:
principalizing the curve ideal gives `D=c+Z`, relative generation gives
`D.E_i<=0`, and the positive-definite matrix with nonpositive
off-diagonal entries implies `Z>=R` for the numerical correction `R`.
The restricted ideal surjection identifies the torsion-free conormal
with `O_c(-D)`, so

    deg N_(C/S)-((C^nu)^#)^2=(Z-R).c>=0.

This proof still applies if `S` is nonnormal at finitely many points on
`C`: all resolution exceptional curves map to points after its finite
normalization, while generic regularity preserves coefficient one along
the strict transform. Thus

    16/a <= 7-e,
    a >= ceil(16/(7-e))

is verified. Together with the already known `a>=4`, the bounds for
`e=0,...,6` are `4,4,4,4,6,8,16`. The degree here belongs to the
generically regular carrier, and cannot be assigned to a mate whose
generic normal order is higher.

## 5. Early-defect and ancestor degree bounds

The [order-one frontier argument](https://github.com/markluxton1/STCI/blob/d158a740d2449c458867ccbc5e3b2ee2c4bec2f4/research/supplements/ORDER_ONE_JETS_AND_DEGREE_BUDGETS.md#2026-10-06-uniform-order-one-frontier)
has the following direct algebraic consequence. For a,b>=4 and an order-one equation, set
s=ab/4-1 and c=7-e. Adjunction gives

\[
\deg D_s=cs+14-4(a+b).
\]

Effectivity forces c>0, so e<=6. Writing s=2q+r or s=3q+r and using
superadditivity gives q deg D2<=2cq+cr+14-4(a+b), and the analogous
third-defect bound. Since c<=7, the additive correction is strictly
negative in both cases (at most 7-18 or 14-18). Thus

\[
\deg D2\le2(7-e)-1,\qquad\deg D3\le3(7-e)-1.
\]

Here q>=1 because ab/4>=4. For the fixed-C0 ancestor application with
the recorded first-socle targets u,v, take
equal-degree multipliers `F_d,G_d` of degree `d`, mapping an ancestor of
graded degree `-(d+3)` to the two first-socle targets of degree `-3`.
Let `n>=3` be its top principal-part order. Assume at least one multiplier
has nonzero linear normal symbol, as in the linked actual-symbol
contraction argument. Its ancestor inequality follows from the top
section degree after removing the pure-power direction:

\[
7n-4d-5-e(n-1)\ge0
\iff (7-e)(n-1)\ge4d-2.
\]

This confirms the stated finite early-jet reduction under its checked BF,
normal-bundle, and linear-contraction inputs. It does not cover two
entirely thick equations or bound either equation degree.

## Evidence and scope

The general compression, arithmetic-genus determinant proof, order-one
application and early-jet bounds reuse their accepted independent source
reviews. The normal-quartic classification supplies the d/rho data; see
[Ishii--Nakayama, Main Theorem and rational types](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf).
Exact arithmetic and the cusp illustration are checked by
[verify_normal_rational_carrier_compression.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_normal_rational_carrier_compression.py).
No new execution is needed for their unchanged formulas. The exact fixed-C0
normal bundle is proved in [the bisection argument](genus_two_bisection_proof.md#2-the-characteristic-zero-normal-bundle).

These bounds do not enumerate surfaces, construct a numerical model as a
carrier, cancel arbitrary local class-group torsion, or cover a pair whose
two equations both have generic normal order at least two. For fixed-C0
quartic mates the later [full exclusion](quartic_carrier_proof.md) closes
that special case; the general compression and higher-degree necessary
bounds remain useful mathematics.


## Consolidated historical supplement: `research/supplements/MIXED_DEGREE_NORMAL_FORMS_AND_POLES.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Mixed-degree normal forms and their pole divisors

For fixed C0 in characteristic zero, this owner separates an allowed global generator subtraction from an uncontrolled rational ratio of first-normal symbols. The actual homogeneous restriction map determines the quotient of possible normal coefficients. Its principal-part class is finite-dimensional even when the ratio has poles; the positions, multiplicities and common vertical divisor remain part of the data.

The original degree (4,5)/(4,6) existence questions are closed by the fixed quartic-carrier theorem. These arguments retain independent structural value: the regular-ratio reduction, exact rational-pole parameterization, countermodels and first-blowup incidence examples explain why local source compatibility does not produce global supported equations. Neither a regular ratio nor a first-blowup common factor is automatic.


The low-degree normal-order bound and persistence argument used below are proved in [formal normal intersection geometry](../normal-geometry/formal-normal-intersection.md), in the retained P-011 and P-006 proofs.

## corrected first-normal reduction for the mixed \((4,6)\) pair

<a id="p-021"></a>

Let \(F,G\) have degrees four and six.  The quartic cannot have normal order
two by P-011.  If both equations initially have order one, P-006 makes their
normal linear forms proportional over \(k(C)\).  Write them on the exceptional
surface as

\[
 f_1=H_F L,\qquad g_1=H_G L,
\]

where \(L\) is the primitive horizontal factor.  The quotient \(H_G/H_F\)
is a **rational**, not automatically regular, section of
\(O_C(2)=O_{\mathbf P^1}(8)\).  A global subtraction is available only on the
regular-ratio branch
\(\operatorname{div}(H_G)\ge\operatorname{div}(H_F)\).  On that branch,

\[
 H^0(\mathbf P^3,O(2))\longrightarrow H^0(C,O_C(2))
\]

is surjective.  Subtracting a quadratic multiple of \(F\) from \(G\) therefore
puts the pair, without changing its ideal, in normal orders \((1,2)\).

The regularity condition cannot be omitted.  In the complete local ring
\(k[[t,u,v]]\),

\[
 F=tu+v^6,\qquad G=u
\]

generate \((u,v^6)\), whose radical is \((u,v)\) and whose quotient is finite
free of transverse length six over \(k[[t]]\), but the first-normal ratio is
\(1/t\).  This disproves the formerly stated universal subtraction.

After the permitted subtraction, write G for the transformed sextic of generic normal order two. On

\[
 E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

the first normal divisors have classes

\[
 D_F\sim(9,1),\qquad D_G\sim(10,2).
\]

Write the saturated horizontal component common to them as
\(R\sim(e,1)\), retaining every closed-point order jump as a vertical divisor:

\[
 D_F=V_B+R,\qquad V_B\sim(9-e,0),
\]

\[
 D_G=R+V_W+T,\qquad
 V_W\sim(w,0),\quad T\sim(10-e-w,1).
\]

Let \(S_q\sim(1,1)\) be the section defined by the normal direction of the
unique quadric.  On that quadric, with \(C\sim(1,3)\), neither equation can be
\(q\)-divisible, and

\[
 F|_Q=C+\rho,\qquad \rho\sim(3,1),
\]

\[
 G|_Q=2C+\sigma,\qquad \sigma\sim(4,0).
\]

The common horizontal section cuts

\[
 D_0=R\cap S_q,\qquad \deg D_0=e+1,
\]

and the exceptional-divisor identities show scheme-theoretically that

\[
 D_0\subset\rho\cap\sigma.
\]

If \(\rho\) and \(\sigma\) have no common component, their proper intersection
on \(Q\) has length

\[
 (3,1)\cdot(4,0)=4.
\]

Hence \(e+1\le4\).  If \(e\ge4\), the two residuals share a component; since
\(\sigma\) is a sum of four ruling fibers, that component is an extra ruling
line contained in both ambient equations.  Therefore every pair in the
regular-ratio branch must
satisfy

\[
 \boxed{e\in\{0,1,2,3\}},
\]

so the vertical singularity divisor of the quartic has degree
\(9-e\ge6\).

For the omitted nonregular order-\((1,1)\) branch, the original divisors have
classes \((9,1)\) and \((17,1)\).  A primitive common horizontal factor may
have \(e\le8\); the endpoint \(e=9\) has constant \(H_F\) and is therefore
regular.  These pole/vertical-divisor strata are not covered by the finite
list below and form a separate necessary incidence stratum; they do not reopen the closed actual mate question.

This bound is sharp at first-normal order.  For \(C_0\), exact linear algebra
identifies the quartic normal image as a rank-17 subspace of
\(H^0(O(9))^2\), and the sextic quadratic-normal image as a rank-22 subspace
of \(H^0(O(10))^3\).  For each \(e=0,1,2,3\), their common-factor incidence
has a nonempty full-rank locus, even after imposing non-\(q\)-divisibility and
the absence of a common residual ruling on \(Q\).  One explicit \(e=0\)
example is

\[
\begin{aligned}
F={}&A(x_0+x_1+x_2+x_3)+B(x_2+x_3)+Dx_2\\
 &+q(x_1x_3+x_2^2+2x_3^2)+2q^2,\\
G={}&A^2+4q^3.
\end{aligned}
\]

Its normal forms are \(H_9a\) and \(a^2\); neither equation is
\(q\)-divisible and the residual divisors on \(Q\) share no ruling.  Yet its
generic transverse length is three rather than six, leaving residual degree
twelve.  Within the regular-ratio branch, the next decisive conditions are
the vanishing,
after formal elimination by the quartic, of the cubic, quartic, and quintic
transverse coefficients, followed by nonvanishing of the sextic coefficient.
The first blowup cannot replace those higher-jet equations.

## finite pole-divisor strata for the nonregular mixed pairs

<a id="p-031"></a>

The ratio gap in P-021 and P-026 is not an arbitrary infinite-dimensional
phenomenon.  It has an exact divisor parameterization.  Let \(b=5\) or \(6\)
and put \(\delta=4(b-4)\), so \(\delta=4\) or \(8\).  On
\(E=\mathbf P(N_{C_0}^*)\), an order-one degree-\(d\) normal divisor has
class \((4d-7,1)\).  Write the primitive common horizontal factor and its
vertical coefficients as

\[
 f_1=hL,\qquad g_1=kL,\qquad L\sim(e,1),
\]

\[
 \deg h=m=9-e,\qquad \deg k=m+\delta.
\]

For the zero divisors \(H=(h)_0\) and \(K=(k)_0\), define their coefficientwise
common part and the remaining pole and zero divisors by

\[
 A=H\wedge K,\qquad P=H-A,\qquad Z=K-A.
\]

Then

\[
 H=A+P,\qquad K=A+Z,\qquad P\wedge Z=0,
\]

\[
 c=\deg A,\qquad p=\deg P,\qquad
 c+p=9-e,\qquad \deg Z=p+\delta.
\]

The quotient \(k/h\) is a rational section of \(O_{\mathbf P^1}(\delta)\)
with divisor \(Z-P\).  It is regular exactly when \(p=0\).  Thus \(A\) records
the common vertical order jumps and \(P\) records precisely the poles omitted
by the former reductions.

Generator changes give finite principal-part quotients.  For \((4,6)\),
restriction of ambient quadrics to \(C_0\) is all of \(H^0(O(8))\), and

\[
 H^0(O(m+8))/hH^0(O(8))\simeq H^0(O_H(m+8))
\]

has dimension \(m\).  On an affine chart whose point at infinity avoids
\(H\), polynomial division and subtraction of a quadratic multiple of \(F\)
give the representative

\[
 \boxed{k=r,\qquad \deg r<m.}
\]

and \(c=\deg\gcd(h,r)\), \(p=m-c\).  This polynomial remainder is a chartwise
description of the intrinsic principal part, not a preferred global
coordinate.  For \((4,5)\), the restrictions of ambient linear forms in the
standard monomial coordinate are

\[
 W_5=\langle1,z,z^3,z^4\rangle\subset H^0(O(4)),
\]

with missing section \(z^2\).  Intrinsically there is an exact sequence

\[
 0\longrightarrow H^0(O(4))/W_5
 \longrightarrow H^0(O(m+4))/hW_5
 \longrightarrow H^0(O_H(m+4))
 \longrightarrow0.
\]

Thus the quotient has dimension \(m+1\): one missing-restriction coordinate
and an \(m\)-dimensional principal part on \(H\).  After choosing a lift \(r\)
of that principal part, it has the representative

\[
 \boxed{k=\lambda z^2h+r,\qquad \deg r<m.}
\]

Here vanishing of the principal part, equivalently \(r=0\) in any such
splitting, is exactly the regular-ratio slice used in P-026; a nonzero
principal part is the full nonregular locus.  On a chart avoiding \(H\), the
lift can be taken with \(\deg r<m\).  The invariant data are its class on
\(H\) and the pole divisor \(P\), not the chosen polynomial remainder.

For \((4,5)\), P-016 leaves gcd types \(e=0,m=9\) and \(e=1,m=8\), and P-025
eliminates the first type without any regular-ratio assumption.  Jaffe's
checked no-common-singularity theorem forces a genuine \((4,5)\) pair to
have a point where both carriers are singular.  Since \(L\) is primitive,
this is exactly \(A\ne0\), or \(c\ge1\).  Hence every remaining nonregular
candidate satisfies

\[
 \boxed{e=1,\qquad 1\le p\le7,\qquad c=8-p,\qquad
 \deg Z=p+4.}
\]

There are seven numerical pole-length strata.

For \((4,6)\), nonregularity first gives \(0\le e\le8\) and \(p\ge1\).
The pair \((4,6)\) is likewise absent from Jaffe's list for carriers with no
common singular point, so again \(c\ge1\).  Before using the global
multiplicity-six filtration, the exact first-normal reduction is

\[
 \boxed{0\le e\le7,\qquad 1\le p\le8-e,\qquad
 c=9-e-p,\qquad \deg Z=p+8.}
\]

This is a triangle of \(8+7+\cdots+1=36\) preliminary numerical strata, while
the regular branch has P-021's preliminary list \(p=0,\ e=0,1,2,3\).  P-042
later imposes the global lci condition \(e\in\{0,1\}\), leaving only 15 of the
nonregular strata and only the first two regular values.

Finite flatness controls special transverse orders but not pole length.  At a
common singular point a length-five fiber forces orders \((2,2)\); a
length-six fiber permits \((2,2),(2,3),(3,2)\).  Nevertheless, for every
\(\alpha\ge1\),

\[
 F=t^\alpha u+v^n,\qquad G=u
\]

defines \((u,v^n)\), which is free of rank \(n\) over \(k[[t]]\), while its
first-normal ratio is \(t^{-\alpha}\).  No bound on \(p\) can therefore follow
from flat transverse length alone.

The unique quadric gives useful exact tangency budgets.  If
\(D_0=L\cap S_q\), then

\[
 R_4|_{C_0}=D_0+H,\qquad R_b|_{C_0}=D_0+K,
\]

and their common restriction has degree
\(\deg(D_0+A)=10-p\).  The residual intersections on the quadric have total
length ten for \((4,5)\) and fourteen for \((4,6)\).  If

\[
 \epsilon_x=i_x(R_4,R_b)-\operatorname{ord}_x(D_0+A),
\]

then \(\epsilon_x\ge0\) and

\[
 \boxed{\sum_x\epsilon_x=p\quad\text{for }(4,5),}
\]

\[
 \boxed{\sum_x\epsilon_x=4+p\quad\text{for }(4,6).}
\]

These are exact constraints, not contradictions.  They show that every unit
of pole length must reappear as residual excess tangency.  P-038 completes the
formerly conjectural defect comparison in the opposite direction:
\(A=2D\) scheme-theoretically.  Hence the type-B \((4,5)\) list collapses to
the single stratum \((c,p,\deg Z)=(2,6,10)\).  P-042 subsequently restricts
every hypothetical \((4,6)\) lci to horizontal degree \(e=0\) or \(1\), so
only15 of the36 preliminary nonregular strata satisfy that additional necessary filtration restriction. They are not current open quartic-mate existence cases after R-0001.

## Characteristic boundary

The decomposition H=A+P,K=A+Z and the principal-part quotient by the **actual** ambient restriction image are algebraic constructions over any field with the stated source and line-bundle data. The numerical e-strata here additionally use their characteristic-zero balanced conormal and no-common-singularity inputs; they must not be imported wholesale to a prime. In characteristic2 the fixed-quartic normal bundle changes. The [every-positive-characteristic quartic-carrier construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) is the separate positive control. A pole-divisor parameter space and correct local finite-flatness do not by themselves construct a global supported pair.



## Consolidated historical supplement: `research/supplements/NORMAL_CARRIERS_PRIMITIVE_JETS_AND_CHARACTERISTIC.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Primitive quartic structures: extension, contact, and factorization

The first unit develops the distinct extension obstruction and ambient
contact maps, including their exact e=1 coordinates and the geometric
limits of a naive jet budget. The second proves the full universal e=2
primitive-fourth classification and cubic factorization. The third gives
a separate parity classification with its bounded fourth-layer defect
obstruction. These statements retain their exact filtration hypotheses;
the [all-degree quartic-carrier theorem](quartic_carrier_proof.md)
is proved independently of the remaining explanatory questions.

---

<a id="2026-10-06-order-one-jet-discrepancy-framework"></a>

## Extension and quartic contact maps on the quadric

Status: structural research note. Statements are labelled individually. This note does **not** prove that the rational quartic is not an STCI.

### 0. Scope and audited starting point

Work in characteristic zero on the fixed smooth monomial rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3,
\]
with unique smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\). In the ruling convention used here, C has class (3,1), and the residual quartic restriction has class (1,3). The audited order-one setup has
\[
N_C^*\simeq O_C(-7)^2\twoheadrightarrow L\simeq O_C(e-7),\qquad e=0,1,2
\]
for quartic carriers. The exact statements below retain their own extension, rank and filtration hypotheses.

The audited e=2 result is stronger than the older P-044-slice formulation: the universal fourth-extension obstruction has reduced zero locus
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on this whole resultant-open locus
\[
H^0(I_{C_3}(4))=H^0(I_{C_4}(4))=T\,H^0(O_{\mathbf P^3}(1)).
\]
This is certified by the universal primitive-quadruple verifier and independently reconstructed by the quartic-factor audit. The dx=1 P-044 saturation certificate is now closed, but it is not needed for the global e=2 carrier exclusion.

### A. Intrinsic setup

#### A.1 Successive condition maps

Let \(C=C_1\subset C_2\subset\cdots\subset C_m\) be primitive with conormal line \(L\), so \(I_{C_j}/I_{C_{j+1}}\simeq L^j\). For degree \(a\), put
\[
V_j(a)=H^0(I_{C_j}(a)),\qquad W_j(a)=H^0(L^j(a)),
\]
and let \(\rho_j(a):V_j(a)\to W_j(a)\) be restriction.

**PROVED (formal).** Define
\[
\eta_j(a)=\dim W_j(a)-\operatorname{rank}\rho_j(a)
\]
(the target shortfall) and
\[
\delta_j(a)=\min\{\dim V_j(a),\dim W_j(a)\}-\operatorname{rank}\rho_j(a)\ge0
\]
(the intrinsic maximal-rank defect). Then
\[
\dim V_{j+1}(a)=\dim V_j(a)-\dim W_j(a)+\eta_j(a).
\]
Thus numerical budget and genuine dependence are separated. For quasiprimitive structures with saturated pieces \(E_j=L^j(D_j)\), use \(W_j(a)=H^0(E_j(a))\); the BF divisors \(D_j\) alter the targets and must not be conflated with rank defects.

#### A.2 Quadric comparison divisor

The conormal sequence for \(C\subset Q\subset\mathbf P^3\) is
\[
0\to O_C(-8)\to N_C^*\to O_C(-6)\to0.
\]
Let \(M=\ker(N_C^*\twoheadrightarrow L)\). Since \(\det N_C^*=O(-14)\),
\[
M\simeq O_C(-e-7).
\]
The composite \(O_C(-8)\to N_C^*\to L=O_C(e-7)\) is a section \(r\in H^0(O_C(e+1))\). Let \(R=Z(r)\). The finite R and 2R formulas in A.2--A.5 assume r is not identically zero. Section K.4 separately treats the actual e=1 comparison-zero boundary.

**PROVED.** The induced map \(M\to O_C(-6)\) is multiplication by the same section up to scalar. Hence
\[
M\simeq O_C(-6)(-R),\qquad \deg R=e+1.
\]

#### A.3 First quartic source

Twisting by \(O_C(4)=O_C(16)\) gives
\[
M(4)=O_C(9-e)\xrightarrow{\cdot r}O_C(10).
\]
After restricting a quartic to \(Q\) and removing \(C\), its residual lies in \(H^0(O_Q(1,3))\), restricting to \(O_C(10)\). Define
\[
K_R=\{h\in H^0(O_C(9-e)):rh\text{ extends to }H^0(O_Q(1,3))\}.
\]

**PROVED.**
\[
K_R\simeq H^0(Q,I_{R/Q}(1,3)).
\]
If \(\operatorname{ev}_R:H^0(O_Q(1,3))\to H^0(O_R(1,3))\), define
\[
\epsilon_Q(R)=\ell(R)-\operatorname{rank}(\operatorname{ev}_R).
\]
Then
\[
\dim K_R=7-e+\epsilon_Q(R).
\]

**PROVED.** For e=0 and e=1, \(\epsilon_Q(R)=0\) for every possible \(R\): \(O_Q(1,3)\) separates every length-one and length-two subscheme. Thus
\[
\dim K_R=7\ (e=0),\qquad \dim K_R=6\ (e=1).
\]
For e=2, length-three schemes can fail to impose three independent conditions. The audited ruling-fiber case has \(\epsilon_Q(R)=1\), hence \(\dim K_R=6\). The first source rank jump is therefore genuinely an e=2 phenomenon.

The residual restriction sequence is

    0 -> O_Q(-2,2) -> O_Q(1,3) -> O_C(10) -> 0.

Since H^0(O_Q(-2,2))=0 and H^1(O_Q(1,3))=0, we obtain

    0 -> H^0(O_Q(1,3)) -> H^0(O_C(10))
      -> H^1(O_Q(-2,2)) -> 0.

By Kunneth,

    H^1(O_Q(-2,2))
      = H^1(P^1,O(-2)) tensor H^0(P^1,O(2)),

so this cokernel has dimension 3.

**PROVED.** The previously observed codimension-three first-normal condition is intrinsic: the extendable degree-10 sections are the kernel of the connecting map to H^1(O_Q(-2,2)). In the affine coordinate basis this is the old

    V = <1,z,z^3,z^4,z^6,z^7,z^9,z^10>;

the missing z^2,z^5,z^8 are a coordinate manifestation of the 3-dimensional cohomological obstruction.

#### A.4 The second primitive quartic condition localizes on 2R

Assume the primitive triple \(C_3\) exists. Then
\[
\rho_2:H^0(I_{C_2}(4))\to H^0(L^2(4))=H^0(O_C(2e+2)).
\]
The quadric square satisfies \(\rho_2(Q^2)=r^2\), up to normalization. Quotienting gives
\[
\bar\rho_2:K_R\to H^0(O_C(2e+2))/\langle r^2\rangle
\simeq H^0(O_{2R}(2e+2)).
\]

**PROVED.** Define
\[
\delta_2^Q(R,C_3)=\min\{\dim K_R,2e+2\}-\operatorname{rank}\bar\rho_2.
\]
For e=0,1,2 the generic source/target sizes are
\[
(7,2),\qquad(6,4),\qquad(5,6).
\]
Only e=2 is generically overdetermined at this stage.

<a id="2026-10-06-quartic-jet-geometry-structural-supplement"></a>

#### A.5 Local first and second jet conditions for e=2

This subsection records the local derivation; signs depend on choices of local generators, but the structural content does not.

Choose local coordinates near p in R:
- u along C,
- v normal to C inside Q,
- w an equation for Q.

Then I_C=(v,w). Normalize the primitive quotient locally so that, to first order,

    v |-> epsilon,    w |-> r epsilon.

Write the canonical triple as

    v = epsilon + alpha epsilon^2,
    w = r epsilon + beta epsilon^2  mod epsilon^3,

and set kappa=beta-r alpha.

A quartic containing C_2 has local expansion

    F = h(w-rv) + 1/2(A v^2 + 2Bvw + Cw^2) + O(I_C^3).

Substitution gives

    rho(F) = h kappa + 1/2(A+2Br+Cr^2),

and modulo r^2,

    bar-rho(F) = [h kappa + A/2 + Br]_{2R}.

Restricting F to Q, write F|_Q=v d_h, where d_h=0 is the residual (1,3)-divisor D_h. Then locally

    d_h = -rh + (A/2)v + ...

At a simple p in R, if u=r is used as local parameter,

    partial_u d_h(p) = -h(p),
    partial_v d_h(p) = A(p)/2.

Thus the value component of bar-rho(F)|_{2p} prescribes a relation between the tangent and transverse derivatives of D_h at p:

    partial_v d_h(p) - kappa(p) partial_u d_h(p) = 0

up to the sign convention for kappa.

**PROVED LOCALLY, subject to the stated generator/sign conventions.** One of the two new conditions at each p in R is a prescribed tangent-direction/contact condition for D_h.

The second coefficient modulo r^2 involves a second jet of d_h, not merely its first jet. Therefore it is premature to identify all six new conditions with containment of three fixed doubled points in Q.

### B. e=2 reconstruction

For e=2 write the quotient by binary quadratics \(A,B\). The comparison section is \(r=A+zB/2\). The exact universal fourth-obstruction locus is
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on it
\[
2r=2A+zB=2a_0+b_2z^3.
\]
Under the standard \(C\subset Q\) identification, the relevant ruling coordinate restricts as \(z^3\).

In the dx=1 coordinate normalization the exact comparison is

    r=x+(a+1/2)z+(1+b/2)z^2+(d/2)z^3.

It is pulled back from a linear equation in that ruling coordinate
if and only if a=-1/2 and b=-2. Then r=x+(d/2)z^3; in the dx=1
normalization d=1/x, this is r=x+z^3/(2x). Thus the P-045 condition
is exactly the ruling-fiber condition in these coordinates. The
statement retains its normalization and generator conventions.

**PROVED.** Every basepoint-free e=2 quotient extending to the canonical primitive quadruple has
\[
R=C\cap F
\]
for a ruling fiber \(F\subset Q\). Thus the fourth-extension condition itself forces the first quartic source to jump from dimension 5 to 6. This is the intrinsic content behind the old P-045 ruling observation, now on the entire universal fourth-obstruction locus. On the relevant fiber,
O_Q(1,3) restricts to O_P1(1). A section vanishing on all three points
of R=C intersect F therefore contains F, including the scheme-theoretic
fiber intersection. Dividing its equation by F identifies
K_R with H0(O_Q(1,2)), of dimension six. This supplies the geometric
source-jump proof, separately from the exact second-map rank below.

**EXACT COMPUTATIONAL CERTIFICATE.** On this locus both \(K_R\) and the finite target of \(\bar\rho_2\) have dimension six, but the audited universal contact matrix has rank exactly three everywhere. Two explicit 3x3 minors, \(-a_0^8\) and \(-b_2^8/256\), cover the parameter space, while all 4x4 minors vanish identically. Hence
\[
\operatorname{rank}\bar\rho_2=3,\qquad \delta_2^Q=3.
\]
In the seven-dimensional ambient pre-contact space (six \(K_R\) directions plus \(Q^2\)), the kernel is four-dimensional and
\[
\boxed{H^0(I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).}
\]

**OPEN CONCEPTUAL STEP.** The ruling condition explains the source jump. The further rank-three collapse is stronger: three of six finite \(2R\) conditions become dependent. The exact matrix proves this universally, but a coordinate-free factorization of \(\bar\rho_2\) through a natural rank-three space attached to the ruling and extension class is still missing.

**PROVED.** BF duality forces the canonical fourth layer to be primitive for the e=2 branches of (4,7) and (4,8). Hence every defining quartic is \(T\ell\). For any mate \(G\), \(V(\ell,G)\) contributes an extra projective curve (or the whole plane), so these e=2 branches are excluded.

### C. e=0 analysis

Here \(L=O(-7)\), \(M=O(-7)\), and \(R\) has length one.

The embedded primitive-triple obstruction lies in
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-7)),
\]
of dimension six.

**PROVED (standard primitive-extension obstruction calculation).** Unlike e=2, a primitive double of direction e=0 does not automatically extend to a triple. If it extends, uniqueness follows from \(H^0(O(-7))=0\). This is compatible with P-010: the defect-free primitive e=0 triple is globally excluded, so positive \(D_2\) is essential in a quasiprimitive carrier filtration.

**PROVED.** Every length-one \(R\) imposes one independent condition on \(|O_Q(1,3)|\), so \(\dim K_R=7\). If a primitive triple existed,
\[
\bar\rho_2:K_R\;(\dim7)\to H^0(O_{2R}(2))\;(\dim2).
\]
Maximal rank would still leave a five-dimensional kernel.

**PROVED NEGATIVE STRUCTURAL RESULT.** The e=2 overdetermined-jet mechanism cannot extend verbatim to e=0. The hard geometry moves to triple existence and, for actual quasiprimitive carriers, to the defect divisor \(D_2\).

**PROVED CONNECTION TO MF6.** MF6 gives \(\deg D_2\ge3\) for e=0 saturated multiplicity-six lci/Gorenstein thickenings and excludes the nonregular (3,6) branch. The (4,5) MF6 incidence lives in a modified target \(L^2(D_2)\), not the primitive target \(L^2\).

**OPEN.** Recast the MF6 type-(4,5) matrix as the quasiprimitive analogue of \(\bar\rho_2\) and identify its exceptional high-gcd locus geometrically.

### D. e=1 analysis

Here \(L=O(-6)\), \(M=O(-8)\), and \(R\) has length two.

\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-4))
\]
has dimension three, while \(H^0(O(-4))=0\).

**PROVED.** Triple existence is a three-coordinate obstruction and, when it exists, the embedded primitive triple is unique. Thus e=1 differs fundamentally from e=2 before quartic second-jet dependence is considered.

**PROVED.** Every length-two subscheme imposes two independent conditions on \(|O_Q(1,3)|\). Hence \(\dim K_R=6\) for every e=1 quotient direction; there is no e=2-style source jump. For an existing primitive triple,
\[
\bar\rho_2:K_R\;(\dim6)\to H^0(O_{2R}(4))\;(\dim4).
\]
Maximal rank leaves a two-dimensional quartic kernel, so quartic survival requires no rank defect.

**The exact coordinate answer appears in Sections J--K below.** An intrinsic incidence interpretation of the obstruction-zero locus remains a separate question.

The audited BF/MF6 e=1 possibilities \((d_2,d_3)=(0,4),(1,3),(2,2)\) should be separated into: first solve the triple-extension obstruction in \(H^1(O(-4))\); then study the finite \(2R\) evaluation map, modified to \(L^2(D_2)\) when \(D_2>0\).

### E. General principle

**PROVED FRAMEWORK.** For a fixed filtration and carrier degree, the signed budget
\[
B_j=\dim V_j-\dim W_j
\]
and maximal-rank defect
\[
\delta_j=\min(\dim V_j,\dim W_j)-\operatorname{rank}\rho_j
\]
separate numerical over/underdetermination from genuine dependence. Rank-defect loci are determinantal loci of families of restriction maps.

**PROVED.** For e=0,1,2, the first two primitive quartic stages are controlled by
\[
R\in |O_C(e+1)|,\qquad
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)).
\]
The source discrepancy is exactly the failure of \(R\) to impose independent conditions on \(|O_Q(1,3)|\). It vanishes identically for e=0,1 and can occur for e=2. On the e=2 fourth-extension locus, extension compatibility forces \(R\) to be a ruling-fiber divisor and the second map has certified rank defect three.

**CONJECTURE.** On the e=2 fourth-extension locus, \(\bar\rho_2\) factors coordinate-freely through a natural rank-three space attached to the ruling fiber and extension class. Such a factorization would explain both rank three and the cubic-times-linear kernel.

**PROVED NEGATIVE RESULT.** There is no uniform theorem saying quartic survival for e=0,1,2 requires jet-rank degeneracy. It is false numerically for e=0 and e=1. A correct uniform theory must include extension-existence obstructions and BF defect divisors, not only containment-map ranks.

#### E.1 Multiplicity growth and the limits of a jet budget

For a primitive complete intersection of surfaces of degrees a,b supported on a degree-d curve, the multiplicity is

    m = ab/d.

Thus increasing carrier degrees has competing effects:
1. it increases the number of available hypersurface sections;
2. it also increases the required multiplicity, hence the number of infinitesimal layers that must be survived.

The relevant comparison is therefore not a single Hilbert-function count. It is the cumulative loss from the successive ranks (or a more invariant replacement accounting for the changing domains) against the initial carrier freedom.

A naive sum of h^0(L^k(a)) is not sufficient: targets can vanish, maps need not be surjective, and dependencies can be forced by geometry. The C_0 ruling-fiber phenomenon is precisely an example where the geometry of the conormal data changes the rank.

#### E.2 A conditional geometric research question

**HEURISTIC / RESEARCH PROGRAM.** Define an expected jet budget for candidate carrier data by comparing available hypersurface freedom with the ranks expected from the successive maps rho_k.

Negative expected budget should not be interpreted as an automatic obstruction. Rather:

> When the expected jet budget is negative, existence of a carrier forces the conormal/multiple-structure data into degeneracy loci of the successive jet maps.

The useful theorem would therefore have the form

    negative expected jet budget
      => STCI only on specified geometric degeneracy loci.

The substantive problem is to describe those degeneracy loci geometrically.

This suggests a possible division:
- underdetermined cases: carrier freedom exceeds the independent jet conditions, so survival is dimensionally plausible;
- overdetermined cases: STCI requires special geometric dependencies among the jet conditions.

Known STCI examples should eventually be tested against this distinction.

The actual rank c_k of a map with domain dimension s_k always satisfies
c_k<=s_k; a proposed regime s_k<c_k is impossible. Only an *expected*
independent-condition count can exceed the domain dimension. Such a
count supplies a determinantal research question, not a theorem of
nonexistence. The explicit e=0/e=1 source-target calculations above
are negative controls for a blanket rank-degeneracy obstruction.

### F. Connections

**Local cohomology — PROVED CONCEPTUAL CONNECTION, not an identification theorem.** The local-cohomology quartic problem is also determinantal: an ancestor \(a\) defines a multiplication matrix \(L(a)\), and multiplier existence is \(\operatorname{rank}L(a)=\operatorname{rank}N(a)+2\). Exact local-cohomology work independently finds exceptional degree-two directions aligned with the e=2 fourth-zero family. A canonical identification with \(\bar\rho_2\) is **OPEN**.

**MF6 — PROVED CONCEPTUAL CONNECTION.** MF6 defect divisors record failure of the primitive associated graded algebra to remain pure powers of \(L\). They modify jet targets from \(L^j\) to \(L^j(D_j)\). MF6 pole/incidence calculations are a quasiprimitive refinement of the jet-budget framework, but the pole divisor is not itself the rank defect.

**P-044/P-045 — PROVED.** The old P-045 ruling condition is the dx=1 shadow of the universal e=2 statement that fourth-extension compatibility forces \(R\) to be a ruling-fiber divisor. The exact dx=1 saturation certificate closes that slice, but the universal primitive-fourth certificate is the stronger carrier input.

**Deformation/extension theory — PROVED.** The obstruction groups
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O(3e-7))
\]
explain why e=0,1,2 differ before any quartic rank count: their dimensions are 6,3,0.

### G. Intrinsic geometric questions

The coordinate e=1 obstruction and its complete reduced zero locus are
proved in Sections J--K below. The remaining structural question is an
intrinsic construction of the map from the quotient pencil
N_C^* -> O(-6) to H1(O(-4)), with a geometric interpretation of its
splitting locus and the associated finite 2R contact map. For e=2,
the rank-three matrix theorem is complete; a coordinate-free factorization
through a natural rank-three space attached to the ruling fiber and
extension class remains a distinct explanatory question.

### H. Literature audit and novelty boundary

The following primary antecedents identify the established extension machinery and the limits of a novelty claim.

#### H.1 Bănică--Forster: extension theory is established machinery

C. Bănică and O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64, is the primary antecedent for the embedded primitive/quasiprimitive filtration used here.

Their Proposition 2.4 states, in the present notation, that extending a primitive multiplicity-k structure \(Z'\) of type \(L\) to multiplicity \(k+1\) is equivalent to choosing a retraction of
\[
0\to L^k\to \nu_{Z'}|_C\to M\to0,
\qquad
M=\ker(\nu_C\twoheadrightarrow L).
\]
Their Corollary 2.5 identifies the splitting obstruction/torsor groups as
\[
H^1(\det(\nu_C)^*\otimes L^{k+1}),\qquad
H^0(\det(\nu_C)^*\otimes L^{k+1}).
\]
For the rational quartic, \(\det\nu_C=O(-14)\), so for double-to-triple extension (\(k=2\)) this is exactly
\[
H^1(O(14)\otimes O(3e-21))=H^1(O(3e-7)).
\]

**LITERATURE-ESTABLISHED, NOT NEW.** The obstruction groups of dimensions \(6,3,0\) for e=0,1,2 are a direct specialization of Bănică--Forster. Likewise their Section 3 already gives the CM filtration, quasiprimitive line bundles \(L_j=L^j(D_j)\), superadditivity \(D_i+D_j\le D_{i+j}\), and the interpretation of later quasiprimitive extensions as meromorphic retractions. These should be cited as the conceptual source of the BF language used throughout STCI.

Source: C. Bănică--O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64; electronic copy on O. Forster's LMU page.

#### H.2 Drézet: modern intrinsic parametrization

Jean-Marc Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, develops primitive curves of arbitrary multiplicity by gluing \(U_i\times\operatorname{Spec}\mathbf C[t]/(t^n)\) and nonabelian \(H^1\). His later survey and papers develop extension, deformation, and moduli theory further.

**LITERATURE-ESTABLISHED, NOT NEW.** Treating primitive multiple curves intrinsically via their canonical filtration and associated line bundle, rather than by ambient coordinates, is standard. Any eventual general theorem should be phrased compatibly with this literature rather than advertised as a new theory of primitive multiple curves.

Relevant sources:
- J.-M. Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, arXiv:math/0605726.
- J.-M. Drézet, *Primitive multiple schemes*, Eur. J. Math. 7 (2021), 985--1045, arXiv:2004.04921.
- J.-M. Drézet, *Primitive multiple curves: classification, deformations and moduli spaces of sheaves* (survey, 2013).

#### H.3 Rational-quartic STCI literature

The unrestricted characteristic-zero rational-quartic STCI problem remains open. The fixed-C0 all-quartic-carrier theorem has its full proof elsewhere. Relevant primary antecedents include:

- P. C. Craighero--R. Gattazzo (1986): the monomial rational quartic is not the set-theoretic intersection of two quartic surfaces.
- P. C. Craighero--R. Gattazzo (1989): no smooth rational quartic is an STCI on a cubic surface.
- D. B. Jaffe, *Applications of iterated curve blow-up to set theoretic complete intersections in P3*, J. reine angew. Math. 464 (1995), 1--46: finite numerical lists of possible degree pairs under the stated hypotheses; for \((d,g)=(4,0)\) the list includes \((4,7)\).
- Ph. Ellia, *Primitive set-theoretic complete intersections* (arXiv:1409.3801): numerical restrictions for primitive STCI structures. Corollary 16 leaves ten rational-quartic numerical cases, including \((a,b,l)=(4,7,5)\), and explicitly describes its improvement over Jaffe as numerical rather than a full rational-quartic exclusion.

**LITERATURE CHECKED / NO PRIOR IDENTIFICATION FOUND.** In the sources located in this search, no formulation was found of the STCI quartic-carrier problem as the pair
\[
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)),
\]
nor a derivation of the e=2 cubic-times-linear factorization from a determinantal rank collapse on the fourth-extension locus. Absence from this search is not a proof of novelty; a stronger novelty claim requires a targeted bibliography/citation-chain search.

#### H.4 Ropes/ribbons literature

The ribbon/rope literature (Bayer--Eisenbud for ribbons; later Gallego--González--Purnaprajna and Drézet for ropes/primitive multiple curves and deformations) confirms that embedded multiple structures, conormal bundles, and deformation maps are mature subjects.

**NOVELTY BOUNDARY.** The potentially project-specific contribution is therefore not:
1. the canonical filtration;
2. conormal quotient \(L\);
3. extension obstruction groups;
4. defect divisors for quasiprimitive structures; or
5. determinantal loci in the abstract.

The candidate new ingredient is their **specific coupling for the rational quartic carrier problem**:
\[
\text{BF extension data}
\longrightarrow R\subset C\subset Q
\longrightarrow K_R
\longrightarrow \text{finite jet evaluation on }2R
\longrightarrow \text{ambient factorization}.
\]
The universal e=2 computation supplies a nontrivial instance where extension compatibility forces a special incidence locus for \(R\), and that incidence is followed by an additional rank-three collapse of the ambient quartic jet map.

#### H.5 Revised status of the framework

**PROVED + LITERATURE-ALIGNED.** The two-layer organization
\[
\text{existence/splitting of the multiple structure}
\quad+\quad
\text{rank of ambient containment maps}
\]
is the correct framework, but the first layer is Bănică--Forster/Drézet theory.

**PROJECT-SPECIFIC PROVED RESULT.** For the rational quartic and quartic carriers, the quadric comparison converts the ambient first-symbol problem into evaluation of \(O_Q(1,3)\) on \(R\), and the next primitive containment condition into a finite map on \(2R\). The e=2 fourth-extension locus forces \(R\) to be a ruling divisor and has exact ambient rank three.

**OPEN NOVELTY QUESTION.** Determine whether this \(R/2R\) ambient-carrier reduction, or an equivalent construction, already occurs in the older literature on contact of surfaces along curves (notably Gallarati), infinitesimal neighborhoods, or Rees/principal-parts methods. Search should continue before publication-level novelty claims.

### J. Exact e=1 primitive-triple obstruction

This section carries out the first revised target from Section G for the fixed quartic
\[
C_0=[s^4:s^3t:st^3:t^4].
\]

#### J.1 Setup

For \(e=1\),
\[
L=O(-6),\qquad M=O(-8),
\]
and every Ferrand double is specified in the fixed split conormal frame by
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
with projective basepoint-free condition
\[
\Delta=a_0b_1-a_1b_0\ne0.
\]

By Bănică--Forster Proposition 2.4, extension to a primitive triple is equivalent to splitting
\[
0\to L^2=O(-12)\to \nu_{C_2}|_C\to M=O(-8)\to0.
\]
The extension class lies in
\[
\operatorname{Ext}^1(M,L^2)=H^1(O(-4)).
\]

**LITERATURE STATUS.** The splitting criterion and obstruction group are standard Bănică--Forster theory. The explicit specialization below to the fixed embedded rational quartic and its quotient pencil was not found in the targeted literature search; it should presently be treated as a project calculation, not a publication-level novelty claim.

#### J.2 Moving-coordinate cocycle

Use the same exact embedded chart transition as in the audited e=2 computation, but now reverse the binary *linear* forms by
\[
A^\vee(w)=wA(1/w),\qquad B^\vee(w)=wB(1/w).
\]
For \(m=Bu-Av\), which has line type \(M=O(-8)\), the quadratic coefficient of the opposite-chart equation gives the Cech cocycle
\[
h_2=-\frac{2A+zB}{8z^5}
\left(12A^2+3z^2B^2+4z^2(A'B-AB')\right).
\]
The same formal expression appeared in the e=2 calculation; the different line type changes which Laurent coefficients survive in cohomology.

For \(H^1(O(-4))\), the basis classes are \(z^{-1},z^{-2},z^{-3}\). Up to a common nonzero scalar, the three obstruction coordinates are
\[
\boxed{
\begin{aligned}
c_1={}&-b_1(2a_0b_1+12a_1^2+16a_1b_0+9b_0^2),\\
c_2={}&-(2a_1+b_0)(8a_0b_1+12a_1^2+4a_1b_0+3b_0^2),\\
c_3={}&-2a_0(2a_0b_1+36a_1^2+16a_1b_0+3b_0^2).
\end{aligned}}
\]

**PROVED COMPUTATIONALLY/FORMALLY.** These are the exact Cech coordinates obtained from the moving-coordinate transition; no sampling is used.

#### J.3 Exact zero locus on the resultant-open quotient space

Localize at \(\Delta\) by adjoining \(t\Delta-1\). An exact Groebner calculation gives, among the localized consequences,
\[
a_0(2a_1+b_0)=b_1(2a_1+b_0)=0,
\]
\[
a_0(a_0b_1+2b_0^2)=b_1(a_0b_1+2b_0^2)=0,
\]
and
\[
a_0(3b_0^2t+2)=b_1(3b_0^2t+2)=0.
\]

Hence the resultant-open zero locus has the following exhaustive set-theoretic decomposition.

##### Main component

If \((a_0,b_1)\ne(0,0)\), then
\[
\boxed{b_0=-2a_1,\qquad a_0b_1=-8a_1^2.}
\]
Here
\[
\Delta=-6a_1^2\ne0,
\]
so \(a_1,a_0,b_1\) are all nonzero. Projectively this is a one-dimensional rational locus.

The quadric-comparison section is
\[
r=A+\frac z2B
=a_0+\frac{b_1}{2}z^2
=a_0-\frac{4a_1^2}{a_0}z^2.
\]
Thus its degree-two divisor \(R\) is a symmetric pair in the chosen affine coordinate. Whether this admits a coordinate-free incidence interpretation is OPEN.

##### Boundary directions

If \(a_0=b_1=0\), put \(r_0=b_0/a_1\). Basepoint-freeness says \(r_0\ne0\), and the remaining obstruction is
\[
(r_0+2)(3r_0^2+4r_0+12)=0.
\]
Thus there are three additional projective quotient directions over an algebraically closed characteristic-zero field:
\[
\boxed{r_0=-2,\quad 3r_0^2+4r_0+12=0.}
\]

At \(r_0=-2\), the comparison section \(A+\frac z2B\) vanishes identically. This is a genuinely exceptional configuration: the primitive conormal kernel \(M=O(-8)\) coincides with the quadric conormal subline \(O(-8)\subset N_C^*\). The divisor \(R\) formalism must therefore be treated separately there; one must not write a length-two \(R=Z(r)\).

At the two quadratic-root directions, the comparison section is a nonzero scalar multiple of \(z\) as an \(O(2)\)-section, so its homogeneous zero divisor consists of the two coordinate boundary points \(0,\infty\).

**PROVED.** The above main component plus three boundary points is the complete reduced/set-theoretic primitive-triple locus on \(\Delta\ne0\), subject to the exact transition conventions already audited for the fixed curve.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_triple\_obstruction.py}.
\]

#### J.4 Consequence for the jet-budget program

The e=1 extension-existence condition is therefore neither vacuous nor a generic three-independent-equation cut. It has a positive-dimensional exceptional component. This reinforces the revised framework:

\[
\text{BF splitting degeneracy}
\quad\text{first, then}\quad
\text{ambient quartic jet rank}.
\]

On the main component, \(R\) has length two and
\[
K_R=H^0(I_{R/Q}(1,3))
\]
has dimension six. The next concrete problem is to compute
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
along the one-dimensional main component and the two nonzero-comparison boundary directions. The \(r\equiv0\) boundary direction requires a separate formulation because the \(R/2R\) reduction degenerates.

#### J.5 Literature check specific to this calculation

A targeted search was made for explicit primitive-triple formulas for embedded rational quartics, Ferrand doubles extended to triples, and formulas for the Bănică--Forster splitting class. The sources located continue to use BF/Ferrand as the general mechanism; no explicit formula matching the three \(c_i\) above was found.

Ellia's primitive-STCI work uses numerical consequences of primitive multiple structures rather than this quotient-pencil splitting locus. Modern papers using quasi-primitive extensions likewise cite BF as the construction machinery. Therefore the safe current classification is:

- **standard:** Ferrand double construction, BF splitting criterion, obstruction group \(H^1(O(-4))\);
- **project-specific exact calculation:** the three displayed \(c_i\) and their resultant-open zero-locus decomposition;
- **unknown novelty:** whether an equivalent classification occurs in older specialized literature not indexed by the searches used here.

Before any external write-up, search citation chains around Bănică--Forster, Ferrand, and older work on multiple/contact structures rather than claiming the explicit locus is new.


### K. Exact e=1 quartic contact on the primitive-triple locus

The e=1 BF splitting locus from Section J can now be tested against the ambient quartic carrier map.

#### K.1 Full quartic-through-double source

The ambient quartic ideal of \(C_0\) has dimension 18. For a quotient
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
impose that the first normal symbol be \(h(B,-A)\), with \(h\in H^0(O(8))\). Exact linear algebra in the 35 quartic monomials gives, away from the exceptional comparison-zero direction below,
\[
h^0(I_{C_2}(4))=7.
\]
This agrees with the intrinsic decomposition
\[
6=\dim K_R,\qquad 7=6+\dim\langle Q^2\rangle.
\]

For a lift \(F\) with symbol \(h(B,-A)\), its restriction to the canonical primitive triple is the quadratic Taylor coefficient
\[
[F(A\epsilon,B\epsilon)]_{\epsilon^2}-h\gamma,
\]
where \(\gamma\) is the nonnegative-chart correction obtained from the BF quadratic cocycle.

#### K.2 Main one-dimensional triple component: no jet-rank defect

Parameterize the main component projectively by
\[
a_0=1,\qquad a_1=t,\qquad b_0=-2t,\qquad b_1=-8t^2.
\]
The resultant is
\[
\Delta=-6t^2,
\]
so every admissible point has \(t\ne0\).

The full second-order contact matrix has rank exactly five for every \(t\ne0\). A single covering \(5\times5\) minor is
\[
\boxed{-589824\,t^{16}},
\]
so there is no specialization gap on the component.

Therefore
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
at every point of the main e=1 primitive-triple family.

Equivalently, after quotienting the universal \(Q^2\) source direction against \(r^2\), the finite map
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
has maximal rank four. Thus
\[
\boxed{\delta_2^Q=0}
\]
uniformly on the main component.

**PROVED.** The e=2 carrier mechanism does not recur here: BF splitting imposes a special one-dimensional family of quotients, but it does not force a second ambient jet-rank defect.

#### K.3 Two nonzero-comparison isolated directions

At the two isolated directions
\[
a_0=b_1=0,\qquad
3(b_0/a_1)^2+4(b_0/a_1)+12=0,
\]
the quartic-through-double source has dimension seven and the full contact map again has rank five. Hence
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
there as well.

So every e=1 primitive triple with nonzero quadric-comparison section has exactly the expected two-dimensional quartic carrier space.

#### K.4 The comparison-zero point is qualitatively different

At the remaining isolated direction, scale to
\[
A=z,\qquad B=-2.
\]
Then
\[
A+\frac z2B=0.
\]
Hence the primitive conormal kernel \(M=O(-8)\) is exactly the quadric conormal subline
\[
O_C(-8)\subset N_C^*.
\]

The first-symbol source jumps:
\[
\boxed{h^0(I_{C_2}(4))=10}.
\]
The BF quadratic cocycle vanishes identically, so the canonical triple has no quadratic gluing correction in the fixed charts. Moreover the quadric equation has chart expression
\[
Q=u+\frac z2v,
\]
and under the triple parameterization
\[
u=z\epsilon,\qquad v=-2\epsilon
\]
it vanishes identically.

Therefore the canonical primitive triple is contained in the smooth quadric:
\[
\boxed{C_3\subset Q}.
\]

Consequently
\[
Q\cdot H^0(O_{\mathbf P^3}(2))
\subseteq H^0(I_{C_3}(4)).
\]
Both sides have dimension ten, so
\[
\boxed{
H^0(I_{C_3}(4))
=
Q\cdot H^0(O_{\mathbf P^3}(2)).
}
\]

**PROVED.** This exceptional e=1 triple has maximal carrier freedom only because the entire triple lies on the quadric; every quartic carrier factors by \(Q\).

For an STCI presentation with a quartic equation, this is immediately dangerous in exactly the same elementary projective sense as the e=2 cubic-times-linear factorization: a defining quartic \(QH_2\) carries the entire surface component \(Q=0\), and intersection with any positive-degree mate contains a curve on \(Q\), not merely the nonplanar quartic support. Thus this direction cannot supply a genuine quartic equation in an STCI pair supported exactly on \(C_0\).

#### K.5 Structural conclusion for e=1

The primitive e=1 locus exhibits two distinct mechanisms:

1. **nonzero comparison section:** BF splitting is exceptional, but ambient quartic contact is maximal rank and leaves exactly a two-dimensional quartic kernel;
2. **zero comparison section:** the primitive structure aligns with the quadric itself, the source jumps to dimension ten, and every quartic factors through \(Q\).

This strengthens the negative conclusion from the jet-budget framework. Rank defect is not the general source of carrier survival. For e=1, the generic primitive-triple survivor locus has **zero** ambient discrepancy:
\[
\delta_2^Q=0.
\]
The remaining two quartics must therefore be understood geometrically rather than eliminated by dimension count.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_quartic\_contact.py}.
\]

### L. Residual geometry as a separate question

On the nonzero-comparison e=1 triple locus the exact two-dimensional
quartic pencil above need not have a jet-rank defect. Whether its residual
geometry is a fixed factor, a fixed residual curve, a larger base locus,
or a genuine pencil is a question about the actual equations, separate
from the primitive extension and first two contact ranks. The
[complete e=1 rebuild](https://github.com/markluxton1/STCI/blob/c68a8cb1f3ade682172bce338abd632f79cf0881/research/supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-e1-jet-rebuild)
repairs the invalid fixed-ruling-line shortcut. The all-quartic mate
problem is already closed by the [full carrier proof](quartic_carrier_proof.md);
these structural questions do not reopen that theorem.

---

<a id="2026-10-06-primitive-quadruple-universal"></a>

## Universal degree-two primitive fourth structures

Status: exact universal classification and carrier theorem, verified over
characteristic zero. The result excludes the degree-two direction branches
of hypothetical `(4,7)` and `(4,8)` complete intersections on the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`. It does not settle STCI for `C0`, other rational
quartics, arbitrary curves, or positive characteristic.

The computation corrects the plausible universal exclusion suggested by
the samples in `2026-10-05-uniform-multiplicity.md`: primitive quadruples of
conormal quotient type `O(-5)` **do exist**. Their quotient directions form
a resultant-open subset of a linear projective three-space. The obstruction
to the indicated complete intersections is instead that every ambient
quartic containing their canonical primitive triple factors as a cubic
times a linear form.

### Formal coordinates and complete parameter coverage

Use the first ambient chart

\[
z=x_1/x_0,\quad v=x_2/x_0-z^3,\quad
u=x_3/x_0-z^4-\tfrac32zv.
\]

The opposite moving coordinate is

\[
W=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]

and its split normal coordinates are

\[
u'=\tfrac12\left(\frac z{z^4+u+\tfrac32zv}-W^3\right),\quad
v'=-\frac{3zW}{z^4+u+\tfrac32zv}+W^4+
\frac2{z^4+u+\tfrac32zv}.
\]

To first order both normal coordinates transition by `z^-7`. Specify
the quotient `O(-7)^2 -> L=O(-5)` by

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2,
\quad u\mapsto A\ell,\quad v\mapsto B\ell.
\]

These are homogeneous binary quadratics, even when an affine leading
coefficient vanishes. Their projective resultant is

\[
\Delta=a_0^2b_2^2-a_0a_1b_1b_2-2a_0a_2b_0b_2+
a_0a_2b_1^2+a_1^2b_0b_2-a_1a_2b_0b_1+a_2^2b_0^2.
\]

The sole parameter restriction is `Delta != 0`. The matrix sending
degree-at-most-one Bezout coefficients `(S0,S1,T0,T1)` to the coefficients
of `(S0+S1 z)A+(T0+T1 z)B` is

\[
\begin{pmatrix}
a_0&0&b_0&0\\a_1&a_0&b_1&b_0\\
a_2&a_1&b_2&b_1\\0&a_2&0&b_2
\end{pmatrix}.
\]

Its determinant is `Delta`, including affine degree drops. Thus the
Bezout gauges exist uniquely over the entire resultant-open set; no
additional leading-coefficient charts, generic-pencil normalization, or
unexamined boundary directions enter the computation. Reversing the
coefficient vectors gives the opposite-chart gauges, with the same
determinant. We do not use arbitrary changes of the split frame or base
coordinate to normalize quotient directions: those would require changing
the full nonlinear transition.

Set `m=Bu-Av`, whose line type is `M=O(-9)`. Then

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6).
\]

Because both cohomology groups of `O(-1)` vanish, each direction has a
unique embedded primitive triple. A zero fourth obstruction also produces
a unique primitive quadruple, since `H0(O(-6))=0`.

### Exact fourth obstruction and its entire zero locus

For `d=A'B-AB'`, the quadratic cocycle is

\[
h_2=-\frac{2A+zB}{8z^5}\left(12A^2+3z^2B^2+4z^2d\right).
\]

Write `gammaU` for its nonnegative Laurent part and put
`gammaV=(-z*(h2-gammaU))|_(z=1/w)`. The canonical triple has
`m+gammaU ell^2=0` on the first chart and
`m'+gammaV(W) ell'^2=0` on the second. Polynomial Bezout coefficients
`SA+TB=1` give its first-chart parameterization

\[
u=A\ell-T\gamma_U\ell^2,\qquad
v=B\ell+S\gamma_U\ell^2.
\]

All coefficient functions in the opposite equation are evaluated at the
moving coordinate `W` **before truncating**. The cubic coefficient of that
equation, multiplied by `z^9`, gives a Laurent cocycle `h3`; its
coefficients of `z^-1,...,z^-5` represent `H1(O(-6))`.

The universal exact result is

\[
(c_1,\ldots,c_5)=(G_1,\ldots,G_5)/\Delta,
\]

where each `Gi` is a homogeneous degree-eight polynomial. Their complete
expanded values are generated by `research/computations/primitive47universal/generate.py`
in `equations.json`. If `I=(G1,...,G5)` and `K=(2a1+b0,2a2+b1)`,
the verified exact certificates are

\[
I\subseteq K,\qquad
\Delta^3(2a_1+b_0)^3\in I,\qquad
\Delta^3(2a_2+b_1)^3\in I.
\]

Consequently, on `Delta != 0`, all five coordinates vanish **if and only if**

\[
\boxed{b_0=-2a_1,\qquad b_1=-2a_2.}
\]

This is a set-theoretic classification; the powers in the membership
certificates are not a claim that the obstruction scheme is reduced.
Its projectivized parameter space is an open subset of a linear `P3`.
The restricted resultant is

\[
\Delta_0=a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, `(a0,b2)` cannot both vanish. Equivalently, the fourth-zero
directions satisfy

\[
2A+zB=q_0=2a_0+b_2z^3.
\]

For example `A=z^2+1, B=-2z` has
`h2=-4/z-8/z^3-3/z^5`, `gammaU=0`,
`gammaV=4+8w^2+3w^4`, and all five fourth coordinates zero. The prior
nonzero sampled direction `A=z^2,B=1` lies outside this locus.

### Every quartic carrier is a cubic multiple, on all charts

Use ambient coordinates `[x:y:Z:W]`, and define

\[
Q=xW-yZ,
\]

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
+a_0^2(x^2Z-y^3)+a_0b_2(xZ^2-y^2W)
-\frac{b_2^2}{4}(yW^2-Z^3).
}
\]

This cubic is in the ideal of `C0`; its first normal symbol is
`-q0(B,-A)/2`. It contains the canonical primitive triple and quadruple.
The universal verifier checks the latter directly through third order in
`ell`, using the unique gluing correction for the quadruple.

The first-symbol image of ambient quartics in `I(C0)` has dimension 17,
with kernel `kQ^2`; its three missing linear combinations are
`Qnormal_2=P_1/2`, `Qnormal_5=P_4/2`, `Qnormal_8=P_7/2`.
For direction `(B,-A)` on the fourth-zero locus, an admissible symbol is
`h(B,-A)`, with

\[
h\in\langle1,z,z^3,z^4,z^6,z^7\rangle.
\]

Thus its quartic lift has seven coefficients, the six coefficients of
`h` and the coefficient `k` of `Q^2`. Restricting these lifts to the
canonical triple gives the following seven-by-seven matrix, with columns
ordered `(h0,h1,h3,h4,h6,h7,k)` and rows ordered by the coefficient of
`z^0,...,z^6` in the quadratic normal jet:

\[
\begin{pmatrix}
a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&0&0&0&a_0^2\\
-a_0b_2^2/4&0&a_0^2b_2/2&0&-a_0^3&0&0\\
0&a_0b_2^2/4&0&-a_0^2b_2/2&0&a_0^3&0\\
a_2b_2^2/2&-a_1b_2^2/2&-a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&2a_0^2a_1&a_0b_2\\
-b_2^3/8&0&a_0b_2^2/4&0&-a_0^2b_2/2&0&0\\
0&b_2^3/8&0&-a_0b_2^2/4&0&a_0^2b_2/2&0\\
0&0&0&-a_1b_2^2/2&-a_0a_2b_2&a_0a_1b_2&b_2^2/4
\end{pmatrix}.
\]

Its minor in zero-based rows `(0,1,2)` and columns `(4,5,6)` is
`-a0^8`; that in rows `(4,5,6)` and columns `(0,1,6)` is
`-b2^8/256`. Because `Delta0 != 0` implies `(a0,b2) != (0,0)`, these
two minors cover every admissible direction and prove rank at least three.
The four independent quartics `xT,yT,ZT,WT` lie in the kernel. The cubic
is never zero: its `y^3` coefficient is `-a0^2`, and its `Z^3`
coefficient is `b2^2/4`. Hence these multiples are linearly independent,
proving rank exactly three on the full resultant-open locus.

For the primitive triple `Y3` and quadruple `Y4`, this proves

\[
\boxed{
H^0(\mathcal I_{Y_3}(4))=
H^0(\mathcal I_{Y_4}(4))=
T\,H^0(O_{\mathbf P^3}(1)).
}
\]

An equivalent compact solution of the matrix is

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4),\qquad
k=2a_1b_2c_1+4a_0a_2c_3.
\]

The coincidence between the fourth-zero locus and the rank-two exceptional
quartic first-symbol direction locus is independently obtained in the
local-cohomology direction investigation. It explains why a generic
first-symbol rank count would miss this family.

### Consequence for hypothetical complete intersections

For a quasiprimitive complete intersection `(4,b)` supported on `C0`,
the checked filtration duality in `2026-10-05-uniform-multiplicity.md`
gives, when `L=O(-5)`, top defect degree `b-7`. At `b=7` the entire
structure is primitive. At `b=8`, superadditivity and complementary
divisor duality force `D2=D3=0`, so its canonical fourth structure is
primitive. Thus either branch requires a direction in the classified
fourth-zero locus and its defining quartic must contain `Y3`.

The carrier theorem forces `F4=T*H` with `H` a nonzero linear form.
For any homogeneous mate `Gb` of positive degree, `V(H,Gb)` is a
projective plane curve or the whole plane. It is contained in
`V(F4,Gb)`, and it cannot be contained in the nonplanar integral curve
`C0`. Therefore `V(F4,Gb)` cannot have support exactly `C0`.

This excludes the **e=2 branches** of `(4,7)` and `(4,8)` on `C0`.
The same argument excludes any `(4,b)` whose e=2 canonical quadruple is
primitive. It does not exclude e=0 or e=1 at these degrees, nor e=2
structures with a defect before the fourth layer, nor carriers of higher
degrees. The cubic `T` can be singular at the zeros of `q0`; its existence
does not furnish a smooth supporting surface or an STCI construction.

### Reproduction and continuation evidence

One repository-local command verifies the full calculation, including
exact ideal membership and all-chart rank minors:

The archived command uses [verify_primitive_quadruple_universal.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/verify_primitive_quadruple_universal.py) from the pinned repository snapshot.

```sh
python research/computations/verify_primitive_quadruple_universal.py
```

It requires SymPy and Macaulay2's `M2`; the recorded verification used Macaulay2 1.26.06. It regenerates its
inspectable scratch equations, derives all jets with sparse polynomial
arithmetic, checks ten directions against the original independent
rational-series implementation, verifies the universal cubic restrictions,
and runs exact Macaulay2 certificates. The ten sample comparisons are
cross-checks; the global conclusions come from the polynomial identities,
resultant-localized membership certificates, and covering minors.

The verifier uses `scratch/primitive47universal/generate.py` to generate
`equations.json` and `classify.m2`, and `quartic_contact.py` to generate
`quartic_contact.m2` and `quartic_contact.json`. A replay from absent
generated files reproduced all four files byte for byte and passed the
exact Macaulay2 certificates. The separate independent quartic-contact
audit uses the retained `quartic_contact.json` as its literal input.
The independent theoretical reconstruction is in
`2026-10-05-primitive-carrier-theory.md`; the frontier-audit lane is
checking the quadratic cocycle and contact matrix by a separate
Bezout-independent computation.

A tempting fifth-order exclusion also fails for the sample
`A=z^2+1,B=-2z`: its fifth obstruction is zero, as recorded with exact
Laurent coefficients in the theory note. The productive next question is
therefore the uniform ambient compatibility of an e=2 primitive triple,
and then the remaining case `deg D2=1`; increasing sampled primitive
orders does not address the ambient quartic factor obstruction.


---

<a id="2026-10-06-primitive-triple-parity"></a>

## A parity slice and its fourth-layer defect obstruction

Status: exact characteristic-zero classification of the entire parity
slice; necessary extension argument checked conceptually by the frontier
audit lane. The statement concerns the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, a hypothetical complete intersection with a
quartic carrier, degree-two first quotient, and **D2=0**. The conclusion is
an all-mate-degree exclusion for this parity slice. It does not exclude
arbitrary degree-two directions or the case `deg D2=1`.

### Exhaustive one-parameter family

Consider the basepoint-free quotient direction

\[
A=a_0+a_2z^2,\qquad B=b_1z.
\]

Projective coprimality forces `a0*a2*b1 != 0`. The actual ambient
automorphism

\[
[x_0:x_1:x_2:x_3]\longmapsto
[x_0:c x_1:c^3x_2:c^4x_3]
\]

preserves `C0` and sends the exact split coordinates `(z,u,v)` to
`(cz,c^4u,c^3v)`. Choose `c^2=a2/a0` and rescale the quotient. This
gives the complete normal form

\[
\boxed{A=1+z^2,\qquad B=\beta z,\qquad \beta\ne0,}
\]

where `beta=b1/a2`. This normalization uses an embedded automorphism and
transports the full jets; it is not an arbitrary normal-frame or pencil
change. Its homogeneous resultant is `beta^2`.

### Exact quartic compatibility of the canonical primitive triple

Because `Hom(M,L^2)=O(-1)`, every degree-two direction has its unique
primitive triple `Y3`. A quartic containing `Y3` must have first symbol
`h(B,-A)`, with `h` a binary form of degree seven, and may have the extra
`Q^2` coefficient, where `Q=x0*x3-x1*x2`. These nine coefficients obey
three ambient first-symbol image constraints and seven actual quadratic
contact equations.

The universal derivation in
`scratch/primitive47universal/general_triple_contact.py` reconstructs the
symbol image from all 35 quartic monomials, chooses a constant rational
right inverse to its 34-dimensional combined restriction/symbol image,
and computes the contact coefficient

\[
f_2-h\gamma_U,
\]

where `f2` is the ordinary quadratic Taylor coefficient and `gammaU`
is the nonnegative Laurent part of the canonical triple cocycle. This
formula does not require a Bezout choice. Three higher polynomial
coefficients are exact multiples of one first-symbol constraint, so the
ten equations are exhaustive.

On the displayed parity family, the resulting matrix is ten by nine.
The exact greatest common divisor of its ten maximal minors, normalized
to be monic, is

\[
\boxed{(\beta-6)(\beta+2)^9(\beta+6)^2.}
\]

Thus the triple has an ambient quartic carrier **if and only if**

\[
\boxed{\beta=-2,\quad -6,\quad\text{or }6.}
\]

At `beta=-2` the matrix rank is five, and the four-dimensional carrier
space is cubic times linear forms, exactly as proved in
`2026-10-06-primitive-quadruple-universal.md`. At `beta=+-6` the rank is
eight and the carrier is unique up to scalar. In ambient coordinates
`[x:y:Z:W]`, convenient forms are

\[
F_+=6xWy^2-x^2yZ-4x^2Z^2+y^4-2y^3Z,
\]

\[
F_-=8xW^3+6xWyZ+12xWZ^2+x^2Z^2-y^3Z
       -6y^2Z^2-12yZ^3-8Z^4.
\]

The normalizations in the exact coefficient certificate are `F+` and
`-F-/6`, respectively. No claim of geometric irreducibility is needed.
A separate Jacobian check found affine singular-ideal dimension two and
degree three for each; these are not covered by an isolated-singularity
normal-quartic argument.

### A necessary condition for introducing the fourth-layer defect

Let `Y3` be the primitive triple associated to a degree-two quotient, and
put `L=O(-5)` and `M=O(-9)`. Its ideal is locally generated by

\[
f=m+\gamma\ell^2,\qquad \ell^3.
\]

Consequently the rank-two bundle

\[
\mathcal V=\mathcal I_{Y_3}/
                 (\mathcal I_C\mathcal I_{Y_3})
\]

fits in an exact sequence

\[
0\longrightarrow L^3\longrightarrow\mathcal V
\longrightarrow M\longrightarrow0.
\]

Its extension class is the ordinary primitive-fourth obstruction
`h3 in H1(Hom(M,L^3))=H1(O(-6))`: the off-diagonal term of the transition
between the two ideal generators is precisely the cubic moving-coordinate
coefficient used in the universal fourth verifier.

Suppose a saturated quasiprimitive fourth layer `Y4` extends `Y3`, with

\[
E_3=\mathcal I_{Y_3}/\mathcal I_{Y_4}=L^3(D_3).
\]

The support ideal `I_C` annihilates `E3`: it does so generically, and
`E3` is torsion free on `C`. Hence the quotient map gives
`V -> E3`. Its restriction to `L^3` is the canonical multiplication
section with zero divisor `D3`. Applying `Hom(-,E3)` to the exact sequence
above shows the necessary condition

\[
\boxed{
h_3\longmapsto0\quad\text{in}\quad
H^1(O(-6+D_3)).
}
\]

This is a necessary condition, not a sufficiency or classification claim
for defective extensions. Equivalently, some nonzero binary form of degree
`deg D3` must annihilate the class under multiplication. Higher terms
`ell*f` and `ell^4` cannot alter this condition, because their images in
`E3` vanish.

For a quartic-carrier complete intersection with degree-two first quotient,
the checked all-degree filtration calculation in
`2026-10-05-uniform-multiplicity.md` gives, with `s=mate_degree-1`,

\[
\deg D_s=s-6.
\]

Write `s=3q+r`, `0<=r<=2`. Superadditivity implies
`q deg D3 <= 3q+r-6 < 3q`, and hence

\[
\boxed{\deg D_3\le2.}
\]

This bound uses the complete-intersection adjunction and divisor duality;
it is not a bound for arbitrary standalone multiple curves.

### The two remaining parity carriers cannot support the bounded defect

The exact fourth-obstruction coordinates, ordered by
`z^-1,...,z^-5`, are

\[
c_+=( -128,0,160,0,-192),\qquad
c_-=(64,0,-8,0,0).
\]

Multiplication by an arbitrary binary quadratic has, in these coordinates,
the matrix

\[
H(c)=\begin{pmatrix}
c_1&c_2&c_3\\c_2&c_3&c_4\\c_3&c_4&c_5
\end{pmatrix}
:H^0(O(2))\longrightarrow H^1(O(-4)).
\]

This follows directly by multiplying a Laurent representative by
`sigma0+sigma1*z+sigma2*z^2` and keeping the three surviving terms
`z^-1,z^-2,z^-3`. The determinants are

\[
\det H(c_+)=-163840,\qquad \det H(c_-)=512.
\]

Thus neither class has a nonzero quadratic annihilator. A degree-zero or
degree-one annihilator would produce a quadratic annihilator by further
multiplication, so these are excluded as well. Neither unique quartic
triple carrier can be part of a hypothetical complete intersection with
`deg D3<=2`. The `beta=-2` carrier has already been excluded by its linear
factor. Every other parameter admits no quartic containing its primitive
triple. Therefore the entire basepoint-free parity family with `D2=0`
is excluded for **every mate degree**.

### Reproduction and remaining open computation

The exact companion is

The archived command uses [verify_primitive_triple_parity.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/verify_primitive_triple_parity.py) from the pinned repository snapshot.

```sh
python research/computations/verify_primitive_triple_parity.py
```

It regenerates the arbitrary-direction quartic contact matrix, uses
polynomial-domain determinants over `QQ[beta]` for all ten maximal minors,
checks their gcd and the three exceptional ranks, reconstructs the two
unique quartics, checks their classes against the original rational-series
fourth-obstruction implementation, and verifies both Hankel determinants.
The replay regenerated `parity_triple_certificate.json` and the full
all-direction matrix `general_triple_contact.json` byte for byte.

The [six-parameter Macaulay2 saturation](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/scratch/primitive47universal/general_triple_contact.m2)
was stopped, as were the [normalized-chart attempt](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/scratch/primitive47universal/triple_contact_p_chart.m2)
and a finite-field version. The
[one-chart Dynamic determinant calculation](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/scratch/primitive47universal/triple_contact_p_factors.m2)
completed with large expanded minors. The saturated rank-drop ideal in
this approach remains uncomputed.

The strongest continuation target is the arbitrary-direction rank-drop
locus of the ten-by-nine matrix, followed by the quadratic-annihilator
incidence condition for its fourth obstruction. The separate case
`deg D2=1` needs a defective-triple gluing state; a primitive-triple
calculation cannot silently be applied to it.


---



## Consolidated historical supplement: `research/supplements/NORMAL_PRIMITIVE_CARRIERS_AND_BOUNDS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Normal singularities, primitive cubic carriers, and ancestor charts

The normal-surface arguments below retain their broader smooth rational
quartic scope, including an independent weighted simple-elliptic proof.
The primitive calculations use the fixed C0 and provide explicit cubic
carriers, higher-extension controls and exact ancestor chart equations.
These are distinct statements: the completed [fixed-C0 all-quartic proof](quartic_carrier_proof.md)
does not make the broader normal-curve arguments or ancestor equations
redundant.

---

## Numerical self-intersection and the normal line

The full proof, ordinary-node correction, unbounded Cartier-index control,
and conditional split-sextic application now have one mathematical home:
[numerical pullback and the normal line](numerical_surface_pullback.md).
The inequality for an integral surface regular generically along the smooth
curve was independently reconstructed in this consolidation. Its special
split-sextic numerical antecedents remain conditional.

---

<a id="2026-10-05-normal-quartic-carriers"></a>

## Normal singularities and smooth rational quartics

Work with normal quartic surfaces in characteristic zero. The classical
rational-singularity exclusion, the passage-through-nonrational-points
reduction, and the smooth elliptic exceptional-curve exclusion below
are proved for the displayed smooth rational quartic scope. They do
not treat nonnormal quartics or higher minimum carrier degree.

Let `C` be a smooth nondegenerate rational quartic, in particular
`C0=[s^4:s^3t:st^3:t^4]`. Suppose an integral normal quartic `S` and a
surface `T` meet set-theoretically in `C`. There is no restriction on `deg T`
or on common singular points.

### 1. Jaffe's rational-singularity theorem

David B. Jaffe, [Applications of iterated curve blowup to set theoretic
complete intersections in P^3](https://arxiv.org/pdf/alg-geom/9410008),
Theorem 11.11, printed p.45 (PDF page index 44), proves that a smooth
set-theoretic intersection on a quartic surface with only rational
singularities is linearly normal. The introduction, printed p.2,
explicitly allows an arbitrary second surface and common singular points.

The hypothesis is substantially different from Jaffe's
no-common-singular-point theorems. It must not be omitted when listing the
known quartic-carrier frontier. Since `h^0(C,O_C(1))=5` whereas ambient
linear forms have dimension four, every smooth rational quartic violates
the conclusion. Thus **a normal quartic carrier with only rational
singularities is excluded for every mate degree**.

A normal hypersurface surface with rational singularities is Gorenstein,
so these singularities are rational double points. The theorem therefore
already covers every normal ADE quartic. A new lattice scan of that class
would reproduce a classical exclusion, rather than advance the frontier.

Jaffe states the theorem over the complex numbers. All assertions in this
note extend to an arbitrary algebraically closed characteristic-zero field
by finitely generated coefficient-field transfer. For precision, descend
the equations of the hypothetical pair, a parametrization of the smooth
rational quartic, and a resolution together with its exceptional divisors
to a sufficiently large finitely generated field `k0` of characteristic
zero. Geometric normality and smoothness can be retained after increasing
`k0`. The two ideal containments expressing radical equality have finite
polynomial witnesses: powers of generators of `I_C` belong to `(F,G)`, and
`F,G` belong to `I_C`. Include those witnesses in `k0` as well. Embed `k0`
in the complex numbers and base change. This preserves the set-theoretic
intersection, the resolution, intersection numbers, exceptional curve
genera, and the rational/simple-elliptic hypotheses being used. The
complex result then supplies the contradiction. Thus no uncountability
assumption on the original field is needed.

### 2. The complete normal quartic classification narrows the survivors

Yuji Ishii and Noboru Nakayama,
[Classification of normal quartic surfaces with irrational singularities,
J. Math. Soc. Japan 56 (2004), 941–965](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf),
give constructions of all such surfaces. The
[author-hosted preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf)
is particularly convenient for its readable extraction and page numbering.
The published Main Theorem, p.955, confirms that the constructions are
exhaustive, so the argument below does not infer a classification from
examples alone. Its introduction lists four possibilities for the resolution:
K3, a bundle over a smooth plane quartic (the cone case), an elliptic ruled
surface, or a rational surface.

For the non-K3 cases, write `sigma:M→S`, `H=sigma^*O_S(1)` and
`K_M=-E`, where `E` is a nonzero effective exceptional anticanonical
divisor. Their condition C includes `H∩E=empty`. Their exhaustive
construction shows:

- Cone case: `M` is a bundle over a curve of genus three and `H` has degree
  one on its ruling fibers.
- Elliptic ruled case (Type C): the general ruling fiber has `H`-degree two
  or three. See preprint §3.3, printed pp.30–34, together with §2.3.
- Rational case: Picard number is 12 for Type B1, 11 for B2 and B3, and
  13 for Type D. See preprint printed pp.14, 17, 19 and 23.

Any rational curve on a surface ruled over a positive-genus curve maps
constantly to the base. Its strict transform is therefore an irreducible
component of a fiber. Because `H` is nef, its `H`-degree is at most the
degree of the whole fiber, which is at most three in these cases.
Consequently **the cone and elliptic ruled normal quartics cannot even
contain a rational curve of degree four**. This statement uses the
classification and elementary intersection theory, independently of a
mate.

It follows that a surviving normal quartic STCI carrier has rational
minimal resolution, contains a nonrational singularity, and has
`rho(M)≤13`.

### 3. Passage through a nonrational singularity

Suppose, for contradiction, that `C` avoids every nonrational singularity
of such a rational normal quartic. Let `c` be its strict transform in `M`.
It is again a smooth rational curve: the blowup centers restrict to
invertible ideals on the smooth support, and the strict-transform map is
an isomorphism. Since `E` lies over the nonrational singularities,
`c.E=0`. Adjunction gives `c^2=-2`.

The divisor of the mate on `S` is `bC`, where `b=deg T`, because both
`S` and `C` have degree four. Thus `bC~bH` on `S`. Its numerical pullback
to `M` gives

`c+Z ≡ H`,

where `Z` is the effective rational exceptional correction. It is supported
only at rational double points on `C`. Orthogonality to each exceptional
curve gives `c.Z=-Z^2`; hence

`Delta := -Z^2 = H^2-c^2 = 4-(-2)=6`.

Let `N` be the total ADE root rank at these points. Jaffe's classification
of smooth curve–rational double point pairs (Theorem 4.1 and Proposition
5.7, printed pp.15 and 23) gives the following local contributions:

| Pair | Root rank | Contribution to Delta |
|---|---:|---:|
| `A_n^k`, `1≤k≤(n+1)/2` | `n` | `k(n+1-k)/(n+1)` |
| `D_n^1` | `n` | `1` |
| `D_n^n` | `n` | `n/4` |
| `E_6^1` | `6` | `4/3` |
| `E_7^1` | `7` | `3/2` |

Every contribution is at most half its root rank. For the `A_n` row,
the quadratic's maximum is `(n+1)/4≤n/2`; the other rows are immediate.
Therefore `Delta≤N/2`.

The ADE exceptional curves above points on `C` are linearly independent
by their negative definite intersection matrix. At least one further
exceptional dimension is supplied by the nonzero anticanonical divisor
`E`, whose support lies above distinct points and whose square is negative.
All these classes are orthogonal to `H`, and `H^2=4`. Thus

`N+1≤rho(M)-1≤12`, so `N≤11`.

We obtain `6=Delta≤11/2`, a contradiction.

**Conclusion.** A normal quartic surface occurring in a characteristic-zero
STCI presentation of a smooth rational quartic must have rational minimal
resolution and the quartic curve must pass through a nonrational
singularity. Normality alone is not an exclusion. No assertion is made
that every quartic carrier is normal, or that the remaining nonrational
points are ADE.

### 4. A smooth elliptic exceptional curve

Assume the anticanonical exceptional divisor `E` is a single smooth,
reduced elliptic curve. This hypothesis specifies the surviving
nonrational singularity as a **simple elliptic singularity**; all other
singularities are rational double points. This section proves that no
normal quartic with this property can be an STCI carrier for a smooth
rational quartic, for any mate degree.

By §3 the curve passes through the simple elliptic point. Put
`d=-E^2`. The exhaustive rational-resolution classification gives

| `d` | Possible rational type | `rho(M)` | ADE rank upper bound `N` |
|---:|---|---:|---:|
| 1 | B2 or B3 | 11 | 9 |
| 2 | B1 | 12 | 10 |
| 3 | D | 13 | 11 |

The rank bound follows from the independence of `H`, `E`, and the ADE
exceptional curves, just as in §3. For a smooth elliptic `E`, its fiber is
the full exceptional locus of the simple elliptic singularity: a further
minimal exceptional curve of discrepancy zero attached to `E` would have
`K_M.R=-E.R<0`, contradicting minimality. Other connected exceptional
fibers are disjoint ADE configurations.

#### Local passage and first-normal orders from a checked classification

Guangfeng Jiang and Dirk Siersma,
[Local embeddings of lines in singular hypersurfaces, Ann. Inst. Fourier
49 (1999), 1129–1147](https://www.numdam.org/item/10.5802/aif.1711.pdf),
§3.7, Theorem and Table 3 on p.1141, classify every smooth
curve–simple elliptic hypersurface pair. Here their local “line” means a
smooth curve germ, straightened to the `x`-axis by an analytic coordinate
change (§1.1). Their invariant `lambda` is the length of the Jacobian
restricted to that axis (§2.3–2.4). Since the tangential derivative
vanishes on the support, it is exactly the common vanishing order `s` of
the two first-normal coefficients.

The following entries of Table 3 were checked visually against the PDF;
the omitted coefficient restrictions are its nondegeneracy conditions.

| Type | Pair normal form, support `y=z=0` | weights `(x,y,z)` | `s` |
|---|---|---|---:|
| `tilde E6` | `x^2 y+a0 x z^2+a1 y^3+a2 y^2 z+a3 y z^2+a4 z^3` | `(1,1,1)` | 2 |
| `tilde E7` | `x^2 z+x^3 y+b x^2 y^2+c x y^3+d0 y^4+z^2` | `(1,1,2)` | 2 |
| `tilde E7` | `x y (x-y)(x-nu y)+z^2`, `nu≠0,1` | `(1,1,2)` | 3 |
| `tilde E8` | `x^3 z+gamma x^2 y^2+delta x^4 y+y^3+z^2` | `(1,2,3)` | 3 |
| `tilde E8` | `alpha x^4 y+x^2 y^2+y^3+z^2`, `alpha≠0,1/4` | `(1,2,3)` | 4 |

The weight of the support parameter `x` is one in every row. In the
weighted `x`-chart put `y=x^(w_y)Y`, `z=x^(w_z)Z`. Factoring the weighted
degree leaves an equation `P(Y,Z)=0`, while the support is `Y=Z=0` and
the exceptional curve is `x=0`. At `(Y,Z)=(0,0)`, `P_Y` or `P_Z` is
nonzero: the five rows respectively have a linear `Y`, a linear `Z`, a
linear `Y`, a linear `Z`, and a linear `alpha Y`. The surface and its
exceptional elliptic curve are smooth in this chart, and the strict
transform of the support meets it transversely with parameter `x`.

This chart belongs to the simple elliptic resolution. In these weighted
forms the exceptional weighted-projective elliptic curve has degree
`d=3,2,1` respectively, and the normal bundle has degree `-d`. It misses
the ambient weighted-projective quotient points because their pure
`y` or `z` terms do not vanish there. Thus the weighted blowup introduces
no extra exceptional component at the support point. Equivalently, the
unique minimal elliptic exceptional curve meets the support once. We have
proved the local data

`c.E=1`, and `s≥3` if `d=1`, while `s≥2` if `d=2` or `3`.

#### A quartic supplies at most nine first-normal zeros

For a smooth rational quartic in characteristic zero,
`N_C^*=O_P1(-7)^2`. The differential of its quartic carrier gives

`O_P1(-16)→O_P1(-7)^2`.

It is a nonzero pair of binary forms of degree nine. Their greatest
common divisor has degree at most nine, and this degree is the sum of
the local first-normal orders over the singular points of the surface on
`C`. Thus the sum `P` of the ADE first-normal orders satisfies

`P≤6` for `d=1`, and `P≤7` for `d=2,3`.

This bound does not require a regular first-normal quotient between the
two defining surfaces or any bound on the mate degree. It uses only the
normal quartic carrier's differential. In the repository's notation its
degree is `9-e`; the weaker bound at most nine is sufficient here.

#### The exact harmonic ADE bound

For a smooth curve through an ADE point, let `n` be its root rank,
`s` its first-normal order, and `delta` its contribution to the numerical
pullback correction. Jaffe's Propositions 5.2 and 5.7 give

| Pair | `s` | `delta` |
|---|---:|---:|
| `A_n^k` | `k` | `k(n+1-k)/(n+1)` |
| `D_n^1` | 2 | 1 |
| `D_n^n`, `n` even | `n/2` | `n/4` |
| `D_n^n`, `n` odd | `(n-1)/2` | `n/4` |
| `E_6^1` | 2 | `4/3` |
| `E_7^1` | 3 | `3/2` |

Every row satisfies `delta≤n s/(n+s)`. In the `A_n` row, after cancelling
positive factors the inequality is `k(1-k)≤0`. For the spin `D_n` row it
is `n≤3s`, true for the permitted `n`; the remaining three rows are
immediate. Summing and applying Cauchy–Schwarz gives

`sum delta ≤ sum n_i s_i/(n_i+s_i) ≤ N P/(N+P)`,

where `N=sum n_i` and `P=sum s_i`. One proof of the second inequality is
to write the middle sum as `N-sum n_i^2/(n_i+s_i)` and use
`sum n_i^2/(n_i+s_i)≥N^2/(N+P)`. When there are no ADE points the
correction is zero, with no denominator needed.

#### Contradiction

Adjunction now gives `c^2=-1`, because `K_M=-E` and `c.E=1`.
The STCI relation still gives numerical pullback `c+Z≡H`, so the whole
correction is `-Z^2=4-c^2=5`. At the simple elliptic point, orthogonality
forces `Z_ell=E/d`, contributing `1/d`. Hence the ADE correction must
equal `5-1/d`.

The necessary correction exceeds its permitted harmonic upper bound
in every row:

| `d` | Required ADE correction | Upper bound | Exact positive gap |
|---:|---:|---:|---:|
| 1 | 4 | `9·6/(9+6)=18/5` | `2/5` |
| 2 | `9/2` | `10·7/(10+7)=70/17` | `13/34` |
| 3 | `14/3` | `11·7/(11+7)=77/18` | `7/18` |

The function `NP/(N+P)` is increasing in each nonnegative variable,
so using the rank and first-normal upper bounds is legitimate. These
strict inequalities contradict the mate relation. This proves the
claimed uniform simple-elliptic subclass exclusion.

Exact companion verification:
`research/computations/verify_normal_quartic_simple_elliptic.py`, run with `python3`, checks the weighted homogeneity,
axis differential orders and smooth weighted charts of all five local
pair forms, 53 permitted ADE rows of rank at most 11, and the three strict
rational gaps. It returned `PASS`. The retirement replay with SymPy 1.14.0
matched the [historical output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/normal_quartic_simple_elliptic_2026-10-06.json)
on stdout.
The script checks formulas, not the classification theorems or the
geometric deductions; those hypotheses remain explicit in this proof.

### 5. Scope of the normal arguments

The rational-resolution classification allows effective exceptional
anticanonical divisors of square -2,-1,-1,-3 in Types B1,B2,B3,D.
The weighted proof above handles the smooth reduced elliptic case.
Its local pair table and exact first-normal orders are a distinct
proof from the [common fixed-C0 normal-carrier proof](quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing),
which completes the reducible, singular and nonreduced cases for
that fixed embedding. The broader smooth-rational-quartic statements
in Sections1--4 retain exactly their stated hypotheses.

The ADE correction identity Delta=6 is used here only when the curve
avoids the nonrational points, so c.K_M=0. It is invalid when c.E>0;
the later smooth elliptic calculation instead uses its actual
c.E=1, weighted first-normal order and elliptic correction1/d.
Neither equality follows from an ADE tangent type alone.

The surface classification and local analytic pair table above are
characteristic-zero inputs. They do not establish the same cases in
positive characteristic. The exact polynomial identities have their
own reduction scope after denominators and bad-prime rank changes are
checked; this is separate from transporting those classification
hypotheses. In particular, fixed C0 has quartic-carrier mates in
[every positive characteristic](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier).

---

<a id="2026-10-05-primitive-carrier-theory"></a>

## Explicit cubic carriers for the primitive fourth locus

Scope: characteristic zero and the fixed monomial smooth
rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

This note independently reconstructs the geometric meaning of the
degree-two primitive-fourth zero locus and the quartics carrying its
canonical primitive triple. The universal primitive-fourth obstruction
calculation is recorded separately by the primitive-quadruple investigation.
Its vanishing locus, on the open set of coprime binary quadratic pairs, is
the linear locus used below. No primitive multiple curve constructed here
is asserted to be a global complete intersection.

### 1. Frames, obstruction degrees, and the factorization of the quadratic jet

On the first affine chart write

\[
z=t/s,\quad a=x_2/x_0-z^3,\quad b=x_3/x_0-z^4,
\quad u=b-\frac32za,\quad v=a.
\]

The split conormal frame has transition \(u'=z^{-7}u\),
\(v'=z^{-7}v\) to first order. A quotient to \(L=O(-5)\) is specified
by a coprime pair of binary quadratics, written on this chart as

\[
u\longmapsto A(z),\qquad v\longmapsto B(z).
\]

Its kernel is \(M=O(-9)\). Consequently

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6),\qquad
\operatorname{Hom}(M,L^4)=O(-11).
\]

Both cohomology groups of \(O(-1)\) vanish. Thus each quotient has a
unique embedded primitive triple, with no free extension parameter. The
next two obstruction spaces have dimensions five and ten respectively.

Let \(D=A'B-AB'\), where primes denote ordinary differentiation in \(z\).
The moving-coordinate calculation in
`research/computations/primitive47/obstruction.py` gives the following
Bezout-independent expression for its quadratic cocycle:

\[
\boxed{
h_2=-\frac{2A+zB}{8z^5}
       \left(12A^2+3z^2B^2+4z^2D\right).
}
\]

Indeed the first displacement of the opposite affine coordinate is

\[
W_1=-z^{-5}A-\frac12z^{-4}B.
\]

The quadratic ambient jets are

\[
u'_2=-\frac52z^{-11}A^2-3z^{-10}AB-\frac38z^{-9}B^2,
\quad
v'_2=3z^{-12}A^2-z^{-11}AB-\frac94z^{-10}B^2.
\]

Using \(b_V'(1/z)A-a_V'(1/z)B=D\), and multiplying the quadratic
coefficient of \(b_V(W)u'-a_V(W)v'\) by \(z^9\), proves the boxed
formula. In particular, this calculation retains the displacement of the
base coordinate; fixing \(W=1/z\) would omit its final summand.

Write \(\gamma_U\) for the nonnegative Laurent part of \(h_2\). With
\(m=Bu-Av\), the first-chart primitive-triple equation is

\[
m+\gamma_U\ell^2=0\pmod{\ell^3}.
\]

### 2. A distinguished cubic on the fourth-obstruction zero locus

The separately computed universal fourth-obstruction vanishing locus is

\[
A=a_0+a_1z+a_2z^2,\qquad
B=-2a_1-2a_2z+b_2z^2.
\]

Define

\[
q_0(z)=2A+zB=2a_0+b_2z^3.
\]

The homogeneous resultant on this locus is

\[
a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, coprimality implies \((a_0,b_2)\ne(0,0)\), so
\(q_0\) is a nonzero section of \(O(3)\).

Use ambient coordinates \([x:y:Z:W]\), and set

\[
Q=xW-yZ,\quad
R_1=x^2Z-y^3,\quad
R_2=xZ^2-y^2W,\quad
R_3=yW^2-Z^3.
\]

The distinguished cubic is

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
  +a_0^2R_1+a_0b_2R_2-\frac{b_2^2}{4}R_3.
}
\]

It lies in \(I(C_0)_3\), and its first conormal symbol in the split
\((u,v)\) frame is

\[
\sigma_1(T)=-\frac{q_0}{2}(B,-A).
\]

Here is an elementary uniqueness derivation. The cubic first symbols have
the form

\[
P=c_0+c_1z-c_5z^2+c_2z^3+c_3z^4+2c_6z^5,
\]

\[
Q_{
m n}=c_4+\frac12c_0z+\frac12c_1z^2
                 +\frac12c_5z^3+\frac12c_2z^4+\frac12c_3z^5,
\]

so \(Q_{
m n}-zP/2=c_4+c_5z^3-c_6z^6\). A symbol proportional to
\((B,-A)\) therefore has a scalar of degree three proportional to
\(q_0\). Equating coefficients gives the displayed cubic. This also
covers \(a_0=0\) or \(b_2=0\) individually: the other coefficient is
nonzero on the coprime locus. Thus the cubic with this conormal direction
is unique up to scalar.

The boxed quadratic-cocycle formula verifies directly that \(T\) contains
the canonical primitive triple. Substituting \(u=A\ell,v=B\ell\) gives
zero constant and linear coefficients for \(T\); its quadratic
coefficient is \(-q_0\gamma_U/2\). The correction
\(m=-\gamma_U\ell^2\) contributes the opposite coefficient, because
the first symbol of \(T\) is \(-q_0m/2\).

### 3. Every quartic containing this triple is a cubic multiple

The exact quartic-symbol image is independently verified in
`research/computations/verify_localcoh_direction_image.py`:

\[
Q_{{\rm n},2}=P_1/2,\quad
Q_{{\rm n},5}=P_4/2,\quad
Q_{{\rm n},8}=P_7/2,
\]

and the kernel of the symbol map is \(kQ^2\). On the present degree-two
direction locus, a quartic symbol has the form \(h(B,-A)\), where

\[
h=h_0+h_1z+h_3z^3+h_4z^4+h_6z^6+h_7z^7.
\]

Take the universal exact lift of this symbol from that verifier, and add
\(kQ^2\). Let \(f_2\) denote its quadratic coefficient after the straight
substitution \(u=A\ell,v=B\ell\). The actual coefficient on the
canonical triple is \(f_2-h\gamma_U\). This expression is independent
of the polynomial Bezout gauge: the second correction has normal kernel
coordinate exactly \(-\gamma_U\).

Introduce the two linear expressions

\[
E_0=4a_0^2h_6-2a_0b_2h_3+b_2^2h_0,
\qquad
E_1=4a_0^2h_7-2a_0b_2h_4+b_2^2h_1.
\]

The coefficients of \(f_2-h\gamma_U\) at degrees four and one are
\(-b_2E_0/8\) and \(-a_0E_0/4\). The coefficients at degrees five and
two are \(b_2E_1/8\) and \(a_0E_1/4\). Since \((a_0,b_2)\ne(0,0)\),
vanishing requires \(E_0=E_1=0\). These two equations have rank two
on the entire coprime locus and are equivalent to

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4).
\]

With this substitution the only remaining condition is

\[
k=4a_0a_2c_3+2a_1b_2c_1.
\]

For explicit coefficient checking, before that substitution the remaining
coefficients at degrees six, three, and zero are respectively

\[
\frac{b_2}{4}
 (4a_0a_1h_7-4a_0a_2h_6-2a_1b_2h_4+b_2k),
\]

\[
\frac12(4a_0^2a_1h_7-4a_0^2a_2h_6-2a_0a_1b_2h_4
 -2a_0a_2b_2h_3+2a_0b_2k-a_1b_2^2h_1+a_2b_2^2h_0),
\]

\[
-a_0(2a_0a_2h_3-a_0k+a_1b_2h_1-a_2b_2h_0).
\]

It follows that the quartic space has dimension four. The four products
\(xT,yT,ZT,WT\) are linearly independent, contain the triple, and span
it. Therefore

\[
\boxed{
H^0(\mathcal I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).
}
\]

The assertion already holds for the primitive triple; imposing the fourth
layer cannot produce an irreducible quartic carrier. In particular, every
quartic containing a primitive quadruple on this fourth-obstruction zero
locus has the same cubic factor. This supplies a carrier exclusion once
the numerical filtration of a hypothetical complete intersection forces
that primitive triple. It does not exclude multiple structures whose
third layer has nonzero defect.

### 4. A sample fifth obstruction vanishes, with no STCI implication

For \(A=z^2+1,B=-2z\), the first-chart correction coefficients through
degree four are all zero. On the second chart the successive primitive
equation coefficients are

\[
\gamma_V=4+8w^2+3w^4,
\]

\[
\rho_V=-18w-50w^3-39w^5-9w^7,
\]

\[
\tau_V=102w^2+360w^4+\frac{1695}{4}w^6
                   +\frac{405}{2}w^8+\frac{135}{4}w^{10}.
\]

The successive moving-coordinate Laurent cocycles are

\[
h_2=-4z^{-1}-8z^{-3}-3z^{-5},
\]

\[
h_3=18z^{-7}+50z^{-9}+39z^{-11}+9z^{-13},
\]

\[
h_4=-102z^{-13}-360z^{-15}-\frac{1695}{4}z^{-17}
                         -\frac{405}{2}z^{-19}-\frac{135}{4}z^{-21}.
\]

Thus \(h_3\) has no Laurent terms \(z^{-1},\ldots,z^{-5}\), and
\(h_4\) has none of \(z^{-1},\ldots,z^{-10}\). The sample extends to a
primitive quintuple, uniquely at these two extension steps. The displayed
second-chart coefficients are the exact Laurent splittings:
\(\rho_V=-z^6h_3\), \(\tau_V=-z^{11}h_4\), written in \(w=1/z\).
In computing \(h_4\), both \(\gamma_V\) and \(\rho_V\) are evaluated at
the full moving coordinate \(W\) before truncation.

Its distinguished cubic is

\[
T=x^2Z-2y^2Z+2xyW-y^3.
\]

An exact restriction of the full eighteen-dimensional quartic space to
the first-chart embedding \(u=(z^2+1)\ell,v=-2z\ell\), modulo
\(\ell^4\), has rank fourteen and kernel
\(\langle xT,yT,ZT,WT\rangle\). Each of these products restricts
identically to zero in this sample; \(Q^2\) does not contain its triple.

### 5. Scope and pitfalls

The scalar \(q_0\) in the cubic conormal symbol is a section of \(O(3)\),
and it vanishes at points. The cubic is therefore not a surface smooth
along the entire curve. For the sample \(q_0=2\) on the first affine
chart, its homogeneous divisor is three times the point at infinity.
In the chart \(W=1\), the cubic has leading term \(2xy\) at that point,
so it is singular there. The primitive extensions and the cubic factor
are entirely compatible with the existing exclusion of characteristic-zero
STCI presentations on cubic surfaces.

No arbitrary \(\operatorname{GL}_2\) change of the split normal frame,
nor arbitrary base \(\operatorname{PGL}_2\) change, may be used to
normalize the binary quadratic pencil while keeping the nonlinear
transition fixed. Such transformations require transport of the full
embedded jet. The ambient symmetries visibly preserving \(C_0\) include
the torus and the coordinate-reversing involution; these alone do not
identify every coprime quadratic pair.

The fifth-order sample is an exact calculation for one quotient. It
establishes neither a universal fifth-order vanishing statement nor
algebraizability of an infinite formal surface. The universal quartic
carrier identity, in contrast, was derived with symbolic coefficients and
uses only the coprimality-open condition. All conclusions in this note are
stated in characteristic zero; special positive characteristics require
their own coefficient and denominator checks.


---

<a id="2026-10-06-localcoh-e2-incidence-charts"></a>

## Four pure-top charts for degree-two ancestor incidence

**Exact specification; full ancestor locus unresolved.** The completed quartic-mate theorem does not compute this ancestor locus.
The companion `localcoh-e2-incidence-2026-10-06.py` exports actual
two-target equations from the verified tensor. This reduces the 30 free
ancestor coordinates while retaining all allowed degeneration of the cyclic
inverse system at its top-symbol zero.

Use the 32-by-30 top map \(M\), of rank 29, and its three-row annihilator
\(L\). For a primitive homogeneous quadratic normal-dual direction
\(\nu=(p,r)\), the pure cubic top is

\[
c_i(t)=h(t)p(t)^i r(t)^{3-i},\qquad i=0,1,2,3,
\]

in the residue divided-power coordinates, where \(h=h_0+h_1t\) is
nonzero. The three equations \(Lc=0\) express precisely that this top lifts
to the 30-dimensional \(H^0(T_4(-7))\) space. They do not assert that its
annihilator quadruple is primitive at the zero of \(h\).

Select 29 independent columns of \(M\) and 29 independent rows of that
column submatrix. Inverting their rational square matrix gives a fixed
rational right inverse \(R\) on \(\operatorname{im}M\). Thus, on the
three-equation top-image locus, every ancestor is uniquely

\[
\alpha=Rc+\lambda k,
\]

where \(k\) spans the one-dimensional \(T_3(-7)\) kernel. The exporter
retains \(\lambda\) and contracts the entire actual quartic multiplication
tensor with these ancestor coordinates.

Primitivity forces at least one of \(p(0),r(0)\) nonzero. Normalize that
coordinate to one. Scaling the ancestor normalizes either \(h_0=1\) when
\(h_0\ne0\), or \(h=t\) when \(h_0=0\). Hence four charts cover every
primitive degree-two ancestor candidate:

| Direction normalization | Top coefficient |
| --- | --- |
| \(p(0)=1\) | \(h=1+h_1t\) |
| \(r(0)=1\) | \(h=1+h_1t\) |
| \(p(0)=1\) | \(h=t\) |
| \(r(0)=1\) | \(h=t\) |

For each chart the exporter writes the three top-image equations and the
74 multiplication equations for each target. The full two-target systems
have 43 variables on the first two charts and 42 variables on the last two:
five free direction coefficients, one optional coefficient \(h_1\), the
one lower correction, and 36 multiplier coefficients. Depending on zero
equations the stored generator count is smaller than 151. A one-target
version is exported as well.

If a computation returns a nonempty closed locus, primitive degree two
requires the homogeneous resultant \(\operatorname{Res}(p,r)\ne0\).
The exported systems do not discard this open condition or pretend that
all their lower-degree boundary directions are primitive degree two. A
unit ideal for the larger chart would suffice for exclusion; a non-unit
ideal requires inspecting this open locus and retaining the rank conditions
in `2026-10-06-localcoh-incidence.md`.

Two direct Gröbner attempts on the \(p(0)=1\) charts were interrupted
after a bounded run on Oct6 without an ideal result. The equations remain
available for continuation. A second run with multiline input and live
terminal output reached the 145-generator ideal on the \(h=t\) chart;
no full-locus conclusion is obtained merely from its progress.

The separate uniform parity certificate excludes the full primitive family
\((p,r)=(a_0+a_2t^2,b_1t)\), whose top coefficient is necessarily the
constant line. It is a verified sublocus of these general charts, not a
classification of all quadratic directions. All other non-ruling direction
strata remain research obligations.
