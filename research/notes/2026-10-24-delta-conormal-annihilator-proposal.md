# A scheme-theoretic annihilator for the filtration defect

Date: 2026-10-24. Status: **proved proposal, independently reconstructed by agent review; not a promoted canonical result**.

Scope: a regular codimension-two embedding \(C\hookrightarrow P\), locally with ideal \(I=(x,y)\), and any coherent ideal \(J\subset I\). For the intended application \(P\) is a smooth threefold, \(C\) is smooth, and \(J=(f,g)\) defines \(Z=X\cap Y\). Neither \(J\) being a complete intersection nor \(Z_{\mathrm{red}}=C\) is needed for the annihilator theorem. Additional components are allowed. The theorem concerns the marked embedding, without a classification of those components.

## 1. Claim and its intrinsic meaning

Use the merged [comparison framework](2026-10-23-ideal-filtrations-independent-investigation.md), with
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

## 2. Elementary proof

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

## 3. Koszul interpretation

In the normal Koszul complex \(K_{R/J}(x,y)\), formula (2) says the cycle represented by \((c,d)\) is an actual boundary. The carrier equation supplies the actual cycle \((a',b')\). Their wedge product is zero because the complex has no degree-three term. Its leading expression is exactly (3).

Under the inherited identification \(Q\simeq\operatorname{Tor}_1^S(S/H,B)\), (4) is the entrywise form of that product vanishing. This explains the special role of normal codimension two. The argument presented here does not assert an unchanged statement in higher codimension.

## 4. Sharpness of the scheme structure

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

## 5. Review, evidence, and next question

The proposing agent `annihilator_probe` derived both the spectral and elementary arguments. Its independent reviewer `annihilator_probe/annihilator_audit` reconstructed the actual Koszul-boundary proof and confirmed that the complete-intersection hypothesis on \(J\) is unnecessary. A separate root-level reviewer independently reconstructed the proof in the [annihilator review](2026-10-24-delta-annihilator-review.md). These are independent agent reviews, not human referee acceptance or canonical promotion.

The new script [exact annihilator samples](../computations/verify_delta_conormal_annihilator_2026_10_24.m2) checks (5), the full comparison denominator, exact annihilation, and sharpness for \(r=1,2,3\). It does not prove the arbitrary-parameter theorem, sheaf gluing, or global existence of projective pairs with prescribed local behavior.

No novelty claim is made for the determinant/Koszul argument or for the named quotient.

The useful next question is now sharper than a support-only question: how do the \(\mathcal O_C/\mathfrak a\)-module structure and normal-degree distribution of \(\Delta\) depend on the filtered extension data? In particular, fixing the conormal *scheme* bounds possible annihilators, but this result supplies no bound on normal degrees or number of generators of \(\Delta\). The retained source lines and maps remain necessary for questions involving the chosen carriers.
