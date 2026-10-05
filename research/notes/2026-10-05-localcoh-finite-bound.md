# A finite principal-part bound for quartic local-cohomology ancestors

Status: **PROVED**, conditional only on the already checked P-037 low-degree
exclusion and the literature's degree-(4,4) exclusion. This note does not
exclude every quartic ancestor; it reduces that question to a finite vector
space and bounds its primitive conormal direction.

Throughout, \(k\) is algebraically closed of characteristic zero,

\[
 S=k[x,y,z,w],\qquad
 C_0=[s^4:s^3t:st^3:t^4],\qquad
 I=I_{C_0},\qquad M=H_I^2(S),
\]

and

\[
 q=xw-yz,\quad B=xz^2-y^2w,\quad
 u=\frac{xz}{qB},\quad v=\frac{yw}{qB}.
\]

The target classes are in the first socle: \(Iu=Iv=0\). Suppose homogeneous
quartics \(F,G\) and a homogeneous \(\alpha\in M_{-7}\) satisfy

\[
 F\alpha=u,\qquad G\alpha=v.
\]

P-037 supplies \(F,G\in I\) and proportional first conormal symbols.

## 1. Coprimality and generic transverse length

The two forms are coprime. Indeed, if their greatest common divisor \(H\)
has positive degree \(r\), then \(\beta=H\alpha\) satisfies

\[
 (F/H)\beta=u,\qquad (G/H)\beta=v.
\]

These are equal-degree multipliers of degree \(4-r\le3\), contradicting
P-037. Scalar-proportional forms are excluded in the same way, or directly
by the linear independence of \(u,v\).

Consequently \(X=V_+(F,G)\) is an unmixed complete-intersection curve of
degree 16. Let \(m\) be its generic multiplicity along \(C_0\), equivalently
the length of the transverse Artinian algebra at the generic point of
\(C_0\). Its cycle contains \(m[C_0]\), so \(4m\le16\) and \(m\le4\).

If \(m=4\), the cycle degree is exhausted by \(4[C_0]\). Unmixedness leaves
no other curve component or isolated embedded point, so the support of \(X\)
is exactly \(C_0\). This would be a degree-\(4,4\) STCI presentation, contrary
to Craighero--Gattazzo, *Rend. Sem. Mat. Univ. Padova* 76 (1986), 177--200,
whose checked scope includes characteristic zero. Thus

\[
 \boxed{m\le3.}
\]

The precise literature record is in `research/LITERATURE_LEDGER.md`, under
“Craighero--Gattazzo, 1986”; the primary source is
<https://www.numdam.org/item/RSMUP_1986__76__177_0/>.

## 2. Generic annihilation extends over every curve point

Write

\[
 \mathcal E=\mathcal H^2_{C_0}(O_{\mathbf P^3}),\qquad
 \mathcal T_n=(0:_{\mathcal E}I^n).
\]

At the generic point of \(C_0\), the ideal \(I\) is the maximal ideal
of a regular local ring of dimension two. A local Artinian algebra of
length \(m\) has its maximal ideal's \(m\)-th power zero: if all successive
powers up to that point were nonzero, their strict descending chain would
already contribute more than \(m\) composition factors. Therefore

\[
 I^m\subset(F,G)
\]

at that generic point. Since \(I(F,G)\alpha=0\), we obtain

\[
 I^{m+1}\alpha=0
\]

generically along \(C_0\).

This is not merely generic information. At a closed curve point \(P\),
smoothness of the curve and ambient space gives the completed local model

\[
 R=k[[c,\xi,\eta]],\qquad I R=(\xi,\eta).
\]

Its local-cohomology module is the finite inverse-monomial module

\[
 H^2_{(\xi,\eta)}(R)
 =\bigoplus_{i,j\ge1}k[[c]]\,\xi^{-i}\eta^{-j}.
\]

In particular it has no \(k[[c]]\)-torsion. More invariantly, any element
of \(R\) whose restriction to \(C_0\) is nonzero acts injectively: in the
largest total inverse degree of a putative kernel element, multiplication
is multiplication by that nonzero restriction; normal terms lower the
inverse degree and cannot cancel it. Thus this sheaf has no nonzero
sections supported at a finite subset of \(C_0\). The generically zero
section \(I^{m+1}\alpha\) therefore vanishes at every curve point.

There is no additional element supported only at the cone vertex. The
composition spectral sequence for \(\Gamma_{\mathfrak m}\Gamma_I\), where
\(\mathfrak m=(x,y,z,w)\), gives

\[
 H^0_{\mathfrak m}(H_I^2(S))=0:
\]

the entry of total degree two has no possible incoming differential and
no outgoing differential because \(H_I^0(S)=H_I^1(S)=0\), while
\(H^2_{\mathfrak m}(S)=0\). Thus \(M\) injects into the graded sections of
its sheafification, and sheaf annihilation implies module annihilation.

Combining these facts gives

\[
 \boxed{I^4\alpha=0,\qquad
   \widetilde\alpha\in H^0(\mathbf P^3,\mathcal T_4(-7)).}
\]

