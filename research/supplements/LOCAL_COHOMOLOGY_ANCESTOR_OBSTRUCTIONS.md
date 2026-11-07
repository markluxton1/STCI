# Local-cohomology ancestor obstructions and an all-stage certificate

Fix the embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\) and
\[
S=k[x,y,z,w],\quad q=xw-yz,\quad A=x^2z-y^3,\quad
B=xz^2-y^2w,\quad C_3=yw^2-z^3,\quad I=I_{C_0}=(q,A,B,C_3).
\]
The module is \(M=H_I^2(S)\). With \(J=(q,B)\), the regular-sequence local-cohomology spectral sequence identifies \(M=\Gamma_I H_J^2(S)\) as a submodule of
\[
H_J^2(S)=\varinjlim_N S/(q^N,B^N),\qquad [P]\longmapsto[qBP].
\]
The specified first-socle targets are
\[
u=\frac{xz}{qB},\qquad v=\frac{yw}{qB},\qquad \deg u=\deg v=-3.
\]
They are annihilated by \(I\). Besides the evident \(q,B\) relations, this follows from
\[
Az=xB+y^2q,\quad Aw=xzq+yB,\quad
xC_3=ywq-zB,\quad yC_3=z^2q-wB.
\]
Their first-socle symbols on \(C\simeq\mathbf P^1\), up to a common frame, are \((s^2,t^2)\). On the \(s\ne0\) chart this is \((1,t^2)\); on the other chart it is \((s^2,1)\). The two targets are linearly independent over \(k\).

A common homogeneous ancestor means \(F\alpha=u,G\alpha=v\) for actual homogeneous polynomial multipliers of the same degree \(d\). Sections 1–2 work in algebraically closed characteristic zero. Section 3's coefficient certificate is integral over \(\mathbf Z[\lambda]\), hence works over every field and every specialization of \(\lambda\). These bounded results do not prove that \(M\) is non-quasi-cyclic and do not decide STCI.

## 1. Every surviving pair has degree at least four and rank-one first symbol

Suppose

\[
 F\alpha=u,\qquad G\alpha=v,\qquad F,G\in S_d
\]

for an arbitrary element \(\alpha\in M\); no finite direct-limit stage
is fixed.  Associativity gives \(Gu=Fv\).  On
\(C_0=[s^4:s^3t:st^3:t^4]\), the first-socle symbols of \(u,v\) are,
up to a common scalar, \((s^2,t^2)\).  Hence

\[
 s^2G|_{C_0}=t^2F|_{C_0}.
\]

Unique factorization gives either both restrictions zero or

\[
 F|_{C_0}=s^2h,\qquad G|_{C_0}=t^2h,\qquad \deg h=4d-2.
\]

If \(h\ne0\), choose any projective zero \(P\) of \(h\).  After completing
along the curve at \(P\), write

\[
 R=A_P[[\xi,\eta]],\qquad A_P\simeq k[[c]],\qquad
 E=H^2_{(\xi,\eta)}(R).
\]

Every element of \(E\) has finite negative \(\xi,\eta\)-support.  If
\(K=k((c))\) and \(e=[1/(\xi\eta)]\), then

\[
 E\hookrightarrow E\otimes_{A_P}K,\qquad E\cap Ke=A_Pe.
\]

Over \(K\), the nonzero curve restriction of the appropriate multiplier is a
unit, and the ancestor equation uniquely forces the coefficient of the socle
term to be a unit times \(h^{-1}\).  Since \(h\) vanishes at \(P\), this has
negative \(c\)-valuation and cannot lie in \(A_Pe\).  The same cancellation
handles the two endpoints.  Therefore

\[
 \boxed{F,G\in I_{C_0}.}
\]

This is the exact finite-Laurent obstruction; it is not the false assertion
that a normal parameter cannot divide a local-cohomology socle class.

Now suppose the first conormal symbols of \(F,G\) are generically independent.
With

\[
 \mathcal T_n=(0:_{\mathcal H_C^2(O_{\mathbf P^3})}I^n),
\]

the ancestor then lies in \(\mathcal T_2\) but not \(\mathcal T_1\), and its
second-principal-part symbol gives a nonzero section of

\[
 (\mathcal T_2/\mathcal T_1)\otimes O_C(-d-3)
 \simeq N_C\otimes\det N_C\otimes O_C(-d-3)
 \simeq O_{\mathbf P^1}(9-4d)^2.
\]

For \(d\ge3\) this space has no global sections.  Thus every possible pair in
those degrees has proportional first conormal symbols.

