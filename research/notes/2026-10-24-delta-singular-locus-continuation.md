# The singular-locus defect: normal Koszul differentials, degrees, and length

Date: 2026-10-24. Status: **proved arguments and parameter families, independently reconstructed within this investigation; research proposal, not canonical promotion**.

This continues the [independent filtration investigation](2026-10-23-ideal-filtrations-independent-investigation.md), especially its question about
\(\Delta=\operatorname{in}_I(IJ)/(S_+\operatorname{in}_I(J))\) at simultaneous singular points. The predecessor's quotient comparison and smooth-carrier support proposition are used as reviewed premises rather than reproved.

Scope: local algebra along a smooth codimension-two marked curve \(C\) in a smooth threefold, with a two-generator regular-sequence ideal \(J\subset I_C\). The entire reduced support may be \(C\), or \(C\) may be a proper marked component. The distinction matters in the examples. No new unrestricted STCI proof or global pair for the fixed rational quartic is asserted.

## 1. Main advances

1. The module \(Q\) is canonically a Tor module. A filtered Koszul complex on the **normal parameters**, rather than the carrier equations, identifies \(\Delta\) exactly with accumulated incoming higher differentials.
2. Over a generic transverse field,
   \[
   \dim\Delta=\mu(\operatorname{in}J)-2.
   \]
   The degrees and spectral-sequence pages refine this excess count.
3. If the generic defect vanishes, a punctual defect is precisely the torsion of \(Q\) lost in the comparison with the filtered equation module. A DVR length formula makes this exact.
4. For every \(d\ge3\) and \(r\ge1\), integral local carriers realize a defect \(k[[t]]/(t^r)\) concentrated in degree \(d\). This example has actual residual support, which is proved separately.
5. A second family has arbitrarily many generic defect generators and explicitly prescribed cancellation page. It admits integral algebraic carriers.
6. A supported quadruple has torsion in \(Q\) but zero defect: torsion alone is insufficient. Whether nonzero punctual defect can occur for a supported, generically defect-free complete intersection remains unresolved here.

## 2. Notation and the intrinsic comparison

Locally write
\[
B=R/I,\quad M=R/J,\quad K=I/J,\quad
S=\operatorname{gr}_IR,\quad A=\operatorname{gr}_KM=S/H,
\]
\[
H=\operatorname{in}_I(J),\quad T=\operatorname{in}_I(IJ),\quad
Q=H/S_+H,\quad\Delta=T/S_+H.
\]
The equation module \(\mathcal D=J/IJ\) has
\[
F^n\mathcal D=((J\cap I^n)+IJ)/IJ.
\]
The predecessor proves
\[
0\to\Delta_n\to Q_n\to G_n\to0,\qquad
G_n=\operatorname{gr}_F^n\mathcal D=H_n/T_n.
\tag{1}
\]
For a regular-sequence \(J=(f,g)\), \(\mathcal D\) is free of rank two over \(B\). On a curve these constructions sheafify; all torsion and ranks below are taken over the actual base \(B=\mathcal O_C\), not over a transverse field unless explicitly specified.

## 3. The correct spectral sequence for the defect

### 3.1 A canonical Tor description

Apply \(-\otimes_SB\) to \(0\to H\to S\to A\to0\). Since
\(H\otimes_SB=H/S_+H\), \(A\otimes_SB=B\), and \(H\subset S_+\), the resulting sequence gives
\[
\boxed{Q\simeq\operatorname{Tor}_1^S(A,B).}
\tag{2}
\]
This assertion needs neither a field base nor regularity of \(J\).

Assume now \(I=(x,y)\) is a regular-sequence ideal. Use
\[
\mathscr K_\bullet=K_M(x,y)=M\otimes_RK_R(x,y),
\qquad
F^n\mathscr K_i=(K^{n-i})^{\binom2i},
\tag{3}
\]
with \(K^a=M\) for \(a\le0\). Both normal Koszul generators have weight one. The associated graded complex is \(K_A(X,Y)\). Since \(S=B[X,Y]\), it yields
\[
E_1^{i,n}=\operatorname{Tor}_i^S(A,B)_n
\ \Longrightarrow\
\operatorname{gr}_F^n\operatorname{Tor}_i^R(M,B),
\qquad
d_r:E_r^{i,n}\to E_r^{i-1,n+r}.
\tag{4}
\]