The argument does not assume that the finite transverse algebras have
constant length at the special points, and does not require global ideal
containment \(I^m\subset(F,G)\). Torsion-freeness is exactly what extends
the generic annihilation of this particular local-cohomology element.

## 3. A genuinely fixed direct-limit stage

Since \(q,B\in I\), the bound implies \(q^4\alpha=B^4\alpha=0\). The sequence
\((q,B)\) is regular in \(S\), and

\[
 (0:_{H^2_{(q,B)}(S)}(q^n,B^n))
 =\left\{\frac{h}{q^nB^n}:h\in S\right\}
 \simeq S/(q^n,B^n)(5n).
\]

One proof first takes the kernel of \(q^n\) via the exact sequence for
\(S/q^nS\), obtaining \(H^1_{(B)}(S/q^nS)\), and then takes the kernel of
\(B^n\). Regularity of \(B\) modulo \(q^n\) identifies that kernel with
\(S/(q^n,B^n)\). The direct-system transition maps are injective as well,
by

\[
 (q^{n+1},B^{n+1}):qB=(q^n,B^n).
\]

Hence an ancestor must already have a representative \(h\in S_{13}\)
at stage \(n=4\), and it obeys the exact equations

\[
 \begin{aligned}
 Fh-xz(qB)^3&=q^4a+B^4b,\\
 Gh-yw(qB)^3&=q^4c+B^4d,
 \end{aligned}
\]

where \(a,c\in S_9\) and \(b,d\in S_5\). In addition
\(I^4h\subset(q^4,B^4)\) expresses membership in \((0:_M I^4)\). Solving in the full stage quotient
without this support/annihilator condition may introduce irrelevant
residual-line classes, so that condition should be retained in a finite
computation.

## 4. The primitive common conormal direction has degree at most two

Use the checked splitting \(N_{C_0/\mathbf P^3}\simeq O_{\mathbf P^1}(7)^2\).
In characteristic zero, the principal-part quotients are

\[
 \mathcal T_n/\mathcal T_{n-1}
 \simeq \operatorname{Sym}^{n-1}N\otimes\det N.
\]

After twisting by \(O_{\mathbf P^3}(-7)|_{C_0}=O_{\mathbf P^1}(-28)\), this
becomes

\[
 (\mathcal T_n/\mathcal T_{n-1})(-7)
 \simeq O_{\mathbf P^1}(7n-21)^{\oplus n}.
\]

Therefore \(H^0(\mathcal T_2(-7))=0\). A nonzero ancestor has a largest
principal-part order \(n\in\{3,4\}\).

Both first conormal symbols cannot vanish: a quartic vanishing to normal
order at least two along \(C_0\) is a scalar multiple of \(q^2\), by P-011
and \(I_2=kq\); two such forms cannot give the independent targets. Write
the nonzero common conormal direction as a basepoint-free pair

\[
 r=(r_1,r_2),\qquad r_i\in H^0(O_{\mathbf P^1}(e)),
\]

of coprime homogeneous binary forms. The quartic symbols are
\((a r,b r)\), with \((a,b)\) sections of \(O(9-e)\), because
\(N^*(4)=O(9)^2\). This definition includes a zero first symbol for one
of the two forms.

Multiplication by a linear normal symbol acts on the highest principal-part
symbol by contraction. Since \(F\alpha,G\alpha\in\mathcal T_1\), the
highest symbol of \(\alpha\) is killed by contraction with \(r\). For
binary symmetric powers in characteristic zero that kernel is the line
generated by

\[
 (-r_2,r_1)^{n-1}.
\]

Thus the highest symbol equals this vector times a nonzero section of

\[
 O_{\mathbf P^1}\bigl(7n-21-(n-1)e\bigr).
\]

Its degree must be nonnegative. For \(n=3\) this forces \(e=0\); for
\(n=4\) it forces \(e\le2\). Consequently

\[
 \boxed{e\le2.}
\]

This is a bound on the degree of the primitive common direction in the
balanced normal-bundle frame. It is not the degree of the quotient
(\sigma(G)/\sigma(F)), and should not be confused with an affine
coordinate polynomial degree before converting to that frame.

## 5. General form of the bound and remaining obstacle

For coprime equal-degree multipliers of degree \(d\) containing a smooth
degree-\(\delta\) curve, the same proof gives

\[
 m\le\left\lfloor\frac{d^2}{\delta}\right\rfloor,
 \qquad I^{m+1}\alpha=0
\]

whenever the targets are in the first socle. Thus each fixed multiplier
degree has a finite principal-part search, although that search grows with
\(d\). If the curve is \(C_0\), the ancestor has degree \(-(d+3)\), and the
highest quotient has degree \(7n-4d-5\) in the balanced normal frame.

For quartics the remaining problem is a finite, genuinely nonlinear
incidence problem: find \(\alpha\in(0:_M I^4)_{-7}\) for which the
quartic multiplication image contains both \(u,v\). The direction bound
\(e\le2\) is necessary, not an existence theorem or an exclusion. Exact
dimensions, annihilator generators, and the formal-neighborhood extension
of the candidate highest symbols require a separate verified computation.