The remaining low degrees close exactly.  Constant multipliers cannot have the two linearly independent targets as images of one class. For degree one, the preceding membership conclusion forces both multipliers into \(I_1=0\), which is impossible. Since \(I_2=kq\), a quadratic pair
would give, after setting \(\beta=q\alpha\), constant multiples of one class
equal to the linearly independent pair \(u,v\).  For cubics, every element is
uniquely

\[
 F=qL+aA+bB+cC_3.
\]

On the chart \([1:t:t^3:t^4]\), with conormal basis \((q,A)\), put

\[
 Q_F=a+bt^3-ct^6,\qquad
 P_F=L|_C-bt^2+2ct^5.
\]

Write \(T=t^3\), \(Q_F=a+bT-cT^2\), and decompose
\[
P_F=(l_0+l_2T)+t(l_1+l_3T)-t^2Q_F'(T)
\]
when \(L|_C=l_0+l_1t+l_2t^3+l_3t^4\); use the analogous expressions for \(G\). The three residue classes modulo three in \(P_FQ_G-Q_FP_G=0\) give two cross-product equations for the first two coefficient rows and
\[
Q_F Q_G'-Q_F'Q_G=0.
\]
If both \(Q\)'s are nonzero, the last identity makes \(Q_G/Q_F\) constant in characteristic zero. The first two rows then force the same scalar ratio for every coefficient of \(F,G\). If one \(Q\) is zero and the other nonzero, the wedge forces the corresponding \(L|_C\) to vanish, so that linear form, and hence that multiplier, is zero; this cannot map an ancestor to its nonzero target. If both \(Q\)'s vanish, both cubics are divisible by \(q\). Therefore precisely the two nonzero possibilities are
\[
G=\lambda F,\qquad\text{or}\qquad F=qL,\ G=qM.
\]

The first would make \(v=\lambda u\); the second makes
\(L(q\alpha)=u\) and \(M(q\alpha)=v\), contradicting the degree-one case proved above.
Therefore no quadratic or cubic pair exists.

The sharp current conclusion is

\[
 \boxed{
 d\ge4,\qquad F,G\in I_d,\qquad
 \sigma(F)\wedge\sigma(G)=0
 }
\]

for any surviving common ancestor.  The last condition is only conormal
rank one; it does not imply scalar proportionality or a common ambient factor.
This is still not a proof that \(H_I^2(S)\) is non-quasi-cyclic.


## 2. Rank one does not force a common ambient factor

Section 1 leaves degree four as the first possible multiplier degree.  Its
17-dimensional first-symbol space, in the affine coefficient frame \(r[A]+k[q]\), admits the sparse description

\[
 r\in\langle1,t,t^3,t^4,t^6,t^7,t^9,t^{10}\rangle,
 \qquad \deg k\le9,\qquad k_9=-2r_{10},
\]

To see that this is the full image, write an arbitrary quartic through
\(C_0\) as \(F=qQ_2+A L_1+B M_1+C_3N_1\). Its first row is
\[
 r=L_1|_C+t^3M_1|_C-t^6N_1|_C,\qquad
 k=Q_2|_C-t^2M_1|_C+2t^5N_1|_C.
\]
Linear restrictions have powers \(0,1,3,4\), so the first expression spans
exactly the eight displayed powers of \(r\). Quadratic restrictions span
all powers zero through eight. The only ninth coefficient comes from
\(2t^5N_1|_C\), whereas \(r_{10}=-(N_1|_C)_4\), proving
\(k_9=-2r_{10}\). Thus the eight coefficients of \(r\) and the nine
lower coefficients of \(k\) are independent, giving dimension seventeen.
Write the other row as \((R,K)\). In the former coordinates

\[
 p=t^2r+t^3k,\qquad P=t^2R+t^3K,
\]

and the wedge equation is simply

\[
 pR-rP=t^3(kR-rK)=0.
\]

The tempting claim that every polynomially coprime solution has constant
symbol ratio is false.  For any \(\lambda\ne0\), put

\[
 F_\lambda=xA+\lambda y^2q,\qquad
 G_\lambda=yA+\lambda xzq.
\]

On the affine normal chart

\[
 x=1,\qquad y=t,\qquad z=t^3+a,\qquad w=t^4+ta+b,
\]

one has the exact identities \(A=a\), \(q=b\).  Thus the conormal rows are

\[
 (r,k)=(1,\lambda t^2),\qquad
 (R,K)=(t,\lambda t^3)=t(r,k).
\]

The ratio is nonconstant, and neither form is \(q\)-divisible.  They are
nevertheless ambient-coprime.  The exact identities

\[
 xzF_\lambda-y^2G_\lambda=A^2,\qquad
 -yF_\lambda+xG_\lambda=\lambda Aq
\]

