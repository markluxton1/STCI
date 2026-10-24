# Independent review: Delta and conormal specialization

Date: 2026-10-24. Reviewer: `audit_rees`, an independent agent in this investigation.

Target: [Rees specialization proposal](2026-10-24-delta-rees-specialization-proposal.md).

Status: **independent reconstruction of the algebraic theorem and explicit family; research evidence, not canonical promotion or external referee acceptance**.

## Scope and method

The review independently reconstructs the quotients, multiplication maps, kernel, specialization exactness, and parameter-flatness statement from the proposed definitions. It does not replay inherited computational certificates. The setup permits a marked smooth curve in a complete-intersection curve with additional components. No equation \(\sqrt J=I\) is imposed.

For the algebraic theorem it suffices that \(R\) is a noetherian algebra over a field \(k\), with ideals \(J\subset I\). Smoothness and the complete-intersection condition are needed for the intended geometric context and the rank-two interpretation of \(D=J/IJ\), rather than for the basic Rees quotient identities.

## 1. Independent degreewise calculation

Write \(I^n=R\) for \(n\le0\), and give \(u\) degree \(-1\). Put
\[
\mathscr R=\bigoplus_{n\in\mathbf Z}I^n u^{-n},\qquad
\mathscr J=\bigoplus_{n\in\mathbf Z}(J\cap I^n)u^{-n},\qquad
\mathscr L=(I/u)\mathscr R.
\]
The equalities
\[
\mathscr R/\mathscr L=B[u],\qquad B=R/I,
\]
and
\[
\mathscr N=\mathscr J/\mathscr L\mathscr J,\qquad
\mathscr N_n=\frac{J\cap I^n}{I(J\cap I^{n-1})}
\tag{R1}
\]
follow directly from multiplication in the extended Rees algebra. In particular the denominator in (R1) is an actual intersection-filtration term, not merely \(IJ\cap I^n\).

The natural map to the extended Rees module of the induced equation filtration is surjective degreewise:
\[
\mathscr N\twoheadrightarrow
\mathscr D_F:=\bigoplus_{n\in\mathbf Z}F^nD\,u^{-n},
\qquad
F^nD=((J\cap I^n)+IJ)/IJ.
\]
Its kernel is
\[
\mathscr E_n=
\frac{IJ\cap I^n}{I(J\cap I^{n-1})}.
\tag{R2}
\]
Multiplication by \(u\) is induced by inclusion into the preceding filtration stage. The target embeds in \(D[u,u^{-1}]\), so multiplication by \(u\) on the target is injective. After inverting \(u\), the displayed surjection is an isomorphism onto \(D[u,u^{-1}]\). Thus
\[
\mathscr E=H^0_{(u)}(\mathscr N),
\tag{R3}
\]
the full \(u\)-power torsion submodule.

Noetherianity makes \(\mathscr J\) a finite ideal of \(\mathscr R\); consequently \(\mathscr N\), and then \(\mathscr E\), are finite over \(B[u]\). Hence one power \(u^N\) kills all of \(\mathscr E\). This can also be read directly from Artin–Rees: (R2) is zero below degree two and above a finite filtration bound.

## 2. The exact specialization, with no missing Tor term

Reducing (R1) modulo \(u\) gives
\[
(\mathscr N/u\mathscr N)_n
=\frac{J\cap I^n}
 {I(J\cap I^{n-1})+(J\cap I^{n+1})}
=Q_n.
\tag{R4}
\]
Here the image of \(I(J\cap I^{n-1})\) in \(H_n\) is precisely \((S_+H)_n\). Every higher positive-degree product factors through the degree-one multiplication appearing in this denominator.

Similarly
\[
\mathscr D_F/u\mathscr D_F=\operatorname{gr}_F D.
\]
Since \(u\) is injective on \(\mathscr D_F\), tensoring the kernel sequence by \(k[u]/(u)\) introduces no left Tor term. Therefore
\[
0\longrightarrow\mathscr E/u\mathscr E
\longrightarrow Q\longrightarrow\operatorname{gr}_F D
\longrightarrow0.
\tag{R5}
\]
The quotient map in (R5) is the original comparison map. Its kernel is canonically
\[
\boxed{\mathscr E/u\mathscr E\simeq\Delta.}
\]
Because \(\mathscr E\) is killed by \(u^N\), the equality \(\mathscr E=u\mathscr E\) implies \(\mathscr E=0\) by iteration. This proves both directions of the vanishing criterion without an unqualified Nakayama argument on the nonlocal ring \(B[u]\).

## 3. Which flatness statement is justified

The module \(D[u,u^{-1}]\) has no torsion over \(k[u]\): choose a \(k\)-basis of \(D\). Every \(k[u]\)-torsion element of \(\mathscr N\) therefore belongs to \(\mathscr E\) after localizing at \(u\). Conversely \(\mathscr E\) is \(k[u]\)-torsion. Since \(k[u]\) is a principal ideal domain, torsion freedom is equivalent to flatness, including for modules not finite over \(k[u]\). Thus
\[
\Delta=0
\quad\Longleftrightarrow\quad
\mathscr E=0
\quad\Longleftrightarrow\quad
\mathscr N\text{ is flat over }k[u].
\tag{R6}
\]

