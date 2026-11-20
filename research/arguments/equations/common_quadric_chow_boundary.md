# The clean common-quadric boundary in every degree

Let \(C\) be any smooth curve of class \((1,3)\) on a smooth quadric
\(Q\subset\mathbf P^3\), over an algebraically closed field of any
characteristic. For degrees \(a,b\ge3\), a deformation through \(C\)
away from the common factor \(Q\) has an explicit **full special
scheme** on the regular-restriction stratum. Its residual linear system
also identifies the [local resultant graph](common_quadric_resultant_blowup.md)
with an ordinary blowup. Neither statement covers rank drops on that center.

## The full special scheme

Take forms \(A,B\) of degrees \(a-2,b-2\), whose restrictions
\(\alpha,\beta\) form a regular sequence on \(Q\). Consider an arc
of pairs through \(C\):
\[
 F_t=QA+tF_1+O(t^2),\qquad G_t=QB+tG_1+O(t^2),\qquad K=BF_1-AG_1,
\]
and assume \(Q\nmid K\). Then the generic pair is automatically
proper, and its flat closure has saturated special ideal
\[
 I_0=(QA,QB,K)=(A,B)\cap(Q,K).
\]
It is ACM of dimension one projectively, has no embedded points, and
has the complete-intersection \((a,b)\) Hilbert function. No reducedness
is asserted. Its fundamental cycle is \([V(A,B)]+[V(Q,K)]\);
higher terms of the arc do not change this special scheme under the
stated first-order nonvanishing condition.

Here is the [clean-cancellation argument](../torus_hilbert_boundary.md#clean-cancellation-and-residual-descent)
without its later torus specialization. Regular restrictions imply that
\(A,B\) are coprime and that \(Q\) is regular on \(S/(A,B)\).
Since \(K\in(A,B)\) and \(Q\nmid K\), one has
\(I_0:Q=(A,B)\), giving
\[
 0\longrightarrow S/(A,B)(-2)\xrightarrow{Q}S/I_0
       \longrightarrow S/(Q,K)\longrightarrow0.
\]
Both end terms are dimension-two CIs. The depth lemma makes \(S/I_0\)
CM, and its Hilbert numerator is
\[
 z^2(1-z^{a-2})(1-z^{b-2})+(1-z^2)(1-z^{a+b-2})
                  =(1-z^a)(1-z^b).
\]
The \(t\)-saturated family ideal contains
\((BF_t-AG_t)/t=K+O(t)\), so its special ideal contains \(I_0\).
Each graded quotient is finite free over \(k[[t]]\). The linear growth
of the special Hilbert function bounds the generic dimension by two;
two homogeneous equations give the reverse bound. Thus the generic
pair is proper. Its CI Hilbert function equals that of \(I_0\),
forcing equality of the special ideals in every degree. Finally
\(Q\)'s regularity modulo \((A,B)\) proves the displayed intersection
of ideals. This establishes scheme structure as well as degree exhaustion.

## The entire residual source

Set \(Z=V_Q(\alpha,\beta)\), of length \(2(a-2)(b-2)\), and let
\(s_C\) define \(C\) on \(Q\). Restriction of the full degree-\(a\)
source through \(C\) is onto
\(s_C H^0(Q,\mathcal O_Q(a-1,a-3))\), by the quadric ideal
sequence; likewise for degree \(b\). Write \(F_1|_Q=s_Cf\),
\(G_1|_Q=s_Cg\). Then
\[
 K|_Q=s_Ck,\qquad k=\beta f-\alpha g\in
 V_Z:=H^0(Q,\mathcal I_{Z/Q}(a+b-3,a+b-5)).
\]
The twisted Koszul sequence is
\[
0\longrightarrow\mathcal O_Q(1,-1)\longrightarrow
 \mathcal O_Q(a-1,a-3)\oplus\mathcal O_Q(b-1,b-3)
 \xrightarrow{(\beta,-\alpha)}
 \mathcal I_{Z/Q}(a+b-3,a+b-5)\longrightarrow0.
\]
Both \(H^0\) and \(H^1\) of the left term vanish. Thus the map on
sections is an isomorphism, and
\(\dim V_Z=a(a-2)+b(b-2)\). Every nonzero \(k\) is realized by a
linear arc with the special scheme just proved. The degree bounds make
these section spaces available; the \((1,3)\) class explains the
acyclic kernel. For a different Cartier class \((r,s)\), that kernel
would be \(\mathcal O_Q(2-r,2-s)\), whose cohomology need not vanish.

The cycle is
\[
 [V(A,B)]+[C]+[D_k],\qquad
 \deg V(A,B)=(a-2)(b-2),\quad D_k\sim(a+b-3,a+b-5).
\]
Its degree is \((a-2)(b-2)+4+2(a+b-4)=ab\). The positive
off-quadric term excludes this clean boundary from a family whose
generic cycle is the constant \(m[C]\). This is an all-degree
restriction on one degeneration stratum, not an STCI exclusion.

For the fixed monomial quartic, the cycle is also outside the **exact**
[Chow-polytope fibre](chow_polytope_rigidity.md): its whole component on
\(Q\) has balanced class \((a+b-2,a+b-2)\), whereas each diagonal
translate lying on \(Q\) has class \((1,3)\). A diagonal automorphism
preserves \(Q\) and its rulings whenever it takes that curve into
\(Q\), by uniqueness of the containing quadric. The class mismatch
excludes a sum of such translates. This does not exclude the closure of
varying translate arrangements, whose components can reach coordinate
boundaries and leave that exact fibre.

## Relative boundary and remaining rank drops

On the regular-restriction locus of ordered \(([A],[B])\), the schemes
\(Z\) vary flatly and the spaces \(V_Z\) form a vector bundle of the
displayed rank. Its projectivization maps to Chow by
\(([A],[B],[k])\mapsto[V(A,B)]+[C]+[D_k]\). For quartic pencils
this descends to the familiar rank-sixteen bundle over the corresponding
open in \(\operatorname{Gr}(2,H^0(\mathcal O(2)))\).

If \(\alpha,\beta\) acquire a common divisor \(h\), the naive
specialized image is \(k=h(\beta'f-\alpha'g)\). Limits of sections
from the regular locus need not lie in that image when rank drops.
That closure, other common-factor strata and the global resultant graph
remain open. On the clean locus, however, the
[ordinary-blowup theorem](common_quadric_resultant_blowup.md) determines
the whole exceptional fibre and covers higher-order arcs.

Independent correctness, geometric and generality reviews reconstructed
the all-degree scheme argument and Koszul isomorphism on November 20,
2026. The first-order excess-intersection literature provides context;
the [source comparison](../../literature/README.md#common-factor-degenerations-and-excess-intersection)
keeps its hypotheses distinct from this direct algebraic proof.
