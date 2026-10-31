# A double-quadric matrix that cannot split into simple-quadric factors

Date: 2026-10-31. Status: **independently reviewed provisional counterexample**;
see the [bounded audit](2026-10-31-simultaneous-equation-geometry-audit.md).
Investigator: `simultaneous_quadric_equations`. No canonical promotion
or STCI conclusion.

Work over an algebraically closed field of characteristic zero. Set

\[
q=x_0x_3-x_1x_2,\qquad Q=V(q)\subset\mathbf P^3,
\qquad C=[s^4:s^3t:st^3:t^4].
\]

An arbitrary hypothetical supported pair \((F_a,G_b)\) supplies an identity
\(q^N=AF+BG\), hence a homogeneous two-by-two matrix
\(\left(\begin{smallmatrix}F&-B\\G&A\end{smallmatrix}\right)\)
with determinant \(q^N\). Its adjugate gives a matrix factorization of
\(q^N\). This retains the actual two global equations, unlike restriction
to the reduced quadric alone. The standard matrix-factorization/ACM-sheaf
dictionary was checked in [Hartshorne, *Liaison with Cohen–Macaulay
modules*, Appendix, pp. 430–431](https://seminariomatematico.polito.it/rendiconti/64-4/419.pdf).
The following example rejects a potential uniform shortcut: decomposing
every such matrix into matrices with determinant \(q\). It does not reject
a theorem with additional hypotheses specific to \(C\).

## The counterexample

Put \(\ell=x_1\), \(m=x_2\), and consider

\[
M=
\begin{pmatrix}
\ell^2&\ell m+q\\
\ell m-q&m^2
\end{pmatrix}:
\mathcal O_{\mathbf P^3}(-2)^2\longrightarrow
\mathcal O_{\mathbf P^3}^{2}.
\tag{1}
\]

Direct multiplication gives

\[
\det M=\ell^2m^2-(\ell m+q)(\ell m-q)=q^2,
\qquad M\operatorname{adj}(M)=q^2I_2.
\tag{2}
\]

On \(Q\),

\[
\overline M=
\begin{pmatrix}\ell\\m\end{pmatrix}
\begin{pmatrix}\ell&m\end{pmatrix}.
\tag{3}
\]

Its rank-zero **support** is exactly the nonempty finite scheme support

\[
T=Q\cap V(x_1,x_2)
=\{p_0=[1:0:0:0],p_\infty=[0:0:0:1]\}.
\tag{4}
\]

Here \(T\) itself is reduced; the ideal of the rank-zero locus of
\(\overline M\) is \((\ell^2,\ell m,m^2)\), so that locus has additional
scheme structure. Only its support is used below. These are precisely
the two marked endpoints of \(C\).

More precisely, the rank-zero scheme has length three at each point,
since its local ideal is the square of the maximal ideal on the smooth
surface Q.

**Proposition.** The map (1) cannot factor as

\[
\mathcal O(-2)^2\xrightarrow{B}\mathcal E
\xrightarrow{A}\mathcal O^2
\tag{5}
\]

through any rank-two vector bundle \(\mathcal E\) on \(\mathbf P^3\)
when the determinant divisor of each map is exactly the reduced quadric
\(Q\). This includes homogeneous matrix factors of determinant a nonzero
constant times \(q\), with arbitrary compatible twists. The same remains
true after invertible changes of source and target.

**Proof.** Each of \(A|_Q\) and \(B|_Q\) has rank exactly one at every
point. Indeed, its determinant vanishes on \(Q\), so the rank is at most
one. If the rank were zero at a point, all four local matrix entries
would belong to the maximal ideal there. The determinant would belong
to its square, contrary to the fact that a local equation of the smooth
reduced divisor \(Q\) has nonzero differential.

Consequently \(\mathcal L=\operatorname{im}(B|_Q)\subset\mathcal E|_Q\)
and \(\mathcal K=\ker(A|_Q)\subset\mathcal E|_Q\) are line subbundles.
The composition in (5) has rank zero at exactly the zeros of the induced
line-bundle map

\[
\mathcal L\longrightarrow\mathcal E|_Q/\mathcal K.
\tag{6}
\]

If this map is zero, the composition has rank zero everywhere on \(Q\).
Otherwise its zero locus is empty or an effective Cartier divisor on
the integral smooth surface \(Q\). Its support cannot be nonempty and
finite. This contradicts (3)–(4). Source and target isomorphisms preserve
pointwise rank, proving the last assertion. \(\square\)

## What the cokernel measures

Let \(\mathcal M=\operatorname{coker}M\). The injective presentation

\[
0\longrightarrow\mathcal O(-2)^2
\xrightarrow{M}\mathcal O^2
\longrightarrow\mathcal M\longrightarrow0
\tag{7}
\]

makes \(\mathcal M\) an ACM sheaf, maximal Cohen–Macaulay on the double
quadric \(2Q=V(q^2)\). For example, (7) gives
\(H^1(\mathbf P^3,\mathcal M(t))=0\) for every integer \(t\), and its
graded module has projective dimension one over the four-variable
polynomial ring. At the generic point of \(Q\), a matrix entry is a unit
and (2) identifies the cokernel with the ring of \(2Q\). Thus it is
generically free of rank one over \(2Q\).

It is locally free of rank one on \(2Q\setminus T\), but not at either
point of \(T\). At those points all entries in (1) lie in the maximal
ideal, so the cokernel needs two generators, whereas a rank-one free
module needs one. Hence even a two-generator, globally ACM, generically
rank-one module on a multiple smooth quadric can have a finite nonfree
locus. An argument using only extensions of line bundles to \(2Q\)
does not cover it.

One can see the precise defect without classifying modules. Write
\(e_1,e_2\) for the two degree-zero generators of the cokernel, and
\(u=\ell e_1+m e_2\). The two column relations in (1) give

\[
q e_1=-m u,\qquad q e_2=\ell u,\qquad qu=0.
\tag{8}
\]

In sheaf notation these identify

\[
\operatorname{Ann}_{\mathcal M}(q)=\mathcal O_Q(-1),
\qquad q\mathcal M=\mathcal I_{T,Q}(-1),
\tag{9}
\]

and give an exact sequence on \(2Q\)

\[
0\longrightarrow\mathcal O_Q(-1)
\longrightarrow\mathcal M
\longrightarrow\mathcal I_{T,Q}(1)
\longrightarrow0.
\tag{10}
\]

For completeness, restricting (7) to \(Q\), its kernel is generated by
\((-m,\ell)\), with source \(\mathcal O_Q(-3)\). The Tor identification
is \(\operatorname{Tor}_1(\mathcal M,\mathcal O_Q)
=\operatorname{Ann}_{\mathcal M}(q)(-2)\), proving the first identity
in (9). Equation (8) proves the second. Modulo \(u\), the generators
map to \(m,-\ell\), giving the quotient in (10).

Thus the complete ACM object has a natural quadric layer containing
the ideal of two points. That layer is not a line bundle; it also fails
the ACM condition, since
\(H^1(Q,\mathcal I_{T,Q}(-1))\simeq k^2\). Factoring through two simple
quadric determinant maps would force the rank-one bundle composition
(6), which cannot encode this punctual defect.

## Exact consequence for the STCI investigation

The false implication is

\[
\det M=q^N\quad\Longrightarrow\quad
M\text{ factors into }N\text{ rank-two maps with determinant divisor }Q.
\]

It already fails at \(N=2\), without degree enumeration or a carrier
classification. This blocks a general reduction of the multiple-quadric
matrix problem to successive simple-quadric factors.

The example is **not** asserted to arise from a pair supported on \(C\).
In fact its first column
\((x_1^2,x_1x_2-q)=(x_1^2,2x_1x_2-x_0x_3)\) defines
the two lines \(V(x_1,x_0)\) and \(V(x_1,x_3)\) as reduced support.
Its finite defect (4) already lies at the two marked points on \(C\).
A hypothetical STCI matrix has the additional actual column
\((F,G)\), whose common support is exactly \(C\); its nonfree locus is
therefore contained in \(C\), a condition this example also satisfies.
A successful argument must use the stronger actual
column-support condition, its homogeneous twists, and the actual normal
action together. No result here shows that those additional conditions
force a simple-quadric factorization or exclude the matrix.

The calculation is direct and needs no computer algebra. No inherited
proof was rerun. Independent review covered the endpoint-aligned example,
the arbitrary-intermediate-bundle argument and its cokernel layers. The
unrestricted characteristic-zero STCI question remains open.