This is flatness over the deformation parameter. It is **not** flatness over \(B[u]\). Even if \(\mathscr E=0\), nonsaturated stages of \(F^\bullet D\) can make the Rees module nonflat over the product base. The review requested that this distinction be explicit in the proposal.

## 4. Geometric quotient and carrier compatibility

Since \(\mathscr J\subset\mathscr L\), the module \(\mathscr N\) is exactly the conormal module of the schematic closure of \(Z\times\mathbf G_m\) in the ambient deformation to the normal cone, restricted to the zero-section family \(C\times\mathbf A^1\):
\[
(\mathscr J/\mathscr J^2)|_{C\times\mathbf A^1}
=\mathscr J/\mathscr L\mathscr J.
\]

The closure of \(Z\times\mathbf G_m\) need not equal the intersection of the closures of \(X\times\mathbf G_m\) and \(Y\times\mathbf G_m\). Its ideal is the \(u\)-saturation of the sum of those two ideals. This distinction retains the carrier arrows while allowing the Cartesian square of the original intersection to fail to remain Cartesian after special degeneration. Extra equations on the special normal cone cannot be identified with extra components of the original intersection by this observation alone.

## 5. Explicit torsion-persistence family

Independently checked family: over \(B=k[[t]]\), take
\[
J=(x^a+y^b,xy),\qquad 2\le a<b,
\qquad d=b-a.
\]
The full extended Rees ideal in the normal coordinates \(X=x/u,Y=y/u\) is
\[
\mathscr J=(F,G,H),\qquad
F=X^a+u^dY^b,\quad G=XY,\quad H=Y^{b+1}.
\tag{R7}
\]
The quotient has free \(B[u]\)-basis
\[
1,X,\ldots,X^{a-1},Y,\ldots,Y^b.
\]
For example a monic Gröbner calculation with leading monomials \(X^a,XY,Y^{b+1}\) gives this basis: its only nontrivial overlap reduces to \(u^dY^{b+1}\), which the third generator removes. This proves \(u\)-saturation and fullness of the ideal, rather than merely an inclusion of three proposed equations.

All syzygies of the displayed generators are generated by
\[
(Y,-X^{a-1},-u^d),\qquad(0,Y^b,-X).
\tag{R8}
\]
Indeed any relation \(AF+BG+CH=0\), reduced modulo \(Y\), forces \(A=YA_1\). Subtracting \(A_1\) times the first relation leaves \(XB'+Y^bC'=0\), which is a multiple of the second relation because \(X,Y^b\) is a regular sequence. Reducing (R8) modulo \((X,Y)\) gives
\[
\mathscr N\simeq
B[u]e_F\oplus B[u]e_G
\oplus B[u]/(u^d)e_H,
\tag{R9}
\]
where the generator degrees are \(a,2,b+1\). In particular
\[
\Delta=B e_H\quad\text{in degree }b+1,
\]
while the torsion block persists for \(d=b-a\) parameter steps. At fixed \(b\ge4\), varying \(a\) keeps the graded defect unchanged while changing this persistence. Thus the graded module \(\Delta\) does not determine the full torsion module \(\mathscr E\).

The integral-carrier upgrade is also valid. Let
\[
f=x^a+y^b+t y^{b+1},\qquad g=f+xy.
\]
Both polynomials are primitive and linear in \(t\), with coprime leading and constant coefficient pairs, hence irreducible by Gauss's lemma. Locally at the marked origin their ideal is exactly the model ideal, since
\[
y^{b+1}=y(x^a+y^b)-x^{a-1}(xy),
\]
\[
f=(1+ty)(x^a+y^b)-t x^{a-1}(xy),
\]
and \(1+ty\) is a unit. This proof uses a generator change with unit determinant; invertibility of \(1+ty\) alone would not justify deleting an arbitrary higher term.

## Outcome and limitations

The general algebraic theorem and family above pass independent reconstruction with the parameter-flatness and carrier-saturation qualifications recorded here. The written proposal was then read in full and compared against (R1)–(R9). The only additional wording correction requested concerns the direction of a possible splitting: the quotient \(R/J\to B\) exists canonically; what is not assumed is a splitting \(B\to R/J\), equivalently a retraction of the scheme onto the marked curve. No arbitrary formal algebraization, fixed-quartic construction, canonical result promotion, or STCI consequence follows. The theorem identifies what \(\Delta\) measures geometrically; the persistence module retains additional information that \(\Delta\) forgets.

The review has not asserted a general identification of every \(u\)-torsion block length with an individual normal-Koszul spectral-sequence page. The explicit family supports that interpretation, but a general statement would need a compatible filtered-resolution comparison and its own proof.
