# Endpoint residues and complementary contact orders

**Status:** exploratory elementary specialization of classical trace/residue theory; no new STCI exclusion. Companion to [research map](README.md). Work over algebraically closed characteristic-zero k. The normalized reduced components of a pure cycle Y missing L=V(z,w) have finite separable projection to P^1_[z:w]. Weight their traces and residues by generic cycle multiplicity. Assume the components meet the dense torus when using logarithmic quotient characters (the formulas with ordinary differentials need no such assumption).

**Scope clarification:** the governing task in [the research map](README.md#governing-research-question-user-clarification) is to calculate \(H_1=T=2S\) on the entire CI realization locus of translated cycles. Sole support is only an already calculated benchmark, not the investigation's starting assumption. No new obstruction is required.

## Classical inputs and averaging

[Tate, Residues of differentials on curves (1968)](https://www.numdam.org/articles/10.24033/asens.1162/): residue-trace compatibility and global residue theorem. [Stacks 50.19, Lemma 50.19.2](https://stacks.math.columbia.edu/tag/0FK6): trace on differentials of finite syntomic morphisms, applicable to finite maps of smooth curves. These classical inputs settle regularity of the differential trace and its residue compatibility. The following is a geometric specialization, not a proposed new residue theorem.

With lambda=w/z, xi=xy/(zw), eta=zy^2/(x^2w), put
\[
 \omega_T=\xi\,d\log\lambda,\quad
 \omega_U=\xi\,d\log\eta,\quad
 \omega_S=(x\,dy-y\,dx)/(zw).
\]
Already as rational differentials upstairs,
\[
 2\omega_S=\omega_T+\omega_U.
\]
Indeed the logarithms combine to 2(dlog y-dlog x). Trace gives S=(T+U)/2. The twisted regular form x dy-y dx has trace in H^0(P^1,omega(2)), so Tr(omega_S)=S dlog lambda with S constant. Tr(xy) is a section of O(2), so T can have simple poles at 0 and infinity. Only their constant Laurent coefficient is measured by res Tr(omega_T) at zero. The corresponding U poles cancel in the average.

## Endpoint contact formulas

Residue-trace compatibility gives
\[
 S=\sum_{P\mid0}n_P\operatorname{res}_P\omega_S
   =-\sum_{P\mid\infty}n_P\operatorname{res}_P\omega_S.
\]
On a normalized branch over zero choose a parameter r with lambda=r^e (e the ramification index). Write a=x/z=sum a_i r^i, b=y/z=sum b_j r^j. Then the unweighted branch contributions are
\[
 S_P=\operatorname{res}_P (a\,db-b\,da)/r^e
     =\sum_{i+j=e}(j-i)a_i b_j,\qquad
 T_P=\operatorname{res}_P ab\,d\lambda/\lambda^2
     =e\sum_{i+j=e}a_i b_j.
\]
The actual S and constant Laurent coefficient of T are the sums weighted by n_P. The formulas follow by coefficient extraction; no CI hypothesis. At infinity use mu=z/w and x/w,y/w; the ordinary differential omega_S has opposite total residue, by the global residue theorem (or the traced differential). The finite jets through order e suffice. If both coordinate functions vanish at the point, only orders 1 through e-1 matter. On their truncated coefficient space the skew pairing has weights e-2i on complementary monomials r^i,r^(e-i); when e is even the middle order e/2 is invisible to S but not T. This describes a local contact imbalance, not nondegeneracy of the curve or the CI.

On C_(u,v) the zero endpoint has lambda=v h^4, x/z=h, y/z=u h^3. Take r=v^(1/4)h. Then S_P=2u/v, T_P=4u/v. At infinity the exponents reverse; omega_S residue is -2u/v. For all translated cycles S=2M_1, T=4M_1. Thus the factor 1/2 is the normalized contact imbalance (3-1)/4. Ordinary residue reciprocity between the two endpoints is automatic for arbitrary cycles and cannot force M_1=0; even a single reduced quartic has nonzero S.

## Actual CI compatibility and remaining gap

For a proper homogeneous CI missing L, the established first-jet bridge identifies
\[
 \operatorname{Res}_{f,g}(ps-qr)
 =\sum_{P\mid0}n_P\sum_{i+j=e_P}(j-i)a_i b_j.
\]
On any CI-realized translated arrangement this is 2M_1, and the question is what values the CI realization permits. Sole support is only the separate benchmark 2m. This is a relation between first normal equation jets on a disjoint projective line and finite normalized curve jets over an endpoint. The right side forgets all nilpotent and embedded lifting information except generic cycle multiplicities. A comparison of the two endpoints by itself does not constrain it further. The next useful calculation is to evaluate the left side on arbitrary actual CI realizations of translated arrangements, using all available source identities.

Control verification: the quadratic elimination in README gives the undivided resultant -lambda*T^12-lambda*T^11-7lambda*T^10-10lambda*T^9-21lambda*T^8-29lambda*T^7-35lambda*T^6-34lambda*T^5+(lambda^2-27lambda+1)*T^4-17lambda*T^3-8lambda*T^2-3lambda*T-lambda. Direct symbolic check: at lambda=2 it is squarefree; its value at T=1 is lambda^2-194lambda+1. This checks the trace 3 and the residual trace -1 used in the control.

Reassessment: classical identities and local contact formulas now explain the averaging and its special coefficient. No additional cycle-level condition on translated arrangements was found. Keep this as geometric understanding, pending independent review; next calculate the range of the residue on the full CI realization locus. Do not assume that range is zero or specialize to the small diagonal.
