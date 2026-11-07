# The equation filtration, conormal torsion and specialization

For a smooth codimension-two curve C in a smooth threefold, retain the marked pair C subset Z=V(f,g), permitting residual components. The [local comparison R-0030](../results/local_filtration_comparison_defect.md) distinguishes minimal full initial equations from the filtered module of actual equations. This supplement owns the additional normal-Koszul, annihilator, extended-Rees and transverse-specialization proofs. They retain their inherited independently reconstructed source-level status; consolidation does not assert a global STCI obstruction.

The organization follows the mechanisms: first the exact comparison and higher cancellation, then the scheme supporting the defect, then its realization as deformation torsion, and finally the separate problem of slicing along the marked curve. All example families and necessary local hypotheses survive. The removed reports repeated these proofs; their substantive corrections are incorporated in the statements below.

<a id="delta-embedding-geometry-report"></a>

## 1. Exact hypotheses, retained inputs, and authority

For the geometric statements, \(C\) is a smooth integral curve in a smooth threefold \(P\), over a field of arbitrary characteristic. Locally
\[
R=\mathcal O_{P,p},\quad I=I_C=(x,y),\quad B=R/I,
\quad A_X=(f),\quad A_Y=(g),\quad J=A_X+A_Y\subset I,
\]
where \(f,g\) form a regular sequence. Distinct integral hypersurfaces give this situation; several algebraic results below have weaker hypotheses, stated in their individual notes. No rational-quartic classification, sole-support theorem, or STCI exclusion is a premise.

