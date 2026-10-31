# Thick sextic equation spaces and a balanced-normal obstruction

Unless a characteristic-free extension is explicitly stated, fix C=C0 over an algebraically closed field of characteristic zero.

This owner gives the full 23-dimensional double-sextic space, its residual-ruling quotient and an explicit integral thick carrier. It also preserves a different proof of the thick–thick (6,6) exclusion: a common quadratic normal component must meet the quadric-direction section and force a shared residual ruling. The argument is separate from the universal effective-cycle inequality, which excludes the same pair by a negative exceptional bidegree. An exact first carrier construction and a pair obstruction are distinct mathematical contributions.


## the first thick carriers, in degree six

<a id="p-017"></a>

Let \(q\) define the unique quadric \(Q\), with
\(C\sim(1,3)\).  Reduction modulo \(q\) gives an exact sequence

\[
 0\longrightarrow \mathcal I_C(4)
 \xrightarrow{\cdot q}\mathcal I_C^{(2)}(6)
 \longrightarrow\mathcal O_Q(4,0)\longrightarrow0.
\]

Indeed, the restriction of a double sextic is \(h^2R\), where \(h\) defines
\(C\) on \(Q\) and

\[
 R\in H^0(Q,\mathcal O_Q((6,6)-2(1,3)))
 =H^0(Q,\mathcal O_Q(4,0)).
\]

The kernel consists of \(qH\) with \(H\in I_C(4)\), and
\(H^1(I_C(4))=0\).  Since

\[
 h^0(I_C(4))=h^0(\mathcal O_{\mathbf P^3}(2))
 +h^0(\mathcal O_Q(3,1))=10+8=18,
\]

one obtains

\[
 \boxed{h^0(I_C^{(2)}(6))=23,\qquad
 H^0(I_C^{(2)}(6))/qH^0(I_C(4))\simeq H^0(O_Q(4,0)).}
\]

Every non-\(q\)-divisible member has exact normal order two, because
\(H^0(I_C^{(3)}(6))=kq^3\).  Its quadric section is

\[
 X\cap Q=2C+D_R,
\]

where \(D_R\) is the union, with multiplicities, of the four ruling lines
selected by the binary quartic \(R\).

For \(C_0\), with

\[
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

the five classes

\[
 A^2,\ AB,\ B^2,\ BD,\ D^2
\]

give a complement to \(qH^0(I_C(4))\).  The missing-looking class satisfies

\[
 AD-B^2=-x_1x_2q^2.
\]

The exact verifier proves that \(I_C^{(2)}=I_C^2\) here and constructs

\[
 F_*=A^2+B^2+D^2+q^2(x_0^2+x_1^2+x_2^2+x_3^2)
\]

with reduced Jacobian locus exactly \(C_0\).  This also forces absolute
irreducibility: a nontrivial factorization would put the curve of intersection
of two factors in the singular locus. If their entire intersection were supported on C0, one factor would have degree at most three and would be a lower-degree carrier of C0. A plane cannot contain C0, cubic carriers have no mate, and the unique quadric cannot have a mate by its unequal ruling classes; these [low-degree carrier obstructions](../synthesis/02-two-surfaces.md) exclude that possibility. Thus integral sextics singular along
the whole quartic genuinely exist; the problem is finding a mate, not finding
the first carrier.

## two thick sextics cannot be the pair

<a id="p-018"></a>

Assume characteristic zero, so
\(N_C\simeq\mathcal O(7)^2\), and suppose two non-\(q\)-divisible double
sextics \(F,G\) cut out only \(C\).  Their complete intersection has degree
36, hence generic transverse length nine along the degree-four support.  In
the transverse ring \(k(C)[[x,y]]\), both equations have order two.  Relatively
prime quadratic initial forms would have intersection length four, so the two
quadratics have a common nonconstant factor.

On the exceptional divisor

\[
 E=\mathbf P(N_C)\simeq\mathbf P^1\times\mathbf P^1,
\]

each quadratic normal divisor has class \((10,2)\).  The generic common factor
closes to a horizontal common component
\(T\sim(a,e)\), where \(a\ge0\) and \(e=1\) or \(2\); vertical factors caused
by closed-point order jumps do not remove this horizontal component.

The first normal form of \(q\) vanishes on the section

\[
 S_q=\mathbf P(N_{C/Q})\sim(1,1).
\]

The class is not \((0,1)\): after twisting the normal inclusion
\(N_{C/Q}=\mathcal O(6)\hookrightarrow\mathcal O(7)^2\) by
\(\mathcal O(-7)\), it is given by two independent linear forms, so its graph
has base degree one.

On \(Q\), write

\[
 F|_Q=h^2R_F,\qquad G|_Q=h^2R_G,\qquad
 R_F,R_G\in H^0(O_Q(4,0)).
\]

Restriction of the quadratic normal divisors to \(S_q\) is exactly the pullback
of the zero divisors of \(R_F,R_G\).  If \(T=S_q\), both residual quartics
vanish identically, so both sextics are divisible by \(q\), contrary to the
hypothesis.  Otherwise

\[
 T\cdot S_q=a+e>0.
\]

At an intersection point the two residual binary quartics have a common root.
The corresponding ruling line of \(Q\) is then contained in both \(F\) and
\(G\), giving an extra curve outside \(C\).  This contradiction proves

\[
 \boxed{\text{no thick--thick \((6,6)\) defining pair exists in
 characteristic zero}.}
\]

The balanced-normal hypothesis is essential to this proof.  In characteristic
two, \(N_{C_0}=\mathcal O(6)\oplus\mathcal O(8)\), so
\(E\simeq\mathbb F_2\) has a negative section disjoint from \(S_q\).  Exact
examples show that two tangent quadratics can share that section while their
residual quartics are coprime; those examples have other extra curves and are
not STCI pairs, but they prevent an invalid characteristic-two extension of
the argument.

## Characteristic boundary

The 23-dimensional double-sextic source and its five-dimensional quadric quotient use the characteristic-free smooth-quadric sheaf-power theorem and binary monomial multiplication; no division by a factorial is used. The explicit F_* Jacobian/radical example retains its certified characteristic-zero scope. The thick–thick intersection proof uses the displayed balanced-normal exceptional product and quadric-direction graph; its conclusion has that hypothesis, which fails for fixed C0 in characteristic2. A negative section on the resulting Hirzebruch surface prevents this argument from extending unchanged. The [every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) is a separate global construction, not supplied by the characteristic2 failure model.