force any common irreducible divisor to divide \(A\), then to divide
\(y^2q\); but \(\gcd(A,yq)=1\).  Therefore

\[
 \gcd(F_\lambda,G_\lambda)=1.
\]

The primitive direction \((1,\lambda t^2)\) is also outside the
seven-dimensional cubic first-symbol image when \(\lambda\ne0\), so this is
not a disguised pair \((xD,yD)\) with \(D\in I_3\). Indeed a cubic direction satisfies \(k=\lambda t^2r\) only if its coefficient of \(C_3\), then of \(B\), and finally of \(A\) vanish: compare respectively the powers \(t^8,t^5,t^2\), noting that a linear form restricted to \(C\) has no \(t^2\) term. This would make the cubic zero.  The fixed ratio-\(t\) slice already has dimension twelve before projectivizing: requiring both \(r\) and \(tr\) in the displayed eight-power span leaves \(r\in\langle1,t^3,t^6,t^9\rangle\). The conditions on \(k\) and \(tk\) give \(\deg k\le8\) and \(k_8=-2r_9\), leaving four plus eight independent coefficients.

This is a counterexample to a reduction strategy, not evidence that an
ancestor \(\alpha\) exists.  At this point a degree-four exclusion required
second normal symbols or the global direct-limit equations; the exact
stage-two saturation already showed that the first potentially populated
stage was \(N=3\).  Section 3 supplies a uniform coefficient
certificate at every stage and excludes this entire explicit family.

The exact script `computations/verify_localcoh_degree4_counterexample.py`
verifies curve membership, the two first-normal rows, the polynomial
identities, and generic coprimality over \(\mathbb Q(\lambda)\).  The written
identity/UFD argument proves coprimality for every nonzero specialization.
The script does not construct or assert a common ancestor.


## 3. An integral coefficient functional excludes the whole explicit family

Retain

\[
 S=k[x,y,z,w],\quad q=xw-yz,\quad A=x^2z-y^3,\quad B=xz^2-y^2w,
\]

and put

\[
 F=xA+\lambda y^2q,\qquad G=yA+\lambda xzq.
\]

The pair is genuinely compatible with the target classes.  An exact identity
is

\[
\begin{aligned}
 xzG-ywF={}&q\bigl(\lambda x^2z^2-\lambda wy^3-x^2yz+xy^3\bigr)\\
 &+B(x^2y-xy^2),
\end{aligned}
\]

so \(Gu=Fv\) in \(H^2_{(q,B)}(S)\).  Thus the associated Koszul class is a
cycle; the question is whether it is a boundary.

At stage \(R_N=S/(q^N,B^N)\), the classes
\(u=xz/(qB)\) and \(v=yw/(qB)\) are represented by

\[
 u_N=xz(qB)^{N-1},\qquad v_N=yw(qB)^{N-1}.
\]

A common ancestor can be replaced by its homogeneous component of degree
\(-7\).  The diagonal stages \((q^N,B^N)\) are cofinal in the usual two-index
Čech direct system, so after passage to a common diagonal stage \(N\) it
would be
represented by \(h\in S_{5N-7}\) and would give

\[
\begin{aligned}
 Fh-u_N&=q^Na+B^Nb,\\
 Gh-v_N&=q^Nc+B^Nd,
\end{aligned}
\]

with \(a,c\in S_{3N-3}\) and \(b,d\in S_{2N-3}\).  Stage \(N=1\) is
impossible because it would require a numerator of degree \(-2\), so take
\(N\ge2\).  For a polynomial \(P\), let \([i,j,k,l]P\) denote the coefficient
of \(x^iy^jz^kw^l\), and define

\[
\begin{aligned}
 \Phi_N(P)={}&-(N-1)\lambda[2N,0,2N-2,N-1]P\\
 &-\lambda[2N-1,1,2N-1,N-2]P\\
 &-[2N-1,0,2N-1,N-1]P,
\end{aligned}
\]

\[
 \Psi_N(P)=N[2N-1,0,2N-2,N]P
  +[2N-2,1,2N-1,N-1]P.
\]

Direct support checks give

\[
 \Phi_N(q^Na)=\Phi_N(B^Nb)=0,
 \qquad
 \Psi_N(q^Nc)=\Psi_N(B^Nd)=0.
\]

Expanding

\[
\begin{aligned}
 F&=x^3z-xy^3+\lambda xy^2w-\lambda y^3z,\\
 G&=x^2yz-y^4+\lambda x^2zw-\lambda xyz^2
\end{aligned}
\]

shows, for every \(h\in S_{5N-7}\), that

\[
 \boxed{\Phi_N(Fh)+\Psi_N(Gh)=0.}
\]