The [comparison construction](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd) and [normal-Koszul continuation](#delta-singular-locus-continuation) include comparison proof and reviewed source-level continuations. Their exact claims are retained as premises, without replaying inherited certificates. In particular,
\[
S=\operatorname{gr}_I R=\operatorname{Sym}_B E,\quad E=I/I^2,
\quad H=\operatorname{in}_I J,\quad T=\operatorname{in}_I(IJ),
\]
\[
D=J/IJ,\quad F^nD=((J\cap I^n)+IJ)/IJ,
\quad Q=H/S_+H,\quad G=\operatorname{gr}_F D,
\]
\[
0\longrightarrow\Delta=T/S_+H\longrightarrow Q
\longrightarrow G\longrightarrow0. \tag{1}
\]
All initial ideals are **full** initial ideals. A list of carrier symbols cannot replace \(H\) or \(T\).

The comparison result is stated in R-0030; the further mechanisms below retain their independently reconstructed source-level scope.

## 2. Retain the entire embedding and its maps

The data remain the actual schemes and inclusions
\[
C\subset Z\subset X,Y\subset P,
\]
including the original Cartesian square \(Z=X\times_PY\), all composites, and both labelled carrier ideals. The nine ideal-power filtrations and seven transitivity sequences are retained as specified in the predecessor, section 2. In particular, on \(C\),
\[
M_X=A_X/IA_X,\qquad M_Y=A_Y/IA_Y,
\qquad D=M_X\oplus M_Y,
\]
\[
\phi=(\alpha,\beta):D\longrightarrow E,
\qquad
0\to F^2D\to D\xrightarrow{\phi}E
\to N^*_{C/Z}\to0. \tag{2}
\]
The quotients \(E/\operatorname{im}\alpha\), \(E/\operatorname{im}\beta\), and \(E/\operatorname{im}\phi\) describe the paths through \(X,Y,Z\); their maps and image intersections remain part of the diagram. For projective carriers of degrees \(d,e\), the source lines in (2) are \(\mathcal O_C(-d),\mathcal O_C(-e)\). None is replaced by an abstract pair of unlabelled generators in questions about the original carriers.

The full quotient \(R/J\), its multiplication, and its Rees algebra retain the embedded scheme and extension information. The normal algebra \(S/H\), the filtration quotients, or \(\Delta\) alone do not reconstruct that scheme. Changing generators preserves the marked ideal \(J\subset I\), but can change the labelled intermediate hypersurfaces and their comparison maps.



<a id="delta-singular-locus-continuation"></a>
<a id="delta-singular-locus-review"></a>

<a id="normal-koszul-cancellation-and-the-actual-equation-filtration"></a>

## The singular-locus defect: normal Koszul differentials, degrees, and length

Date: 2026-10-24. Status: **proved arguments and parameter families, independently reconstructed within this investigation; research proposal**.

This continues the [independent filtration investigation](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd), especially its question about
\(\Delta=\operatorname{in}_I(IJ)/(S_+\operatorname{in}_I(J))\) at simultaneous singular points. The predecessor's quotient comparison and smooth-carrier support proposition are used as reviewed premises rather than reproved.

Scope: local algebra along a smooth codimension-two marked curve \(C\) in a smooth threefold, with a two-generator regular-sequence ideal \(J\subset I_C\). The entire reduced support may be \(C\), or \(C\) may be a proper marked component. The distinction matters in the examples. No new unrestricted STCI proof or global pair for the fixed rational quartic is asserted.

### 1. Main advances

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

### 2. Notation and the intrinsic comparison

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

### 3. The correct spectral sequence for the defect

#### 3.1 A canonical Tor description

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

#### 3.2 The target filtration is exactly the previous one

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

#### 3.3 The higher differentials recover the entire defect

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

### 4. Generic generator counts and punctual length

#### 4.1 The exact generic count

Let \(R=L[[x,y]]\), \(I=(x,y)\), and let \(J\) be an \(I\)-primary two-generator complete intersection. Write \(h=\mu(H)=\dim_LQ\). Since \(\dim_L\mathcal D=2\), summing (1) proves
\[
\boxed{\dim_L\Delta=h-2.}
\tag{8}
\]
Degreewise it is \(\dim_L\Delta_n=\dim_LQ_n-\dim_LG_n\).

The minimal graded Hilbert–Burch resolution of the artinian \(L[X,Y]/H\) has total Betti numbers \((1,h,h-1)\). Equations (4)–(6) remove exactly \(h-2\) pairs between homological degrees two and one, leaving \((1,2,1)\). A syzygy in degree \(a\) is paired with an equation in degree \(b>a\), with page \(r=b-a\). The literature calls these **negative consecutive cancellations**, despite the positive increase in internal filtration degree.

This mechanism is established mathematics: [Rossi–Sharifan, Theorem 3.1](https://arxiv.org/abs/0904.1086) and [Sammartano, Theorem 2 and its spectral-sequence proof](https://arxiv.org/abs/1605.05220) treat such cancellations. The relative proof above additionally identifies the actual \(B\)-module filtration needed here. These papers are not being used to replace a module calculation over a curve by field-valued Betti numbers.

For a transverse field complete intersection, a nonzero defect cannot occur below degree four. If one generator has order one, the predecessor's smooth-carrier proposition gives zero defect; otherwise \(J\subset I^2\), and (7) gives vanishing through degree three. The predecessor's degree-four example is therefore sharp.

#### 4.2 Exact torsion formula on a smooth curve

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

### 5. Arbitrary punctual degree and length, with integral carriers

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

#### 5.1 Full initial ideal, rather than a chosen-generator approximation

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

#### 5.2 Defect, annihilator, and conormal rank

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

#### 5.3 Actual fibres and residual support

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

### 6. Arbitrarily many generic defects and a prescribed cancellation page

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

#### Integral algebraic carriers

The recursive generators themselves need not be integral equations. There is an explicit upgrade. In affine three-space with marked line \(C=(x,y)=0\), choose \(N\ge qn+1\) and set
\[
F=D_n+t\,y^N,\qquad
G=y^qD_{n-1}+t(x^N+y^N).
\tag{21}
\]
Both are primitive and linear in \(t\), hence irreducible by Gauss's lemma. For the first, \(\gcd(D_n,y)=1\). For the second, over an algebraic closure each factor of \(x^N+y^N\) is a line \(x=\lambda y\), \(\lambda\ne0\); substituting it into \(D_{n-1}\) gives a nonzero lowest term \(\lambda^{n-1}y^{n-1}\). There is no common factor.

Since \(I^{qn}\subset J_{n,q}\) after completion, the perturbations lie in \(IJ_{n,q}\). The new generator-change matrix is the identity modulo \(I\), hence invertible in the completions along the affine line. Thus (18)–(20) remain exact there. Homogenization gives integral projective carriers, with this local defect along the affine part of a line. Residual global components are allowed. This proves unbounded local defects under integral-carrier hypotheses; it is not a construction for the fixed rational quartic.

### 7. A supported quadruple: torsion in Q is not enough

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

### 8. What has been settled, and the remaining question

The proposed connection with higher Koszul cancellation now has a theorem, including the actual filtration and pagewise subquotients. Generic defect is exactly generator excess, while punctual defect is a loss of torsion measured by (10). There is no bound on punctual degree or length under the broader marked-component hypotheses, nor on generic defect rank even with integral carriers.

The positive punctual examples have residual support. The supported quadruple proves that simultaneous singularity and torsion in \(Q\) are not sufficient for a defect. This investigation does not yet decide:

> If \(J=(f,g)\) is a complete intersection with \(\sqrt J=I_C\), \(C\) smooth, and \(\Delta_\eta=0\), can \(\Delta\) be nonzero at isolated points? If so, what is its smallest supported example; if not, which duality or support condition forces vanishing?

This is a strictly narrower question than the unrestricted STCI problem. It retains actual support and all local equations. The family in section 5 must not be used as an answer to it.

The literature already studies the generic tangent-cone generator and cancellation problem; [Mandal–Rossi, The tangent cone of a local ring of codimension 2](https://arxiv.org/abs/1402.2756) is another relevant primary source. No novelty claim is made here. The useful research interface is the precise relative defect, its torsion, and its relation to supported versus residual intersection geometry.



<a id="delta-conormal-annihilator-proposal"></a>
<a id="delta-annihilator-review"></a>

<a id="scheme-theoretic-annihilation"></a>

## A scheme-theoretic annihilator for the filtration defect

Date: 2026-10-24. Status: **proof independently reconstructed by agent review**.

Scope: a regular codimension-two embedding \(C\hookrightarrow P\), locally with ideal \(I=(x,y)\), and any coherent ideal \(J\subset I\). For the intended application \(P\) is a smooth threefold, \(C\) is smooth, and \(J=(f,g)\) defines \(Z=X\cap Y\). Neither \(J\) being a complete intersection nor \(Z_{\mathrm{red}}=C\) is needed for the annihilator theorem. Additional components are allowed. The theorem concerns the marked embedding, without a classification of those components.

### 1. Claim and its intrinsic meaning

Use the merged [comparison framework](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd), with
\[
 B=R/I,\quad S=\operatorname{gr}_I R=\operatorname{Sym}_B E,
 \quad E=I/I^2,\quad H=\operatorname{in}_I(J),
\]
\[
 Q=H/S_+H,\quad
 \Delta=\operatorname{in}_I(IJ)/S_+H,\quad
 \phi:J/IJ\longrightarrow E.
\]
Let \(\mathfrak a\subset B\) be the contraction ideal
\[
 \mathfrak a=\operatorname{im}
 \bigl(E^\vee\otimes_B(J/IJ)\xrightarrow{1\otimes\phi}
 E^\vee\otimes_B E\xrightarrow{\mathrm{ev}}B\bigr).
\]
In local frames it is the ideal of all entries of \(\phi\). Equivalently,
\[
 \mathfrak a=\operatorname{Fitt}_1
 \bigl(I/(I^2+J)\bigr).
\]
The Fitting description uses the rank-two locally free target \(E\), so the subscript is fixed by codimension two.

**Proposition.** In this scope,
\[
 \boxed{\mathfrak a\Delta=0.}
\tag{1}
\]
Consequently \(\Delta\) is canonically a sheaf on the *scheme* cut out by the entries of the conormal map. This strengthens the inherited set-theoretic containment of support in the simultaneous carrier-singular locus. It is not an equality of supports, and it supplies no converse to vanishing.

For two carriers retain the labelled source lines
\(M_X=I_X/I_CI_X\), \(M_Y=I_Y/I_CI_Y\) and their maps
\(\alpha,\beta\) into \(E\). Then \(\mathfrak a\) is the sum of the entry ideals of \(\alpha\) and \(\beta\). This form preserves the whole diagram while showing that the annihilator itself depends only on \(J\subset I\). On a smooth curve in a smooth threefold, a carrier's entries vanish at a point exactly when that carrier is singular there. No claim about reducedness of that singular scheme is made.

### 2. Elementary proof

Degree one has \(\Delta_1=0\), because \(IJ\subset I^2\). Fix \(n\ge2\) and a class in \(\Delta_n\), represented by
\(h\in IJ\cap I^n\). Choose
\[
 h=xc+yd,\qquad c,d\in I^{n-1}.
\]
Since also \(h\in IJ=xJ+yJ\), there are \(u,v\in J\) with \(h=xu+yv\). Exactness of the Koszul complex on the regular sequence \((x,y)\) gives \(w\in R\) with
\[
 c-u=-yw,\qquad d-v=xw.
\tag{2}
\]
Take any equation \(f\in J\), written \(f=xa'+yb'\). Set
\(a=a'\bmod I\), \(b=b'\bmod I\), so its first symbol is
\(f_1=aX+bY\in H_1\), possibly zero. Formula (2) gives the *actual* identity
\[
 a'd-b'c=a'v-b'u+fw\in J\cap I^{n-1}.
\tag{3}
\]
Write \(c^*,d^*\in S_{n-1}\) for their classes modulo \(I^n\), allowing zero classes when their orders are larger. Taking degree \(n-1\) of (3) gives
\[
 \ell=ad^*-bc^*\in H_{n-1}.
\]
The degree-\(n\) initial class of \(h\) is
\(h^*=Xc^*+Yd^*\). Hence
\[
 ah^*=c^*f_1+Y\ell,\qquad
 bh^*=d^*f_1-X\ell.
\tag{4}
\]
Every term on the right belongs to \((S_+H)_n\), since \(n-1\ge1\). Thus \(a,b\) annihilate the class of \(h^*\) in \(Q_n\), and in particular its class in \(\Delta_n\). Varying \(f\) proves (1).

This proof uses the full initial ideal through membership of \(\ell\) in \(H_{n-1}\); it makes no assertion that chosen carrier initials generate \(H\). It also avoids completeness and spectral-sequence convergence assumptions.

At a DVR point where \(\mathfrak a=(t^r)\ne0\), every elementary divisor of every \(\Delta_n\) has exponent at most \(r\). In particular, \(\operatorname{length}_B\Delta_n\le r\,\mu_B(\Delta_n)\). This bounds coefficient thickness, rather than normal degree or generator count. It gives no assertion when \(\mathfrak a=0\).

### 3. Koszul interpretation

In the normal Koszul complex \(K_{R/J}(x,y)\), formula (2) says the cycle represented by \((c,d)\) is an actual boundary. The carrier equation supplies the actual cycle \((a',b')\). Their wedge product is zero because the complex has no degree-three term. Its leading expression is exactly (3).

Under the inherited identification \(Q\simeq\operatorname{Tor}_1^S(S/H,B)\), (4) is the entrywise form of that product vanishing. This explains the special role of normal codimension two. The argument presented here does not assert an unchanged statement in higher codimension.

### 4. Sharpness of the scheme structure

Let \(B=k[[t]]\), \(R=B[[x,y]]\), \(I=(x,y)\), choose \(r\ge1\), set \(a=t^r\), and take
\[
 f=ax+y^2,\qquad g=ay+x^2,\qquad h=xg-yf=x^3-y^3.
\]
The algebraic carriers are distinct integral polynomials: \(f\) is primitive and linear in \(x\) over \(k[t,y]\), because \(t^r\) and \(y^2\) are coprime; symmetrically \(g\) is primitive and linear in \(y\) over \(k[t,x]\). Gauss's lemma proves irreducibility. Distinctness then gives the regular-sequence assertion after localization and completion.

Here
\[
 H=(aX,aY,X^3-Y^3),\qquad
 \operatorname{in}_I(IJ)=(aX^2,aXY,aY^2,X^3-Y^3).
\tag{5}
\]
A standard-basis proof is obtained from the two full symbol syzygies and their exact lifts
\[
 yf-xg+h=0,\qquad -x^2f+y^2g+ah=0.
\]
Modulo \(a\), the monic polynomial \(X^3-Y^3\) is a nonzerodivisor even over the nonreduced coefficient ring \(B/(a)\). Thus the syzygies of the three symbols are generated by
\((Y,-X,0)\) and \((-X^2,Y^2,a)\). Their exact lifts raise the filtered weight whenever a correction is needed; the usual complete filtered correction argument proves (5). The finite samples below separately check the full Rees-saturated ideals.

The conormal map is \(\operatorname{diag}(a,a)\), so its injectivity gives \(F^2(J/IJ)=0\). Therefore
\[
 \Delta_3\simeq B/(t^r),\qquad \Delta_n=0\ (n\ne3),
 \qquad\operatorname{Ann}_B\Delta=(t^r)=\mathfrak a.
\]
For \(r>1\), the reduced ideal \((t)\) does not annihilate \(\Delta\). The full scheme structure of the conormal entry ideal matters. The example illustrates the sharpness of (1); the theorem itself is not inferred from examples. No sole-support hypothesis or conclusion is attached to this family.



<a id="delta-rees-specialization-proposal"></a>
<a id="delta-rees-specialization-review"></a>

<a id="deformation-torsion-and-its-persistence"></a>

## Delta as the specialization of equation-module torsion

Date: 2026-10-24. Status: **proved local arguments independently reconstructed by agent review**.

This note continues the [merged ideal-filtration investigation](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd) and [normal-Koszul continuation](#delta-singular-locus-continuation). It studies the marked embedding \(C\subset Z=X\cap Y\), without imposing \(Z_{\mathrm{red}}=C\). All claims below concern the marked embedding and its deformation; residual components are permitted.

### 1. Exact scope and retained dependencies

Let \(R\) be a noetherian \(k\)-algebra, \(I\subset R\), and \(J\subset I\). Put
\[
B=R/I,\quad S=\operatorname{gr}_I R,\quad H=\operatorname{in}_I J,
\quad D=J/IJ,
\]
\[
F^nD=((J\cap I^n)+IJ)/IJ,\qquad
Q=H/S_+H,\qquad
\Delta=\operatorname{in}_I(IJ)/S_+H.
\]
Set \(I^n=R\) and \(F^nD=D\) for \(n\le0\). The local algebra below does not require smoothness or a complete-intersection hypothesis. For the geometric application, \(R\) is the local ring of a smooth ambient threefold, \(I=I_C\) for a smooth marked curve, and \(J=(f,g)\subset I\) is a regular-sequence ideal. Then \(D\) is locally free of rank two on \(C\).

The inherited comparison \(0\to\Delta_n\to Q_n\to\operatorname{gr}_F^nD\to0\) is used within its reviewed scope. Its predecessor has the proof and review scope stated there. The present note does not use any rational-quartic classification or STCI exclusion. No novelty claim is made for extended Rees modules, conormal specialization, or parameter-torsion removal.

For terminology, the [Stacks normal-cone construction](https://stacks.math.columbia.edu/tag/062Z) defines the normal cone from the full ideal-power algebra, and [conormal functoriality](https://stacks.math.columbia.edu/tag/01R1) supplies the inclusion-induced maps. The statements below are proved directly.

### 2. Keep the deformation, then restrict its conormal module

Introduce a deformation parameter \(u\), independent of parameters on \(C\), and define
\[
\mathscr R=R[u,I/u]
=\bigoplus_{n\in\mathbf Z}I^nu^{-n}
\subset R[u,u^{-1}].
\]
This indexing assigns weight \(n\) to \(I^nu^{-n}\); multiplication by \(u\) lowers weight by one. Define the induced ideal
\[
\mathscr J=\bigoplus_{n\in\mathbf Z}(J\cap I^n)u^{-n}
=J R[u,u^{-1}]\cap\mathscr R.
\tag{1}
\]
The quotient \(\mathscr R/\mathscr J\) is the extended Rees algebra of \(R/J\) for \(K=I/J\). Its fibres are \(R/J\) at \(u=1\), and \(S/H\) at \(u=0\). These are actual algebras, with their maps; the special algebra alone does not reconstruct the former.

There is a canonical zero section
\[
\mathscr R\twoheadrightarrow B[u],\qquad
L=\ker(\mathscr R\to B[u])=(I/u)\mathscr R.
\tag{2}
\]
No splitting \(B\to R/J\) of the canonical quotient, or scheme retraction \(Z\to C\), is assumed: (2) is simply reduction of coefficients modulo \(I\), sending every positive normal generator \(a/u\) to zero. Since \(J\subset I\), one has \(\mathscr J\subset L\). Consequently
\[
\boxed{\mathscr N=\mathscr J/L\mathscr J}
\tag{3}
\]
is the conormal module of the deformed \(Z\) in the deformed ambient space, restricted to \(C\times\mathbf A^1\). Indeed restricting \(\mathscr J/\mathscr J^2\) to this zero section gives exactly (3).

Its fibres are canonically
\[
\mathscr N/(u-1)\mathscr N=D,
\qquad
\mathscr N/u\mathscr N=Q.
\tag{4}
\]
The second equality follows from \(\mathscr J/u\mathscr J=H\), using the induced filtration, and \(L\bmod u=S_+\). Thus \(Q\) really is a special conormal fibre of the actual embedded deformation.

### 3. The intrinsic torsion module whose special fibre is Delta

Define the Rees module of the filtered equation module by
\[
\mathscr D=\bigoplus_{n\in\mathbf Z}F^nD\,u^{-n}
\subset D[u,u^{-1}].
\tag{5}
\]
Taking the class modulo \(IJ\) gives a canonical surjection
\[
\mathscr N\twoheadrightarrow\mathscr D.
\]
This is well defined because \(L\mathscr J\) maps to zero. Its kernel is
\[
\mathscr E=
\frac{\bigoplus_n(IJ\cap I^n)u^{-n}}{L\mathscr J}.
\tag{6}
\]
In coefficient form, these modules are especially explicit:
\[
\mathscr N_n=\frac{J\cap I^n}{I(J\cap I^{n-1})},\qquad
\boxed{\mathscr E_n=\frac{IJ\cap I^n}{I(J\cap I^{n-1})}.}
\tag{7}
\]
To verify the denominator, \(L\) is generated in weight one by \(I/u\). Equivalently, every term \(I^a(J\cap I^{n-a})\), \(a\ge1\), lies in \(I(J\cap I^{n-1})\), and the \(a=1\) term gives equality. Multiplication \(u:\mathscr E_n\to\mathscr E_{n-1}\) is induced by inclusion of the numerators.

**Proposition.** There is a canonical exact sequence of finite graded \(B[u]\)-modules
\[
0\longrightarrow\mathscr E\longrightarrow\mathscr N
\longrightarrow\mathscr D\longrightarrow0,
\tag{8}
\]
where \(\mathscr E\) is exactly the submodule of elements killed by a power of \(u\). Moreover
\[
\boxed{\Delta\simeq\mathscr E/u\mathscr E.}
\tag{9}
\]
In weight \(n\), the denominator in (9) is the image of \(u\mathscr E_{n+1}\).

**Proof.** Surjectivity and the kernel formula follow degree by degree from (5)–(7). The target \(\mathscr D\) embeds in \(D[u,u^{-1}]\), so multiplication by \(u\) is injective. After inverting \(u\), both middle and target modules become \(D[u,u^{-1}]\), and their map is the identity. Thus every kernel element is killed by a power of \(u\), and every such element of \(\mathscr N\) lies in the kernel.

The induced Rees ideal \(\mathscr J\) is a finite ideal of the noetherian ring \(\mathscr R\). Hence \(\mathscr N\), \(\mathscr D\), and \(\mathscr E\) are finite over \(B[u]=\mathscr R/L\). One can also see uniform nilpotence directly: \(\mathscr E_n=0\) for \(n\le1\), while Artin–Rees gives \(J\cap I^n=I(J\cap I^{n-1})\) for large \(n\). Thus only finitely many weights occur in \(\mathscr E\).

Tensor (8) with \(B[u]/(u)=B\). Its possible left obstruction is \(\operatorname{Tor}_1^{B[u]}(\mathscr D,B)\), which is the kernel of multiplication by \(u\) on \(\mathscr D\), hence zero. Since \(\mathscr D/u\mathscr D=\operatorname{gr}_FD\), this gives
\[
0\to\mathscr E/u\mathscr E\to Q\to\operatorname{gr}_FD\to0.
\]
The map sends the symbol of \(j\in J\cap I^n\) to its class in \(F^nD/F^{n+1}D\), exactly the inherited comparison map. Its kernel is \(\Delta\), proving (9). \(\square\)

This identifies the defect intrinsically: it is the special fibre of the parameter-torsion in the restricted conormal module. It is not torsion in the algebra \(\mathscr R/\mathscr J\), which is already parameter-torsionfree.

### 4. What vanishing does and does not say

Uniform \(u\)-nilpotence and (9) imply
\[
\Delta=0\iff\mathscr E=0
\iff\mathscr N\xrightarrow{\sim}\mathscr D.
\tag{10}
\]
For instance \(\mathscr E=u\mathscr E\) would imply \(\mathscr E=u^N\mathscr E=0\) for a sufficiently large \(N\).

Since \(k\) is a field, this is also equivalent to **flatness over the deformation parameter**:
\[
\boxed{\Delta=0\iff\mathscr N\text{ is flat over }k[u].}
\tag{11}
\]
Indeed (10) makes \(\mathscr N\) a submodule of \(D[u,u^{-1}]\), which is torsionfree over the PID \(k[u]\); torsionfree modules over this PID are flat. Conversely a \(k[u]\)-flat module has no \(u\)-torsion. Equivalently, any polynomial torsion in \(\mathscr N\) must already be \(u\)-power torsion, since its localization away from \(u\) is \(D[u,u^{-1}]\).

**This is not a statement of flatness over \(B[u]\).** Filtration pieces on the curve may fail to be saturated even when \(D\) is locally free and \(\Delta=0\). The supported quadruple in the predecessor has precisely this behaviour: its associated filtered pieces retain torsion on the curve. Thus there are separate directions of variation, the deformation parameter and the marked-curve parameter; they must not be merged into a single flatness assertion.

Likewise \(\Delta=0\) does not imply that the original embedding is determined by its associated graded algebra, or that its normal cone is a complete intersection, or that the carrier normal cones meet scheme-theoretically in that normal cone.

### 5. Preserve the carrier maps: a distinct saturation defect

Write \(A=I_X\), \(B_Y=I_Y\), so \(J=A+B_Y\). The different notation \(B_Y\) avoids confusing the carrier ideal with the base ring \(B=R/I\). Form their induced Rees ideals \(\mathscr A\), \(\mathscr B_Y\) by (1). All inclusions and quotient maps remain:
\[
C\times\mathbf A^1\subset\mathscr Z\subset
\mathscr X,\mathscr Y\subset\mathscr P.
\]
The two routes through the carriers commute with the direct embeddings. However, the original Cartesian square need not remain Cartesian at the special fibre:
\[
\boxed{\mathscr J=(\mathscr A+\mathscr B_Y):u^{\infty}.}
\tag{12}
\]
The right side is the contraction after inverting \(u\), where the sum is simply \(J R[u,u^{-1}]\). This proves (12). Thus \(\mathscr Z\) is the flat closure of the generic carrier intersection, and maps as a closed subscheme to \(\mathscr X\times_{\mathscr P}\mathscr Y\). Their difference is measured by
\[
\mathscr V=\mathscr J/(\mathscr A+\mathscr B_Y),
\tag{13}
\]
not by \(\Delta\). In particular, \(\mathscr V\) is parameter torsion of the carrier-intersection algebra; \(\mathscr E\) is parameter torsion of a restricted conormal module for the already saturated \(\mathscr Z\).

An elementary distinction is \(J=(x,x+y^m)=(x,y^m)\), \(m\ge2\), with \(I=(x,y)\). Both displayed carriers are smooth. In normal coordinates \(X=x/u,Y=y/u\), their deformed intersection has ideal
\[
(X,X+u^{m-1}Y^m)=(X,u^{m-1}Y^m),
\]
whose saturation is \((X,Y^m)\). The carrier cone intersection at \(u=0\) has ideal \((X)\), while the actual normal cone has ideal \((X,Y^m)\). Nonetheless \(\mathscr N\) is freely generated over \(B[u]\) by the classes of \(X,Y^m\), so \(\Delta=0\). Carrier-intersection saturation and conormal specialization therefore measure different failures.

These vertical features belong to the deformation and do not by themselves establish an extra component of the original \(Z\).

### 6. The torsion duration refines Delta: an exact family

Work locally with \(R=B[x,y]_{(\mathfrak m_B,x,y)}\), where \(B=k[t]_{(t)}\), and set
\[
I=(x,y),\qquad J=(x^a+y^b,xy),\qquad 2\le a<b.
\tag{14}
\]
Its quotient is free over \(B\) with basis
\[
1,x,\ldots,x^{a-1},y,\ldots,y^b,
\]
using \(xy=0\), \(x^a=-y^b\), and \(y^{b+1}=0\). The ideal is a regular-sequence ideal and is supported on the marked curve in this local neighbourhood. The example is used only to examine the invariant; no support condition is imposed in the general theorems.

Put \(r=b-a>0\). In deformation coordinates, the full induced Rees ideal is
\[
\mathscr J=(F,G,T),\quad
F=X^a+u^rY^b,\quad G=XY,\quad T=Y^{b+1}.
\tag{15}
\]
To see fullness, this ideal has the correct localization at \(u\), and its quotient is free over \(B[u]\) on the analogous displayed basis. The reduction rules \(X^a=-u^rY^b,XY=0,Y^{b+1}=0\) are compatible: their only nontrivial overlap is \(YF-X^{a-1}G=u^rT\). Hence the ideal is \(u\)-saturated and is exactly (1).

All syzygies of the three generators are generated by
\[
(Y,-X^{a-1},-u^r),\qquad (0,Y^b,-X).
\tag{16}
\]
Here is a direct completeness check. In a relation \(A_0F+B_0G+C_0T=0\), reduction modulo \(Y\) forces \(A_0\) to be divisible by \(Y\). Subtracting that multiple of the first relation eliminates its \(F\)-coefficient. Dividing the resulting relation by \(Y\) leaves \(X B_1+Y^b C_1=0\), and the regular polynomial pair \(X,Y^b\) gives the second relation. Localization preserves the presentation.

Modulo \(L=(X,Y)\), (16) gives just \(u^r[T]=0\). Therefore
\[
\boxed{\mathscr N\simeq
B[u]\,e_F\oplus B[u]\,e_G\oplus
\bigl(B[u]/(u^{b-a})\bigr)e_T,}
\tag{17}
\]
with weights \(a,2,b+1\), respectively. Thus
\[
\mathscr E\simeq(B[u]/(u^{b-a}))e_T,
\qquad
\boxed{\Delta\simeq B e_T\text{ in weight }b+1.}
\tag{18}
\]
For fixed \(b\), varying \(a\in\{2,\ldots,b-1\}\) leaves this graded defect unchanged but changes the parameter-torsion exponent \(b-a\). The full equation module also records the surviving weights \(a,2\); the claim of unchanged data concerns \(\Delta\), not all filtered invariants.

This duration matches the normal-Koszul cancellation weight gap: the relation \(YF-X^{a-1}G\) has source weight \(a+1\), the killed equation has weight \(b+1\), and their gap is \(b-a\). Here the explicit calculation establishes the match; no general classification of all relative torsion modules by spectral-sequence pages is claimed.

If integral algebraic carriers are desired, the same local ideal is realized by
\[
\widetilde f=x^a+y^b+t y^{b+1},\qquad
\widetilde g=\widetilde f+xy.
\tag{19}
\]
Both are primitive linear polynomials in \(t\), with relatively prime coefficient \(y^{b+1}\) and constant coefficient, hence irreducible in \(k[t,x,y]\). They are distinct. Since
\(y\widetilde f-x^{a-1}xy=y^{b+1}(1+ty)\), and \(1+ty\) is a unit at the origin, their localized ideal contains \(y^{b+1}\), then \(x^a+y^b\). Conversely \(y^{b+1}\) already belongs to the model ideal in (14). Thus the ideals agree locally. This is a local marked-line realization, not a new global projective pair for the fixed rational quartic.

### 7. Consequences, limits, and next questions

The geometric meaning is now precise: \(\Delta\) detects the failure of the conormal module, restricted to the fixed marked curve, to vary flatly in deformation to the normal cone. The flat algebra of the embedded deformation and all carrier maps remain necessary context. The module \(\mathscr E\), not merely its special fibre \(\Delta\), additionally records how long a spurious special conormal equation persists under the deformation parameter.

Promising questions are therefore intrinsic and separate:

1. Determine the \(u\)-power filtration of \(\mathscr E\) as sheaves on \(C\), and its precise relation to the incoming normal-Koszul differential filtration already identified in the predecessor. Over a transverse field one has elementary-divisor blocks; over \(\mathcal O_C[u]\) there need not be a compatible splitting.
2. Study curve-parameter base change of the exact sequence (8). Formation of \(\Delta\) can fail to commute with specialization on \(C\); this should be expressed using explicit Tor terms rather than inferred from deformation-parameter flatness.
3. Compare the distinct modules \(\mathscr V\) and \(\mathscr E\) while preserving the carrier source lines and all conormal maps. The smooth-carrier example proves that one cannot replace either invariant by the other.
4. Investigate local freeness of \(\mathscr N\) over \(\mathcal O_C[u]\), which is stronger than \(\Delta=0\), and identify the additional saturation conditions on the filtered equation bundle that it requires.

No assertion here reconstructs \(Z\) from \(\Delta\), determines unmarked components, or resolves unrestricted STCI. The core advance is an exact intrinsic interpretation of the existing invariant and a finer module that retains deformation duration.


The annihilator also controls persistence: since a*Delta=0 and Delta=E/uE, one has a*E subset uE. If u^N E=0 locally, iteration gives a^N E=0. This does not assert aE=0; the full persistence module can require a larger exponent than its special fiber. The exponent is local unless a uniform one has been chosen.


<a id="delta-normal-geometry-proposal"></a>

## Delta, normal-cone regularity, and the labelled carrier square

Date: 2026-10-24. Status: **research with an independent agent reconstruction**.

### Scope and retained inputs

Let \(p\) be a closed point of a smooth integral curve \(C\) in a smooth threefold \(P\), over a field of arbitrary characteristic. Put \(R=\mathcal O_{P,p}\), \(B=\mathcal O_{C,p}\), \(I=I_C\), and \(J=(f,g)\subset I\), where \(f,g\) form a regular sequence. The labelled principal ideals \(A=(f), B_Y=(g)\) are retained; the letter \(B\) denotes the curve ring, not the second carrier ideal. There is **no assumption** that \(\sqrt J=I\). All statements concern the marked embedding, not classification of any additional components. The examples are local algebraic examples, not constructions for the fixed projective rational quartic.

Use the reviewed comparison from [the merged investigation, section 4](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd):
\[
S=\operatorname{gr}_I R=\operatorname{Sym}_B(I/I^2),\quad
H=\operatorname{in}_I J,\quad Q=H/S_+H,\quad D=J/IJ\simeq B^2,
\]
\[
F^nD=((J\cap I^n)+IJ)/IJ,\quad
0\longrightarrow\Delta_n\longrightarrow Q_n\longrightarrow G_n\longrightarrow0,
\qquad G_n=F^nD/F^{n+1}D. \tag{1}
\]
The [continuation](#delta-singular-locus-continuation) is the source for the generic generator count and the supported quadruple used below. Those inherited proofs and scripts are not replayed here. The standard definition of regular immersion is recalled in [Stacks, regular immersions](https://stacks.math.columbia.edu/tag/0638).

### 1. Two separate obstructions to regularity of the normal-cone embedding

Write \(\mathfrak n=(\mathfrak m_B,S_+)\). The following conditions are equivalent:

1. \(C_{C/Z}=\operatorname{Spec}(S/H)\hookrightarrow N_{C/P}=\operatorname{Spec}S\) is a regular immersion on a neighborhood of the zero section over \(p\).
2. \(Q\) is a free \(B\)-module of rank two.
3. \(\Delta=0\), and every \(G_n\) is \(B\)-torsion-free.
4. \(\Delta=0\), and every \(F^nD\) is saturated in \(D\), meaning that \(D/F^nD\) is torsion-free.

This is a criterion for the **embedding of the normal cone in the ambient normal bundle**. It is neither a flatness criterion for the cone over \(C\) nor a regular-immersion criterion for \(C\hookrightarrow Z\).

**Proof.** The associated graded dimension theorem for a proper ideal in a noetherian local ring gives
\[
\dim\operatorname{gr}_{I/J}(R/J)=\dim(R/J)=1.
\]
Consequently \(H_{\mathfrak n}\) has height two in the regular local ring \(S_{\mathfrak n}\) of dimension three. This dimension input is essential: the abstract homogeneous ideal \((tX,tY)\subset B[X,Y]\) has \(Q\simeq B^2\) but height one, and cannot be substituted for the full initial ideal in this argument.

Moreover
\[
Q/\mathfrak m_BQ\simeq H_{\mathfrak n}/\mathfrak nH_{\mathfrak n}.
\]
If the immersion is regular near the zero section, this vector space has dimension two. Choose two homogeneous lifts \(h_1,h_2\in H\) of a minimal generating set. Nakayama over \(B\), followed by graded Nakayama over \(S\), shows \(H=(h_1,h_2)\). A height-two ideal generated by two elements in a regular ring is a regular sequence. Its syzygies are generated by \((-h_2,h_1)\). Since \(h_i\in S_+\), reducing the presentation modulo \(S_+\) gives
\[
Q\simeq B(-a)\oplus B(-b),\qquad a=\deg h_1,\ b=\deg h_2.
\]
Conversely, a homogeneous basis of a free rank-two \(Q\) lifts by graded Nakayama to two generators of \(H\), which form a regular sequence by the same height argument. This proves 1 \(\Longleftrightarrow\) 2.

At the generic point of \(C\), \(J\) becomes primary to the transverse maximal ideal: a prime contained in the height-two prime \(I\) and containing the height-two regular-sequence ideal \(J\) must be \(I\) itself. The finite filtration of \(D_\eta\simeq k(C)^2\) therefore has total graded dimension two. If \(Q\) is free of rank two, summing (1) gives \(\Delta_\eta=0\). Hence \(\Delta\) is torsion; its inclusion in the torsion-free module \(Q\) forces \(\Delta=0\). Now (1) identifies each \(G_n\) with \(Q_n\), so all are free. Conversely, condition 3 identifies \(Q\) with a direct sum of free graded pieces; their total generic rank is two. Finally, for a finite filtration of a finite free module over a DVR, all successive quotients are torsion-free if and only if every filtration stage is saturated. For the forward direction build the quotients \(D/F^nD\) successively by extensions of free modules. For the reverse direction \(G_n\) is a submodule of the free module \(D/F^{n+1}D\). This proves all equivalences. \(\square\)

The local statement sheafifies on a smooth curve. The filtration and its quotients are intrinsic; no preferred splitting of \(D\), or of its filtration, is asserted. In particular, \(\Delta=0\) leaves a separate possible failure: initial equation classes can be retained in \(G_n\) as torsion arising from nonsaturated filtration stages.

### 2. The labelled carrier square has a stronger condition

Let \(f^*,g^*\in S\) denote the first nonzero normal symbols of the **original labelled equations**. Since \(S\) is a domain, normal order is additive on nonzero products, so
\[
\operatorname{in}_I(A)=(f^*),\qquad
\operatorname{in}_I(B_Y)=(g^*).
\]
There is a natural diagram
\[
C_{C/Z}\longrightarrow C_{C/X},\ C_{C/Y}\longrightarrow N_{C/P}.
\]
Its scheme-theoretic fibre product has coordinate algebra \(S/(f^*,g^*)\), and the actual normal cone has algebra \(S/H\). Thus the natural inclusion is measured by the exact sequence
\[
0\longrightarrow H/(f^*,g^*)\longrightarrow S/(f^*,g^*)
\longrightarrow S/H\longrightarrow0. \tag{2}
\]
The normal-cone square is Cartesian if and only if \(H=(f^*,g^*)\), which holds if and only if \(f^*,g^*\) form a regular sequence in \(S\).

For sufficiency, take \(j=uf+vg\). If the lowest weighted terms of the two summands cancel, their coefficients form a homogeneous syzygy of \(f^*,g^*\). Regularity makes it a Koszul syzygy. Lift its multiplier and modify \((u,v)\) by an actual multiple of \((g,-f)\); this leaves \(j\) unchanged and strictly raises the canceled weighted order. Only finitely many such steps are needed to reach the fixed normal order of nonzero \(j\). Its symbol is therefore in \((f^*,g^*)\). Necessity follows from height two. This is the elementary two-generator standard-basis argument; it does not require a choice of formal splitting of the ambient ring.

The condition in (2) retains the maps through both carriers and is stronger than regularity of \(C_{C/Z}\hookrightarrow N_{C/P}\). It differs from \(\Delta\): (2) compares the **two labelled principal carrier ideals with their sum**, whereas \(\Delta\) compares **the full initial ideal with the intrinsic filtered equation module**. Changing \((f,g)\) by a generator transformation preserves \(J,D,F,\Delta\), but can change the labelled carrier ideals and the quotient in (2).

For example, for \(m\ge2\),
\[
f=x,\qquad g=x+y^m,\qquad I=(x,y),\qquad J=(x,y^m),
\]
both labelled carriers are smooth and integral. The full initial ideal is \(H=(X,Y^m)\), with
\[
Q=B(-1)\oplus B(-m),\quad \Delta=0,\quad
F^2D=\cdots=F^mD=B(e_g-e_f),\quad F^{m+1}D=0.
\]
But \((f^*,g^*)=(X)\), and the carrier normal cones intersect in a line bundle, larger than the actual normal cone. Replacing \(g\) by \(g-f=y^m\) adapts the generators but changes the labelled carrier; it must not be used to declare the original normal-cone square Cartesian.

### 3. Two geometric distinctions that Delta alone cannot settle

First, take two smooth integral algebraic carriers
\[
f=y,\qquad g=y+tx,\qquad I=(x,y),\qquad J=(y,tx).
\]
Here
\[
H=(Y,tX),\quad Q=B(-1)^2,\quad F^2D=0,\quad\Delta=0.
\]
The first conormal map has columns \(Y\) and \(Y+tX\); it is injective with cokernel \(B/(t)\). The cone embedding is a regular immersion, while
\[
S/H\simeq B[X]/(tX)
\]
has \(t\)-torsion and is not flat over \(B\). This example is permitted by the marked-embedding scope. No component-classification objective is attached to it.

Second, the inherited supported quadruple
\[
J=(x^2,y^2+tx),\quad
H=(tX,X^2,XY^2,Y^4)
\]
has \(\Delta=0\), but \(Q_2\simeq Q_3\simeq B/(t)\). These torsion classes survive in \(G_2,G_3\). The normal-cone embedding is therefore not a regular immersion. This is exactly the additional filtration-saturation obstruction in section 1, and the example does not require residual support.

Finally, regularity of \(C\hookrightarrow Z\) itself is much stronger: it is equivalent to \(C=Z\) locally at \(p\). Indeed, both local rings have dimension one and \(R/J\) is Cohen–Macaulay; a regular sequence cutting out \(C\) in \(Z\) must have length zero. Equivalently, the central conormal map \(D\to I/I^2\) is surjective; Nakayama applied to \(I/J\) then gives \(I=J\). A regular normal-cone embedding can coexist with an arbitrarily thick marked curve.

### 4. Next directions and evidence boundary

The full embedding framework now separates three questions: whether degeneration preserves the labelled carrier fibre product; whether the actual normal cone is regularly embedded in the ambient normal bundle; and whether its structural map to the marked curve is flat. Formula (2), the two conditions in section 1, and \(B\)-torsion of \(S/H\) address these respectively. Their distinctions should be retained in future examples and global constructions.

The most useful next local question is how the nonsaturated stages \(F^nD\) interact with the algebra filtration of \(\mathcal O_Z\), especially when \(\Delta\) vanishes. A second question is to identify global bundle/extension data obstructing locally adapted normal equations from coming from the original global carriers. Neither question is resolved by the local criteria here.

Independent audit: agent `geometry_maps/audit_cone_criterion` independently reconstructed all four equivalences, the labelled-square criterion, both elementary examples, and the distinction between regular cone embedding and flatness over \(C\). It specifically checked the homogeneous local Nakayama step and flagged the essential height-two input. This is an agent proof audit, not external acceptance. No new finite computation is needed for the general proofs; the supported quadruple is inherited evidence, not a newly replayed calculation. No result/question record or accepted proof is changed.

<a id="delta-base-change-proposal"></a>

## Delta, transverse specialization, and normal flatness

Date: 2026-10-24. Status: **proved local algebra with independent agent reconstruction; research evidence**.

This develops a distinction needed in the broader marked-embedding problem: vanishing of the ideal-filtration defect is different from compatibility of the normal cone with a transverse slice. No hypothesis that the reduced support of the intersection equals the marked curve is imposed.

### 1. Scope, retained data, and dependencies

Locally let the smooth marked curve have ideal `I=(x,y)` in a smooth threefold. Choose a lift `t` of a parameter on the curve and a local coefficient algebra `B=k[[t]]`; in formal coordinates `R=B[[x,y]]`. Put
\[
J=(f,g)\subset I,\quad M=R/J,\quad K=IM,\quad
S=\operatorname{gr}_I R=B[X,Y],\quad
H=\operatorname{in}_I J,\quad T=\operatorname{in}_I(IJ),
\]
\[
A=\operatorname{gr}_K M=S/H,\quad
\mathcal D=J/IJ,\quad G=\operatorname{gr}_F\mathcal D=H/T,
\quad Q=H/S_+H,\quad\Delta=T/S_+H.
\]
The exact comparison `0 -> Delta -> Q -> G -> 0` and the smooth-carrier vanishing statement are retained reviewed premises from the [original investigation](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd). The statements retain the review scopes stated here. The [continuation](#delta-singular-locus-continuation), sections 5 and 7, supplies the inherited punctual family and supported quadruple used below. Their previously reviewed computations are not rerun here.

The parameter lift is additional data for an actual transverse slice. The cone `Spec_C A` is intrinsic to `C subset Z`; the transverse slice `M/tM` need not be independent of that lift. All assertions comparing with the slice use the specified `B`-algebra structure.

The carrier ideals `(f),(g)`, the quotient `R/J`, the source lines in `J/IJ`, and all maps of the nine-embedding diagram are retained. None is reconstructed from `Delta`. The construction below applies functorially to every compatible ideal-power filtration in that diagram; one uses the actual ambient quotient and its induced ideal for each arrow.

### 2. An exact measure of failure of normal-cone specialization

The next proposition needs neither a complete-intersection assumption nor a support assumption.

**Proposition 1.** Let `B` be a DVR with uniformizer `t` and residue field `k`, let `M` be a noetherian `B`-algebra, and let `K` be an ideal. Set
\[
N_n=M/K^n,\quad A_n=K^n/K^{n+1},\quad
U_n=\operatorname{Tor}_1^B(N_n,k),\quad \bar M=M/tM.
\]
Let `bar K` be the image of `K` in `bar M`. There is a natural exact sequence
\[
U_{n+1}\longrightarrow U_n\longrightarrow
A_n\otimes_B k\xrightarrow{\gamma_n}
\operatorname{gr}_{\bar K}^n\bar M\longrightarrow0.
\tag{1}
\]
Consequently the kernel of `gamma_n` is canonically
\[
E_n=\operatorname{coker}(U_{n+1}\longrightarrow U_n).
\tag{2}
\]
The kernels together form the graded ideal of the closed immersion from the actual slice cone into the fibre of the relative cone.

**Proof.** Tensor the short exact sequence
\[
0\longrightarrow A_n\longrightarrow N_{n+1}
\longrightarrow N_n\longrightarrow0
\]
with `k`. The image of `A_n tensor k` in `N_{n+1} tensor k` is
\[
\frac{K^n+tM}{K^{n+1}+tM}
=\operatorname{gr}_{\bar K}^n\bar M.
\]
The Tor exact sequence gives (1). The maps are the ordinary multiplication-compatible maps of associated graded algebras, so their kernels form a graded ideal. All constructions are natural for compatible maps of filtered algebras. This proves (2) and the diagram compatibility.

If multiplication by `t` on `M` is injective, the same kernel has the concrete form
\[
E_n=
\frac{(K^n\cap tM)+K^{n+1}}
 {tK^n+K^{n+1}}.
\tag{3}
\]
Under `U_n=(K^n:t)/K^n`, the connecting homomorphism sends the class of `m`, with `tm in K^n`, to the class of `tm` in `A_n tensor k`. Thus `E_n` records torsion in a neighborhood that cannot be lifted to the next neighborhood. It is not simply the torsion of `A_n`.

### 3. All degrees detect normal flatness

**Proposition 2.** In Proposition 1 assume that `t` is a nonzerodivisor on `M` and `M/K=B`. The following are equivalent:

1. `gamma_n` is an isomorphism for every `n`.
2. Every `M/K^n` is `B`-flat.
3. Every `A_n` is `B`-flat.
4. Every power `K^n` is saturated with respect to `t`: `(K^n:t)=K^n`.

Condition 3 says that the normal cone is flat over the marked curve. This is the classical normal-flatness condition, not a novelty claim. The exact torsion diagnostic (1) is the useful interface with the retained neighborhood tower.

**Proof.** Conditions 2 and 4 are equivalent because a module over a DVR is flat exactly when it is torsion free. Conditions 2 and 3 are equivalent by successive extensions, starting from `M/K=B`, and by the fact that `A_n` is a submodule of `M/K^{n+1}`. Condition 2 implies 1 directly from (1).

For the converse, (1) makes every map `U_{n+1}->U_n` surjective. Artin--Rees applied to `tM subset M` gives a constant `c` such that
\[
tM\cap K^{n+c}\subset tK^n.
\]
The map `U_{n+c}->U_n` is zero: a representative `m` satisfies `tm in K^{n+c}`, hence `tm in tK^n`, so cancellation of `t` gives `m in K^n`. This same map is surjective as a composite of adjacent transition maps. Therefore `U_n=0` for every `n`, proving 2. Completeness is not needed for this argument.

The quantifier over all degrees is essential. In the inherited punctual family of continuation section 5, `A_1=(B/t^r)^2`, yet its degree-one slice comparison is an isomorphism `k^2 -> k^2`.

The standard conormal-algebra construction and functorial maps are recorded in [Stacks, normal cones](https://stacks.math.columbia.edu/tag/062Z). Normal flatness and the relation between normal cones and tangent cones of fibres are classical themes of [Lejeune-Jalabert--Teissier, *Normal cones and sheaves of relative jets*, 1974](https://www.numdam.org/item/CM_1974__28_3_305_0.pdf). The proof above is direct and does not use their more general theorems as a dependency.

### 4. A sufficient criterion for Delta to commute with the slice

Return to the smooth marked curve and the two-generator regular-sequence ideal of section 1. The two normal algebras involved are
\[
A=S/H=\operatorname{gr}_I(R/J),\qquad
A'=S/T=\operatorname{gr}_I(R/IJ).
\tag{4}
\]
The second is essential: the defect compares `J` with `IJ`, so considering only the normal cone of `Z` omits half the comparison.

**Proposition 3.** Assume `R/J` is `B`-flat. If both `A` and `G=gr_F(J/IJ)` are `B`-flat in every degree, then the full initial ideals `H,T`, and the modules `Q,G,Delta`, commute with the specified slice. In particular
\[
\Delta\otimes_Bk\simeq\Delta_{\mathrm{actual\ slice}}.
\tag{5}
\]
Equivalently, the sufficient hypothesis is normal flatness of both algebras in (4).

**Proof.** The module `D=J/IJ` is free of rank two over `B` because `J` is a regular-sequence ideal contained in `I`. The sequence
\[
0\longrightarrow D\longrightarrow R/IJ
\longrightarrow R/J\longrightarrow0
\]
therefore makes `R/IJ` flat over `B`. Degreewise there is another exact sequence
\[
0\longrightarrow G_n\longrightarrow A'_n\longrightarrow A_n\longrightarrow0.
\tag{6}
\]
Thus flatness of `A,G` implies flatness of `A'`; conversely flatness of `A,A'` implies flatness of `G`, which is a submodule of the flat module `A'` over a DVR.

The induced filtration on `D subset R/IJ` is exactly `F^nD=D cap I^n(R/IJ)`, and the quotient map to `R/J` is strict. This verifies (6), including its left exactness. Also `t`-regularity on `R/J` gives `J cap tR=tJ`, hence `D tensor k=bar J/(bar I bar J)`. Since `(f,g,t)` is a regular sequence in the regular local ring, permutation shows that the sliced pair `(bar f,bar g)` is still a regular sequence. Thus the object on the right of (5) is the same complete-intersection comparison for the actual slice.

Proposition 2 applied to `R/J` and `R/IJ` now shows that their normal algebras commute with the slice. Since the ambient `S_n` and the quotient algebras `A_n,A'_n` are flat, the kernels `H_n,T_n` commute with the slice as well. The initial ideal for the sliced `IJ` is the full initial ideal of `bar I bar J`, because ordinary products commute with passage to the quotient. Finally tensoring the cokernel descriptions
\[
Q=H/S_+H,\quad G=H/T,\quad\Delta=T/S_+H
\]
is right exact, and the images of the multiplication maps become exactly `bar S_+ bar H`. This gives all asserted identifications, including (5).

These are sufficient conditions for `Delta`, not necessary ones. The supported example below has `Delta=0` in both relative and sliced settings, although its first normal algebra is not flat.

### 5. Two sharp distinctions

#### 5.1 Zero Delta does not imply compatibility of normal cones

Use the inherited supported quadruple
\[
J=(x^2,y^2+tx),\quad I=(x,y),\quad
H=(tX,X^2,XY^2,Y^4).
\]
The continuation proves `Delta=0`. Nevertheless
\[
A\otimes_B k=k[X,Y]/(X^2,XY^2,Y^4),
\qquad
\operatorname{gr}_{\bar K}(M/tM)=k[X,Y]/(X^2,Y^2).
\]
The specialization kills `Y^2` in degree two and `Y^3` in degree three. Hence `E_2=E_3=k`, with all other `E_n=0`. The actual intersection is finite flat over the curve and supported on it; even here, absence of ideal-filtration cancellation does not establish normal flatness. The two measurements answer different questions.

#### 5.2 Flatness of the actual algebra is a genuine hypothesis

In `R=k[[t,x,y]]`, take
\[
I=(x,y),\qquad f=x,\qquad g=ty+x^2,
\qquad J=(x,ty).
\]
The carrier polynomials `x` and `ty+x^2` are distinct and integral in `k[t,x,y]`: the latter is primitive and linear in `t`, with coprime coefficients `y,x^2`. They form a regular sequence. The central first conormal matrix, in the source frames `(e_f,e_g)` and target frames `(X,Y)`, is
\[
\phi=\begin{pmatrix}1&0\\0&t\end{pmatrix}.
\]
The actual quotient and its normal algebra are
\[
M=B[[y]]/(ty),\qquad A=B[X,Y]/(X,tY).
\]
The ideal `J` is homogeneous for the normal grading, so its full initial ideal is exactly `(X,tY)`. Also
\[
\operatorname{in}_I(IJ)=(X^2,XY,tY^2)=S_+H,
\]
and `Delta=0`. Yet `A_n=B/(t)` for every `n>=1`, so the cone is not flat over `B`. Every slice comparison is an isomorphism: both graded algebras are `k[Y]`. Multiplication by `t` on `M` is not injective. This explicitly rules out dropping that hypothesis in Proposition 2, even with integral carriers and a smooth marked curve.

This example is used only to identify the necessary flatness hypothesis. Its additional support is permitted by the investigation's scope and is not a separate classification objective.

### 6. In this codimension-two setting, normal flatness of A already suffices

The additional condition on `G` in Proposition 3 can be removed for the actual two-generator complete intersection along the smooth marked curve. The following lemma identifies why the rank-two equation module is unusually rigid.

**Lemma 4 (the two lowest initial-equation degrees).** Let `(V,m,L)` be an equicharacteristic regular local ring of dimension two, and let `J_0 subset m` be a two-generator regular-sequence ideal. Let `H_0=in_m J_0` in `L[X,Y]`. The two weights `a<=b` of the filtered vector space `D_0=J_0/mJ_0` are exactly the two lowest degrees, counted with multiplicity, of a minimal homogeneous generating set of `H_0`. Both weights are determined by the Hilbert function of `L[X,Y]/H_0`.

**Proof.** The finite filtration on `D_0` admits an adapted basis. Choose lifts `f,g` of its two basis classes, of orders `a<=b`; Nakayama makes them generators of `J_0`. Every element of `J_0` has order at least `a`, and the initials in degree `a` have dimension one or two. If `a=b`, they are independent: a constant leading relation would produce a nonzero class in `F^{a+1}D_0`, contrary to adaptation.

Suppose `a<b`. For any `n<b`, an expression `c f+d g` with order `n` has initial a multiple of `in f`, since `d g` has order at least `b`. At degree `b`, the initial of `g` is not a multiple of `in f`. If it were `u in f` for a homogeneous polynomial `u` of degree `b-a>0`, lifting `u` and replacing `g` by `g-u f` would raise the order of the same nonzero class of `D_0` beyond `b`, again contradicting adaptation. Thus the first two minimal-generator degrees of `H_0` are `a,b`, with no intervening minimal equation. All other minimal equations have larger degree.

For the Hilbert-function assertion, `a` is the first degree with `H_{0,a}!=0`. If `dim_L H_{0,a}=2`, then `b=a`. Otherwise, multiplication by the single nonzero degree-`a` initial equation is injective in the polynomial ring, and gives `dim_L H_{0,n}=n-a+1` for `a<=n<b`. Hence `b` is the first degree with
\[
\dim_L H_{0,b}>b-a+1.
\]
These dimensions are obtained by subtracting the quotient Hilbert function from `dim L[X,Y]_n=n+1`. This proves the lemma.

**Proposition 5.** In the formal smooth-curve setting of section 1, if `A=gr_I(R/J)` is flat over `B` in every degree, then `G=gr_F(J/IJ)` is flat over `B` in every degree. Consequently normal flatness of `C_{C/Z}` alone suffices for all the base-change conclusions of Proposition 3.

**Proof.** First `t` is a nonzerodivisor on `M=R/J`. Indeed the `K`-adic filtration is separated by Krull intersection. A nonzero element killed by `t` would have a nonzero initial class in some `A_n`, also killed by `t`, contradicting flatness. Thus `M` is `B`-flat. The exact sequences `0 -> A_n -> M/K^{n+1} -> M/K^n -> 0`, starting with `M/K=B`, show that every `M/K^n` is `B`-flat.

It follows that reduction modulo `t` is strict on the filtered ideal `J`:
\[
J\cap I^n\longrightarrow \bar J\cap\bar I^n
\quad\text{is surjective for every }n.
\tag{7}
\]
To see this directly, lift an element on the right to `h in J`. Since it lies in `bar I^n`, write `h=i+t r` with `i in I^n`. In `M`, `t[r]` lies in `K^n`. Flatness of `M/K^n` makes `K^n` saturated, so `[r] in K^n`; write `r=i'+j'` with `i' in I^n,j' in J`. Then `h-tj'` belongs to `J cap I^n` and has the required reduction. Since `D tensor k=bar J/(bar I bar J)`, (7) gives
\[
\operatorname{image}(F^nD\longrightarrow D\otimes_Bk)
=F^n\bar D.
\tag{8}
\]

Each `A_n` is a finite free `B`-module, so the generic and special transverse initial algebras have the same Hilbert function. Flat specialization identifies the latter with the actual sliced initial algebra. Both actual transverse ideals are two-generator complete intersections: the generic one follows by flat localization/completion at the generic point of `C`; the special one follows from `t`-regularity on `R/J`. Lemma 4 therefore gives the same two filtered equation-module weights in the generic and special fibres. In particular
\[
\operatorname{rank}_B F^nD
=\dim_k F^n\bar D\qquad\text{for every }n.
\tag{9}
\]

Now `F^nD` is a finite free submodule of `D=B^2`. Its image modulo `t` has, by (8)--(9), the same dimension as its rank. Smith normal form therefore has only unit invariant factors for the inclusion `F^nD subset D`; the submodule is saturated and a direct summand. Every quotient `F^nD/F^{n+1}D` is consequently torsion free over `B`, hence flat. This is precisely the assertion about `G`. Proposition 3 supplies the remaining base-change identifications.

**Geometric limitation.** Normal flatness is a strong conditional locus in the broader investigation. Since `Z` is a pure one-dimensional complete intersection and `C` is a component, the generic transverse algebra is artinian. Thus `A_n` has generic rank zero for large `n`. Flatness makes those finite modules zero; hence `K^N=K^{N+1}` for some `N`, and Nakayama gives `K^N=0`. Therefore normal flatness itself forces the local reduced support to be `C`. This is a conclusion under the additional flatness hypothesis, not an imposed support assumption. Points where further components meet `C` remain covered by Proposition 1, rather than by this normal-flat specialization corollary.

### 7. Consequences and next questions

The useful invariants now separate three geometric issues while retaining their maps:

- `Delta` measures minimal normal equations lost on passage to the filtered equation module.
- `E_n` measures failure of the relative normal cone to agree with the cone of the specified actual transverse slice.
- The tower `M/K^n`, and the corresponding tower for `R/IJ`, records the saturation/flatness information required to compare them.

Proposition 5 settles the focused question whether normal flatness of `C_{C/Z}` alone forces the required flatness of `G` for the two-generator complete intersection: it does. It does not prove that `Q` or `Delta` are flat, or that they vanish. A remaining useful question is whether they can have punctual torsion even on this normal-flat locus; the flat quotient `G` would then force all torsion of `Q` into `Delta`. For points outside that locus, a promising invariant is the joint profile of the two specialization kernels for `R/J` and `R/IJ`; it should explain precisely how the defect changes when one normal algebra specializes strictly and the other does not.

No statement here identifies the filtered scheme from the cone or `Delta`, and no unrestricted STCI consequence is claimed.


### Evidence scope and the remaining geometric bridge

The normal-Koszul edge filtration, generic count, punctual torsion family and recursive cancellation family were independently reconstructed in the inherited source state. The annihilator and full Rees-persistence arguments received separate reconstructions, including the exact entry ideal, all syzygies and the distinction between k[u]-flatness and O_C[u]-flatness. The supported quadruple's full initials were checked against its displayed free base-module basis; sampled Rees computations are supplemental rather than the arbitrary-parameter proof. Exact implementations remain in the [conormal-annihilator checker](../computations/verify_delta_conormal_annihilator_2026_10_24.m2), [Rees equation-module checker](../computations/verify_delta_rees_equation_module_2026_10_24.m2), [singular identity checker](../computations/verify_delta_singular_identities_2026_10_24.py), and [singular-family checker](../computations/verify_delta_singular_families_2026_10_24.m2).

There is no established general sheaf-level identification between the u-power filtration of the persistence module and each page of the incoming normal-Koszul differential filtration. The explicit family proves its own page/duration match. Over O_C[u] the persistence module need not split into compatible elementary blocks. Nor does local realization supply actual homogeneous equation source lines on P3. In particular the supported, generically defect-free punctual question remains open, as stated with the exact examples above.

### Characteristic reach

The exact equation-module comparison, normal-Koszul filtration, conormal-entry annihilator, extended-Rees quotient and Tor specialization sequences are integral local algebra constructions with the displayed noetherian/regular-sequence hypotheses; no characteristic-zero division or separability is used. The explicit families retain their individual restrictions: for example the punctual-family special-fiber length computation uses a unit of constant2 when m=2, so that assertion was stated in characteristic zero and requires a separate characteristic2 calculation. The scalar coefficient-vanishing and nilpotent lengths in examples may change on reduction. The intrinsic defect construction remains available in positive characteristic, and the prescribed characteristic2 quartic illustrates higher cancellation with zero comparison defect. It is compatible with [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier); no defect here is a universal STCI obstruction.


---

<a id="source-2026-10-26-filtration-local-proof-auditmd"></a>

## Local filtration audit and scope boundary — 2026-10-26

Status: mathematical review of local statements, not an independent executable replay, not a global sheafification certification, and not a new theorem. Sources: RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md and the October 23–24 investigation and independent review notes.

### 1. Exact comparison from ideals

Let R be a noetherian local ring, I an ideal, J subset I, S=gr_I(R), H=in_I(J), B=in_I(IJ), and S_+ its positive part. The inclusion S_+H subset B is immediate by multiplying representatives and taking leading terms, even when cancellations make B larger. The filtration F^n on D=J/IJ is the image of J intersect I^n. Its nth graded quotient is (J intersect I^n)/(J intersect I^(n+1) + IJ intersect I^n). The initial-symbol identification therefore gives gr_F^n D=H_n/B_n. Consequently

0 -> B_n/(S_+H)_n -> H_n/(S_+H)_n -> H_n/B_n -> 0

is exact. In particular the comparison map is a surjection from Q to gr_F D, not the reverse. This argument is local and requires no global splitting.

### 2. Generic generator excess

At the generic point of a smooth curve, suppose R is a regular transverse two-dimensional local ring and J is a two-generator parameter ideal. Then D=J/IJ is a two-dimensional vector space over the residue field. The induced finite filtration is exhaustive and separated; hence dim gr_F D=2. The initial ideal H is a finite-colength homogeneous ideal in a polynomial ring in two variables, and Q=H/S_+H has dimension mu(H). Summing the exact comparison gives dim Delta=mu(H)-2. This does not imply Delta vanishes whenever J is a complete intersection: the initial ideal can need extra generators.

### 3. Punctual torsion criterion

On a smooth curve, suppose the graded comparison is an isomorphism generically. Each Delta_n is torsion. Over a local DVR, Q_n -> G_n is surjective with equal generic rank. The induced map of torsion-free quotients is an isomorphism (the target is free and the source quotient has equal rank), so there is an exact torsion sequence 0 -> Delta_n -> tors(Q_n) -> tors(G_n) -> 0. Length Delta_n equals length tors(Q_n) minus length tors(G_n). Thus torsion in Q is necessary but not sufficient for a punctual defect. If Q is torsion-free, the defect vanishes.

### 4. Smooth-carrier support and its precise logical role

The independent October 23 review reconstructs the completed-local straightening of a smooth carrier and concludes Delta_p=0 wherever at least one carrier has nonzero first normal symbol. Therefore Supp Delta is contained in C intersect Sing(F) intersect Sing(G), under the regular ambient and two-generator CI hypotheses. Containment is not an existence assertion. The argument is local, and no global line-bundle twist is needed for this support inclusion.

### 5. What the examples do and do not show

The October 24 punctual family has Delta concentrated in one degree with arbitrary torsion length, but its actual complete intersection has residual support, so it does not address radical(J)=I. The supported quadruple J=(x^2,y^2+tx) has radical I and torsion in Q, but Delta=0. These are opposite controls, not a solution to the supported punctual-defect question.

### 6. Still unverified

The characteristic-two quartic claim ker(D -> I/I^2) is isomorphic to O(-24) and to Q_4 relies on global chart frames and transitions; it is supported by the prior independent audit, but has not been rechecked in this turn. The normal-Koszul spectral sequence requires its filtered-complex indexing, convergence and incoming-differential identifications to be retained exactly as in the source; no simplified global spectral-sequence theorem is proved here. The case radical(J)=I with generic Delta=0 and nonzero isolated Delta remains open.

### Decision

The local exact comparison, generic excess, torsion criterion and support containment have independently reviewed proofs and are suitable for a *separately scoped local-algebra* result after schema/path validation. Do not infer CR-13's global O(-24) assertion or a general supported-defect vanishing theorem from this note. This review does not perform a fresh executable replay.
