# Common-quadric first-order Chow boundary

Work over an algebraically closed field with the fixed quartic
\(C\sim(1,3)\) on its unique smooth quadric
\(Q\simeq\mathbf P^1\times\mathbf P^1\). This calculation concerns
quartic pencils through \(C\) whose special equations share the factor
\(Q\). It determines the cycle of a first-order proper degeneration and
its residual linear system.

## The cycle of the flat closure

Fix quadrics \(A,B\) such that \(V(A,B)\) is a proper degree-four
curve and their restrictions \(a,b\in H^0(Q,\mathcal O_Q(2,2))\)
form a regular sequence. Thus \(Z=V_Q(a,b)\) has length eight and
\(V(A,B)\) has no component in \(Q\). Take an arc of quartic pairs
through \(C\):
\[
 F_t=QA+tF_1+O(t^2),\qquad G_t=QB+tG_1+O(t^2).
\]
Assume its generic pair is proper and \(K=BF_1-AG_1\) is not
divisible by \(Q\). Let \(\mathcal Y\) be the flat closure of the
generic complete intersection. Its special fundamental cycle is
\[
 [\mathcal Y_0]=[V(A,B)]+[V(Q,K)],\qquad 4+12=16.
\]

Indeed, off \(Q\) the limiting equations are \(A,B\). Off
\(V(A,B)\), one of \(A,B\) is invertible, and eliminating the common
factor with \(BF_t-AG_t=tK+O(t^2)\) gives the limiting equations
\(Q,K\). The regular-sequence and nondivisibility hypotheses make
these proper curve contributions with no shared component; their
degrees exhaust the generic degree sixteen. The claim concerns the
fundamental cycle of the flat closure, not the naive special equation
scheme \(V(QA,QB)\), which has a surface component. It does not assert
reducedness of \(\mathcal Y_0\).

## The residual linear system

Write \(s_C\in H^0(Q,\mathcal O_Q(1,3))\) for the equation of
\(C\). The ideal sequence of \(Q\) shows that restrictions of quartics
through \(C\) exhaust \(s_C H^0(Q,\mathcal O_Q(3,1))\). Therefore
\[
 K|_Q=s_C(bf-ag),\qquad
 k=bf-ag\in H^0(Q,\mathcal I_{Z/Q}(5,3)),
\]
and the cycle is \([V(A,B)]+[C]+[D_k]\), with
\(D_k\sim(5,3)\) of degree eight. The twisted Koszul resolution is
\[
 0\longrightarrow\mathcal O_Q(1,-1)
 \longrightarrow\mathcal O_Q(3,1)^{\oplus2}
 \xrightarrow{(b,-a)}\mathcal I_{Z/Q}(5,3)\longrightarrow0.
\]
Both \(H^0(Q,\mathcal O_Q(1,-1))\) and
\(H^1(Q,\mathcal O_Q(1,-1))\) vanish, while
\(h^0(Q,\mathcal O_Q(3,1))=8\). Thus every residual section is
obtained from first-order quartic deformations, and their space has
dimension sixteen. Its projectivization is \(\mathbf P^{15}\);
the proper-arc conditions still apply to interpreting sections as limits.

## Relative family and rank drops

Let \(B_Q^\circ\subset\operatorname{Gr}(2,H^0(\mathbf P^3,\mathcal O(2)))\)
be the locus where the two restrictions form a regular sequence on
\(Q\). The schemes \(Z_W\) vary flatly there. The same Koszul
calculation gives a rank-sixteen bundle \(\mathcal E\) with fibre
\(H^0(Q,\mathcal I_{Z_W/Q}(5,3))\). Its projectivization has a
natural cycle map
\[
 \mathbf P_{B_Q^\circ}(\mathcal E)\longrightarrow
 \operatorname{Chow}_{1,16}(\mathbf P^3),\qquad
 (W,[k])\longmapsto[V(A,B)]+[C]+[D_k].
\]

If \(a,b\) acquire a common divisor \(h\) on \(Q\), the specialized
multiplication image has \(k=h(b'f-a'g)\). Limits of sections from the
regular-sequence locus need not lie in that image when its rank drops.
The closure of the projective bundle must therefore be distinguished
from the naive fibrewise incidence \(k\in(a,b)\).

The cycle argument uses the common-factor elimination and properness;
the explicit dimension sixteen uses the quartic degrees and the
\((1,3)\) embedding. It supplies no all-degree STCI obstruction.
The closure over rank drops, higher-order arcs, and identification of
the entire exceptional fibre of the resultant graph remain unresolved.
No equality with the ordinary blowup of the common-quadric locus is claimed.

## Review

Independent review on November 20, 2026 reconstructed the localized
cycle argument, degree exhaustion, Koszul dimensions and relative bundle,
and checked that the rank-drop and higher-order limitations remain
explicit. This is a proof of the scoped first-order statement; it does
not accept a full exceptional-fibre or blowup classification.

Final integration review checked the framework and Chow entry points
against current main. This boundary family lies in the already excluded
quartic degree pair and changes neither higher-degree coverage nor the
strategic ranking. The framework comparison yielded no further supported
implication requiring propagation; the remaining closure questions need
new mathematical evidence. The focused proof and its links passed the
file and retrieval review.