Only three coefficient positions of \(h\) can contribute; their total
coefficients are respectively
\(-\lambda(N-1)+\lambda N-\lambda=0\), \(-1+1=0\), and
\(-\lambda+\lambda=0\).  On the target pair, however,

\[
 \boxed{\Phi_N(u_N)+\Psi_N(v_N)=-1,}
\]

because the \(y\)-free leading term of \(u_N\) has coefficient one at
\((2N-1,0,2N-1,N-1)\), while the other requested target coefficients vanish.
Applying the two functionals to the proposed ancestor equations gives the
contradiction \(0=-1\).

The certificate is compatible with the direct-system transition
\([P]\mapsto[qBP]\): the four-term expansion of \(qB\) gives

\[
 \Phi_{N+1}(qBP)=\Phi_N(P),\qquad
 \Psi_{N+1}(qBP)=\Psi_N(P).
\]

In any event, an equality in the direct limit must become an equality at some
common finite stage, where the displayed contradiction applies; no injectivity
of a transition map is assumed.  The identities lie in \(\mathbf Z[\lambda]\)
and use no division, so the certificate is valid over every field and for
every \(\lambda\).  For Section 2's coprime, nonconstant-ratio family one retains
\(\lambda\ne0\).

Thus the entire explicit family of §2 is eliminated as a source of common
ancestors.  Other degree-four rank-one pairs and all higher-degree pairs remain
untreated.  This is not a non-quasi-cyclicity theorem.


The exact [all-stage coefficient checker](../computations/verify_localcoh_degree4_allstage_certificate.py) preserves the sparse support calculations; [the coprimality checker](../computations/verify_localcoh_degree4_counterexample.py) supports §2's polynomial identities. The written coefficient cancellations, transition identities and cofinality argument establish the all-stage quantifier, rather than extrapolation from finitely many successful stages. Broader ruling-ratio exclusions and fixed finite-stage reductions have their distinct proofs in [direction images and apolarity](LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md).


## Endpoint multiplier controls and the finite primary model

<a id="p-024"></a>


Let

\[
 S=k[x,y,z,w],\quad q=xw-yz,\quad
 A=x^2z-y^3,\quad B=xz^2-y^2w,\quad C=yw^2-z^3,
\]

\(I=(q,A,B,C)\), and \(J=(q,B)\).  The Hartshorne--Polini module is

\[
 M=H_I^2(S)=\Gamma_I H_J^2(S),\qquad
 H_J^2(S)=\varinjlim_n S/(q^n,B^n).
\]

Consider

\[
 u=\frac{xz}{qB},\qquad v=\frac{yw}{qB}.
\]

At a residual-line endpoint, the completed local model is
\(R=k[[c,q,r]]\), with \(e=1/(qr)\), and the two classes map, up to a common
sign, to

\[
 u\longmapsto c^2e,\qquad v\longmapsto e.
\]

The \(c\)-adic valuations then give all-stage contradictions to a common
ancestor with the natural \((A,C)\) multipliers.  Solving the degree-one
compatibility equations shows that the only linear multiplier pair is
proportional to \((y,z)\), and its required local ancestor would satisfy
\(c\alpha=e\), again impossible.  Constant multipliers are also impossible.

This is a genuine obstruction to these bounded multiplier classes, not a
proof that \(M\) is non-quasi-cyclic.  The all-stage proof in §1 supersedes the former
degree-two computational frontier by excluding every multiplier pair of
degree at most three at every direct-limit stage.  One correction remains important for reproducing the finite primary-correction model in its local(a,c,q) coordinates: its retained approximation is

\[
 (q^2,\ a(ac+2q),\ a^2q,\ a^3),
\]

not the overly simple monomial ideal \((q^2,a^2)\).

The formerly tempting compatible quadratic pair

\[
 f=x^2+z^2,\qquad g=y^2+w^2,
\]

does satisfy

\[
 g\,xz-f\,yw=q(zw-xy).
\]

On the normalization its restrictions are \((s^2h,t^2h)\), with
\(h=s^6+t^6\).  The all-stage proof turns any zero of \(h\) into a characteristic-zero
finite-Laurent contradiction, so the earlier inconsistent stage-three system
over \(\mathbf F_{32003}\) is now only a superseded corroborative experiment.

A failed modular correction experiment in a finite primary model is not a characteristic-zero all-stage proof. The exact direct-limit statements in §1 and §3 supply their own arguments; they do not rely on extrapolating such finite experiments.

## Consolidation review

Independent review reconstructed the preserved arguments, source coverage and
characteristic boundaries. The bounded proof clarifications in this account
were checked against the original arguments; no material preservation finding
remains. The claims retain their stated hypotheses.