If \(K\) is nilpotent, this is a finite filtration and convergence is immediate. For the formal marked-component examples below, work in the complete noetherian \(I\)-adic setting with the displayed good filtrations. Convergence for this bounded complex can be seen directly from Artin–Rees: there is a uniform \(c\) such that
\(d\mathscr K_i\cap F^p\mathscr K_{i-1}\subset d(F^{p-c}\mathscr K_i)\).
If \(z\in F^p\mathscr K_i\) is an approximate cycle with \(dz\in F^{p+r}\) and \(r>c\), choose \(w\in F^{p+r-c}\) with \(dw=dz\). Then \(z-w\) is an actual cycle with the same leading class as \(z\). The same bound supplies all boundary representatives after a bounded number of pages. Thus the limit is the graded actual homology with its induced filtration. Separatedness follows from the local adic filtration. This argument concerns a bounded finite-module complex with good adic filtrations, not arbitrary unbounded filtrations. See the general [filtered-complex construction](https://stacks.math.columbia.edu/tag/012K).

### 3.2 The target filtration is exactly the previous one

The connecting homomorphism for \(0\to J\to R\to M\to0\) identifies
\[
\operatorname{Tor}_1^R(M,B)=J/IJ=\mathcal D.
\]
A cycle in (3) is represented by \((a,b)\) with \(ax+by\in J\), and maps to \([ax+by]\in J/IJ\). Changes of lifts alter this by \(IJ\); Koszul boundaries map to zero.

A filtered cycle of degree \(n\) can be represented by \(a,b\in I^{n-1}\), hence maps into \(J\cap I^n\). Conversely any \(j\in J\cap I^n\) has \(j=xa+yb\) with \(a,b\in I^{n-1}\). Thus the induced filtration on Tor is precisely \(F^n\mathcal D\) in (1), not an unspecified filtration supplied by an existence theorem.

For regular \(J=(f,g)\), its carrier Koszul resolution also gives
\[
\operatorname{Tor}_0^R(M,B)=B,\quad
\operatorname{Tor}_1^R(M,B)=\mathcal D,\quad
\operatorname{Tor}_2^R(M,B)=\bigwedge_B^2\mathcal D.
\tag{5}
\]

### 3.3 The higher differentials recover the entire defect

Here \(E_1^{0,n}=0\) except \(E_1^{0,0}=B\). Thus all outgoing higher differentials from \(E_r^{1,n}\), \(n\ge1\), vanish. It follows that
\[
Q_n=E_1^{1,n}\twoheadrightarrow E_2^{1,n}
\twoheadrightarrow\cdots\twoheadrightarrow E_\infty^{1,n}=G_n.
\]
The edge map is exactly (1). Put
\[
C_{0,n}=0,\qquad
C_{r,n}=\ker(Q_n\to E_{r+1}^{1,n}).
\]
Then
\[
\boxed{
C_{r,n}/C_{r-1,n}
\simeq\operatorname{im}
(d_r:E_r^{2,n-r}\to E_r^{1,n}),
\qquad C_{\infty,n}=\Delta_n.
}
\tag{6}
\]
This is a filtration of \(\Delta_n\), not a preferred direct-sum decomposition. It answers the question about higher cancellations precisely.

The source is Tor of the **full** normal initial algebra. It is not necessarily a relation between the two displayed leading carrier equations. The earlier filtered carrier Koszul complex \(K(f,g)\) has a different first page. Confusing those two spectral sequences would identify different invariants.

Since the degree-two normal Koszul term has weight two, only \(1\le r\le n-2\) can contribute to (6). In particular
\[
\Delta_1=\Delta_2=0.
\tag{7}
\]
More generally, \(J\subset I^e\) implies \(\Delta_n=0\) for \(n\le e+1\): in degree \(e+1\), the initial piece of \(IJ\) is exactly \(S_1H_e\).

## 4. Generic generator counts and punctual length

### 4.1 The exact generic count

Let \(R=L[[x,y]]\), \(I=(x,y)\), and let \(J\) be an \(I\)-primary two-generator complete intersection. Write \(h=\mu(H)=\dim_LQ\). Since \(\dim_L\mathcal D=2\), summing (1) proves
\[
\boxed{\dim_L\Delta=h-2.}
\tag{8}
\]
Degreewise it is \(\dim_L\Delta_n=\dim_LQ_n-\dim_LG_n\).

The minimal graded Hilbert–Burch resolution of the artinian \(L[X,Y]/H\) has total Betti numbers \((1,h,h-1)\). Equations (4)–(6) remove exactly \(h-2\) pairs between homological degrees two and one, leaving \((1,2,1)\). A syzygy in degree \(a\) is paired with an equation in degree \(b>a\), with page \(r=b-a\). The literature calls these **negative consecutive cancellations**, despite the positive increase in internal filtration degree.

This mechanism is established mathematics: [Rossi–Sharifan, Theorem 3.1](https://arxiv.org/abs/0904.1086) and [Sammartano, Theorem 2 and its spectral-sequence proof](https://arxiv.org/abs/1605.05220) treat such cancellations. The relative proof above additionally identifies the actual \(B\)-module filtration needed here. These papers are not being used to replace a module calculation over a curve by field-valued Betti numbers.

For a transverse field complete intersection, a nonzero defect cannot occur below degree four. If one generator has order one, the predecessor's smooth-carrier proposition gives zero defect; otherwise \(J\subset I^2\), and (7) gives vanishing through degree three. The predecessor's degree-four example is therefore sharp.

### 4.2 Exact torsion formula on a smooth curve

Suppose \(\Delta\) vanishes generically on an integral smooth curve. Then it is a torsion submodule of \(Q\). In particular
\[
Q\text{ torsion free and }\Delta_\eta=0\quad\Longrightarrow\quad\Delta=0.
\tag{9}
\]

At a point, let \(B\) be the corresponding DVR. The surjection \(Q_n\to G_n\) has equal generic ranks. On torsion-free quotients it is a surjection between free modules of the same rank, hence an isomorphism. Consequently
\[
0\to\Delta_n\to\operatorname{tors}Q_n
\to\operatorname{tors}G_n\to0,
\]
\[
\boxed{
\operatorname{length}_B\Delta_n
=\operatorname{length}_B\operatorname{tors}Q_n
-\operatorname{length}_B\operatorname{tors}G_n.
}
\tag{10}
\]
The generic-vanishing hypothesis is essential. Torsion in the filtered equation quotients must be subtracted; torsion in \(Q\) alone is not the defect.

## 5. Arbitrary punctual degree and length, with integral carriers

Work in characteristic zero. Let \(D=k[[t]]\), \(R=D[[x,y]]\), \(I=(x,y)\). Choose \(r\ge1\), \(m\ge2\), put \(a=t^r\), and define
\[
f=ax+x^2+y^m,\qquad
g=ay+xy+y^m+x^{m+1},
\]
\[
h=xg-yf=xy^m-y^{m+1}+x^{m+2},
\qquad q=XY^m-Y^{m+1}.
\tag{11}
\]
The same polynomials define integral algebraic hypersurfaces before completion. For \(f\), its quadratic discriminant \(t^{2r}-4y^m\) is squarefree in \(k(t)[y]\), so is not a square in \(k(t,y)\). For \(g\), viewed as a monic polynomial in \(x\), Eisenstein at \(y\) over \(k(t)[y]\) applies: its constant term is \(ay+y^m\), of \(y\)-order one. Gauss's lemma gives irreducibility in \(k[t,x,y]\). Thus the carriers are distinct integral hypersurfaces, and their localized ideal is a regular sequence. Completion preserves the latter assertion.

### 5.1 Full initial ideal, rather than a chosen-generator approximation

The full initial ideal is
\[
\boxed{H=(aX,aY,q).}
\tag{12}
\]
Here is a proof for every \(r,m\). All polynomial syzygies of these three symbols are generated by
\[
(Y,-X,0),\qquad (-Y^m,Y^m,a).
\]
Indeed reduce \(aXA+aYB+qC=0\) modulo \(a\). The polynomial \(q=Y^m(X-Y)\) is a nonzerodivisor over \((D/a)[X,Y]\): both monic factors \(Y\) and \(X-Y\) are nonzerodivisors. Hence \(C=aC'\), and canceling \(a\) reduces the claim to the syzygies of \(X,Y\).

Both symbol syzygies lift exactly:
\[
yf-xg+h=0,\qquad
(-y^m-x^{m+1})f+y^mg+(a+x)h=0.
\tag{13}
\]
Give \(f,g,h\) weights \(1,1,m+1\). The corrections in (13) have strictly larger weights. The complete filtered syzygy-lifting criterion therefore proves (12). Concretely one corrects the lowest canceled part of any expression using (13), repeatedly raises its weight, and passes to the \(I\)-adically complete limit. This supplies a standard-basis proof for all parameters, independent of the finite samples.

### 5.2 Defect, annihilator, and conormal rank

The conormal map is \(\phi=\operatorname{diag}(a,a)\) over \(D\); it is injective. Thus \(F^2\mathcal D=0\), and every higher \(Q_n\) is defect. Formula (12) gives
\[
Q_1\simeq D^2,\qquad
Q_{m+1}=\Delta_{m+1}\simeq D/(t^r),
\]
with all other higher pieces zero. The annihilator is exactly \((a)\): the relation \(aq\in S_+(aX,aY)\) shows one inclusion; the unit coefficients in \(q\) show there is no smaller coefficient annihilator. Also
\[
\operatorname{in}_I(IJ)=(aX^2,aXY,aY^2,q).
\tag{14}
\]
The inclusion of \(q\) is already witnessed by \(h=xg-yf\in IJ\). Fullness follows alternatively from \(F^n\mathcal D=0\) for \(n\ge2\).

Therefore every normal degree \(d=m+1\ge3\) and every local length \(r\ge1\) occur independently. Degree three is the smallest possible punctual defect by (7). This contrasts with the transverse-field lower bound four.

### 5.3 Actual fibres and residual support

After inverting \(t\), the normal algebra along the marked curve has length one: \(H_{k((t))}=(X,Y)\) and \(\phi\) has rank two. At \(t=0\), the actual fibre has length \(m+2\). To check the latter, eliminate \(x^2=-y^m\). The other equation gives \(xy=-y^m v(y)\) with \(v(0)=1\); if \(m+1\) is odd, first divide by a unit of \(k[[y]]\). Comparing \(x(xy)\) and \(y(x^2)\) yields
\[
y^{m+1}(1+y^{m-2}v(y)^2)=0.
\]
Its second factor is a unit, of constant \(1\) for \(m>2\), and \(2\) for \(m=2\). Hence \(y^{m+1}=0\), then \(x^3=0\), and \(xy=-y^m\). The quotient has basis \(1,x,y,\ldots,y^m\). Conversely these relations define an associative algebra of that dimension satisfying the equations.

For \(m\ge3\), its full fibre initial ideal is \((X^2,XY,Y^{m+1})\); for \(m=2\), it is instead
\((X^2+Y^2,XY+Y^2)\), a regular quadratic pair. The actual fibre defect is respectively one-dimensional in degree \(m+1\), or zero when \(m=2\).

In contrast, base-changing the relative normal algebra (12) gives \(k[X,Y]/(q)\), which has infinite length. In the smallest case even defect formation fails to commute with the fibre:
\[
\Delta\otimes_Dk=k\text{ in degree }3,\qquad
\Delta_{\text{actual closed fibre}}=0.
\tag{15}
\]

The actual algebra \(R/J\) is finite flat over \(D\), of rank \(m+2\): the finite special fibre gives finiteness by completeness; \(t\) is a parameter on this one-dimensional Cohen–Macaulay complete intersection, hence a nonzerodivisor. But its marked component has generic local length one. There is therefore a genuine residual generic contribution of rank \(m+1\). This is a marked-component example, not a thickening supported only on \(C\). That residual assertion uses the actual finite algebra; it is not an inference from vertical pieces of its normal cone.

## 6. Arbitrarily many generic defects and a prescribed cancellation page

Let \(L\) be any field, \(n\ge2\), \(q\ge3\), \(R=L[[x,y]]\), \(I=(x,y)\). Define
\[
D_0=1,\quad D_1=x,\quad D_j=xD_{j-1}-y^qD_{j-2},
\]
\[
J_{n,q}=(D_n,y^qD_{n-1}),\qquad
h_i=y^{qi}D_{n-i}\quad(0\le i\le n).
\tag{16}
\]
The recurrence gives
\[
y^qh_{i-1}-xh_i+h_{i+1}=0,\quad h_{n+1}=0.
\tag{17}
\]
Thus \(h_i\in IJ\) for \(i\ge2\).

Because \(q>2\), \(\operatorname{in}D_j=X^j\) and
\(\operatorname{in}h_i=X^{n-i}Y^{qi}\). Consequently \((X,Y^q)^n\subset H\). Its colength is \(qn(n+1)/2\).

The monic resultant recurrence gives
\[
\operatorname{Res}_x(D_n,D_{n-1})
=\pm y^{qn(n-1)/2}.
\]
It follows inductively by reducing \(D_n\) modulo \(D_{n-1}\), which leaves \(-y^qD_{n-2}\). Taking the resultant with \(y^qD_{n-1}\) adds \(y^{qn}\). As \(D_n\) is monic, this is the determinant of multiplication over \(L[[y]]\), so the quotient length is \(qn(n+1)/2\). Equality of colengths proves the full initial ideal:
\[
H=(X,Y^q)^n.
\tag{18}
\]

Set \(a_i=n+(q-1)i\). The first two classes \(h_0,h_1\) survive in \(\mathcal D\), in degrees \(a_0,a_1\), while the rest lie in \(IJ\). Equation (1), or the length-two quotient \(\mathcal D\), now gives
\[
\boxed{\Delta=\bigoplus_{i=2}^nL(-a_i),\qquad
\dim_L\Delta=n-1.}
\tag{19}
\]
Both the number and degrees of defect generators are unbounded.

There is an explicit resolution realizing every cancellation. Index generator rows \(0,\ldots,n\) and syzygy columns \(1,\ldots,n\). In column \(i\), put \(y^q\) in row \(i-1\), \(-x\) in row \(i\), and \(1\) in row \(i+1\) if \(i<n\). This is a nonminimal Hilbert–Burch matrix for the redundant list (16). Dropping the units gives the minimal graded matrix of (18), with syzygy degrees \(b_i=a_i+1\). The lifted units have gap
\[
a_{i+1}-b_i=q-2.
\]
Tensoring the strict filtered resolution with \(L\) leaves only these unit entries. Its Tor spectral sequence has
\[
d_{q-2}(u_i)=e_{i+1}\quad(1\le i<n),
\tag{20}
\]
and no other nonzero differential. It removes precisely (19), leaving Tor-one degrees \(a_0,a_1\) and Tor-two degree \(b_n=qn+1\). This is an explicit resolution model of the same filtered Tor comparison; a choice of resolution supplies the displayed bases.

### Integral algebraic carriers

The recursive generators themselves need not be integral equations. There is an explicit upgrade. In affine three-space with marked line \(C=(x,y)=0\), choose \(N\ge qn+1\) and set
\[
F=D_n+t\,y^N,\qquad
G=y^qD_{n-1}+t(x^N+y^N).
\tag{21}
\]
Both are primitive and linear in \(t\), hence irreducible by Gauss's lemma. For the first, \(\gcd(D_n,y)=1\). For the second, over an algebraic closure each factor of \(x^N+y^N\) is a line \(x=\lambda y\), \(\lambda\ne0\); substituting it into \(D_{n-1}\) gives a nonzero lowest term \(\lambda^{n-1}y^{n-1}\). There is no common factor.

Since \(I^{qn}\subset J_{n,q}\) after completion, the perturbations lie in \(IJ_{n,q}\). The new generator-change matrix is the identity modulo \(I\), hence invertible in the completions along the affine line. Thus (18)–(20) remain exact there. Homogenization gives integral projective carriers, with this local defect along the affine part of a line. Residual global components are allowed. This proves unbounded local defects under integral-carrier hypotheses; it is not a construction for the fixed rational quartic.

## 7. A supported quadruple: torsion in Q is not enough

There is a useful control example with no residual support. Let \(D=k[[t]]\),
\[
J=(x^2,y^2+tx)\subset D[[x,y]],\qquad I=(x,y).
\]
It can be presented by the two integral polynomial carriers \(y^2+tx\) and \(x^2+y^2+tx\). Both are primitive and linear in \(t\), with coprime coefficient pairs. Both are singular at the origin; at generic \(C\) their first symbols agree and have rank one.

The actual algebra is free of rank four over \(D\), with basis \(1,x,y,xy\), relations \(x^2=0,y^2=-tx\). In particular \(I^4=0\) and its entire reduced support is \(C\).

Its full initial ideal is
\[
H=(tX,X^2,XY^2,Y^4).
\tag{22}
\]
This follows directly from the basis: \(K\) is spanned by \(x,y,xy\), \(K^2\) by \(tx,xy\), \(K^3\) by \(txy\), and \(K^4=0\). Thus
\[
Q_1=D,\quad Q_2=D/(t),\quad Q_3=D/(t),\quad Q_4=D.
\]
In the original generator frames \(e_f,e_g\), its equation filtration is
\[
F^2\mathcal D=De_f,\quad F^3\mathcal D=tDe_f,\quad
F^4\mathcal D=t^2De_f,\quad F^5\mathcal D=0.
\]
The comparisons \(Q_n\to G_n\) are isomorphisms. Hence \(\Delta=0\) despite torsion in \(Q_2,Q_3\). All that torsion is retained in \(G_2,G_3\), exactly as required by (10).

## 8. What has been settled, and the remaining question

The proposed connection with higher Koszul cancellation now has a theorem, including the actual filtration and pagewise subquotients. Generic defect is exactly generator excess, while punctual defect is a loss of torsion measured by (10). There is no bound on punctual degree or length under the broader marked-component hypotheses, nor on generic defect rank even with integral carriers.

The positive punctual examples have residual support. The supported quadruple proves that simultaneous singularity and torsion in \(Q\) are not sufficient for a defect. This investigation does not yet decide:

> If \(J=(f,g)\) is a complete intersection with \(\sqrt J=I_C\), \(C\) smooth, and \(\Delta_\eta=0\), can \(\Delta\) be nonzero at isolated points? If so, what is its smallest supported example; if not, which duality or support condition forces vanishing?

This is a strictly narrower question than the unrestricted STCI problem. It retains actual support and all local equations. The family in section 5 must not be used as an answer to it.

The literature already studies the generic tangent-cone generator and cancellation problem; [Mandal–Rossi, The tangent cone of a local ring of codimension 2](https://arxiv.org/abs/1402.2756) is another relevant primary source. No novelty claim is made here. The useful research interface is the precise relative defect, its torsion, and its relation to supported versus residual intersection geometry.

## 9. Review and reproducibility

The normal Koszul theorem was independently derived by lifting_audit and checked against the primary agent's separate filtration and Tor analysis. diagrams_derived independently reconstructed the generic generator count and cancellation resolution; its family_singular reviewer reconstructed (16)–(21). singular_family proved the punctual parameter family, and completeness independently reproduced its full Rees initials and lifted syzygies. The primary agent separately checked the integral-carrier arguments, special-fibre length, supported quadruple, and all saved code.

The [review record](2026-10-24-delta-singular-locus-review.md) distinguishes completed independent mathematical checks from the primary-agent synthesis and remaining convergence qualifications. The [validation directory](../validation/delta-singular-locus-2026-10-24/README.md) preserves exact commands and outputs.

Two independent implementations accompany the proofs: [Python full-product identities](../computations/verify_delta_singular_identities_2026_10_24.py) and [Macaulay2 Rees-saturation samples](../computations/verify_delta_singular_families_2026_10_24.m2). Finite samples verify their stated boundaries, not the arbitrary-parameter theorems. No canonical result or question record is altered.
